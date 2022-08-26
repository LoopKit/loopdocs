# Updating Loop

!!! info "Time Estimate"

    - 25 minutes, if Xcode and macOS are updated
    - up to 2 days, if need to install macOS and / or Xcode update(s)

!!! abstract "Summary"

    Follow links to sections of other build pages then hit the back button on your browser to return to this page. These are the steps you should follow:

    * Step 1: Install macOS and Xcode updates based on your phone iOS
    * Step 2: Check your Developer Account
    * Step 4a and 4b: Delete provisioning profiles and derived data
    * Download Updated Loop code and Build Loop

!!! question "FAQs"

    - **"What is an update?"** Anytime you want to change versions or if the app is about to expire, follow the instructions on this page.
    - **"Do I delete my old Loop app first?"** Definitely **not**! If you keep your Loop app on your phone, your Loop settings (and existing pod) will continue to work the same after the update. Seamless.
    - **"Do I need to start a new pod when I update?"** No. Your existing pod session will continue seamlessly if you are using the same Developer Account to sign the Loop app targets as you did the last time you built.
    - **"What if I'm using a new/different developer account?"** If you aren't building with the same developer account used when your existing app was built (this includes going from free to paid), then you will be installing a brand new (second) Loop app on your phone. Your existing pod won't work with the new app, so you might want to time this transition when you are due to change pods. Delete the old app once you get the new one all set up.
    - **"What if it is a new computer but the same developer account?"** No big deal...use the Updating Steps to check your new computer has the required compatible versions and then build your app. This will include installing Xcode and configuring Xcode preferences. There is no need to delete provisioning profiles on a branch new computer, but you can follow the steps if you prefer.

## When to Update Loop

Under ordinary circumstances, you do not *have to* update your Loop app until it expires (1 year for a paid account). However, we encourage regular updates when a new version of iOS, or of Loop, is released because they often contain bug fixes or improvements which may increase operational stability.

### iOS Updates

Under ordinary circumstance, updating the iOS on your phone does not require a rebuild of the app on your phone. However, it's important to be prepared in case of an emergency, such as a lost phone.

!!! abstract "Best Practice"

    It is good practice to first check if your computer (macOS or Xcode) will require an update to support building Loop to your phone BEFORE applying an iOS update to your Looping phone. 

    Follow these "safe Looping" steps for updating your iOS:

    1. Check which [version of macOS and Xcode](step8.md#how-do-all-the-minimum-versions-relate-to-each-other) is required for the phone iOS you intend to install.
    1. [Update macOS / Xcode if needed](updating.md#step-1-install-macos-and-xcode-updates)
    1. Check [Loop: Current Release](../faqs/release-faqs.md#current-release) status - if there is new code, you should download it
    1. Build app to your iPhone
    1. Then update your iPhone iOS

[Loop Releases](../faqs/release-faqs.md#loop-releases) provides information about current and previous Loop versions.

The apps built and signed by you in Xcode with a paid developer account will only last for 12 months before they expire and need rebuilding. So, at least once per year you will have to rebuild your app and go through this update process. If you do not update and the "provisioning profile" on your phone expires, you will see this message:

### "Loop" is No Longer Available

When you see "Loop" is No Longer Available on your phone, the only solution is to rebuild the app.  All of your settings are still present on your phone, but your "provisioning profile" expired and you need to generate a new one. Once you build Loop on your phone, following the instructions on this page, all your settings will be maintained - assuming you build with the same [Apple Developers ID](../faqs/FAQs.md#what-happens-when-i-switch-apple-developer-id) that was used initially.

!!! warning "iOS 15 Warning - Check Before You Update"

    DO NOT INSTALL iOS 15 on your phone without first [updating](#when-to-update-loop) Loop if the Xcode version used to build your Loop app is 12D or earlier - the Loop app will stop working and you will have to rebuild Loop.

    Follow this link, [Xcode version](../faqs/update-faqs.md#how-can-i-confirm-xcode-version-i-used), for instructions to determine what version was used when building the Loop app currently on your phone.

## Build Video

The Loop and Learn team prepared this [YouTube video](https://youtu.be/gddhljzsNkM) showing how to prepare for an update and build Loop Master. We recommend reading the written directions below before (and while) watching the video.

## Step 1: Install macOS and Xcode updates

### Determine Required Xcode and macOS Versions

Between Loop app builds, there's a high likelihood that Apple has updated one or more of the systems involved in your Loop app. If you don't have the minimum Xcode version required for your phone iOS, you cannot build on that phone. Sometimes you must also update the macOS version to allow you to use the required Xcode version.

Based on the iOS on your phone, or the iOS you plan to install on your phone, determine the required macOS and Xcode versions. Click on this  link [versions for iOS, macOS and Xcode](step8.md#how-do-all-the-minimum-versions-relate-to-each-other) to determine the versions needed and then hit the back button in your browser to finish the steps on this updating page.

!!! warning "First macOS and Then Xcode"
    Your macOS must meet the minimum requirement for the Xcode version you need to support your current iOS as detailed in that link above. 
    
    * If the macOS is too old, the Xcode version will not appear in the App Store
    * You might think you don't need to update Xcode (but you do)
    * Your build will fail and mentors might need to help you
    
    Don't be that person. Follow the directions.

Minimum means you need to have at least that version - newer versions build just fine.

### Verify / Update macOS

* Click on this link [Check your macOS Version](step1.md#check-your-macos-version) and follow the instructions on that page if an update is required.
* After you've reviewed that section, hit the back button on your browser to return here

### Verify / Update Xcode

Click on this link [Check your Xcode Version](step9.md#xcode-version) to find your Xcode version number.

If you need to update your Xcode, follow the instructions at this link [Install Xcode](step8.md#install-xcode) and continue through [Xcode Preference](step9.md).

Advanced users: If you are finding installation of Xcode from the App Store incredibly slow, try the alternate method of [Direct Download of Xcode](#direct-download-of-xcode). 

!!! warning "Direct Download"

    - If you previously did a direct download of Xcode, it will not show up in the App Store.
    - Either do another direct download or follow these directions in the Direct Download section to reconfigure so it will show up in the App Store.
        - [Direct Download of Xcode](updating.md#direct-download-of-xcode)

#### Missing Xcode or Command Line Tools

!!! warning "WARNING"

    If you fail to have [Xcode](step8.md) or [Xcode Command Line Tools](step9.md) installed, you will get one of these error when you attempt to run the build-select script (or something similar):

    * xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun
    * xcrun: error: active developer path ("/Applications/Xcode.app/Contents/Developer") does not exist
    * xcode-select: Failed to locate 'git', requesting installation of command line developer tools
    * xcode-select: error: tool 'xed' requires Xcode
    * Scripting Bridge could not launch application . . .


!!! abstract "Follow Xcode Preferences page after updating Xcode"

        Make sure to restart your computer after updating Xcode and follow the instructions on the Xcode Preferences page. There's a known issue that happens often enough to be frustrating if you skip those steps. It's not always required...but this is a good easy ounce of problem prevention.


## Step 2: Check your Developer Account

Apple updates its License Agreement for the Developer Program frequently. You need to login to your [developer account](https://developer.apple.com/account/) to manually check if there is a new agreeement to accept.  If you see a big red or orange banner across the top of your Developer Account announcing a new license agreement like shown below...please read and accept it before building Loop.

![Screenshot: Account - Apple Developer](img/license.png)

## Step 4a: Delete old provisioning profiles

!!! info ""

    Yes - we do know how to count - but we've changed the order of steps. A lot of links are used historically, so we try not to change the names of headers (and thus the links) unless it is absolutely necessary.

    **Steps 4a and 4b** are completed with this new method.

In order to ensure a full year of use for your Loop app, you need to delete any existing provisioning profile(s) from your computer. If you want to know more information before executing this step - or if you want to do it manually, read the [Background Information](#background-information).

### Build Select Utilities

The easiest way to delete the old provisioning profiles and clean up derived data uses the same build-select script that you will use for building.

#### Open Terminal

Go to the Finder app, click on Applications, then open the Utilities folder.  Locate the Terminal app and double-click Terminal to open a terminal window. The terminal window is very plain looking when you open it. That is normal.

If you happen to have Xcode open, go on and quit out of Xcode now.

#### Load the Paste Buffer

Copy the line below that starts with `/bin/bash` by hovering the mouse near the bottom right side of the text and clicking the copy icon (should say Copy to Clipboard when you hover over it). When you click the icon, a message that says “Copied to Clipboard” will appear on your screen.

``` title="Run the Build-Select script to Clean Profiles & Derived Data"
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/loopnlearn/LoopBuildScripts/main/BuildLoop.sh)"
```

Paste the line of text into Terminal. Be sure to click anywhere in the terminal before trying to paste. (Ways to paste: CMD-V; or CNTL-click and select from menu or Edit-Paste at top of Mac screen.)

#### Utilities

The expected script responses are shown in the list and graphics below.  Each graphic shows the number you are instructed to type to proceed - the words on this page also tell you what to type.  

- If you do not have Xcode and Xcode command line tools installed - you will get errors.
- If you have Xcode open, you may get errors.

![paste the script line into terminal](img/build-select-01.png){width="750"}
{align="center"}

Type 1 and return to acknowledge the warning.

![select utilities option](img/build-select-02.png){width="750"}
{align="center"}

Type 3 and return to select `Utilities`.

![select clean profiles and derived data option](img/build-select-03.png){width="750"}
{align="center"}

Type 3 and return to select  `Clean Profiles & Derived Data`. 

Once this completes, you should see this in your terminal.

![clean utility script completed](img/build-select-04.png){width="750"}
{align="center"}

### Step 4a Completed: No Errors

As long as there are no errors, you are now ready to proceed to [Build the Loop App: Download Loop](step14.md#download-loop) to build the released version of the app.


### Step 4a Had Errors

If instead, you saw something like:

* `rm: /Users/marion/Library/Developer/Xcode/DerivedData: Directory not empty`

This means it could not delete all the Derived Data folder because Xcode was open.

Please quit out of Xcode and repeat the steps from [Load the Paste Buffer](#load-the-paste-buffer).

---


## Background Information

The rest of this page is kept for historical reasons (and to maintain saved links).  If you followed the steps above, you do not need the rest of this page.

#### Delete Old Copies

When you update, you no longer need to keep old copies of the code on your computer. If you want to clean up space, you can delete those old folder(s) now if you want).

!!! abstract "Where is the old folder?"

    Maybe you don't remember where you put the folder. Both the older zip-download method and the new build-select-script method make folders in your download folder as shown in the graphic below. If you are tight on space, all of these folders can be deleted.  Or, if you are paranoid, download fresh and build Loop; and then go back and delete all but the most recent copy.  The nice thing about the build-select script is it automatically generates the folder name with the date and time of the download.

    ![Download folder with multiple Loop folders](img/loop-downloads.png)


#### Provisioning Profile Details

Older versions of Xcode used to automatically create a new "provisioning profile" as part of the Loop building process. That provisioning profile, among other things, sets the expiration date for your app. If you sign with a paid team, that profile is set to expire in 12 months. If you sign with a free team, that profile is set to expire in 7 days.

You can always check the expiration date immediately after a successful build of your loop app by clicking the little "i" icon next the "Provisioning Profile" line in the target signing area. Add 12 months to the "created" date (paid account), or 7 days (free account), and you'll have your app's date of future spontaneous death, which you can record in your calendar.

![Screenshot: Xcode showing Provisioning Profile](img/provisioning-profile-date.png){width="850"}
{align="center"}

Here's what started happening about September 2019 with Xcode 11, the provisioning profiles were being reused so the date was not updated each time you built. This change resulted in many people's apps expiring unexpectedly (and therefore dying suddenly) starting in September 2020 despite having updated/rebuilt recently and having current developer accounts (either manually renewed or automatically renewed, doesn't matter).

Once you follow the steps in the orange box below, Xcode will have no memory of the old provisioning profiles and will be forced to create a brand new one with the next Loop build. Therefore, you'll get a brand spanking new "created" date that will match the build date.  Simple and straight-forward. (Leave Terminal app open to do Step 4b afterwards too.)

#### Delete Profiles

- This process deletes the provisioning profiles on your computer to force Xcode to generate new ones with your next build
- This does not affect the provisioning profiles currently on your phone


!!! question "How to delete old provisioning profiles"
    - Find your Terminal app (in Applications under Utilities)
    - Open your Terminal app
    - Hover to right of text, click copy to clipboard, then paste it into the Terminal prompt and return

    ``` title="Delete Provisioning Profiles"
    rm ~/Library/MobileDevice/Provisioning\ Profiles/*.mobileprovision
    ```

    * No response will be shown in the terminal if you have Provisioning Profiles stored on this computer
    * If you do not have Provisioning Profiles stored on this computer, the message be similar to this one:
        * rm: /Users/marion/Library/MobileDevice/Provisioning Profiles/*.mobileprovision: No such file or directory

    ![Screenshot: terminal after provisioning profile deletion](img/empty-profiles.png){width="650"}
    {align="center"}

#### Infrequent Builder, App Expires soon

If your app will expire soon or you build infrequently, then [Delete Profiles](updating.md#delete-profiles). Not sure when your app expires? Here are instructions to check your [Loop Expiration Date](https://www.loopandlearn.org/loop-expiration-date/).

#### Frequent Builder

If you build frequently, you do not need to delete the profiles every time. One user reported deleting profiles gave a [Revoke Certificate](updating.md#revoke-certificate-issue) message - follow the link to see other reasons why that might happen.

#### Revoke Certificate Issue

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
        * To transfer your keychain, check this [Apple Documentation Link](https://help.apple.com/xcode/mac/current/#/dev8a2822e0b)
    1. Your version of Xcode is way out-of-date
        * Mentors have seen this with people trying to build with Xcode 11.4 or earlier
        * Update [Xcode](step8.md) to the most recent version

    **If you revoke and keep going:**

    * If you do hit Revoke Certificate, you'll be given a new one
    * Even with the new certificate, your Apple Developer ID is not affected
    * You can re-build on the existing Loop app on your device(s) and maintain all your settings with the new certificate.

    Be aware that you will have to rebuild to every device that used the certificate you just revoked and if you have other apps built with this certificate, they will stop working too.


#### Clean cache and derived data

This may not be necessary, but it is one of the first steps to try if you do get a build error. Since you already have Terminal app open, you can prevent one of the possible sources of build errors in advance by cleaning out straggler data from previous Loop builds.

!!! abstract "Clean cache and derived data"

    Using Terminal app that should still be open from Step 4a, hover to right of text, click copy to clipboard, then paste it into the Terminal prompt and return.

    ``` title="Clean cache and derived data"
    rm -rf ~/Library/Caches/org.carthage.CarthageKit
    rm -rf ~/Library/Developer/Xcode/DerivedData
    ```

    * No response will be shown in the terminal if Xcode is closed or you have never built from this folder
    * If you have previously built the app from this folder AND Xcode is open, you will get message(s) similar to this
        * rm: /Users/marion/Library/Developer/Xcode/DerivedData/ModuleCache.noindex: Directory not empty
        * rm: /Users/marion/Library/Developer/Xcode/DerivedData: Directory not empty




    ![Screenshot: terminal after clean cache and derived data](img/cleaned-terminal.png){width="650"}
    {align="center"}

#### Build like normal

You are ready to proceed to [Build the Loop App: Download Loop](step14.md#download-loop) and continue on that page until you have completed the build.

!!! info "Add a Calendar Reminder"

    - It is good practice to add a reminder to your calendar when the app will expire (7 days or 1 year).
    - Be sure to add an alert to that reminder so you have enough time to do all the [Loop Updating](updating.md) steps to build the app again before it expires


!!! abstract "Double check expiration date"

    If you want to make sure that step 4 above (deleting the provisioning profiles) went well, check the "created" date on your provisioning profile after you sign your Loop target for this rebuild. It should have the current date as the "created" date and your Loop app, if you successfully build, will function for 12 more months (for paid accounts) so long as you keep your developer account paid/automatically renewed.

    To find out expiration date later, read [Loop App Expiration Date](../operation/features/notifications.md#loop-app-expiration-date).


#### Resolve Build Errors if needed

!!! danger "Check Build Errors Page"

    If you get a build error, check the [Build Errors page](build_errors.md). You might be able to resolve it yourself.

    Even if your exact error isn't there, the information you need to provide when asking for help is listed on that page. And that information is critical to allow mentors to help troubleshoot your build error.

## Direct Download of Xcode

Many people find updating Xcode from the App Store to be incredibly slow - especially when a new version has just been released.  This method still takes time and enough space on your disk, but is faster than going through the App Store.  Depending on your internet speed, this download can be done in about an hour. Then once it is downloaded, expect another fifteen minutes to several hours (depending on the speed of your computer) for the "xip" file to "expand".

The instructions do not hold your hand.

* Your macOS must be at the minimum verion (or newer) to support the version of Xcode you're about the download
* You need to know how to log into your Apple Developer account and navigate those menus
* You need to know how to use Finder to navigate to Downloads
* You need to know how to drag the Xcode icon into your Applications folder (after download and expand completes)
* After you have done a direct download, the App Store will not show you updates
    - Either repeat the Direct Download or
    - Delete Xcode from Applications folder
        - Open the App Store and search for Xcode
        - Install fresh
        - After you use the App Store for a download, then Updates will show in the future

Here are the different steps you need to follow doing the Direct Download instead of the App Store method:

1. [Login to your Apple developer account](https://developer.apple.com/account)
    - Examine the menus (on my computer there are buttons on the left hand side)
    - Click on Downloads (under Additional Resources)
    - Look at menu items (on my computer there are buttons at the top) that say Beta, Release, Profiles and Logs, and More
    - Click on More
    - Scroll down until you find the item you want (for example, Xcode 13)
    - Click on View Details and click on the Download button for the "xip" file
1. Wait for Download to complete
1. Expand the file by clicking on it in Finder
1. Move the Xcode icon to Applications after the expansion completes
1. Check the [Command Line Tools](step9.md#command-line-tools) setting under Xcode->Preferences
    - The selection cannot be blank or Build-Script will fail to open Xcode automatically
    - It should be the same version as your Xcode
1. Reboot the computer
