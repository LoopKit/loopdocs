# Build Errors

There are two types of build errors that happen; they are yellow warnings and red alerts. You'll see the warnings and alerts in the left-hand column of the Xcode window.

<font color="orange">**Yellow warnings**</font> do not cause the build to fail, those are just warnings.  Occasionally, a Loop version may have some minor discrepancies that cause a yellow alert...ignore those. Do not try to do anything to fix those...leave them alone.

<font color="red">**Red error alerts** </font> will have to be resolved before you can successfully build the Loop app. The steps below explain how to resolve them based on the messages you are seeing.

## Start with the obvious error causes

Before you start trying to resolve your red errors...start with the most obvious things that can cause a red error message:

1. **DO NOT USE BETA VERSIONS**  If you are using an iOS beta version or an Xcode beta version, your Loop will not build. If you have Xcode beta, uninstall it and get regular Xcode. If you have iOS beta on your iPhone, you will need to restore your iPhone entirely. You can restore to either (1) the last non-beta backup version you saved or (2) restore as a new iPhone (default settings). Yes, deleting iOS beta is a pain...so don't install it in the first place.

2. **Did you check for Xcode updates?** Cannot emphasize this one enough...you should check for Xcode updates (and install them) before building. If you are updating your Loop app, you often have updated your iOS since the previous build. Best practice is that you update your Xcode version before you update your iOS. Sometimes this may require a macOS update in order to have the App Store tell you there's an even newer Xcode available. So...check both macOS and then Xcode for updates!! And if you did not [**Turn Off Automatic Updates**](step2.md#turn-off-automatic-updates) on your iPhone/iPod, do it now.

3. **Did you check your Apple developer account for new license agreement?** Periodically, Apple will release a new developer license agreement that you need to sign before you can build new apps. You will get a build failure if there is a pending license agreement to sign. [Login to your Apple developer account](https://developer.apple.com/account) to check if there's a new license agreement.

4. **Did you reboot your computer after updating Xcode?** Yup...that was in the reminder on the page about updating your Loop app...did you ignore it? ;) And make sure your command line tools match the version of Xcode you just installed. [Xcode Command Line Tools](step9.md#command-line-tools)

5. **Did you get a fresh download of Loop code, don't just recycle an old download that you built with a long time ago?** That old version may not be compatible with new iOS and new Xcode versions.

6. **Are you are using a free developer account?** Make sure you finished the [removal of Siri and Push Notification capabilities](../build/step14.md#free-account).

1. **Are you doing a WorkSpace build?** Make sure you selected Loop (Workspace) instead of Loop.

## Fix 95% of errors

If you have checked all those steps above and think you have a true build error...here's the best starting place that resolves 95% of all build errors.

1. Open your project in Xcode as normal. Then go to the Xcode menu at the top of the screen and find the "Product" menu item. Use the drop down selection for "Clean Build Folder" or press shift-command-K. Either will work the same.
1. On the far right, next to the name Full Path is the folder name that Xcode will be using to build. Make sure it is the new code you just downloaded and not an older folder.
1. Open the Terminal app on your computer.
1. Copy and paste this command and press return: `rm -rf ~/Library/Developer/Xcode/DerivedData` Note: you won't see any message back if the command runs successfully.
1. Return to Xcode and try building your app again.

If the build fails again, look through the list below and see if you can match up your error message with one specific error messages listed in the later section of this page. If you really can't find your solution then post for help. But help us help you.

- Confirm it really is an error not already on this page; read all the circled bits in the images in the Specific Error Messages section
- Follow the steps in the Posting for Help section
- WE CANNOT HELP without version numbers and screenshots
- Do not take pictures of your computer screen with your phone


## Posting for help

STOP!!  Read this section! Important!

Before you post in Zulipchat or Looped Group asking for help with build errors, do your work first. The build errors listed below (and the obvious checks listed above) are very successful ***IF PEOPLE READ THIS PAGE***. The volunteer group of people answering questions in Looped and Zulipchat would love to spend more time on improving Loop in other ways than answering build error questions that can be answered by using this page as a first step.

Therefore, first use the error topics (listed in sections below) to try to resolve your build error yourself. Then, if you need to post for help because this page did not fix your problem, you'll need to include information with the post so we (the troubleshooters) know you read this page and where you are in your troubleshooting attempts

!!! danger "Must include in your post"
    * The version of Xcode you are using
    * The version of Loop you are building with
    * The version of iOS on your Loop iPhone
    * Specify if you are using a free or paid account, and if free...confirm you deleted Siri and Push Notification capabilities
    * Confirm you are not using an Xcode beta or iOS beta version (so we don't have to ask, actually type "I am not using beta versions"...this will save a lot of time and hassle)
    * Screenshots of your WHOLE Xcode window and/or Terminal window showing your error and any messages you've seen while working through the build errors/solutions.  NOT phone pics.  See below for instructions on how to do this.
    * State which fixes from the below list that you have already tried AND post the screenshots of the results of those fix attempts.

Helpful tip: Shift-Command-4-spacebar will give you a screenshot tool that you can use to click on the Xcode window to grab a screenshot. The screenshot will save to your desktop so you can include it in your post. Phone photos of your computer screen won't be of sufficient clarity to read the needed information and often cuts off valuable information that we look for in the various parts of the Xcode window. Use the whole Xcode window's screenshot when posting for help.

## Find your error message(s)

To begin fixing the error, use the Report Navigator view to find your error message.

![img/report-nav.png](img/report-nav.png){width="750"}
{align="center"}

The key is to (1) ***READ THE ERROR MESSAGE*** and then (2) ***FIND YOUR MESSAGE IN ONE OF THE TOPICS BELOW***.

Here's a super tip: Merely seeing the "exit code" in Xcode is not enough information to discern what error is causing your build to fail - some exit codes can have multiple causes. Look at the detailed message to really help guide your search for the matching solution.

Notice how in the screenshots in the topics below, there are red circles highlighting certain error messages? Read your error messages similar to where those red circles are in the screenshots below. Once you find your error message (hint: not "exit code"), you can either:

* Take the error message from your Xcode screen and use LoopDoc's search function to enter in some of that phrase to bring up the appropriate solution topic, or

* Take the error message from your Xcode screen and read through EACH OF THE TOPICS BELOW. Check each of the red circles to see if you have a match. Kind of like a matching puzzle.

For example, if you see "Invalid active developer path (/Library/Developer/CommandLineTools)" in your error message, use the search tool in LoopDocs with simply "invalid active". You will get a couple of links and one is the Command Line Tools fix for that error message. Click on the link and you'll find your solution.

![img/search-errors.png](img/search-errors.png){width="650"}
{align="center"}

## Specific Error Messages

### Carthage Error

If you have previously installed carthage and it got updated to a version newer than 0.36.0, you may get a carthage error. The error looks similar to:

!!! info "Wrong Version of Carthage Error"
    Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/lipo: one of -create, -thin <arch_type>, -extract <arch_type>, -remove <arch_type>, -replace <arch_type> <file_name>, -verify_arch <arch_type> … , -archs, -info, or -detailed_info must be specified.

Solution is to manually uninstall carthage:

- Open a Terminal
- Copy and paste this command into the terminal
    - `rm -rf /usr/local/bin/carthage`
- Copy and paste this command into the terminal
    - `sudo rm -rf /Library/Frameworks/CarthageKit.framework`
- You will be prompted for a password when you hit enter on the second command
- It is the same password you use in order to log into the computer
- It will not echo to the screen

### Could not locate device support files

If you see an error message that says "Could not locate device support files." That messages is telling you that your iOS on the phone requires you to get a newer version of Xcode to be able to build Loop onto that phone. Update your Xcode version.

![img/device-support-files.jpg](img/device-support-files.jpg){width="750"}
{align="center"}

Often people get confused at this point because their App Store may be telling them "no updates available" for Xcode, so they incorrectly assume that they have the most current Xcode.  

Instead, realize that the App Store only shows the updates available for your macOS version. If your macOS version falls behind...then the App Store will not show you Xcode versions that are incompatible with your older macOS. In other words if you are have Mojave macOS, you won't see newer versions of Xcode in the App Store that would require you to have Catalina or Big Sur macOS.

How are the versions all related? This figure will NOT be updated every time iOS updates, so check the linked reference. Use this figure as a guide to determine your minimum requirements using the up-to-date linked figure. We will attempt to keep the words below the figure updated.

(Source for the figure below is [wikipedia](https://en.wikipedia.org/wiki/Xcode#11.x_series))

![img/minimum-related.png](img/minimum-related.png){width="750"}
{align="center"}

If you're using iOS 14.4 on your iPhone, you'll need Catalina macOS 10.15.4 as a minimum to be able to see Xcode 12.4 in the App Store for download. Therefore, update to Catalina (or Big Sur) and then update to Xcode 12.4 to resolve your build error message about "device support logs missing".

With Xcode 12, the simulators are no longer being downloaded automatically. If you are missing a simulator, follow the steps under Step 9 [Simulator Download](step9.md#simulator-download).

### No such module 'LoopKit' or similar message

If you see a **Cartfile failure** and several other red errors (in particular saying there is "no such module 'LoopKit'"), double click on the Cartfile error message.  If it says that the build failed in one of the schemes, as shown in the screenshot below, then re-run the fix listed above.

Solution: Make sure to download a fresh version of code!  Anything downloaded before Jan 21, 2021 will not work.  That's when the need for carthage was removed.

![img/exit-code-65.png](img/exit-code-65.png){width="850"}
{align="center"}

### Developer License Update

Error message: "**The Apple Developer Program License Agreement has been updated,  In order to access certain membership resources, you must accept the latest license agreement.**"

Solution: You'll need to log onto your developer account at [developer.apple.com](https://developer.apple.com/account/) and accept the latest license agreement.

![img/license.png](img/license.png){width="750"}
{align="center"}

### Could not get a container directory URL

Error message: "**Could not get a container directory URL. Please ensure App Groups are set up correctly in entitlements.**"

![img/container-1.png](img/container-1.png){width="750"}
{align="center"}

![img/container-2.png](img/container-2.png){width="750"}
{align="center"}

![img/container-3.png](img/container-3.png){width="750"}
{align="center"}

To resolve this error, you will need to click on the Loop target's signing area and then the plus-sign in the App Groups area under the signing. Copy and paste the bundle indentifier into the new container that starts with `group.` and then add `Group` to the end of the name. Click OK to save.

The final App Group should now have a blue check box, the name should start with `group` and end with `LoopGroup`. See the screenshot as an example. Click the build button after your App Group is setup similarly and you should be good.

### Missing Command Line Tools

Error message:  "**Invalid active developer path (/Library/Developer/CommandLineTools)**" or "**unable to find utility "xcodebuild", not a developer tool or in PATH**"

![img/command-line-error-1.jpg](img/command-line-error-1.jpg){width="550"}
{align="center"}

![img/command-line-error-2.jpg](img/command-line-error-2.jpg){width="550"}
{align="center"}

Solution: Go to your Xcode preferences and under the Locations tab, select your Xcode version (the figure shows 12.0.1 - yours should match your Xcode version) in the dropdown menu for Command Line Tools.

![img/command-line-error-3.png](img/command-line-error-3.png){width="550"}
{align="center"}

### Device Management could not launch Loop

Error message: "Could not launch "Loop". Verify the Developer App certificate for your account is trusted on your device. Open Settings and navigate to General -> Device Management, then select your Developer App certificate to trust it."

![img/trust_device.jpg](img/trust_device.jpg){width="750"}
{align="center"}

Solution: If you get this message and are unable to find the Device Management option in your phone settings, then we need to do a little extra step to clear out some old info.

1. Plug phone in and open Loop in Xcode
2. Click the "Window" menu item in Xcode and then choose "Devices and Simulators"
3. Right click your phone on the left and pick "Show Provisioning Profiles"
4. Delete all of the items in the list that have Loop in the name
5. Go to your four signing targets and change the signing team back to "None" for a quick bit, and then change back to your regular signing team name again.
6. Rebuild Loop

That should clear out the old, unworking profiles and give you a successful build.

If your problem persists after that, then you can use a total reset to clear out the pesky problem:

1. Wipe the iPhone clean and setup as a new device
    - But FIRST - write down or screenshot all your settings
    - Pod users - you will have to start a fresh pod after this but your old pod will continue giving you basal rate if you leave it running - you won't be able to bolus
2. Delete all certificates from your Developer account (you'll need to login to your Developer account to do that)
3. Delete your old Loop code download and get a new one.
4. Rebuild Loop on the phone with the new download of Loop code.

### Pending Certificate Request

Error message: "You already have a current iOS Development certificate or a pending certificate request."

![img/pending_certification_request.jpg](img/pending_certification_request.jpg){width="750"}
{align="center"}

Solution: This error message has just recently started to appear for some new Loop builders. To resolve the issue, please log in to your Developer account at [developer.apple.com](https://developer.apple.com) and then click on "Certificates, Identifiers & Profiles".  Under that screen, you will see "Development" under the "Certificates" section in the column on the left.  You will need to click on the certificates, and choose to "revoke" from the options that show after you click on the certificate. Confirm the warning message that will appear asking "Do you want to revoke the certificate?"

![img/revoke1.png](img/revoke1.png){width="750"}
{align="center"}

After you do that, return to Xcode and open up Xcode preferences.  Under the Accounts section of Preferences, click on the minus sign to delete your Apple ID.

![img/account.png](img/account.png){width="650"}
{align="center"}

Re-enter your Apple ID (yes...add that account right back that you literally just deleted), return to your Loop's target signing areas in Xcode and your error message should have resolved itself now as a new certificate will have been issued and a provisioning profile should have been created automatically.

For double measure, you can verify that the iOS development certificates are all in good working order by clicking on your "Manage Certificates" in your Xcode Preferences, Accounts and viewing the iOS development Certificates.  You should have one for your account that has a clean status similar to the screenshot below.

![img/verify_cert.png](img/verify_cert.png){width="650"}
{align="center"}

### Command CodeSign failed

Error message: "**errSecInternalComponent,  Command CodeSign failed with a nonzero exit code**"

![img/errsecinternal.jpg](img/errsecinternal.jpg){width="850"}
{align="center"}

Solution:  This error message is likely due to inadvertently saying "no" to allowing Keychain Access or changing your computer or AppleID password. Regardless, the solution is as follows:

1. Close Xcode
2. Open your Keychain Access application (found in Applications within the Utilities folder, similar to where Terminal app is found)
3. In the upper left corner of keychain access, make sure you have the keychain `login` highlighted and then right-click the lock next to the `login`.  Click the lock closed, and then click the lock to open it again. You will be prompted for a password.  Enter your computer admin password.  Close Keychain Access app.

![img/keychain4.png](img/keychain4.png){width="450"}
{align="center"}

4. Open your Loop project again in Xcode.
5. In the main Xcode menu (grey menu bar at the very top of your Apple display area), select the word `Product` and then select the option for `Clean`. (keyboard shortcut is shift-command-k)
6. Now try rebuilding your Loop app.  If you ever get prompted again to allow Xcode access to Keychain, make sure to Always Allow.

### Unrecognized arguments: --cache-builds

Error message: "**Unrecognized arguments: --cache-builds**"

![img/cache-builds.png](img/cache-builds.png){width="850"}
{align="center"}

![img/exit-code-1-cartfile.jpg](img/exit-code-1-cartfile.jpg){width="850"}
{align="center"}

Solution: This is a homebrew / carthage error, so I don't think you'll see this. If you do, download a fresh copy of code and try again. If it repeats, reach out via zulipchat or Facebook or post an Issue on the LoopKit/Loop github site.

### Abort with Payload

Error message: "**Abort with payload**"  Your app will only open briefly with a white screen and then close, if you build with this error.

![img/abort_payload.png](img/abort_payload.png){width="750"}
{align="center"}

Solution: This error message is caused by having Loop download folder in an iCloud mapped drive.  Move your download folder back to the Downloads folder, then rebuild.


## Apple Watch Issues


### Apple Watch: Loop app not appearing

Error: **Apple watch app is not appearing**.

Solution: Usually because you have not updated the watchOS prior to when you built Loop, or you didn't have your Apple watch paired at the time of building Loop.  Don't forget to open the iPhone's Watch app, select My Watch tab on the bottom left, scroll all the way down, and click `Install` for the Loop app listed at the very bottom under "available apps".


### Apple Watch: Loop app not installing

Error: **The Loop app appears on the list of apps available to install on the watch, but when you press "install", and it goes through the animation of filling in the circle while it's installing, but then at the end it just toggles back to saying "INSTALL"**.

Solution:  Plug your iPhone into the computer and start Xcode.  On your watch, look for a prompt that says "Trust this computer".  Scroll down on the watch face and select the "Trust" button.  

Now we need to do one step before rebuilding Loop app again. Go to the top menu bar of Xcode and select "Clean Build Folder" from the Product menu option. Rebuild your Loop app.

For an unknown reason (developers are working on fixing it currently), if you do repeated builds in the same Loop project folder...the watch app can fail to install properly after the first build. Therefore, a simple "Clean Build Folder" will reset the folder back to new and you should be able to install the watch after that fresh build.

Sometimes, if the problem is really a bugger...you have to do a more painful troubleshooting. If you still can't get the Loop app to install on the watch after a "Clean Build Folder" attempt at rebuilding, we need to start at square one. Unpair your watch from the iPhone and setup as a brand new device. Yes, pain in the butt. But, usually wiping the watch, re-pairing fresh, and then building Loop again on the phone will fix the issue. Sorry, wish I had a shorter path to fixing that problem, but this is where the current state is. This is a known bug and may take several tries and include wiping devices of content. It is a pain...but we really don't have a magic bullet solution other than keep trying...and starting your devices from scratch is a pain for sure...but also the most likely to get rid of the bug.
