# Open-Loop

Open-loop is a great place to start with Loop.

It is understandable to want to jump straight away into closed-loop mode, but a lot can be learned by watching Loop operate in open mode. The `Closed Loop` switch is disabled by default.  Becoming familiar with the algorithm can be easier by watching it in action rather than only reading about it in docs. Practice with the user interface.

Speaking of practice, there are simulators available in the app. You can build Loop and practice using it with a simulated CGM and a simulated pump. For even more fidelity, use Dexcom Share or (Loop-dev only) Nightscout as a CGM to follow your own blood sugar and make dosing decisions. You can `dose` the simulated pump and your real pump at the same time and watch the glucose predictions.


#### Loop 2.2.x Open Loop

!!! warning "WARNING"
    In earlier versions of Loop, a debug feature was left active.  This was never intended as a "teaching" tool, however, it was used that way. This capability is not in Loop-dev for safety reasons. It is too easy to tap on an unlocked phone and provide extra insulin inadvertently.
    
    When you are operating in open-loop mode, Loop 2.2.x offers recommendations for insulin delivery adjustment and displays them on the main screen. The recommendations are enacted if you tap on the recommendation line on the [HUD](../loop-settings/displays.md#heads-up-display). To protect against enacting accidentally, make sure your phone is locked when not in use.

### Open Loop

While running in open loop mode, you should pay attention to the glucose prediction line. If the predictions don't make sense, do not enable `Closed Loop`. You may need to adjust settings or  learn more about how the app works. Loop tries to keep you in your correction range but also wants to keep you above your glucose safety level (`suspend threshold` in Loop 2.2.x). 

There's a lot to learn and understand. Take the time you need so you can safely use Loop. If the meal bolus and manual correction suggestions that Loop makes are not consistent with your manual pumping experience, take the time to adjust your settings.  Typically, new loopers need to adjust (1) Basal Rates and then (2) Insulin Sensitivity Factor and finally (3) Carb Ratios. Using an algorithm that updates glucose predictions and adjusts insulin delivery every 5 minutes requires more fidelity for those settings than manual pumping. The meal entry in terms of carbs and absorption time is also a new skill that takes time to understand.

* Meal Entry:
    * In Loop, you enter carbs and then are taken to a meal bolus screen at which you can save the carbs or save the carbs and bolus
    * [Link for Loop 2.2.x Meal Entry](../features/carbs.md)
    * If running Loop-dev, understand the link for Loop 2.2.x Meal Entry (above) and then review the [Meal Bolus](../../loop-3/features.md#meal-bolus) features that are updated
    * You should investigate entering a Meal to understand the interface and examine the recommended bolus for that meal
        * Does the recommendation make sense to you based on your prior experience
        * Practice modifying when the carbs are expected and how long they are expected to last
        * Practice modifying the bolus recommendation
        * When you are confident, then you can deliver the bolus manually

* Manual Correction:
    * The manual correction suggested by Loop is based on the glucose prediction line, your glucose safety limit, your correction range and your Settings
    * [Link for Loop 2.2.x Manual Bolus](../features/bolus.md)
    * [Link for Loop 3 Manual Bolus](../../loop-3/features.md#manual-bolus)

## Testing

A great benefit of open-loop mode is that you can establish a baseline of BG trends without the influence of temp-basal or automatic-bolus from Loop. This is particularly helpful if you haven't used Medtronic sites/pumps or Omnipod prior to Loop. You may find that your basal rates change significantly coming from other brands of pumps or from multiple daily injections (MDI).  

Taking the time to establish a good basal profile using the pump you plan to use for Loop will set you up for a smoother transition to closed-loop mode.

Test your insulin sensitivity factor (ISF) during open-loop time after your basal rates are established, as ISF is an important component for every Loop calculation for insulin delivery adjustment.  Every 5 minutes, Loop uses your ISF...so it's worth testing it ahead of closed-loop mode.

## Eventual BG

One of the best things you can do is to train yourself to watch the eventual BG in addition to the current BG for helping understand Loop recommendations for insulin delivery adjustment.  So many of us have become accustomed to dealing with current BGs and perhaps IOB at the same time...but Loop is also looking at BG momentum, carbs on board, retrospective trends.  Loop is utilizing all of those variables to predict an eventual BG.  Its current decisions are based on that eventual BG.  Training yourself to watch that eventual BG will help you understand the temp basals being offered at any given time.

On the other hand, Loop will not recommend increased insulin delivery now if a temporary dip in BG is predicted; it may even be recommending a decrease, i.e., temp basal of 0 U/hr.  So the eventual BG may be higher than you want, but if you see a dip below your correction range, pay attention over time.  Once a dip is no longer predicted, then Loop will again recommend an increase in insulin delivery. If the Loop predictions don't match your experience - probably a sign that your settings may need to be adjusted.

## Carb Absorption

Probably the next most difficult transition involves using carb absorption as a component to every [meal entry](../features/carbs.md).  Similar to how you perhaps used extended boluses for meals that impacted BGs longer than the duration of your insulin...that same idea applies to estimate your carb absorption times. Watch your meals and try to estimate how long they are impacting your BG for various types of food.  Watch the times when Loop would've wanted to suspend basal or increase insulin delivery...ask yourself why it would be doing that.  Especially ask yourself if that is the same decision as you would've made at that time in a meal normally.  Would you be worried that you might go low later if you see Loop offering increased insulin delivery early after a meal?  Would you be worried about going high later if Loop wants to suspend basals instead?  If you put some effort into this effort before closing the loop, it will pay off with a smoother transition to closed loop.

## Troubleshooting

Get used to carrying the RileyLink around. DASH Omnipod users do not need the RileyLink, but should determine how far the phone can be from the pod. Find how far your connectivity stretches before you have pump communication problems.  Get used to [troubleshooting yellow and red loops](../../troubleshooting/yellow-red-loop.md), finding out the pattern/cause of any potential loop issues.  You'll be less frustrated starting on closed loop if you aren't dealing with learning new electronics at the same time as you are learning carb absorption times in a closed loop.

## Bolus

All new Loop users need to learn to [bolus for meals](../features/carbs.md) by first entering carbs.  For Medtronic users, do not enter carbs on the pump. For Omnipod users, learn how to use the Loop interface instead of the PDM.  Become familiar with entering carbs into the Loop app, as well as editing them.  Watch how long it takes for Loop app to display the bolus after you enact it.  Familiarize yourself with the ["Bolus May Have Failed"](../features/bolus.md#bolus-failure-notifications) notifications and how to handle them.  Double-check the pump and verify that the bolus didn't enact before trying to give the bolus again.

Learn about correction or [manual bolus](../features/bolus.md) from Loop. If you manually enter a correction you think is right, but Loop (using the settings you entered) disagrees, it will probably recommend a 0 temp basal right away. It is OK to override Loop sometimes (e.g., a super bolus that trades bolus now for zero basal later) but you need to understand what you are doing and why.  It's best to adjust settings rather than "fight" with Loop.

## Caregiver training

If you are the caregiver of someone with Type 1 Diabetes using Loop, make sure you take the time to educate caregivers around your family and school (or other facility) for how to use Loop.  Perhaps you want to draft individualized quick info sheets for those caregivers to use with Loop.  If your child needs a site change at school, school staff or your child need to know how to handle that.  Try to watch Nightscout while you get to know Loop so that you can become better at remote troubleshooting of any problems that you might encounter.
