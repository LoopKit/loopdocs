# Bolus Recommendations

Loop will recommend bolus insulin corrections when the eventual blood glucose is greater than the correction target and the active insulin plus any active 30 minute temporary basal will not be sufficient to cover the predicted excursion above correction target. These recommendations are not proacrtively sent to the Loop user through any notification or banner alert; the recommendation is only viewable when the user clicks on the bolus tool. Note that Loop never issues a bolus command automatically; all boluses are initiated by the user. 

The bolus dose calculation is identical to the dose equation given in the basal recommendations section, with the exception that:

* the insulin contribution from the currently running temporary basal set by Loop is removed or subtracted from the recommended bolus amount, and  
* the delta is calculated for the top of the correction range, rather than the average of the correction range.

For recently saved carbohydrates where the projected carbohydrate absorption will outlast the insulin activity duration (e.g., very slow digesting meals like pizza or pasta), Loop’s algorithm will inherently decrease the initial meal bolus — to prevent hypoglycemia events that often occur after these meals — by only recommending enough bolus to prevent going below the correction range. As described above, the Loop algorithm computes the recommended bolus such that predicted glucose will not dip below the correction range. This may result in a future blood glucose predicted above correction range, but will prevent a hypoglycemia event shortly after the meal (as is sometimes occurs for people giving a "pizza bolus" in traditional pump therapy). Loop will then later make corrections by issuing higher temporary basals. In effect, this algorithm behavior mimics traditional pump therapy of “extended” or “dual wave” bolusing, but with the benefit of added information about actual carbohydrate absorption effects as time goes by.

Finally, Loop checks that the result of the calculations are below the maximum single bolus the Loop user specified in their settings. If the calculated bolus is less than the maximum single bolus setting, then the recommended bolus will be displayed in Loop’s bolus tool.

!!!info "Bolusing safety feature"
    If the current blood glucose, or any predicted blood glucose, falls below the suspend threshold, Loop will not return a recommended bolus. When the minimum blood glucose rises above suspend threshold, the bolus tool will provide a recommended bolus.
