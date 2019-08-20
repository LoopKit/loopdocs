# Step 13: Build Loop app

## Open Loop project in Xcode

Go to your Downloads folder, open the `Loop-master` folder (or whatever you named it...double check that the folder does not contain any spaces in the folder name, as described above), and double click on Loop.xcodeproj. For Omnipod Loop, the folder will likely be named `Loop-omnipod-testing`.

<p align="center">
<img src="../img/loop_code.png" width="750">
</p>

A warning may appear asking if you really want to open it, click Open.  Xcode will get itself organized and installed, this may take a few minutes.  

<p align="center">
<img src="../img/loop_open.jpg" width="450">
</p>

Once Xcode has finished indexing, the Loop project's various folders and files will appear in the far left column (if you don't see the files/folders, click on the little blue folder icon at the top of that far left column).  At the very top, click on the blue "Loop" at the top of the list.  Then click on the box in the middle screen to reveal the targets column.  The four targets we will sign in the upcoming steps are now easily viewable.

<p align="center">
<img src="../img/target_view.png" width="750">
</p>

## Connect your iPhone to Computer

Connect your iPhone via cable to the computer, select your iPhone from the very top of the drop down list.  Your **<u>iPhone’s personal name</u>** should be at the top of the list.  Don't accidentally select the generic iOS simulators listed below your iPhone's name.  

!!!info "Helpful Tip"
If your iPhone has a lock enabled, Xcode will not be able to install Loop app once your phone locks during the build progress.  Please temporarily disable the lock until you finish building Loop app.  Go to your iPhone Settings >> Display & Brightness >> Auto-Lock and set it to `Never`.  You can reset your lock once Loop is done building onto the phone.

<p align="center">
<img src="../img/select_device.png" width="750">
</p>

<p align="center">
<img src="../img/your_device.png" width="650">
</p>

!!!info ""
These next steps are usually only needed on the first Loop build; they can be skipped on subsequent builds.

* If this is the first time your iPhone has been plugged in to this computer, you will need to open the iPhone and select "Trust this Computer" before your device will be useable in the menu selection.</br></br>
* If this is the first time you are building an app onto this iPhone using this particular Apple developer account, you will need to “register the device” to your developer account.  The device registration screen, as shown below, may appear when your iPhone is selected.  If these prompts for "register device" don't immediately appear, there will be a prompt later to register device.  Either registration prompt, now or later, will work.
<p align="center">
<img src="../img/device1.png" width="450">
</p>
<p align="center">
<img src="../img/device2.png" width="450">
</p>
<p align="center">
<img src="../img/device3.png" width="450">
</p>

## Signing Targets

!!!info "Free Developer Account Users: READ ME"
If you are using a free developer account to sign your targets in this next step, you will need to do a code customization first. As a free developer account, you are restricted from building apps that have Siri capabilities built-in. Loop has Siri capabilities...so you will need to disable them before proceeding on with signing and building your app. Please click [here to find instructions](https://loopkit.github.io/loopdocs/build/code_customization/#disable-siri-capabilities) on how to disable your Siri capabilities before moving on with signing your targets. Once you finish that step, come back here and finish the rest of the instructions.

Once you select your device (your iPhone's name), we are ready to start signing the four targets. We will start with the Loop target, the first one on the target list.  Under the "Signing" area, select the dropdown menu where it currently says "none". Choose your team that you'd like to sign with. If you select a team name with (personal team), your app will expire after 7 days. If you select a team name without that (personal team), your app will last a full year.  If you never signed up for a free developer account, you will not have a (personal team) showing. Make sure you keep the "automatically manage signing" box checked above the team selection area.

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

## Code Customizations

**New Loop users**: Customizations are not a required part of any Loop build.  As you gain experience in how you use your Loop app, you may want to customize some of the features.  You can always update your Loop app to add customizations at a later time.  Really though, building with the standard, default installation is JUST FINE.

If you want any custom configurations to your Loop or Loop Apple Watch apps, now is the time to make them before you finish with the last step of Loop installation on your iPhone.  Follow the step-by-step instructions on the [Code Customizations](code_customization.md) page. If you are a person familiar with Apple's swift language, feel free to make your own customizations as well.

When you've finished your customizations, come on back to this section and continue on with the rest of the build.

## Pair your Apple Watch
**New Apple Watch users**: If you have an unopened Apple watch and want to use it with Loop, first pair the watch with the iPhone before continuing to the next steps.  If you get a new watch after building the Loop app, you'll need to redo your Loop build. (Don't worry, it's as easy as pressing play on your saved Loop project.)</br>

**Existing Apple Watch users**: Please update your watchOS prior to building Loop app.  The current version of Loop requires watchOS 4.1 or newer.

!!!info "Series 0 Apple Watch users: Read Me"
**Series 0 Apple Watch users**: Please you will need to do a minor change in Loop code for your watch to use Loop. Select the WatchApp Extension target and under the 'Linked Frameworks and Libraries' section, click the '+' and type 'ClockKit' and press 'Add'. In the 'Status' column of the new row where ClockKit been added, change 'Required' to 'Optional'. You can move on with the rest of the instructions below now that you've completed that step. Whew, that old Apple Watch is still gonna work with this modern app.

## INTERMISSION

STOP STOP STOP

You guys...this is about safety.

People keep ignoring this advice and I'm frankly a little peeved, as it is ABOUT SAFETY. So, I'm moving this advice up in the process so that you don't ignore it. This is me getting in your face.

![attention](https://media.giphy.com/media/EqVipgL5iu0ivcddvA/source.gif)

!!!warning "DO NOT WING THE SETUP"
I have warnings all over these instructions to **continue to use these docs to finish setting up your app after it builds. DO NOT IGNORE THAT ADVICE. DO NOT ENTER ONE SETTING WITHOUT HAVING THE DOCS OPEN AND FOLLOWING ALONG AT THE SAME TIME.**

The section in these docs called "Set up App" (See it? Look for it now...at the top of your webpage) needs to be used to input all the settings in your app. READ ALONG WITH THE DOCS to enter those settings. There are important safety tips and advice in there. And then after you finish setup, you need to read the "Operate" section...like BEFORE YOU OPERATE LOOP. Don't bolus for a meal, or enter a meal, until you've read through the Operate section. 

I'm worried you will fail to heed the advice about using the setup and operate sections. People have ignored it before. They skim read and think that's good enough. DO NOT BE LIKE THAT. Read each section. 

![attention](https://media.giphy.com/media/xT9DPJVjlYHwWsZRxm/source.gif)

BUT, to mitigate the inevitable people who will ignore that advice....here's the two most important safety tips that I feel obliged to present out of order because (damn it), people will ignore my advice still.

!!!warning "TOP TWO SAFETY MISTAKES YOU SHOULD AVOID"
1. DO NOT ENTER SETTINGS YOU ARE UNSURE OF. If you don't know your settings or know what the terms mean, stop. Read the docs, all the settings entries are explained there. Ask your endo if you don't have established values for those settings. Don't just guess an ISF, carb ratio, basal rate, or maximum delivery limits.</br></br>

2. DO NOT ENTER ACCIDENTAL DUPLICATE CARB ENTRIES. When you enter a meal in Loop and press the `save` button...those carbs are saved. Let me repeat: THOSE CARBS ARE SAVED...even if you cancel the bolus for them. This is an automated insulin delivery system and if it thinks you have carbs on board, it will try to give you appropriate insulin for those carbs. Most common new user mistake: enters a meal, saves the carbs, has change of heart or gets confused, and cancels the bolus screen...thinking they've just canceled the entire meal entry. Then they enter in a new carb entry. AND NOW, when you go to bolus...you'll be bolusing for the meal you wanted AND the meal you are mistakenly thinking you had "canceled". You didn't cancel that carb entry though, you had only canceled the bolus...you didn't "unsave" the carbs. If you make a mistake or change your mind on a carb entry after you pressed save, then tap the green carb chart in Loop's main display and edit or delete that entry. **CANCELING A BOLUS DOES NOT CANCEL THE CARB ENTRY THAT GOT YOU THERE. You must delete or edit a saved carb entry if you no longer want Loop to provide insulin for it.**

Ok, so now that I've got your attention, you can continue on with the last step in building you app...but remember, we just pinky swore that you would use the setup and operate sections to finish this all? Don't break my heart, keep your promise.


## Build Loop

Signed the four targets? All done with any customizations? Have your Apple watch paired and updated? iPhone is unlocked and plugged into computer?

Let’s finish the installation of the Loop app onto your iPhone.  Double check to make sure your iPhone's name is still selected and then press the “play” button (or build button) to start Xcode on its way.  You’ll see the progression of the build in the status window.  New builds can take about 40-60 minutes depending on the speed of the computer and internet.  **Just be patient.**  The progress will get "stuck" on one step for a very long time, and then the others will fly by when that one slow step is done. Not every step is equal in duration. Do not give up on the build. Xcode will ALWAYS tell you eventually that the build either succeeded or failed...it will not just leave you hanging without an answer. 

You will be interrupted during the build for the codesign/keychain access prompt discussed below though. However, you can remain useful during the wait by reading the section below titled "While it's building...." 

<p align="center">
<img src="../img/build_button.png" width="750">
</p>

Be aware though! Sometime during your first ever build on a computer, be ready for a codesign/keychain access prompt that you will see part-way through the build process.</br></br>

<p align="center">
<img src="../img/keychain-prompt.png" width="450">
</p></br>

This prompt above, when you see it, requires you to enter your computer password and then select "Always Allow". Normal behavior, this prompt will come up four times in a row even after you enter the correct password. In frustration, people think the prompt must be broken because it keeps reappearing and then people will press deny or cancel.  **Don't deny.**  Keep entering your computer password and pressing the Always Allow button...as many times as it takes (four times to be exact; one for each target that Xcode is saving the password for).  After four times of successful password entry, the build will keep proceeding.

While it is building...read the next section below.

## While it's building...

While you are waiting for this build to finish, please take a moment to read this section. You're about to see a really crazy cool and amazing app on your phone that you've waited a long time for. It will suck you in immediately. And you will be so excited by how easy it is to use, that you will push your chair back from this computer screen and forget about any further instructions.</br>

<p align="center"><b>DON'T DO THAT!!</b></p>
<p align="center"><b>DON'T BE THAT PERSON!!</b></p>

There is SUPER valuable information contained in these documents that really needs to be reviewed and read. Such as:

* How to resolve any [build errors](https://loopkit.github.io/loopdocs/build/build_errors/) that you might get
* What all the settings mean in your Loop app and what reasonable ones might be
* How to enter carbs and what carb absorption duration means to bolusing
* How to handle sick days
* How to use override targets
* What the difference is between insulin models

### Once your build is successful, DO NOT JUST GO ENTERING SETTINGS IN BY YOURSELF!

Instead, work step-by-step to make sure you get through these pieces of helpful information:

* For USA Loopers, read the [Jaeb Observational Study page](https://loopkit.github.io/loopdocs/build/jaeb-study/)
* Read the [Health Permissions page](https://loopkit.github.io/loopdocs/build/health/) to make sure you get your Loop data recording properly
* Start with following the step-by-step directions for setting up your Loop correctly. THIS IS IMPORTANT! There are safety considerations in how you setup your app...so please follow along with the setup guides. [Loop App Overview and Setup Pages](https://loopkit.github.io/loopdocs/operation/overview/)</br></br>

And longer term:

* Bookmark [LoopDocs.org](https://loopdocs.org) and [LoopTips.org](https://looptips.org) so that you can come back to these resources to learn more if you have any questions.
* Join the [Looped Group](https://www.facebook.com/groups/TheLoopedGroup/?fref=nf) in Facebook
* Join the [Loop Users group](https://groups.google.com/forum/#!forum/loop-ios-users) in case of urgent notifications

Many of the greatest challenges in starting Loop can be helped by reading the pages in these docs and in Looptips.org. Please don't underestimate the help that a little reading can provide.

## Build Succeeded

If the build is successful, your brand new Loop app will have a screen open immediately on the iPhone asking about allowing Loop notifications and Health App access. Allow Loop to send you notifications. In the next screen that follows that, click on the `Turn All Categories On` line and then click `Allow` in the upper right corner.</br></br>

And now that you're built, I'm going to remind you again to use the guides to help you setup and understand your Loop app:
[Loop App Overview and Setup Pages](https://loopkit.github.io/loopdocs/operation/overview/)</br></br>

!!! info "First time builders"
If this is the first time you have installed an app on your iPhone using your developer account, you may get a warning like below.  Don't worry, Loop installed on the phone but needs you to do an extra step on the phone before Loop app can open.  Just follow the directions shown in the warning for what you need to do on your iPhone, and the issue resolves very quickly.  Click ok and you can safely disconnect your iPhone from the computer.  (If you don’t get a warning and the Loop app installs but does not open, you may still need to go to Settings->General->Device Management and enable trust for your Developer Account.)
<p align="center">
<img src="../img/trust_device.jpg" width="750">
</p>

## Build Failed
If you get a message that your build failed, you're likely going to see a list of red alerts on your left-hand column of Loop app. Those messages will be the key to resolving your build error.

<p align="center">
<img src="../img/general-error.jpg" width="750">
</p>

!!!info "IF YOUR BUILD FAILS..."
You'll need to go to the [Build Errors](build_errors.md) page to resolve the error message. Read your error message(s), find the matching error in the Build Errors page's images and descriptions, and follow the directions for repairing the error.
If you need help after trying the Build Errors page, please don't forget to provide the information requested in that page's "Posting for Help" section to help streamline the troubleshooting...including screenshots.

## Next Step: Jaeb's Loop Observational Study
You're done building your Loop app...but first, if you are a USA Loop user, please read about the [Jaeb Observational Study](https://loopkit.github.io/loopdocs/build/jaeb-study/) before moving onto [Loop App setup](https://loopkit.github.io/loopdocs/operation/loop-settings/settings/)



