# Open Loop

## Open Loop Introduction

Open Loop is the best place to start with Loop.

* Become familiar with Loop by watching it operate with Closed Loop disabled.
* Take it slow and safe to become a successful Looper.

!!! tip "Practice with Simulators"
    You can build Loop without connecting it to any hardware.

    * You can use your phone, a partner's phone or a simulated phone on the computer
    * You can practice with a simulated CGM and / or  a simulated pump.
    * You can use Dexcom Share or Nightscout as a CGM to follow your own glucose.
    * You can "dose" the simulated pump and your real pump at the same time and watch the glucose predictions.

#### Loop 2.2.x Open Loop

!!! warning "Loop 2.2.x SAFETY WARNING"
    When you are operating in Open Loop mode, Loop 2.2.x offers recommendations for insulin delivery adjustment and displays them on the [HUD](../loop-settings/displays.md#heads-up-display).

    * If you tap on the recommendation line, Loop applies that recommendation without asking for confirmation
    * To protect against accidental command of increased or decreased insulin dosing, make sure your phone is locked when not in use

### Glucose Prediction

Pay attention to the [glucose prediction chart](../loop-settings/displays.md#glucose-chart). Practice with the user interface while you manually control your insulin delivery. Compare the recommended insulin after entering carbs for a familiar meal. If you do not understand the predictions or recommendations, do not enable Closed Loop. You may need to adjust settings or learn more about how the app works. Loop tries to keep predicted glucose in the Correction Range and, more importantly, above your Glucose Safety Limit (suspend threshold in Loop 2.2.x).

There's a lot to learn and understand. New loopers may need to adjust the following Therapy Settings, typically in this order:

1. Basal Rates
1. Insulin Sensitivity Factor (ISF)
1. Carb Ratios (CR)

Using an algorithm that updates glucose predictions and adjusts insulin delivery every 5 minutes requires accurate settings. Entering carbs and absorption time is a new skill that takes time to master.

### Eventual Glucose

Watch the eventual glucose, current glucose and prediction curve to understand Loop recommendations for insulin delivery adjustment.  Loop is looking at current glucose, glucose momentum, carbs on board, insulin on board, and retrospective trends to predict an eventual glucose.  Its current decisions are based on that eventual glucose.

If there is a dip in the predicted glucose below your Glucose Safety Limit, Loop will not recommend increased insulin delivery even when the eventual glucose is above your correction range.

* In this case, Loop recommends a temp basal of 0 U/hr
    * With Loop 2.2.x, you can issue that 0 U/hr temp basal by tapping on the HUD
    * With Loop dev, you can issue a Manual Temp basal of 0 U/hr for 30 minutes
* Loop will recommend an increase in insulin delivery only after predicted glucose is above Glucose Safety Limit

If the Loop predictions don't match your experience, your settings may need to be adjusted.

### Testing

Open Loop mode shows you glucose trends without the influence of temp-basal or automatic-bolus from Loop. This is particularly helpful if you haven't used Medtronic sites/pumps or Omnipod prior to Loop. You may find that your basal rates and carb ratios can change significantly coming from other brands of pumps or from multiple daily injections (MDI).

Take the time to establish a good basal profile using the pump you plan to use for Loop while in Open Loop mode.

Test your insulin sensitivity factor (ISF) during Open Loop after your basal rates are established.  Loop uses your ISF every 5 minutes to update predictions, so it's worth testing before turning on automated insulin dosing with Closed Loop mode.

## Meal Entry

**Loop recommends increased insulin dosing as soon as you save carbs.**

[Meal Entry](../features/carbs.md) is an important concept - there's a whole page devoted to it - but here's a quick summary. You tap on the plate icon in the Toolbar to start a meal entry.

* Meal Entry:
    * In the Add Carb Entry screen, you enter carbs along with an expected "eating" time and absorption duration
    * The meal entry is not saved when you tap continue - Loop takes you to the meal bolus screen
    * In the Meal Bolus screen, you can save the carbs and accept or override the recommended bolus
        * [Link for Loop 2.2.x Meal Entry](../features/carbs.md)
        * If running Loop-dev, understand the link for Loop 2.2.x Meal Entry (above) and then review the [Loop dev Meal Bolus Features](../../loop-3/features.md#meal-bolus)
    * Review the recommended bolus for the carb entry
        * Does the recommendation make sense based on your prior experience
        * Pay attention to the glucose prediction chart embedded in the Meal Bolus tool
        * Practice modifying when the carbs are expected and how long they are expected to last
        * Practice modifying the bolus recommendation - note how the prediction changes
        * When you are confident, you can save the carbs and deliver the bolus



### Carb Absorption

Loop uses carb absorption as a component to every meal entry. Watch your meals and try to estimate how long they impact your glucose for various types of food. Notice when Loop would suspend basal or increase insulin delivery and ask yourself why it would be doing that. Ask if this is the same decision you would make.  This effort  will help smooth the transition to closed loop.


## Correction or Manual Bolus

At any time, you can enter a bolus using the Bolus icon in the Toolbar. Loop offers a recommendation if the glucose prediction supports one. The [Bolus](../features/bolus.md) tool  has a whole page devoted to it - but here's the quick summary.

* Bolus:
    * The bolus suggested by Loop is based on the glucose prediction line, your Glucose Safety Limit, your Correction Range and your Therapy Settings
    * [Link for Loop 2.2.x Manual Bolus](../features/bolus.md)
    * [Link for Loop 3 Manual Bolus](../../loop-3/features.md#manual-bolus)


## Troubleshooting

If you use a RileyLink, determine how far the link can be from your phone and pump, and plan where to carry the link. DASH Omnipod users do not need the RileyLink but should determine how far their phone can be from the pod without communication problems.

Learn to troubleshoot [red loops](../../troubleshooting/yellow-red-loop.md) and the cause of potential loop issues. You'll be less frustrated starting on closed loop if you know how to address these issues

Familiarize yourself with the ["Bolus May Have Failed"](../features/bolus.md#bolus-failure-notifications) notifications and how to handle them.  Double-check the displays to verify that the bolus didn't enact before trying to give the bolus again.

## Caregiver training

Caregivers for Loopers should learn how to use Loop. Consider giving caregivers an individualized quick info sheet on Loop. School staff or your child need to know how to handle a site change at school. Try to watch Nightscout while you get to know Loop so that you can become better at remote troubleshooting of any problems that you might encounter.
