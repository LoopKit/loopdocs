## New with Loop 3

This page discusses some features new with Loop 3.

## Remote Carb / Bolus

Loop 3 has a Remote Carb and Remote Bolus feature to enable remote caregivers to better assist the person who needs support managing with Loop. This requires the Loop user have a Nightscout site. Please review these pages:

* [Remote Overview](../nightscout/remote-overview.md)
* [Remote Configuration](../nightscout/remote-config.md)
* [Remote Commands](../nightscout/remote-commands.md)
* [Remote Errors](../nightscout/remote-errors.md)
* [<span translate="no">LoopCaregiver</span> App](../nightscout/loop-caregiver.md)

!!! warning "WARNING"

    You will be using this feature at your own risk, like any other Loop code you build. It is very important you completely read and re-read the links listed above before getting started.
   
    Be aware:
    
    * Apple limits how many push notifications (used by this feature) can be received on an iOS device
    * If the system feels too many are being sent, it may begin to throttle notifications
        * There is no published limit, but consider limiting it to 1 or 2 per hour
    * When on cellular data, there may be further limitations to protect your data usage

## **New with Loop 3.4.0**

Additional details about the 3.4.0 release are found here: [Version: Releases: 3.4.0](../version/releases.md#loop-v340){: target="_blank" }

## Algorithm Experiments

Two algorithm experiments are now available in the *Loop* app (version 3.4.0 or later). These are _<span translate="no">Glucose Based Partial Application</span>_ and _<span translate="no">Integral Retrospective Correction</span>_. They can be viewed on the Loop Settings screen just below Therapy Settings and Usage Data Sharing as shown in the graphic below:

![algorithm experiments](img/algorithm-experiments.svg){width="650"}
{align="center"}

### <span translate="no">Glucose Based Partial Application</span> (_<span translate="no">GBPA</span>_)

??? abstract "Do you want to know more? (Click to open/close)"
    * Originally proposed as [Loop PR 1988](https://github.com/LoopKit/Loop/pull/1988)

    * Many people used a customization provided by *CustomTypeOne LoopPatches* informally called the switcher patch. It transitioned from Automatic Bolus at higher glucose values to Temp Basal Only at lower glucose values where the user had to select the threshold for the shift external to the *Loop* app.

        * The "switcher" patch is no longer compatible
        * The GBPA feature is intended to replace the functionality of that older customization and is controlled completely inside the *Loop* app

_<span translate="no">Glucose Based Partial Application</span>_ is only used when _Automatic Bolus_ (AB) is selected for _Dosing Strategy_

* This modification **does not affect the recommended dose**, only how quickly the recommended dose is automatically delivered

When AB is selected and _<span translate="no">GBPA</span>_ is enabled, the percentage of the recommended dose delivered per Loop cycle ranges from 20% to 80% based on glucose level and user selected correction range. (Without _<span translate="no">GBPA</span>_ enabled, AB uses a fixed 40% percentage regardless of glucose level.)

* Partial Application = 20% when glucose is at or below the users correction range lower value (including overrides) plus 10 mg/dL (0.6 mmol/L)
* Partial Application increases linearly from 20% to 80% up to a glucose level of 200 mg/dL (11.1 mmol/L)
* Partial Application is 80% when glucose level is above 200 mg/dL (11.1 mmol/L)

#### Insulin Delivery Using _<span translate="no">GBPA</span>_

Loop makes a prediction and recommends an insulin dose based on your settings and your glucose, insulin and carb history. The selected _Dosing Strategy_ (_Automatic Bolus_ with or without _<span translate="no">GBPA</span>_ or _Temp Basal Only_) only changes how quickly that recommended dose is delivered.

This example assumes Loop recommends 1 U (at time 0) and future glucose values match Loop's prediction for each successive 5-minute update. In other words, over half an hour, Loop provides about 1 U of insulin above that delivered by the scheduled basal rate.

The tables below show Automatic Bolus patterns, using a pump minimum bolus increment of 0.05 U, for several application factors. When using _<span translate="no">GBPA</span>_, the application factor can vary with glucose, but that is ignored for this **simplified example**.

The first table shows the bolus delivered each Loop cycle for several application factors. Higher application factors start with higher boluses, but go to zero (indicated by a dash) more quickly.

_Incremental Dose for several application factors when initial recommendation is 1 U_

| Minutes | 20% | 40% | 60% | 80% |
|--:|--:|--:|--:|--:|
|0|0.20|0.40|0.60|0.80|
|5|0.15|0.25|0.25|0.15|
|10|0.15|0.15|0.10|0.05|
|15|0.10|0.10|0.05|  - |
|20|0.10|0.05|  - |  - |
|25|0.05|  - |  - |  - |
|30|0.05|  - |  - |  - |

The second table shows the cumulative delivery. A dash shows recommended dose was delivered. Remember, **this is a simplified example**.

_Cumulative Dose for several application factors when initial recommendation is 1 U_

| Minutes | 20% | 40% | 60% | 80% |
|--:|--:|--:|--:|--:|
|0|0.20|0.40|0.60|0.80|
|5|0.35|0.65|0.85|0.95|
|10|0.50|0.80|0.95|1.00|
|15|0.60|0.90|1.00|  - |
|20|0.70|0.95|  - |  - |
|25|0.75|0.95|  - |  - |
|30|0.80|0.95|  - |  - |

The 20% and 40% application factor columns did not reach 1 U in 30 minutes because the requested dose is smaller than this pump will deliver. The 60% application factor only reached 1 U because tiny doses down to 0.03 U were rounded up to 0.05 U.

When _Dosing Strategy_ is set to _Temp Basal Only_ , Loop provides about 17% of the recommended bolus each 5-minute interval. The minimum _<span translate="no">GBPA</span>_ application factor of 20% was selected to be similar to that rate for lower glucose values. Initially, an application factor of 20% delivers insulin more quickly than _Temp Basal Only_, but by the end of 30 minutes, the basal program inside the pump keeps track of how much is delivered to reach the **rate** requested, acheiving the full 1 U (**for this example**).

### <span translate="no">Integral Retrospective Correction</span> (_<span translate="no">IRC</span>_)

??? abstract "Do you want to know more? (Click to open/close)"
    * Originally proposed in [Loop Issue 695](https://github.com/LoopKit/Loop/issues/695)
        * This was tested in a few forks but not included into dev until recently
        * Initial merge into the *Loop* app: [Loop PR 2008](https://github.com/LoopKit/Loop/pull/2008)
    * Updated with a modification to limit stacking of _<span translate="no">IRC</span>_ with Glucose Momentum: [Loop PR 2028](https://github.com/LoopKit/Loop/pull/2028)

    The _<span translate="no">IRC</span>_ term is described in this (updated) [comment](https://github.com/LoopKit/Loop/issues/695#issue-310265141) in Loop Issue 695 which  includes plots and equations. Some of the information in that comment is repeated below: [Important points about _<span translate="no">IRC</span>_](#important-points-about-irc).

    If you want to look at the code for RC and IRC, examine these files found in LoopKit/LoopKit:

    * RetrospectiveCorrection code: [StandardRetrospectiveCorrection.swift](https://github.com/LoopKit/LoopKit/blob/675655b833bcd5aef2391c47562b57a213bfffb4/LoopKit/RetrospectiveCorrection/StandardRetrospectiveCorrection.swift)
    * IntegralRetrospectiveCorrection code: [IntegralRetrospectiveCorrection.swift](https://github.com/LoopKit/LoopKit/blob/675655b833bcd5aef2391c47562b57a213bfffb4/LoopKit/RetrospectiveCorrection/IntegralRetrospectiveCorrection.swift)


_<span translate="no">Integral Retrospective Correction</span>_, when enabled:

* changes the Loop prediction model and thus can affect the recommended dose
* applies to _Dosing Strategy_ of both _Temp Basal Only_ and _Automatic Bolus_ 

Refering to the [Algorithm: Prediction](../operation/algorithm/prediction.md) page:

* When _<span translate="no">IRC</span>_ is disabled (default), the equation used to predict glucose continues to be:

$$ BG[t] = Insulin[t] + Carb[t] + RetrospectiveCorrection[t] + Momentum[t] $$

* When _<span translate="no">IRC</span>_ is enabled that equation changes to:

$$ BG[t] = Insulin[t] + Carb[t] + IntegralRetrospectiveCorrection[t] + Momentum[t] $$

Note that the Momemtum term does not just add to the other effects; it is actually more complicated (and also more challenging to describe in simple math terms).

The Retrospective Correction section of the [Predicted Glucose Chart](../loop-3/displays-v3.md#predicted-glucose-chart) is updated when _<span translate="no">IRC</span>_ is enabled, as shown in the graphic below. The `Integral effect`, inside lower blue rectangle, is the difference between the _<span translate="no">IRC</span>_ and _<span translate="no">RC</span>_ calculations.

![predicted glucose retrospective section with irc disabled and enabled](img/glucose-details-irc.svg){width="400"}
{align="center"}

#### Important points about _<span translate="no">IRC</span>_:

1. Known risk factors compared to standard Loop: 
    * With _<span translate="no">IRC</span>_ turned on, Loop will likely increase insulin corrections in response to persistent discrepancies between observed and predicted glucose motion, which may increase the risks of hypoglycemia
    * _<span translate="no">IRC</span>_ may also lead to increased oscillations ("roller-coaster") in glucose responses
    * Both of these risk factors are higher if the user's setting value for Insulin Sensitivity (ISF) is too low
    * Increasing ISF setting value tends to mitigate these risks but it is impossible to offer any guarantees for anything around T1D

2. Compared to standard _<span translate="no">RC</span>_, _<span translate="no">IRC</span>_ is more likely to improve glucose control in the following scenarios:
    * Glucose remaining high or decreasing slower than expected due to temporarily reduced insulin sensitivity or due to poor site absorption
    * Glucose trending low faster than expected due to temporarily higher insulin sensitivity
    * Glucose spikes due to unannounced meals
    * Glucose remaining high (or trending low) on tail ends of meals where carbs entered were underestimated (or overestimated)
    * Glucose remaining elevated due to unannounced protein+fat effects
    * Glucose staying above (or below) the correction range due to too low (or too high) basal rate settings

3. In some scenarios _<span translate="no">IRC</span>_ does not differ from standard Loop _<span translate="no">RC</span>_

    * Regardless of the current glucose level, neither _<span translate="no">RC</span>_ nor _<span translate="no">IRC</span>_ is adding to the glucose forecast during the times when the absorption rate of announced carbs is greater than the minimum absorption rate.
    * Neither _<span translate="no">RC</span>_ nor _<span translate="no">IRC</span>_ effects depend on glucose level; both depend on discrepancies between predicted and actual glucose responses.

4. Please do not expect immediate or very substantial improvements in blood glucose control. A one-time success after turning _<span translate="no">IRC</span>_ on does not really mean that _<span translate="no">IRC</span>_ "works" - this could just as well be a temporal coincidence. Some ways to decide if _<span translate="no">IRC</span>_ could be safe and effective for you include:
    * Responses to unannounced meals - spikes should in general be somewhat lower than with standard Loop, but there should also be no follow-up lows
    * Nighttime responses over a few weeks - highs or lows should be less frequent compared to standard Loop; at the wake-up time blood glucose should in general be closer to the correction range.

## Favorite Foods

This feature allows you to save _Favorite Foods_.

A new row on the <span translate="no">Loop</span> app Settings screen, see graphic below, provides access to create and edit your _Favorite Foods_.

![favorite foods feature](img/favorite-foods.svg){width="300"}
{align="center"}

In the example meal entry shown below:

1. The _Favorite Food_ row (at the bottom) is tapped
1. The desired Favorite Food is selected

At this point the meal can be saved by tapping the Continue button, or the user can modify the time (typical) or any other of the carb entry rows before tapping Continue.

![carb entry with favorite foods feature](img/favorite-foods-carb-entry.svg){width="500"}
{align="center"}

Note that to create a _Favorite Food_ on the _Carb Entry_ screen, an icon must be selected by typing on the plate icon and choosing one of the specific food emoji icons. The standard Lollipop, Taco, Pizza icons can be selected at that level, but choosing them at the top level is not sufficient to enable the _Save as Favorite_ button. The favorite food examples seen in the graphic above were created in the Favorite Foods Settings row. The taco was chosen to go with the absorption time chosen.

## Non-Pump Insulin

If insulin is taken from a different source and the user wants to let Loop know, there is a new method in Loop 3.

With Loop 2.2.x, the user manually entered the Insulin dose into the Apple Health app. Loop then imported that value.

With Loop 3, the "old" method still works, but there is a new method for entering this information. This method enables the user to indicate the type of insulin so that the appropriate model is used by Loop. An updated `Glucose` prediction chart is displayed prior to saving the dose.

### Enter non-pump insulin before carbs

!!! warning "WARNING"
    If you are planning to enter non-pump insulin to cover carbs and you do NOT want Loop to automatically start increasing insulin based on the carb entry, enter the non-pump insulin first and then add the carbs.
    
    To find out what Loop recommends, without actually dosing with Loop:
    
    * Wait for a CGM entry (or fingerstick) to appear in the HUD
        * Enter the carbs and continue to the bolus screen, i.e., do not save carbs
        * Note the recommended bolus, but do not actually bolus
        * Back up to the carb entry screen and `Cancel`
    * Go to the non-pump insulin screen and enter the bolus amount you've decided to take, and select the model if it's different from your pump
        * Don't forget to actually take the insulin
        * Add the carb entry and save the carbs without bolusing

1. Tap on either of the insulin charts (Active Insulin or Insulin Delivery) on the home screen to display the `Insulin Delivery Screen`. This screen has 3 tabs.
    * **Event History** (default) lists delivery events from the Pump (does not include times when pump is returned to Scheduled Basal Rates)
    * **Reservoir** This is the reservoir level reported by the attached pump. Pods are treated differently from other pumps because the reservoir does not begin to report until the pod has reached 50 U or below. You may see the previous pod reservoir levels following a pod change.
    * **Non-Pump Insulin** injections can be recorded or edited here

2. Select the `Non-Pump Insulin` tab to bring up the graphic shown below
    * Tap on the &plus; sign (green solid lines)
    * `Log Dose` screen is displayed showing the current `Glucose` prediction
    * The default insulin type is that used by the pump
    * To modify Insulin Type, tap on that row (red dashed lines)
        * Picker wheel allows other insulin types to be selected
        * Note that some insulin types, such as Afrezza are only available for non-pump insulin selection
    * Tap on the `Bolus` row (blue dash-dot lines) to bring up a keyboard
        * The `Glucose` prediction chart updates automatically based on the value entered in the Bolus row
        * Tip, add 0.001 to the actual dose to make it easier to see if reviewing in Apple Health
        * Once the user selects `Done` on the keyboard display, the entered value is displayed on the `Bolus` row, and the `Log Dose` button changes from gray to blue
        * Tap on `Log Dose` to record or `Cancel` to quit

![entering non-pump insulin into Loop](img/non-pump-insulin.svg){width="500"}
