# How to Update Loop

When a new version of Loop is released, you can click [HERE](https://github.com/LoopKit/Loop/releases) to read what features or fixes were a part of the new release. 

!!!info "Update macOS and Xcode before updating Loop"
    Between Loop app builds, there's a high liklihood that Apple has updated one or more of the systems involved in your Loop app; your Apple Developer license agreement, your iPhone's iOS, your computer's macOS, your Xcode app, and/or your watchOS.  If you don't install the updates, you will likely run into build problems.  You can check for macOS and Xcode updates using the App Store link under the apple logo in your computer display's upper left corner.</br></br>
        * [Check your Apple developer account](http://developer.apple.com) and accept any updated license agreements.</br>
        * Update to macOS Sierra on your Apple</br>
        * Update your Xcode app to at least v8.3</br>
        * Update your iPhone (iOS 10.3.3) and Apple Watch (watchOS 3.2.3)</br></br>


### Update your Loop app


* First you will need to download the current Loop version's zip file [HERE (for master branch)](https://github.com/LoopKit/Loop/archive/master.zip) or [HERE (for dev branch)](https://github.com/LoopKit/Loop/archive/dev.zip)

!!!warning ""
    If you have your browser preferences set to download to a different drive than Downloads, make sure the specified drive is **not** an iCloud drive.  iCloud drives can cause problems with the frameworks for the project and Loop may not build properly.  If you have your System Preferences for iCloud set as shown below, you should **NOT** download Loop source code to your Documents or Desktop.  Holding the control key while you click on the download link will allow you to choose a specific download folder.
    <p align="center">
    <img src="../img/icloud-drive.png" width="650">
    </p>

* Follow the guide for installation as you did before, beginning [HERE](https://loopkit.github.io/loopdocs/build/installing/#install-loop-using-xcode) to navigate to your newly downloaded source code.

* When you've opened the project in Xcode, choose `Product` from the Xcode top menu and then select `Clean`.  This will help clean out any legacy issues from previous builds.

* **Use the same MAIN_APP_BUNDLE_IDENTIFIER as you used in the first installation.**  If you can't remember it, you can open your old Loop folder on your computer and check.  Alternatively, open your Loop settings, open the Issue Report and look for a line titled `appGroupName`.  Save your project after changing the MAIN_APP_BUNDLE_IDENTIFIER.

<p align="center">
<img src="../img/app_group_name.jpg" width="400">
</p>

* Add or redo any customizations, if needed.  These will not be carried over automatically from the old app.

* Sign the four targets and rebuild.

!!!note ""
    If you use a different MAIN_APP_BUNDLE_IDENTIFIER than you previously used, Xcode will install a completely new Loop app.  This Loop app will need all your settings and configurations re-entered.  If you have two Loop apps installed on your iPhone, only one of them can be open and running at any given time; looping will stop with two apps open.  Loop is not designed to have multiple installations on one iPhone.

## Xcode Source Control and GitHub git
If you used git to locally clone your Loop source code, you will want to `cd` into your Loop repository on your local computer and `git pull https://github.com/LoopKit/Loop.git` to update your Loop repository.  Then you can navigate to the Loop.xcodeproj and update as described above.

