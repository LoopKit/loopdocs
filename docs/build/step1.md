# Step 1: Compatible Computer

!!! info "Time Estimate"
    - 5 minutes, if you have a Mac with Monterey macOS (12.x)
    - 30-60 minutes, if you need to install macOS updates

    Hint: OS stands for Operating System

!!! abstract "Summary"
    Your computer, iPhone and Xcode must have compatible versions to build Loop.

    * A summary list of [Compatible Versions](#compatible-versions) is found on this page with more detail in a later page

	If you are buying a Mac, chose one with Monterey (or newer) operating system and at least 256 GB (512 GB is better).


!!! question "FAQs"
    - **"Can I use a PC or Windows computer? I don't own an Apple computer."** Yes, you can. Please read this FAQ about using a [Virtual Machine](../faqs/FAQs.md#can-i-use-a-pc-or-windows-computer-to-build).
    - **"Can I borrow someone else's Apple computer?"** Please see this FAQ about [Borrowing a Computer](../faqs/FAQs.md#do-i-need-to-own-my-own-apple-computer).
    - **"How often do I need to use the computer?"** Computer access is required when
        * Initially installing the Loop app
        * Loop app expires (Annually for a paid account or weekly for a free account)
        * Updating to a newer Loop release
        * You do NOT need access to an Apple computer to update your phone iOS, troubleshoot or change Loop settings


If you have access to a computer with MacOS 12.0 or newer, you can skip ahead to [Check Space Available](#check-the-space-available).

## Compatible Versions

The minimum macOS depends on the iOS of your iPhone/iPod.  Monterey is **required** to build on any iPhone with an iOS version starting with iOS 15.4 and can be used to build Loop for **any** of the phone iOS versions listed below. Higher values of iOS might trigger the need for an update to macOS or Xcode. The [Loop and Learn Versions](https://www.loopandlearn.org/version-updates) page is brought up-to-date faster than LoopDocs.

* ** iOS 15.4 or newer**, the minimum macOS is Monterey (12.0)

* ** iOS 15 - 15.3.1**, the minimum macOS is Big Sur (11.3)

* ** iOS 14.5**, the minimum macOS is Big Sur (11.0)

If your macOS does not meet the minimum, check to see if you can [update your macOS](step1.md#check-your-macos)

If you are an **existing Looper with an older macOS**, [please see this warning](#older-operating-system-warning). Do not update your phone to iOS 15.


!!! warning "iOS Dictates Your Computer Needs"

    The more up-to-date you keep your phone iOS, the more up-to-date your computer and macOS needs to be to build Loop. A new build is required at least once a year. More information on iOS is in [Build Step 8: Download Xcode](step8.md#download-xcode).

Do not use any of the beta macOS versions. (If you don't know what that means, you aren't using one.)

## Check Your macOS Version

To find your macOS version, click on the Apple icon in the computer's upper left corner and select `About this Mac`. The graphic below highlights the macOS version with a red rectangle. Your computer can be a MacBook, iMac, macMini, etc... if it has the minimum required macOS version and enough storage.

If you do not have the required minimum macOS version, check the `Software Update` button on that screen to see if you can update.

![image showing macOS and system details](img/macos-12.svg){width="500"}

Apple says upgrading to macOS Monterey requires 26 GB of available storage.

## Check the Space Available

You need to have 50 GB free space in order to install Xcode in [Build Step 8: Download Xcode](step8.md). At the top of the menu on the graphic above, click on the Storage Tab highlighted with a red rectangle.

 To free up space, move things like photos to an external drive. The Xcode application cannot be run from an external drive.

If you are evaluating a used computer, it's best to have at least 256 GB total disk space (more is better).

## Which Macs Are Compatible with macOS Monterey?

Monterey is the best operating system for building Loop. You can install Monterey on the following:

* MacBook, early 2016 or newer
* MacBook Air, early 2015 or newer
* MacBook Pro, early 2015 or newer
* Mac Pro, late 2013 or newer
* Mac Mini, late 2014 or newer
* iMac, 2015 or newer
* iMac Pro, 2017 or newer
* get the full list from [Apple for Monterey](https://support.apple.com/en-us/HT212551)

## New Apple Computers

Many new Apple computers use the M1 or M2 chips, instead of Intel chips. These computers make building Loop extremely fast. With these computers, yßou need to [configure the terminal app for Rosetta](#configure-terminal-app-for-rosetta). This only needs to be done one time.

### Configure Terminal App for Rosetta

!!! abstract "New Apple M1 or M2 chip users: IMPORTANT STEP"

    If you have a new computer that uses an M1 or M2 chip, open the Terminal app using a "converter" app, called Rosetta.

    Go to the Finder app, click on Applications, then open the Utilities folder.  Locate the Terminal app but do not double click it to open a Terminal window. Instead, hold down the Control Key on the keyboard and single click on Terminal. This will bring up a menu of choices, select the "Get Info" option.

    ![menu tree for get info on terminal app](img/get-info.png){width="650"}

    In the informational window that appears, find the checkbox that says "Open using Rosetta". Check that box to allow the Terminal app to open using Rosetta when you double click on terminal in the future. Then close that informational window and proceed with the rest of the directions.

    ![terminal app selection for using rosetta](img/rosetta.png){width="450"}

## Older Operating System Warning

!!! warning "Check before Upgrading iPhone"

    If you built Loop with Catalina - DO NOT UPGRADE your phone to iOS 15 - FIRST upgrade to at least Xcode 13, build the app on your phone - THEN upgrade to iOS 15. Otherwise you will get the dreaded ["Loop" is no longer available](updating.md#loop-is-no-longer-available) and need to rush through the updating Loop steps.  (Your pod will continue delivering basal, but you will not be able to bolus.)


## Next Step: Compatible iPhone/iPod Touch

In Step 2, you will check if you have a [Compatible iPhone/iPod touch](step2.md).

