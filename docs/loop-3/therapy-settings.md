# Therapy Settings

The Therapy Settings were summarized under [Onboarding](onboarding.md#therapy-settings-onboarding). This page provides more details about each setting.

!!! danger "Work in Progress"

    This is page is not complete - expect revisions.

## Authorization Required

Loop 3 has a special Therapy Settings screen that is reached during onboarding and by going through the Loop Settings screen after a pump has been added. 

All the settings configured under Therapy Settings are protected by the same authorization method (FaceID, Fingerprint or Passcode) used to enable the app to issue a manual bolus.

## Details for Therapy Settings

Loop 3 has Guardrails for each of the Therapy Settings. The guardrails are noted under each setting and are summarized in the [Guardrails for Settings](#guardrails-for-settings) quick reference section.

New Loopers may prefer settings that show up outside the "Recommended" range and show yellow font on the picker dial. Those recommendations, in some cases, came from a survey of experienced Loopers.

The Therapy Settings on this page are used for automated insulin delivery, when Loop is in Closed-Loop mode.

!!! abstract "Screens Displayed"
    The screens displayed on this page were acquired during [Onboarding](onboarding.md#therapy-settings-onboarding) and show the full information screens available in the app with the `Continue` button.
    
    When you return to the Therapy Settings after you have onboarded and added a pump, the information screens are shown when you touch the information icon, &#9432;, on the upper right.

### Glucose Safety Limit

Loop will deliver basal and recommend bolus insulin only if your glucose is predicted to be above the Glucose Safety Limit for the next three hours.

![several screens showing glucose safety limit entry](img/loop-3-therapy-setting-safety.svg){width="600"}
{align="center"}

The graphic above shows the default Glucose Safety Limit of 80 mg/dL bottom left and a Glucose Safety Limit of 100 mg/dL bottom right. If you feel more comfortable with a higher limit, then start there - do not let the yellow font influence you. Once you've used Loop for a while, you can revisit this setting.  

Note that the value you select for Glucose Safety Limit will dictate the lowest value on the glucose picker that is available for Correction Range and Pre-Meal Range. Those cannot be lower than the Glucose Safety Limit.

Guardrails for Glucose Safety Limit:

* Code constraint: [67 to 110 mg/dl; 3.7 to 6.1 mmol/L]
* Cannot be adjusted higher than bottom of lowest correction range or your pre-meal range (if those are set)
    * You must consider all three ranges when deciding what is limiting your allowed setting for these three

### Correction Range

Your Correction Range is the glucose value (or range of values) that you want Loop to aim for in adjusting your basal insulin and helping you calculate your boluses.

![several screens showing correction range entry](img/loop-3-therapy-setting-correction.svg){width="600"}
{align="center"}

The graphic above shows the default Correction Range of 100 to 120 mg/dL. Do not let the yellow font discourage you if you want to have a "higher than typical" range to start with. Once you've used Loop for a while, you can revisit this setting.  


* Code constraint: [87 to 180 mg/dl; 4.8 to 10 mmol/L]
* Bottom range can be limited by code constraint AND your selected Glucose Safety Limit

### Pre-Meal Range

Your Pre-Meal Range is used to temporarily lower your glucose target before a meal to impact post-meal glucose spikes.

![several screens showing pre-meal range entry](img/loop-3-therapy-setting-pre-meal.svg){width="600"}
{align="center"}

The graphic above shows the default Pre-Meal Range as empty.  This is the only Therapy Setting that is optional. You can enter a value or range of values during onboarding if you choose. This setting can be edited or deleted later. Once you've used Loop for a while, you can revisit using this option.

If you do not add an entry, the pre-meal icon on the toolbar is disabled.

If you add an entry, the pre-meal icon is activated for 1 hour or until carbs are entered or until the user cancels it.

* Code constraint: [up to 130 mg/dl; 7.2 mmol/L]
* Bottom range is limited by your selected Glucose Safety Limit

### Basal Rates

Your Basal Rate of insulin is the number of units per hour that you want to use to cover your background insulin needs.

* Loop supports 1 to 48 rates per day.
* The schedule starts at midnight and cannot contain a rate of 0 U/hr (as the only entry)

* Limited by your selected pump (or if no pump selected, then generic pump limits apply)
* Limited by Max Basal Rate (if already set)

#### Delivery Limits

Delivery Limits are safety guardrails for your insulin delivery.", comment: "Information about delivery limits

* Click on each of the limits: Max Basal and Max Bolus to display the picker wheel
* You must first move the picker off the default value before it registers - you can restore the picker to the original level once it has been moved

#### Maximum Basal Rate

Maximum Basal Rate is the maximum automatically adjusted basal rate that Loop is allowed to enact to help reach your correction range. Some users choose a value 2, 3, or 4 times their highest scheduled basal rate. Work with your healthcare provider to choose a value that is higher than your highest scheduled basal rate, but as conservative or aggressive as you feel comfortable.

The maximum basal rate entered can be no higher than 6.4 times the highest basal rate in your scheduled basal rates.

### Maximum Bolus

Maximum Bolus is the highest bolus amount that you will allow Loop to recommend at one time to cover carbs or bring down high glucose. If your typical max bolus supports it, consider choosing a value such as 9 U or 9.9 U to avoid accidental entry of values over 10 U when the intended value was 1.5 U.

The maximum bolus is limited by your pump, but it is a good idea to limit it to the maximum you use for a common meal. This only limits the bolus at a single time.

### Insulin 

For fast acting insulin, Loop assumes it is actively working for 6 hours. You can choose from different models for the peak activity.

There is only one model for ultra-rapid insulin. If you use those, this setting is ignored.

* This offers the selection of either the Adult or Child model which will later be applied to any of the "rapid acting" insulins, e.g., Novolog, Humalog or Apidra
* Later on, during Add pump, you can enter the actual type of insulin used in the pump
    * If you use an "ultra rapid" such as Fiasp or Lyumjev, there is only a single model
    * The brand for the "rapid acting" insulins, such as Novolog, Humalog or Apidra can be selected - for these insulins, the model for Adult and Child is slightly different

### Carb Ratios

Your Carb Ratio is the number of grams of carbohydrates covered by one unit of insulin.

* At least one carb ratio must be entered
* A daily schedule with varying carb ratio at different times of day can be entered using the &plus; sign

### Insulin Sensitivities

Your Insulin Sensitivities refer to the drop in glucose expected from one unit of insulin.


## Guardrails for Settings

The Loop app has strict guardrails for some settings and the 3 glucose level settings must be consistent. For example, Loop will not allow you to have a Glucose Safety Limit higher than a Correction Range and therefore limits the glucose picker.

#### Glucose Safety Limit
* Same as suspend threshold for Loop 2.2.x, but with a 3-hour time window
* Code constraint: [67 to 110 mg/dl; 3.7 to 6.1 mmol/L]
* Cannot be adjusted higher than bottom of lowest correction range or your pre-meal range (if those are set)
    * You must consider all three ranges when deciding what is limiting your allowed setting for these three

#### Correction Range
* Code constraint: [87 to 180 mg/dl; 4.8 to 10 mmol/L]
* Bottom range can be limited by code constraint AND your selected Glucose Safety Limit

#### Pre-Meal Range
* Code constraint: [up to 130 mg/dl; 7.2 mmol/L]
* Bottom range is limited by your selected Glucose Safety Limit

#### Basal Rates
* Limited by your selected pump (or if no pump selected, then generic pump limits apply)
* Limited by Max Basal Rate (if already set)

#### Delivery Limits
* Click on each of the limits: Max Basal and Max Bolus to display the picker wheel
* You must first move the picker off the default value before it registers - you can restore the picker to the original level once it has been moved

#### Maximum Basal Rate

The maximum basal rate entered can be no higher than 6.4 times the highest basal rate in your scheduled basal rates.

#### Maximum Bolus

The maximum bolus is limited by your pump, but it is a good idea to limit it to the maximum you use for a common meal. This only limits the bolus at a single time.

#### Insulin Model
* This offers the selection of either the Adult or Child model which will later be applied to any of the "rapid acting" insulins, e.g., Novolog, Humalog or Apidra
* Later on, during Add pump, you can enter the actual type of insulin used in the pump
    * If you use an "ultra rapid" such as Fiasp or Lyumjev, there is only a single model
    * The brand for the "rapid acting" insulins, such as Novolog, Humalog or Apidra can be selected - for these insulins, the model for Adult and Child is slightly different

#### Carb Ratios
* At least one carb ratio must be entered
* A daily schedule with varying carb ratio at different times of day can be entered

#### Insulin Sensitivities
* At least one insulin sensitivity factor (ISF) must be entered
* A daily schedule with varying ISF at different times of day can be entered

