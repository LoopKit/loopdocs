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
* This LoopTips 3-page section on [Settings](https://loopkit.github.io/looptips/settings/overview/){: target="_blank" } is recommended.


Perhaps in subsequent versions of Loop, auto-adjustment of settings or machine learning could be incorporated. Until then, you will need to tell Loop if your underlying settings change or make temporary adjustments for short term issues.

The use of [Overrides](../operation/features/overrides.md) can be quite helpful for short-term changes.

## What does negative Active Insulin mean?

When Loop withholds or suspends some of your scheduled basal insulin, that starts an accumulation of insulin deficit. If you have a kinked cannula and insulin is not delivered, you'd call yourself "lacking insulin" (negative IOB).

When Loop reports negative IOB, it is a sign that Loop has been actively helping you prevent a low blood sugar. If you find significant negative IOB regularly, you probably need to [adjust/test your settings](https://loopkit.github.io/looptips/settings/settings/){: target="_blank" }. Glucose that continues to decrease (away from a meal) when IOB goes negative is typically a sign that the scheduled basal rate is too high.

!!! abstract "Developer Notes"
    Scheduled basal rates are meant to counteract your endogenous glucose production. Another way of saying this is that Loop expects your body to be producing an amount of glucose at a rate that is handled by your basal insulin settings.

    Your body doesn't really produce glucose at a fixed rate, but that's how it's modeled in Loop.

    "All models are wrong, but some are useful." (Quote attributed to British statistician George E. P. Box.)


## How is IOB calculated?

Insulin on board (IOB) is calculated from the amount of insulin delivered above or below the scheduled basal rate. For each dose of insulin, the insulin model is used to determine how much of that [insulin is active](../operation/algorithm/prediction.md#insulin-effect) over time. Loop is adding up all the amounts over the full Duration of Insulin Action (DIA). The DIA is 6 hours for most rapid insulin in the models used by Loop.

IOB is plotted on the [Active Insulin Chart](../loop-3/displays-v3.md#active-insulin-chart) in the main Loop display.

## How do Delivery Limits Affect Automatic Dosing?

With each cycle, _<span translate="no">Loop</span>_&nbsp;generates a glucose prediction and a recommended dose (positive or negative) to bring you to your correction range.

* The nearest 3 hours has more influence on the recommendation than the later 3 hours, but the entire 6 hours is considered
* The automated response to a negative recommended dose is to reduce basal rate, typically to zero
* The automated response to a positive recommended dose depends on your Dosing Strategy and is adjusted by your Delivery Limits

Let $\mathit{dose}$ be the amount the app thinks you need for this cycle before considering Delivery Limits. The relationship between $\mathit{dose}$, delivery limits: $\mathit{maximumBolus}$ and $\mathit{maximumBasalRate}$, and current IOB: $\mathit{currentIOB}$ are detailed in the following sections:

* [Manual Dose](#manual-dose)
* [Automatic Dose](#automatic-dose)
    * [Automatic Bolus: Constant Partial Application Factor](#automatic-bolus-constant-partial-application-factor)
    * [Automatic Bolus: Glucose Based Partial Application Factor](#automatic-bolus-glucose-based-partial-application-factor)
    * [Temp Basal Only](#temp-basal-only)

### Manual Dose

In this case, where you are manually requesting a bolus recommendation by using the double orange triangles (circled below) in the toolbar at the bottom of the Loop status screen, only the $\mathit{maximumBolus}$ Delivery Limit is considered.

![Loop toolbar](../operation/features/img/toolbar-bolus.svg){width="300"}
{align="center"}

* If $\mathit{dose}$ > $\mathit{maximumBolus}$: app recommends $\mathit{maximumBolus}$
* If $\mathit{dose}$ < $\mathit{maximumBolus}$: app recommends $\mathit{dose}$

### Automatic Dose

Because this will be an automatic dose, the app will not provide a dose that would exceed an IOB of 2 times the $\mathit{maximumBolus}$. The term automatic dose refers to insulin the app automatically delivers above your scheduled basal rate.

$$ autoDose = minimum (dose, {2*maximumBolus} - currentIOB) $$

Note that a manual dose can exceed $\mathit{autoDose}$. There will be no warning if this happens. But no additional automatic dosing will happen until IOB is below $\mathit{2*maximumBolus}$. As long as the prediction is above the correction range, scheduled basal continues regardless of IOB.

#### Automatic Bolus: Constant Partial Application Factor

There is a new feature coming with the next release, available now with customization or the development version, called Glucose Based Partial Application Factor. This feature is disabled by default. When disabled, the Partial Application Factor is a constant 40%.

* If $\mathit{autoDose}$ > $\mathit{maximumBolus}$: app boluses 40% of $\mathit{maximumBolus}$
* If $\mathit{autoDose}$ < $\mathit{maximumBolus}$: app boluses 40% of $\mathit{autoDose}$

#### Automatic Bolus: Glucose Based Partial Application Factor

When Glucose Based Partial Application Factor is enabled, the application factor is modified based on the current glucose level. The value ranges from 20% at lower glucose to 80% at higher glucose. Let $\mathit{gbpa\%}$ represent the application factor, then:

* If $\mathit{autoDose}$ > $\mathit{maximumBolus}$: app boluses $\mathit{gbpa\%}$ of $\mathit{maximumBolus}$
* If $\mathit{autoDose}$ < $\mathit{maximumBolus}$: app boluses $\mathit{gbpa\%}$ of $\mathit{autoDose}$

#### Temp Basal Only

This automatic method uses both Delivery Limits: $\mathit{maximumBasalRate}$ and $\mathit{maximumBolus}$. As explained above, the $\mathit{maximumBolus}$ is used to calculate [$\mathit{autoDose}$](#automatic-dose).

The desired dose, $\mathit{autoDose}$, is multiplied by two (to get an hourly rate) and then added to the scheduled basal rate to determine the desired temporary basal rate ($\mathit{BR_temp}$) with a duration of half-an-hour to provide that amount of insulin. This calculated $\mathit{BR_temp}$ is compared to $\mathit{maximumBasalRate}$.

* If $\mathit{BR_temp}$ > $\mathit{maximumBasalRate}$: app sets rate to $\mathit{maximumBasalRate}$
* If $\mathit{BR_temp}$ < $\mathit{maximumBasalRate}$: app sets rate to $\mathit{BR_temp}$

## More Algorithm Information

There is more detail about the Loop Algorithm at the bottom of the Operate tab.

* [Algorithm Overview](../operation/algorithm/overview.md)
    * [Bolus Recommendations](../operation/algorithm/bolus.md)
    * [Blood Glucose Prediction](../operation/algorithm/prediction.md)
    * [Automatic Adjustments](../operation/algorithm/auto-adjust.md)

