## New with Loop 3

This page discusses some features new with Loop 3.

## Remote Carb / Bolus

Loop 3 has a Remote Carb and Remote Bolus feature to enable remote caregivers to better assist the person who needs support managing with Loop. This requires the Loop user have a Nightscout site. Please review these pages:

* [Remote Overview](../nightscout/remote-overview.md)
* [Remote Configuration](../nightscout/remote-config.md)
* [Remote Commands](../nightscout/remote-commands.md)
* [Remote Errors](../nightscout/remote-errors.md)
* [<span translate="no">Loop Caregiver</span> App](../nightscout/loop-caregiver.md)

## **New with Loop 3.4.0**

## Algorithm Experiments

Two algorithm experiments have been added to dev. These are <span translate="no">Glucose Based Partial Application</span> and <span translate="no">Integral Retrospective Correction</span>. They can be viewed on the Loop Settings screen just below Therapy Settings and Usage Data Sharing as shown in the graphic below:

![algorithm experiments](img/algorithm-experiments.svg){width="650"}
{align="center"}

### <span translate="no">Glucose Based Partial Application</span> (<code>GBPA</code>)

??? abstract "Do you want to know more? (Click to open/close)"
    * Originally proposed as [Loop PR 1988](https://github.com/LoopKit/Loop/pull/1988)

<span translate="no">Glucose Based Partial Application</span> is only used when <code>Automatic Bolus</code> (AB) is selected for <code>Dosing Strategy</code>

* This modification **does not affect the recommended dose**, only how quickly the recommended dose is automatically delivered

When AB is selected and <code>GBPA</code> is enabled, the percentage of the recommended dose delivered per Loop cycle ranges from 20% to 80% based on glucose level and user selected correction range. (Without <code>GBPA</code> enabled, AB uses a fixed 40% percentage regardless of glucose level.)

* Partial Application = 20% when glucose is at or below the users correction range lower value (including overrides) plus 10 mg/dL (0.6 mmol/L)
* Partial Application increases linearly from 20% to 80% up to a glucose level of 200 mg/dL (11.1 mmol/L)
* Partial Application is 80% when glucose level is above 200 mg/dL (11.1 mmol/L)

#### Insulin Delivery Using <code>GBPA</code>

Loop makes a prediction and recommends an insulin dose based on your settings and your glucose, insulin and carb history. The selected <code>Dosing Strategy</code> (<code>Automatic Bolus</code> with or without <code>GBPA</code> or <code>Temp Basal Only</code>) only changes how quickly that recommended dose is delivered.

This example assumes Loop recommends 1 U (at time 0) and future glucose values match Loop's prediction for each successive 5-minute update. In other words, over half an hour, Loop provides about 1 U of insulin above that delivered by the scheduled basal rate.

The tables below show Automatic Bolus patterns, using a pump minimum bolus increment of 0.05 U, for several application factors. When using <code>GBPA</code>, the application factor can vary with glucose, but that is ignored for this **simplified example**.

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

The <code>Temp Basal Only</code> <code>Dosing Strategy</code> provides about 17% of the recommended bolus each 5-minute interval. The minimum <code>GBPA</code> application factor of 20% was selected to be similar to that rate for lower glucose values. Initially, an application factor of 20% delivers insulin more quickly than <code>Temp Basal Only</code>, but by the end of 30 minutes, the basal program inside the pump keeps track of how much is delivered to reach the **rate** requested, acheiving the full 1 U (**for this example**).

### <span translate="no">Integral Retrospective Correction</span> (<code>IRC</code>)

??? abstract "Do you want to know more? (Click to open/close)"
    * Originally proposed in [Loop Issue 695](https://github.com/LoopKit/Loop/issues/695)
        * This was tested in a few forks but not included into dev until recently
        * Initial merge into dev: [Loop PR 2008](https://github.com/LoopKit/Loop/pull/2008)
    * Updated with a modification to limit stacking of <code>IRC</code> with Glucose Momentum: [Loop PR 2028](https://github.com/LoopKit/Loop/pull/2028)

    The <code>IRC</code> term is described in this (updated) [comment](https://github.com/LoopKit/Loop/issues/695#issue-310265141) in Loop Issue 695 which  includes plots and equations. Some of the information in that comment is repeated below: [Important points about <code>IRC</code>](#important-points-about-irc).

    If you want to look at the code for RC and IRC, examine these files found in LoopKit/LoopKit:

    * RetrospectiveCorrection code: [StandardRetrospectiveCorrection.swift](https://github.com/LoopKit/LoopKit/blob/675655b833bcd5aef2391c47562b57a213bfffb4/LoopKit/RetrospectiveCorrection/StandardRetrospectiveCorrection.swift)
    * IntegralRetrospectiveCorrection code: [IntegralRetrospectiveCorrection.swift](https://github.com/LoopKit/LoopKit/blob/675655b833bcd5aef2391c47562b57a213bfffb4/LoopKit/RetrospectiveCorrection/IntegralRetrospectiveCorrection.swift)


<span translate="no">Integral Retrospective Correction</span>, when enabled:

* changes the Loop prediction model and thus can affect the recommended dose
* applies to both Dosing Strategies: <code>Temp Basal</code> or Automatic Bolus

Refering to the [Algorithm: Prediction](../operation/algorithm/prediction.md) page:

* When <code>IRC</code> is disabled (default), the equation used to predict glucose continues to be:

$$ BG[t] = Insulin[t] + Carb[t] + RetrospectiveCorrection[t] + Momentum[t] $$

* When <code>IRC</code> is enabled that equation changes to:

$$ BG[t] = Insulin[t] + Carb[t] + IntegralRetrospectiveCorrection[t] + Momentum[t] $$

Note that the Momemtum term does not just add to the other effects; it is actually more complicated (and also more challenging to describe in simple math terms).

The Retrospective Correction section of the [Predicted Glucose Chart](../loop-3/displays-v3.md#predicted-glucose-chart) is updated when <code>IRC</code> is enabled, as shown in the graphic below. The `Integral effect`, inside lower blue rectangle, is the difference between the <code>IRC</code> and <code>RC</code> calculations.

![predicted glucose retrospective section with irc disabled and enabled](img/glucose-details-irc.svg){width="400"}
{align="center"}



#### Important points about <code>IRC</code>:

1. Known risk factors compared to standard Loop: 
    * With <code>IRC</code> turned on, Loop will likely increase insulin corrections in response to persistent discrepancies between observed and predicted glucose motion, which may increase the risks of hypoglycemia
    * <code>IRC</code> may also lead to increased oscillations ("roller-coaster") in glucose responses
    * Both of these risk factors are higher if the user's setting value for Insulin Sensitivity (ISF) is too low
    * Increasing ISF setting value tends to mitigate these risks but it is impossible to offer any guarantees for anything around T1D

2. Compared to standard <code>RC</code>, <code>IRC</code> is more likely to improve glucose control in the following scenarios:
    * Glucose remaining high or decreasing slower than expected due to temporarily reduced insulin sensitivity or due to poor site absorption
    * Glucose trending low faster than expected due to temporarily higher insulin sensitivity
    * Glucose spikes due to unannounced meals
    * Glucose remaining high (or trending low) on tail ends of meals where carbs entered were underestimated (or overestimated)
    * Glucose remaining elevated due to unannounced protein+fat effects
    * Glucose staying above (or below) the correction range due to too low (or too high) basal rate settings

3. In some scenarios <code>IRC</code> does not differ from standard Loop <code>RC</code>

    * Regardless of the current glucose level, neither <code>RC</code> nor <code>IRC</code> is adding to the glucose forecast during the times when the absorption rate of announced carbs is greater than the minimum absorption rate.
    * Neither <code>RC</code> nor <code>IRC</code> effects depend on glucose level; both depend on discrepancies between predicted and actual glucose responses.

4. Please do not expect immediate or very substantial improvements in blood glucose control. A one-time success after turning <code>IRC</code> on does not really mean that <code>IRC</code> "works" - this could just as well be a temporal coincidence. Some ways to decide if <code>IRC</code> could be safe and effective for you include:
    * Responses to unannounced meals - spikes should in general be somewhat lower than with standard Loop, but there should also be no follow-up lows
    * Nighttime responses over a few weeks - highs or lows should be less frequent compared to standard Loop; at the wake-up time blood glucose should in general be closer to the correction range.

## Favorite Foods

This feature allows you to save Favorite Foods.

A new row on the <span translate="no">Loop</span> app Settings screen, see graphic below, provides access to create and edit your <span translate="no">Favorite Foods</span>.

![favorite foods feature](img/favorite-foods.svg){width="300"}
{align="center"}

In the example meal entry shown below:

1. The Favorite Food row (at the bottom) is tapped
1. The desired Favorite Food is selected

At this point the meal can be saved by tapping the Continue button, or the user can modify the time (typical) or any other of the carb entry rows before tapping Continue.

![carb entry with favorite foods feature](img/favorite-foods-carb-entry.svg){width="500"}
{align="center"}

Note that to create a Favorite Food on the Carb Entry screen, an icon must be selected by typing on the plate icon and choosing one of the specific food emoji icons. The standard Lollipop, Taco, Pizza icons can be selected at that level, but choosing them at the top level is not sufficient to enable the Save as Favorite button. The favorite food examples seen in the graphic above were created in the Favorite Foods Settings row. The taco was chosen to go with the absorption time chosen.

## **New with Loop 3.0.0**

## Loop 3 Screens

!!! info "Loop 3 Screens"
    One thing you may notice on some screens is the primary button, with associated information message, is always visible at the bottom of even small screens.  You may need to scroll to see intermediate rows. 
    
    For example, if the default action on a bolus screen is to deliver the recommended bolus, that button is visible and active. The button remains fixed as other portions of the screen are scrolled up and down. When you make changes to selections, then the information displayed and the button label updates to reflect the action taken if you tap on the button.
    
    There are other screens, like the Onboarding and Therapy Settings screens, where you should read all the provided information.  Those screens require you to scroll to the bottom before being able to hit `Continue` or `Save`.

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
    * Go to the non-pump insulin screen and enter the bolus amount you've decided to take and select the model if a different from your pump
        * Don't forget to actually take the insulin
        * Add the carb entry and save carbs without bolusing

1. Tap on either of the insulin charts (Active Insulin or Insulin Delivery) on the home screen to display the `Insulin Delivery Screen`. This screen has 3 tabs.
    * **Event History** (default) is similar to Loop 2.2.x; however, the event history from a prior pod is not displayed once it is deactivated
    * **Reservoir** is similar to Loop 2.2.x; however, the reservoir value from a prior pod is not displayed once it is deactivated
    * **Non-Pump Insulin** is a new feature with Loop 3


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
        * Once the user selects `Done` on the keyboard display, the entered value is displayed on the `Bolus` row and the `Log Dose` button changes from gray to blue
        * Tap on `Log Dose` to record or `Cancel` to quit

![entering non-pump insulin into Loop](img/non-pump-insulin.svg){width="500"}


## Bolus Entry

The bolus following carbs (`Meal Bolus`) and manual bolus (`Bolus`) screens are updated from Loop 2.2.x version. There is still a predicted `Glucose` chart that actively updates as the bolus value is updated and various buttons. 

* With Loop 2.2.x
    * The Recommended Bolus is provided but the default for the Bolus value is 0
    * If the user taps on the Recommended Bolus row, the recommended amount is transferred to the Bolus row
* With Loop 3
    * The Recommended Bolus is provided AND the default for the Bolus is the recommended value
    * If the user taps on the Bolus row, the amount is modified to 0 and the keyboard is opened for entry

!!! info "Blue Means Active"
    * The blue color indicates an active button, whereas a grey button is inactive.
    * The value displayed on the `Bolus` row is blue to indicate if you tap on that, you can edit the value

### Meal Bolus

When the `Meal Bolus` screen is entered following a carb entry or edit action, the active button might be `Save and Bolus` or, if no bolus was recommended, `Save without Bolusing`. The `Save` refers to saving the Carb entry or Carb edit that led to this screen in addition to saving the amount that might be bolused. It can also refer to saving a fingerstick value entered in the Meal Bolus screen.


#### Accept Recommendation

In the graphic below, the user enters carbs and taps continue to display the Meal Bolus screen.

* The left graphic shows a case where a bolus is recommended - tapping on the `Save and Deliver` button saves the carbs and delivers the bolus
* The right graphic shows a case where no bolus is recommended - tapping on the `Save without Bolusing` saves the carbs
* Note that these graphics are taken from a small phone - the left graphic shows all the information at once whereas the right graphic has an extra information message that requires the user to scroll to see the `Recommended Bolus` and `Bolus` rows
* For both graphics
    * Active Carbs and Active Insulin are displayed above the `Glucose` prediction graph - these are accurate at the time this screen is entered (before carbs or bolus are saved)
    * The Bolus Summary is presented below the `Glucose` prediction graph with three rows:
        * `Carb Entry`, the proposed carbs with the time to add the carbs and the absorption time displayed - to modify that information, tap on the `< Carb Entry` button at upper left
        * `Recommended Bolus` displays what Loop recommends for that proposed `Carb Entry`
        * `Bolus` default display is what Loop recommends, but user can edit that value

![meal bolus when bolus is recommended on left and not recommended on right](img/loop-3-meal-bolus-rec.svg){width="900"}
{align="center"}

If a CGM entry arrives while in this screen, a **Bolus Recommendation Updated** [modal message](onboarding.md#what-does-modal-mean) will be displayed and must be acknowledged.

#### Modify Bolus

This section is a continuation of the information presented in the [Accept Recommendation](#accept-recommendation) portion of the `Meal Bolus` section. In the graphic below, the user overrides the recommended bolus.

* The left side shows a modified bolus less than the recommended bolus
* The right side shows a modified bolus greater than the recommended bolus
* Note that the `Glucose` prediction graph updates based off the `Bolus` value, giving the user the opportunity to accept or change their proposed value before tapping `Save and Deliver`
* At the next Loop cycle, the app modifies insulin delivery based on the saved information
    * For the example with bolus less than recommended amount:
        * Loop will **NOT** begin to automatically increase insulin delivery until the current glucose is above the bottom of the `Correction` range
        * The recommendation to add insulin when the current glucose is below the `Correction Range` is only offered as a manual feature and is limited to an amount predicted to maintain glucose above the `Safety Threshold`
    * For the example with bolus greater than recommended amount:
        * Loop will probably issue an automatic temp basal of 0 U/hr
        * This is a common "super-bolus" scenario; in other words, "borrow" basal for the meal bolus to limit post meal spikes
* Remember - the `Glucose` prediction is what happens if you `Save and Deliver` and then no further adjustments are made to insulin delivery by Loop

![meal bolus when bolus recommended is decreased on left and increased on right](img/loop-3-meal-bolus-mod-rec.svg){width="900"}
{align="center"}


### Manual Bolus

When the `Bolus` screen is entered directly from the toolbar, the button choices are `Enter Bolus` if none is recommended, `Deliver` if a value is on the `Bolus` row or `Cancel` using the button on the upper left. The user can also tap on the value on the `Bolus` row to bring up a keyboard to modify that amount. When doing that, the value is automatically set to zero.

There are other alert messages that might be displayed if the pump or CGM is not active.  Those are found on the [Loop 3 Displays](displays-v3.md) page.

The two graphics below are examples of manual bolus screens. 

* In the first graphic, no bolus was recommended
    * If you tap on the `Enter Bolus` button at the bottom, it brings up a screen to enable you to type in an amount and then `Deliver` it. 
    * Alternatively, you can tap the `0` amount in the `Bolus` row and perform the same action as the `Enter Bolus` button
    * If you do not want to override the recommendation, hit the `Cancel` button at upper left.

![manual bolus when no bolus recommended](img/loop-3-manual-bolus-no-rec.svg){width="350"}
{align="center"}

* In the second graphic, a recommended amount is shown
    * If you tap on `Deliver` that recommended dose is delivered
    * If you tap on the value on the `Bolus` row, you can override the amount
    * The amount displayed on the `Bolus` row is modified to 0 U with the first tap - at that point, you may enter a new value or tap `Cancel` using the button at upper left of the screen

![manual bolus when bolus is recommended](img/loop-3-manual-bolus-rec.svg){width="350"}
{align="center"}
