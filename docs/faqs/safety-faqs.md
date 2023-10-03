## Know your settings

Do not enter settings that you are unsure of. For example, if you haven't any idea what your carb ratio is, please don't enter a wild guess. Instead, test your settings and talk to your health care provider about what your appropriate settings should be.

## Understand the App Displays

If you do not understand the components displayed in the graphic below, please spend time reviewing the information at [Displays](../loop-3/displays-v3.md).

![main loop screen when running nominally with annotation for heads-up-display, charts and toolbar](../loop-3/img/loop-3-main-annotated.png){width="450"}
{align="center"}

## Carb Entry and Insulin Delivery

If you configured the app with closed-loop enabled:

* Once carbohydrates are entered into&nbsp;<span translate="no">Loop</span>, the algorithm will begin to dose insulin to anticipate those carbs

If you entered carbs and then changed your mind on the amount or the time at which they were eaten, use these [instructions](../operation/features/carbs.md#edit-meals) to delete or edit them. This will make&nbsp;<span translate="no">Loop</span>&nbsp;better able to predict blood glucose and adjust insulin delivery appropriately.

## How to Cancel a Bolus

Once a bolus starts, the progress of that bolus appears in the [HUD Status Row](../loop-3/displays-v3.md#hud-status-row). Note that the phone must be held in portrait mode to see this. Simply tap on the row that shows the delivery to halt the bolus.

![bolus-in-progess message: message size is 500 x 50 pixels](../loop-3/img/status-row-bolus-in-progress.svg){width="350"}

## Understand Delivery Limits

With each cycle, <span translate="no">Loop</span>&nbsp;generates a glucose prediction and a recommended dose (positive or negative) to bring you to your correction range.

* The automated response to a positive recommended dose depends on your Dosing Strategy and is adjusted by your Delivery Limits

For more information, please read [How do Delivery Limits Affect Automatic Dosing?](algorithm-faqs.md#how-do-delivery-limits-affect-automatic-dosing).

## Health app permissions

For older versions of&nbsp;<span translate="no">Loop</span>, or if you customized&nbsp;<span translate="no">Loop 3</span>&nbsp;to read carbohydrates from third-party apps, be aware that you cannot edit those entries inside the&nbsp;<span translate="no">Loop</span>&nbsp;app.

If you let other apps, such as MyFitnessPal, write carbohydrates to the Health app, <span translate="no">Loop</span>&nbsp;could read those carbohydrates and you could be dosed for those carbohydrates.

* <span translate="no">Loop 3</span>: review [Customization: Build Time Features](../build/code-customization.md#build-time-features)
* <span translate="no">Loop 2</span>: Check your [Health](../build/health.md#loop-permissions) permissions and review .

## Beware the Medtronic Easy Bolus button

Medtronic's easy bolus button has been the cause of several accidental boluses when the pump has been carried in a pocket. Best practice would be to disable the Easy Bolus button since you will be doing boluses from the phone anyways.

## Finish your Medtronic priming

After a site change and reservoir rewind, Medtronic's pump will have a menu on the pump screen related to finishing your prime. Make sure you complete that screen and always return to the main menu. Medtronic's pump won't resume basal insulin delivery until that priming screen is completed.
