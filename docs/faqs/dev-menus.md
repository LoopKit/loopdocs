# Loop dev Preview

Loop users are directed to select a released version of Loop to download during the build process. The next version of Loop is developed under the dev branch and, when ready for testing, the developers ask for volunteers to assist in testing the new code. Please read [What's going on in the dev branch?](branch-faqs.md#whats-going-on-in-the-dev-branch) before deciding to test the dev branch. If you decide to build the dev branch, instructions are found the [Advanced Users Only](../build/step13.md#advanced-users-only) section of Build Step 13.

The Loop dev branch is in a state where there is active testing going on by experienced Loopers.  To assist those Loopers, this preliminary documentation has been prepared. With Loop dev branch, the app screens have an updated appearance and organization.  People familiar with the layout of features in Loop v2.2.x may need to reorient slightly to find particular settings; but for the most part, the layout will be natural to current Loop users.


## First Time With Loop 3

!!! note ""
    Although the LoopWorkspace dev branch (Loop-dev) is not released yet, when it is released it will have a new major version number starting with 3.

The first time you build Loop version 3.x on a device, you will need to go through the [onboarding](#onboarding) process. This link shows a [video of onboarding with Loop-dev](https://drive.google.com/file/d/1NkS-YGREFn1UBmBbOjsD2Yy0ZUyEYM1l/view?usp=sharing).

* If you build Loop-dev over Loop verson 2.x on your device, the onboarding remembers the settings, previously saved overrides and your current pod or pump information is maintained. (Yes, you can build Loop-dev and keep using the same pod.)  

* If you build Loop-dev onto a device without an existing Loop app and you have a Nightscout site, you can enter your Nightscout URL (remember to use https: with the "s") and API Secret and it will ask if you want to import your settings from your Nightscout profile. This includes all the overrides you have previously saved.

* If you are building on a device that does not have an existing Loop app and you choose not to use Nightscout, then you must add settings (click on the row to edit or + to add a row) as you are taken through each screen.

You are presented with an information screen describing the setting (with a continue button) followed by your current settings (if available), which you must confirm to keep - or can modify and then confirm to change. Depending on the device you are using, you may need to scroll down to see the Continue or Save buttons for each setting. Once you have been walked through all the Therapy Settings, there is a final review and confirm all Therapy Settings screen.

### Entering and Editing Values:

There are some nice features of the new user interface that are different from previous (pre-Loop 3.0) versions:

* If you want more information about the specific therapy setting, tap on the information icon.
* When you tap +, you can add an entry to any time-slot that does not already have an entry
    * Adjust the time and value(s) as desired
    * Tap Add to include this entry in your schedule
* If a time-slot has an entry, you can tap on it to edit it
    * You can change the time within the constraint of the time entries before and after the slot you are editing
    * You can edit the value to any allowed value
* If you want to delete one or more entries, tap on Edit
    * Tap the red icon to the left of the time-slot you want to delete and select delete
    * Continue until done, then tap Done

### Therapy Information:

The order of Therapy Setting Information is:

* Glucose Safety Limit
    * Same as suspend threshold for Loop v2.x, but with a 3-hour time window
    * Code constraint: [67 to 110 mg/dl; 3.7 to 6.1 mmol/L]
    * Cannot be adjusted higher than bottom of lowest correction range or your pre-meal range (if those are set)
        * You must consider all three ranges when deciding what is limiting your allowed setting for these three
* Correction Range
    * Code constraint: [87 to 180 mg/dl; 4.8 to 10 mmol/L]
    * Bottom range can be limited by code constraint AND your selected Glucose Safety Limit
* Pre-Meal Range
    * Code constraint: [up to 130 mg/dl; 7.2 mmol/L]
    * Bottom range is limited by your selected Glucose Safety Limit
* Basal Rates
    * Limited by your selected pump (or if no pump selected, then generic pump limits apply)
    * Limited by Max Basal Rate (if already set)
* Delivery Limits
    * Click on each of the limits: Max Basal and Max Bolus to display the picker wheel
    * You must first move the picker off the default value before it registers - you can restore the picker to the original level once it has been moved
* Insulin Model
    * This offers Adult or Child rapid acting models which will later be applied to any of the "rapid acting" insulins, e.g., Novolog, Humalog or Apidra
    * Later on, during Add pump, you can enter more insulin details
        * If you use an "ultra rapid" such as Fiasp or Lyumjev you can select the type in your pump menu (there is only a single model for these insulins)
        * The brand for the "rapid acting" insulins, such as Novolog, Humalog or Apidra can be selected - for these insulins, the model for Adult and Child is slightly different
* Carb Ratios
* Insulin Sensitivities

!!! danger "The most common question"

    - How do I enter the type of insulin I use?
        * Therapy Settings -> Insulin Model is used to distinguish between adults and children
        * Pump Settings -> Insulin Type is used to select the specific brand of insulin, e.g., Novolog, Humalog, Apidra, Fiasp, Lyumjev, etc.

## Loop is Running

The following graphics are taken from an instance of Loop that has been configured and is operating.

### Main Loop Screen

The main Loop screen is similar to earlier versions with a Heads-Up Display at the top (when in portrait mode) with various graphs in the middle and a toolbar at the bottom of the screen. The graphs and the toolbar act similarly to earlier versions, e.g., v2.2.x.  The Settings display shown when tapping on the settings (gear icon) is quite different as described [below](#settings-screen).

![main loop screen when running nominally](img/loop-dev-main.svg){width="300"}

### Heads-Up Display

The Heads-Up Display (HUD) for Loop dev branch has been simplified.  There are only 3 icons (instead of the 5 used up through Loop Versions 2.2.x.). The left icon shows the CGM value, the middle icon indicates Loop status and the right icon show pump status.

#### CGM Icon

Tapping on the CGM icon shows more information about the last CGM reading. The same screen is obtained by tapping on Loop Settings->CGM.  This display includes the time of the last reading to the nearest second, along with other information about that sensor and transmitter. It also has an option to go to the Dexcom app on the same device.

![dexcom information screen from ](img/dexcom-info-menu.svg){width="250"}


### Loop Status Icon

Tapping on the Loop Status Icon provides information about Loop Status.

Examples of Green and Yellow Loop Status are shown in the graphic below. The Red Status says over 15 minutes.  After 20 minutes and every 20 minutes thereafter that Loop stays Red, you will also get a notification (if you enabled notifications).

![left: tap on green loop; right: tap on yellow loop ](img/green-yellow-status-x2.svg){width="500"}


#### Pump Icon

Tapping on the pump icon leads to the [Pump Menu](../operation/loop-settings/pump-commands.md).  These screens have the same information as Loop version 2.2.x, although the order may be slightly different.

For Omnipod users who have selected Automatic Bolus Dosing Strategy, you may want to turn on Confirmation Beeps. In earlier Loop versions, the beep happened for all boluses; with the dev branch, only manually entered boluses beep at you, automated boluses are silent.


### Settings Screen

* Most of the Settings you may be familiar with are reached from Settings by tapping on Therapy Settings
* Nightscout can be added from Settings by tapping on Add Service (if you did not add it as part of onboarding)
* Issue Report is reached from Settings by tapping on Support
    * The Expiration Date for the Loop app is now included in the Issue Report for dev

![composite therapy screen](img/loop-dev-settings.svg){width="250"}

### Loop Widget on Lock Screen

Loop has a widget which can be added to the lock screen. The example graphic below shows the Dexcom G6 widget above the Loop dev widget.

![widget on lock screen, dex above, loop below](img/dex-loop-dev-widget.svg){width="250"}


&nbsp;

## Onboarding

Some of the onboarding screens are shown below. Depending on your device resolution, you may need to scroll down to see the entire screen. Only the top portion of any given screen is shown in these graphics.

If you have not already read it, please review the [First Time With Loop 3](#first-time-with-loop-3) now

&nbsp;

### Welcome Screens:

![first two welcome screens when onboarding](img/welcome-menus-x2.svg){width="500"}

&nbsp;

### Nightscout Selection:

![Nightscout screens when onboarding if select Use Loop with Nightscout](img/nightscout-menus-x2.svg){width="500"}

&nbsp;

### Therapy Settings:

Next are the therapy settings in order (a few graphics are shown, not all screens) and for taller screens, such as the Correction Range screen, you'll need to scroll down to read the entire screen and reveal the Continue button:

* Glucose Safety Limit
* Correction Range

![Instructions for Glucose Safety Limit and Correction Range](img/onboard-safety-target-range-x2.svg){width="500"}

* Pre-Meal Range
* Workout Range
* Basal Rates
* Delivery Limits
* Insulin Model (note - Adult or Child, actual type is associated with pump)
* Carb Ratios
* Insulin Sensitivities

&nbsp;

### Therapy Settings Review:

Once these are all entered, then the Therapy Settings screen is shown for your review. You must scroll down to see all settings and reveal the Save Settings button.  Only the top and bottom portions are shown, the other settings were not captured for this graphic.

![verify that all therapy settings are correct](img/therapy-setting-review-x2.svg){width="500"}


&nbsp;

### Notifications and Bluetooth:

Once you save settings, Loop asks to send notifications and use Bluetooth

![enable notifications and BLE](img/notify-ble-x2.svg){width="500"}

&nbsp;

### Add CGM and Add Pump:

Loop shows the following screen indicating you can Add CGM and Add Pump. If you are building over an existing Loop app, the CGM and Pump are remembered so you will not see this screen.

![therapy settings complete, add cgm and pump](img/add-cgm-pump.svg){width="250"}

The CGM and Pump entry screens are similar to those in the Setup App screens for Loop v2.2.x.  The one exception is when adding the pump, the specific type of insulin is requested.

For those using the DASH pods, the user interface screens have been completely rewritten.  They are self explanatory.  A [video is found here for pairing a DASH pod](https://drive.google.com/file/d/1mN5s8-oorvoa-gbjAaYbnUnl_-vvuhNC/view?usp=sharing). Once the pod starts priming, you may want to skip ahead in the video (it takes about a minute to prime).

### Select Insulin type

The default is Novolog.  Depending on your screen, you may have to scroll down to see the other icons.


![select specific type of insulin when adding pump](img/add-pump-insulin-type.svg){width="500"}
