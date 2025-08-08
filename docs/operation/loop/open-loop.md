## <code>Open Loop</code> Introduction

<code>Open Loop</code> is the best place to start with Loop.

* Become familiar with the *Loop* app by watching it operate with <code>Closed Loop</code> disabled.
* Take it slow and safe to become a successful Looper.

??? warning "Menus do not include all Manual Pump Features (Click to learn more)"
    The *Loop* app is built around the concept of <code>Closed Loop</code> performance.

    If you use a Medtronic pump and want to use a feature not found in the *Loop* app, simply disable <code>Closed Loop</code> and control delivery with your Medtronic Controller.

    If you use an Omnipod pump, keep reading:

    There may be a feature, like extended bolus, that you used with an *Omnipod* Personal Device Manager (PDM) that is not in the *Loop* app.

    Please refer to [Extended Bolus](#extended-bolus).

??? tip "Practice with Simulators (Click to learn more)"
    You can build the *Loop* app without connecting it to any hardware.

    * You can use your phone, a partner's phone or a simulated phone on the computer
    * You can practice with a simulated CGM and / or a simulated pump.
    * You can use Dexcom Share or Nightscout as a CGM to follow your own glucose.
    * You can "dose" the simulated pump and your real pump at the same time and watch the glucose predictions.

### Glucose Prediction

Pay attention to the prediction in the [Glucose Chart](../../loop-3/displays-v3.md#glucose-chart){: target="_blank" }. Practice with the user interface while you manually control your insulin delivery. Compare the recommended insulin after entering carbs for a familiar meal. Be sure you understand the predictions and recommendations before you enable <code>Closed Loop</code>. You may need to adjust settings or learn more about how the app works. The *Loop* app tries to keep predicted glucose in the Correction Range and, more importantly, above your Glucose Safety Limit.

There's a lot to learn and understand. New loopers may need to adjust the following Therapy Settings, typically in this order:

1. Basal Rates
1. Insulin Sensitivity Factor (ISF)
1. Carb Ratios (CR)

Using an algorithm that updates glucose predictions and adjusts insulin delivery every 5 minutes requires accurate settings. Entering carbs and absorption time is a new skill that takes time to master.

### Eventual Glucose

Watch the eventual glucose, current glucose and prediction curve in the **[Glucose Chart](../../loop-3/displays-v3.md#glucose-chart)** to understand recommendations for insulin delivery adjustment. The *Loop* app is looking at current glucose, glucose momentum, carbs on board, insulin on board, and retrospective trends to predict an eventual glucose. Its current decisions are based on actual, predicted and eventual glucose. Predictions for the first three hours of insulin duration of activity are given more emphasis than later predictions when deciding how much insulin should be recommended or withheld from basal.

If there is a dip in the predicted glucose below the Glucose Safety Limit, the *Loop* app will not recommend insulin even if the eventual glucose is above your Correction Range.

* In <code>Closed Loop</code> mode, the *Loop* app automatically decreases insulin delivery using a temp basal of 0 U/hr until the predicted glucose exceeds the Glucose Safety Limit
* When you tap on the Bolus icon in the Toolbar, the *Loop* app recommends insulin delivery only after predicted glucose is above Glucose Safety Limit
* In <code>Closed Loop</code> mode, the *Loop* app automatically increases insulin delivery only after predicted glucose is above the bottom of the Correction Range

If the *Loop* predictions don't match your experience, your settings may need to be adjusted.

If you want to issue a manual temp basal, this is done on the pump for Medtronic or using the [Manual Temp Basal](../../loop-3/omnipod.md#manual-temp-basal){: target="_blank" } feature for Omnipod.

### Testing

<code>Open Loop</code> mode shows you glucose trends without the influence of temporary basal or automatic bolus. This is particularly helpful if you haven't used Medtronic sites/pumps or Omnipod before. You may find that your basal rates and carb ratios can change significantly coming from other brands of pumps or from multiple daily injections (MDI).

**The suggestions below work for most people. You need to adjust for your own situation.**

Take the time to establish a good basal profile while in <code>Open Loop</code> mode using the pump you plan to use for the *Loop* app. When using an algorithm, your basal rates needs to be neutral; in other words your glucose, in the absence of food and exercise, should be stable. (When you do basal testing, you should aim to stay at a glucose that is steady within 35 mg/dL (2 mmol/L).)

If you previously ran a high basal rate during the day to cover meals, you may need to adjust your CR (to a smaller value) after your basal rate is adjusted to be neutral.

Test your insulin sensitivity factor (ISF) during <code>Open Loop</code> after your basal rates are established. The *Loop* app uses your ISF every 5 minutes to update predictions, so it's worth testing before turning on automated insulin dosing with <code>Closed Loop</code> mode. You may need a different, probably higher value, than what you used as a correction factor with manual pumping or MDI.

The algorithm uses the ratio of ISF/CR as part of the prediction while meals are being absorbed. That ratio is approximately how much a single gram of carbohydrate raises your glucose. Experiment by taking a small fast-acting "low treatment" when stable with no other food or exercise. 

> Assume ISF is 75 mg/dL and CR is 15 g/U. When a 4 g glucose tablet is consumed, you expect to see a sharp rise in glucose by about 20 mg/dL over the next half hour to an hour. (Your ISF/CR ratio times the grams eaten should be within a factor of two of how much rise you see in glucose.)

## Meal Entry

**Loop recommends increased insulin dosing as soon as you save carbs.**

Meal Entry is an important concept - there's a whole page devoted to it later in the docs - but here's a quick summary. You tap on the plate icon in the Toolbar before you meal to show the Add Carb Entry screen.

![Loop toolbar](../features/img/toolbar-meal.svg){width="300"}
{align="center"}

* In the Add Carb Entry screen, you must enter Amount Consumed, defaults are ok for other rows
* The meal entry is not saved when you tap continue - the *Loop* app takes you to the Meal Bolus screen
* In the [Meal Bolus](../features/bolus.md#meal-bolus){: target="_blank" } screen, you can save the carbs and accept or override the recommended bolus
* Review the recommended bolus for the meal entry
    * Does the recommendation make sense based on your prior experience
    * Pay attention to the glucose prediction chart embedded in the Meal Bolus tool
    * Practice modifying when the carbs are expected and how long they are expected to last
    * Practice modifying the bolus recommendation - note how the prediction changes
    * When you are confident, you can save the carbs and deliver the bolus

### Carb Absorption

Loop uses carb absorption as a component to every meal entry. Most people are successful with the default absorption time of 3 hours. Remember the *Loop* app updates the prediction every 5 minutes and will adjust if you get the amount or absorption time wrong, as long as you are close.

* For low-glucose treatment, you can enter using the 30-minute (lollipop) icon
* For high-fat meals, you can try the 5-hour (pizza) icon

The [Active Carbohydrate](../../loop-3/displays-v3.md#active-carbohydrates-chart){: target="_blank" } chart displays how the app thinks your meal is being aborbed. This is affected by your basal rates, ISF and CR. If it looks wrong, examine your settings.

Depending on the type of food you eat, you may increase the carb entry to include some protein or fat.

## Manual (or Correction) Bolus

At any time, you can enter a bolus using the Bolus (double orange triangles) icon in the Toolbar. The *Loop* app offers a recommendation if the glucose prediction supports one. Review the [Eventual Glucose](#eventual-glucose) section above to understand when the app will recommend a bolus. The *Loop* recommendation can be modified by editing the Bolus amount.

If you tap on the Bolus button (on the Toolbar), does the app recommend more insulin? 

![Loop toolbar](../features/img/toolbar-bolus.svg){width="300"}
{align="center"}

* If so, you can choose to accept if it looks reasonable to you
* If not, look at the prediction plot to understand the decision

Ask if this is the same decision you would make. This effort will help smooth the transition to <code>Closed Loop</code>.

## Troubleshooting

If you use a RileyLink, determine how far the link can be from your phone and pump, and plan where to carry the link. DASH Omnipod users do not need the RileyLink but should determine how far their phone can be from the pod without communication problems.

Learn to troubleshoot [Red Loops](../../troubleshooting/red-loop.md){: target="_blank" } and the cause of potential loop issues. You'll be less frustrated starting on closed loop if you know how to address these issues.

Familiarize yourself with the [Bolus Failure Notifications](../features/bolus.md#bolus-failure-notifications){: target="_blank" }.

## Caregiver training

Caregivers for Loopers should learn how to use the *Loop* app. School staff or your child need to know how to handle a site change or CGM failure at school. Consider preparing an individualized quick info sheet for your child.

Learn to observe the *Nightscout* site while your child is with you and you can look at their phone. This will help you help your child if they have problems when they are not with you.

For more reading, there's a whole set of pages on using [*Nightscout* with the *Loop* app](../../nightscout//remote-overview.md){: target="_blank" } and setting up a secure method for you to provide bolus or carb entries via remote commands.

## *Apple* Health in <code>Open Loop</code>

If you are using the *Apple* Health app to examine insulin given while in <code>Open Loop</code>, basal delivery is not recorded in the Health app promptly. You can force an update from the *Loop* app to Health by suspending and then resuming the pump. If you do this, keep watching the app to make sure delivery did resume.

## Extended Bolus

A menu item to set an extended bolus is not a feature provided by the *Loop* app at this time. You can make your own extended bolus using the <code>Manual Temp Basal</code> feature with Omnipod.

**During the time the <code>Manual Temp Basal</code> command is running, the *Loop* app will make no automated changes to dosing even if the <code>Closed Loop</code> slider is selected as enabled.**

### Extended Bolus Equations

> This section was added at user request. Once you switch to <code>Closed Loop</code> mode, you should not need this. But before you are ready for that step, you may want to use a tested method for a known meal.

Consider a desired total bolus $(BolusTotal)$ given over an extended time with a prompt amount $(PromptAmount)$ now and the balance $(Balance)$ delivered over the next $(H)$ hours with a current scheduled basal rate $(BR)$.

First the equations to calculate the desired rate $(MTB)$ to enter into the <code>Manual Temp Basal</code> menu and then an example.

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

$$ MTB = (2 / 1.5) U/hr + 0.5 U/hr = 1.85 U/hr $$

You have your choice of rounding $MTB$ up or down to the nearest $0.05 U/hr$. For this example, the quantity of $(2/1.5)=1.333$ was rounded up to $1.35 U/hr$ and then the scheduled basal rate was added.

??? question "Why isn't there a menu item? (Click to see more)"
    Each item provided by the *Loop* app needs a volunteer to decide it is important and develop a method to provide that item. If a volunteer steps up to do this work, there is a long process of discussion and code review before such a modification is considered for the development branch.

    Most Loopers go to <code>Closed Loop</code> quickly and this feature is not an option at this time.
