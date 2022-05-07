# Onboarding

## First Time Using Onboarding

The first time you build Loop-dev on a device, you will need to go through the onboarding process. This link shows a [video of onboarding](https://drive.google.com/file/d/1NkS-YGREFn1UBmBbOjsD2Yy0ZUyEYM1l/view?usp=sharing) with the pre-release version under test in March 2022.

* If you build Loop-dev over Loop 2.2.x on your device, the onboarding remembers the settings, previously saved overrides and your current pod or pump information is maintained. (Yes, you can build Loop-dev and keep using the same pod.)

* If you build Loop-dev onto a device without an existing Loop app and you have a Nightscout site, you can enter your Nightscout URL (remember to use https: with the "s") and API Secret and it will ask if you want to import your settings from your Nightscout profile. This includes all the overrides you have previously saved.

* If you are building on a device that does not have an existing Loop app and you choose not to use Nightscout, then you must add settings (click on the row to edit or + to add a row) as you are taken through each screen.

You are presented with an information screen describing the setting (with a continue button) followed by your current settings (if available), which you must confirm to keep - or can modify and then confirm to change. Depending on the device you are using, you may need to scroll down to see the Continue or Save buttons for each setting. Once you have been walked through all the Therapy Settings, there is a final review and confirm all Therapy Settings screen.

!!! warning "Check Imported Settings"

    The new onboarding forces you to check all your imported [Therapy Settings](#therapy-information) but there may be other settings you need to check as well.

    * Dosing Strategy: may be at the default value of `Temp Basal Only`, even if you were using `Automatic Bolus` with Loop 2.x.x
    * Overrides: verify these are populated as expected

### Entering and Editing Values

There are some nice features when entering your settings with Loop-dev.

* If you want more information about the specific therapy setting, tap on the information icon.
* When you tap +, you can add an entry to any time-slot that does not already have an entry
    - Adjust the time and value(s) as desired
    - Tap Add to include this entry in your schedule
* If a time-slot has an entry, you can tap on it to edit it
    - You can change the time within the constraint of the time entries before and after the slot you are editing
    - You can edit the value to any allowed value
* If you want to delete one or more entries, tap on Edit
    - Tap the red icon to the left of the time-slot you want to delete and select delete
    - Continue until done, then tap Done


### Therapy Information

The order of Therapy Setting Information is:

* Glucose Safety Limit
    * Same as suspend threshold for Loop 2.2.x, but with a 3-hour time window
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
        * Therapy Settings -> Insulin Model is used to distinguish between adults and children for "rapid" insulin
        * Pump Settings -> Insulin Type is used to select the specific brand of insulin, e.g., Novolog, Humalog, Apidra, Fiasp, Lyumjev, etc
        * The ultra-rapid insulins: Fiasp and Lyumjev have only a single model - the adult/child therapy setting selection is irrelevant for those insulin types


## Onboarding Details

Some of the onboarding screens are shown below. Depending on your device resolution, you may need to scroll down to see the entire screen. Only the top portion of any given screen is shown in these graphics.

If you have not already read it, please review the [First Time Using Onboarding](#first-time-using-onboarding) now


### Welcome Screens

The graphic below, shows the initial Welcome Screen, with a modal alert.


#### What is a Modal Alert?

!!! info "Modal Alert"

    Loop-dev has many updates to the user experience.  A modal alert is a small window that shows up on top of your app with information that you must acknowledge, as shown in the graphic below.  You will see a lot of these.


![first two welcome screens when onboarding](img/welcome-menus-x2.svg){width="500"}



### Nightscout Selection

![Nightscout screens when onboarding if select Use Loop with Nightscout](img/nightscout-menus-x2.svg){width="500"}

&nbsp;

### Therapy Settings

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

### Therapy Settings Review

Once these are all entered, then the Therapy Settings screen is shown for your review. You must scroll down to see all settings and reveal the Save Settings button.  Only the top and bottom portions are shown, the other settings were not captured for this graphic.

![verify that all therapy settings are correct](img/therapy-setting-review-x2.svg){width="500"}


&nbsp;

### Notifications and Bluetooth

Once you save settings, Loop asks to send notifications and use Bluetooth

![enable notifications and BLE](img/notify-ble-x2.svg){width="500"}

&nbsp;

## CGM and Pump

If you are building over an existing app, your CGM and pump selections should have carried over.

If you need to add a [CGM](loop-3-cgm.md) or [Pump](loop-3-pump.md) follow the links.

