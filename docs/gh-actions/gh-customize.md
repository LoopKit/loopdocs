## How to Customize a GitHub Build

These are bare-bones instructions for applying customizations.

You do not need very many "git" commands (and I'll tell you which ones).

You do not need a Mac, you can still do this using any browser - easiest to do this on a computer.

There is some background information at the bottom of this page starting at [LoopWorkspace](#loopworkspace) if you want to know what you are doing. Otherwise, just follow the steps like a cookbook.

## Editing Code

You will be using the online tool associated with GitHub called Codespaces. Any repository in your account can be opened with Codespaces.

You will need a text editor to format a command line for each module you change. Use the same text editor you use for saving your Secrets. You do not want characters like double hypen or quote symbols modified by a smart editor.

## Decide Which Modules You Want to Modify

If you have a [Code Customization](../build/code_customization.md) in mind, you will see that each item lists a folder name. You only need the Module name (first name before the first / character).

This table lists all the modules referred to on the Code Customization page linked above:

| Folder | Module | Fork From |
| --- | --- | --- |
| Loop/LoopCore | Loop | [https://github.com/LoopKit/Loop](https://github.com/LoopKit/Loop) |
| LoopKit/LoopKitUI/Extensions | LoopKit | [https://github.com/LoopKit/LoopKit](https://github.com/LoopKit/LoopKit) |
| OmniBLE/OmniBLE/PumpManagerUI | OmniBLE | [https://github.com/LoopKit/OmniBLE](https://github.com/LoopKit/OmniBLE) |
| rileylink_ios/OmniKit/OmnipodCommon | rileylink_ios | [https://github.com/ps2/rileylink_ios](https://github.com/ps2/rileylink_ios) |

!!! tip "Pro Tip"
    Open 4 browser tabs or windows so you can click between locations.

    * This page
    * [LoopDocs: Code Customization](../build/code_customization.md) 
    * Your GitHub account
    * A new one that you'll use to open Codespaces

## Create a Fork for Selected Module

If you want a modification that uses a particular module, you must fork that module to your GitHub account.

1. Log into your GitHub account
1. Right click (or control click) on the URL in the table above to open in your browser
1. This shows the repository you need to fork
1. Tap on Fork

Remember - you can only have a single fork of a given repository. If you already have a fork, you don't need another one; but it must be a fork from the URL listed above.

When you fork a repository, the default branch is the one that is forked. That is ok. Only include that default branch when forking.

| Repository | Default Branch |
| --- | --- |
| LoopKit/LoopWorkspace | main |
| LoopKit/Loop | dev |
| LoopKit/LoopKit | dev |
| LoopKit/OmniBLE | dev |
| ps2/rileylink_ios | dev |

The LoopWorkspace main branch is always the most recent released code.

This page has instructions for applying customizations to released code, main branch of LoopWorkspace. Don't worry about the other repositories using dev as the default branch. Everything you need to update LoopWorkspace main is included in the dev branches of the lower level repositories (modules).

!!! warning "Loop with LnL Patches"
    Some Loop users build with the loopnlearn version of LoopWorkspace using the main_lnl_patches branch. If you are one of those users, do not use the URL table above. There is also an extra step to prepare your fork. The LnL instruction page is not yet available; but will be found on the LnL website (later).

    If you want to deal with both released Loop (fork from LoopKit) and LnL with Patches, it is suggested you set up a second free GitHub account. The second account could have a name like username-lnl, where you insert your current username. If you do it this way, you use the same four Apple Secrets for both repositories and you can choose the same MATCH_PASSWORD, but the GH_PAT will be unique for each GitHub account.

## Open Module in Codespaces

Now that the selected module fork exists in your GitHub account, you will open it in Codespaces. (If you are returning to change a customization you've already made, be sure to select the branch where you are already made the previous customization.)

1. Click on [Codespaces](https://github.com/codespaces)
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

1. Find the correct command list in the [Configure for Loop 3.0.0](#configure-for-loop-300) section below, click the copy button and then return to these instructions
1. In the section indicated by the red rectangle labeled 4 (the terminal window), click to the right of the line where it says and paste the commands: 
    ```@username -> /workspaces/moduleName (dev) $```

### Configure for Loop 3.0.0

These commands are used ONLY for Loop 3.0.0. Copy the indicated set of commands and paste into the terminal window.

#### Configure Loop Module

* Do not use if you have already made modifications
* Do not use if you built the LnL Patched Version

``` { .sh .copy title="Loop: Copy and Paste into Terminal" }
git checkout 743b8d7
git checkout -b main_3.0_custom
```

#### Configure LoopKit Module

* Do not use if you have already made modifications
* Do not use if you built the LnL Patched Version

``` { .sh .copy title="LoopKit: Copy and Paste into Terminal" }
git checkout 0d5929e
git checkout -b main_3.0_custom
```

#### Configure OmniBLE Module

* Do not use if you have already made modifications
* Same commands are used for released and LnL Patched Version

``` { .sh .copy title="OmniBLE: Copy and Paste into Terminal" }
git checkout 6d9b57d
git checkout -b main_3.0_custom
```

#### Configure rileylink_ios Module

* Do not use if you have already made modifications
* Same commands are used for released and LnL Patched Version

``` { .sh .copy title="rileylink_ios: Copy and Paste into Terminal" }
git checkout 482ef4f
git checkout -b main_3.0_custom
```

### Configure for LnL Patched Version of Loop 3.0.0

If you built using the loopnlearn/LoopWorkspace, these 2 modules require a different set of configuration commands. These should ONLY be used if you forked your LoopWorkspace from loopnlearn/LoopWorkspace. Note that the new branch you create includes the information that these started with main_lnl_patches branch for 3.0.0.

For these modules you must add a new branch, main_lnl_patches to your fork, before starting the Codespaces. And when you start code spaces, select main_lnl_patches as the branch before creating the code space.

#### Configure Loop Module for main_lnl_patches

* Do not use if you have already made modifications
* Do not use these with released version

``` { .sh .copy title="Loop: Copy and Paste into Terminal" }
git checkout d41cf86
git checkout -b main_lnl_patches_3.0_custom
```

#### Configure LoopKit Module for main_lnl_patches

* Do not use if you have already made modifications
* Do not use these with released version

``` { .sh .copy title="LoopKit: Copy and Paste into Terminal" }
git checkout 21816df
git checkout -b main_lnl_patches_3.0_custom
```


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

