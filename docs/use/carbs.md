# Carb Entry

<p align="center">
<img src="../img/toolbar.jpg" width="400">
</p>  

## New Carbs

<p align="center">
<img src="../img/carb_entry.png" width="250">
</p>

New carb entries can be made by using the carb tool (green fork) in the toolbar at the bottom of the status screen.  Simply enter the number of carbs to be eaten in the `amount consumed` line.  By default, the carb absorption time for a new carb entry will correspond to the taco icon.  If you haven't made any customizations to this during your Loop build, then the default carb absorption time will display as 3 hours.  The default time entry is for the current time and date.  

You do not have to enter all carbs for a meal at the same absoption or eating time.  If you want to enter some of the meal's carbs as faster, and some slower, you can log the meal over several individual carb entries.

Pressing the `Save` button in the top right corner will save the carbs into the Loop app and bring up the bolus wizard (if you are above your Minimum BG guard).

## Carb Absorption Time

<p align="center">
<img src="../img/food_icons_times.png" width="400">
</p>

These default carb absorption times are average representations for high, medium, and low glycemic index foods.  Loop app has been updated in v1.4.0 to incorporate dynamic carb absorption.  Previous Loop versions were based on a curve that assumed the rate of carb absorption would start out slow, increase to a mid-point, and then taper off.  However, in the real world, carb absorption is quite variable.  Dynamic carb absorption model is able to model some of this variability and allow Loop to respond more reasonably when actual carb absorption is not matching well with the selected carb absorption time for a meal.  In short, while entering a carb absorption time is still part of recording meals in Loop, it is much less critical to get it right.  Now your entry serves more as a guideline, than a rule, for Loop to model carb absorption. 

For a more detailed explanation of the new dynamic carb absorption model, please read about it [here](https://github.com/LoopKit/Loop/pull/507).

To select your carb entry's absorption time, you can either click on the default food emojis or manually enter carb absoprtion time by selecting the `absorption time` line in the carb entry tool.  

A new feature of Loop v1.4.0 is the plate emoji, found to the right of the pizza emoji.  If you select the plate icon, you can use new food emojis and add text to your `food type`.  Updating and deploying your Nightscout cgm-remote-monitor repository to the latest dev branch will allow those entries to be displayed on your graph.

<p align="center">
<img src="../img/plate.png" width="300">
</p>

<p align="center">
<img src="../img/ns-plate.png" width="900">
</p>

## Prebolus 
You can let Loop know you are going to prebolus a meal by adjusting the time of the carb entry on the “date” line of the carb entry.  If you are prebolusing by 20 minutes, simply add 20 minutes to the carb entry time.  

## Edit Carbs 

<p align="center">
<img src="../img/carb_edit.png" width="300">
</p>

Clicking on the Carbohydrate chart in the Loop's main status screen will open the carb entry history and previous entries can be modified or deleted through this screen.  If you need to change a prebolus time, add carbs, adjust carb absorption times (even mid-meal), just go into that edit screen and tap on the carb entry you'd like to edit.  Pretty straight-forward.

## Third Party Apps
If you use a 3rd party app, such as My Fitness Pal, to enter and track carbs and that app also stores the carb values in HealthKit, Loop will read those values from Apple HealthKit and display and use them in calculating temp basal rates. Entries from 3rd party apps can not be removed from within Loop.  You will have to edit them in the third party app, or from the Health app. Because of this potential for confusion, it is recommended to turn off Loop's ability to read other apps' carbohydrate data from HealthKit. You are asked if you want to enable this when Loop is first installed. After installation, you can also go to the Settings App -> Privacy -> Health -> Loop and turn off `Read Data for Carbohydrates`.

## Avoid Double Carb Entries
When you press `Save` for a carb entry, Loop will consider that carb entry saved and use it for calculating temp basals and recommended boluses.  Be cautious about repeated attempts to enter the same meal...Loop will continue to save the carb entries UNLESS you push cancel.  Simply not bolusing for the meal does not cancel the carb entry.
