# Closed-Loop

After you learn what you need from open-loop, this page provides suggestions to smooth the transition to closed loop.

## Timing

Consider transitioning in steps.  Some loopers start closed-loop when there are fewer distractions, possibly on weekends, and, transition at a time that does not involve food, possibly overnight.

## Maximum Basal Rate

When starting closed-loop, it is important to be conservative. Start with the "Temp Basal Only" dosing strategy and limit the maximum basal rate.  These steps are important in case your other settings (e.g., carb absorption time, carb ratio, ISF) are incorrect to avoid overly aggressive increases in insulin. Typically, experienced loopers set their max closed-loop basal rate at no more than 3-4 times their average basal rate.  Wait until you are comfortable with the slower corrections in "Temp Basal Only" before transitioning to "Automatic Bolus".

!!! info "Temp Basal Only vs Automatic Bolus"
	Both Dosing Strategy methods update the prediction with every CGM or glucose reading, typically every 5 minutes, and uses the updated prediction to modify dosing.
	
	* "Temp Basal Only" provides no more than 17% of what Loop predicts you will need and updates the calculation every 5 minutes (using temporary basal)
    * "Automatic Bolus" mode provides 40% of what Loop predicts you will need as an immediate bolus and updates the calculation in 5 minutes

## Glucose Correction Range

If your basal, ISF, or carb ratios are not correct, Loop may give you more insulin than you need to reach the correction you selected. Setting the correction range slightly higher at first helps prevent unexpected low glucose as you adjust your settings.

## Watch the IOB

Watch whether Loop accumulates positive or negative IOB while holding your glucose steady when no food is present.  If you consistently have positive or negative IOB, review whether to adjust your  basal rate or ISF.

!!! tip "Expert Tip"
	In the absence of food, glucose trends should flatten out when positive or negative IOB trends to zero.

	* If glucose drops below the correction range and continues to drop while IOB goes negative, basal rates may be too high
	* If glucose remains above the correction range while IOB remains positive, basal rates may be too low
	
	The ISF is also important, but basal should be evaluated first.

## Meals

Start with meals that you know well. If Loop suggests far less or far more insulin than expected as a bolus before the meal - consider why this may be true.

* If glucose is trending down, Loop may be trying to prevent a low glucose event
* If glucose is trending up, Loop may be trying to add a correction to the meal dose
* In any case:
	* You can adjust the absorption time and carb amount to see if that modifies the suggested bolus
	* You can override the Loop suggestion
	* Do not be surprised if Loop immediately suspends basal
	* Loop needs to see glucose start to rise before deciding you need more insulin
	* Loop will not automatically provide more insulin until your glucose is above the lower range of the correction range (but will recommend a manual bolus)

This is definitely an area where YDMV (your diabetes may vary), so don't expect or accept that what works for others will work for you.  Test, observe, and adjust as needed.
