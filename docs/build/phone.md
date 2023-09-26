## Compatible iPhone

!!! info "Time Estimate"
    - 5 minutes, to check your device and iOS
    - 20 minutes, if need to update your compatible device to a new iOS
    - 10 minutes, if you need to order a [compatible device](phone.md#compatible-devices) from Apple website
    - 0 minutes, if you own an Android and won't buy Apple products; check out [AndroidAPS Documention](https://androidaps.readthedocs.io/en/latest/)

!!! abstract "Summary"
    - Check your iPhone against the device compatibility list
        * For all devices, the newest iOS is strongly recommended
    - Make sure the phone has good battery life
    - Turn off automatic updates

!!! question "FAQs"
    - **"Can I use an android?"** No. Check out [AndroidAPS Documention](https://androidaps.readthedocs.io/en/latest/).
    - **"Can I use an iPad?"** No. Older iPads do not support Apple Health which is required for Loop. It may be possible with newer iPads and newer iOS, but this has not been tested.
    - **"Does my iPhone need a cell plan?"** No. Loop works using communication on your phone with your CGM and your pump; no internet connection required. However, if access to Dexcom Follow or Nightscout monitoring of Loop is a priority, then a cell plan may be desired.
    - **What watches work with Loop?** Only Apple watches work with Loop. With Loop 3, some of the older Apple watch series are no longer compatible. See: [Watch Hardware and OS Requirements](../operation/features/watch.md#watch-hardware-and-os-requirements)

## Which Devices Are Compatible?

Loop requires an Apple device. Loop uses the Apple Health app to store and retrieve your blood glucose and insulin data and to store your carbohydrate records. Older iPads do not support Apple Health which is required for Loop. It may be possible with newer iPads and newer iOS, but this has not been tested.

You need a minimum version of the mobile operating software, called the phone's "iOS", to be installed on your iPhone. Loop is compatible with iPhone devices with iOS 15.1 or newer.

### Compatible Devices

Note: 

* iPhone 15 is expected to be compatible
* iOS 17 is expected to be compatible, but it's a good idea to wait for iOS updates that come out quickly after a new iOS is released before updating your older phone (you won't have that choice if you buy an iPhone 15)

These devices are compatible with iOS 15.1 and newer iOS.

- iPhone 14, all variants
- iPhone 13, all variants
- iPhone 12, all variants
- iPhone 11, all variants
- iPhone X, all variants
- iPhone 8, all variants
- iPhone SE (3rd generation or later model; 2022 first release)
- iPhone SE (2nd generation; 2020 first release)

These devices are compatible with Loop 3, which requires iOS 15.1, but cannot be upgraded to iOS 16 or newer.

- iPhone 7, all variants
- iPhone 6s, all variants - but note the "s"
- iPhone SE (1st generation; 2016 first release)
- iPod Touch, 7th generation

## Find Your Device's iOS

Your phone's iOS version can be found under the phone Settings -> General -> About display as shown below. The iOS number is found on the `Software Version` line.

![phone current iOS display](img/ios.svg){width="300"}

Do not use any of the beta iOS versions. (Don't worry...if you don't know what that means, then you aren't using one.)

### Developer Mode - Mac-Xcode Build Only

With iOS 16 or newer and watchOS 9 or newer, Apple added a feature. If you want to know more, click on this [Apple Link about Developer Mode](https://developer.apple.com/documentation/xcode/enabling-developer-mode-on-a-device).

When you build Loop on your phone from Xcode directly and then transition to or start with iOS 16 or newer, you need to have Developer Mode enabled. This is also a requirement to use the Loop app on a watch paired to your phone running watchOS 9 or newer. You will be told to enable it in the [Build Loop App: Prepare your Phone and Watch](build-app.md#prepare-your-phone-and-watch) instructions.

When you build Loop using the new Browser Build method [GitHub Overview](../gh-actions/gh-overview.md), Developer Mode is not required.

!!! info "Developer Mode with iOS 16 or newer, watchOS 9 or newer"
    If you already have Loop, built with Xcode on a Mac, on your phone/watch when you update to iOS 16 or newer/watchOS 9 or newer or newer, you will be told that Loop requires Developer Mode to run.
    
    You will not be able to run Loop on your phone (or watch) until you have enabled Developer Mode on the device(s).

    ![phone message if trying to run xcode app without developer mode enabled](img/phone-developer-mode-required.jpeg){width="300"}
    {align="center"}


## Battery Health

Make sure the battery on your phone is solid. Your phone will become a critical health device - you want it to keep working.

* Make sure a charger and cord are in your diabetes supplies
* Consider buying a battery pack, keep it charged and add it to your travel bag

!!! tip "Low Power Mode"
    With newer iOS (15 and 16), some people have reported Loop continues working in the background (phone locked) even in [Low Power Mode](https://support.apple.com/en-us/HT205234). Others, have reported they still get red loops. You can experiment to determine if your phone/iOS/app is able to maintain green loops in low power mode.  Otherwise, best practice is to avoid Low Power Mode.

## Use Automatic Time

Be sure to set the phone to automatic time. Do not try to defeat a game by modifying time on the same phone used to control your insulin.

Please read: [Loop Phone Must be on Automatic Time](../faqs/time-faqs.md#loop-phone-must-be-on-automatic-time).

## Turn Off Automatic Updates

Apple provides updates regularly to the iOS.  Often, these updates include critical security patches in addition to improved new features.

**Please be proactive - install updates as soon as the "Loop" all-clear is given.**

If a limitation on your Mac prevents you from updating your phone to the latest iOS, consider using the Browser Build method; start with this link: [GitHub Build Overview](../gh-actions/gh-overview.md).


### Why Turn off Automatic Updates?

* Once you accept an iOS phone update, you cannot go backwards
    * Some iOS updates require updates to Xcode and macOS before people can build Loop on that device again
    * It is rare, but iOS updates have caused Loop to stop working until other updates were made and Loop was rebuilt on that phone
* Turn off automatic updates so you can choose when to update your phone and avoid being caught without a working Loop app
* Google the instructions for your device:
    1. Configure your phone to automatically download the updates
    1. Choose to perform the installation of the updates manually

When iOS updates are released, the [Loop and Learn Version Updates](https://www.loopandlearn.org/version-updates) page is typically updated faster than LoopDocs. Check to see if a new update is causing an issue with Loop or your CGM before accepting the update from Apple.

Within a few days, the "All-Clear" or "WAIT there's a problem" will be posted.

## Next Step: Compatible Pump

Now you are ready to check if you have a [Compatible Insulin Pump](pump.md).
