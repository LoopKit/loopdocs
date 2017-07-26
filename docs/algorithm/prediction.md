# Glucose Prediction

All of Loop's insulin dosing decisions are based on the different between the target glucose and Loop's glucose prediction. 
Therefore, the best way to understand Loop's recommendations is to understand the prediction.  Loop makes a new glucose
prediction every five minutes by computing the effects of insulin that has been administered from the pump, and carbohydrate
records that have been entered into Loop. Two additional terms, glucose momentum, and optionally retrospective correction are
also used. 

You can see the individual contributions of these effects by tapping on the predicted glucose graph on Loop's
status screen. In addition, by tapping on the Active Carbohydrates screen, you can see important information about 
carbohydrate absorption that affects the glucose prediction, which is discussed in more detail below.

On the glucose screen, you will see that Loop says glucose will "eventually" reach a level.  This eventual time is at the end of the Duration of Insulin Action - the DIA, which you have supplied in the settings screen.  So, if you are currently at 130, and Loops shows "eventually 105", and you supplied a DIA of 4 hours, that means that in four hours, the blood glucose is predicted to be at 105.  It makes sense to anchor the dosing recommendations on the prediction at the end of the DIA becasue that's when all the insulin is expected to be absorbed, so from that point the glucose should be stable - unless there are slow burning carbs that are longer than the DIA, which is discussed below.  Loop also calculates the predicted path of the glucose, and will suspend insulin delivery if the prediction is expected to go below the Minimum BG Guard Level, which you also supply in the settings screen. This avoids hypoglycemia in situations where carb absorption is delayed, or as a result of pre-bolusing too far in advance.

The easiest way to understand the glucose prediction is the follow a specific example through.  Assume the following, about to bolus for a meal with no pre-bolusing:

Target 100
I/C 6
ISF 75
DIA 4 hours

Carbs consumed 30
Expected carb absorption time 2 hours

Recent BG trend: -3 mg/dl/5 minutes
Current BG 145

In this example we are assuming a meal is about to be consumed.  It's important to realize that Loop's bolus recommendation is not the simple "bolus wizard" math of carbs/IC ratio.  Rather, Loop first calculates the predicted eventual glucose without any bolus.  It then compares that prediction to the target.  The bolus recomendation is then (prediction - target)/ISF. 

The first driver of the glucose prediction is the glucose momentum.  In essence, glucose momentum says that what has been happening over the last 15 minutes is probably the best prediction of what will happen over the next half hour.  Mathematically, Loop takes the regression coefficient of the last 3 glucose measurements (one every 5 minutes, so looking back 15 minutes) to get the recent trend.  This is pretty close to taking the average of the last 3 changes.  You can see the changes in mg/dl/5 minutes in Nightscout - this is also the value that drives the trend arrows in Loop and the CGM.  Then, Loop looks forward to the next half hour and applies the calculated trend, decaying to 0.  This is pretty similar to taking the average change of the last 15 minutes, dividing it in half, using it to project forward for the next half hour.  So in our example, glucose momentum would suggest that in 30 minutes, the blood glucose will be 136. (`144 -3/2*6`)

From that point, Loop needs to know the effect the carbs about to be consumed will have.  Since the glucose momentum pre-dates the meal, the effect of the carbs to be consumed is additional to the momentum-based forecast.  So, with 30 carbs consumed, and ISF of 75, and an I/C of 6, the CSF (carb sensitivity factor - how much the BG will change per gram of carbs) is 12.5 (ISF/IC).  Therefore, 30 grams of carbs consumed without any insulin will raise the blood glucose by `30*12.5` = 375 points.  If we add this to the predicted value from the momentum, we get 511 (`136+375`).  Scary! but of course this is without insulin. Loop then compares the prediction of 511 to the target of 100, producing a difference of 411.  Divide 411 by the ISF and the necessary insulin to treat to target is 5.48.  That will be Loop's recommended bolus.  Once that bolus is delivered, the eventual glucose should show a number very close to 100 - the target. For most T1Ds it's probably easier to think of this calculation in two parts - how much insulin to cover the carbs (30/6, or 5 units) and how much to correct the current BG back to target (`(145-100)/75 = .6`). In this situation a reasonable bolus might be 5.6 units.  Some T1Ds, recognizing the recent downward trend, would back off the bolus a little bit; in this case Loop says that without doing anything, we expect the BG to drop to 136.  So the needed correction is only `36/75 = .48`.  That produces a total bolus recommendation of 5.48 units.

So far, the prediction is pretty straightforward and easy to reproduce in your head.  But once the bolus is delivered and the carbs start getting absorbed is when things start to get interesting and Loop really starts making a difference.  The first key question the algorithm has to answer is - how much insulin is left? To answer this question, Loop uses an Insulin On Board (IOB) curve.  For every dose of insulin taken at a point in time, the IOB curve gives an amount remaining at a point in the future.  For example, with DIA set to 4, Loop assumes TK% of the insulin is left after the first hour, Y% after the second, Z% after the third, and that it is gone after the fourth.  So, assume you are running high, and you haven't eaten for a long time so there are no carbs to absorb left.  Say you are at 175.  You might decide to correct and take a one unit bolus.  With a DIA of 4, we expect the correction to take 4 hours, and eventually deliver you to the target of 100.  But what is the path? the IOB curve says that .3 units are delivered in the first hour; .4 units in the second; .3 in the third and .1 in the fourth.  This means that in the first hour you will drop `.3*75 = 22.5` mg/dl, so you'll be at 152.5.  Of course, in the first hour, the drop will not be smooth; probably very little will happen in the first 20 or 30 minutes (YDMV) and the bulk of the 22.5 point drop will happen in the second half hour, continuing into the second hour - this is people refer to as the "peak".  But it's important to realize when dealing with Loop that the peak just means that's is the moment when the most insulin is being absorbed; but some is absorbed before the peak, and quite a bit is absorbed after the peak.  In this case, after the second hour, you are past the peak but there is still .3 of unit on board, and the BG still has 22.5 points to drop.   After 3 hours .9 units have been delivered so you will have dropped 67.5 mg/dl and you will be at 107.5.  Loop does this calculation for every 5 minute increment into the future until all the insulin is gone, in order to know what the expected effect of insulin is at every point in the future.  

This section needs to be fleshed out with details of how insulin and carb
effects are calculated, and how momentum and retrospective correction work. For
now, refer to:

  -  [CarbStore.getGlucoseEffects()](https://github.com/LoopKit/LoopKit/blob/master/CarbKit/CarbStore.swift#L615)
  - [DoseStore.getGlucoseEffects()](https://github.com/LoopKit/LoopKit/blob/master/InsulinKit/DoseStore.swift#L936)
  -  [GlucoseStore.getRecentMomentumEffect()](https://github.com/LoopKit/LoopKit/blob/master/GlucoseKit/GlucoseStore.swift#L244)
  - [LoopDataManager.updateRetrospectiveGlucoseEffect()](https://github.com/LoopKit/Loop/blob/master/Loop/Managers/LoopDataManager.swift#L445)
