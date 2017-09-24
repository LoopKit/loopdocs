# How to Update Loop

When a new version of Loop is released, you can click [HERE](https://github.com/LoopKit/Loop/releases) to read what features or fixes were a part of the new release. 

### Update Apple devices

!!!info "IMPORTANT INFO, PLEASE READ"
    Between Loop app builds, there's a high liklihood that Apple has updated one or more of the systems involved in your Loop app; your Apple Developer license agreement, your iPhone's iOS, your computer's macOS, your Xcode app, and/or your watchOS.  <u>If you don't install the updates, you will run into build problems.</u>  You can check for macOS and Xcode updates using the App Store link under the apple logo in your computer display's upper left corner.</br></br>
        * [Check your Apple developer account](http://developer.apple.com) and accept any updated license agreements.</br>
        * Update to macOS Sierra on your Apple.  Currently you will need macOS 10.12.6 at a minimum.</br>
        * Update to Xcode 9 </br>
        * Update your iPhone (iOS 10.3.3 at least), or if you use an Apple watch you'll need iOS 11 and watchOS 4.</br></br>

!!!warning "Special note about upgrading to Loop v1.5 for existing Loopers"
    If you are an existing Looper encountering this error message below while trying to update to Loop v1.5, please open your Terminal app found in the Applications>>Utilities folder and then enter `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`  Confirm the homebrew installation by pressing enter, and then typing in your computer password.  When the installation finishes, use the command `brew link --overwrite carthage`.  After those two steps, you can close out Terminal app, return to Xcode and press the build/play button again.  This error is a legacy for people who installed carthage using the carthage.pkg option (the primary installation method on the old docs)...installing homebrew with these directions will resolve the conflict between carthage installations.
    <p align="center">
    <img src="../img/exit127.jpg" width="450">
    </p>

### Download new Loop source code

You can use these links to download new versions of the Loop source code:
</br></br>
<p align="center">
[Loop: Master branch source code](https://github.com/LoopKit/Loop/archive/master.zip)
</p></br>
<p align="center">
**OR**</br></br>
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

### Change Main App Bundle ID and Build

**<u>Follow the guide for installation as you did before, beginning [HERE](https://loopkit.github.io/loopdocs/build/installing/#install-loop-using-xcode) to navigate to your newly downloaded source code.</u>**

The most common error in updating a Loop app is to use a different MAIN_APP_BUNDLE_IDENTIFIER than you used in your original Loop build.  If you use a different MAIN_APP_BUNDLE_IDENTIFIER, your iPhone will have a brand new second Loop app and none of the settings from the original Loop app will carry over.  While some people use this technique intentionally, you will have to be aware that you cannot successfully loop with two different Loop apps actively running (opened) at the same time on the same iPhone.  So, you will have to make sure you double-tap the home button and up-swipe to close out any unused Loop apps that you don't need running.

If you **use the same MAIN_APP_BUNDLE_IDENTIFIER as you used in the first installation**, all your old settings will be preserved and you will not have to re-enter them.  If you can't remember what you used on your current Loop app, you can open your old Loop folder on your computer, click on the `Loop.xcconfig` file, and check what you used.  Alternatively, open your Loop settings, open the Issue Report and look for a line titled `appGroupName` that is within the RileyLinkDevice section of the Issue Report.  Your MAIN_APP_BUNDLE_IDENTIFIER is shown within that area.  **Don't forget to save your project after changing the MAIN_APP_BUNDLE_IDENTIFIER.**

<p align="center">
<img src="../img/app_group_name2.png" width="750">
</p></br>
<p align="center">
<img src="../img/app_group_name.png" width="400">
</p>

Add or redo any customizations, if needed.  These will not be carried over automatically from the old app.

Sign the four targets and rebuild.  If you get any build errors, please check [this section](https://loopkit.github.io/loopdocs/build/installing/#build-errors) for fixes.




