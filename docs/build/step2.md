# Step 2: Compatible iPhone or iPod touch

!!!danger "Time Estimate"
    * 5 minutes, if already have iOS 12.4 or newer
    * 20 minutes, if need to update your compatible device to iOS 12.4 or newer
    * 10 minutes, if you need to order a device from Apple website
    * 0 minutes, if you own an Android and won't buy Apple products...that's fine, too.

!!!info "Summary"
    * Check your iOS version and make sure you have 12.4 minimum.
    * Do not use any of the beta iOS versions. (Don't worry...if you don't know what that means, then you aren't using one.)
    * If using Dexcom CGM, your Looping iPhone/iPod touch will need the Dexcom app installed on it in order to Loop without an internet connection.

!!!warning "FAQs"
    * **"Can I use an android?"** No.
    * **"But why not?"** Because Loop is written in Apple's Swift language, which does not compile onto Android operating systems.  Loop also relies on Apple Health, and Android does not have a suitable native equivalent.
    * **"Can I use an iPad?"** No. iPads do not support Apple Health and that is an important part of Loop's inner workings.
    * **"Does my iPhone need cell plan?"** No. Loop will work without an internet connection...however you will not have Dexcom Follow data or Nightscout data if you choose to use a device that doesn't have an internet connection. In other words Loop will work, but remotely watching followers won't see Looping data unless the Loop device has an internet connection.

## Which Devices are compatible? Why those?

Why is Loop limited to just iPhones and iPod touches? Why can't you use an iPad? Because Loop uses the Apple Health app to store and retrieve your blood glucose, carbohydrate, and insulin data records. iPads do not have the Apple Health app, so those devices will not work with Loop. iPhones and iPod touches have the Apple Health app, so they will work with Loop.

The next compatibility check is that we need a minimum version of the operating software, called the phone's "iOS", on those iPhones and iPod touches. Loop is compatible with iPhone and iPod touch devices with iOS 12.4 or newer. Therefore, the compatible devices include:

* iPhone 11, 11 Pro, 11 Pro Max 

* iPhone X, XS, XR, XS Max 

* iPhone 8, 8+ 

* iPhone 7, 7+ 

* iPhone 6s, 6s+ 

* iPhone SE 

* iPod Touch, 7th generation 

## Devices that will be incompatible "soon"

* iPhone 5s, 6, 6+

* iPod Touch, 6th generation 

Apple has decided that those models have lived their useful life and can no longer be be updated past iOS 12.4. They've reached the end of their "apple supported" update life cycle. Apple released iOS 13 and iOS 14 in the recent past and those models cannot be updated to use them. This does not pose a problem currently...you can still build Loop's master branch so long as your device has iOS 12.4 at a minimum. HOWEVER, there are upcoming Loop changes that will require users to have iOS 13 on their devices to build Loop onto the device. There is no set timeframe for when that minimum requirement will be changed.  We will make an announcement when it does and the docs will be updated here.

Side note for people who are seasoned Loop users and know about branches and such: Currently (as of October 2020), Loop's dev branch requires devices to have iOS 13 or newer. There's no set timeframe for when dev will next be merged into master.

## Find your device's iOS
Your phone's iOS version can be found under the Settings app, General, About as shown below.

<p align="center">
<img src="https://loopkit.github.io/loopdocs/build/img/ios.jpg" width="300">
</p>

## Next Step: Compatible Pump

Now you are ready to move onto Step 3 to check if you have a [Compatible pump](https://loopkit.github.io/loopdocs/build/step3/).
