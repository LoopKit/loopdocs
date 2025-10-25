## Order a RileyLink Compatible Device

**Not needed for any pump that supports direct Bluetooth BLE commands such as Dana, DASH and Medtrum**

**Required when using an older Medtronic pump or Omnipod Eros pods**

!!! info "Time Estimate"
    - 0 minutes if you plan to use a pump that supports direct BLE communication - you don't need one
    - 15-20 minutes to read about RileyLink compatible devices
    - 15 minutes to order a device

!!! abstract "Summary"
    - Decide what kind of RileyLink compatible device to buy
    - Order your compatible device

!!! question "FAQs"
    - **What is a RileyLink Compatible Device?** RileyLink refers to both the communication protocol and the name of the original device. Other DIY Loopers have created [RileyLink Compatible Devices](rileylink.md#rileylink-compatible-devices) that use the RileyLink protocol. All these devices can be used interchangeably with the *Loop* app to support Eros and Medtronic use.
    - **Do I have to buy one?** These are open-source hardware devices, but it takes special skills to build them yourself. It is recommended you buy one (or two) if you require it. At the current time, new OrangeLink and EmaLink devices are available for purchase. There are many used devices available in the community now that many users have switched to DASH. **Not needed for DASH or Dana pumps**
        * Facebook Group where you may find used items: [Looping in a time of covid](https://www.facebook.com/groups/1087611668259945/)
    - **"What happens if I lose my RileyLink compatible device or walk away from it?"** Within a half hour, your pump returns to the normal scheduled basal rate
    - **"Can I swap out RileyLink compatible devices at any time?"** Yes, you can. You do not need to start a new pod or rebuild the *Loop* app. Tap on the pump menu in settings to search for new devices. You can swap between compatible devices.
    - **"How close does the RileyLink compatible device need to be to me? Do I have to carry it with me?"** See [RileyLink Compatible Device Range](../faqs/rileylink-faqs.md#range){: target="_blank" }.


## What is a RileyLink Compatible Device

The RileyLink compatible device is required to allow your phone to talk to compatible *Medtronic* and *Omnipod Eros* pumps. **It is not needed for *Omnipod DASH* or Sooil Dana pumps.**

!!! abstract "Details for RileyLink"
    The RileyLink compatible device is an open-source hardware device that can bridge Bluetooth Low Energy (BLE) to the radio-frequency wireless communication used by compatible *Medtronic* and *Omnipod Eros* pumps.

Loop 3 has *Omnipod DASH* support, among other new features. When using *Omnipod DASH*, the RileyLink compatible device is not necessary.  If you are using *Medtronic* or *Omnipod Eros* (not DASH), you still need the device regardless of which version of Loop you are running.

*Medtronic* and *Omnipod Eros* pumps require a RileyLink compatible device.

![Omnipod Eros or Medtronic pump communicating through RileyLink to phone running Loop app](img/rileylink-comm-pod-mmt.svg){width="600"}


## RileyLink Compatible Devices

The RileyLink protocol defines a specific Bluetooth interface and way of opening a Sub-GHz radio channel to pumps. All RileyLink compatible devices follow the RileyLink protocol.

> Many Omnipod users have switched to DASH and no longer need a RileyLink device, so the demand is significantly less than it used to be. You can still buy the devices, but there are fewer options.

There used to be just one option, the original RileyLink. Now there are more options, so you have to make a decision. Depending on your choice, be sure to have the correct charger and cables or batteries handy and add spare compatible supplies to your diabetes go-bag.

- A [Comparison Chart](https://getrileylink.org/rileylink-compatible-hardware-comparison-chart?fbclid=IwAR2vHbOzla-zmM-cSp4NkOB_23k3spgnaYvCIGRcACcIQ25FJAU_7HRkH2A) is provided by the GetRileyLink organization for all the RileyLink compatible devices listed below
- RileyLink
    - Designed by Pete Schwamb
    - Rechargeable battery (max 36 hours per charge)
    - No longer available new, check this Facebook Group for used ones:
        * [Looping in a time of covid](https://www.facebook.com/groups/1087611668259945/)
- OrangeLink
    - Designed by Vic Wu, available from [GetRileyLink](https://getrileylink.org)
    - Uses 2 AAA batteries, batteries typically last weeks or more, depending on the batteries/pump type
    - Works with either Omnipod or Medtronic
    - Uses new chipsets, reported to have a longer range
    - Matches Apple AirPod form factor, so you can use AirPod cases
- EmaLink
    - Designed by Sorin Kupas-Spunei to increase range, offer smaller sizes
    - Rechargeable battery (various case/battery sizes available)
        - Micro/Nano: 2 to 3 days
        - Standard: 6 to 7 days
        - Maxx: 12 to 14 days
    - Must order either Omnipod or Medtronic version
    - This [EmaLink Information](https://github.com/sks01/EmaLink#emalink) includes photos of various EmaLink configurations as well as photos showing relative sizes of EmaLink, OrangeLink and RileyLink
    - In North America, available from [EmaLink.us](https://www.emalink.us)

## More information

There is an entire FAQs page on [RileyLink Compatible Devices](../faqs/rileylink-faqs.md){: target="_blank" }.

Sections of interest include:

* [Firmware Update](../faqs/rileylink-faqs.md#orangelink-firmware) information on the OrangeLink

## Waiting for your RileyLink Compatible Device

While you are waiting for the RileyLink compatible device to arrive, you can proceed with these build directions and can try one of the [Simulated Loop](../version/simulator.md){: target="_blank" } options. After that, unless you are using *Omnipod DASH* or Sooil Dana, you'll have to wait for your device.

The population of DIY loopers (Loop and Android APS) has grown enough that you might be able to find someone local to loan you their spare.

## Next Step: Enroll in Apple Developer Program

Now you are ready to enroll in the [Apple Developer Program](apple-developer.md).
