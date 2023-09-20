## Overview

Changing phones means you have to rebuild the&nbsp;<span translate="no">Loop</span>&nbsp;app onto the new phone. When you transfer information from your old phone to your new one, all your&nbsp;<span translate="no">Loop</span>&nbsp;information is included and the&nbsp;<span translate="no">Loop</span>&nbsp;icon will appear, but the app will not open until you install&nbsp;<span translate="no">Loop</span>&nbsp;from either&nbsp;<span translate="no">TestFlight</span>&nbsp;(<span translate="no">GitHub</span>&nbsp;Build) or&nbsp;<span translate="no">Xcode</span>&nbsp;(<span translate="no">Mac-Xcode</span>&nbsp;Build).

Some people don't have access to their old phone. There are instructions for handling that on this page. It makes the whole process more stressful, but remember, pods continue to deliver basal rate and Medtronic pumps can be controlled on the pump itself. Use your backup plan until you can get&nbsp;<span translate="no">Loop</span>&nbsp;running on a new phone.

### Forced iOS Update

When you change phones,&nbsp;<span translate="no">Apple</span>&nbsp;will force you to the latest iOS version available for your new phone.

### Prepare Before Upgrade

If you are using Dexcom G7, make sure you keep the 4-digit code for your current sensor.

If you still have your old phone, you can prepare before switching to the new phone.

* Be sure to record your&nbsp;<span translate="no">Loop</span>&nbsp;Settings (screenshots work well)

If you don't have your old phone, hopefully you have an iCloud backup and can use that to transfer your information to your new phone.

!!! tip "Keep the Old Phone Until&nbsp;<span translate="no">Loop</span>&nbsp;is Working on the New One"
    Even if you plan to turn your old phone in for a rebate, you can ask to keep the old one for a week or two. Most vendors will agree to this.

Update your old phone to the latest iOS the hardware supports - this simplifies the automatic transfer process&nbsp;<span translate="no">Apple</span>&nbsp;provides to move all your data and apps from your old phone to your new phone.

!!! abstract "New Phone Checklist for *Browser Build*"
    * The&nbsp;<span translate="no">Loop</span>&nbsp;app will install from&nbsp;<span translate="no">TestFlight</span>&nbsp;onto the most recent iOS
    * If a new version of&nbsp;<span translate="no">Loop</span>&nbsp;is available, we recommend updating and building to the latest [GitHub Update](../gh-actions/gh-update.md)

!!! abstract "New Phone Checklist for <span translate="no">Mac-Xcode</span>&nbsp;Build"
    * Are your [Mac and Xcode versions](../build/xcode-version.md#how-do-all-the-minimum-versions-relate-to-each-other) compatible with the latest iOS version?
    * If not, you should configure and build the app with [Browser Build](../gh-actions/gh-overview.md)

### Different Developer ID

!!! important "Different Developer ID"
    If you need to build&nbsp;<span translate="no">Loop</span>&nbsp;with a different developer ID on the new phone, the settings and pump information will **not** transfer.

    * The new app that you build with the new Developer ID will open and you can [Onboard](../loop-3/onboarding.md)
    * The old app will still be on the phone: find it and delete it to avoid confusion

## Procure a New Phone

1. Procure the new phone and keep the old one (if possible)
    * [<span translate="no">Loop</span>&nbsp;with the old phone](#loopwith-the-old-phone) until it is convenient to switch to the new phone
1. Transfer your information to your new phone
    * Let the new phone vendor help you
    * Use an [iCloud back-up](https://support.apple.com/en-us/HT210217) for the transfer
    * Use both devices with [Quick Start](https://support.apple.com/en-us/HT210216) to transfer from the old to the new phone

### <span translate="no">Loop</span>&nbsp;with the Old Phone

If you cannot keep the old phone, or it is not available, then skip ahead to the [<span translate="no">Loop</span>&nbsp;with the New Phone](#loopwith-the-new-phone).

* You can use the old phone to&nbsp;<span translate="no">Loop</span>&nbsp;until you are ready to switch
* Use WiFi with the old phone and use your new phone as a cellular hot-spot as needed
* Keep the CGM on the old phone
    * If using Dexcom, use the Dexcom app on the old phone
    * If using&nbsp;<span translate="no">Libre</span>;, the&nbsp;<span translate="no">Libre</span>&nbsp;is connected to&nbsp;<span translate="no">Loop</span>&nbsp;on the old phone

## <span translate="no">Loop</span>&nbsp;with the New Phone

### Install&nbsp;<span translate="no">Loop</span>

It is easier if you transfer information from the old phone to the new phone before you install and open&nbsp;<span translate="no">Loop</span>&nbsp;on the new phone. If this is not possible, then you will do the normal [Onboarding](../loop-3/onboarding.md) for a new&nbsp;<span translate="no">Loop</span>&nbsp;app.

1. When you transfer information from your old phone to your new phone, all the&nbsp;<span translate="no">Loop</span>&nbsp;settings files get copied to the new device including information about the pod
    * If the timing works, you can keep the pod if you switch to using the new phone for&nbsp;<span translate="no">Loop</span>&nbsp;after the information transfer and before changing pods with the old phone
    * If this is not possible, you will need to start a new pod with the new phone
    * Medtronic users will have all their information transferred but will only have one phone connected to the RileyLink
1. Install&nbsp;<span translate="no">Loop</span>&nbsp;on the new phone (all your settings should be there)
    * Install from&nbsp;[<span translate="no">TestFlight</span>](#install-fromtestflight)&nbsp;for&nbsp;<span translate="no">GitHub</span>&nbsp; Build or from Xcode for&nbsp;[<span translate="no">Mac-Xcode</span>&nbsp;Build](#build-using-mac-xcode)
1.  As soon as you install&nbsp;<span translate="no">Loop</span>&nbsp;on the new phone, go ahead and disable Closed Loop.
    * Keep closed loop disabled until you complete the full transfer and checkout.

#### Install from&nbsp;<span translate="no">TestFlight</span>

* Open&nbsp;<span translate="no">TestFlight</span>&nbsp;app on new phone
* Install&nbsp;<span translate="no">Loop</span>&nbsp;on your new phone from&nbsp;<span translate="no">TestFlight</span>

#### Build using Mac-Xcode

* Open Xcode – use the same build as you used for the old phone
* Plug in the new phone to the computer (trust phone/computer) and hit build
* Build&nbsp;<span translate="no">Loop</span>&nbsp;on the new phone

### Prepare to Change&nbsp;<span translate="no">Loop</span>&nbsp;Phones

On old phone (if available):

1. <span translate="no">Loop</span>&nbsp;app, turn off the slider for the RileyLink if using Medtronic or Eros Pods
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
* On the new phone, in&nbsp;<span translate="no">Loop</span>, delete Dexcom as your CGM so you can pair the new phone to the Dexcom app
* On the new phone, open the Dexcom app and pair to the transmitter (G5, G6 or One) or enter the four-digit code for G7
    * You can keep using your current sensor session
    * You indicate you are starting a new sensor (it’s not really new)
        * G5, G6 or ONE, enter transmitter ID
            * If you enter no code, you will be warned that calibrations are required (don't worry)
            * When the app pairs with the tranmistter, it picks up the current session, and calibrations are not required
        * G7, enter 4-digit code
    * Within 5 to 10 minutes, Dexcom app should read the current session and keep going

* Wait for Dexcom to connect
* On new phone, add the CGM to&nbsp;<span translate="no">Loop</span>

#### <span translate="no">Libre</span>&nbsp;CGM

Placeholder for&nbsp;<span translate="no">Libre</span>&nbsp;CGM instructions. Suggested procedures from the community are encouraged.

* On the new phone, in&nbsp;<span translate="no">Loop</span>, delete&nbsp;<span translate="no">Libre</span>&nbsp;as your CGM
* On the new phone, in&nbsp;<span translate="no">Loop</span>, add&nbsp;<span translate="no">Libre</span>&nbsp;as your CGM
* Wait for&nbsp;<span translate="no">Libre</span>&nbsp;to connect

### Ready to&nbsp;<span translate="no">Loop</span>

1. Keep closed loop disabled until you complete the full transfer and checkout.

    !!! important "Check Every Setting"
        * Make sure all the basal, ISF, CR, Insulin Selection and ranges are correct
        * Check Dosing Strategy selection
        * Check permissions and notification settings
        * Check Focus mode settings - make sure&nbsp;<span translate="no">Loop</span>&nbsp;and CGM apps have permission for all Focus modes

1. Do a manual bolus of the smallest possible amount to make sure&nbsp;<span translate="no">Loop</span>&nbsp;and pump are working.

1. Monitor CGM values to ensure new readings are coming in.

1. Check COB and IOB

    !!! important "<span translate="no">Apple Health</span>&nbsp;History"
        Your COB and IOB may not carry over to your new phone.

        <span translate="no">Loop</span>&nbsp;reads from&nbsp;<span translate="no">Apple Health</span>&nbsp;and may restore COB and IOB from health – this assumes health is stored on iCloud and synchronized between old and new phone

        If your COB and IOB show up as blank, you can go open loop for 3 to 6 hours.
        
        If you are impatient, you can try this but be cautious:
        
        * Add back your insulin via&nbsp;<span translate="no">Apple Health</span>&nbsp;(on your new phone) to the time that the boluses and positive temp basals were recorded on your old phone:&nbsp;<span translate="no">Apple Health</span>&nbsp;, Insulin Delivery, Add Data.
        * Wait about 5 minutes for that insulin to show up in&nbsp;<span translate="no">Loop</span>&nbsp;as Active Insulin
        * Finally, add the Carbohydrates to&nbsp;<span translate="no">Loop</span>&nbsp;by entering them in your Add Carb Entry screen and rolling back the Date/Time wheel to the time of the original entry(ies)

1. Once you are happy with the configuration of&nbsp;<span translate="no">Loop</span>&nbsp;on your new phone, go ahead and enable closed loop mode again.

### Old Phone

Once you are using&nbsp;<span translate="no">Loop</span>&nbsp;on your new phone, you can delete the pump from the old phone.

* On the old phone, in the&nbsp;<span translate="no">Loop</span>&nbsp;app:
    * Delete the pump
* If using DASH pods with direct Bluetooth connection to your phone
    * Go into the old phone Settings -> Bluetooth and turn it back on
    * Forget the pod; it will show up as TWI_BOARD or NXP_BLE

You can either keep the Old Phone as a backup, reset it and turn it in for credit or give it to some deserving individual.
