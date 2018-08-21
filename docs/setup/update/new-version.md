# Loop v1.5.7 Features

As always, there is a [GitHub page](https://github.com/LoopKit/Loop/releases/tag/v1.5.7) with release notes about the features and changes since the previous Loop release.  

## Minimum OS updates required

Before you start the update process, please make sure you update your devices to the minimum required versions.

* **macOS Sierra**: macOS 10.3.2 High Sierra</br>
* **Xcode**: Xcode 9.4 </br>
* **iPhone**: iOS 11.1 at a minimum</br>
* **watchOS**: watchOS 4.3</br></br>

## Automatic Carthage Installation

The preparation steps to build Loop have changed.  Old versions of Loop required the manual installation of Homebrew and Carthage before you began the installation of Loop.  The new version only requires you to install Homebrew, Xcode will automatically install Carthage in the background if it is not already installed on your computer.  So if you are building on a new computer and think "Wait, aren't I missing a step in the directions?  I thought I had to install Carthage somewhere."...don't worry.  You haven't missed a step, Loop is just going to do it for you.

<p align="center">
<img src="../img/carthage-gone.png" width="750">
</p>
</br></br>

## Automatic Main App Bundle ID

Remember how the first step used to be that you had to change the `com.loopkit ` to something unique-to-you?  And if you updated you had to remember what you used last time?  No longer.

The Main App Bundle Identifier is now going use your unique development team ID that Apple has assigned using your developer account.  You don't have to change anything now.  Just leave that as is.  When you sign your targets, Loop will automatically populate all the necessary bundle IDs with the needed information. 

<p align="center">
<img src="../img/new-main-id.png" width="750">
</p>
</br></br>


## Initial Loop Build Slower

The new Loop will take awhile longer to build than you are used to.  This is due to some changes in the way Loop deals with integrated frameworks.  BE PATIENT.  Depending on the speed of the computer and internet, your initial build could take between 15-40 mins or so.  Subsequent builds will be fast again, it is just the first build that will take awhile.

You will see this step take the longest...`Building Loop: Cartfile  |  Running 2 of 2 custom shell scripts`  Just wait it out.

<p align="center">
<img src="../img/step2.png" width="750">
</p>
</br></br>

## Initial Pump Setup 

You'll notice one of the changes in the update almost immediately when you go to the Loop settings and see an `Add Pump` prompt.

<p align="center">
<img src="../img/pump-manager.PNG" width="250">
</p>

The new pump setup has pretty self-explanatory steps for setting up your pump in Loop.  
</br></br>

## Basal Rates and Delivery Limits (save to pump...)

Loop now automatically reads and imports the following settings from the pump during initial setup:

* Basal Rates (Standard basal rates)
* Delivery Limits (maximum basal rate and maximum bolus)

<p align="center">
<img src="../img/delivery-limits.png" width="250">
</p>
</br></br>

Even better news?  Loop now saves edits to those settings back to the pump.  There's a new `Save to pump...` button that must be used after you edit those settings in Loop.  If you don't use that button, the edits you make to those Loop settings will not be saved in Loop nor in the pump.  The purpose is to keep Loop and your pump in snyc.  **Now, if Loop fails for whatever reason, you can be sure that the basal rate in the pump will match what you've been using in your Loop.**

<p align="center">
<img src="../img/save-to-pump.png" width="250">
</p>
</br></br>

!!!info ""
    Loop will read/write to the  Standard basal rates in your pump. If you have Pattern A or Pattern B selected, Loop will automatically switch your pump to Standard basal.  Therefore, make sure that you have updated your Standard basal pattern to reflect your current basal rates before setting up your new Loop.

## Pump Clock integration

As part of the initial setup, Loop will now automatically prompt you to set your pump's time to exactly match your Loop's time.  Additionally, if you forget the warnings and set the pump time manually using the pump's menu, Loop app will now have RileyLink automatically get the pump back in-sync with Loop.  Loop will fix your mistake.  

As always, you will not have to worry about pump time changes if you travel.  You do not have to change your pump's time when you travel, unless you want to.  If you decide to, remember to use your Loop to set the pump's time...don't actually use the pump buttons for time changes.

<p align="center">
<img src="../img/pump-clock.png" width="250">
</p>
</br></br>

## Integral Retrospective Correction

Integral Retrospective Correction (IRC) is an optional algorithm change, meaning it will affect how your Loop sets temp basals and recommends boluses compared to older Loop versions.  Just as with standard retrospective correction, IRC was developed to make Loop less dependent on how well carb entries, ISF, carb ratios, or programmed basal rates represent reality, and to improve Loop responses in the presence of "unannounced" factors.

You can read more about IRC developement [here](https://github.com/LoopKit/Loop/issues/695).

## Updated Watch App Display

There is a brand new Loop watch display.  This includes a BG graph and information about IOB and COB.  You can access the new watch screen

## Language Translations

This release includes several new language translations.  If the user has their iPhone's language set to one of the following languages, the Loop app will match:

* English
* Spanish
* German
* French
* Russian
* Norwegian Bokmål
* Dutch
* Chinese (simplified)


