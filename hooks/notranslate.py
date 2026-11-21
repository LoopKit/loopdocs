"""Keep the name "Loop" from being machine-translated.

Google Translate turns "Loop" into words such as "boucle" (French).
It skips any text marked translate="no", so this hook wraps the names
in NAMES with <span translate="no"> on every built page, including the
navigation, page titles and table of contents. Writers can type "Loop"
without italics or spans.

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

# Names to protect. Matched as whole words, capitalized.
NAMES = ("Loopers", "Looper", "Loop")

# A name right after one of these words is part of a phrase that should
# be translated as a whole.
PHRASE_WORDS = {"open", "closed"}

NAME_RE = re.compile(r"(?<![\w-])(" + "|".join(NAMES) + r")(?![\w-])")
WORD_BEFORE_RE = re.compile(r"(\w+)[\s-]*$")

SKIP_TAGS = {"head", "code", "pre", "kbd", "samp", "script", "style", "textarea", "svg", "math"}
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


def _wrap_text(text):
    out = []
    last = 0
    for m in NAME_RE.finditer(text):
        before = WORD_BEFORE_RE.search(text[: m.start()])
        if before and before.group(1).lower() in PHRASE_WORDS:
            continue
        out.append(text[last : m.start()])
        out.append('<span translate="no">' + m.group(1) + "</span>")
        last = m.end()
    if not out:
        return text
    out.append(text[last:])
    return "".join(out)


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
        new = _wrap_text(data)
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
