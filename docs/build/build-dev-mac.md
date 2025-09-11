## Overview


**This page is only relevant when building the `dev` branch with a *Mac*.**

**For *Browser Build*, please see: [Build Loop dev with Browser](../browser/build-dev-browser.md)**

**No matter the method used to build Loop-dev, you are testing development code. Please read this link now before continuing.**

* **[What's going on in the `dev branch`](../version/development.md#whats-going-on-in-the-dev-branch)**

## Build `dev` with Mac

The same script is used to build the `dev` branch as is used to build the `main` branch. Copy and paste this command in any terminal. Follow the instructions on the screen. Choose Build Loop and then choose `dev` branch.

``` { title="Copy and Paste to start the BuildLoop Script" }
/bin/bash -c "$(curl -fsSL \
  https://raw.githubusercontent.com/loopandlearn/lnl-scripts/main/BuildSelectScript.sh)"
```

For more detailed instructions, head over to:

* [Experienced Builder: Instructions to Download and Build Loop](https://loopkit.github.io/loopdocs/build/build-app/#download-loop){: target="_blank" }

* [New Builder: Start here to set up Developer Mode on Phone and Watch](https://loopkit.github.io/loopdocs/build/build-app/#prepare-your-phone-and-watch){: target="_blank" }

### Build Other Branches

You can use the BuildLoop script to build a feature branch that was advertised in zulipchat but has not been merged into `dev`. 

> Note. You cannot use the BuildSelectScript to select a custom branch. You must directly choose the app you wish to build. In this case, BuildLoop.

In the command (shown below), there is a space after the final quote, followed by a hyphen, another space and then the branch name. This example would build `other-branch`, if such a branch existed. 

> This is just an example. You need to substitute the branch you desire for `other-branch`. The example below uses a continuation character to put the extra characters on a new line to make this easier to read.

``` { title="Replace <code>other-branch</code> with the desired branch" }
/bin/bash -c "$(curl -fsSL \
  https://raw.githubusercontent.com/loopandlearn/lnl-scripts/main/BuildLoop.sh)" \
   - other-branch
```

If you want to customize this custom branch. You can call the Customization Select script after you download the custom branch. This script finds the most recent download in your ~/Downloads/BuildLoop folder. If you want to customize a specific branch, first set the terminal to be in the LoopWorkspace folder for the download you want to customize.

``` { title="Copy and paste to start the CustomizationSelect script" }
/bin/bash -c "$(curl -fsSL \
  https://raw.githubusercontent.com/loopandlearn/lnl-scripts/main/CustomizationSelect.sh)"
```

## Update Loop-dev

While Loop-dev is under active development, you should monitor zulipchat and update frequently.

Checking for updates every week is a good idea. Also - subscribe to all the streams on [Loop Zulipchat](https://loop.zulipchat.com) to make sure you don't miss critical information.

You may choose to download fresh each time you update. 

You may prefer to use commands to fetch and pull the latest code without making a new clone.

* Some users like to use [GitKraken](https://support.gitkraken.com/) to assist them (link takes you to a tutorial video).
* Some are comfortable with the command line git commands described on [here](../version/loopworkspace.md#updating-loop-using-loopworkspace).

## Loop-dev Version

Starting with v3.7.x, the version of code that shows up under the Loop Settings screen increments with each formal change to the `dev` branch using the pull request process. That increment might be an update to match a hotfix to `main` or might be from a new feature brought just into the `dev` branch.

If you need help with your app, the mentors need to know you are running a `dev` branch and the specific version that shows on your settings screen. 

For a summary of features added to the `dev` branch by version number:

* [Updates in `dev`](../version/development.md#updates-in-dev){: target="_blank" }

For more information about version numbers:

* [`Loop` Version Numbering](../version/releases.md#loop-version-numbering){: target="_blank" }
