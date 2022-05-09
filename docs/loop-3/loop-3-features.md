# Features

This page discusses updated versions of Loop features as well as new capabilities provided with Loop-dev.


## Carb Data Source

There were many instances with prior versions of Loop where a user would use a "food" app that stored information in Apple Health, not realizing that Loop would read that entry and start adjusting insulin delivery.

To avoid this problem, Loop-dev is designed with a separate carbohydrate storage system that does not rely on Apple Health.  Loop still writes carbohydrate entries to Apple Health but it does not read carbohydrate entries from Apple Health.

There are some experienced loopers who want to modify the code to enable Loop to read carbohydrate records from Apple Health with the full understanding of how that works.  This code customization option is discussed in zulipchat.

## Non-Pump Insulin

There are times when a looper needs to let Loop know they have taken insulin from a different source. The instruction with Loop 2.2.x was to manually enter the dose into the Apple Health app for Insulin and Loop would import that value.

With Loop-dev, the "old" method still works, but there is a new method for entering this information that provides the user with updated `Glucose` predictions based on that dose and enables the user to indicate the type of insulin taken so that the appropriate model is used by Loop.  

1. By tapping on either of the insulin charts (Active Insulin or Insulin Delivery) on the home screen, the Insulin Delivery Screen is displayed with 3 tabs.
    * **Event History** (default) is the same as for Loop 2.2.x
    * **Reservoir** is similar to Loop 2.2.x; however, the reservoir value from a prior pod is not displayed after a new pod is applied
    * **Non-Pump Insulin** is a new feature with Loop-dev


2. Select the `Non-Pump Insulin` tab to bring up the graphic shown below
    * Tap on the + sign (green solid lines)
    * `Log Dose` screen is displayed showing the current `Glucose` prediction
    * The default insulin type is that used by the pump
    * To modify Insulin Type, tap on that row (red dashed lines)
        * Picker wheel allows other insulin models to be selected
        * _At the current time, no model is in place for Afrezza_
    * Tap on the `Bolus` row (blue dash-dot lines) to bring up a keyboard
        * As a value is entered using the keyboard, the `Glucose` prediction chart updates automatically
        * Tip, add 0.001 to the actual dose to make it easier to see if reviewing in Apple Health
        * Once the user selects `Done` on the keyboard display, the entered value is displayed on the `Bolus` row and the `Log Dose` button changes from gray to blue
        * Tap on `Log Dose` to record or `Cancel` to quit

![entering non-pump insulin into Loop](img/non-pump-insulin.svg){width="500"}


## Bolus Entry

The bolus following carbs (`Meal Bolus`) and manual bolus (`Bolus`) screens are updated from Loop 2.2.x. There is still a predicted `Glucose` chart that actively updates as the bolus value is updated and various buttons. 

* With Loop 2.2.x
    * The Recommended Bolus is provided but the default for the Bolus value is 0
    * If the user taps on the Recommended Bolus row, the recommended amount is transferred to the Bolus row
* With Loop-dev
    * The Recommended Bolus is provided AND the default for the Bolus is the recommended value
    * If the user taps on the Bolus row, the amount is modified to 0 and the keyboard is opened for entry

!!! info "Blue Means Active"
    * For those who can see colors, the blue color indicates an active button.
    * The value displayed on the `Bolus` row is blue to indicate if you tap on that, you can edit the value

### Meal Bolus Screen

When the `Meal Bolus` screen is entered following a carb entry or edit action, the active button might be `Save and Bolus` or, if no bolus was recommended, `Save without Bolusing`. 

Some people reported issues with the overlap between buttons and the keyboard for the `Meal Bolus` screen when choosing an option other than `Save and Bolus`.

* This interface might be modified, so graphics have not been prepared
* There are several topic threads in zulipchat


### Manual Bolus Screen

When the `Bolus` screen is entered direct from the toolbar, the button choices are `Enter Bolus` if none is recommended, `Deliver` if a value is on the `Bolus` row or `Cancel`. The user can also tap on the value on the `Bolus` row to bring up a keyboard to modify that amount. When doing that, the value is automatically set to zero.

The two graphics below are from entering selecting manual bolus from the toolbar. 

* In the first graphic, no bolus was recommended 
* In the second graphic, a recommended amount is shown

![manual bolus when no bolus recommended](img/loop-3-manual-bolus-no-rec.svg){width="350"}
{align="center"}

![manual bolus when bolus is recommended](img/loop-3-manual-bolus-rec.svg){width="350"}
{align="center"}


## Remote Carb / Bolus

Loop-dev has a Remote Carb and Remote Bolus feature to enable remote caregivers to better assist the person who needs support managing with Loop.

The author of this feature wrote this [Remote Carb/Bolus Guide](https://docs.google.com/document/d/1wPpCljo9NuwllltjhImf7YZReIgqP9yF05PN7E6hphM/edit#) documentation. Please read carefully and use with the appropriate level of caution.

!!! warning "WARNING"

    You will be using this feature at  your own risk, like any other Loop code you build. It is very important you completely read and re-read the [Remote Carb/Bolus Guide](https://docs.google.com/document/d/1wPpCljo9NuwllltjhImf7YZReIgqP9yF05PN7E6hphM/edit#) before getting started. 
    
    There are validation and troubleshooting steps for each section of the guide. 
    
    Please make sure not to skip sections as this makes it difficult to troubleshoot.
    
    Be aware:
    
    * Apple limits how many push notifications (used by this feature) can be received on an iOS device
    * If the system feels too many are being sent, it may begin to throttle notifications
    * There is not a published limit, but consider limiting it to 1 per hour
    * When on cellular data, there may be further limitations to protect your data usage
 
