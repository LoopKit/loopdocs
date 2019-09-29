# Loop Docs

[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

This is the repo that contains the source files for the
[Loop Docs](https://loopkit.github.io/loopdocs) site.

## Contributing

To suggest changes, fork this repository, edit the files, and submit your
changes as a pull request.

### Previewing Changes

To preview your work as you edit you must set up two python packages that are
used to create this site using [MkDocs](http://www.mkdocs.org/). They are
`mkdocs`, and `mkdocs-bootswatch`.

Review
[Properly Installing Python](http://docs.python-guide.org/en/latest/starting/installation/)
for help getting Python installed. MkDocs works with Python 2.7, 3.3+, and pypy.

- Install python modules

```bash
$ cd <loopdocs project location>
$ pip install -r requirements.txt
```

**mkdocs Version Warning:** Use the latest `0.16.x` patch version of `mkdocs`,
but don't upgrade `mkdocs` to version `0.17.x`. It is NOT compatible with the
theme being used. Same for updated versions of `mkdocs-bootswatch`, do not use
the latest version.

- Or, install modules individually

```bash
$ pip install mkdocs<0.17
$ pip install mkdocs-bootswatch==0.4.0
```

- Run mkdocs server locally

```bash
$ cd <loopdocs project location>
$ mkdocs serve
```

- Preview docs in browser. Most changes will update automatically as you edit.
  Configuration and navigation changes will require restarting the mkdocs
  server.
- Optionally, you can share the preview with others by uploading them to your
  repository's `gh-pages` branch

```bash
$ mkdocs gh-deploy
```

#### Autoformatting Changes

Before committing, set up the project's auto-formatter. This will prettify your
code upon commit! If you `pip install -r requirements.txt` above, you will have
pre-commit installed in your environment. To configure it in the repo,

- Set up pre-commit

```bash
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

If you want to format your code before commit, you will need to install
prettier:

```bash
npm install --save-dev --save-exact prettier
# or globally
npm install --global prettier
```

then you can run:

```bash
$ prettier --write --prose-wrap=always "**/*.md" "*.md"
```

## Conventions

- Use images for clarity whenever appropriate

### Admonitions

[Admonitions](https://pythonhosted.org/Markdown/extensions/admonition.html) are
a markdown extension that enable formatted blocks for visually calling out
information. The types are: note, info, warning, and danger. Here are some
examples of how to write the markdown:

```markdown
!!! note This admonition uses the default title: 'Note'.

!!! info "My Custom Title" This admonition is blue and has a custom title.

!!! warning "" This admonition is yellow and has no title.
```
