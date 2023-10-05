## Overview

Changing phones means you have to rebuild the *Loop* app onto the new phone. When you transfer information from your old phone to your new one, all your *Loop* information is included and the *Loop* icon will appear, but the app will not open until you install *Loop* from either *TestFlight* (*GitHub* Build) or&nbsp;<span translate="no">Xcode</span>&nbsp;(<span translate="no">Mac-Xcode</span>&nbsp;Build).

Some people don't have access to their old phone. There are instructions for handling that on this page. It makes the whole process more stressful, but remember, pods continue to deliver basal rate and Medtronic pumps can be controlled on the pump itself. Use your backup plan until you can get *Loop* running on a new phone.

### Forced iOS Update

When you change phones, *Apple* will force you to the latest iOS version available for your new phone.

### Prepare Before Upgrade

If you are using Dexcom G7, make sure you keep the 4-digit code for your current sensor.

If you still have your old phone, you can prepare before switching to the new phone.

* Be sure to record your *Loop* Settings (screenshots work well)

If you don't have your old phone, hopefully you have an iCloud backup and can use that to transfer your information to your new phone.

!!! tip "Keep the Old Phone Until *Loop* is Working on the New One"
    Even if you plan to turn your old phone in for a rebate, you can ask to keep the old one for a week or two. Most vendors will agree to this.

Update your old phone to the latest iOS the hardware supports - this simplifies the automatic transfer process *Apple* provides to move all your data and apps from your old phone to your new phone.

!!! abstract "New Phone Checklist for *Browser Build*"
    * The *Loop* app will install from *TestFlight* onto the most recent iOS
    * If a new version of *Loop* is available, we recommend updating and building to the latest [Update with Browser](../gh-actions/gh-update.md)

!!! abstract "New Phone Checklist for <span translate="no">Mac-Xcode</span>&nbsp;Build"
    * Are your [Mac and Xcode versions](../build/xcode-version.md#how-do-all-the-minimum-versions-relate-to-each-other) compatible with the latest iOS version?
    * If not, you should configure and build the app with [Browser Build](../gh-actions/gh-overview.md)

### Different Developer ID

!!! important "Different Developer ID"
    If you need to build *Loop* with a different developer ID on the new phone, the settings and pump information will **not** transfer.

    * The new app that you build with the new Developer ID will open and you can [Onboard](../loop-3/onboarding.md)
    * The old app will still be on the phone: find it and delete it to avoid confusion

## Procure a New Phone

1. Procure the new phone and keep the old one (if possible)
    * [*Loop* with the old phone](#loopwith-the-old-phone) until it is convenient to switch to the new phone
1. Transfer your information to your new phone
    * Let the new phone vendor help you
    * Use an [iCloud back-up](https://support.apple.com/en-us/HT210217) for the transfer
    * Use both devices with [Quick Start](https://support.apple.com/en-us/HT210216) to transfer from the old to the new phone

### *Loop* with the Old Phone

If you cannot keep the old phone, or it is not available, then skip ahead to the [*Loop* with the New Phone](#loopwith-the-new-phone).

* You can use the old phone to *Loop* until you are ready to switch
* Use WiFi with the old phone and use your new phone as a cellular hot-spot as needed
* Keep the CGM on the old phone
    * If using Dexcom, use the Dexcom app on the old phone
    * If using&nbsp;<span translate="no">Libre</span>;, the&nbsp;<span translate="no">Libre</span>&nbsp;is connected to *Loop* on the old phone

## *Loop* with the New Phone

### Install *Loop*

It is easier if you transfer information from the old phone to the new phone before you install and open *Loop* on the new phone. If this is not possible, then you will do the normal [Onboarding](../loop-3/onboarding.md) for a new *Loop* app.

1. When you transfer information from your old phone to your new phone, all the *Loop* settings files get copied to the new device including information about the pod
    * If the timing works, you can keep the pod if you switch to using the new phone for *Loop* after the information transfer and before changing pods with the old phone
    * If this is not possible, you will need to start a new pod with the new phone
    * Medtronic users will have all their information transferred but will only have one phone connected to the RileyLink
1. Install *Loop* on the new phone (all your settings should be there)
    * Install from&nbsp;[<span translate="no">TestFlight</span>](#install-from-testflight)&nbsp;for *GitHub*  Build or from Xcode for&nbsp;[<span translate="no">Mac-Xcode</span>&nbsp;Build](#build-using-mac-xcode)
1.  As soon as you install *Loop* on the new phone, go ahead and disable Closed Loop.
    * Keep closed loop disabled until you complete the full transfer and checkout.

#### Install from *TestFlight*

* Open *TestFlight* app on new phone
* Install *Loop* on your new phone from *TestFlight*

#### Build using Mac-Xcode

* Open Xcode – use the same build as you used for the old phone
* Plug in the new phone to the computer (trust phone/computer) and hit build
* Build *Loop* on the new phone

### Prepare to Change *Loop* Phones

On old phone (if available):

1. *Loop* app, turn off the slider for the RileyLink if using Medtronic or Eros Pods
    * Do not delete the pump; if using pods, this cannot be reversed
1. Phone Settings, Bluetooth
    * Forget the connections to the CGM (Dexcom or&nbsp;<span translate="no">Libre</span>)
    * Do not forget anything that says&nbsp;<span translate="no">TWI_BOARD</span>&nbsp;or&nbsp;<span translate="no">NXP_BLE</span>&nbsp;(this is your&nbsp;<span translate="no">DASH</span>&nbsp;pod)
1. Phone Settings, Bluetooth: Disable Bluetooth

### Transfer Pump

Bluetooth must be off on the old phone.

* On the new phone, examine the pump status
    * If everything transfered, your new phone should be communicating with your pump
    * If using a RileyLink device and it doesn't show as connected, try a power cycle on the device
    * If you need to start a new pod, do it now
* If necessary, delete the pump type and add it back

### Transfer CGM

It is now time to transfer the CGM to the new phone.

* [Dexcom CGM](#dexcom-cgm)
* [<span translate="no">Libre</span>&nbsp;CGM](#librecgm)

#### Dexcom CGM

The Dexcom app might have transferred successfully, but it’s not a bad idea to install that fresh from the App Store on the new phone. Doing so may be required.

* You need your Dexcom Transmitter ID or 4-digit code (for G7)
* On the new phone, in *Loop*, delete Dexcom as your CGM so you can pair the new phone to the Dexcom app
* On the new phone, open the Dexcom app and pair to the transmitter (G5, G6 or One) or enter the four-digit code for G7
    * You can keep using your current sensor session
    * You indicate you are starting a new sensor (it’s not really new)
        * G5, G6 or ONE, enter transmitter ID
            * If you enter no code, you will be warned that calibrations are required (don't worry)
            * When the app pairs with the tranmistter, it picks up the current session, and calibrations are not required
        * G7, enter 4-digit code
    * Within 5 to 10 minutes, Dexcom app should read the current session and keep going

* Wait for Dexcom to connect
* On new phone, add the CGM to *Loop*

#### <span translate="no">Libre</span>&nbsp;CGM

Placeholder for&nbsp;<span translate="no">Libre</span>&nbsp;CGM instructions. Suggested procedures from the community are encouraged.

* On the new phone, in *Loop*, delete&nbsp;<span translate="no">Libre</span>&nbsp;as your CGM
* On the new phone, in *Loop*, add&nbsp;<span translate="no">Libre</span>&nbsp;as your CGM
* Wait for&nbsp;<span translate="no">Libre</span>&nbsp;to connect

### Ready to *Loop*

1. Keep closed loop disabled until you complete the full transfer and checkout.

    !!! important "Check Every Setting"
        * Make sure all the basal, ISF, CR, Insulin Selection and ranges are correct
        * Check Dosing Strategy selection
        * Check permissions and notification settings
        * Check Focus mode settings - make sure *Loop* and CGM apps have permission for all Focus modes

1. Do a manual bolus of the smallest possible amount to make sure *Loop* and pump are working.

1. Monitor CGM values to ensure new readings are coming in.

1. Check COB and IOB

    !!! important "<span translate="no">Apple Health</span>&nbsp;History"
        Your COB and IOB may not carry over to your new phone.

        *Loop* reads from&nbsp;<span translate="no">Apple Health</span>&nbsp;and may restore COB and IOB from health – this assumes health is stored on iCloud and synchronized between old and new phone

        If your COB and IOB show up as blank, you can go open loop for 3 to 6 hours.
        
        If you are impatient, you can try this but be cautious:
        
        * Add back your insulin via&nbsp;<span translate="no">Apple Health</span>&nbsp;(on your new phone) to the time that the boluses and positive temp basals were recorded on your old phone:&nbsp;<span translate="no">Apple Health</span>&nbsp;, Insulin Delivery, Add Data.
        * Wait about 5 minutes for that insulin to show up in *Loop* as Active Insulin
        * Finally, add the Carbohydrates to *Loop* by entering them in your Add Carb Entry screen and rolling back the Date/Time wheel to the time of the original entry(ies)

1. Once you are happy with the configuration of *Loop* on your new phone, go ahead and enable closed loop mode again.

### Old Phone

Once you are using *Loop* on your new phone, you can delete the pump from the old phone.

* On the old phone, in the *Loop* app:
    * Delete the pump
* If using DASH pods with direct Bluetooth connection to your phone
    * Go into the old phone Settings -> Bluetooth and turn it back on
    * Forget the pod; it will show up as TWI_BOARD or NXP_BLE

You can either keep the Old Phone as a backup, reset it and turn it in for credit or give it to some deserving individual.
