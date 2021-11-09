# Step 13: Download Loop Code

!!! info "Time Estimate"
    - 10 minutes to read this page
    - Wait until Step 14 to download Loop code (New Workspace Method)

!!! abstract "Summary"
    - All Loopers: Loop can only be built with the Workspace Build method
    - To make it easy, there's a script for you to use
    - New Builders: Review this page until told to go to Step 14
    - Repeat Builders: There is important information about iOS updates - don't skip that section
    - Advanced Users: There is information for you too

!!! question "FAQs"
    - **When do I need to download new Loop code?** There are three times you need to download new code:
        1. When you build Loop initially
        1. When a new release of Loop has features you want
        1. When your app expires (one year paid, one week free)
    - **What do I do when a new iOS is released?** The short answer is wait a bit:
        * It's a good idea to be prepared to rebuild before updating your phone to the new iOS
        * This is even more important when there has been a major change to iOS or Xcode
        * Check with the experts - there will be announcements in all the [Loop Social Media](../index.md#stay-in-the-loop) sites
    - **How do I find out about new features?** Please see [Loop Releases and Branch FAQs](../faqs/branch-faqs.md)

## Download Loop

You’ll need to first download the Loop code and then build the app on your computer with Xcode, which will transfer the app to your iPhone or iPod. This page prepares you to download Loop - you'll actually do the download in the next step.

## New Loopers

If this is your first time, you only need to read the Build Select Script Workspace Method section.

At the end of that section you'll be directed to Step 14.  You are welcome to read the rest of this page, but you can ignore any comments about old and new build methods or instructions for advanced users.

## Build Select Script Workspace Method

The Build Select script is a quick and easy way to build Loop:

* Builds Loop using the Workspace method
    * Workspace build is required as of Xcode 13
    * Workspace build works fine with Xcode 12
* Supports more than just Loop
* Provided by the Loop and Learn mentors

New builders - head to Step 14 in which you will execute the script steps and [Build the Loop App](step14.md).

---

If you are a "Repeat Looper" or interested in the dev branch, there is more information on the the rest of this page.

For those "Repeat Loopers" who remember when you had to use a "dev" branch to get features like automatic-bolus, you do not need to do that.  Automatic-bolus Dosing Strategy is included in Loop Master.


## Repeat Loopers

You may remember building with the old zip download method. The zip download is no longer supported.

* The zip download method had a very fast download, followed by a very long build while Xcode collected more code from the internet to enable you to build the complete app. It is not an option now that Loop needs to support Xcode 13, which is required for iOS 15.

* The new method uses Workspace and works for Xcode 12 as well as Xcode 13. This downloads everything you need up front and builds much faster.

* You may remember information indicating that Workspace is only for experts - that only refers to people working on the next version of Loop (known as the dev branch).

### Xcode 13, iOS 15 changes

!!! warning "DO NOT UPDATE your phone to iOS 15 without reading this"

    Any Loop app built with Xcode version prior to Xcode 12.5 will immediately fail when the phone is updated to iOS 15. (Any one who last built with Catalina should not install iOS 15 without following "safe steps" below.)

    Follow this link, [Xcode version](../faqs/update-faqs.md#how-can-i-confirm-xcode-version-i-used), for instructions to determine what version was used when building the Loop app currently on your phone.

    Safe steps to keep Loop going if you want to install iOS 15

    * update your macOS
    * update your Xcode to version 13
    * build the Loop app on your phone
    * update phone to iOS 15

Modifications to building Loop with Xcode 13:

* iOS 15 requires Xcode version 13 to build
* You must use the Workspace method to build Loop with Xcode 13
* The old download the zip method will not work once you update your Xcode to version 13
* For earlier iOS versions, you can still use Xcode 12 but should use the Workspace method


## Manual Workspace Method

In order to manually create the Loop app using the Workspace method, and not use the script, you need to execute the commands listed below on your computer. You are welcome to do this and put the downloaded code where you prefer. The advantage of using the script is it provides options to do steps that are required when building Loop a second time, creates a date-time stamped folder for the download, clones the code into that folder, automatically opens Xcode in the correct folder and opens the graphic showing you the steps required to finish building the code.

If you decide to do a manual download, please create a folder for it where there are no embedded spaces in the path name. At the current time, embedded spaces are causing a problem when building.  For Loop master, the problem is easy to solve, but you will get a [build error](build_errors.md#compileassetcatalog-error).

There is a copy button on the right-hand side if you hover your mouse over the text block below. It may be obscured by the long text-string, but it is there.

``` title="Manual Clone command for Loop Master"
git clone --branch=master  --recurse-submodules https://github.com/LoopKit/LoopWorkspace
```

Confirm there were no errors in the download.

``` title="Change directory and automatically open Xcode"
cd LoopWorkspace; xed .
```

At this point, you should move to [Build Step 14: Xcode Steps](step14.md#wait-for-xcode-to-finish-indexing).


## Advanced Users Only

If you are an advanced user who wants to build the dev branch - this section is for you.

**At the current time, embedded spaces are causing a problem when building dev and there is no known solution.**

* Be sure to clone into a directory with no embedded spaces in the path

!!! abstract "Advanced Users Only"

    **Only build the dev branch if you're a developer/advanced user**

    Please read [What's going on in the dev branch?](../faqs/branch-faqs.md#whats-going-on-in-the-dev-branch) before deciding to test the dev branch.

    - Note, the dev branch requires a minimum of iOS 14 on your device
    - Once you install the dev branch on a device, you must delete the app to return to master, which means all settings will need to be entered and a new pod started
    - The dev branch user interface is different, i.e., the documentation in LoopDocs does not always match the screens you will see when you use the Loop app built from the dev branch
    - [Loop dev Preview](../faqs/dev-menus.md) is found in the FAQs section with some preliminary documentation

    The dev branch requires using LoopWorkspace and requires installation of carthage 0.36.0 on your Mac.  The links below are to the wiki for LoopWorkspace, the LoopDocs page on building with LoopWorkspace and the instructions for installing carthage 0.36.0 (not needed for Loop master)  


    * [LoopWorkspace README](https://github.com/LoopKit/LoopWorkspace#readme): Replace "<branch\>" in "git clone" line with "dev"

    * LoopDocs page on [LoopWorkspace](loopworkspace.md)

    * LoopDocs page, ["Skip Step 7"](step7.md#install-carthage-0360) for installing carthage 0.36.0

    New trick (dev branch only):

    * Edit the LoopConfigOverride.xcconfig
    * Uncomment the line starting with `LOOP_DEVELOPMENT_TEAM = `
    * Insert your developer ID
    * Build the Loop(Workspace) - all targets are signed automatically
