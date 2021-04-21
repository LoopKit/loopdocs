# Step 2: Compatible iPhone or iPod touch

!!! danger "Time Estimate"
    - 5 minutes, if your iPhone or iPod touch is at iOS 12.4 or newer; iOS 14.4.2 or higher is recommended
    - 20 minutes, if need to update your compatible device to a new iOS
    - 10 minutes, if you need to order a [compatible device](step2.md#compatible-devices) from Apple website
    - 0 minutes, if you own an Android and won't buy Apple products; check out [AndroidAPS Documention](https://androidaps.readthedocs.io/en/latest/)

!!! info "Summary"
    - Check your iOS version and make sure you have iOS 12.4 minimum
    - WARNING, although the current version of Loop can be built with iOS 12.4, using newer iOS is strongly recommended
    - If using Dexcom CGM, your Looping iPhone/iPod touch will need the Dexcom app installed on it to Loop without an internet connection.
    - This is a good time to [Turn Off Automatic Updates](#turn-off-automatic-updates) in your iPhone/iPod settings

!!! warning "FAQs"
    - **"Can I use an android?"** No. Check out [AndroidAPS Documention](https://androidaps.readthedocs.io/en/latest/).
    - **"Can I use an iPad?"** No. iPads do not support Apple Health and Loop uses Apple Health.
    - **"Does my iPhone need a scell plan?"** No. Loop works using communication via Bluetooth and the RileyLink compatible device with your CGM and pump; no internet connection required. However, without a cell plan, connection to the internet relies on WiFi availability. If access to Dexcom Follow or Nightscout monitoring of Loop is a priority, then a cell plan may be desired.  


## Which Devices Are Compatible?

Loop requires an iPhone or iPod touch. Loop uses the Apple Health app to store and retrieve your blood glucose and insulin data and to store your carbohydrate records. iPads do not have the Apple Health app, so iPads will not work with Loop.

You need a minimum version of the mobile operating software, called the phone's "iOS", to be installed on your iPhone or iPod touch. Loop is compatible with iPhone and iPod touch devices with iOS 12.4 or newer. The next version of Loop may require a minimum of iOS 14.

### Compatible Devices

These devices are compatible with iOS 14, which is expected to be the minimum iOS required to build the next version of Loop.

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

Apple stopped providing iOS updates for these devices at iOS 12.4. Apple released iOS 13 and iOS 14 in the recent past and these older devices cannot be updated to use these newer iOS versions. This does not pose a problem currently...you can still build Loop's master and automatic-bolus branch so long as your device has iOS 12.4 at a minimum. HOWEVER, there are upcoming Loop changes that will require users to have iOS 14 on their devices to build Loop. There is no set timeframe for when that minimum requirement will change.  When that happens, the docs will be updated and an announcement made in all the [Loop Social Media](../index.md#stay-in-the-loop) sites.

Side note for people who are seasoned Loop users and know about branches and such: Currently (April 2021), Loop's dev branch and several popular forks require devices to have iOS 13 or newer, and it is expected dev will soon require iOS 14. There's no set timeframe for when dev will next be merged into master.

## Find Your Device's iOS

Your phone's iOS version can be found under the Settings app, General, About as shown below.

![img/ios.jpg](img/ios.jpg){width="300"}

Do not use any of the beta iOS versions. (Don't worry...if you don't know what that means, then you aren't using one.)


## Turn Off Automatic Updates

This is important - this allows you to choose when to update your phone. We recommend that updates be installed as soon as the All-Clear is given.  Updates are important.

- An iOS update has never prevented Loop from working
- But an iOS update often requires an Xcode update to build Loop on that device
- Rarely, but it has happened, that Xcode update requires a Loop code update
- If a problem is found, the solution is typically posted pretty quickly
- Most people who Loop want to keep Looping - so do yourself a favor and turn off automatic updates
- Google the instructions for your device if you cannot figure it out
    1. It's fine to automatically download the updates
    1. Do not enable automatic installation of the updates
- Check on your favorite [Loop Social Media](../index.md#stay-in-the-loop) site to see if a newly released iOS is causing an issue with Loop or your CGM before accepting the update from Apple
- The "All-Clear" or "WAIT there's a problem" is normally posted within a few days

## Next Step: Compatible Pump

Now you are ready to move onto Step 3 to check if you have a [Compatible pump](step3.md).
