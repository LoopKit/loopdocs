# Pump Configuration

The pump configuration can be selected from the Heads-Up-Display ([HUD](loop-3-displays.md#heads-up-display)) or from the [Loop Settings](loop-3-settings.md) screen.

## Add Pump

The HUD will look like the graphic below if no CGM or Pump is configured for Loop:

![Loop HUD when both CGM and Pump have not been added](img/loop-3-hud-add-cgm-add-pump.svg){width="350"}
{align="center"}

If no pump has been configured, the user has a choice of 3 pumps and a simulator:

* Minimed 500/700 Series
* Omnipod
* Omnipod DASH
* Insulin Pump Simulator


For all pumps, there is now an new selection option prior to adding the pump:

* Insulin Type
    * User can select from Rapid (Novolog, Humalog, Apidra) or Ultra-Rapid (Fiasp, Lyumjev)

If a user selects Minimed 500/700 Series, follow these directions to [add a Medtronic Pump](../operation/loop-settings/mdt-pump.md).

If a user selects Omnipod, this is an Omnipod Eros selection which requires a RileyLink compatible device. TO DO - UPDATE THIS. New user interface. OUT-OF-DATE: Follow these directions to [add Omnipod](#add-omnipod).

If a user selects Omnipod DASH, this is the Bluetooth enabled Pod which does not require a RileyLink compatible device. Tapping on that row brings up the new user interface for DASH. Please refer to these instructions to [add Omnipod DASH](#add-omnipod-or-omnipod-dash).

If a Medtronic pump is configured, tapping on the pump icon leads to the same [Pump Settings Screen](../operation/loop-settings/pump-commands.md) as Loop 2.2.x. (TO DO - there is  a difference in the Medtronic screen - revise and update links.)

If an Omnipod or Omnipod DASH pod has been configured, tapping on the pump icon leads to the [Omnipod or Omnipod DASH Pump Screen](loop-3-omnipod.md).

## Modify Pump

You must first delete the old pump before you can switch to a new pump type.

If you are using Pods, you must first deactivate your current pod.  After the pod has been deactivated, a new row will show at the bottom of the pod setting screen. Tap on `Switch to other insulin delivery device` and follow the directions to complete the task. The HUD will now show the add pump icon and you can [select a new pump](#add-pump).





## Add Omnipod

For Omnipod, you must first select a RileyLink compatible device to enable communications with the Omnipod pods.  After that, continue with the next section.

TO DO - make a page that explains this for Medtronic or Omnipod.

## Add Omnipod or Omnipod DASH

When you select Omnipod (and have chosen a RileyLink compatible device) or Omnipod DASH you will need to configure default settings for the following 3 items.  These default values can be modified later in the [Configuration](loop-3-omnipod.md#dash-configuration) section of the Pump Settings screen.

1. Expiration Reminder
    * No Reminder 
        * Pod is silent until it expires
    * Reminder between 1 and 24 hours before expiration
        * Pod beeps the "expiration" alert pattern until acknowledged by user through the Loop app
1. Low Reservoir
    * Loop app provides a [modal alert](onboarding.md#what-does-modal-mean) when reservoir reaches value selected (10 to 50 U)
1. Insulin Type
    * User can select from Novolog, Humalog, Apidra, Fiasp, or Lyumjev
    * Only the first three (rapid insulin) types have a [different model for children and adults](onboarding.md#insulin-model).
    

A [video is found here for pairing an Omnipod DASH pod](https://drive.google.com/file/d/1mN5s8-oorvoa-gbjAaYbnUnl_-vvuhNC/view?usp=sharing). Once the pod starts priming, you may want to skip ahead in the video (it takes about a minute to prime). The Omnipod pairing protocol is the same. The only difference is that Omnipod requires a RileyLink compatible device and there are slight differences in some of the text, e.g., Omnipod DASH uses a blue needle cap and Omnipod has a clear needle cap.


