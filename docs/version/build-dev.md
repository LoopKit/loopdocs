## Building Development Code

**No matter the method used to build Loop-dev: GitHub actions or git commands, you are testing development code. Please read this link now before continuing.**

* **[What's going on in the `dev branch`](../version/development.md#whats-going-on-in-the-dev-branch)**

There are several methods to build Loop-dev. First review the general information on this page then choose the link for the method of your choice:

## Update Frequently

While Loop-dev is under active development, you should monitor zulipchat and update frequently. Sometimes the `dev` branch is quiet for a month or more and other times it gets updated daily. Please pay attention.

Checking for updates every week is a good idea. Also - subscribe to all the streams on [Loop Zulipchat](https://loop.zulipchat.com) to make sure you don't miss critical information.

## Loop-dev Version

The version of code that shows up under the Loop Settings screen does not change when the `dev branch` is modified.

If you need help with your app, the mentors need more information. Please issue a Loop Report when asking for help. Refer to [Support](../loop-3/settings.md#support) for how to issue a Loop Report. If you want to keep track yourself, refer to [Identify Loop-dev Version](#identify-loop-dev-version)

* [`Loop` Version Numbering](releases.md#loop-version-numbering)

### Identify Loop-dev Version

The version of code that shows up under the Loop Settings screen will remain fixed until Loop-dev is released. In order to identify which version of dev you have on your phone, you need the commit.

The commit is identified by a 7-digit alphanumeric code.  That code was also appended to the folder name of the downloaded code under Downloads/BuildLoop as shown in the graphic above.  You can use finder to view the folder name after the script completes. It also appears in the Loop Report, refer to [Support](../loop-3/settings.md#support) for instructions on issuing a Loop Report. After you issue the Loop Report, look at the workspaceGitRevision number near the beginning of the report.

## Build `Loop` `dev`

1. For the Build with Browser method
    * [Build dev with Browser](../browser/build-dev-browser.md)
1. For the Build with *Mac* method:
    * [Build dev with *Mac*](../build/build-dev-mac.md)
