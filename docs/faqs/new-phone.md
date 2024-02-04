## Overview

!!! info "Time Estimate"
    At least a few hours.

    You can choose to keep Looping on the old phone and swap later. Most vendors give you more than a week to turn in your old device for credit.


!!! abstract "Page Summary"

    - Don't start right before a meal - choose a time when Loop is stable and won't need much attention
    - Keep your old phone (if you can) and use it to Loop (connected to WiFi) before switching to the new phone
        * Make sure Apple Health from the old phone is uploaded to the cloud
        * Keep the old phone connected to WiFi after the transfer; you want the Apple Health records created on the old phone to transfer via the cloud to the new phone
            * Warning - it can take hours for Health entries created on the old phone after the transfer was started to show up on the new phone
        * Plan to be Open Loop for a while after switching to the new phone - the glucose, carb and insulin records found on the old phone that occurred after the transfer begins (or you complete the iCloud backup) will not be transferred in the records you send to the new phone
    - Two methods for transfer:
        * Use cloud backup from old phone to transfer information to the new phone
            * You will not be able to use your new phone during the transfer
        * Do direct phone-to-phone transfer
            * You will not be able to use your old or new phone during the transfer
    * What happens after transfer
        * You can keep using your old phone to control your pump and read your CGM until you are ready to switch to the new phone
        * The new phone has the Loop records from the time the transfer started
        * If you change a pod on the old phone after the transfer, it will not be available on the new phone so plan to deactivate your pod on the old phone and pair the next pod on the new phone
        * If you change Dexcom, you just enter a new Transmitter number (G6) or wait for G7 to automatically connect
    * When ready to start using the new phone to loop
        * First turn off Bluetooth on the old phone
        * Review the IOB, COB and glucose trend on the old phone - that determines how long you need to run Open Loop on the new phone
        * Then build Loop on the new phone
            * Browser Build: Open TestFlight and Install Loop
            * Mac Build: Plug the new phone in
                * Your new phone with have the same name as your old phone - might what to change the display name on the phone so you don't get confused in Xcode
                * You will have to trust the new phone and register it
                * If you have trouble building, you should try to reboot phone, watch, quit Xcode, restart computer, delete old provisioning profiles and then ask for help
    * Stay in Open Loop until all glucose, carb and insulin Apple Health records transfer
        * This can take hours
        * Loop will pick up the missing records from Apple Health
        * If you have small IOB and glucose is flat, you can probably enable closed loop on the new phone

!!! warning "Plan Ahead"
    * Choose when to change from old phone to new phone
        * Stable glucose
        * No meals planned
    * Plan to use Open Loop after the transfer to allow recent Health records to transfer via the cloud

## Steps Required

Changing phones means you have to rebuild the *Loop* app onto the new phone. When you transfer information from your old phone to your new one, all your&nbsp;_<span translate="no">Loop</span>_&nbsp;information is included and the&nbsp;_<span translate="no">Loop</span>_&nbsp;icon will appear, but the app will not open until you install&nbsp;_<span translate="no">Loop</span>_&nbsp;from either [*TestFlight*](../gh-actions/gh-deploy.md#install-app-with-testflight) or [*Mac* with *Xcode*](../build/build-app.md). 

The records on the new phone are from the time you started the transfer from the old phone to the new phone. The more recent records are transferred via Apple Health. You may want to adjust carbs after the transfer because those are not read by the *Loop* app. But if you enter them again and you are uploading to Nightscout or Tidepool - they will show up twice. Best to have COB and IOB close to zero when you start using your new phone.

Some people don't have access to their old phone. There are instructions for handling that on this page. It makes the whole process more stressful, but remember, pods continue to deliver basal rate and *Medtronic* pumps can be controlled on the pump itself. Use your backup plan until you can get&nbsp;_<span translate="no">Loop</span>_&nbsp;running on a new phone.

### Forced iOS Update

When you change phones, *Apple* will force you to the latest iOS version available for your new phone.

### Prepare Before Upgrade

If you are using Dexcom G7, make sure you keep the 4-digit code for your current sensor.

If you still have your old phone, you can prepare before switching to the new phone.

* Be sure to record your&nbsp;_<span translate="no">Loop</span>_&nbsp;Settings (screenshots work well)

If you don't have your old phone, hopefully you have an iCloud backup and can use that to transfer your information to your new phone.

!!! tip "Keep the Old Phone Until the *Loop* app is Working on the New One"
    Even if you plan to turn your old phone in for a rebate, you can ask to keep the old one for a week or two. Most vendors will agree to this.

Update your old phone to the latest iOS the hardware supports - this simplifies the automatic transfer process *Apple* provides to move all your data and apps from your old phone to your new phone.

!!! abstract "New Phone Checklist for Build with Browser"
    * The *Loop* app will install from *TestFlight* onto the most recent iOS
    * If a new version is available, we recommend updating and building to the latest [Update with Browser](../gh-actions/gh-update.md)

!!! abstract "New Phone Checklist for Build with *Mac*"
    * Are your [Mac and Xcode versions](../build/xcode-version.md#how-do-all-the-minimum-versions-relate-to-each-other) compatible with the latest iOS version?
    * If not, you need to install the correct versions on your *Mac*
    * If you cannot do that, you should consider [Build with Browser](../gh-actions/gh-overview.md)

### Different Developer ID

!!! important "Different Developer ID"
    If you need to build the *Loop* app with a different developer ID on the new phone, the settings and pump information will **not** transfer.

    * The new app that you build with the new Developer ID will open and you can [Onboard](../loop-3/onboarding.md)
    * The old app will still be on the phone: find it and delete it to avoid confusion

## Procure a New Phone

1. Procure the new phone and keep the old one (if possible)
    * [Use the Old Phone](#use-the-old-phone-until-ready) until it is convenient to switch to the new phone
1. Transfer your information to your new phone
    * Let the new phone vendor help you
    * Use an [iCloud back-up](https://support.apple.com/en-us/HT210217){: target="_blank" } for the transfer
    * Use both devices with [Quick Start](https://support.apple.com/en-us/HT210216){: target="_blank" } to transfer from the old to the new phone

### Use the Old Phone until Ready

If you cannot keep the old phone, or it is not available, then skip ahead to the [Use the New Phone](#use-the-new-phone).

* You can use the old phone to&nbsp;_<span translate="no">Loop</span>_&nbsp;until you are ready to switch
* Use WiFi with the old phone and use your new phone as a cellular hot-spot as needed
* Keep the CGM on the old phone
    * If using Dexcom, use the Dexcom app on the old phone
    * If using *Libre*, the *Libre CGM* is connected to the old phone

## Use the New Phone

### Install the *Loop* App

It is easier if you transfer information from the old phone to the new phone before you install and open&nbsp;_<span translate="no">Loop</span>_&nbsp;on the new phone. If this is not possible, then you will do the normal [Onboarding](../loop-3/onboarding.md) for a new&nbsp;_<span translate="no">Loop</span>_&nbsp;app.

1. When you transfer information from your old phone to your new phone, all the&nbsp;_<span translate="no">Loop</span>_&nbsp;settings files get copied to the new device including information about the pod
    * If the timing works, you can keep the pod if you switch to using the new phone for&nbsp;_<span translate="no">Loop</span>_&nbsp;after the information transfer and before changing pods with the old phone
    * If this is not possible, you will need to start a new pod with the new phone
    * *Medtronic* users will have all their information transferred but will only have one phone connected to the *RileyLink*
1. Install&nbsp;_<span translate="no">Loop</span>_&nbsp;on the new phone (all your settings should be there)
    * [Install from *TestFlight*](#install-from-testflight)<br>or
    * [Build using *Mac*](#build-using-mac)
1.  As soon as you install the *Loop* app on the new phone, go ahead and disable <code>Closed Loop</code>.
    * Keep <code>Closed Loop</code> disabled until you complete the full transfer and checkout.

#### Install from *TestFlight*

* Open *TestFlight* app on new phone
* Install the app on your new phone from *TestFlight*
* If necessary, review [*TestFlight* for a Child](../gh-actions/gh-deploy.md#testflight-for-a-child)

#### Build using *Mac*

* Open *Xcode* – use the same build as you used for the old phone
* Plug in the new phone to the computer (trust phone/computer) and hit build
* Build the app on the new phone

### Prepare to Change Phones

On old phone (if available):

1. _<span translate="no">Loop</span>_&nbsp;app, turn off the slider for the *RileyLink* if using *Medtronic* or *Eros Pods*
    * Do not delete the pump; if using pods, this cannot be reversed
1. Phone Settings, *Bluetooth*
    * Forget the connections to the CGM (*Dexcom* or *Libre*)
    * Do not forget anything that says *TWI_BOARD or *NXP_BLE*(this is your *DASH* pod)
1. Phone Settings, *Bluetooth*: Disable *Bluetooth*

### Transfer Pump

*Bluetooth* must be off on the old phone.

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
* On the new phone, in&nbsp;_<span translate="no">Loop</span>_, delete Dexcom as your CGM so you can pair the new phone to the Dexcom app
* On the new phone, open the Dexcom app and pair to the transmitter (G5, G6 or One) or enter the four-digit code for G7
    * You can keep using your current sensor session
    * You indicate you are starting a new sensor (it’s not really new)
        * G5, G6 or ONE, enter transmitter ID
            * If you enter no code, you will be warned that calibrations are required (don't worry)
            * When the app pairs with the tranmistter, it picks up the current session, and calibrations are not required
        * G7, enter 4-digit code
    * Within 5 to 10 minutes, Dexcom app should read the current session and keep going

* Wait for Dexcom to connect
* On new phone, add the CGM to&nbsp;_<span translate="no">Loop</span>_

#### <span translate="no">Libre</span>&nbsp;CGM

Placeholder for&nbsp;<span translate="no">Libre</span>&nbsp;CGM instructions. Suggested procedures from the community are encouraged.

* On the new phone, in&nbsp;_<span translate="no">Loop</span>_, delete&nbsp;<span translate="no">Libre</span>&nbsp;as your CGM
* On the new phone, in&nbsp;_<span translate="no">Loop</span>_, add&nbsp;<span translate="no">Libre</span>&nbsp;as your CGM
* Wait for&nbsp;<span translate="no">Libre</span>&nbsp;to connect

### Check out the Transfer

1. Keep closed loop disabled until you complete the full transfer and checkout.

    !!! important "Check Every Setting"
        * Make sure all the basal, ISF, CR, Insulin Selection and ranges are correct
        * Check Dosing Strategy selection
        * Check permissions and notification settings
        * Check Focus mode settings - make sure&nbsp;_<span translate="no">Loop</span>_&nbsp;and CGM apps have permission for all Focus modes

1. Do a manual bolus of the smallest possible amount to make sure&nbsp;_<span translate="no">Loop</span>_&nbsp;and pump are working.

1. Monitor CGM values to ensure new readings are coming in.

1. Check COB and IOB

    !!! important "_<span translate="no">Apple Health</span>_&nbsp;History"
        Your COB and IOB may not carry over to your new phone.

        _<span translate="no">Loop</span>_&nbsp; reads from&nbsp;_<span translate="no">Apple Health</span>_&nbsp;and may restore COB and IOB from health – this assumes health is stored on iCloud and synchronized between old and new phone

        If your COB and IOB show up as blank, you can go open loop for 3 to 6 hours.
        
        If you are impatient, you can try this but be cautious:
        
        * Add back your insulin via *Apple Health* (on your new phone) to the time that the boluses and positive temp basals were recorded on your old phone: *Apple Health*, Insulin Delivery, Add Data.
        * Wait about 5 minutes for that insulin to show up in the *Loop* app as Active Insulin
        * Finally, add the Carbohydrates by entering them in your Add Carb Entry screen and rolling back the Date/Time wheel to the time of the original entry(ies)

1. Once you are happy with the configuration of&nbsp;_<span translate="no">Loop</span>_&nbsp;on your new phone, go ahead and enable closed loop mode again.

### Old Phone

Once you are using&nbsp;_<span translate="no">Loop</span>_&nbsp;on your new phone, you can delete the pump from the old phone.

* On the old phone, in the *Loop* app:
    * Delete the pump
* If using DASH pods with direct *Bluetooth* connection to your phone
    * Go into the old phone Settings -> *Bluetooth* and turn it back on
    * Forget the pod; it will show up as TWI_BOARD or NXP_BLE

You can either keep the Old Phone as a backup, reset it and turn it in for credit or give it to some deserving individual.
