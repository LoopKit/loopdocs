# How to Update Loop

When a new version of Loop is released, you can click [HERE](https://github.com/LoopKit/Loop/releases) to read what features or fixes were a part of the new release.

!!!info ""
    The process to update is very similar to the original building of Loop app, except you get to skip several of the first steps.  The basic steps are:

    * Update iOS, macOS, Xcode, or watchOS as needed
    * Download new Loop source code
    * Change the MAIN_APP_BUNDLE_IDENTIFIER
    * Save project
    * Add any customizations
    * Sign all four targets
    * Build app

### Update Apple devices

Between Loop app builds, there's a high liklihood that Apple has updated one or more of the systems involved in your Loop app; your Apple Developer license agreement, your iPhone's iOS, your computer's macOS, your Xcode app, and/or your watchOS.  <u>If you miss some of the updates, you may run into build problems.</u>  You can check for macOS and Xcode updates using the App Store link under the apple logo in your computer display's upper left corner.  Check below to make sure your equipment is running the minimum versions of the programs.</br></br>

* **macOS Sierra**: macOS 10.12.6 Sierra at a minimum, but High Sierra will work, too.</br>
* **Xcode**: Xcode 9.2 (if using iOS 11 or newer), Xcode 9 or newer (if using iOS 10.3.3) </br>
* **iPhone**: iOS 10.3.3 at a minimum, but iOS 11.2.5 is the most current and works well.</br></br>


### Download new Loop source code

You can use these links to download new versions of the Loop source code.  These links will always provide the most recent version of Loop:
</br></br>
<p align="center">
[Loop: Master branch source code](https://github.com/LoopKit/Loop/archive/master.zip)
</p></br>
<p align="center">
**OR**</br></br>
[Loop: Dev branch source code](https://github.com/LoopKit/Loop/archive/dev.zip)
</p></br>

FYI: The Loop source code resides in [GitHub](https://github.com/LoopKit/Loop) within a repository.  A repository is kind of like a project's bookshelf, holding various books (aka branches) of a project.  The master branch is considered a stable version.  Any new features or options are first tested in a dev (short for "development") branch of the Loop.  New or inexperienced users should not build from the dev branch of Loop.  So if you hear of "new features in dev", these are things that may be eventually merged into the master branch once any bugs are worked out.

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

**<u>You can follow the guide for installation as you did before, beginning [HERE](/setup/build/installing.md#installing-loop-using-xcode) to navigate to your newly downloaded source code.</u>**

**The most common error in updating a Loop app is to use a different MAIN_APP_BUNDLE_IDENTIFIER than you used in your original Loop build.**  If you use a different MAIN_APP_BUNDLE_IDENTIFIER, your iPhone will have a brand new second Loop app and none of the settings from the original Loop app will carry over.  While some people use this technique intentionally, you will have to be aware that you cannot successfully loop with two different Loop apps actively running (opened) at the same time on the same iPhone.  So, you will have to make sure you double-tap the home button and up-swipe to close out any unused Loop apps that you don't need running.

If you **use the same MAIN_APP_BUNDLE_IDENTIFIER as you used in the first installation**, all your old settings will be preserved and you will not have to re-enter them.  If you can't remember what you used on your current Loop app, you can open your old Loop folder on your computer, click on the `Loop.xcconfig` file, and check what you used.  Alternatively, open your Loop settings, open the Issue Report and look for a line titled `appGroupName` that is within the RileyLinkDevice section of the Issue Report.  Your MAIN_APP_BUNDLE_IDENTIFIER is shown within that area. 

<p align="center">
<img src="../img/app_group_name2.png" width="750">
</p></br>

<p align="center">
<img src="../img/app_group_name.PNG" width="400">
</p>

###  Save Project

**Don't forget to save your project after changing the MAIN_APP_BUNDLE_IDENTIFIER.**  Saving the project forces Xcode to update the individual bundle identifiers that are associated with the four targets.  If you don't save the project and Xcode doesn't update the bundle identifiers, you will get a build error.  SO...please remember to save project after you change your MAIN_APP_BUNDLE_IDENTIFIER.

### Add customizations

Add or redo any customizations, if needed.  These will not be carried over automatically from the old app.  Be sure to read up in the [code customizations section](/setup/build/code_customization.md) before building, as there may be new customizations available since the previous build.

### Sign Targets and Build

Sign the four targets and rebuild.  Nothing is changed here.  Just make sure to pick your paid developer team, if you have one.

### Build Errors

**If you get any build errors, please check [this section](/setup/build/build_errors.md) for fixes.**




