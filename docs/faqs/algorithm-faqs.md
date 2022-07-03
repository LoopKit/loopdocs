# Algorithm FAQs

## Does Loop "learn" or detect changes in your insulin needs?

The answer is both Yes and No.

Yes in that:

* There is a short-term retrospective analysis built into Loop which will apply a weighted-correction based on the past 60 minutes of blood glucose changes.
* Loop works best if you enter an estimate of carbs and absorption time for meals, but it also is fairly forgiving
    * There are discussions on Insulin Counteraction Effect (ICE) on a number of pages within LoopDocs:
        * [Dynamic Carb Absorption](../operation/features/carbs.md#dynamic-carb-absorption)
        * [Carbohydrate Effect](../operation/algorithm/prediction.md#carbohydrate-effect)
        * [Insulin Counteraction Effect](../operation/features/ice.md)

No in that:

* Loop assumes the settings you've provided are correct.
    * Loop does not adjust or "learn" the [Therapy Settings](../loop-3/therapy-settings.md) portion of Loop parameters directly
        * It keeps those fixed and user controlled, separate from the dynamic part of the Loop algorithm, which does learn based on short-term patterns
        * If outside factors (such as hormones, illness, exercise, medications, etc) affect your underlying Therapy Settings you may need to manually adjust those settings.
* This LoopTips 3-page section on [Settings](https://loopkit.github.io/looptips/settings/overview/) is recommended.


Perhaps in subsequent versions of Loop, auto-adjustment of settings or machine learning could be incorporated. Until then, you will need to tell Loop if your underlying settings change or make temporary adjustments for short term issues.

The use of [Overrides](../operation/features/workout.md) can be quite helpful for short-term changes.

## What does negative Active Insulin mean?

When Loop withholds or suspends some of your scheduled basal insulin, that starts an accumulation of insulin deficit. If you have a kinked cannula and insulin is not delivered, you'd call yourself "lacking insulin" (negative IOB).

When Loop reports negative IOB, it is a sign that Loop has been actively helping you prevent a low blood sugar. If you find significant negative IOB regularly, you probably need to [adjust/test your settings](https://loopkit.github.io/looptips/settings/settings/). Glucose that continues to decrease (away from a meal) when IOB goes negative, is typically a sign that the scheduled basal rate is too high.

!!! abstract "Developer Notes"
    Scheduled basal rates are meant to counteract your endogenous glucose production. Another way of saying this is that Loop expects your body to be producing an amount of glucose at a rate that is handled by your basal insulin settings.

    Your body doesn't really produce glucose at a fixed rate, but that's how it's modeled in Loop.

    "All models are wrong, but some are useful." (Quote attributed to British statistician George E. P. Box.)


## How is IOB calculated?

Insulin on board (IOB) is calculated from the amount of insulin delivered above or below the scheduled basal rate. For each dose of insulin, the insulin model is used to determine how much of that [insulin is active](../operation/algorithm/prediction.md#insulin-effect) over time. Loop is adding up all the amounts over the full Duration of Insulin Action (DIA). The DIA is 6 hours for most rapid insulin in the models used by Loop.

IOB is plotted on the [Active Insulin Chart](../loop-3/displays_v3.md#active-insulin-chart) in the main Loop display.

## How does Loop use Apple HealthKit?

Loop uses Apple HealthKit as long term storage for glucose, insulin and carbohydrates.  But there is more going on than simple storage.

It is important that permissions for Loop be properly configured for the Health app.

* Loop 2.2.x: See [Health Permissions](../build/health.md)
* Loop 3: See [Apple Health Permissions](../loop-3/onboarding.md#apple-health-permissions)

To view the list of data stored in Health

* Tap on the Health icon (red heart) to open the app
* Tap on Blood Glucose, Carbohydrates or Insulin
* Scroll all the way to the bottom
* Tap on Show All Data

!!! example "To Set Blood Glucose, Carbohydrates and Insulin as Favorites"
    * Tap on the Health icon (red heart) to open the app
    * There's a toolbar at the bottom of the screen (always visible in the app)
    * Tap on the Browse icon (bottom right of toolbar)
    * Tap on
        * Other Data for Blood Glucose and Insulin
        * Nutrition for Carbohydrates
    * Tap each item, scroll down to Options section and tap on Add to Favorite
    * Repeat until all three are added
    * Tap on the Summary (bottom left icon of toolbar), Favorites show up first

### Glucose and Apple HealthKit

For Dexcom users with the Dexcom app on the Loop phone, the Dexcom app writes the value to Health with a 3-hour delay.

Loop reads the Dexcom information at the same time the Dexcom app gets the reading from the transmitter. It uses the glucose value to update predictions and stores it in Health.

If you look at your Health glucose readings, you'll notice the Loop icon for the last 3 hours and the Dexcom icon for times earlier than that.

All other CGM are reported with the Loop icon and there is no transition after 3 hours.

You may also notice that the Dexcom numbers get smoothed out. For example, the Dexcom readings, when they first are read from the transmitter may bounce up and down a bit. The Dexcom app will retrospectively smooth the numbers, changing what is displayed in their app compared to the original reading. The last 3 hours of data from Loop does not show that smoothing - it reports the value sent by the transmitter. If you suspect a sensor is not behaving well, check the Loop glucose plots compared to the Dexcom plots to assist in your evaluation. It might be time to confirm glucose with a fingerstick meter as well.

### Carbohydrates and Apple HealthKit

In Loop 2.2.x, if you set Apple Health app permissions to allow it, Loop will read carbohydrates from the Health app. If you give a third-party app permission to store carbohydrate data in Health, and do not realize that Loop reads that information, you might get unexpected insulin delivery based off those carbs. To avoid that unanticipated behavior, the directions tell you to set permissions to allow Loop to write to carbohydrate storage but not read.

In Loop 3, the option to read from Health carbohydrates is explicitly disabled and can only be enabled by setting up special parameters when you build the app. The insructions for the code customization are not in LoopDocs yet. If it is important to you to use a third-party app to record carbohydrates and have Loop read the information and automatically dose with insulin, [ask for help in zulipchat](../index.md#finding-help).

### Insulin and Apple HealthKit

The relationship between Loop and Apple HealthKit is very important to understand if you ever need to do one of these actions:

* Dose insulin from another source (injection, smart pen)
* Remove insulin that wasn't really given (failed site or forgot to reattach a tubed pump)

!!! danger "Be Cautious"
    Allowing users to delete events is fairly risky. If a user deletes a dose accidentally, or does not understand the IOB impact while in Closed Loop, then Loop may start giving insulin that is not needed.

    One method to deal with insulin that wasn't given is to go Open Loop for 3 to 6 hours. However, if you take care, you can remove insulin from Loop.


!!! abstract "Developer Notes: Pump Events and Insulin Delivery"
    Loop stores Pump Events separately from Insulin Delivery. With permissions set to allow Loop to read insulin from Health (recommended), the Insulin Delivery store contains doses entered from Health as well as the subset of pump events that represent doses.

    Pump Events are displayed by tapping an insulin chart on the main screen and viewing the Event History tab.

    When you delete a pump event using the Event History interface in Loop, the associated entry in Insulin Delivery is not deleted.

#### Bolus

* When Loop commands the pump to provide a bolus, either manual or automatic, it is shown in the Loop Event History and in the Health app insulin data list. (It may take a Loop Cycle or two to show up in Health, but it will appear.)
* When you add insulin, such as from an injection, to the Health app, Loop reads it and adds it to IOB. It will not be added to the Event History because this is not a pump event.
    * Loop 3 adds a new feature that allows you to add non-pump insulin from within the app instead of requiring you to add it inside the Health app
* If you delete an entry from the Loop Event History list, but leave that same entry in Health, Loop reads it back from Health.
    * It will not show up in the Event History, but it will still contribute to IOB.
    * You must delete a pump event from both Loop Event History and Health data, best if you do this within one Loop Cycle.
    * If that dose showed up in Event History but you could not find it in Health, look again after the next Loop cycle.
* If you delete an entry from Health, but leave that same entry in Loop Event History, Loop reports it to Health again.
    * You must delete a pump event from both the Loop Event History list and Health data, best if you do this within one Loop Cycle.

!!! tip "Pro Tip"
    Write on a piece of paper the times and values you think you should delete.

    Look at those values in both Loop Event History and Health Insulin data list.

    Record what Loop is reporting as IOB.

    Review the values one more time, and then delete those entries in both places. Review IOB again. If you made a mistake, you can refer to that written list and adjust appropriately.

#### Basal

Loop keeps track of how much basal is delivered so the IOB is properly reported. In older versions of Loop, there may be occasional display glitches, but the **internal** accounting is correct and updates every Loop Cycle.

!!! abstract "Developer Notes: Scheduled Basal is Not a Pump Event"
    Scheduled basal is not a pump event so you will not see it listed in the Event History tab.

    Scheduled basal does not affect IOB when delivered as scheduled.

    The Insulin Delivery store keeps track of the insulin delivered via scheduled basal.

Loop updates the amount of insulin delivered through basal (both scheduled and temporary) to Health at regular intervals - this does not happen every Loop Cycle when basal rates are not changing. The updates to Health happen:

* At midnight
* When the scheduled basal rate changes
* When a temporary basal rate changes

A simple example to illustrate this - for a pump with smallest insulin delivery of 0.05 U:

| <div style="width:55px"></div> Schedule | <div style="width:55px"></div> Temp Basal (TB) | <div style="width:55px"></div> Health | Explanation |
|---|---|---|---|
|12:00 AM<br>0.4 U/hr | --- | --- | Start of Day / Start of Example |
|06:00 AM<br>0.5 U/hr | --- | 06:00 AM<br>Basal<br>2.4 U | Loop reports insulin delivered by basal for the last 6 hours when the scheduled basal rate has a new entry |
|--- | 07:15 AM<br>0.0 U/hr | 07:15 AM<br>Basal<br>0.6 U | Loop reports insulin delivered by basal since last report up to time TB starts |
|--- | 07:45 AM<br>TB expires | 07:45 AM<br>Basal<br>0 U | No insulin was delivered during TB |
|08:00 AM<br>0.4 U/hr | --- | 08:00 AM<br>Basal<br>0.1 U | Loop reports insulin delivered by basal since last report; the scheduled basal rate has a new entry|


### Tidepool and Apple HealthKit

If you have a [Tidepool](https://tidepool.org) account and use the Tidepool uploader on your Loop phone, the data in Health is uploaded to your Tidepool database where you can view displays with the [Tidepool web browser tool](https://loopkit.github.io/looptips/data/tidepool/).
