# Carb Entry

<p align="center">
<img src="../img/toolbar.png" width="400">
</p>

New carb entries can be made by using the green carb tool in the toolbar at the bottom of the status screen.  Do not use your pump's bolus wizard or pump's carb entry to record carbs into the Loop app.  Nor should you use Nightscout's careportal to enter carbs, as Loop does not read carb entries remotely.

## New Carbs

To begin a new meal entry, simply enter the number of carbs to be eaten in the `amount consumed` line.  By default, the carb absorption time for a new carb entry will correspond to the taco icon.  If you haven't made any customizations to the lollipop, taco, or pizza icons during your Loop build, then the default carb absorption time will display as 3 hours.  The default time entry is for the current time and date.  Once you press `Save` on the carb entry screen, the Loop's bolus tool will open to provide a recommended bolus.

<p align="center">
<img src="../img/carb_entry.png" width="300">
</p>

## Avoid Double Carb Entries

!!!info "Be Aware"
    When you press `Save` for a carb entry, Loop will consider that carb entry saved and use it for calculating temp basals and recommended boluses.  Be cautious about repeated attempts to enter the same meal...Loop will continue to save the carb entries UNLESS you push cancel on the carb entry screen.</br></br>
    **Simply canceling a bolus does not cancel the carb entry.**</br></br>
    If you have accidentally made multiple entries for the same carbs, click on the Carbs Chart in the main Loop display and you can delete the redundant carb entries by swiping left on the entries.


## Carb Absorption Time

<p align="center">
<img src="../img/food_icons_times.png" width="300">
</p>

To select your carb entry's absorption time, you can either click on the default food emojis or manually enter carb absorption time by selecting the `absorption time` line in the carb entry tool.

Tapping the `Food Type` row can also be used if you are unsure of a new food.  There are other food emojis grouped into fast, medium, and slow absorbing foods.  This may be particularly useful for teens that are trying to learn new foods/meals.  Additionally, you can add text to your `food type` by selecting the `abc` button in the bottom left corner of the screen.

<p align="center">
<img src="../img/plate.png" width="300">
</p>

<p align="center">
<img src="../img/ns-plate.png" width="900">
</p>

The default carb absorption times in Loop app are average representations for high, medium, and low glycemic index foods.  Ever since Loop v1.4.0, the algorithm incorporates dynamic carb absorption.  Previous Loop versions were based on a curve that assumed the rate of carb absorption would start out slow, increase to a mid-point, and then taper off.  However, in the real world, carb absorption is quite variable.  Dynamic carb absorption model is able to model some of this variability and allow Loop to respond more reasonably when actual carb absorption is not matching well with the selected carb absorption time for a meal.  In short, while entering a carb absorption time is still part of recording meals in Loop, it is much less critical to get it right.  Now your entry serves more as a guideline, than a rule, for Loop to model carb absorption.  For a more detailed explanation of the new dynamic carb absorption model, please read about it [here](https://github.com/LoopKit/Loop/pull/507).

To help Loop adjust for carbs that may digest slower than your original estimate, Loop will initially apply a 1.5x multiplier to your entered carb absorption time.  So, a meal entered using the taco icon will initially be treated as a 4.5 hour absorption meal.  As Loop observes the BG impacts of the meal, Loop will shorten the meal's absorption time if BGs are showing quicker impacts than expected, as well as adjust insulin deliveries (e.g., increase temp basals).  You can watch the progression of the Loop's observations of your meal by clicking on the Carbs Chart and watching the insulin counteraction effects.

## Mixed Carb Meals

You do not have to enter all carbs for a meal at the same absorption or eating time.  If you want to enter some of the meal's carbs as faster, and some slower, you can log the meal over several individual carb entries.  For example, for meals that have sugary carbs as well as slow acting carbs (Chinese food), you may wish to do part of the carbs as lollipop and part of the carbs as pizza.

Pressing the `Save` button in the top right corner will save the carbs into the Loop app and bring up the Loop's bolus tool.  When entering multiple carb absorption durations for a single meal, press save on the carb entry and then press cancel on the bolus tool when it appears.  When you have entered your last carb entry for the meal, then use the bolus tool to deliver the bolus for the entire meal.  Loop will provide a recommendation based on all the saved carbs and their respective absorption durations in total.

## Prebolus 
You can let Loop know you are going to prebolus a meal by adjusting the time of the carb entry on the “date” line of the carb entry.  If you are prebolusing by 20 minutes, simply add 20 minutes to the carb entry time.  

## Edit Carbs

Clicking on the Carbohydrate chart in the Loop's main status screen will open the carb entry history and previous entries can be modified or deleted through this screen.  If you need to change a prebolus time, add/subtract carbs, adjust carb absorption times (even mid-meal), just go into that edit screen and tap on the carb entry you'd like to edit, or left-swipe to delete the entry entirely.  This can be a particularly useful tool when:

* You did not finish an entire meal that you bolused for,
* You did not get to eat meal at the time you originally expected,
* You ate more servings than originally entered, or
* You suspect your carb count was in error because BGs are rising more/less than expected.

<p align="center">
<img src="../img/carb_edit.png" width="300">
</p>

## Third Party Apps
If you use a 3rd party app, such as My Fitness Pal, to enter and track carbs and that app also stores the carb values in HealthKit, Loop will read those values from Apple HealthKit and display and use them in calculating temp basal rates. Entries from 3rd party apps can not be removed from within Loop.  You will have to edit them in the third party app, or from the Health app. Because of this potential for confusion, it is recommended to turn off Loop's ability to read other apps' carbohydrate data from HealthKit. You are asked if you want to enable this when Loop is first installed. After installation, you can also go to the Settings App -> Privacy -> Health -> Loop and turn off `Read Data for Carbohydrates`.

