## Recommended Bolus

The *Loop* app will recommend bolus insulin corrections when the eventual glucose is greater than the correction target and the active insulin plus any active 30-minute temporary basal will not be sufficient to cover the predicted excursion above correction target.

These recommendations are not proactively sent to the *Loop* user through any notification or banner alert; the recommendation is only viewable when the user clicks on the bolus tool. Note that *Loop* never issues a bolus command automatically while using the default Temp Basal Only [Dosing Strategy](../../loop-3/settings.md#dosing-strategy); all boluses are initiated by the user unless the [Automatic Bolus](../../loop-3/settings.md#automatic-bolus) dosing strategy is enabled. With automatic bolus enabled, each automatic bolus is limited to 40% of the recommended amount or the maximum bolus setting, whichever is smaller.

The recommended bolus calculation is described in [Determine the Recommended Dose](auto-adjust.md#determine-the-recommended-bolus){: target="_blank" }, with these exceptions:

* the insulin contribution from the currently running temporary basal set by *Loop* is removed or subtracted from the recommended bolus amount, and  
* the delta is calculated for the top of the correction range, rather than the average of the correction range.

### Slow Absorption Time (Extended Bolus)

For recently saved carbohydrates with longer absorption time, e.g., very slow-digesting meals like pizza or pasta, Loop’s algorithm provides an initial meal bolus less than the simple grams divided by carbohydrate ratio calculation for [Carbohydrate Effect](prediction.md#carbohydrate-effect){: target="_blank" }.

The *Loop* algorithm computes the recommended bolus such that predicted glucose will not dip below the Glucose Safety Limit. This may result in future glucose levels predicted above correction range, but will prevent a hypoglycemia event shortly after the meal.

* As time progresses after the meal, when appropriate, *Loop* modifies insulin delivery
* A decrease in recommended insulin amount is always provided as a decreased Temporary Basal rate
* An increase in recommended insulin amount is delivered based on the user-selected [Dosing Strategy](../../loop-3/settings.md#dosing-strategy){: target="_blank" }:
    * Temp Basal Only: [Increase Basal Rate](auto-adjust.md#increase-basal-rate){: target="_blank" }
    * Automatic Bolus: 40% of the recommended amount
* In effect, this algorithm behavior mimics traditional pump therapy of “extended” or “dual wave” bolusing, but with the benefit of added information about actual carbohydrate absorption effects as time goes by

Finally, *Loop* checks that the result of the calculations is below the maximum single bolus the *Loop* user specified in their settings. If the calculated bolus is less than the maximum single bolus setting, then the recommended bolus will be displayed in Loop’s bolus tool.

!!! info "Bolusing safety feature"

    If the current glucose, or any predicted glucose, falls below the Glucose Safety Limit, *Loop* will not return a recommended bolus. When the minimum glucose rises above the Glucose Safety Limit, the bolus tool will provide a recommended bolus.

## Algorithm Section Menu

* [Algorithm Overview](overview.md)
    * [Bolus Recommendations](bolus.md)
    * [Glucose Prediction](prediction.md)
    * [Automatic Dosing Adjustments](auto-adjust.md)
