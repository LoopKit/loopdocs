# Settings

!!! danger "Placeholder"

    This is a placeholder page - expect revisions.

The Settings screen has been completely updated for Loop 3 as shown in the graphic below.

![settings screen for loop 3](img/loop-3-settings.svg){width="250"}
{align="center"}

The page is a work in progress for Loop 3 - not all graphics have been populated, but the alt-text is provided.

For those coming from Loop 2.2.x

* Many of the Settings you may be familiar with are reached from Settings by tapping on [Therapy Settings](loop-3-therapy.md)
    * Note that changes to Therapy settings are protected by the same authorization required to dose insulin
* Nightscout can be added from Settings by tapping on Add Service (if you did not add it as part of onboarding)
* Issue Report is reached from Settings by tapping on Support
    * The Expiration Date for the Loop app is now included in the Issue Report

## Closed Loop

The user can enable closed loop or open loop using this slider.

![slider to enable or disable closed loop](img/loop-3-slider.svg){width="250"}
{align="center"}


This slider will be disabled under the following conditions.

* No Pump added
* No CGM added
* User has enacted a Manual Temp Basal
* User has suspended insulin delivery for the pump

## Dosing Strategy

This configuration setting gives you the ability to select the Dosing Strategy. 

![Dosing Strategy selection screen](img/dosing-strategy.svg){width="350"}
{align="center"}

Both Temp Basal Only and Automatic Bolus strategies restrict basal rates to reduce the amount of insulin delivered when appropriate to avoid future low glucose.

### Temp Basal Only

1. When your glucose is below target or predicted to go below target, negative temp basals (i.e., reduction of your scheduled basal rate) are used to reduce your IOB. This decision is re-evaluated during every Loop interval.
1. When your glucose is at or above target, Loop determines the amount of Recommended Bolus based upon your settings.  Subject to your Delivery Limits, Loop will deliver the Recommended Bolus over 30 minutes using positive temp basals (i.e., increase over your scheduled basal rate) to increase your IOB. This decision is re-evaluated during every Loop interval.

You can manually bolus at any time by pressing the Bolus icon in the center of the toolbar.

### Automatic Bolus

When you first starting Loop, we encourage you to leave automatic boluses disabled until you are sure your settings are dialed in.  To enable automatic boluses, click on Settings – Dosing Strategy – Automatic Bolus.  This Automatic Bolus checkbox turns-off positive temporary basal so that:

1. When your glucose is below target or predicted to go below target, negative temp basals (i.e., reduction of your scheduled basal rate) are used to reduce your IOB. This decision is re-evaluated during every Loop interval.
1. When your glucose is at or above target, you receive 40% of the Recommended Bolus at every Loop interval.

The Automatic Bolus selection causes Loop to provide 40% of the recommended dose as a bolus at the beginning of each Loop cycle (when a CGM reading comes in). This is a faster method of getting the recommended insulin delivered. When Loop delivers extra insulin, the scheduled basal rate continues unchanged.

As with all Loop versions, you can manually bolus at any time by pressing the Bolus icon in the center of Loop's Main Screen.  Any bolus recommendation that you see when you press the Bolus icon will be 100% of the Recommended Bolus.


## Configuration

The Configuration section allows entry to the following screens:

* [Therapy Settings](loop-3-therapy.md)
* [Pump Settings](loop-3-pump.md)
* [CGM Settings](loop-3-cgm.md)

## Services

The Services section allows additions of other services such a Nightscout

## Support

The Support section enables the user to provide output data about the app. This information can be very helpful to folks trying to assist with problem reports. It's a good idea to use the Issue Report button and save it along with a screen shot if you think you will ask for help.  You can always discard these if you resolve the problem on your own.

The Issue Report row creates a Loop Report text file with a lot of useful information for the developers if they need to assist you in solving an issue. This covers 84-hours (to enable a full pod history for users of Omnipod or Omnipod DASH).

The next two rows need to be explained - TO DO.

The last row creates a zip (compressed file) with detailed app information over a 7-day period. It is stored in a different format from the Loop Report.
