## Overview


**This page is only relevant when building the `dev` branch with a *Mac*.**

**For *Browser Build*, please see: [Build Loop dev with Browser](../browser/build-dev-browser.md)**

**No matter the method used to build Loop-dev, you are testing development code. Please read this link now before continuing.**

* **[What's going on in the `dev branch`](../version/development.md#whats-going-on-in-the-dev-branch)**

## `BuildLoopDev` Script

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

Checking for updates every week is a good idea. Also - subscribe to all the streams on [Loop Zulipchat](https://loop.zulipchat.com){: target="_blank" } to make sure you don't miss critical information.

You may choose to download fresh each time you update. 

You may prefer to use commands to fetch and pull the latest code without making a new clone.

* Some users like to use [GitKraken](https://support.gitkraken.com/){: target="_blank" } to assist them (link takes you to a tutorial video).
* Some are comfortable with the command line git commands described on [here](../version/loopworkspace.md#updating-loop-using-loopworkspace).

## Loop-dev Version

The version of code that shows up under the Loop Settings screen does not change when the `dev branch` is modified.

If you need help with your app, the mentors need more information. Please issue a Loop Report when asking for help. Refer to [Support](../loop-3/settings.md#support) for how to issue a Loop Report. If you want to keep track yourself, refer to [Identify Loop-dev Version](#identify-loop-dev-version)

* [`Loop` Version Numbering](../version/releases.md#loop-version-numbering)

### Identify Loop-dev Version

The version of code that shows up under the Loop Settings screen will remain fixed until Loop-dev is released. In order to identify which version of dev you have on your phone, you need the commit.

The commit is identified by a 7-digit alphanumeric code.  That code was also appended to the folder name of the downloaded code under Downloads/BuildLoop as shown in the graphic above.  You can use finder to view the folder name after the script completes. It also appears in the Loop Report, refer to [Support](../loop-3/settings.md#support) for instructions on issuing a Loop Report. After you issue the Loop Report, look at the workspaceGitRevision number near the beginning of the report.
