# Bolus

<p align="center">
<img src="../img/toolbar.jpg" width="400">
</p> 

Bolus entries can be made manually through the bolus tool (double orange triangles) in the toolbar, either as part of a meal bolus or as a correction for a high BG.

## Meal Bolus
Loop has a Bolus Wizard, similar to a pump’s bolus wizard.  After a carb entry is made, Loop will provide a bolus screen with a recommended bolus amount.  If you want to deliver the total amount of the recommended bolus, simply tap on the recommended amount of units and the bolus delivery line will automatically be filled-in with the same units.  If you want to give fewer units than the recommended amount, you can manually enter the desired amount to be delivered.   

The Bolus Wizard will not offer a recommended bolus if your BG is below, or predicted to go below, your specified Minimum BG Guard.  A screen will appear letting you know the reason no bolus is being recommended as well as the status of your active COB and IOB.  You can choose to override that warning and give a bolus, or treat the low BG and come back to the bolus tool when your BG has recovered.

<p align="center">
<img src="../img/below_min.png" width="400">
</p> 

## Correction Bolus
Occasionally, a recommended bolus will be offered in the bolus screen unrelated to a recent carb entry.  In those cases, Loop is calculating that it will not be able to stay in target range through the use of max temp basals alone and is offering a “correction bolus”.  Correction boluses will not be delivered automatically by Loop, they must be delivered by the user.  Loop will also not give an alert when a correction bolus is being offered, the bolus entry tool must be clicked to check for one.  In a well-run loop with decent carb counting, correction boluses should be infrequently needed.

Part of Loop's predictions for future BG changes include a component called BG momentum. Loop looks at the previous three BG readings and calculates a best-fit-straight-line for those three points. In other words, it tries to draw a future trend line using the last three BG data points. Loop extends that line 30 minutes into the future and gives a fair amount of weight to that component of the BG prediction. In instances of rapidly changing BGs, BG momentum may overestimate the rise/fall of BG. Therefore, please be cautious giving corrective boluses using Loop recommendations during times of rapid change.

## Bolus Failure Notifications
On occasion, you will receive notification that a bolus may have failed. In some of these cases, the bolus actually will begin delivery. Therefore, you should always check the pump screen to verify the bolus status before attempting to redeliver a failed bolus.

## Eating Soon
You can modify your Workout Target range to help prebolus for meals.  If you set your Workout Target to 80 mg/dl - 80 mg/dl for an hour before a meal, this will help Loop to deliver additional insulin prior to the meal, and help control post-prandial BGs.  The Loop will account for the amount of insulin it has prebolused when it offers the recommended bolus for the meal.


## Bolus Strategies
Unfortunately, Loop cannot enact temp basals while the pump is delivering a square wave or dual wave bolus.  Therefore, we recommend that you find alternate bolusing strategies for situation where you would've previously used those extended bolusing techniques.

While you adapt to new bolusing techniques, it is important to monitor closely to see what works for you.  It will take some trial and error to get it right.  In particular, pay close attention to what you enter for the carb absorption time for the food.  If you are used to using a square wave or extended bolus, then it is for food that takes a longer than normal period of time to digest so adjust accordingly. 

Many Loop users use a combination of (1) splitting individual boluses and/or (2) setting carbs in the future before a slower, larger carb meal to help control BG levels that would otherwise rise without an extended bolus.

Using the [Glucodyn](https://perceptus.org) model can help you simulate new bolusing strategies.  Glucodyn allows you to simulate your post-prandial BGs based on your particular ISF, carb ratio, and carbs.  You can simulate split boluses and watch their impact on simulated BG responses.  The underlying math of the Glucodyn model is the basis of Loop's insulin/carb calculations.

