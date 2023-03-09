## How to Customize a GitHub Build

These are bare-bones instructions for applying customizations.

You do not need very many "git" commands (and I'll tell you which ones).

You do not need a Mac, you can still do this on any computer.

## Editing Code

You need some kind of editor that handles multiple folders and files as a consolidated project.

* I recommend Visual Studio Code, which is provided, free, by the same folks that provide GitHub
* If you have a Mac with Xcode - you can continue to use Xcode as your editor
    * Xcode works as your editor even if not up-to-date enough to build
    * Some modules, like G7SensorKit might refuse to open in older Xcode, but no customizations are expected for that module

!!! tip "Install VS Code"
    You can use any editor you want, this is the one I use.

    [Install Visual Studio Code](https://code.visualstudio.com/download)

## Decide Which Modules You Want to Modify

If you have a [Code Customization](../build/code_customization.md) in mind, you will see that each item lists a folder name. You only need the Module name (first name before the first / character).

Here are the most common modules:

| Folder | Module | Fork From |
| --- | --- | --- |
| Loop/LoopCore | Loop | LoopKit/Loop |
| LoopKit/LoopKitUI/Extensions | LoopKit | LoopKit/LoopKit |
| OmniBLE/OmniBLE/PumpManagerUI | OmniBLE | LoopKit/OmniBLE |
| rileylink_ios/OmniKit/OmnipodCommon | rileylink_ios | ps_2/rileylink_ios |

## Create a Fork for Selected Module(s)

If you want a modification that uses a particular module, you must fork that module in your GitHub account. Simply add the characters `https://github.com/` in front of the Fork From name to generate the URL you need. Enter that into your browser to go to the repository you need to fork.

When you fork a repository, the default branch is the one that is forked. That is ok. Only include that default branch when forking. If you need a different branch, you will add that as a second step.

| Repository | Default Branch |
| --- | --- |
| LoopKit/LoopWorkspace | main |
| LoopKit/Loop | dev |
| LoopKit/LoopKit | dev |
| LoopKit/OmniBLE | dev |
| ps_2/rileylink_ios | dev |

The LoopWorkspace main branch is always the released code.

The instructions on this page are for the main branch. This page has instructions for applying customizations to released code.

### LoopWorkspace

The LoopWorkspace repository is the umbrella organization holding all the pieces needed to build the Loop app. Part of what LoopWorkspace provides is a list of pointers to a specific commit for each modules in the workspace.

* A commit is a specific version of code for a repository
* A workspace is a grouping of several repositories (modules) into a complete package
* The workspace includes a list of the specific commit for each repository (module)

This process separates changes in a given module from what the workspace builds.

* A commit to a module can be made without affecting the workspace
* To update the workspace to use the new commit for a module, the list containing the specific commit for that repository (module) must also be updated
    * This update is itself a commit to the workspace repository

This allows a given module, say Loop, to be updated with a new commit; but that commit doesn't affect the Loop app that you build using LoopWorkspace.

### What are branches again?

Branches indicate different version of code - this tutorial is pretty nice.

!!! tip "Git Tutorial"
    When I first started using git, my adult son answered a my questions very politely then started sending me links to this tutorial instead.

    [Learn Git Branching](https://learngitbranching.js.org/)

    There's a section called `Main` which goes over commands in your local copy (clone) of the code. There's a section called `Remote` that goes over fetching, pulling and pushing to remote copies.

    For Open Source Software, you might fetch and pull from the master copy, but you will only push to your copy of the fork.

But all you need to know about branches is that the history required for the main branch (released code) is also present in the dev branch for the submodules.

