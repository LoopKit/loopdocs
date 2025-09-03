## Overview


**This page is only relevant when building the `dev` branch with a *Mac*.**

**For *Browser Build*, please see: [Build Loop dev with Browser](../browser/build-dev-browser.md)**

**No matter the method used to build Loop-dev, you are testing development code. Please read this link now before continuing.**

* **[What's going on in the `dev branch`](../version/development.md#whats-going-on-in-the-dev-branch)**

## `BuildLoopDev` Script

> With the modification of how the `dev` branch is handled starting with v3.7.x, the build scripts will be updated. In the interim, choose the tip of dev when using the existing scripts. The concept of the lightly tested commit is no longer needed and the SHA is not being updated.

There is a script to assist in building the `dev branch`. It gives you the option to choose the tip of the `dev branch` or to build a lightly tested commit. If you have not used the [Build Select Script](../build/build-app.md#build-select-script) to build Loop previously, you may want to review that page. The command below can be pasted into the terminal of your Mac. Read the directions in the script.

``` { .bash .copy title="Copy and Paste to start the BuildLoopDev script" }
/bin/bash -c "$(curl -fsSL \
  https://raw.githubusercontent.com/loopandlearn/lnl-scripts/main/BuildLoopDev.sh)"
```

### Build Other Branches

You can use the BuildLoopDev script to build a specific development branch, other than `dev`. At the end of the script (from above), add a space after the final quote, followed by a hyphen, another space and then the branch name. See the example below that would build `other-branch`, if such a branch existed. This is just an example. You need to substitute the branch you desire for `other-branch`. The example below uses a continuation character to put the extra characters on a new line to make this easier to read.

``` { title="Replace <code>other-branch</code> with the desired branch" }
/bin/bash -c "$(curl -fsSL \
  https://raw.githubusercontent.com/loopandlearn/lnl-scripts/main/BuildLoopDev.sh)" \
   - other-branch
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
