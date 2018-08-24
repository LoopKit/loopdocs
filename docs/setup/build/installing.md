# Overview

The overall installation process is pretty simple.  Loop is written in code that is stored online; available for us to download for free.  In order to compile all that code into a useable app on your iPhone, we need to use a free Apple program called Xcode.  Xcode takes all that code & makes an app...but Apple is particular about apps and installation on devices.  So, in order to put this app on our iPhones, we have to enroll in Apple's Developer Program.  Once you enroll as a developer, you will be able to "sign" the Loop app in Xcode so that it will properly install onto your iPhone.

While all of this is straight forward...I'll tell you some hints upfront to save time.

* Check your watchOS, iPhone OS, macOS, Xcode first to see if they need updates.  Currently you'll need to have these versions (or newer) watchOS 4.3, iOS 11.1, macOS 10.13.4 High Sierra, and Xcode 9.4.
* Downloading Xcode can take hours depending on your internet connection speed.  You can do that ahead of time if you want to save yourself some waiting when you're ready to build.
* Apple watches need to be paired with the iPhone BEFORE the Loop app is built onto the phone in order to have the Loop on the watch, too.  If you pair a new Apple watch later, you'll have to rebuild the Loop app onto the iPhone again, before the watch will work with Loop functions.

## Setup your Apple Computer

### Verify macOS

You need to be running macOS High Sierra, at least version 10.13.4, so verify by clicking the apple logo in your computer display's upper left corner and selecting `About this Mac`.

<p align="center">
<img src="../img/macosx.png" width="450">
</p>

If your macOS is not High Sierra, click on the `Software Update` button and update to High Sierra.  If your computer is older than late 2009/2010 (depending on computer model), you may not be able to update to Sierra.  You can check High Sierra compatibility [here](https://www.apple.com/macos/how-to-upgrade/#hardware-requirements).

### Install Homebrew

Homebrew is a program that will allow us to install the needed packages to build Loop.  Open the Terminal application on your computer.  It is located in the Applications folder, and then look in the Utilities subfolder for the Terminal application.

* Copy and paste the line below into Terminal prompt.  Press return after you paste it in.

`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

* There will be a prompt asking if you want to continue.  Press return to continue, then it may prompt for your password.  Enter your computer user password (don't worry, Terminal app doesn't show keystrokes when you enter passwords, but it is still reading your typing).  Wait while the script does its thing...you’ll see info scroll by and then it will pause for awhile.  Eventually, it will be done and you’ll see something that says “Installation successful” and you’ll have a ready Terminal prompt again.

<p align="center">
<img src="../img/carthage.jpg" width="450">
</p>

You can close the Terminal application now.  You’re done with it.  You do not need to do these steps again for any subsequent Loop builds.


## Setup your Apple Developer Account

In order to build your own copy of the Loop app onto your iPhone, you will need an Apple developer account.  You will have two options for your individual account; free or paid.

If you decide to enroll in a **FREE** developer account, here's what you need to know:

1. Loop apps signed with a free developer team will expire after 7 days.  On the 7th day, your Loop app will simply turn white when you open it and then immediately close.  To rebuild the Loop app, you will have to find a computer and rebuild the app onto your iPhone again.  You cannot rebuild the app on day 5 (when it is convenient, for example)...hoping to reset the 7-day clock.  The app will still expire on the 7th day from when it was first signed and created.</br></br>
2. If you decide to switch to a paid account after trying out the free account, you will need to rebuild your Loop app with a new main app bundle identifier (this will make sense when you go through the rest of these instructions...just make a mental note for now) and sign with the new team name.

To activate enrollment in a free developer account, you simply need to add your Apple ID to the Xcode application's Preferences in the Accounts tab, as outlined in the Xcode section below.  (Note: The Apple ID you use to sign up for the developer account does not need to be the same Apple ID as the Looping iPhone uses, for example parent's installing Loop on kid's iPhone.  Typically for the developer account, use the Apple ID of the person who will be doing the Loop app building.)  You don't have to specifically go into the Apple Developer Program website to enroll...Xcode automatically amends your Apple ID to include the free developer signing.  Once you add your Apple ID, you will see a team name listed, like the screenshot below, with a `(personal team)` designation to indicate that is a free developer team.

<p align="center">
<img src="../img/free-enroll.png" width="650">
</p>
    
If you decide to enroll in a **PAID** developer account, here's what you need to know:
    
1. Loop apps signed with a paid developer team will last for a full year.</br></br>
2. The paid developer account is $99 per year and is default set to auto-renew annually.  You can change that selection in your developer account settings at any time.
3. If your household has multiple T1D Loop users, only one developer account is needed.  That one developer account can be used to sign multiple Loop apps.</br></br>

To activate a paid account, go to the [Apple Developer website](https://developer.apple.com/programs/enroll/) to sign-up for your individual account.  (Note: The Apple ID you use to sign up for the developer account does not need to be the same Apple ID as the Looping iPhone uses, for example parent's installing Loop on kid's iPhone.  Typically for the developer account, use the Apple ID of the person who will be doing the Loop app building.)   After you enroll, make sure you look for a confirmation email.  Apple says it can take up to 24 hours to confirm and setup a new Apple developer account, however some people have had the process only take minutes.  It can vary.

Periodically, Apple will update the license agreement for the Developer Program.  When that happens, you'll need to login to your developer account and accept the new license agreement before you can sign a new/updated Loop app again.


## Setup Xcode
Open the App Store application on your computer.  Search for Xcode and click on the link to download/install Xcode for free.  The most current version of Xcode is 9.4.1.  The file size is fairly large so expect about 45 minutes, or even multiple hours, to download depending on your internet speed.  You will need version Xcode 9.4 at least to build the current Loop app.  If you have a previous installation of Xcode, please make sure to check for updates first, before building Loop.

<p align="center">
<img src="../img/xcode1.png" width="450">
</p>

Once you have Xcode downloaded, open it from your Applications folder.  There may be a short delay as Xcode installs new Command Line Tools that the app uses.  Once Xcode is open and ready, we will start with adding your new developer account to Xcode.

!!!info ""
    IMPORTANT NOTES: Do not stop the installation of Command Line Tools, that is an important installation for Xcode to work properly.  Additionally, if you see a pop-up window later during this Loop building process asking for `Keychain Access`, answer `Always Allow`.  This will let Xcode have access to the signing certificates that it needs for your Apple Developer account.  You will have to enter a password to allow keychain access.  That password is the admin password for your computer.

Go to the Xcode main menu (top left of your screen) and select Preferences from the Xcode dropdown menu.  Then, click on the “Accounts” tab in the Preferences window and then press the `+` in the lower left corner to add an Apple ID account.

<p align="center">
<img src="../img/xcode_account.png" width="750">
</p>

If you are establishing a free developer account, you will simply enter your Apple ID in this section and Xcode will automatically create your free developer account. If you enrolled in the paid account, enter the Apple ID of the paid developer account.  If you never enrolled in the free account, you will not have a (personal team) showing.  The screenshot is what will appear if you have used both types of enrollment under the same Apple ID.

<p align="center">
<img src="../img/apple_id.png" width="750">
</p>

Finally, we are going to turn on Line Numbers to make some later steps in the build process easier.  Go to the "Text Editing" tab in the top of the Preferences window.  Click the box to show Line Numbers.

<p align="center">
<img src="../img/text_lines.png" width="750">
</p>

You are now done setting up your Xcode environment.  Great job!  You will not need to redo the account setup steps on any subsequent builds or updates of your Loop app.  Xcode will remember these settings.

## Download Loop Source Code

Next, you’ll need to obtain the Loop’s source code in order to build the app on your computer.  Click on ONE of the links below to download your Loop source code.  **We recommend Master branch source code be used to build your Loop.**

Master vs Dev?  What is the difference? The Loop source code resides in [GitHub](https://github.com/LoopKit/Loop) within a repository.  A repository is kind of like a project's bookshelf, holding various books versions (aka branches) of a project.  The master branch is considered a stable version.  Any new features or options are first tested in a dev (short for "development") branch of the Loop.  New or inexperienced users should not build from the dev branch of Loop.  So if you hear of "new features in dev", these are things that may be eventually merged into the master branch once any bugs are worked out.
</br></br>
<p align="center">
[Loop: Master branch source code](https://github.com/LoopKit/Loop/archive/master.zip)</br></br>
[Loop: Dev branch source code](https://github.com/LoopKit/Loop/archive/dev.zip)
</p></br>


!!!info ""
    IMPORTANT NOTES: Best practice is to leave your Loop source code in your Downloads folder.  If you store your Loop code a different folder than Downloads (such as your Documents folder or Desktop), make sure the specified folder is **not** an iCloud drive.  Storing your Loop code in an iCloud drive folder will prevent Loop from building successfully.  How do you know if a folder is an iCloud drive?  Check your System Preferences.  If your System Preferences for iCloud is set as shown below, your Documents and Desktop folders are iCloud drives and **NOT** appropriate places to save your Loop download.
    <p align="center">
    <img src="../img/icloud-drive.png" width="650">
    </p></br>
    Depending on your browser and settings, your Loop download may or may not automatically unzip.  If it does not unzip automatically, you can right-click on the zip file and choose to "Open With" Archive Utility.  This will create a blue folder called `Loop-master`.  HOWEVER, if you already have an existing `Loop-master` folder from a previous download, the name of the next download will be something like `Loop-master (1)`.  The problem with that folder name is that it contains a space...and spaces in the name will cause your Loop build to fail.  So, either delete old copies of Loop before downloading/unzipping or rename the folder(s) to ensure that NO SPACES are in the folder name.
    <p align="center">
    <img src="../img/folder-name.png" width="650">
    </p>


## Installing Loop using Xcode

Here’s where the fun really begins.  You’re about to build your Loop app.

Go to your Downloads folder, open the `Loop-master` folder (or whatever you named it...double check that the folder does not contain any spaces in the folder name, as described above), and double click on Loop.xcodeproj.

<p align="center">
<img src="../img/loop_code.png" width="750">
</p>

A warning may appear asking if you really want to open it, click Open.  Xcode will get itself organized and installed, this may take a few minutes.  The first time you load Xcode you may also be asked about allowing keychain access (and yes, always allow...if the window pops up).  Xcode will eventually open the Loop project...the first open of Xcode just takes a little longer than subsequent uses.

<p align="center">
<img src="../img/loop_open.jpg" width="450">
</p>

Once Xcode has finished indexing, the Loop project's various folders and files will appear in the far left column.  At the very top, click on the blue Loop main project folder.  Then click on the box in the middle screen to reveal the targets' column.  The four targets we will sign in the upcoming steps are now easily viewable.

<p align="center">
<img src="../img/target_view.png" width="750">
</p>

Connect your iPhone via cable to the computer, select your iPhone from the very top of the drop down list.  Your **<u>iPhone’s personal name</u>** should be at the top of the list.  Don't accidentally select the generic iOS simulators listed below your iPhone's name.  

!!!info "Helpful Tip"
    If your iPhone has a lock enabled, Xcode will not be able to install Loop app once your phone locks during the build progress.  Please temporarily disable the lock until you finish building Loop app.  Go to your iPhone Settings >> Display & Brightness >> Auto-Lock and set it to `Never`.  You can reset your lock once Loop is done building onto the phone.

<p align="center">
<img src="../img/select_device.png" width="750">
</p>

<p align="center">
<img src="../img/your_device.png" width="750">
</p>

!!!info ""
    These next steps are usually only needed on the first Loop build; they can be skipped on subsequent builds.
    
    * If this is the first time your iPhone has been plugged in to this computer, you will need to open the iPhone and select "Trust this Computer" before your device will be useable in the menu selection.</br></br>
    * If this is the first time you are building an app onto this iPhone using this particular Apple developer account, you will need to “register the device” to your developer account.  The device registration screen, as shown below, may appear when your iPhone is selected.
    <p align="center">
    <img src="../img/device1.png" width="450">
    </p>
    <p align="center">
    <img src="../img/device2.png" width="450">
    </p>
    <p align="center">
    <img src="../img/device3.png" width="450">
    </p>

Once you select your device (your iPhone's name), let's start signing our four targets.  We will start with the Loop target, the first one on the target list.  Under the "Signing" area, select the dropdown menu where it currently says "none".  Choose your team that you'd like to sign with.  If you select a team name with (personal team), your app will expire after 7 days.  If you select a team name without that (personal team), your app will last a full year.  If you never signed up for a free developer account, you will not have a (personal team) showing.  Make sure you keep the "automatically manage signing" box checked above the team selection area.

<p align="center">
<img src="../img/team.png" width="750">
</p>

Once you choose your signing team, Xcode will automatically generate provisioning profiles and signing certificates.  If this is the first time you are building on this iPhone with this developer account, you may again be prompted to register the device.  Simply click on the "Register Device" button to confirm.

<p align="center">
<img src="../img/register_device.png" width="750">
</p>

A successfully signed target will have a provisioning profile and signing certificate similar to the screenshot below.  Click on each of the three remaining targets, and repeat the signing steps by choosing the same team name as you selected in the first target.

<p align="center">
<img src="../img/success.png" width="750">
</p>

!!!info "Do you want customizations before you finish building?"
    **New Loop users**: Customizations are not a required part of any Loop build.  As you gain experience in how you use your Loop app, you may want to customize some of the features.  You can always update your Loop app to add customizations at a later time.  Really though, building with the standard, default installation is JUST FINE.</br></br>
    If you want any custom configurations to your Loop or Watch apps, now is the time to make them before you finish with the last step of Loop installation on your iPhone.  Follow the step-by-step instructions on the [Code Customizations](code_customization.md) page.  When you’ve completed those customizations, please return here and follow the next steps to finish the installation of Loop.

!!!info "Have you paired your Apple Watch already?"
    **New Apple Watch users**: If you have an unopened Apple watch and want to use it with Loop, first pair the watch with the iPhone before continuing to the next steps.  If you get a new watch after building the Loop app, you'll need to redo your Loop build. (Don't worry, it's as easy as pressing play on your saved Loop project.)</br></br>
    **Existing Apple Watch users**: Please update your watchOS prior to building Loop app.  The current version of Loop requires watchOS 4 or newer.
    

All done with any customizations? Have your Apple watch paired and updated?  Let’s finish the installation of the Loop app onto your iPhone.  Double check to make sure your iPhone's name is still selected and then press the “play” button (or build button) to start Xcode on its way.  You’ll see the progression of the build in the status window.  New builds can take about 15-40 minutes depending on the speed of the computer and internet.  Just be patient.  Subsequent builds from the same download folder will be much faster.

<p align="center">
<img src="../img/build_button.png" width="750">
</p>

If the build is successful, your brand new Loop appswill have a screen open immediately on the iPhone asking about allowing Loop notifications and Health App access. Allow Loop to send you notifications. In the next screen that follows that, click on the `Turn All Categories On` line and then click `Allow` in the upper right corner.</br></br>

!!!warning ""
    **If you encountered any build errors that prevented your Loop from installing on your phone, please review the [Build Errors](build_errors.md) page.  Read your error message(s) and follow the directions for repairing the error.**

**First time builders:** If this is the first time you have installed an app on your iPhone using your Developer Account, you may get a warning like below.  Just follow the directions in the warning for what you need to do in your iPhone settings, and the issue resolves very quickly.  Click ok and you can safely disconnect your iPhone from the computer.  (If you don’t get a warning and the Loop app installs but does not open, you may still need to go to Settings->General->Device Management and enable trust for your Developer Account.)

<p align="center">
<img src="../img/trust_device.jpg" width="750">
</p>

!!!info "CONGRATS!  YOU JUST INSTALLED LOOP!"
    While the Loop app has been built...you are not done with these docs yet.  There are valuable pieces of information you will need to read in order to get, and keep, your Loop working.  Please continue on with the Loop App Setup section of these docs.
    
!!!warning "STOP...did you read that blue box above?"
    **Are you tempted to just start pushing buttons in Loop since it looks so easy?  PLEASE read about the Loop App Setup. There are four sections: [Loop settings](/setup/loop-settings/settings.md), [Loop services](/setup/loop-settings/services.md), [RileyLink menu](/setup/loop-settings/rileylink_menu.md), and [Pump setup](/setup/loop-settings/pump.md).  All of them have very valuable information to read.**




