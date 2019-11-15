# Build Errors

There are two types of build errors that happen; they are yellow warnings and red alerts. You'll see the warnings and alerts in the left-hand column of the Xcode window.

<font color="orange">**Yellow warnings**</font> do not cause the build to fail, those are just warnings.  Occasionally, a Loop version may have some minor discrepancies that cause a yellow alert...ignore those. Do not try to do anything to fix those...leave them alone.

<font color="red">**Red error alerts** </font> will have to be resolved before you can successfully build the Loop app. The steps below explain how to resolve them based on the messages you are seeing.

## Start with the obvious error causes

Before you start trying to resolve your red errors...start with the most obvious things that can cause a red error message:

1. **DO NOT USE BETA VERSIONS**  If you are using an iOS beta version or an Xcode beta version, your Loop will not build. If you have Xcode beta, uninstall it and get regular Xcode. If you have iOS beta on your iPhone, you will need to restore your iPhone entirely. You can restore to either (1) the last non-beta backup version you saved or (2) restore as a new iPhone (default settings). Yes, deleting iOS beta is a pain...so don't install it in the first place.

2. **Did you check for updates?** Cannot emphasize this one enough...you should check for Xcode updates (and install them) before building.

3. **Did you reboot your computer after updating Xcode?** Yup...that was in the message on the Update Loop page...did you ignore it? ;)

4. **Get a fresh download of Loop code, don't just recycle an old download that you built with a long time ago.** That old version may not be compatible with new iOS and new Xcode versions.

5. If you are using a free developer account, you need to have finished the [removal of Siri capabilities](https://loopkit.github.io/loopdocs/build/step14/#sign-four-targets).

## Posting for help

STOP!!  Read this section! Important!

Before you post in Zulipchat or Looped Group asking for help with build errors, <u>do your work first</u>. The build errors listed below (and the obvious checks listed above) are very successful ***IF PEOPLE READ THIS PAGE***. The volunteer group of people answering questions in Looped and Zulipchat would love to spend more time on improving Loop in other ways than answering build error questions that can be answered by using this page as a first step.

Therefore, first use the error topics (listed in sections below) to try to resolve your build error yourself. Then, if you need to post for help because this page did not fix your problem, you'll need to include information with the post so we (the troubleshooters) know you read this page and where you are in your troubleshooting attempts

!!!danger "Must include in your post" 
    * The version of Xcode you are using
    * The version of Loop you are building with
    * The version of iOS on your Loop iPhone
    * Specify if you are using a free or paid account, and if free...confirm you deleted Siri capabilities
    * Confirm you are not using an Xcode beta or iOS beta version (so we don't have to ask, actually type "I am not using beta versions"...this will save a lot of time and hassle)
    * Screenshots of your WHOLE Xcode window and/or Terminal window showing your error and any messages you've seen while working through the build errors/solutions.
    * **<u>State which fixes from the below list that you have already tried AND post the screenshots of the results of those fix attempts.</u>**

Helpful tip: Shift-Command-4-spacebar will give you a screenshot tool that you can use to click on the Xcode window to grab a screenshot. The screenshot will save to your desktop so you can include it in your post. Phone photos of your computer screen won't likely be of sufficient clarity to read the needed information and often cuts off valuable information that we look for in the various parts of the Xcode window. Use the whole Xcode window's screenshot when posting for help.

## Find your error message(s)

To begin fixing the error, use the Report Navigator view to find your error message. 

</p>
<p align="center">
<img src="../img/report-nav.png" width="750">
</p>

The key is to (1) ***READ THE ERROR MESSAGE*** and then (2) ***FIND YOUR MESSAGE IN ONE OF THE TOPICS BELOW***.

Here's a super tip: Merely seeing the "exit code" in Xcode is not enough information to discern what error is causing your build to fail. Look at the detailed message to really help guide your search for the matching solution.

Notice how in the screenshots in the topics below, there are red circles highlighting certain error messages? Read your error messages similar to where those red circles are in the screenshots below. Once you find your error message (hint: not "exit code"), you can either:

* Take the error message from your Xcode screen and use LoopDoc's search function to enter in some of that phrase to bring up the appropriate solution topic, or

* Take the error message from your Xcode screen and read through EACH OF THE TOPICS BELOW. Check each of the red circles to see if you have a match. Kind of like a matching puzzle.

For example, if you see "Invalid active developer path (/Library/Developer/CommandLineTools)" in your error message, use the search tool in LoopDocs with simply "invalid active". You will get a couple of links and one is the Command Line Tools fix for that error message. Click on the link and you'll find your solution.

</p>
<p align="center">
<img src="../img/search-errors.png" width="650">
</p>

## No such module 'LoopKit' or similar message

If you see a **Cartfile failure** and several other red errors (in particular saying there is "no such module 'LoopKit'"), double click on the Cartfile error message.  If it says that the build failed in one of the schemes, as shown in the screenshot below, then you need to open the Terminal app (remember it is located in your Applications folder under the Utilities group of applications).  You will use the command `cd ~/downloads/loop-dev && carthage update`.  NOTE:  YOU MAY HAVE TO CHANGE THE COMMAND SLIGHTLY.  If your loop folder isn't named loop-dev and instead is loop-dev-2 or loop-master or some other folder name...change the command to match your folder's actual name. 

</p>
<p align="center">
<img src="../img/exit-code-65.png" width="850">
</p>

Carthage update will take about 15-25 minutes to run successfully.  A successful carthage update will look like the following:

</p>
<p align="center">
<img src="../img/carthage-update-success.png" width="550">
</p>

Once carthage update has run successfully, you can return to Xcode and press the build button again.  Your project should build successfully.

If your carthage update fails, try opening the Terminal app and running these commands to clear out your carthage cache and saved derived data in Xcode:

`rm -rf ~/Library/Caches/org.carthage.CarthageKit` and `rm -rf ~/Library/Developer/Xcode/DerivedData`

After running those commands, retry the `cd ~/downloads/loop-master && carthage update` (remembering to update the name of your Loop download folder, as needed).

## Could not get a container directory URL

Error message: "**<u>Could not get a container directory URL. Please ensure App Groups are set up correctly in entitlements.</u>**"

</p>
<p align="center">
<img src="../img/container-1.png" width="750">
</p>

</p>
<p align="center">
<img src="../img/container-2.png" width="750">
</p>

</p>
<p align="center">
<img src="../img/container-3.png" width="750">
</p>

To resolve this error, you will need to click on the Loop target's signing area and then the plus-sign in the App Groups area under the signing. Copy and paste the bundle indentifier into the new container that starts with `group.` and then add `Group` to the end of the name. Click OK to save.

The final App Group should now have a blue check box, the name should start with `group` and end with `LoopGroup`. See the screenshot as an example. Click the build button after your App Group is setup similarly and you should be good.



## Missing Command Line Tools

Error message:  "**<u>Invalid active developer path (/Library/Developer/CommandLineTools)</u>**" or "**<u>unable to find utility "xcodebuild", not a developer tool or in PATH</u>**"

</p>
<p align="center">
<img src="../img/command-line-error-1.jpg" width="550">
</p>

</p>
<p align="center">
<img src="../img/command-line-error-2.jpg" width="550">
</p>

Solution: Go to your Xcode preferences and under the Locations tab, select "Xcode 11.2.1" in the dropdown menu for Command Line Tools.

</p>
<p align="center">
<img src="../img/command-line-error-3.png" width="550">
</p>

## Pending Certificate Request

Error message: "You already have a current iOS Development certificate or a pending certificate request."

<p align="center">
<img src="../img/pending_certification_request.jpg" width="750">
</p>

Solution: This error message has just recently started to appear for some new Loop builders. To resolve the issue, please log in to your Developer account at [developer.apple.com](https://developer.apple.com) and then click on "Certificates, Identifiers & Profiles".  Under that screen, you will see "Development" under the "Certificates" section in the column on the left.  You will need to click on the certificates, and choose to "revoke" from the options that show after you click on the certificate. Confirm the warning message that will appear asking "Do you want to revoke the certificate?"

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


## Command CodeSign failed

Error message: "**<u>errSecInternalComponent,  Command CodeSign failed with a nonzero exit code</u>**"

</p>
<p align="center">
<img src="../img/errsecinternal.jpg" width="850">
</p>


Solution:  This error message is likely due to inadvertently saying "no" to allowing Keychain Access or changing your computer or AppleID password. Regardless, the solution is as follows:

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
Error: **<u>The Loop app appears on the list of apps available to install on the watch, but when you press "install", and it goes through the animation of filling in the circle while it's installing, but then at the end it just toggles back to saying "INSTALL"</u>**.

Solution:  Plug your iPhone into the computer and start Xcode.  On your watch, look for a prompt that says "Trust this computer".  Scroll down on the watch face and select the "Trust" button.  

Now we need to do one step before rebuilding Loop app again. Go to the top menu bar of Xcode and select "Clean Build Folder" from the Product menu option. Rebuild your Loop app. 

For an unknown reason (developers are working on fixing it currently), if you do repeated builds in the same Loop project folder...the watch app can fail to install properly after the first build. Therefore, a simple "Clean Build Folder" will reset the folder back to new and you'll be able to install the watch after that fresh build.

## Xcode path not set correctly after using Xcode 11 GM
Error: **<u>xcrun: error: active developer path ("/Users/pops/Downloads/Xcode.app/Contents/Developer") does not exist
Use sudo xcode-select --switch path/to/Xcode.app to specify the Xcode that you wish to use for command line developer tools, or use xcode-select --install to install the standalone command line developer tools.
See man xcode-select for more details.</u>**.

Please note that the path in the example error above is just an example. Your path in the error may be different.

Solution:  This may occur if you have installed Xcode 11 GM before you installed the updated general release version. So, Xcode may get confused on which path to be using. Run the command below:

`sudo xcode-select --switch /Applications/Xcode.app`

Enter your password that you use to login to your Mac with and press Enter. You may now proceed with your build commands.
