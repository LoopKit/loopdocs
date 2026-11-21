"""Keep the name "Loop" from being machine-translated.

Google Translate turns "Loop" into words such as "boucle" (French).
It skips any text marked translate="no", so this hook wraps the names
in NAMES with <span translate="no"> on every built page, including the
navigation, page titles and table of contents. Writers can type "Loop"
without italics or spans.

Google Translate drops the spaces and punctuation that touch a
translate="no" element ("the Loop app." becomes "l'applicationLoop").
So the span takes in the space on each side and any possessive or
punctuation right after the name: "the<span translate="no"> Loop. </span>Next". Browsers
show the same text, since a space next to another space or at the start
of a line is not displayed.

Left alone:
- lowercase "loop" ("closed loop", "red loop" are ordinary words)
- "Open Loop" and "Closed Loop", mode names that translate correctly
  as a phrase
- longer names such as LoopKit, LoopDocs or Loop-to-Pump
- text in code, scripts and anything already marked translate="no"

The page is not reformatted: the only change is the inserted spans.
"""

import re
from html.parser import HTMLParser

# Names to protect, longest first. Matched as whole words, capitalized.
NAMES = ("Loop and Learn", "Loopers", "Looper", "Loop")

# A name right after one of these words is part of a phrase that should
# be translated as a whole.
PHRASE_WORDS = {"open", "closed"}

NAME_RE = re.compile(
    r"(?<![\w-])(" + "|".join(re.escape(n).replace(r"\ ", r"\s+") for n in NAMES) + r")(?![\w-])"
)
WORD_BEFORE_RE = re.compile(r"(\w+)[\s-]*$")
# Kept inside the span after a name: a possessive, then punctuation.
PUNCT_RE = re.compile(r"(?:['\u2019]s(?!\w))?[.,;:!?)\]]*")

SKIP_TAGS = {"head", "code", "pre", "kbd", "samp", "script", "style", "textarea", "svg", "math"}
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


def _wrap_text(text, space_before, space_after):
    """Wrap the names in text.

    space_before / space_after say whether the visible text just outside
    this text node (past any tags) is whitespace.
    """
    out = []
    last = 0
    for m in NAME_RE.finditer(text):
        before = WORD_BEFORE_RE.search(text[: m.start()])
        if before and before.group(1).lower() in PHRASE_WORDS:
            continue
        start = m.start()
        name_end = end = PUNCT_RE.match(text, m.end()).end()

        # Space before: move it inside the span, or add one when the space
        # is outside this text node.
        if start > last and text[start - 1].isspace():
            start -= 1
            lead = " "
        elif start == 0 and space_before:
            lead = " "
        else:
            lead = ""

        # Space after: the same.
        if end < len(text) and text[end].isspace():
            tail = " "
            end += 1
        elif end == len(text) and space_after:
            tail = " "
        else:
            tail = ""

        name = re.sub(r"\s+", " ", text[m.start() : name_end])
        out.append(text[last:start])
        out.append('<span translate="no">' + lead + name + tail + "</span>")
        last = end
    if not out:
        return text
    out.append(text[last:])
    return "".join(out)


def _visible_char_before(html, i):
    """The character before html[i], skipping over tags."""
    i -= 1
    while i >= 0:
        if html[i] == ">":
            i = html.rfind("<", 0, i) - 1
            continue
        return html[i]
    return ""


def _visible_char_after(html, i):
    """The character at html[i] or later, skipping over tags."""
    while i < len(html):
        if html[i] == "<":
            j = html.find(">", i)
            if j < 0:
                return ""
            i = j + 1
            continue
        return html[i]
    return ""


class _Scanner(HTMLParser):
    """Find text outside skipped elements and record where to insert spans."""

    def __init__(self, html):
        super().__init__(convert_charrefs=False)  # keep offsets matching the source
        self.html = html
        self.line_starts = [0] + [m.end() for m in re.finditer("\n", html)]
        self.stack = []  # (tag, skip)
        self.edits = []  # (start, end, replacement)

    def _offset(self):
        line, col = self.getpos()
        return self.line_starts[line - 1] + col

    def handle_starttag(self, tag, attrs):
        if tag in VOID_TAGS:
            return
        a = dict(attrs)
        skip = (
            tag in SKIP_TAGS
            or a.get("translate") == "no"
            or "notranslate" in (a.get("class") or "").split()
        )
        self.stack.append((tag, skip))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        if "Loop" not in data or any(skip for _, skip in self.stack):
            return
        start = self._offset()
        if self.html[start : start + len(data)] != data:
            return  # position not certain; leave this text alone
        new = _wrap_text(
            data,
            _visible_char_before(self.html, start).isspace(),
            _visible_char_after(self.html, start + len(data)).isspace(),
        )
        if new != data:
            self.edits.append((start, start + len(data), new))


def on_post_page(output, page, config):
    if "Loop" not in output:
        return output
    scanner = _Scanner(output)
    scanner.feed(output)
    scanner.close()
    for start, end, new in reversed(scanner.edits):
        output = output[:start] + new + output[end:]
    return output
