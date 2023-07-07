# Loop Docs

## Presentation
📚You can view the published version of [Loop Docs here](https://loopkit.github.io/loopdocs). 

This repository contains the source files for [Loop's](https://github.com/LoopKit/Loop) documentation.

*LoopDocs* focuses on documenting the latest release and the `dev` branch:
- [What is Loop?](https://loopkit.github.io/loopdocs/#what-is-loop)
    > The *Loop* iOS app is a Do-It-Yourself closed-loop algorithm.  
    > It works together with your CGM, Pump, (and Radio-link device) to manage your insulin delivery by predicting Blood Glucose outcomes.
- [Overview](https://loopkit.github.io/loopdocs/intro/overview-intro/)
- [**Requirements**](https://loopkit.github.io/loopdocs/intro/requirements/)
- [Build Loop](https://loopkit.github.io/loopdocs/intro/requirements/#two-loop-build-methods)
- [Configuration](https://loopkit.github.io/loopdocs/loop-3/loop-3-overview/)
- [Usage](https://loopkit.github.io/loopdocs/operation/loop/open-loop/)
- [Troubleshooting](https://loopkit.github.io/loopdocs/troubleshooting/overview/)
- Remote monitoring and commands with [*Nightscout*](https://loopkit.github.io/loopdocs/nightscout/overview/)
- [FAQs](https://loopkit.github.io/loopdocs/nightscout/overview/)


## Contributing

The easy way:

* To suggest changes, please review [Issues](https://github.com/LoopKit/loopdocs/issues).  Add your comment if an Issue is already open, otherwise, add a new Issue.
* If it is a simple typo or wording change, follow the instructions in this video to submit a *pull request* the easy way.
  * [How to submit a LoopDocs Pull Request?](https://youtu.be/6qSppvgGxpg)

If it is a more substantive change and you want to "[install](#install)" that is make a fork and provide pull requests, please keep reading.

## Install

- [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this project
- Install *Python*  3
  Review [Properly Installing Python](http://docs.python-guide.org/en/latest/starting/installation/) for help getting *Python* installed.
- Install Python Virtual Environment.  
  In this example, I use [`venv`](https://realpython.com/python-virtual-environments-a-primer/#how-can-you-work-with-a-python-virtual-environment), but use whichever you prefer.  
  ```shell
  cd loopdocs # cd into the folder where you cloned this repository
  
  # Creates a virtual environment using Python 3 in the venv folder  
  python3 -m venv venv 

  # Activate the virtual environment
  # Run the next line **each time** you start a new shell window/tab
  source venv/bin/activate
  ```
- Install the project's required *Python* packages
  ```shell
  cd loopdocs # Make sure you are in the folder where you cloned this repository

  python -m pip install -r requirements.txt  
  ```
## Run
Once [installed](#install), you can preview the doc locally as you edit.
### Preview Changes
To preview your work as you edit:

- Run **`mkdocs serve`** locally and keep it running:
  ```shell
  cd loopdocs # the folder where you cloned this repository
  mkdocs serve
  ```
    By default, this runs a local web server that hosts the documentation at http://127.0.0.1:8000/ .
* Preview docs in your Web browser. Most changes will update automatically as you edit. Configuration and navigation changes will require restarting the *mkdocs* server.
* Optionally, you can share the preview with others by uploading them to your repository's `gh-pages` branch
  ```bash
  mkdocs gh-deploy
  ```

Note that the `master` branch will automatically be published to your personal repository `gh-pages` by *Github actions* when it is pushed to the *GitHub* server.

## Conventions

### Links

Links should be written like this:

```markdown
In the same directory: Click here for [Update FAQs](update-faqs.md)

In a directory below the current page: Click here for [Update FAQs](faqs/update-faqs.md)

In a directory "outside" the current directory: Click here for [Update FAQs](../faqs/update-faqs.md)

Like above, but linking directly to a heading/anchor in update-faqs.md:

Click here for [When Should You Update?](../faqs/update-faqs.md#when-should-you-update)

```

ℹ️ **Notice about mkdocs**

> Using absolute paths with links is not officially supported.  
> Relative paths are adjusted by MkDocs to ensure they are always relative to the page.
> Absolute paths are not modified at all.  
> This means that your links using absolute paths might work fine in your local environment but they might break once you deploy them to your production server.


```markdown
⛔️ Do NOT use a link that starts with a '/': Click here for [Update FAQs](/faqs/update-faqs.md)
```

### Images

The conventions for linking to images are the same as linking to pages as described above.

New images should be placed in the `img` directory just below the Markdown file.

An example of a correct link to an image is `[alt-text](relative_path_to/image_name)`.

```markdown
![iPhone](img/phones.png)
```

With images, it is possible to add extra attributes like `width` and `center`.

#### Image Width

```markdown
![iPhone](img/phones.png){width="300"}
```

This will get rendered to this: 
```html
<img alt="iPhone" src="img/phones.png" width="300">
```

#### Center an Image

You can also center an image, by adding `{align="center"}` **on a new line**
just **below** the paragraph you want to center:

```markdown
![Eros](img/eros.png){width="750"}
{align="center"}
```

This will get rendered to this:

```html
<p align="center">
    <img alt="Eros" src="../img/eros.png" width="750" />
</p>
```

#### Images in Tables

Use HTML on the first line that indicates the table.  
For example, in [displays_v3.md](https://loopkit.github.io/loopdocs/loop-3/displays_v3/#loop-cycle) there are many icons with descriptions to the right.
This format provides appropriate views on both desktop and mobile.

For **no header row**, replace `|||` with:

```markdown
| <div style="width:72px"></div> |                        |
|---                             |---                     |
| ![icon alt-text](img/icon)     | image description here |
```

To **add a header row**, use:
```markdown
| <div style="width:72px">Column 1 Header</div> | Column 2 Header |
```

### Admonitions and CSS

Now using the standard set of [admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/) and CSS styles that come with the Material theme.

The admonitions in use are:
First 3 boxes for Build Pages:
* `info`
* `abstract`
* `question`

To get a warning triangle, use `warning`.  
To get a red zag icon, use `danger`.  
To get a pencil icon, use `note`.  

[Admonition](https://python-markdown.github.io/extensions/admonition/) is a markdown extension that enables formatted blocks for visually calling out information.

The Markdown syntax used by *LoopDocs* is:

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

The copy-to-clipboard button is built into the Material theme for every code block and displayed on the right side.  
When clicked it copies the content of the block into the clipboard.  
However we chose to disable it by default for all code blocks and enable it on a case by case basis.  
Here is how to enable the copy-to-clipboard button for a "code" block containing regular text.

````
``` { .txt .copy title="title of this code block" }
Content of the code block here
```
````

where:
- `.txt` denotes the language used in the content of the code block.  
  For instance, use `.txt` for regular text, `.sh` for a regular shell script, or `.bash` for a Bash script.  
  This is a **required** parameter.  
  Here is the list of [supported languages](https://pygments.org/languages/) (use one of the `Short Name`s).
- `.copy` shows the copy-to-clipboard button when present (hidden otherwise)
- `title=“title of this code block”` adds a title to the code (none when absent)

Do note that:
- There is a space before **and** after the opening curly brace ` { `.
- There is space before the closing curly brace `}`.


[Source](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/?h=copy+clipboard#code-copy-button)
