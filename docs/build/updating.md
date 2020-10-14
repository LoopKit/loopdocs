# Updating Loop

!!!danger "Time Estimate"
    * 25 minutes, if already have updates done
    * 40-90 minutes, if need to install Apple update(s)

!!!info "Summary"
    1. Update macOS, Xcode, iOS, and/or watchOS
    2. Download updated Loop code
    3. Open in Xcode, sign targets
    4. Add optional code customizations
    5. Build onto your iPhone
    6. Resolve Build Errors

!!!warning "FAQs"
    * **"What is an update?"** Anytime you want to change branches (i.e., go from omnipod-testing to dev branch), change customizations, or grab updates to the same branch you built with before...that is an "update" of your Loop app.
    * **"Do I delete my old Loop app first?"** Definitely not! If you keep your Loop app on your phone, your Loop settings (and existing pod) will continue to work the same after the update. Seamless.
    * **"Do I need to start a new pod when I update?"** No. Your existing pod session will continue seamlessly if you are using the same Developer Account to sign the Loop app targets as you did the last time you built.
    * **"What if I'm using a new/different developer account?"** If you aren't building with the same developer account as your existing app was built with (this includes going from free to paid), then you will be installing a brand new (second) Loop app on your phone. Your existing pod won't work with the new app, so you might want to time this transition when you are due to change pods. Delete the old app once you get the new one all set up.
    * **"What if it is a new computer but the same developer account?"** No big deal...you just want to make sure the computer has Homebrew installed already and you've added your developer account to Xcode preferences.


## When to Update Loop

You will have to rebuild your Loop app at a minimum once every 12 months. The apps built and signed by you in Xcode with a paid developer account will only last for 12 months before they expire and need rebuilding. So, at least once per year you will have to rebuild your app and go through this update process.

Under ordinary circumstances, you do not *have to* update your Loop app until you are ready to grab new features. However, we encourage regular updates when a new version is released because they often contain bug fixes or improvements which may increase operational stability.

Since omnipod-testing branch has been retired and Loop v2.0 has been released, this is a good time to update your Loop app to the master branch. There will be some translations fixes in the near future. If you encounter any strange translations in master branch, please report them in in this [Looped Group thread](https://www.facebook.com/groups/TheLoopedGroup/permalink/2454410898108895/) so that I can get them fixed.  Thank you!

## Step 1: Avoid Build Errors in advance

!!!danger "Update to Xcode 11.6"
    Between Loop app builds, there's a high likelihood that Apple has updated one or more of the systems involved in your Loop app. If you miss macOS or Xcode updates, you may run into build problems. For example, the newest iOS on your phone requires the newest Xcode version to properly build Loop.  Currently the most recent version of Xcode is 11.6. **UPDATE TO XCODE 11.6 BEFORE UPDATING YOUR LOOP APP. **</u> 

!!!info "Check your Apple Developer Account"
    On October 28, 2019, Apple updated its License Agreement for the Developer Program. You need to login to your [developer account](https://developer.apple.com/account/) and accept the new agreement, or you will get a build error.
        
!!!warning "Restart computer after updating Xcode"
        Make sure to restart your computer after updating Xcode. There's a known issue that happens often enough to be frustrating if you don't reboot. Either a build error about missing simulators or a "device not connected" (even when phone is connected). Just restart computer. It's easy enough.


## Step 2: Download Updated Loop Code

After you've finished the updates to your devices listed above, you can move onto downloading updated Loop code. You will not be simply using your old downloaded Loop code (and in fact, you can delete those old folders now if you want). Click on **ONE** of the links below to download an updated version of the Loop code. Almost every user should be using Master branch of Loop now. On December 31, 2019, Loop v2.0 was released and offers support for Omnipod and Medtronic users, as well as numerous features that have been in development and testing for awhile.
</br></br>
<p align="center">
[Loop: Master branch](https://github.com/LoopKit/Loop/archive/master.zip)
</p></br>
<p align="center">
**OR**</br></br>
[Loop: Dev branch](https://github.com/LoopKit/Loop/archive/dev.zip)
</p></br>

## Step 3: Build Like Normal

From here it is just like the old directions...you can go straight to [Step 14 Build Loop app](https://loopkit.github.io/loopdocs/build/step14/) and do just like you did the first time. Open the project, plug in the phone, sign four targets, code customizations (if wanted), and then build button. Easy peasy.

Note: If this is a computer that hasn't built Loop before, you would want to make sure to do [Step 7: install Homebrew](https://loopkit.github.io/loopdocs/build/step7/) before doing your build on that computer.

## Step 4: Check Build Errors page if needed
    
!!!danger "CHECK BUILD ERRORS PAGE"
    If you get a build error...still check the [Build Errors page](https://loopkit.github.io/loopdocs/build/build_errors/). Because even if your exact error isn't there...the information you NEED to provide when asking for help is listed out on that page. And that information is critical. CRITICAL to be able to troubleshoot your build error.


