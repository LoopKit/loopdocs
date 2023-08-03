## Building Development Code

**No matter the method used to build Loop-dev: GitHub actions or git commands, you are testing development code. Please read this link now before continuing.**

* **[What's going on in the dev branch](../version/development.md#whats-going-on-in-the-dev-branch)**

Several methods to build Loop-dev are mentioned on this page:

1. For the GitHub Browser Build method
    * [Update Loop-dev: GitHub Build method](#github-build-method)
1. For the Mac-Xcode method:
    * [Update Loop-dev: Mac-Xcode Build method](#mac-xcode-build-method)

## BuildLoopDev Script

There is a script to assist in building the dev branch. It gives you the option to choose the tip of the dev branch or to build a lightly tested commit. If you have not used the [Build Select Script](../build/step14.md#build-select-script) to build Loop previously, you may want to review that page.

``` { .bash .copy title="Copy and Paste to start the BuildLoopDev script" }
/bin/bash -c "$(curl -fsSL \
  https://raw.githubusercontent.com/loopandlearn/lnl-scripts/main/BuildLoopDev.sh)"
```
### BuildLoopDev Script Libre

There used to be a section here telling you how to build a special branch that had Libre support included. That is no longer necessary because Libre support was merged into dev.

Both the dev branch and the lightly tested branch of dev have Libre support.

### BuildLoopDev Other Branches

You can use the BuildLoopDev script to build a specific development branch, other than dev. See the example below that would build `other-branch`, if such a branch existed. This is just an example. You need to substitute the branch you desire for `other-branch`. There must be a space after the final quote, followed by a hyphen, another space and then the branch name.

``` { .bash .copy title="Example using <code>other-branch</code> with the BuildLoopDev script" }
/bin/bash -c "$(curl -fsSL \
  https://raw.githubusercontent.com/loopandlearn/lnl-scripts/main/BuildLoopDev.sh)" - other-branch
```

## Update Loop-dev

While Loop-dev is under active development, you should monitor zulipchat and update frequently.

### GitHub Build Method

If you are using the GitHub method, once you have configured your fork to point to the dev branch, just follow the update instructions.

* [GitHub Build for dev](../gh-actions/gh-update.md#github-build-for-dev)

### Mac-Xcode Build Method

You can use TestFlight with this method if you want the convenience of a remote build. See [TestFlight with your Mac-Xcode build](../build/testflight-xcode.md). With TestFlight, you need to renew the build every 90 days.

When building frequently, it is optional to update your provisioning profile with every new build. If you want to always ensure one year, copy and paste the following command into the terminal before building. This forces Xcode to create a new provisioning profile instead of reusing one with an older expiration date.

```title="Copy and Paste to remove Provisioning Profiles"
rm ~/Library/MobileDevice/Provisioning\ Profiles/*.mobileprovision
```

Checking for updates every week is a good idea. Also - subscribe to all the streams on [Loop Zulipchat](https://loop.zulipchat.com) to make sure you don't miss critical information.

You may choose to download fresh each time you update. 

You may prefer to use commands to fetch and pull the latest code without making a new clone.

* Some users like to use [GitKraken](https://support.gitkraken.com/) to assist them (link takes you to a tutorial video).
* Some are comfortable with the command line git commands described on [here](../version/loopworkspace.md#updating-loop-using-loopworkspace).

## Loop-dev Version

The version of code that shows up under the Loop Settings screen does not change when the dev branch is modified.

If you need help with your app, the mentors need more information. Please issue a Loop Report when asking for help. Refer to [Support](../loop-3/settings.md#support) for how to issue a Loop Report. If you want to keep track yourself, refer to [Identify Loop-dev Version](#identify-loop-dev-version)

With the release of Loop 3, the numbering for Loop-dev has a new pattern of even (released) and odd (dev) numbers for the "x" place in 3.x.m. 

For example:

* Loop 3.0.0 was the first released version of Loop 3
    * If minor updates are required before the next release, they will be numbered Loop 3.0.1, etc.
* Loop 3.1.0 was the development version before Loop 3.2.0 was released
* Loop 3.2.0 was the next released version
* Loop 3.2.1 and 3.2.2 were minor releases
* Loop 3.3.0 is the current development version

### Identify Loop-dev Version

The version of code that shows up under the Loop Settings screen will remain fixed until Loop-dev is released. In order to identify which version of dev you have on your phone, you need the commit.

The commit is identified by a 7-digit alphanumeric code.  That code was also appended to the folder name of the downloaded code under Downloads/BuildLoop as shown in the graphic above.  You can use finder to view the folder name after the script completes. It also appears in the Loop Report, refer to [Support](../loop-3/settings.md#support) for instructions on issuing a Loop Report. After you issue the Loop Report, look at the workspaceGitRevision number near the beginning of the report.
