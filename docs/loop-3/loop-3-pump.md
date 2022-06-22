# Pump Configuration

## Pump Choices

The pump configuration can be selected from the Heads-Up-Display ([HUD](loop-3-displays.md#heads-up-display)) or from the [Loop Settings](loop-3-settings.md) screen.

The HUD will look like the graphic below if no CGM or Pump is configured for Loop:

![Loop HUD when both CGM and Pump have not been added](img/loop-3-hud-add-cgm-add-pump.svg){width="350"}
{align="center"}

!!! question "Switching Pumps?"
    If you already have a pump connected to Loop and want to switch to a different pump, go to [Modify Pump](#modify-pump).

Loopers can choose from 3 pumps and a simulator:

* Minimed 500/700 Series
* Omnipod
* Omnipod DASH
* Insulin Pump Simulator

!!! info "Omnipod vs Omnipod DASH"
    Insulet uses the term Omnipod to refer to the older (Eros) pods.

    Insulet uses the term Omnipod DASH to refer to newer BLE DASH pods.

    The Loop app and documentation follow this convention:

    * **Omnipod**: refers to the older (Eros) pods
    * **Omnipod DASH**: refers to the new BLE pods
    * **Omnipod Common**: refers to information that is common to both types of pods


## Add Pump

The graphic below shows the display when a user taps on Add Pump in the Settings screen. Tap on the desired Pump to advance to the next screen.

![graphic showing the pumps available with Loop 3](img/loop-3-setting-add-pump.svg){width="500"}
{align="center"}


If you are adding a Medronic pump, skip ahead to [Medtronic](#medtronic)

## Omnipod Common

### Pod Nofication Defaults

The graphics below show the common screens for adding Omnipod or Omnipod DASH. These are the default notifications used for all future pods. These default settings can be modified later.

![initial screens for pod set up to define default notifications](img/loop-3-pod-setup.svg){width="450"}
{align="center"}

After these screens are completed, the insulin type is selected.

### Insulin Selection

The insulin selection screen is presented for all pumps.

* Insulin Type
    * User can select from Rapid (Novolog, Humalog, Apidra) or Ultra-Rapid (Fiasp, Lyumjev)

![initial selection for insulin used in pump](img/loop-3-pump-insulin.svg){width="450"}
{align="center"}

After this screen is presented, [Omnipod DASH](#omnipod-common_1) users should skip ahead - they will not use a RileyLink compatible device.

## Omnipod

### Select RileyLink

For Omnipod and Medtronic pumps, a RileyLink compatible device is required for Loop to control your pump. You will learn to make it a habit to keep that device and your phone within range of your pump to keep Loop a nice green color.

!!! warning ""
    New RileyLink compatible devices won't have a name listed next to their slider at first. The name will only be displayed after connecting the device to Loop for the first time. So, if all you see in the device list is a little toggle and no "RileyLink" name...go ahead and switch that toggle. The default device name will appear after that toggle is green.

    You can later [personalize](../operation/loop-settings/rileylink.md) the default device name once it is connected to Loop.

![img/pod-rl.png](../operation/loop-settings/img/pod-rl.png){width="400"}
{align="center"}

A list of all RileyLink compatible devices in the nearby area will display in the RileyLink Setup screen. Select your RileyLink by sliding the toggle to display green and then press the blue `Continue` button at the bottom of the screen. 

If your device does not appear:

* Make sure it is charged and turned on
* Make sure it is not still connected to a different phone or app

## Omnipod Common

After the detour for selecting a RileyLink for Omnipod, all other actions for Omnipod and Omnipod DASH are the same. Once a pod is paired, the Pump display will be the same, except the Omnipod screen has a section for the RileyLink Devices.

### Pod Pairing

A [video is found here for pairing an Omnipod DASH pod](https://drive.google.com/file/d/1mN5s8-oorvoa-gbjAaYbnUnl_-vvuhNC/view?usp=sharing). Once the pod starts priming, you may want to skip ahead in the video (priming takes a minute to complete). The Omnipod Common pairing protocol is the same. The difference is that Omnipod requires a RileyLink compatible device and Omnipod DASH does not. There are also slight differences in some of the text, e.g., Omnipod DASH uses a blue needle cap and Omnipod has a clear needle cap.

## Medtronic

When adding Medtronic, the documentation is not consolidated yet so follow links and use your back button to return to this list.

1. Select Minimed 500/700 Series as your pump
1. Select [Insulin Type](#insulin-selection)
1. Follow links to 2 sections in the Loop 2.2.x Documentation
    * [Prepare Medtronic Pump](../operation/loop-settings/mdt-pump.md#prepare-medtronic-pump)
    * Skip the Add Pump Step - you've already done that
    * [Connect Pump to Loop](../operation/loop-settings/mdt-pump.md#connect-pump-to-loop) section.


## Modify Pump

You must first delete the old pump before you can switch to a new pump.

* If you are using Omnipod or Omnipod DASH, you must first deactivate your current pod

    * After the pod has been deactivated, a new row will show at the bottom of the pod screen
    * Tap on `Switch to other insulin delivery device` and follow the directions to complete the task

* If you are using Medtronic, scroll to the bottom of the pump screen and select `Switch to other insulin delivery device`

The HUD will now show the add pump icon and you can [select a new pump](#add-pump).
