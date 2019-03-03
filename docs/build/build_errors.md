# Build Errors

There are two types of build errors that happen; yellow alerts and red alerts.  Yellow alerts will not cause a build to fail, and can generally be ignored.  Red alerts will have to be resolved before you can successfully build Loop app.

<font color="orange">**Yellow error alerts**</font> do not cause the build to fail, those are just warnings.  Occasionally, a Loop version may have some minor discrepencies that cause a yellow alert...but you can ignore those.

<p align="center">
<img src="../img/master-done.png" width="750">
</p>

<font color="red">**Red error alerts** </font> will have to be resolved before you can successfully build Loop app.  The most common cause of red alerts comes from being out of sync between the various parts of Apple's infrastructure (iOS, Xcode, Swift, watchOS, macOS) that are frequently updated.  For every update to iOS/Xcode, the volunteer Loop developers have to make changes to the underlying source code.  This takes time...so when Apple updates are pushed out, sometimes there may be a short period of time until the code is updated to match.  If you encounter a build error that is not listed below, please get on the Facebook Looped group or Gitter to let us know.

!!!info ""
    Before looking at the solutions below...please double click on your red error message to bring up additional information about your particular error message.  Merely seeing the title of the error code on the left column of Xcode is not necessarily enough information to discern what error is causing your build to fail.  And therefore, you need to look at the detailed message and find the matching error message in the sections below.
    
## Build Failed in frameworks

If you see a **Cartfile failure** and several other red errors (in particular saying there is "no such module 'LoopKit'"), double click on the Cartfile error message.  If it says that the build failed in one of the schemes, as shown in the screenshot below, then you need to open Terminal app.  You will use the command `cd ~/downloads/loop-master && carthage update`.  NOTE:  YOU MAY HAVE TO CHANGE THE COMMAND SLIGHTLY.  If your loop folder isn't named loop-master and instead is loop-master-2 or loop-dev or some other folder name...change the command to match your folder's actual name. 

</p>
<p align="center">
<img src="../img/exit-code-65.png" width="850">
</p>

Carthage update will take about 15 minutes to run successfully.  A successful carthage update will look like the following:

</p>
<p align="center">
<img src="../img/carthage-update-success.png" width="550">
</p>

Once carthage update has run successfully, you can return to Xcode and press the build button again.  Your project should build successfully.

If your carthage update fails, try opening Terminal app and running these commands to clear out your carthage cache and saved derived data in Xcode:

`rm -rf ~/Library/Caches/org.carthage.CarthageKit` and `rm -rf ~/Library/Developer/Xcode/DerivedData`

After running those commands, retry the `cd ~/downloads/loop-master && carthage update` (remembering to update the name of your Loop download folder, as needed).

IF there are still red errors and you post for help in Looped group or Gitter...**TAKE A SCREENSHOT of the whole Xcode screen after you double click on the red error message** (command-shift-space bar-4 will make a screenshot tool active and the screenshot will save to your desktop).  Or even better, copy and paste the "xcodebuild output can be found at..." log file that is listed in yellow/orange color in the carthage update screen.  You can get to that log file by copy and pasting the file path (in yellow) into your Finder >> Go >> Go to Folder.. Once you open that log file, you can scroll to the bottom of the file and there will be detailed information about why carthage update failed.

Please do not post without being able to provide detailed information.  It is very difficult to help troubleshoot based on vague "I have errors" information.

## Siri Capabilities

Error message: "Your development team does not support the Siri capability"

<p align="center">
<img src="../img/siri-error.jpg" width="750">
</p>

Solution: You need to customize your code to remove Siri capabilities when you are building Loop with a free developer account. See the Code Customization section [here](https://loopkit.github.io/loopdocs/build/code_customization/#disable-siri-capabilities) for directions.

## Pending Certificate Request

Error message: "You already have a current iOS Development certificate or a pending certificate request."

<p align="center">
<img src="../img/pending_certification_request.jpg" width="750">
</p>

Solution: This error message has just recently started to appear for some new Loop builders. To resolve the issue, please login to your Developer account at [developer.apple.com](https://developer.apple.com) and then click on "Certificates, Identifiers & Profiles".  Under that screen, you will see "Development" under the "Certificates" section in column on the left.  You will need to click on the certificates, and choose to "revoke" from the options that show after you click on the certificate. Confirm the warning message that will appear asking "Do you want to revoke the certificate?"

<p align="center">
<img src="../img/revoke1.png" width="750">
</p>

After you do that, return to Xcode and open up Xcode preferences.  Under the Accounts section of Preferences, click on the minus sign to delete your Apple ID.

<p align="center">
<img src="../img/account.png" width="650">
</p>

Re-enter your Apple ID (yes...add that account right back that you literally just deleted), return to your Loop's target signing areas in Xcode and your error message should have resolved itself now as a new certificate will have been issued and a provisioning profile should have been created automatically.

For double measure, you can verify that the iOS development certificates are all in good working order by clicking on your "Manage Certificates" in your Xcode Preferences, Accounts and viewing the iOS development Certificates.  You should have one for your account that has a clean status similar to the screenshot below.

<p align="center">
<img src="../img/verify_cert.png" width="650">
</p>

## Outdated Xcode
Error message: The error message may change over time and Xcode versions...currently if you use iOS 12 and have not updated to Xcode 10, you will receive the following errors when you try to build:

<p align="center">
<img src="../img/xcode10-update.png" width="750">
</p>

Solution: You will need to go to your computer's App Store and install the Xcode app update.

## Command Line Tools

Error message:  "**<u>Invalid active developer path (/Library/Developer/CommandLineTools)</u>**" or "**<u>unable to find utility "xcodebuild", not a developer tool or in PATH</u>**"

</p>
<p align="center">
<img src="../img/command-line-error-1.jpg" width="550">
</p>

</p>
<p align="center">
<img src="../img/command-line-error-2.jpg" width="550">
</p>

Solution: Go to your Xcode preferences and under the Locations tab, select "Xcode 10" in the dropdown menu for Command Line Tools.

</p>
<p align="center">
<img src="../img/command-line-error-3.png" width="550">
</p>

## Command CodeSign failed

Error message: "**<u>errSecInternalComponent,  Command CodeSign failed with a nonzero exit code</u>**"

</p>
<p align="center">
<img src="../img/errsecinternal.jpg" width="850">
</p>


Solution:  This error message has been more frequent lately, but I believe it is due to inadvertently saying "no" to allowing Keychain Access. Regardless the solution is as follows:

1. Close Xcode
2. Open your Keychain Access application (found in Applications within the Utilities folder, similar to where Terminal app is found)
3. In the upper left corner of keychain access, make sure you have the keychain `login` highlighted and then click the large lock icon above the keychains area (High Sierra users) or right-click the lock next to the `login` (Mojave macOS users).  Click the lock closed, and then click the lock to open it again. You will be prompted for a password.  Enter your computer admin password.  Close Keychain Access app.
</p>
<p align="center">
<img src="../img/keychain3.png" width="450">
</p>

</p>
<p align="center">
<img src="../img/keychain4.png" width="450">
</p>

4. Open your Loop project again in Xcode.
5. In the main Xcode menu (grey menu bar at the very top of your Apple display area), select the word `Product` and then select the option for `Clean`. (keyboard shortcut is shift-command-k)
6. Now try rebuilding your Loop app.  If you ever get prompted again to allow Xcode access to Keychain, make sure to Always Allow.

## Developer License Update
Error message: "**<u>The Apple Developer Program License Agreement has been updated,  In order to access certain membership resources, you must accept the latest license agreement.</u>**"

Solution: You'll need to log onto your developer account at [developer.apple.com](https://developer.apple.com/account/) and accept the latest license agreement.
<p align="center">
<img src="../img/license.png" width="750">
</p>

## Carthage update message

If you see a message about updating carthage version, open Terminal app and enter the following command `brew update && brew upgrade carthage`

</p>
<p align="center">
<img src="../img/carthage-update.jpg" width="850">
</p>

## Unrecognized arguments: --cache-builds

Error message: "**<u>Unrecognized arguments: --cache-builds</u>**"

</p>
<p align="center">
<img src="../img/cache-builds.png" width="850">
</p>

</p>
<p align="center">
<img src="../img/exit-code-1-cartfile.jpg" width="850">
</p>


Solution: Please open your Terminal app found in the Applications>>Utilities folder and then enter `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`  Confirm installation by pressing enter, and then typing in your computer password.  When the installation finishes, use the command `brew link --overwrite carthage`.  After those two steps, you can close out Terminal app, return to Xcode and press the build/play button again.


## Abort with Payload
Error message: "**<u>Abort with payload</u>**"  Your app will only open briefly with a white screen and then close, if you build with this error.
<p align="center">
<img src="../img/abort_payload.png" width="750">
</p>
Solution: This error message is caused by either

1. Saving Loop download folder into an iCloud mapped drive, or
2. Having a space in the name of your Loop download folder.

Rename the folder to have no spaces and/or move it back to the Downloads folder, then rebuild.

## Apple Watch: Loop app not appearing
Error: **<u>Apple watch app is not appearing</u>**.

Solution: Usually because you have not updated to watchOS prior to when you built Loop, or you didn't have your Apple watch paired at the time of building Loop.  Don't forget to open the iPhone's Watch app, select My Watch tab on the bottom left, scroll all the way down, and click `Install` for the Loop app listed at the very bottom under "available apps".

## Apple Watch: Loop app not installing
Error: **<u>The Loop app appears on the list of app available to install on the watch, but when you press "install", and it goes through the animation of filling in the circle while it's installing, but then at the end it just toggles back to saying "INSTALL"</u>**.

Solution:  Plug your iPhone into the computer and start Xcode.  On your watch, look for a prompt that says "Trust this computer".  Scroll down on the watchface and select the "Trust" button.  Now rebuild your Loop app in Xcode, but look for a pop-up message that warns you that the Watch isn't registered with the Developer portal.  Click on the "register" button that is in the pop-up window and proceed with the Loop app building again.

!!!info ""
    WatchOS 5 appears to be an issue for some users currently.  If your Loop app is not properly installing on your watch using watchOS 5, please reopen Loop in Xcode and change the deployment targets in the WatchApp and WatchApp Extension targets to a Deployment Target of 5.0.  Rebuild and your watch app should install properly.

<p align="center">
<img src="../img/watchOS-5.png" width="750">
</p>
