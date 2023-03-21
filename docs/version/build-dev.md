## Building Development Code

**No matter the method used to build Loop-dev: GitHub actions or git commands, you are testing development code. Please read this link now before continuing.**

* **[What's going on in the dev branch](../version/development.md#whats-going-on-in-the-dev-branch)**

Several methods to build Loop-dev are mentioned on this page:

1. For the GitHub Browser Build method
    * [Update Loop-dev: GitHub Build method](#github-build-method)
1. For the Mac-Xcode method:
    * [Update Loop-dev: Mac-Xcode Build method](#mac-xcode-build-method)

## Build Loop dev with a Script

!!! danger "No Script for dev"
    There was interim script that was provided for users in the time just before the release of Loop 3. It helped build a lightly-tested version of the dev branch.

    * After the release of Loop 3, this script is no longer available
    * It was provided as a convenience for users who wanted DASH but were not comfortable with the requirements of building a dev branch
    * People should either be on the released version of Loop or know how to build dev without a script using either the GitHub or Mac-Xcode method

## Update Loop-dev

While Loop-dev is under active development, you should monitor zulipchat and update frequently.

### GitHub Build Method

If you are using the GitHub method, once you have configured your fork to point to the dev branch, just follow the update instructions.

* [GitHub Build for dev](../gh-actions/gh-update.md#github-build-for-dev): Configure your fork to point to dev branch (one time only)
* [GitHub Update](../gh-actions/gh-update.md): Instructions are the same as for main, but the Actions are different as described in the first link

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
* Loop 3.2.1 is a minor release
* Loop 3.3.0 is the current development version

### Identify Loop-dev Version

The version of code that shows up under the Loop Settings screen will remain fixed until Loop-dev is released. In order to identify which version of dev you have on your phone, you need the commit.

The commit is identified by a 7-digit alphanumeric code.  That code was also appended to the folder name of the downloaded code under Downloads/BuildLoop as shown in the graphic above.  You can use finder to view the folder name after the script completes. It also appears in the Loop Report, refer to [Support](../loop-3/settings.md#support) for instructions on issuing a Loop Report. After you issue the Loop Report, look at the workspaceGitRevision number near the beginning of the report.
