# Step 13: Download Loop Code

!!! info "Time Estimate"
    - 10 minutes to read this page
    - Wait until Step 14 to download Released Loop code (New Workspace Method)

!!! abstract "Summary"
    - **All Loopers:** Loop can only be built with the Workspace Build method
        - To make it easy, there's a script for you to use
    - **New Loopers:** Review this page until told to go to Step 14
    - **Repeat Builders:** Optional information for the curious
    - **Advanced Users:** Read all of Step 13

!!! question "FAQs"
    - **When do I need to download new Loop code?** You need new code before you build
    - **What if I want to get a new feature in my copy of Loop?** Start at [Updating](updating.md)
    - **How do I find out about new features?** Please see [Loop Release FAQs](../faqs/release-faqs.md)
    - **What do I do if there is a major release (by Apple) of new iOS?** The short answer is wait a bit:
        * It's a good idea to be prepared to rebuild before updating your phone to the new iOS
        * This is even more important when there has been a major change to iOS or Xcode
        * Check with the experts - there will be announcements in all the [Loop Social Media](../index.md#stay-in-the-loop) sites
    - **How often to I have to rebuild?**
        1. You must build when your app expires (one year paid, one week free)
        1. It is recommended you rebuild more frequently to avoid panic when your app is about to expire as explained in [Updating FAQs](../faqs/update-faqs.md)

## New Loopers

You will do the download in the next step.

For those who are new to Loop, never built Loop or can't remember anything about the last time you built Loop:

Head to Step 14 to [Build the Loop App](step14.md).

## Repeat Builders

In you haven't built in a while, but have been using Loop for a long time:

* The method to build Loop changed with the advent of Xcode 13 (Sept 2021).
* Loop must be built with a workspace build as explained in Step 14 [Build the Loop App](step14.md).
* The Dosing Strategy of Automatic Bolus or Temp Basal Only is in the released version of Loop (Aug 2021)
    * You do not need a special branch to get this feature


## Advanced Users Only

!!! abstract "Advanced Users Reminders"

    If you are an advanced user who wants to build the dev branch - this section is for you.

    Everyone else - head to Step 14 to [Build the Loop App](step14.md).

    * Be sure to clone into a new directory that does not already have a folder called LoopWorkspace in it.
    * Loop-dev is the only workspace build that still requires carthage and it requires a specific version - don't worry - instructions are provided below

Yes - this section is "out-of-place", but the Step 14 Build Loop App page is already very long and complicated. If you can build Loop-dev, you can find this section.

**Only build the dev branch if you're a developer/experienced user**

### Before Downloading

Please read [What's going on in the dev branch?](../faqs/branch-faqs.md#whats-going-on-in-the-dev-branch) before deciding to test the dev branch.

- Note, the dev branch requires a minimum of iOS 14 on your device
- Once you install the dev branch on a device, you must delete the app to return to master, which means all settings will need to be entered in master and a new pod started
- The dev branch user interface is different, i.e., the documentation in LoopDocs does not always match the screens you will see when you use the Loop app built from the dev branch
- Please read the [Loop dev Preview](../faqs/dev-menus.md) page

### Carthage and Downloading

The dev branch requires installation of carthage 0.36.0 on your Mac.

* [Check carthage Status](#check-carthage-status) to ensure you have carthage 0.36.0 installed

* Review the instructions here: [LoopWorkspace README](https://github.com/LoopKit/LoopWorkspace#readme) 

* Use finder to create a new folder, typically in Downloads
    - Navigate to Downloads
    - Hold down the control key and click on the folder to open a menu
    - Select (near the bottom) New Terminal at Folder
    - You can choose to use an existing folder, but it cannot already have a folder in it called LoopWorkspace

* Copy and paste the lines below into that terminal window

```
git clone --branch=dev --recurse-submodules https://github.com/LoopKit/LoopWorkspace
cd LoopWorkspace
xed .
```

These three lines will download the code and open Xcode. Be sure to select LoopWorkspace and your phone.

### Signing Targets

If you choose to sign manually instead of using the new capability (next paragraph), you must sign 6 targets (add these 2 to the usual 4)

* Loop Intent Extension
* Learn

With Loop-dev, the signing of targets can be done by editing a single file:

* Edit the LoopConfigOverride.xcconfig file (you can do this in Xcode)
* The next to last line says `// Put your team id here for signing`
* The last line starts with two slashes `//` – remove those
* Replace the ID to the right of the equal sign with your Apple Developer ID
* Apple Developer Team ID can be found for your account (after you sign in) at:
    * [https://developer.apple.com/account/#!/membership](https://developer.apple.com/account/#!/membership)

!!! warning "Loop.xcodeproj/project.pbxproj"

    If you manually sign any of the targets, for example as an alternative way to get your Developer ID, the file in the Loop folder called `Loop.xcodeproj/project.pbxproj` is automatically modified to use that target name.

    Once that happens, the feature that enables Xcode to use the `LOOP_DEVELOPMENT_TEAM` keyword in the LoopConfigOverride.xcconfig is no longer available.

    To restore that capability, navigate in the terminal to the LoopWorkspace/Loop folder and issue this command:

    ```
    git restore Loop.xcodeproj/project.pbxproj
    ```


#### Loop-dev with Free Account

Yes you can build Loop-dev with the free account (Personal Team). There are some extra steps needed compared to the steps given for Loop 2.2.x on the [Build Step 14: Free Account](step14.md#free-account) section.

Note - if you know your Personal Team ID, you can enter it as directed in [Signing Targets](#signing-targets) above.

1. You must remove additional capabilities, the complete list is:
    * **Loop Target:** Push Notifications; Siri and **Time Sensitive Notifications**
    * **Watch App Extension Target:** Siri
1. Add the keyword `SIRI_DISABLED` to the LoopConfigOverride.xcconfig file
    * Examine the file and find the line that starts with `SWIFT_ACTIVE_COMPILATION_CONDITIONS = $(inherited)`
    * Insert the new keyword (separated by a space) any where after `$(inherited)` and before the slashes near the end of the line


### Build Loop-dev

* There are some package dependencies (new for Loop-dev) that are resolved first and then the indexing takes place
* If you notice a red x in Xcode (indicating an error) while it is resolving packages and indexing - please follow the steps for [Couldn't Get Revision for Package Dependency](build_errors.md#couldnt-get-revision-for-package-dependency)
* Once the packages are resolved and the indexing has started, you can build the app following the directions in the "Build Loop" section on the next page: [Step 14: Build Loop App #Build Loop](step14.md#build-loop).

We suggest reading the tips below on keeping Loop-dev updated. Checking for updates every week is a good idea.  Also - subscribe to all the streams on [Loop Zulipchat](https://loop.zulipchat.com) to make sure you don't miss critical information.

### Update Loop-dev

While Loop-dev is under active test, you will want to update frequently.

* Some users like to use [GitKraken](https://support.gitkraken.com/) to assist them (link takes you to a tutorial video).
* Some just repeat the cloning.
* Some are comfortable with the command line git commands described on [here](loopworkspace.md#updating-loop-using-loopworkspace).


### Check carthage Status

The steps required to install the correct version of carthage depend on whether carthage is already installed.

First copy and paste this phrase into the terminal and hit return:

```
carthage version
```

* If the response includes "0.36.0", you can build the Loop-dev branch. Ignore the instructions to "Please update to the latest Carthage version: . . ." You want to stick with 0.36.0.

* If the response is, "-bash: carthage: command not found", then skip ahead to the [Install carthage 0.36.0 step](#install-carthage-0360).

* Any other response requires you to delete the current version of carthage first.

Copy and paste the following line into the terminal window and hit return.  

```
rm -rf /usr/local/bin/carthage
```

Wait for the prompt to appear, then copy and paste this line into the terminal window and hit return:

```
sudo rm -rf /Library/Frameworks/CarthageKit.framework
```

You will be prompted for a password when you hit enter on the second line.   It is the same password you use in order to log into the computer.   It will not echo to the screen.


### Install carthage 0.36.0

Go to this link: [Carthage.pkg](https://github.com/Carthage/Carthage/releases/tag/0.36.0) to download the carthage 0.36.0 package. After following the preceding link, ignore the warning message, scroll down to the Assets section and click on Carthage.pkg to start the download.

Once the download has completed, you need to take extra steps to install it - **do not double click to open it**.

Go to the Finder app, click on Downloads, locate Carthage.pkg. Hold down the Control Key on the keyboard and single click on Carthage.pkg. This will bring up a menu of choices, select Open from the menu and then Open (greyed out) again from the pop up box.  Then run through the install process.  You will need to enter your password. **The password is your computer's password.** Once installation completes, you can discard the Carthage.pkg when prompted.

If you need more help with this, this external link to the [Loop and Learn website](https://www.loopandlearn.org/carthage-0-36-0/#carthage-install) has some graphics to assist in this step.
