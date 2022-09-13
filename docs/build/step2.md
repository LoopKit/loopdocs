# Compatible iPhone or iPod touch

!!! info "Time Estimate"
    - 5 minutes, to check your device and iOS
    - 20 minutes, if need to update your compatible device to a new iOS
    - 10 minutes, if you need to order a [compatible device](step2.md#compatible-devices) from Apple website
    - 0 minutes, if you own an Android and won't buy Apple products; check out [AndroidAPS Documention](https://androidaps.readthedocs.io/en/latest/)

!!! abstract "Summary"
    - Check your iPhone/iPod touch against the device compatibility list
        * For all devices, the newest iOS is strongly recommended
    - Make sure the phone has good battery life
    - Turn off automatic updates

!!! question "FAQs"
    - **"Can I use an android?"** No. Check out [AndroidAPS Documention](https://androidaps.readthedocs.io/en/latest/).
    - **"Can I use an iPad?"** No. iPads do not support Apple Health and Loop uses Apple Health.
    - **"Does my iPhone need a cell plan?"** No. Loop works using communication on your phone with your CGM and your pump; no internet connection required. However, if access to Dexcom Follow or Nightscout monitoring of Loop is a priority, then a cell plan may be desired.

## Which Devices Are Compatible?

Loop requires an iPhone or iPod touch. Loop uses the Apple Health app to store and retrieve your blood glucose and insulin data and to store your carbohydrate records. iPads do not have the Apple Health app, so iPads will not work with Loop.

You need a minimum version of the mobile operating software, called the phone's "iOS", to be installed on your iPhone or iPod touch. Loop is compatible with iPhone and iPod touch devices with iOS 12.4 or newer. The next version of Loop will require a minimum of iOS 14.

### Compatible Devices

These devices are compatible with iOS 14 through iOS 16.

- iPhone 14, all variants
- iPhone 13, all variants
- iPhone 12, all variants
- iPhone 11, all variants
- iPhone X, all variants
- iPhone 8, all variants
- iPhone SE (2nd generation or later model; 2020 first release)

These devices are compatible with Loop 3, but cannot be upgraded to iOS 16. Loop 3 is the soon-to-be released version of Loop. This version of Loop requires iOS 14.

- iPhone 7, all variants
- iPhone 6s, all variants - but note the "s"
- iPhone SE (1st generation; 2016 first release)
- iPod Touch, 7th generation

### Devices Incompatible with Loop 3

These devices are compatible with Loop 2.2.x but will not be compatible when Loop 3 is released.

!!! Warning "Plan to Update Soon"

    - You will not be able to build the next release of Loop on these devices

- iPhone 5s, 6, 6+
- iPod Touch, 6th generation


## Find Your Device's iOS

Your phone's iOS version can be found under the phone Settings -> General -> About display as shown below. The iOS number is found on the `Software Version` line.

![phone current iOS display](img/ios.svg){width="300"}

Do not use any of the beta iOS versions. (Don't worry...if you don't know what that means, then you aren't using one.)

### Developer Mode

With iOS 16 and watchOS 9, Apple has added a feature. If you want to know more click on this [Apple Link about Developer Mode](https://developer.apple.com/documentation/xcode/enabling-developer-mode-on-a-device).

When you build Loop on your phone running iOS 16, and watch paired to your phone running watchOS 9, you need to have Developer Mode enabled. You can go on and enable it now - or wait until the instructions to build the app on your phone tell you to do it.

!!! info "Developer Mode with iOS 16, watchOS 9"
    If you already have Loop on your phone/watch when you update to iOS 16/watchOS 9, you will be asked if you want to enable Developer Mode. Say yes, allow the device to reboot. After the reboot, you get a new message asking if you want to Turn On Developer Mode. Tap on `Turn On`.

    If you are not prompted if you want to enable Developer Mode, it can be enabled in Phone Settings under Privacy & Security - scroll to the bottom of the screen and enable it.

    Loop will not run until you enable Developer Mode, reboot and turn it on. After those steps; Loop continues as before.

## Battery Health

Make sure the battery on your phone is solid. Your phone will become a critical health device - you want it to keep working.

With newer iOS (14 and 15), some people have reported Loop continues working even in [Low Power Mode](https://support.apple.com/en-us/HT205234) if you need to preserve battery; others, have reported they still get red loops.

Older iOS (and associated older phones) were reported to cause Loop to stop updating when the phone was locked. If you are running an older version of iOS (on an older device) with Loop 2.2.x, you may need to avoid Low Power Mode.

* Make sure a charger and cord are in your diabetes supplies
* Consider buying a battery pack, keep it charged and add it to your travel bag

## Turn Off Automatic Updates

Apple provides updates regularly to the iOS.  Often, these updates include critical security patches in addition to improved new features.

**Please be proactive - install updates as soon as the "Loop" all-clear is given.**

If a limitation on your Mac prevents you from updating your phone to the latest iOS, please pay attention to security vulnerabilities.


### Why Turn off Automatic Updates?

* Once you accept an iOS phone update, you cannot go backwards
    * Some iOS updates require updates to Xcode and macOS before people can build Loop on that device again
    * It is rare, but iOS updates have caused Loop to stop working until other updates were made and Loop was rebuilt on that phone
* Turn off automatic updates so you can choose when to update your phone and avoid being caught without a working Loop app
* Google the instructions for your device:
    1. Configure your phone to automatically download the updates
    1. Choose to perform the installation of the updates manually


When iOS updates are released, check your favorite [Loop Social Media](../intro/loopdocs-how-to.md#how-to-find-help) site to see if the update is causing an issue with Loop or your CGM before accepting the update from Apple.

Within a few days, the "All-Clear" or "WAIT there's a problem" will be posted.

!!! warning "Older Builds"
    Updating to iOS 15 immediately stops the Loop app if it was built with Xcode versions 12.4 or earlier and requires a rebuild to continue Looping**

    - Look at an Issue Report to determine the [Xcode version](../faqs/update-faqs.md#how-can-i-confirm-xcode-version-i-used) used to build Loop on your phone


## Next Step: Compatible Pump

Now you are ready to check if you have a [Compatible Insulin Pump](step3.md).
