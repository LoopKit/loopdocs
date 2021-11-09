# Loop Docs

This is the repo that contains the source files for the [Loop Docs](https://loopkit.github.io/loopdocs) site.

## Contributing

The easy way:
* To suggest changes, please review Issues.  Add your comment if an Issue is already open, otherwise, add a new Issue.
* If it is a simple typo or wording change, follow the instructions in this video to submit a pull request the easy way.
  * [LoopDocs Pull Requests](https://youtu.be/6qSppvgGxpg)

If it is a more substantive change and you want to make a fork and provide pull requests, please keep reading.

### Previewing Changes

To preview your work as you edit you must set up two python packages that are used to create this site using [MkDocs](http://www.mkdocs.org/). They are `mkdocs`, and `mkdocs-bootswatch`.

Review [Properly Installing Python](http://docs.python-guide.org/en/latest/starting/installation/) for help getting Python installed. MkDocs works with Python 2.7, 3.3-3.6, and pypy.

* Install python modules

```bash
$ cd <loopdocs project location>
$ pip install -r requirements.txt
```

* Run mkdocs server locally

```bash
$ cd <loopdocs project location>
$ mkdocs serve
```

* Preview docs in browser. Most changes will update automatically as you edit. Configuration and navigation changes will require restarting the mkdocs server.
* Optionally, you can share the preview with others by uploading them to your repository's `gh-pages` branch

```bash
$ mkdocs gh-deploy
```

Note that these two branch names: `working-docs` and `master` will automatically be published to your personal repository `gh-pages` by github actions when they are pushed to the github server.

## Conventions

### Links

Links should be written like this:

```markdown
In the same directory: [Click here for Step 14](step14.md)

In a directory below the current page: [Click here for Step 14](build/step14.md)

In a directory "outside" the current directory: [Click here for Step 14](../build/step14.md)

Like above, but linking directly to a heading/anchor in step14.md:

[Click here for Step 14](../build/step14.md#sign-four-targets)

```

Notice about mkdocs: "Using absolute paths with links is not officially supported. Relative paths are adjusted by MkDocs to ensure they are always relative to the page. Absolute paths are not modified at all. This means that your links using absolute paths might work fine in your local environment but they might break once you deploy them to your production server."

```markdown
Do NOT use a link starts that with a '/': [Click here for Step 14](/build/step14.md)
```

### Images

The conventions for linking to images is the same as linking to pages as described above.

New images should be placed in the "img" directory just below the md-file.

Example of correct link to image is [alt-text](relative path/image-name).

```markdown
![iPhone](img/phones.png)
```

With images it is possible to add extra attributes like 'width' and 'center'.

```markdown
![iPhone](img/phones.png){width="300"}

This will get rendered to this: <img alt="iPhone" src="img/phones.png" width="300">

You can also center a image, by adding '{align="center"}' on a new line
just below the paragraph you want to center:

![Eros](img/eros.png){width="750"}
{align="center"}

This will get rendered to this:
<p align="center">
    <img alt="Eros" src="../img/eros.png" width="750" />
</p>
```

A note about images in tables. Use html on the first line that indicates the table.
For example, in displays.md there are many icons with descriptions to the right. This format provides appropriate views on both desktop and mobile.

For no header row, replace `|||` with:

```markdown
| <div style="width:72px"></div> ||
|---|---|
|![icon alt-text ](img/icon)|text with description|
```

To add header row, use:
```markdown
| <div style="width:72px">Column 1</div> | Column 2 |
```

### Admonitions and CSS

Now using the standard set of [admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/) and css styles that come with the Material theme.

The admonitions in use are:
First 3 boxes for Build Steps:
* `info`
* `abstract`
* `question`

To get a warning triagle, use `warning`

To get a red zag icon, use `danger`

To get a pencil icon, use `note`

[Admonitions](https://python-markdown.github.io/extensions/admonition/) are a markdown extension that enable formatted blocks for visually calling out information.

The markdown syntax used by loopdocs is:

```markdown
!!! keyword ""
    If a blank title is provided, no title is applied.
    Every indented line is included in the "box" created by this admonition

!!! keyword "Title String"
    If an explicit title string is provided, that is used as the title.
    The displayed title string matches the capitalization provided.

    Every indented line is included in the "box" created by this admonition
```


## Copy Button

The copy button is built into the Material theme for every code block.
