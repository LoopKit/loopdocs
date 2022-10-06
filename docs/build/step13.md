# Advanced Users Only

**Only build the dev branch if you're a developer/experienced user**

## About Loop-dev

Please read [What's going on in the dev branch?](../faqs/branch-faqs.md#whats-going-on-in-the-dev-branch) before deciding to test the dev branch.

- Note, the dev branch requires a minimum of iOS 14 on your device
- Once you install the dev branch on a device, you must delete the app to return to master (the released version), which means all settings will need to be entered in master and a new pod started
- The dev branch Loop user interface is updated - as an experienced Looper, you will notice the difference
- Updated documentation is a work-in-progress located under the [Loop 3](../loop-3/loop-3-overview.md) tab of LoopDocs

The development branch supports Omnipod DASH and many less experienced users want that capability. To assist these individuals, a special script (similar to build select) is provided.

!!! danger "Building Over Master"
    If you are building dev over Loop master (or FreeAPS), check your correction ranges on your current app before continuing. You must set the bottom of your correction range no lower than 87 mg/dl (4.8 mmol/L) or your new app will crash during onboarding. 
    
    If your app crashes during onboarding, [Customize the Code](code_customization.md#modify-the-guardrails) to change the minimum correctionRange value and rebuild to continue.

## Download Loop-dev

This page documents using a script, different from the usual Build Select script, to build the development branch of the app. If you have not previously built the released version of the app using the Build Select script as documented in [Build the Loop App](step14.md), you may find the documentation sparse.

* A new script has been prepared to assist building the development branch for Loop and FreeAPS
* This script downloads the development branch and then selects a specific commit that has been lightly tested

This is still code under development, so please pay attention to your app and report any unexpected behavior on [Loop Zulipchat](https://loop.zulipchat.com).

The commit is identified by a 7-digit alphanumeric code.  That code is appended to the folder name of the downloaded code under Downloads/BuildLoop.  You can use finder to view the folder name after the script completes.

When you run the script, the instructions inform you of the commit that will be built.

Copy the line below that starts with `/bin/bash` by hovering the mouse near the bottom right side of the text and clicking the copy icon (should say Copy to Clipboard when you hover over it). When you click the icon, a message that says “Copied to Clipboard” will appear on your screen.

```title="Copy and Paste to start the script to build a specific commit"
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/loopnlearn/LoopBuildScripts/main/BuildLoopFixedDev.sh)"
```

Paste the line into a Terminal window. Be sure to click anywhere in the terminal before trying to paste. (Ways to paste: CMD-V; or CNTL-click and select from menu or Edit-Paste at top of Mac screen.)

Read the screen (shown below).  Type 1 and return if you understand the warning and agree.

![paste the script line into terminal - agree to warning](img/bss-01-initial-message.svg){width="700"}
{align="center"}

* Please read what is on the screen as you progress.
* Adjust font size as directed if you have difficulty seeing the directions.

You must type 1 (as shown in the graphic above) and return to indicate you understand the warning.

The next graphic warns you about building a development branch. The date and commit number in the script might not match the graphic below. The values in the script will be updated at appropriate times. The date indicates when that commit was added to the branch.

![message about development branch commit](img/build-select-dev.svg){width="700"}
{align="center"}

Continue following directions with the script and wait for the download to complete. If you get errors, [review this section](step14.md#xcode-errors-with-build-select) of the directions for building the released code. Resolve the errors, if possible, then return to this page.

After the download step, the specific commit will be "checked out". Verify there are no errors and proceed.

## Signing Targets

The script helps you configure a permanent file used by Xcode to automatically sign all your targets.

The first time you use the script, you will be asked how you want to sign the targets. If you have previously run the script and configured your computer with your Apple Developer ID, this question will not be shown. Skip ahead to [Use Permanent LoopConfigOverride.xcconfig](#use-permanent-loopconfigoverridexcconfig).

The next question, as shown in graphic below, is whether you will (1) Enter Apple Developer ID or (2) Sign Manually.

* If you are building with a paid developers account, choose option 1, and skip ahead to [Create Permanent LoopConfigOverride.xcconfig](#create-permanent-loopconfigoverridexcconfig)
* If you plan to build to a simulator on your computer, choose option 2 and proceed with signing as described on the [Build Loop](step14.md#prepare-to-build) page
* If you are building with a Free option, choose option 2 then:
    * Review [Loop-dev with Free Account](#loop-dev-with-free-account)
    * Proceed with signing as described on the [Build Loop](step14.md#prepare-to-build)

![messages for choosing Apple ID or Sign Manually](img/build-dev-b-01-choose.svg){width="750"}
{align="center"}

### Loop-dev with Free Account

Yes you can build Loop-dev with the free account (Personal Team). There are some extra steps needed compared to the steps given for Loop 2.2.x on the [Build with Free Account](step14.md#free-account) section.

If you know your Personal Team ID, you can enter it as directed in [Signing Targets](#signing-targets) above, otherwise, do manual signing.

1. You must remove additional capabilities, the complete list is:
    * **Loop Target:** Push Notifications; Siri and **Time Sensitive Notifications**
    * **Watch App Extension Target:** Siri
1. Add the keyword `SIRI_DISABLED` to the LoopConfigOverride.xcconfig file
    * Examine the file and find the line that starts with `SWIFT_ACTIVE_COMPILATION_CONDITIONS = $(inherited)`
    * Insert the new keyword (separated by a space) anywhere after `$(inherited)` and before the slashes near the end of the line


### Create Permanent LoopConfigOverride.xcconfig

The following graphics show the messages for the first time the script is used on your computer.

If you see a message that starts with "The file used by Xcode to sign your app . . .", then skip ahead to [Use Permanent LoopConfigOverride.xcconfig](#use-permanent-loopconfigoverridexcconfig). You've already configured your file.


* Graphic 1 below shows:
    - User types 1 to use Apple Developer ID
    - User reads instructions for getting Team ID from the Membership page
       - The developer.apple.com web page is opened automatically when user is ready
    - User obtains ID
    - User enters ID in terminal

!!! note "Use Your Team ID"
    The Team ID entered in the graphics below is bogus - the script only checks that the entry is 10 characters long.

    Please follow directions and use your actual Apple Developer ID (the Team ID on the Membership page).

![messages for configuring the override file first time through](img/build-dev-b-01.svg){width="750"}
{align="center"}

#### First Use of Script, continued:

* Graphic 2 below shows:
    - The permanent file is automatically created
    - User is given an opportunity to review the file information

![messages for configuring the override file first time through](img/build-dev-b-02.svg){width="750"}
{align="center"}

User is then shown the [Final Messages](#final-messages)

### Use Permanent LoopConfigOverride.xcconfig

* Graphic 3 below shows:
    - The permanent file is detected, user gets a chance to review it

![messages for using the override file for subsequent use](img/build-dev-b-03.svg){width="750"}
{align="center"}

#### Final Messages

* Graphic 2 and 3 above showed:
    * The user is always told which web pages will be opened and that Xcode will be opened
    * Then they must hit return when they are done reading

With the Loop-dev version, there are fewer build steps because the targets should already be signed.

The final messages (not shown) inform you that you can rerun the script with an up-arrow / return, close the terminal window and provides an optional command to configure the terminal to be in the LoopWorkspace folder for the downloaded code.

* Wait until you've successfully built the app before closing the terminal
* The command of the form: `cd /<specific-to-you-and-your-computer>/Downloads/BuildLoop/<download-folder-name>/LoopWorkspace` can be useful for some specific actions; most people will not need this.

## Build Loop

### Plug in Your Phone

Refer to the graphic below. The messages in the terminal instruct you to:

* Unlock your phone
* (Optional) If you have an Apple Watch that has never had Loop on it
    * Make sure watch is paired, unlocked and on your wrist
* Plug Phone into the computer
    * If you have never "Trusted" this computer with these device(s), do so now
        * A screen will pop up on your phone (and watch) asking if you trust the computer
        * Select "Trust"
* Now you are ready to hit return in the terminal window

![script instructions for plugging in phone and trusting computer on phone and watch](img/build-dev-b-04.svg){width="750"}
{align="center"}

The final action of the script is to 

* Open a browser window displaying this section of LoopDocs
* Open Xcode

### Initial Xcode Screens

If you want to [Customize Loop](../build/code_customization.md), do it before you proceed with the build.


Refer to the GIF below:

* Frame 1:  Xcode screen opened by the script after a fresh download
    * **Wait for indexing to begin**
        * If you see messages about fetching symbols or resolving packages, please wait until you see the Indexing message as shown in the GIF below just to the left of the dashed-blue rectangle
        * Indexing makes finding text with Xcode faster; it does not need to complete before building
    * The red rectangle indicates where you will change Loop to Loop (Workspace)
    * The red x in the dashed-blue rectangle region indicates you need to fix a problem before building
* Frame 2: Inset shows the action needed to select Loop (Workspace)
* Frame 3: Loop (Workspace) selected but there's a red x in the dashed-blue rectangle region

![gif showing the initial xcode screens following fresh download](img/xcode-build-loop3-a.gif){width="750"}
{align="center"}

### Package Dependency Error

If there is no red x in the dashed-blue rectange region on your Xcode screen, skip ahead to [Start Build](#start-build) on this page.

Otherwise, tap on the red x in the dashed-blue rectange region:

* If your screen is similar to the figure below, perform the [Fix for Package Dependency](#fix-for-package-dependency) (repeated below - also found on Build Errors page)
* If you have a different error, search the [Build Error](build_errors.md) page

![gif showing the xcode screens with dependency error](img/xcode-build-loop3-b.svg){width="750"}
{align="center"}

### Fix for Package Dependency

1. Click on the folder icon (indicated by red square)
1. Hold down the Control-Key and click the `Package Dependency` row to display the dropdown menu (shown in the inset)
1. Select Resolve Package Versions from the dropdown menu
1. Once the package resolution completes, the red x should vanish and you can build as soon as the Indexing message appears

![package dependency solution](img/xcode-package-dependency-solution.svg){width="600"}

## Start Build

Refer to the GIF below:

* Frame 1: Package Dependency resolved (no red x)
    * Xcode is Indexing as seen in dashed-green rectangle region
        * Indexing makes finding text with Xcode faster; it does not need to complete before building
    * Click the "Play" button highlighted by red rectangle to start the build
* Frame 2: Build has started
    * Xcode is Building as seen in dashed-green rectangle region
* Frame 3: Build succeeded
    * App is running as seen in dashed-green rectangle region

At this point, you can unplug your phone and acknowledge the Xcode message: `Lost connection to the debugger on . . .`.  The square icon next to the play button goes away as soon as you unplug your phone from Xcode.

The Loop app on your phone closes (but does not quit) when you unplug the phone. Open the Loop app on your phone just to be sure.

![gif showing the xcode screens when building](img/xcode-build-loop3-c.gif){width="750"}
{align="center"}

## New to Loop-dev

If this is your first build with Loop-dev, please review these pages before you continue:

* First Build on this phone: [Onboarding](../loop-3/onboarding.md)
* Building Loop-dev over Loop 2.2.x or FreeAPS: [Experienced Looper Onboarding](../loop-3/onboarding.md#experienced-loopers)

### Carb Absorption Time Update

If you used earlier versions of Loop, please be aware that absorption times have changed.

!!! warning "Loop-dev Carb Absorption Times"
    Loop uses the absorption time for the carbs, along with your glucose readings, ISF and CR to recommend insulin dosing and estimate over time the carbs absorbed and carbs expected. See [Algorithm: Prediction](../operation/algorithm/prediction.md) for more details.

    * Loop-dev uses absorption times of 30 minute, 3 hours and 5 hours for the Candy, Taco, Pizza icons
        * Loop 2.2.x used 2 hours, 3 hours and 4 hours
    * The 30 minute (candy) time is for rapid acting carbs only

    If you selected the candy icon for a complex meal, you told Loop to expect your glucose to rise rapidly. When that rapid rise does not materialize, you may find Loop predicts an unexpectedly low glucose because the algorithm assumes something must be affecting your glucose downward in a strong way.

    If this happens to you, edit the carb entry to have a longer absorption time and Loop will recalculate the prediction.

## Update Loop-dev

While Loop-dev is under active test, you should update frequently.

When building frequently, it is optional to update your provisioning profile with every new build. If you want to always ensure one year, follow the steps for [Updating: Step 4a](updating.md#step-4a-delete-old-provisioning-profiles) to use a different script for this action.

Checking for updates every week is a good idea.  Also - subscribe to all the streams on [Loop Zulipchat](https://loop.zulipchat.com) to make sure you don't miss critical information.

You may choose to run the script each time you update. You can discard older versions of the download by using Finder and navigating to Downloads/BuildLoop. Only the most recent copy is required to build loop. Do not discard the Downloads/BuildLoop/LoopConfigOverride.xcconfig file - that is used to automatically sign your app so you can build.

You may prefer to use commands to fetch and pull the latest code without making a new clone.

!!! tip "Folder Name"
    If you decide to update code in the same folder, you should edit the folder name to remove the specific build commit appended by the script. 
    
    This is not required but may avoid confusion.

### Open a Terminal in LoopWorkspace Folder

Refer to the graphic below.  The Downloads folder in Finder is highlighted on the upper left. The full path to Loop.xcworkspace is highlighted along the bottom. Double clicking on that file opens Xcode; but some people prefer to use command lines in the terminal.

* Open Finder
* Navigate to Downloads/BuildLoop and look for your download by name and date
* Open that folder, for example, Downloads/BuildLoop/Loop-220803-1145
* Find the LoopWorkspace folder icon (dashed-blue rectangle)
* Hold down the CTRL key and click (or right-click) LoopWorkspace
* A menu appears - select `New Terminal at Folder` (near the bottom of the list)

This new terminal window is now in the LoopWorkspace folder needed to perform `git` commands needed to update your downloaded copy (clone) when new updates are made to the repository.

![how to use finder to find the correct download and open xcode](img/finding-loopworkspace.svg){width="750"}
{align="center"}

* Some users like to use [GitKraken](https://support.gitkraken.com/) to assist them (link takes you to a tutorial video).
* Some are comfortable with the command line git commands described on [here](loopworkspace.md#updating-loop-using-loopworkspace).

## Manual vs Automatic Signing

If you manually sign any of the targets, for example as an alternative way to get your Developer ID, the file in the Loop folder called `Loop.xcodeproj/project.pbxproj` is automatically modified to use that target name.

Once that happens, the feature that enables Xcode to use the `LOOP_DEVELOPMENT_TEAM` keyword in the LoopConfigOverride.xcconfig is no longer available.

To restore that capability, navigate in the terminal to the LoopWorkspace/Loop folder and issue this command:

```
git restore Loop.xcodeproj/project.pbxproj
```


## Remove carthage

!!! abstract "Completely Optional"
    This section is completely optional.

    It is only provided to assist those who installed carthage for Loop and want to remove it.

* You no longer need carthage, and can uninstall it from your system.

* You do NOT need to uninstall carthage - your choice. If you share the computer with someone else, make sure they don't need carthage.

First copy and paste this phrase into the terminal and hit return:

```
carthage version
```

* If the response gives you a version number, then carthage is installed - you can uninstall it if you choose

* If the response indicates, "carthage: command not found", you are done - it is no longer needed to build Loop-dev

If carthage is on your system, you can choose to remove it (completely optional with respect to building Loop with updated code).

Copy and paste the following line into the terminal window and hit return.  

```
rm -rf /usr/local/bin/carthage
```

!!! danger ""
    If the response says you don't have the privilege to do this - it is best to stop.

    * That means carthage was installed by another user - not you.
    * Check with them to make sure they don't require carthage on the computer.
    * The presence or absence of carthage no longer affects the build process for Loop - so it is fine to leave it on your computer.

Assuming the previous line did not give an error, then copy and paste this line into the terminal window and hit return to complete carthage removal:

```
sudo rm -rf /Library/Frameworks/CarthageKit.framework
```

You will be prompted for a password when you hit enter on the second line.   It is the same password you use in order to log into the computer.   It will not echo to the screen.
