# Loop Docs

This is the repo that contains the source files for the [Loop Docs](https://loopkit.github.io/loopdocs) site.

## Contributing

To suggest changes, fork this repository, edit the files, and submit your changes as a pull request.

To preview your work as you edit you'll want to set up two python packages with `pip install <package>`:
* [mkdocs](http://www.mkdocs.org/), and
* mkdocs-bootswatch

At that point you can run `mkdocs serve` in the project directory to view your changes.

## Conventions

* Use images for clarity whenever appropriate

### Admonitions
[Admonitions](https://pythonhosted.org/Markdown/extensions/admonition.html) are a markdown extension that enable formatted blocks for visually calling out information. The types are: note, info, warning, and danger. Here are some examples of how to write the markdown:

```markdown
!!! note
    This admonition uses the default title: 'Note'.

!!! info "My Custom Title"
    This admonition is blue and has a custom title.

!!! warning ""
    This admonition is yellow and has no title.
```
