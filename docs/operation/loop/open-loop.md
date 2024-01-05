## Open Loop Introduction

Open Loop is the best place to start with Loop.

* Become familiar with Loop by watching it operate with <code>Closed Loop</code> disabled.
* Take it slow and safe to become a successful Looper.

??? warning "Menus do not include all Manual Pump Features. (Click to learn more)"
    The *Loop* app is built around the concept of <code>Closed Loop</code> performance.

    If you use a Medtronic pump and want to use a feature not found in the *Loop* app, simply disable <code>Closed Loop</code> and control delivery with your Medtronic Controller.

    If you use an Omnipod pump, keep reading:

    There may be some features, like extended bolus, that you used with an *Omnipod* Personal Device Manager (PDM) that are not an option as a menu item in the *Loop* app. When users transition from using a PDM, they may want this as an interim feature.

    Please refer to [Extended Bolus](#extended-bolus).

!!! tip "Practice with Simulators"
    You can build Loop without connecting it to any hardware.

    * You can use your phone, a partner's phone or a simulated phone on the computer
    * You can practice with a simulated CGM and / or  a simulated pump.
    * You can use Dexcom Share or Nightscout as a CGM to follow your own glucose.
    * You can "dose" the simulated pump and your real pump at the same time and watch the glucose predictions.

### Glucose Prediction

Pay attention to the prediction in the **[Glucose Chart](../../loop-3/displays-v3.md#glucose-chart)**. Practice with the user interface while you manually control your insulin delivery. Compare the recommended insulin after entering carbs for a familiar meal. If you do not understand the predictions or recommendations, do not enable Closed Loop. You may need to adjust settings or learn more about how the app works. Loop tries to keep predicted glucose in the Correction Range and, more importantly, above your Glucose Safety Limit.

There's a lot to learn and understand. New loopers may need to adjust the following Therapy Settings, typically in this order:

1. Basal Rates
1. Insulin Sensitivity Factor (ISF)
1. Carb Ratios (CR)

Using an algorithm that updates glucose predictions and adjusts insulin delivery every 5 minutes requires accurate settings. Entering carbs and absorption time is a new skill that takes time to master.

### Eventual Glucose

Watch the eventual glucose, current glucose and prediction curve in the **[Glucose Chart](../../loop-3/displays-v3.md#glucose-chart)** to understand Loop recommendations for insulin delivery adjustment.  Loop is looking at current glucose, glucose momentum, carbs on board, insulin on board, and retrospective trends to predict an eventual glucose.  Its current decisions are based on predicted, actual and eventual glucose.

If there is a dip in the predicted glucose below the Glucose Safety Limit, Loop will not recommend insulin even if the eventual glucose is above your Correction Range.

* In Closed Loop mode, Loop automatically decreases insulin delivery using a temp basal of 0 U/hr until the predicted glucose exceeds the Glucose Safety Limit
* When you tap on the Bolus icon in the Toolbar, Loop recommends insulin delivery only after predicted glucose is above Glucose Safety Limit
* In Closed Loop mode, Loop automatically increases insulin delivery only after predicted glucose is above the bottom of the Correction Range

If the Loop predictions don't match your experience, your settings may need to be adjusted.

### Testing

Open Loop mode shows you glucose trends without the influence of temp-basal or automatic-bolus from Loop. This is particularly helpful if you haven't used Medtronic sites/pumps or Omnipod prior to Loop. You may find that your basal rates and carb ratios can change significantly coming from other brands of pumps or from multiple daily injections (MDI).

Take the time to establish a good basal profile using the pump you plan to use for Loop while in Open Loop mode.

Test your insulin sensitivity factor (ISF) during Open Loop after your basal rates are established.  Loop uses your ISF every 5 minutes to update predictions, so it's worth testing before turning on automated insulin dosing with Closed Loop mode.

## Meal Entry

**Loop recommends increased insulin dosing as soon as you save carbs.**

[Meal Entry](../features/carbs.md) is an important concept - there's a whole page devoted to it - but here's a quick summary. You tap on the plate icon in the Toolbar to start a meal entry.

* Meal Entry:
    * In the Add Carb Entry screen, you must enter Amount Consumed, defaults are ok for other rows
    * The meal entry is not saved when you tap continue - Loop takes you to the Meal Bolus screen
    * In the [Meal Bolus](../features/bolus.md#meal-bolus) screen, you can save the carbs and accept or override the recommended bolus
    * Review the recommended bolus for the carb entry
        * Does the recommendation make sense based on your prior experience
        * Pay attention to the glucose prediction chart embedded in the Meal Bolus tool
        * Practice modifying when the carbs are expected and how long they are expected to last
        * Practice modifying the bolus recommendation - note how the prediction changes
        * When you are confident, you can save the carbs and deliver the bolus

### Carb Absorption

Loop uses carb absorption as a component to every meal entry. Watch your meals and try to estimate how long they impact your glucose for various types of food. Notice when Loop would suspend basal or increase insulin delivery and ask yourself why it would be doing that. Ask if this is the same decision you would make.  This effort  will help smooth the transition to closed loop.


## Manual (or Correction) Bolus

At any time, you can enter a bolus using the Bolus (double orange triangles) icon in the Toolbar. Loop offers a recommendation if the glucose prediction supports one. Review the [Eventual Glucose](#eventual-glucose) section above to understand when Loop will recommend a bolus. The Loop recommendation can be modified by editing the Bolus amount.

More detail is provided at this [link](../features/bolus.md#manual-or-correction-bolus).

## Troubleshooting

If you use a RileyLink, determine how far the link can be from your phone and pump, and plan where to carry the link. DASH Omnipod users do not need the RileyLink but should determine how far their phone can be from the pod without communication problems.

Learn to troubleshoot [Red Loops](../../troubleshooting/red-loop.md) and the cause of potential loop issues. You'll be less frustrated starting on closed loop if you know how to address these issues

Familiarize yourself with the ["Bolus May Have Failed"](../features/bolus.md#bolus-failure-notifications) notifications and how to handle them.  Double-check the displays to verify that the bolus didn't enact before trying to give the bolus again.

## Caregiver training

Caregivers for Loopers should learn how to use Loop. Consider giving caregivers an individualized quick info sheet on Loop. School staff or your child need to know how to handle a site change at school. Try to watch Nightscout while you get to know Loop so that you can become better at remote troubleshooting problems you might encounter.

## Extended Bolus

A menu item to set an extended bolus is not a feature provided by the *Loop* app at this time. You can make your own extended bolus using the <code>Manual Temp Basal</code> feature with Omnipod. Note that during the time the <code>Manual Temp Basal</code> command is running, the *Loop* app will make no automated changes to dosing even if the <code>Closed Loop</code> slider is selected as enabled.

### Extended Bolus Equations

Consider a desired total bolus $(BolusTotal)$ given over an extended time with a prompt amount $(PromptAmount)$ now and the balance $(Balance)$ delivered over the next $(H)$ hours with a current scheduled basal rate $(BR)$.

First the equations to calcuate the desired rate $(MTB)$ to enter into the <code>Manual Temp Basal</code> menu and then an example.

$$ Balance = BolusTotal - PromptAmount $$

$$ MTB = Balance / H + BR $$


1. Turn on a [<code>Manual Temp Basal</code>](../../loop-3/omnipod.md#manual-temp-basal) to value of $MTB$ units/hour for $H$ hours
2. Tap the bolus icon on the main toolbar and enter a bolus for $PromptAmount$ units

The order is important. Sending the <code>Manual Temp Basal</code> request to the pod is a single command and then the *Loop* app is available for the next command to be entered. The *Loop* app (and pod) will not respond to any pod commands until the bolus finishes delivering; this takes about 40 seconds per unit requested.

### Specific Example

For this example:

* $BolusTotal$ is 3 U
* $PromptAmount$ is 1 U
* Time in hours, $H$, is 1.5
* Scheduled basal rate, $BR$, is 0.5 U/hr

$$ Balance = 3 U - 1 U = 2 U $$

$$ MTB = (2 / 1.5) U/hr + 0.5 U/hr = 1.55 U/hr $$

You have your choice of rounding $MTB$ up or down to the nearest $0.05 U/hr$. For this example, the quantity of $(2/1.5)=1.333$ was rounded up to $1.35 U/hr$.

??? question "Why isn't there a menu item? (Click to see more)"
    Each item provided by the *Loop* app needs a volunteer to decide it is important and develop a method to provide that item. If a volunteer steps up to do this work, there is a long process of discussion and code review before such a modification is considered for the development branch.

    Most Loopers go to <code>Closed Loop</code> quickly and this feature is not an option at this time.
