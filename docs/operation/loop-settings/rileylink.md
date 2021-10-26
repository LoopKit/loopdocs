# RileyLink

The RileyLink (or compatible device) screen is accessed by clicking on the image of your connected pump in Loop settings or the Reservoir (Medtronic) or Pod Age (Omnipod) in the Heads Up Display to bring up the associated pump screen. From that screen, scroll down to the section labeled `DEVICES` to view the list of connected RileyLink compatible device(s). Tapping on a name with a green slider by it takes you to the RileyLink screen for that device.

!!! danger "Helpful Tip - Personalize Your Device"
    As soon as you connect the device initially - it is strongly encouraged that you rename it from the default name for that device, e.g., RileyLink or OrangeLink or EmaLink. Tap on the device as directed above, then tap on the Name line and enter your desired name. The new name may need to sit for a few seconds before exiting back out of the naming screen for it to be transferred and saved in the device. The device must be connected and on to change its name.

The name at the top center is whatever you named your RileyLink compatible device. With recent Loop updates, the RileyLink screen is the same regardless of the pump you are using.

!!! info "Patch Required"

    Some devices have features not available with other devices.  With Loop 2.2.6 some features were added to the OrangeLink, but there is a mismatch of reported hardware for some versions of OrangeLink firmware which prevents the Find Device row from showing up for OL Pro. The EmaLink extra features did not make it into the Loop v2.2.6 release.

    * To see the displays shown in the graphics below, please follow instructions in the [EmaLink and OrangeLink Feature and Patch sections](../../faqs/rileylink-faqs.md#emalink-and-orangelink-features).


The [firmware](../../faqs/rileylink-faqs.md#firmware-version) displayed is specific to each device. The three graphics were taken from Loop master after the patch was applied.


![example rileylink screens for riley, ema, orange after patch](img/rl-comp-v225-patched.svg){width="600"}
{align="center"}

## Device

The lines under the Device section provide information on the device. The two most important lines are the Connection Status and Signal Strength.

* The Connections Status should say `connected` if the device is connected to the iPhone's Bluetooth. If the status says `connecting` or `disconnected` then you should toggle the iPhone's BT and/or power cycle the device to help reconnect.

* The Signal Strength is the strength of the Bluetooth signal between the iPhone and the device.  It is **not** the signal strength of the radio communications with the pump/pod.  This is reported as a negative number so a -50&nbsp;dB signal is stronger than -80&nbsp;dB. As you move the device and iPhone closer/farther apart, you will be able to see the signal strength change. In a pinch, this can be used to help locate a lost device in the house or at the park after dark.

![img/RL_bt.jpg](img/RL_bt.jpg){width="350"}
{align="center"}
