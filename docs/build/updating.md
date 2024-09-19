## Overview

**This page is only relevant when building with a Mac and Xcode.**

**For Browser Build, please see: [Update/Rebuild with Browser](../browser/bb-update.md){: target="_blank" }**

> Regardless of build method, this is an **update** and will install over your existing app; your **settings are maintained including your current CGM and Pump.**

!!! info "Time Estimate"

    - 25 minutes, if Xcode and macOS are already updated to support the current or desired iOS
    - up to 2 days, if need to install macOS and / or Xcode update(s)

!!! abstract "Summary"

    Summary of tasks to prepare for and update your app:

    * Determine required macOS and Xcode version based on your phone iOS
        * If necessary, update first macOS and then Xcode
    * Check your Developer Account
    * Download Updated Loop code and Build Loop

    In each of the sections below, follow links to sections of other build pages then hit the back button on your browser to return to this page.

!!! question "FAQs"

    - **"What is an update?"** Anytime you want to change versions or if the app is about to expire, follow the instructions on this page.
    - **"Do I delete my old Loop app first?"** Definitely **not**! If you keep your Loop app on your phone, your Loop settings (and existing pod) will continue to work the same after the update. Seamless.
    - **"Do I need to start a new pod when I update?"** No. Your existing pod session will continue seamlessly if you are using the same Developer Account to sign the Loop app targets as you did the last time you built.
    - **"What if I'm using a new/different developer account?"** If you aren't building with the same developer account used when your existing app was built (this includes going from free to paid), then you will be installing a brand new (second) Loop app on your phone. Your existing pod won't work with the new app, so you might want to time this transition when you are due to change pods. Delete the old app once you get the new one all set up.
    - **"What if it is a new computer but the same developer account?"** No big deal...use the Updating Steps to check that your new computer has the required compatible versions and then build your app. This will include installing Xcode, configuring Xcode Settings, and adding your Developer ID to Xcode: refer to [What about a New Computer?](#what-about-a-new-computer).

## When to Update Loop

Under ordinary circumstances, you do not *have to* update your Loop app until it expires (1 year for a paid account). However, we encourage regular updates when a new version of iOS, or of Loop, is released because they often contain bug fixes or improvements which may increase operational stability.

### iOS Updates

Under ordinary circumstance, updating the iOS on your phone does not require a rebuild of the app on your phone. However, it's important to be prepared in case of an emergency, such as a lost phone.

!!! abstract "Best Practice"

    It is good practice to first check if your computer (macOS or Xcode) will require an update to support building Loop to your phone BEFORE applying an iOS update to your Looping phone.

    Follow these "safe Looping" steps for updating your iOS:

    1. Check which [version of macOS and Xcode](xcode-version.md#how-do-all-the-minimum-versions-relate-to-each-other) is required for the phone iOS you intend to install.
    1. [Update macOS / Xcode if needed](#macos-and-xcode-versions)
    1. Check [Loop: Current Release](../version/releases.md#current-release) status - if there is new code, you should download it
    1. Build app to your iPhone
    1. Then update your iPhone iOS

[Loop Releases](../version/releases.md#loop-releases){: target="_blank" } provides information about current and previous Loop versions.

Updating to iOS 16 (watchOS 9 or newer) requires enabling [Developer Mode](build-app.md#developer-mode){: target="_blank" }. Your existing app will not open until you take this step. Once enabled, the app opens again. A rebuild is **not** required.

### "Loop" is No Longer Available

The apps built and signed by you in Xcode with a paid developer account will last for 12 months; then they expire and must be rebuilt. At least once per year you will have to rebuild your app and go through this update process. If you do not update and the "provisioning profile" on your phone expires, you will see the "Loop" is No Longer Available message. You will be given multiple [Loop App Expiration Notifications](../operation/features/notifications.md#loop-app-expiration-notification){: target="_blank" } on the Loop phone, but might miss them if you are a caregiver.

When you see "Loop" is No Longer Available on your phone, the only solution is to rebuild the app.  All of your settings are still present on your phone, but your "provisioning profile" expired and you need to generate a new one. Once you build Loop on your phone, following the instructions on this page, all your settings will be maintained - assuming you build with the same [Apple Developers ID](../faqs/loop-faqs.md#what-happens-when-i-switch-apple-developer-id){: target="_blank" } that was used initially.

## macOS and Xcode Versions

### Determine Required Xcode and macOS Versions

Between Loop app builds, there's a high likelihood that Apple has updated one or more of the systems involved in your Loop app. If you don't have the minimum Xcode version required for your phone iOS, you cannot build on that phone. Sometimes you must also update the macOS version to allow you to use the required Xcode version.

Based on the iOS on your phone, or the iOS you plan to install on your phone, determine the required macOS and Xcode versions. Click on this  link [versions for iOS, macOS and Xcode](xcode-version.md#how-do-all-the-minimum-versions-relate-to-each-other){: target="_blank" } to determine the versions needed and then hit the back button in your browser to finish the steps on this updating page.

If you are tired of the macOS and Xcode version update requirements, check out the [Build with Browser](../browser/bb-overview.md){: target="_blank" } option.

!!! warning "First macOS and Then Xcode"
    Your macOS must meet the minimum requirement for the Xcode version you need to support your current iOS as detailed in that link above.

    * If the macOS is too old, the Xcode version will not appear in the App Store
    * You might think you don't need to update Xcode (but you do)
    * Your build will fail and mentors might need to help you

    Don't be that person. Follow the directions.

Minimum means you need to have at least that version - newer versions build just fine.

### Verify / Update macOS

* Click on this link [Check your macOS Version](computer.md#check-your-macos-version){: target="_blank" } and follow the instructions on that page if an update is required.
* After you've reviewed that section, hit the back button on your browser to return here

### Verify / Update Xcode

Click on this link [Check your Xcode Version](xcode-settings.md#xcode-version){: target="_blank" } to find your Xcode version number.

If you need to update your Xcode, follow the instructions at this link [Install Xcode](xcode-version.md#which-version-of-xcode-do-i-need){: target="_blank" } and continue through [Xcode Settings](xcode-settings.md).

Advanced users: If you are finding installation of Xcode from the App Store incredibly slow, try the alternate method of [Direct Download of Xcode](#direct-download-of-xcode).

!!! warning "Direct Download"

    - If you previously did a direct download of Xcode, it might not show up in the App Store.
    - Either do another direct download or follow these directions in the Direct Download section to reconfigure so it will show up in the App Store.
        - [Direct Download of Xcode](updating.md#direct-download-of-xcode)

#### What about a New Computer?

Make sure your new computer has the macOS and Xcode required by your phone iOS. Be sure Xcode [Command Line Tools](xcode-settings.md#command-line-tools){: target="_blank" } are installed and that you [Add Apple ID](xcode-settings.md#add-apple-id) to Xcode.

#### Missing Xcode or Command Line Tools

!!! warning "WARNING"

    If you fail to have [Xcode](xcode-version.md) or [Xcode Command Line Tools](xcode-settings.md) installed, you will get one of these errors (or something similar) when you attempt to run the Build Select Script:

    * xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun
    * xcrun: error: active developer path ("/Applications/Xcode.app/Contents/Developer") does not exist
    * xcode-select: Failed to locate 'git', requesting installation of command line developer tools
    * xcode-select: error: tool 'xed' requires Xcode
    * Scripting Bridge could not launch application . . .

!!! abstract "Follow Xcode Settings page after updating Xcode"

        Make sure to restart your computer after updating Xcode and follow the instructions on the Xcode Settings page. There's a known issue that happens often enough to be frustrating if you skip those steps. It's not always required...but this is a good easy ounce of prevention step.

## Check your Developer Account

Apple updates its License Agreement for the Developer Program frequently. You need to login to your [developer account](https://developer.apple.com/account/){: target="_blank" } to manually check if there is a new agreement to accept.  If you see a big red or orange banner across the top of your Developer Account announcing a new license agreement like shown below...please read and accept it before building Loop.

![Screenshot: Account - Apple Developer](img/license.png)

## Ready to Build Loop

As long as there are no errors, you are now ready to proceed to [Build the Loop App: Developer Mode](build-app.md#developer-mode){: target="_blank" }

After building the new app, you may choose to return to this page and follow the instructions to [Delete Old Copies](#delete-old-copies). This is optional, but cleans up space on your computer.

## Delete Old Copies

This step is optional, but if your computer is low on space, it helps to clean up old downloads your are no longer using.

There is an easy way to do this. The Build Select Script used to download and build Loop provides Maintenance Utilities to help free up disk space.
    
Please review [Loop and Learn: Build Select Script](https://www.loopandlearn.org/build-select/){: target="_blank" } for more information.

Copy the line below that starts with `/bin/bash` by hovering the mouse near the bottom right side of the text and clicking the copy icon (should say `Copy to Clipboard` when you hover over it). When you click the icon, a message that says `Copied to Clipboard` will appear on your screen.

``` { .bash .copy title="Copy and Paste to start the Build Select Script" }
/bin/bash -c "$(curl -fsSL \
  https://raw.githubusercontent.com/loopandlearn/lnl-scripts/main/BuildSelectScript.sh)"
```

Paste the line of text into Terminal. Be sure to click anywhere in the terminal before trying to paste. (Ways to paste: ++command+"V"++ ; or ++control++ click and select from menu or `Edit`-`Paste` at top of Mac screen.)

* Please read what is on the screen as you progress
* Choose Option 3. Run Maintenance Utilities

If you prefer to clean up old downloads yourself, keep reading.

!!! abstract "Where is the old folder?"

    Assuming you used the Build Select Script, your downloads are in the ~/Downloads/BuildLoop folder as shown in the graphic below. If you are tight on space, the older folders can be deleted.  Best practice, download fresh and build Loop; and then go back and delete all but the most recent copy.  The nice thing about the Build Select script is it automatically generates the folder name with the date and time of the download. Delete each unwanted folder, one at a time.

    If you see a file (not a folder) in ~/Downloads/BuildLoop called LoopConfigOverride.xcconfig, keep that around. If you delete it, you'll need to recover it from the trash, regenerate it (if you know how) or sign your targets manually for your current download.

    The Scripts folder can also be left alone, but if you delete it, it is regenerated with the next use of the Build Select Script.

    ![Download folder with multiple Loop folders](img/loop-downloads.png)

## Background Information

New Loopers do not need to read the rest of this page.

Experienced Loopers may wonder what happened to deleting derived data.

* Each workspace folder has a unique folder for storing derived data
* Deleting derived data across all Xcode workspaces and projects for a brand new download is not required to ensure a year for a given build
* The Clean Derived Data option in the Utilities menu can be required for some special cases, but you probably won't need it

### Frequent Builder

If you build frequently, you do not have to delete the profiles every time. When the build script asks if you want to "Ensure a Year?", you can skip that step.

On the other hand, you may need to delete the provisioning profiles or saved Xcode information about a version of LoopWorkspace (or other app) currently on your computer. The maintenance utilities found in the BuildSelectScrip can be run to delete your provisioning profiles or clear derived data. Or you can use the individual commands in the next sections to do the same thing.

### Delete Provisioning Profiles

You can delete your provisioning profiles by copying this command and pasting it into any terminal. This does not affect any build you currently have on your phone - this just forces your current computer to generate a new one next time you build with *Xcode*.

* For those using *Xcode 16* or newer:

``` { .bash .copy title="Copy and Paste to manually remove Xcode 16 Provisioning Profiles on your computer" }
rm ~/Library/Developer/Xcode/UserData/Provisioning\ Profiles/*.mobileprovision
```

* For those using *Xcode 15* or older:

``` { .bash .copy title="Copy and Paste to manually remove Xcode 15 Provisioning Profiles on your computer" }
rm ~/Library/MobileDevice/Provisioning\ Profiles/*.mobileprovision
```

### Delete Derived Data

If you build using the same clone on your computer and then update that clone, sometimes you want to remove derived information that *Xcode* remembers and force it to start fresh.

First quit out of *Xcode*. The following command will delete all derived information for all your clones, so next time you build any app from an existing clone on your computer, the build will take longer. All dependencies will download again. So wait until you see the "indexing" indication on *Xcode* before trying to build.

``` { .bash .copy title="Copy and Paste to manually force Xcode on your computer to start fresh" }
rm -rf ~/Library/Developer/Xcode/DerivedData
```

### Revoke Certificate Issue

What does it look like if you run into the Revoke Certificate message? When you prepare to Sign the Targets with Xcode, you'll see the message highlighted in the figure below.

<br/>
![Screenshot: Xcode showing Revoke Certificate message](img/rejected-cert.svg){width="850"}
{align="center"}

More information is shown in the orange box below.

!!! warning "Revoke certificate"
    The important part of this message is:

    * ". . . signing certificate . . . private key is not installed in your keychain . . ."

    **WAIT - You might not need to revoke your certificate**

    1. You might get this if you logged in as a different user, have a new computer or if your computer had to undergo a factory reset
        * You can transfer your keychain to your new computer (or just revoke and keep going)
        * To transfer your keychain, check this [Apple Documentation Link](https://help.apple.com/xcode/mac/current/#/dev8a2822e0b){: target="_blank" }
    1. Your version of Xcode is way out-of-date
        * Mentors have seen this with people trying to build with Xcode 11.4 or earlier
        * Update [Xcode](xcode-version.md) to the most recent version

    **If you revoke and keep going:**

    * If you do hit Revoke Certificate, you'll be given a new one
    * Even with the new certificate, your Apple Developer ID is not affected
    * You can re-build on the existing Loop app on your device(s) and maintain all your settings with the new certificate.

    Be aware that you will have to rebuild to every device that used the certificate you just revoked and if you have other apps built with this certificate, they will stop working too.


## Direct Download of Xcode

Many people find updating Xcode from the App Store to be incredibly slow - especially when a new version has just been released.  This method still takes time and enough space on your disk but is faster than going through the App Store.  Depending on your internet speed, this download can be done in about an hour. Then once it is downloaded, expect another fifteen minutes to several hours (depending on the speed of your computer) for the "xip" file to "expand".

The instructions do not hold your hand.

* Your macOS must be at the minimum version (or newer) to support the version of Xcode you're about the download
* You need to know how to log into your Apple Developer account and navigate those menus
* You need to know how to use Finder to navigate to Downloads
* You need to know how to drag the Xcode icon into your Applications folder (after download and expand completes)
* After you have done a direct download, the App Store will not show you updates
    - Either repeat the Direct Download or
    - Delete Xcode from Applications folder
        - Open the App Store and search for Xcode
        - Install fresh
        - After you use the App Store for a download, then Updates will show in the future

Here are the different steps you need to follow when doing the Direct Download instead of the App Store method:

1. Open the [Apple Developer Download page](https://developer.apple.com/download){: target="_blank" }
    - You may need to login
    - Examine the menus (on my computer there are buttons across the top)
    - Click on Applications
    - Look at the available applications, which should include one or more Xcode version
    - Scroll down until you find the item you want (for example, Xcode 15.4 or Xcode 16)
    - Click on View Details and click on the Download button for the "xip" file
1. Wait for Download to complete
1. Expand the file by clicking on it in Finder
1. Move the Xcode icon to Applications after the expansion completes
1. Check the [Command Line Tools](xcode-settings.md#command-line-tools){: target="_blank" } setting under Xcode->Settings
    - The selection cannot be blank or Build-Script will fail to open Xcode automatically
    - It should be the same version as your Xcode
1. Reboot the computer
