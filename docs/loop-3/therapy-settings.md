# Therapy Settings

Loop 3 has a special Therapy Settings screen. All the settings configured under Therapy Settings are protected by the same authorization method (FaceID, Fingerprint or Passcode) used to enable the app to issue a manual bolus.

The Therapy Settings were summarized under [Onboarding](onboarding.md#therapy-settings). This page provides more details about each setting.  Please come back to this page after using the app in [Open Loop](../operation/loop/open-loop.md) and review the concepts before enabling [Closed Loop](../operation/loop/close-loop.md).

!!! danger "Placeholder"

    This is a placeholder page - expect revisions.

The order of Therapy Setting Information is:

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

#### Maximum Bolus

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

