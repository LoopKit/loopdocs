# Onboarding

## New Looper

!!! danger "New Loopers Should NOT Use Loop-dev Before it is Released"
    Once Loop-dev is released, this page will be the first page in the Set Up App section of LoopDocs.
    
    To make life easier for those of us preparing the new documentation, the wording on many pages in the Loop 3 section is set in the future - after the release.
    
    This is **not** an invitation for brand-new loopers to build Loop-dev as their first looping adventure.
    
    After the release, this section will be replaced with the words: If this is your first time using Loop - congratulations!

It is a good idea to review this page, _and the rest of what is now the Loop 3 Section (and will become the Set Up App section once Loop-dev is released),_ before pressing any buttons on your phone with your new Loop 3 app.

As soon as your app builds on your phone, you are guided through the set up process - this is called onboarding. As part of onboarding, there are information screens for each `Therapy Setting`. You are "forced" to acknowledge each screen while onboarding. If you later want to review those informational screens again - they are available on your phone through the [`Therapy Settings`](loop-3-therapy.md) screen.

This link shows a [video of onboarding](https://drive.google.com/file/d/1NkS-YGREFn1UBmBbOjsD2Yy0ZUyEYM1l/view?usp=sharing) with the pre-release version under test in March 2022.

### Entering and Editing Values

There are some mechanics associated with entering and editing values with Loop 3. Come back to this section if you have trouble later when you want to enter or modify a setting.

* If you want more information about a specific therapy setting, tap on the information icon on that screen.
* Some screens only have one value for a given quantity
    * In that case you see the value that you can tap on and edit
    * If you tap on the value and the `Confirm Setting` or `Save` button is inactive (this can happen on the delivery limits screen), simply move the picker value to make the button active
* Some screens allow different values for different times of day
    * During onboarding as a new looper, you must tap the + sign to get the midnight time slot (all scheduled entries must start at midnight)
    * When you tap +, you can add an entry to any time-slot that does not already have an entry
        - Adjust the time and value(s) as desired (the last available time slot is 11:30 pm)
        - Tap Add to include this entry in your schedule
    * If a time-slot has an entry, you can tap on it to edit it
        - You can change the time within the constraint of the time entries before and after the slot you are editing
        - You can edit the value to any allowed value
    * If you want to delete one or more entries, tap on Edit
        - Tap the red icon to the left of the time-slot you want to delete and select delete
        - Continue until done, then tap Done

### What does Modal Mean?

!!! info "Modal Alert or Message"

    A modal alert or message is a small window that shows up on top of your app with information that you must acknowledge.  You will see a lot of these during onboarding and while using the Loop app.
    
## Onboarding Steps

Each of the onboarding steps is presented in order. It is a good idea to follow along on this page while you are entering values into your app for the first time.

### Welcome to Loop

The first screen you will see is the Welcome to Loop screen shown in the graphic below. Tap on `Let's Go` to continue.

![initial welcome screens when onboarding](img/welcome-loop-3.svg){width="250"}
{align="center"}

### Apple Health Permissions

The next set of screens is used to give Loop permission to read and write to Apple Health. In the graphic below, from left to right, tap on the buttons highlighted with red boxes to configure permisions:

* Tap on the `Share with Apple Heath` button
* Tap on the `Turn On All` button in the middle
* Tap on the `Allow` button at upper right

The screen in the right side of the graphic was scrolled to enable the write and read permissions to be visible in that view. You need to enable Health Permissions to get the full capabilities of Loop.


![setting up Apple Health permissions with Loop 3](img/health-loop-3.svg){width="600"}
{align="center"}

You can reach the permissions screen later, if you want to review it. Open the Apple Health app, look at the toolbar at the bottom of the app where it says Sharing. Scroll to the bottom of Sharing and Select Apps, then review the Loop Settings.

!!! warning "Advanced Users Only"
    [What about reading carbohydrates with Loop?](#carb-data-source)
    
### Download Loop Profile from Nightscout

The next screen, shown on the left of the graphic below, enables the user to download existing Loop Profile information from Nightscout. 

* A new Looper would choose the bottom button and enter their settings one at a time. 
* An experienced Looper who also uses Nightscout might choose the top button.
    * In that case, you are taken to the screen on the right of the graphic below to enter your Nightscout URL (remember to use https: with the "s") and API_SECRET. 
    * Once those credentials are accepted, you must confirm that you want to import your settings from your Nightscout profile. 
    * This includes all the overrides you have previously saved.

In either case, every Therapy Setting is presented and the user must enter or confirm the value until all Therapy Settings are reviewed.

&nbsp;

![Nightscout screens when onboarding if select Use Loop with Nightscout](img/nightscout-menus-x2.svg){width="500"}
{align="center"}


### Therapy Settings

The following screens take you through the therapy settings one at a time.

The therapy settings are the heart of how Loop makes predictions. If your settings are not correct, the predictions will not be correct. 

* This is yet another reminder to start with Open Loop after you enter what you think are good settings for Basal, Insulin Sensitivity Factor and Carb Ratio.
* But wait - what are these other settings and what do they mean?
* A brief summary of each therapy setting is provided on this page, but there is a more detailed [Therapy Settings](loop-3-therapy.md) page as well for your review.

#### Glucose Safety Limit

If Loop predicts that your glucose will go below the [Glucose Safety Limit](loop-3-therapy.md#glucose-safety-limit) at any time in the next 3 hours and Loop is in Closed Loop, it will set a temporary basal rate of 0 U/hr in an attempt to prevent that future low.

If you ask Loop for a bolus recommendation, and the current prediction is that your glucose will go below the Glucose Safety Limit at any time in the next 3 hours, no bolus will be recommended.

There are some related settings: [Correction Range](loop-3-therapy.md#correction-range) and [Pre-Meal Range](loop-3-therapy.md#pre-meal-range). The Glucose Safety Limit can never be higher than the lowest of those ranges.

#### Correction Range

The [Correction Range](loop-3-therapy.md#correction-range) is the glucose range that you would like Loop to use when providing automated corrections. Correction range is not necessarily the same glucose range that you have discussed with your endocrinologist; generally the doctor's range may be much wider. For example, you may keep a correction range of 100-110 for Loop, but use a desired glucose range of 80-180 when discussing things with your endo about "time in range".

If you ask Loop for a [manual bolus recommendation](loop-3-features.md#manual-bolus) while your current glucose is below the bottom of the correction range and above the glucose safety limit, Loop will recommend a value that should keep your glucose above the safety limit. Note - this is only if you request the bolus recommendation.  Loop will **not** automatically provide extra insulin, via high temp basal or automatic bolus, until your current glucose is higher than the bottom of the correction range. 


#### Pre-Meal Range

The [Pre-Meal Range](loop-3-therapy.md#pre-meal-range), optional, can be used to as an easy way to get a small amount of insulin delivered before a meal to help control post-meal glucose spikes. If you choose not to enter a value, the [pre-meal icon](../operation/features/premeal.md) in the toolbar will be inactive. If you enter a range and later prefer not to have one, you can remove it later.

If your normal target is 100-110 mg/dL and pre-meal target is 80-80 mg/dL, for example, Loop will give you an extra push to get you to the lower target number before the meal. This early insulin brings you into the meal with a mini-prebolus. The pre-meal target, when activated by pressing on the [pre-meal icon](../operation/features/premeal.md) in the toolbar, will stay active for one hour, until carbs are entered, or until it is manually cancelled...whichever comes first.


#### Basal Rates

Only one basal schedule may be configured in the Loop app and the schedule must start at midnight. 

As a new Looper onboarding with Loop, or anyone onboarding basal rates before a pump is added, you are limited to increments of 0.05 U/hr for basal rates and 0.00 U/hr is not allowed. Put values close to what you actually use because the values entered here affect what is allowed as a maximum basal rate in the [Delivery Limits](#deliver-limits) section.

Once a pump is added, the basal increments will match that for your particular pump. Once you complete onboarding and add your pump, you can then return to Therapy Settings and adjust the Basal rates for your particular pump.

During onboarding, the basal rates are saved by Loop.  Once you've added a pump, those same rates will be saved to your pump. 

##### Medtronic Pump Users

!!! alert ""
    If you will be connecting a Medtronic pump after onboarding:

    * The values entered here will overwrite whatever is in your Medtronic pump when you first connect it
    * For those who build Loop 3 over an existing Loop app with a Medtronic pump attached - you will just be confirming values you used previously
    * If you have values in a [Loopable Medtronic pump](../build/step3.md#check-medtronic-pump-version) that you plan to attach after onboarding - please record those values


#### Delivery Limits

The maximum basal rate and maximum bolus settings are collectively referred to as Delivery Limits.

The Maximum Basal the app allows you to choose will be limited based on the basal rate schedule you just entered as well as pump limits, so make sure you put in sensible values. (There is a back button if you need it.)

##### Medtronic Pump Users

!!! alert ""
    If you will be connecting a Medtronic pump after onboarding:

    * The values entered here will overwrite whatever is in your Medtronic pump when you first connect it
    * Make sure that the Delivery Limit values in the Medtronic pump are equal to or greater than the values you enter while onboarding or you will not be allowed to connect to the pump.


#### Maximum Basal Rate

Maximum basal rate will cap the the maximum temporary basal rate that the Loop is allowed to enact to meet your correction range when you are in closed loop and you have selected a [Dosing Strategy](loop-3-settings.md#dosing-strategy) of Temp Basal Only. Typically, Loop users set their maximum basal rate around 3-4 times their highest scheduled basal rate. When you are first beginning to use Loop, it is wise to start conservative (low) in setting your maximum basal rate. If your settings are incorrect in other areas (basal rates, insulin sensitivity, carb ratio, etc), you may need time to identify where settings need to be adjusted. This process is easier if Loop is given less latitude to set high basal rates. Gradually increase your maximum basal rate as your comfort and confidence in Loop increases. If you need help with your settings adjustment, head over to LoopTips for some [initial settings help](https://loopkit.github.io/looptips/settings/settings/).

#### **Maximum Bolus**

Enter your desired single bolus maximum here. For safety, don't set a maximum bolus limit any higher than your typical large meal bolus. Many people like to set a sub 10 U maximum like 9 or 9.9 U to avoid accidentally typing in a bolus of 10 instead of 1.0 U.

#### Insulin Model

When Loop was originally developed, the fastest insulins available, also know as "rapid acting", had published data for behavior in adults and children. Therefore, Loop offers an Adult or Child model as part of onboarding. If you use a newer "ultra rapid" insulin, the model selected here is irrelevant, but a selection is required.

The specific type of insulin used is set when you select or edit the configuration of your [pump](loop-3-pump.md).

#### Carb Ratios

Your [Carb Ratio](loop-3-therapy.md#carb-ratios) is the number of grams of carbohydrates covered by one unit of insulin.

* At least one carb ratio must be entered
* A daily schedule with varying carb ratio at different times of day can be entered

#### Insulin Sensitivities

Your [Insulin Sensitivity Factor](loop-3-therapy.md#insulin-sensitivities) refers to the drop in glucose expected from one unit of insulin over the entire duration of insulin activity. It may be different than what was used as a correction factor with shots or manual pumping. Loop uses these value(s) every 5 minutes when calculating predicted glucose levels.

* At least one insulin sensitivity factor (ISF) must be entered
* A daily schedule with varying ISF at different times of day can be entered

Loop works best if you have [tested and optimized](https://loopkit.github.io/looptips/settings/settings/) your ISF settings for accuracy. Insulin sensitivities can change for many reasons including waiting too long to change your infusion set. Loop will not auto-detect changes in ISF.

Incorrectly set ISF is the most common cause of roller coaster glucoses for new Loop users. You may need to raise (increase) your ISF value/number to help smooth a roller coaster glucose trend. You can read about that topic more over in LoopTips [here](https://loopkit.github.io/looptips/settings/settings/#3rd-insulin-sensitivity-factor).


### Therapy Settings Review

Once these are all entered, then the Therapy Settings screen is shown for your review. You must scroll down to see all settings and reveal the Save Settings button.  Only the top and bottom portions are shown, the other settings were not captured for this graphic.

![verify that all therapy settings are correct](img/therapy-setting-review-x2.svg){width="500"}


&nbsp;

### Notifications and Bluetooth

Once you save settings, Loop asks to send notifications and use Bluetooth. You need to allow both or Loop will not work properly.

![enable notifications and BLE](img/notify-ble-x2.svg){width="500"}

&nbsp;

## CGM and Pump

If you are building over an existing app, your CGM and pump selections should have carried over.

If you need to add a [CGM](loop-3-cgm.md) or [Pump](loop-3-pump.md) follow the links.

## Experienced Loopers

The first time you build Loop 3 on a device, you will need to go through the onboarding process too. 

* If you build Loop 3 over Loop 2.2.x on your device, the onboarding remembers the settings, previously saved overrides and your current pod or pump information is maintained. (Yes, you can build Loop 3 and keep using the same pod.)

* If you build Loop 3 onto a device without an existing Loop app and you have a Nightscout site, you can enter your Nightscout URL (remember to use https: with the "s") and API_SECRET and it will ask if you want to import your settings from your Nightscout profile. This includes all the overrides you have previously saved.

* If you are building on a device that does not have an existing Loop app and you choose not to use Nightscout, then follow the new Looper [Onboarding Steps](#onboarding-steps).

You will be presented with an information screen describing the setting (with a continue button) followed by your current settings (if available), which you must confirm to keep - or can modify and then confirm to change. Depending on the device you are using, you may need to scroll down to see the Continue or Save buttons for each setting. 


### Check Imported Settings

!!! warning "WARNING"

    The new onboarding forces you to check all your imported [Therapy Settings](#therapy-information) but there may be other settings you need to check as well.

    * Dosing Strategy: may be at the default value of `Temp Basal Only`, even if you were using `Automatic Bolus` with Loop 2.x.x
    * Overrides: verify these are populated as expected
    * Pumps that use a RileyLink: confirm the device is selected and active in the Pump settings screen


### Carb Data Source

Loop 3 does not read non-Loop carbohydrate entries from Apple Health, as previous versions did. It still writes to Apple Health. Some experienced loopers want to modify the code to enable Loop to read carbohydrate records from Apple Health with the full understanding of how that works. The instructions for this code customization option, using a flag set in the LoopConfigOverride.xcconfig file, will be added to the documentation later. For now search in zulipchat.

Users who build Loop 3 over Loop 2.2.x, may find a permission switch to give Loop permission to read carb data from health, but without making the customization mentioned above, changing permission does not change the behavior of Loop.
