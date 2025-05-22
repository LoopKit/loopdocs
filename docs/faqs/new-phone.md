## Overview

!!! info "Time Estimate"
    At least a few hours.

    You can choose to keep Looping on the old phone and swap later. Most vendors give you more than a week to turn in your old device for credit.


!!! abstract "Phone Transition Overview - Detailed steps below"

    **Don't start right before a meal:**
    
    * Choose a time when Loop is stable and won't need much attention

    **Keep your old phone (if you can, connected to WiFi) and use it for the *Loop* app:**

    * Make sure Apple Health from the old phone is uploading to the *iCloud*
    * If you are using the old phone with your *Loop* app:
        * Keep the old phone connected to WiFi when convenient
            * The *Loop* app maintains a 7-day database on the phone and will upload when connected
        * You want the Apple Health records created by the *Loop* app on the old phone to transfer via the *iCloud* to the new phone
    
    **Two methods to transfer your phone information (plan for 1 hour, may be faster):**

    1. Do direct phone-to-phone transfer
        * You will not be able to use your old or new phone during the transfer
        * Both phones need to stay close to each other and on the same WiFi network
    2. Use *iCloud* backup from old phone to transfer information to the new phone
        * You will not be able to use your new phone during the transfer
    
    **What happens after you transfer your phone information:**

    * Use your new phone for everything except the *Loop* app and your CGM app
    * You can keep using your old phone to control your pump and read your CGM until you are ready to switch to the new phone
    * The new phone has the Loop records up until the time the transfer started
        * If you change a pod on the old phone after the transfer
            * Plan to deactivate your pod on the old phone and pair the next pod on the new phone
        * If you change Dexcom on the old phone after the transfer
            * On the new phone, you will need to enter the new Transmitter number (G6) or wait for G7 to automatically connect
        * Glucose, Insulin and Carbohydrate records created on the old phone, after the transfer, will be transferred to the new phone via Apple Health - but this may be slow
    * Plan to be **Open Loop** when you decide to start using the *Loop* app on the new phone - the Glucose, Insulin and Carbohydrate records found on the old phone that occurred after the transfer begins will not be included in the *Loop* records sent to the new phone
    
    **When ready to start using the new phone to control your app:**

    * First turn off Bluetooth on the old phone
    * Review the IOB, COB and glucose trend on the old phone - that determines how long you need to run **Open Loop** on the new phone
    * Then build Loop on the new phone
        * [Browser Build](../browser/phone-install.md#subsequent-times-on-phone){: target="_blank" }: Open TestFlight and Install Loop
            * The TestFlight records were transferred to your new phone so no need to redeem a code
        * Mac Build: Plug the new phone into your computer
            * If you recently built to your old phone, you can use the same download - otherwise, you need to [Download Loop](../build/build-app.md#download-loop){: target="_blank" }
            * Your new phone will have the same name as your old phone - might want to change the display names so the two phones are different so you don't get confused in Xcode
            * You will have to trust your computer on your new phone (and watch)
            * You will need to register your new phone (you can do this with *Xcode*)
            * You may need to enable [Developer Mode](../build/build-app.md#developer-mode){: target="_blank" } if it is not already on
            * If you have trouble building, you should try to reboot phone, watch, quit Xcode, restart computer, delete old [provisioning profiles](../build/updating.md#delete-provisioning-profiles){: target="_blank" } and then ask for help
    
    **Plan to stay in Open Loop until all Glucose, Insulin and Carbohydrate *Apple Health* records transfer:**

    * This can take hours
    * Loop will pick up the missing records from Apple Health for insulin and glucose (but not carbohydrates)
        * If you upload to *Nightscout* or *Tidepool*, the carbohydrates entered with the old phone should be already uploaded so your record will be complete
    * If you have small IOB and COB and glucose is flat, you can probably enable closed loop on the new phone without waiting for the missing records
    * If there are carbs entered on old phone that are still active, plan on a longer time open loop when you transition to the new phone

!!! warning "Plan Ahead"
    * Choose when to change from old phone to new phone
        * Stable glucose
        * No meals planned
    * Plan to use **Open Loop** after the transfer to allow recent Health records to transfer via *iCloud*

## Steps Required

Changing phones means you have to rebuild the *Loop* app onto the new phone. When you transfer information from your old phone to your new one, all your&nbsp;_<span translate="no">Loop</span>_&nbsp;information is included and the&nbsp;_<span translate="no">Loop</span>_&nbsp;icon will appear, but the app will not open until you install&nbsp;_<span translate="no">Loop</span>_&nbsp;from either [*TestFlight*](../browser/phone-install.md#install-app-with-testflight) or [*Mac* with *Xcode*](../build/build-app.md). 

The records on the new phone are from the time you started the transfer from the old phone to the new phone. The more recent records are transferred via Apple Health. You may want to adjust carbs after the transfer because those are not read by the *Loop* app. But if you enter them again and you are uploading to Nightscout or Tidepool - they will show up twice. Best to have COB and IOB close to zero when you start using your new phone.

Some people don't have access to their old phone. There are instructions for handling that on this page. It makes the whole process more stressful, but remember, pods continue to deliver basal rate and *Medtronic* pumps can be controlled on the pump itself. Use your backup plan until you can get&nbsp;_<span translate="no">Loop</span>_&nbsp;running on a new phone.

### Forced iOS Update

When you change phones, *Apple* will force you to the latest iOS version available for your new phone.

### Prepare Before Upgrade

If you are using Dexcom, record the transmitter or sensor number in case it doesn't transfer

* G6: Record the Transmitter number (found in the G6 and the *Loop* app)
* G7: Record the 4-digit Sensor number (pairing code) found in the G7 app under Connections, Sensor

If you still have your old phone, you can prepare before switching to the new phone.

* Be sure to record your&nbsp;_<span translate="no">Loop</span>_&nbsp;Settings (screenshots work well)

If you don't have your old phone, hopefully you have an iCloud backup and can use that to transfer your information to your new phone.

!!! tip "Keep the Old Phone Until the *Loop* app is Working on the New One"
    Even if you plan to turn your old phone in for a rebate, you can ask to keep the old one for a week or two. Most vendors will agree to this.

Update your old phone to the latest iOS the hardware supports - this simplifies the automatic transfer process *Apple* provides to move all your data and apps from your old phone to your new phone.

!!! abstract "New Phone Checklist for Build with Browser"
    * The *Loop* app will install from *TestFlight* onto the most recent iOS
    * If a new version is available, we recommend updating and building to the latest, see [Update with Browser](../browser/bb-update.md){: target="_blank" }

!!! abstract "New Phone Checklist for Build with *Mac*"
    * Are your [Mac and Xcode versions](../build/xcode-version.md#how-do-all-the-minimum-versions-relate-to-each-other){: target="_blank" } compatible with the latest iOS version?
    * If not, you need to install the correct versions on your *Mac*
    * If you cannot do that, you should consider [Build with Browser](../browser/bb-overview.md)

### Different Developer ID

!!! important "Different Developer ID"
    If you need to build the *Loop* app with a different developer ID on the new phone, the settings and pump information will **not** transfer.

    * The new app that you build with the new Developer ID will open and you can [Onboard](../loop-3/onboarding.md)
    * The old app will still be on the phone: find it and delete it to avoid confusion

## Procure a New Phone

1. Procure the new phone and keep the old one (if possible)
    * [Use the Old Phone](#use-the-old-phone-until-ready) until it is convenient to switch to the new phone
1. Transfer your information to your new phone. Your options are:
    1. Use both devices with [Quick Start](https://support.apple.com/en-us/HT210216) to transfer from the old to the new phone
    1. Use an [iCloud back-up](https://support.apple.com/en-us/HT210217) for the transfer
    1. Let the new phone vendor help you

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
    * If the timing works, you can keep the pod when you switch to using the new phone for&nbsp;_<span translate="no">Loop</span>_&nbsp;after the information transfer and before changing pods with the old phone
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
* If necessary, review [*TestFlight* for a Child](../browser/phone-install.md#testflight-for-a-child)

#### Build using *Mac*

Preparatory steps:

* Your new phone will have the same name as your old phone - might want to change the display names so the two phones are different so you don't get confused in Xcode
* If the new phone does not have Developer Mode enabled, wait until you plug it in to try to configure it

When building:

* Open *Xcode*
    * Use the same build as you used for the old phone if you built recently
    * Otherwise, do a fresh download and let the [BuildSelectScript](../build/build-app.md#download-loop){: target="_blank" }  open *Xcode* for you
* Plug in the new phone to the computer
* You will have to trust the computer on the new phone (and watch)
* There should be a modal pop-up in Xcode asking if you want to register the new phone
* You may need to enable [Developer Mode](../build/build-app.md#developer-mode){: target="_blank" } if it is not already on
* Build the app on the new phone

If you have trouble finding the new phone in *Xcode* or trouble building, you should try to reboot phone, watch, quit Xcode, restart computer, delete old [provisioning profiles](../build/updating.md#delete-provisioning-profiles){: target="_blank" } and then ask for help

### Prepare to Change Phone used for the *Loop* App

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
* [<span translate="no">Libre</span>&nbsp;CGM](#libre-cgm)

#### Dexcom CGM

The Dexcom app might have transferred successfully, but it’s not a bad idea to install that fresh from the App Store on the new phone. Doing so may be required.

* You need your Dexcom G6 Transmitter ID or G7 4-digit pairing code (Sensor number)
* On the new phone, in&nbsp;_<span translate="no">Loop</span>_, delete Dexcom as your CGM so you can pair the new phone to the Dexcom app
* On the new phone, open the Dexcom app and pair to the transmitter (G5, G6 or One) or enter the four-digit code for G7
    * You can keep using your current sensor session
    * You indicate you are starting a new sensor (it’s not really new)
        * G5, G6 or ONE, enter transmitter ID
            * If you enter no code, you will be warned that calibrations are required (don't worry)
            * When the app pairs with the tranmistter, it picks up the current session, and calibrations are not required
        * G7, enter 4-digit code if asked, otherwise just wait for it to connect
    * Within 5 to 10 minutes, Dexcom app should read the current session and keep going

* Wait for Dexcom to connect
* On new phone, add the CGM to&nbsp;_<span translate="no">Loop</span>_

#### <span translate="no">Libre</span>&nbsp;CGM

Placeholder for&nbsp;<span translate="no">Libre</span>&nbsp;CGM instructions. Suggested procedures from the community are encouraged.

* On the new phone, in&nbsp;_<span translate="no">Loop</span>_, delete&nbsp;<span translate="no">Libre</span>&nbsp;as your CGM
* On the new phone, in&nbsp;_<span translate="no">Loop</span>_, add&nbsp;<span translate="no">Libre</span>&nbsp;as your CGM
* Wait for&nbsp;<span translate="no">Libre</span>&nbsp;to connect

### Check out the Transfer

1. Stay in **Open Loop** (closed loop disabled) until you complete the full transfer and checkout.

    !!! important "Check Every Setting"
        * Make sure all the basal, ISF, CR, Insulin Selection and ranges are correct
        * Check Dosing Strategy selection
        * Check permissions and notification settings
        * Check Focus mode settings - make sure&nbsp;_<span translate="no">Loop</span>_&nbsp;and CGM apps have permission for all Focus modes

1. Do a manual bolus of the smallest possible amount to make sure&nbsp;_<span translate="no">Loop</span>_&nbsp;and pump are working.

1. Monitor CGM values to ensure new readings are coming in.

1. Check Glucose, Insulin and Carbohydrate records

    !!! important "_<span translate="no">Apple Health</span>_&nbsp;History"
        Your Glucose, IOB and COB may not have correct history on your new phone.

        _<span translate="no">Loop</span>_&nbsp; reads from&nbsp;_<span translate="no">Apple Health</span>_&nbsp;and will restore Glucose and Insulin records if health is stored on iCloud and synchronized between old and new phone - but this can take a long time to synchronize
        
        The *Loop* app does not read Carbohydrates from Apple Health, so stay **Open Loop** if you have high COB from an entry on the old phone

        Be prepared to spend 3 to 6 hours in **Open Loop**.

1. Once you are happy with the configuration of&nbsp;_<span translate="no">Loop</span>_&nbsp;on your new phone, your glucose is being read and your COB and IOB on the new phone is valid, then you can restore **Closed Loop**.

### Old Phone

Once you are using&nbsp;_<span translate="no">Loop</span>_&nbsp;on your new phone, you can delete the pump from the old phone.

* On the old phone, in the *Loop* app:
    * Delete the pump
* If using DASH pods with direct *Bluetooth* connection to your phone
    * Go into the old phone Settings -> *Bluetooth* and turn it back on
    * Forget the pod; it will show up as TWI_BOARD or NXP_BLE

You can either keep the Old Phone as a backup, reset it and turn it in for credit or give it to some deserving individual.
