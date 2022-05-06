# Pump Configuration

The pump configuration can be selected from the [HUD](loop-3-displays.md#heads-up-display) or from the [Loop Settings](loop-3-settings.md) screen.

## Add Pump

If no pump has been configured, the user has a choice of 3 pumps and a simulator:

* Minimed 500/700 Series
* Omnipod
* Omnipod DASH
* Insulin Pump Simulator

For all pumps, there is now an new selection option prior to adding the pump:

* Insulin Type
    * User can select from Rapid (Novolog, Humalog, Apidra) or Ultra-Rapid (Fiasp, Lyumjev)

If a user selects Minimed 500/700 Series, follow these directions to [add a Medtronic Pump](../operation/loop-settings/mdt-pump.md).

If a user selects Omnipod, this is an Omnipod Eros selection which requires a RileyLink compatible device. Follow these directions to [add Omnipod Eros](../operation/loop-settings/omnipod-pump.md).

If a user selects Omnipod DASH, this is the Bluetooth enabled Pod which does not require a RileyLink compatible device. Tapping on that row brings up the new user interface for DASH. Please refer to these instructions to [add Omnipod DASH](#add-dash-pod).

If a Medtronic or Omnipod Eros pump is configured, tapping on the pump icon leads to same [Pump Settings Screen](../operation/loop-settings/pump-commands.md) as Loop 2.2.x.

If an Omnipod DASH pod has been configured, tapping on the pump icon leads to the [DASH Pump Screen](dash-pump.md).

## Modify Pump

You must first delete the old pump before you can switch to a new pump type.

If you are using Pods, you must first deactivate your current pod.  After the pod has been deactivated, a new row will show at the bottom of the pod setting screen. Tap on `Switch to other insulin delivery device`. The HUD will now show the add pump icon and you can [select a new pump](#add-pump).


## Add DASH Pod

When you select DASH you will need to configure default settings for the following 3 items.  These default values can be modified later in the [DASH Configuration](dash-pump.md#dash-configuration) section.

1. Expiration Reminder
    * No Reminder 
        * Pod is silent until it expires
    * Reminder between 1 and 24 hours before expiration
        * Pod beeps the "expiration" alert pattern until acknowledged by user through the Loop app
1. Low Reservoir
    * Loop app provides a [modal alert](onboarding.md#what-is-a-modal-alert) when reservoir reaches value selected (10 to 50 U)
1. Insulin Type
    * User can select from Rapid (Novolog, Humalog, Apidra) or Ultra-Rapid (Fiasp, Lyumjev)
    


For those using the DASH pods, the user interface screens have been completely rewritten, [DASH Pod Screen](dash-pump.md) 

A [video is found here for pairing a DASH pod](https://drive.google.com/file/d/1mN5s8-oorvoa-gbjAaYbnUnl_-vvuhNC/view?usp=sharing). Once the pod starts priming, you may want to skip ahead in the video (it takes about a minute to prime).


