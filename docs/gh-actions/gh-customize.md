## Overview

!!! info "Time Estimate"
    * About half an hour to an hour per Module
        * Typically 1 or 2 Modules
    * Ten minutes to configure your LoopWorkspace branch
    * One minute to start the build
    * An hour before the TestFlight build shows up on your phone

!!! abstract "Summary"
    * LoopDocs: Decide on Modules to modify [Code Customization](../build/code_customization.md)
    * GitHub (each Module):
        1. Fork Module (GitHub)
        1. Modify Module (GitHub->Codespaces)
        1. Save your new branch (Codespaces->GitHub)
        1. Prepare command line and save
    * All Module command lines prepared
    * GitHub (build Loop)
        1. Modify LoopWorkspace (GitHub->Codespaces)
        1. Save your new branch (Codespaces->GitHub)
        1. Action: Build Loop
    * Phone: Install Loop with TestFlight

!!! question "FAQs"
    - **Do I need a Mac computer?** No. This can be done on any browser, although it will be easier using a computer.
    - **Should I build without customizations first?** Yes. Make sure the build process works without customizations. You don't need to install the build on your phone, just make sure it builds without errors before you start modifying.

## How to Customize a GitHub Build

You do not need a Mac, you can still do this using any browser on a computer.

There is some background information at the bottom of this page starting at [LoopWorkspace](#loopworkspace) if you want to know what you are doing. Otherwise, just follow the steps like a cookbook.

## Editing Code

You will be using the online tool associated with GitHub called Codespaces. Any repository in your GitHub account can be opened with Codespaces.

You will need a text editor to format a command line for each module you change. Use the same text editor you use for saving your Secrets. You do not want characters like double hypen or quote symbols modified by a smart editor.

## Decide Which Modules You Want to Modify

Decide which [Code Customization](../build/code_customization.md) you want to make. Each customization lists a Module name. You will want a fork for each Module you wish to modify.

This table lists all the modules referred to on the Code Customization page linked above:

| Folder | Module | Fork From |
| --- | --- | --- |
| Loop/LoopCore | Loop | [https://github.com/LoopKit/Loop](https://github.com/LoopKit/Loop) |
| LoopKit/LoopKitUI/Extensions | LoopKit | [https://github.com/LoopKit/LoopKit](https://github.com/LoopKit/LoopKit) |
| OmniBLE/OmniBLE/PumpManagerUI | OmniBLE | [https://github.com/LoopKit/OmniBLE](https://github.com/LoopKit/OmniBLE) |
| rileylink_ios/OmniKit/OmnipodCommon | rileylink_ios | [https://github.com/ps2/rileylink_ios](https://github.com/ps2/rileylink_ios) |

!!! tip "Pro Tip"
    Open 4 browser tabs or windows so you can click to switch locations.

    * This page
    * [LoopDocs: Code Customization](../build/code_customization.md) 
    * Your GitHub account
    * A new one that you'll use to open Codespaces

## Create a Fork for Selected Module

If you want a modification that uses a particular module, you must fork that module to your GitHub account. You will repeat the Fork and Modify steps for each module.

1. Log into your GitHub account
1. Right click (or control click) on the URL in the table above
1. This opens a new browser tab at the URL of the repository you need to fork
1. Tap on Fork, your fork will show up in the tab

Remember - you can only have a single fork of a given repository. If you already have a fork, you don't need another one; but it must be a fork from the URL listed above.

!!! question "I already have a fork"
    Go to [Existing Fork for Module](#existing-fork-for-module) and follow the directions there.

When you fork a repository, the default branch is the one that is forked. That is ok. Only include that default branch when forking.

| Repository | Default Branch |
| --- | --- |
| LoopKit/LoopWorkspace | main |
| LoopKit/Loop | dev |
| LoopKit/LoopKit | dev |
| LoopKit/OmniBLE | dev |
| ps2/rileylink_ios | dev |

The LoopWorkspace main branch is always the most recent released code.

This page has instructions for applying customizations to released code, main branch of LoopWorkspace. Don't worry about the other repositories using dev as the default branch. Everything you need to update LoopWorkspace main is included in the dev branches of the lower level repositories (Modules).

!!! warning "Loop with LnL Patches"
    Some Loop users build with the loopnlearn version of LoopWorkspace using the main_lnl_patches branch. If you are one of those users, do not use the URL table above. There is also an extra step required to prepare your fork. The LnL instruction page is not yet available; but will be found on the LnL website (later).

    If you want to deal with both released Loop (fork from LoopKit) and LnL with Patches, it is suggested you set up a second free GitHub account. The second account could have a name like username-lnl, where you insert your current username. If you do it this way, you use the same four Apple Secrets for both repositories and you can choose the same MATCH_PASSWORD, but the GH_PAT will be unique for each GitHub account.

## Open Module in Codespaces

Now that the selected module fork exists in your GitHub account, you will open it in Codespaces. (If you are returning to change a customization you've already made, be sure to select the branch where you already made the previous customization; [Update Customization](#update-customization))

1. Right click (or control click) on [Codespaces](https://github.com/codespaces)
    * The opens a new tab in your browser
    * Click on the green button on the right that says `New Codespace`
1. On new screen
    * Click on Select a repository and choose your GitHub username/moduleName for the module you want to modify
    * You will see a message the `Codespace usage for this repository is paid for by username` - you get 60 free hours per month, so you can ignore this message
        * First time - leave the branch alone (dev)
        * Subsequent times - select your customized branch, e.g., main_3.0_custom
    * You do not need to modify the region or machine type
    * Click on the green button at the bottom that says `Create codespace`
1. A message appears saying setting up your codespace; and then the Codespaces screen appears showing the README.md file (by default) for that repository
1. Your screen will be similar to that shown below

    ![Codespaces screen for newly opened codespace](img/codespace-initial-loop.png){width="500"}
    {align="center"}

    * Note:
        * The URL includes the name of the machine that was assigned to you, for example: congenial space spork
        * There are 4 sections of the display you need to worry about - highlighted with numbered red rectangles

If you have already made a customization in this module and you are returning for another modification, skip to [Customize the Module](#customize-the-module).

### First Time for this Module

1. In the section indicated by the red rectangle labeled 4 (the terminal window), click to the right of the line where it says and paste the commands: 
    ```@username -> /workspaces/moduleName (dev) $```
1. Find the correct command list in the [First Time for Loop 3.0.0](#first-time-for-loop-300) section below, click the copy button and then paste into the terminal window.
    * you will be asked if you want to allow the paste - say yes and check the do not ask me again box
1. If there were errors, read the steps to see what might be wrong and reach out for help - do not continue if you see errors.

Skip ahead to [Customize the Module](#customize-the-module).

## First Time for Loop 3.0.0

These commands are used ONLY for Loop 3.0.0 and only the first time you work with a given Module. Copy the indicated set of commands and paste into the terminal window. This takes the repository to the correct version for Loop 3.0.0 and creates a special branch where your customizations will live on your fork.

#### Configure Loop Module

* Do not use if you have already made modifications
* Do not use if you built the LnL Patched Version

``` { .sh .copy title="Loop: Copy and Paste into Terminal" }
git checkout -q 743b8d7
git switch -c main_3.0_custom
```

After you paste in the Codespaces terminal window, then skip ahead to [Customize the Module](#customize-the-module).

#### Configure LoopKit Module

* Do not use if you have already made modifications
* Do not use if you built the LnL Patched Version

``` { .sh .copy title="LoopKit: Copy and Paste into Terminal" }
git checkout -q 0d5929e
git switch -c main_3.0_custom
```

After you paste in the Codespaces terminal window, then skip ahead to [Customize the Module](#customize-the-module).

#### Configure OmniBLE Module

* Do not use if you have already made modifications
* Same commands are used for released and LnL Patched Version

``` { .sh .copy title="OmniBLE: Copy and Paste into Terminal" }
git checkout -q 6d9b57d
git switch -c main_3.0_custom
```

After you paste in the Codespaces terminal window, then skip ahead to [Customize the Module](#customize-the-module).
Module](#customize-the-module).

#### Configure rileylink_ios Module

* Do not use if you have already made modifications
* Same commands are used for released and LnL Patched Version

``` { .sh .copy title="rileylink_ios: Copy and Paste into Terminal" }
git checkout -q 482ef4f
git switch -c main_3.0_custom
```

After you paste in the Codespaces terminal window, then skip ahead to [Customize the Module](#customize-the-module).

## Update Customization

If you are returning to change a customization you've already made, follow these directions.

1. Click on [Codespaces](https://github.com/codespaces)
    * Click on the green button on the right that says `New Codespace`
1. On new screen
    * Click on Select a repository and choose your GitHub username/moduleName for the module you want to modify
    * You will see a message the `Codespace usage for this repository is paid for by username` - you get 60 free hours per month, so you can ignore this message
    * Select your customized branch, e.g., main_3.0_custom
    * You do not need to modify the region or machine type
    * Click on the green button at the bottom that says `Create codespace`
1. A message appears saying setting up your codespace; and then the Codespaces screen appears showing the README.md file (by default) for that repository
1. In the section indicated by the red rectangle labeled 4 (the terminal window), you should see the line: 
    ```@username -> /workspaces/moduleName (main_3.0_custom) $```

Continue with [Customize the Module](#customize-the-module).

### Customize the Module

## Special Cases

### Existing Fork for Module

What if you already have a fork of one of the modules?

#### Situation 1

**Your fork is from using this page earlier and you already have a main_#.#_custom branch**

* Option A: You want to add a new customization to your existing main_#.#_custom branch
    * Go to [Update Customization](#update-customization)
* Option B: You want to throw away your existing main_#.#_custom branch and start over
    * Follow the [GitHub Instructions to delete a branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository#deleting-a-branch)
    * Click on Code, make sure you are at the dev branch and sync the fork
    * Go to [Open Module in Codespaces](#open-module-in-codespaces)

#### Situation 2

**Your existing fork is from the correct location (LoopKit or ps2)**

* Option A: Your existing fork shows the dev branch as the default branch
    * Tap on sync fork
    * Go to [Open Module in Codespaces](#open-module-in-codespaces)
* Option B: You probably know what to do or this would not be your situation - ask for help if you are confused

#### Situation 3

**Your existing fork is from the repository other than (LoopKit or ps2)**

If your fork is from loopnlearn then you need to follow the directions (that are not written yet) on the loopandlearn dot org website.

If you know this is a fork you do not care about, you can delete the repository.

* Instructions to delete a repository are found at [GitHub Docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository)

Once deleted, go to [Create a Fork for Selected Module](#create-a-fork-for-selected-module).


## Background Information

### LoopWorkspace

The LoopWorkspace repository is the umbrella organization holding all the pieces needed to build the Loop app. Part of what LoopWorkspace provides is a list of pointers to a specific commit for each module used in the workspace.

* A commit is a specific version of code in a repository
* A workspace is a grouping of several repositories (modules) into a complete package
* The workspace includes a list of the specific commit for each repository (module)

The steps given earlier on this page modifies the commit for the module that you change used by LoopWorkspace when it builds.

* A commit to a module can be made without affecting the workspace
* To update the workspace to use the new commit for a module, the list containing the specific commit for that repository (module) must also be updated
    * This update is itself a commit to the workspace repository

This allows a given module, say Loop, to be updated with a new commit; but that commit doesn't affect the Loop app that you build using LoopWorkspace. Once you change the LoopWorkspace to point to the new commit in Loop, then the Loop app you build 

### What are branches again?

Branches indicate different version of code - this tutorial is pretty nice.

* The history required for the main branch (released code) is also present in the dev branch for the submodules
* The commands listed earlier on this page are to assist you in creating your own branch and you will customize that branch
* If you later want to modify your customization, start with the branch you already created and edit it

