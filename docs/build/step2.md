# Step 2: Compatible iPhone or iPod touch

!!! info "Time Estimate"
    - 5 minutes, if your iPhone or iPod touch is at iOS 12.4 or newer; iOS 14.4.2 or higher is recommended
    - 20 minutes, if need to update your compatible device to a new iOS
    - 10 minutes, if you need to order a [compatible device](step2.md#compatible-devices) from Apple website
    - 0 minutes, if you own an Android and won't buy Apple products; check out [AndroidAPS Documention](https://androidaps.readthedocs.io/en/latest/)

!!! abstract "Summary"
    - Check your iOS version and make sure you have iOS 12.4 minimum
    - WARNING, although the current version of Loop can be built with iOS 12.4, using newer iOS is strongly recommended
    - If using Dexcom CGM, your Looping iPhone/iPod touch will need the Dexcom app installed on it to Loop without an internet connection.
    - Make sure the phone has good battery life
    - This is a good time to read [Turn Off Automatic Updates](#turn-off-automatic-updates)

!!! question "FAQs"
    - **"Can I use an android?"** No. Check out [AndroidAPS Documention](https://androidaps.readthedocs.io/en/latest/).
    - **"Can I use an iPad?"** No. iPads do not support Apple Health and Loop uses Apple Health.
    - **"Does my iPhone need a cell plan?"** No. Loop works using communication via Bluetooth and the RileyLink compatible device with your CGM and pump; no internet connection required. However, without a cell plan, connection to the internet relies on WiFi availability. If access to Dexcom Follow or Nightscout monitoring of Loop is a priority, then a cell plan may be desired.  


## Which Devices Are Compatible?

Loop requires an iPhone or iPod touch. Loop uses the Apple Health app to store and retrieve your blood glucose and insulin data and to store your carbohydrate records. iPads do not have the Apple Health app, so iPads will not work with Loop.

You need a minimum version of the mobile operating software, called the phone's "iOS", to be installed on your iPhone or iPod touch. Loop is compatible with iPhone and iPod touch devices with iOS 12.4 or newer. The next version of Loop will require a minimum of iOS 14.

### Compatible Devices

These devices are compatible with iOS 14, which is expected to be the minimum iOS required to build the next version of Loop.

- iPhone 13, all variants
- iPhone 12, all variants
- iPhone 11, all variants
- iPhone X, all variants
- iPhone 8, all variants
- iPhone 7, all variants
- iPhone 6s, all variants - but note the "s"
- iPhone SE (2016 or later model)
- iPod Touch, 7th generation

### Devices That Will Soon Be Incompatible

- iPhone 5s, 6, 6+
- iPod Touch, 6th generation

Apple stopped providing iOS updates for these devices at iOS 12.x. These older devices cannot be updated to use these newer iOS versions, e.g., iOS 13, 14 or above. You can still build Loop with these older devices so long as your device has iOS 12.4 at a minimum. HOWEVER, there are upcoming Loop changes that will require users to have iOS 14 on their devices to build Loop. There is no set timeframe for when that minimum requirement will change.  When that happens, the docs will be updated and an announcement made in all the [Loop Social Media](../index.md#stay-in-the-loop) sites.

Side note for people who are seasoned Loop users and know about branches and such: Currently (July 2021), several popular Loop forks require devices to have iOS 13 or newer, and Loop dev requires iOS 14 as a minimum. There's no set timeframe for when dev will next be merged into master.

## Find Your Device's iOS

Your phone's iOS version can be found under the phone Settings -> General -> About display as shown below.

![phone current iOS display](img/ios.svg){width="300"}

Do not use any of the beta iOS versions. (Don't worry...if you don't know what that means, then you aren't using one.)


## Avoid Low Power Mode

Make sure the battery on your phone is solid. Your phone will become a critical health device - you want it to keep working.

Even with a solid battery, there will be times when your phone battery is low. In this case, the phone will warn you and offer to go into Low Power Mode. One of the things that happens in low power mode is that apps allowed to work in the background, i.e., when the phone is locked, will no longer do that. Loop is one of those apps - you want Loop to keep working when your phone is locked.  Your CGM is also one of those apps.

* Say NO to Low Power Mode
* Make sure a charger and cord are in your diabetes supplies
* Consider buying a battery pack, keep it charged and add it to your travel bag

## Turn Off Automatic Updates

Loop mentors recommend that automatic updates be turned off.

Apple provides updates regularly to the iOS.  Often, these updates include critical security patches in addition to improved new features.

* **Why Turn off Automatic Updates?** Once you accept an iOS phone update, you cannot go backwards and this can force a requirement to update your Mac operating system and then Xcode before you can build Loop on that device again

For new people - you may be wondering why you care?

  * Loop must be rebuilt at least once a year (the app expires)
  * When the Loop app expires, you get a ["Loop" is no available](updating.md#loop-is-no-longer-available) message and must rebuild
  * With the most recent Loop release, v2.2.6, you get automated [notifications](../operation/features/notifications.md#loop-app-expiration-notification) when expiration is approaching
  * Although Loop is fairly stable now; in the past, messages were posted to encourage people to rebuild ASAP because:
      * There were issues found with the code
      * Important new feature were implemented

When you turn off automatic updates, then you can choose when to update your phone.

**Please be proactive - install updates as soon as the "Loop" all-clear is given. If a limitation on your Mac is preventing you from being able to update your phone to the latest iOS, please pay attention to security vulnerabilities.**

We recommend that updates be installed as soon as the All-Clear is given.  Updates are important.

- **Updating to iOS 15 immediately stops the Loop app if it was built with Xcode versions 12.4 or earlier and requires a rebuild to continue Looping**
    - Look at the Issue Report to determine the [Xcode version](../faqs/update-faqs.md#how-can-i-confirm-xcode-version-i-used) used to build Loop on your phone
    - With major iOS updates, it's not a bad idea to wait a few weeks for Apple to push out a few minor updates
- An iOS update often requires an Xcode update to build Loop on that device and in some cases, that also requires a computer macOS update before the required Xcode version can be installed
- Sometimes, for example iOS 13 and iOS 15, the Xcode update required a Loop code update
- If a problem is found, the solution is typically posted pretty quickly
- Google the instructions for your device if you cannot figure it out
    1. Please configure your phone to automatically download the updates
    1. You should choose to perform the installation of the updates manually
- Check on your favorite [Loop Social Media](../index.md#stay-in-the-loop) site to see if a newly released iOS is causing an issue with Loop or your CGM before accepting the update from Apple
- The "All-Clear" or "WAIT there's a problem" is normally posted within a few days

Apple released iOS 15 on September 20, 2021.

## Next Step: Compatible Pump

Now you are ready to move onto Step 3 to check if you have a [Compatible pump](step3.md).
