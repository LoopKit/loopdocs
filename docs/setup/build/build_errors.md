## Build Errors

### Yellow Error Alerts
**Yellow error alerts** do not cause the build to fail, those are just warnings.  Occasionally, a Loop version may have some minor discrepencies that cause a yellow alert...but you can ignore those.

<p align="center">
<img src="../img/master-done.png" width="750">
</p>

### Red Error Alerts
**Red error alerts** will prevent Loop from building on your phone, and you can read what the failure was.  The most common red error alerts are:

1. "**<u>The Apple Developer Program License Agreement has been updated,  In order to access certain membership resources, you must accept the latest license agreement.</u>**"  You'll need to log onto your developer account at [developer.apple.com](https://developer.apple.com/account/) and accept the latest license agreement.
<p align="center">
<img src="../img/license.png" width="750">
</p>
2. "**<u>Swift Language Version” (SWIFT_VERSION) is required to be configured correctly</u>** for targets which use Swift. Use the [Edit > Convert > To Current Swift Syntax…] menu to choose a Swift version or use the Build Settings editor to configure the build setting directly"  or also "Could not locate device support files.  This iPhone is running iOS 11, which may not be supported by this version of Xcode."  You will need to go to your computer's App Store and install the Xcode app update.
<p align="center">
<img src="../img/old_xcode.jpg" width="750">
</p>
<p align="center">
<img src="../img/old_xcode2.jpg" width="750">
</p>
<p align="center">
<img src="../img/update.jpg" width="750">
</p>
3. "**<u>Swift Compilier Error.  Module compiled with Swift 4.0 cannot be imported in Swift 4.0.2</u>**"  Xcode was recently updated to version 9.1, and the currently Loop master branch will produce this error message if you are building with Xcode 9.1.
<p align="center">
<img src="../img/xcode9_1.png" width="750">
</p>
You can build with the Loop's dev branch (the dev branch has the fix built in) or just perform the following steps, if building with master branch:
    * Close Xcode
    * Open Terminal App
    * Navigate to your Loop download by doing the command:
        `cd downloads/Loop-master`
        (or whatever you named your Loop folder...go check)
    * Now use the command:
        `carthage bootstrap`
        It will run for about 4-5 minutes and then show you a screen like below.
            <p align="center">
            <img src="../img/carthage-bootstrap.png" width="750">
            </p>
    * If during the run of `carthage bootstrap`, you instead see an error message like below:
                    </p>
                    <p align="center">
                    <img src="../img/exit-code-72.jpg" width="550">
                    </p>
                    Please go to your Xcode preferences, under the Locations tab, select `Xcode 9.1` under the Command Line Tools
                    <p align="center">
                    <img src="../img/command-line-tools.png" width="750">
                    </p>
    * Reopen your Loop project in Xcode, select your iPhone, and press the build button. You'll still see some yellow alerts, but those are fine.
            <p align="center">
            <img src="../img/yellow-update.png" width="750">
            </p>
4. "**<u>Swift Compilier Error.  Module compiled with Swift 3.1 cannot be imported in Swift 3.2</u>**"  Make sure your Xcode and Loop source code are updated (see item above). **Older Loop versions (older than v1.5) will not compile with the new Xcode 9 app.**
<p align="center">
<img src="../img/swift_errors.png" width="750">
</p>
5. "**<u>Embedded Binary Validation Utility.  error: Embedded binary's bundle identifier is not prefixed with the parent app's bundle identifier</u>**".  This error usually happens because you've used an incorrect syntax in the MAIN_APP_BUNDLE_ID (like adding an extension to it) or forgotten to save project after the MAIN_APP_BUNDLE_ID was changed (the save forces Xcode to update all the targets to use the Main App Bundle ID within their individual bundle names).  In any case however, usually this error is most easily solved by closing out your project, deleting the download folder, and starting with a fresh download of Loop app.  The next time you build, make sure to follow the directions carefully to use a MAIN_APP_BUNDLE_ID in the right format and press `command-s` to force Xcode to update the targets' naming scheme correction.
<p align="center">
<img src="../img/bundle_fail.jpg" width="750">
</p>
6. "**<u>Abort with payload</u>**"  Your app will only open briefly with a white screen and then close, if you build with this error.  This error message is cause by having your Loop folder either (1) saved into an iCloud mapped drive or (2) having a space in the name of your downloaded Loop source code folder.  Rename the folder to have no spaces and/or move it back to the Downloads folder, then rebuild.
<p align="center">
<img src="../img/abort_payload.png" width="750">
</p>
7. "**<u>Shell Script Invocation Error.  Command /bin/sh failed with exit code 127</u>**"  This error code is happening for Loopers updating to Loop who used carthage.pkg and don't have homebrew installed.  We have since updated the installation docs, so new users likely won't run into this error.  But, if you are an existing Looper encountering this error message while trying to update to Loop v1.5, please open your Terminal app found in the Applications>>Utilities folder and then enter `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`  Confirm installation by pressing enter, and then typing in your computer password.  When the installation finishes, use the command `brew link --overwrite carthage`.  After those two steps, you can close out Terminal app, return to Xcode and press the build/play button again.
<p align="center">
<img src="../img/exit127.jpg" width="450">
</p>
8.  **<u>Apple watch app is not appearing</u>**.  Usually because you have not updated to watchOS 4 prior to when you built Loop, or you didn't have your Apple watch paired at the time of building Loop.  Don't forget to open the iPhone's Watch app, select My Watch tab on the bottom left, scroll all the way down, and click `Install` for the Loop app listed at the very bottom under "available apps".