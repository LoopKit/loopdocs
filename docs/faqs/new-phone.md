## Overview

Changing phones means you have to rebuild the Loop app onto the new phone. When you transfer information from your old phone to your new one, all your Loop information is included and the Loop icon will appear, but the app will not open.

### Most Recent iOS is Required

When you change phones, *Apple* will force you to the latest iOS version available for your new phone.

### Prepare Before Upgrade

If you are using Dexcom G7, make sure you keep the 4-digit code for your current sensor.

If you still have your old phone, you can prepare before switching to the new phone.

!!! tip "Keep the Old Phone Until Loop is Working on the New One"
    Even if you plan to turn your old phone in for a rebate, you can ask to keep the old one for a week or two. Most vendors will agree to this.

Update your old phone to the latest iOS the hardware supports - this simplifies the automatic transfer process *Apple* provides to move all your data and apps from your old phone to your new phone.

!!! abstract "New Phone Checklist for *Mac-Xcode Build*"
    * Are your [Mac and Xcode versions](../build/xcode-version.md#how-do-all-the-minimum-versions-relate-to-each-other) compatible with the latest iOS version?
    * If not, you should configure and build the app with [Browser Build](../gh-actions/gh-overview.md)

!!! abstract "New Phone Checklist for *Browser Build*"
    * The Loop app will install from TestFlight onto the most recent iOS
    * If a new version of Loop is available, we recommend updating and building to the latest [GitHub Update](../gh-actions/gh-update.md)

### Different Developer ID

!!! important "Different Developer ID"
    If you need to build Loop with a different developer ID on the new phone, the settings and pump information will **not** transfer.

    * The new app that you build with the new Developer ID will open and you can [Onboard](../loop-3/onboarding.md)
    * The old app will still be on the phone: find it and delete it to avoid confusion

## Step-by-Step Instructions

### Procure a New Phone

1. Procure the new phone and keep the old one (if possible)
1. Transfer your information to your new phone
    * Let the new phone vendor help you
    * Use an [iCloud back-up](https://support.apple.com/en-us/HT210217) for the transfer
    * Use both devices with [Quick Start](https://support.apple.com/en-us/HT210216) to transfer from the old to the new phone

If you cannot keep the old phone, or it is not available, then skip ahead to the [Use New Phone to Loop](#use-new-phone-to-loop).

### Keep the Old Phone

Start using the new phone as a phone, but wait for a convenient time to complete the process.

* You can use the old phone to Loop until you are ready to switch
* Use WiFi with the old phone and use your new phone as a cellular hot-spot as needed
* Keep the CGM on the old phone
    * If using Dexcom, use the Dexcom app on the old phone
    * If using Libre, the Libre is connected to Loop on the old phone

### Use New Phone to Loop

Make sure the new phone has bluetooth turned on.

It's important to do the transfer of information from the old phone to the new phone before you install and open Loop on the new phone. If this is not possible, then you will do the normal [Onboarding](../loop-3/onboarding.md) for a new Loop app.

* When you transfer information from your old phone to your new phone, all the Loop settings files get copied to the new device including information about the pod
    * If you have changed pods after the transfer, then you should swap at your next pod change
    * If you time things well, you can keep the pod
* Be sure to record (or screenshot) all your settings from your old phone before you start
* Install Loop on the new phone (all your settings should be there)
    * Install via [*Mac-Xcode Build*](#build-using-mac-xcode) or from [*TestFlight*](#install-from-testflight) for *Browser Build*

As soon as you install Loop on the new phone, go ahead and disable Closed Loop.

* Keep closed loop disabled until you completed the full transfer and checkout.

#### Build using Mac-Xcode

* Open Xcode – use the same build as you used for the old phone
* Plug in the new phone to the computer (trust phone/computer) and hit build
* Build Loop on the new phone

#### Install from TestFlight

* Open TestFlight app on new phone
* Install Loop on your new phone from TestFlight

### Transfer CGM

It is now time to transfer the CGM to the new phone.

#### Dexcom App

The Dexcom app might have transferred successfully, but it’s not a bad idea to install that fresh from the App Store on the new phone. It may be required to do so.

* Be sure to record your Dexcom Transmitter ID or 4-digit code (for G7)
* On the new phone, in Loop, delete Dexcom as your CGM so you can pair the new phone to the Dexcom app
* On the old phone, go into Bluetooth settings and forget every Dexcom ID you can find
    * If you are not able to forget the connection between the old phone with the Dexcom transmitter, you might need to call Dexcom for help
* On the old phone, turn off Bluetooth
* On the new phone, open the Dexcom app and pair to the transmitter (G5, G6 or One) or enter the four-digit code for G7
    * You can keep using your current sensor session
    * You indicate you are starting a new sensor (it’s not really new)
        * G5, G6 or ONE, enter transmitter ID and "no code"
        * G7, enter 4-digit code
    * Within 5 to 10 minutes, Dexcom app should read the current session and keep going

* Wait for Dexcom to connect
* On new phone, add the CGM to Loop

#### Libre

Placeholder for Libre instructions. Suggested procedures from the community are encouraged.

* On the new phone, in Loop, delete Libre as your CGM
* On the old phone, turn off Bluetooth
* On the new phone, in Loop, add Libre as your CGM
* Wait for Libre to connect

### Transfer Pump

* On the old phone, make sure Bluetooth is off - this disables connection from the old phone to the pump
* On the new phone, examine the pump status
    * If everything tranfered, you should be communicating with your pump
    * If not, delete the pump and add it back

### Ready to Loop

1. Keep closed loop disabled until you completed the full transfer and checkout.

    !!! important "Check Every Setting"
        Make sure all the basal, ISF, CR, Insulin Selection and ranges are correct before using the new phone to Loop.

        Check permissions and notification settings.

        Check Focus mode settings - make sure Loop and Dexcom apps have permission for all Focus modes.

1. Do a manual bolus of the smallest possible amount to make sure Loop and pump are working.

1. Monitor CGM values to ensure new readings are coming in.

1. Check COB and IOB

    !!! important "Apple Health History"
        Your COB and IOB might not carry over to your new phone.

        Loop reads from Apple HealthKit and might restore COB and IOB from health – this assumes health is stored on iCloud and synchronized between old and new phone

        If your COB and IOB show up as blank, you can go open loop for 3 to 6 hours.
        
        If you are impatient, you can try this but be cautious:
        
        * Add back your insulin via Apple Health (on your new phone) to the time that the boluses and positive temp basals were recorded on your old phone: Apple Health/Insulin Delivery/Add Data.
        * Wait about 5 minutes for that insulin to show up in Loop as Active Insulin
        * Finally, add the Carbohydrates to Loop by entering them in your Add Carb Entry screen and rolling back the Date/Time wheel to the time of the original entry(ies)

1. Once you are happy with the configuration of Loop on your new phone, go ahead and enable closed loop mode again.

### Old Phone

Once you are using Loop on your new phone, you can remove the pump from the old phone.

* On the old phone, in the Loop app:
    * If using Medtronic, delete the pump
    * If using DASH pods, go into phone Settings -> Bluetooth and forget the pod; it will show up as TWI_BOARD or NXP_BLE

You can either keep the Old Phone as a backup or reset it and turn it in for credit or give to some deserving individual.
