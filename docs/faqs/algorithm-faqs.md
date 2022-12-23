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

When Loop reports negative IOB, it is a sign that Loop has been actively helping you prevent a low blood sugar. If you find significant negative IOB regularly, you probably need to [adjust/test your settings](https://loopkit.github.io/looptips/settings/settings/). Glucose that continues to decrease (away from a meal) when IOB goes negative is typically a sign that the scheduled basal rate is too high.

!!! abstract "Developer Notes"
    Scheduled basal rates are meant to counteract your endogenous glucose production. Another way of saying this is that Loop expects your body to be producing an amount of glucose at a rate that is handled by your basal insulin settings.

    Your body doesn't really produce glucose at a fixed rate, but that's how it's modeled in Loop.

    "All models are wrong, but some are useful." (Quote attributed to British statistician George E. P. Box.)


## How is IOB calculated?

Insulin on board (IOB) is calculated from the amount of insulin delivered above or below the scheduled basal rate. For each dose of insulin, the insulin model is used to determine how much of that [insulin is active](../operation/algorithm/prediction.md#insulin-effect) over time. Loop is adding up all the amounts over the full Duration of Insulin Action (DIA). The DIA is 6 hours for most rapid insulin in the models used by Loop.

IOB is plotted on the [Active Insulin Chart](../loop-3/displays_v3.md#active-insulin-chart) in the main Loop display.

## More Algorithm Information

There is more detail about the Loop Algorithm at the bottom of the Operate tab.

* [Algorithm Overview](../operation/algorithm/overview.md)
    * [Bolus Recommendations](../operation/algorithm/bolus.md)
    * [Blood Glucose Prediction](../operation/algorithm/prediction.md)
    * [Temp Basal Adjustments](../operation/algorithm/temp-basal.md)

