# RileyLink Compatible Device FAQs

## What is the RileyLink compatible device? Do I have to have one?

The RileyLink compatible device is a required part of Loop. It is a small device that helps your iPhone and pump/pod speak to each other. The Loop compatible pumps communicate via radio-frequency and the iPhone communicates via Bluetooth. The device is like a translator that can speak both formats so that the pump and iPhone can loop together. The device uses the RileyLink protocol to communicate information to/from your pump by radio communications, and to/from your iPhone using Bluetooth.

Purchase information for these devices is found in [Build Step 5: RileyLink Compatible Devices](../build/step5.md#rileylink-compatible-devices)

## Do I have to carry the RileyLink compatible device everywhere?

If you want your Loop to keep automatically adjusting insulin dosing and issuing commands to your pump, you will need the device so that these communications can happen. Put it in a purse, pocket, SPIbelt. Clip it to a backpack, belt, or bra...but please do bring it with you.

There is now a topics section on The Looped Facebook group. (Right hand side when you're in the discussion location).

[Link to Topics: Cases Riley Ema Orange](https://www.facebook.com/groups/1782449781971680/post_tags/?post_tag_id=2516136941936290)

You can also use the search feature on the general discussion page of The Looped Facebook group if you already have a case and want more ideas, e.g., "How to carry rileylink".

### How far away can the RileyLink compatible device be?

Please review [RileyLink Compatible Device Range](../build/step5.md#rileylink-compatible-device-range)

## What happens if I walk away from my RileyLink compatible device?

While you are out of the communication range for your device, any running temp basal will keep going until it finishes (the longest temp basal that Loop sets are for 30 minutes duration...so within 30 minutes or less your pump would go back to your regularly scheduled basal). When you come back into range of your device, Loop will pick back up within 5-10 minutes without you needing to do anything.


## Is the RileyLink compatible device waterproof?

Nope. Nor is it sweat-proof. Be careful. There are waterproof cases.

## When should I power cycle my RileyLink compatible device?

This is one of the first things to try if you have a Red Loop saying Pump Data Too Old. Many people prefer toggling phone Bluetooth off then on again, first, but if that doesn't work, try a power cycle on the device.

## Can I use more than one RileyLink compatible device at a time? Will it improve anything?

Yes, you can have two turned on. Loop only uses one device at a time. If you have several devices turned on in Loop settings, your Loop will only look for another device after Loop fails for over 15 minutes on the original device. It is rare that Loop would fail for more than 15 minutes and a second device would help in the same environment. However, if one device is in the bedroom and another in the kitchen, it will switch for you. If one device gets damaged and you need to swap out to a second device; there are no issues with that.

## How can I find the firmware versions for my RileyLink compatible device?

In Loop settings, tap on your pump, find your device (RileyLink or other) and tap on that menu. The figure below shows firmware specific to the RileyLink. If you have another type of device, the firmware value reported will be different.

![Expected firmware display under device menu for post-Aug 2018 RileyLink](img/rl-firmware.jpg){width="350"}
{align="center"}

With RileyLink, the firmware displayed should match or be a higher version number than what is shown in the figure above, e.g., `subg_rfspy 2.2/ble_rfspy 2.0`. (If you are running with a very old RileyLink from pre-Aug 2018, it might be a lower number.) Check it when the device is working well and make a note of what it says. If you're having Red Loops, you might want to check firmware and connected state. Make sure, after power cycling your device, that the correct firmware is displayed. If several power cycles do not help, contact the manufacturer for assistance.


## RileyLink Questions

### What are the differences between the RileyLink Medtronic and Omnipod Antennas?

There are two types of antennas for RileyLinks; each antenna is optimized for the pump you are using. Otherwise they are identical. See [Build Step 5: RileyLink Compatible Devices](../build/step5.md#rileylink-compatible-devices) for other devices.  The OrangeLink has both antennas included in its design and can talk to either Medtronic or Omnipod.  The EmaLink requires selection for type of pump.

!!! note ""
    The color of the RileyLink circuit board in the photos below is irrelevant.

![components for RileyLink: case, board, battery; Medtronic on left, Omnipod on right](img/two-rl.png){width="650"}
{align="center"}

### What will happen if your RileyLink has the wrong antenna?

You can *technically* use that RileyLink with either pump on Loop. But, you will have significant frustrations and probably a lot of red loops. With mismatched antenna/pump, the device needs to be very close (think inches) and in clear line-of-sight to pump/pod. This makes everyday living (and sleeping) a bit hard. If you use the appropriate-antenna-for-your-pump device, the distances the pump/pod and RileyLink can tolerate from each other is much more "real world" friendly and stable. The OrangeLink contains both antennas so will work with either pump. This may be a good choice if you like to switch between Medtronic and Omnipod.

In a pinch, if you have a RileyLink that you used with a Medtronic pump and have switched to Omnipod, it might work as a backup, but you won't love it.

### Can you swap out the old antenna on a RileyLink?

Yes, the antenna swap is not a hard swap if you have basic soldering skills and tools. The old antenna can be removed easily by reheating the solder. New 433MHz antennas and a cap can be found on the [GetRileyLink site](https://getrileylink.org/product/433diyupgrade/).

Tips: use flux and clean the antenna stub before soldering. Poorly DIY-soldered antennas can lead to a decreased range and frequent communication drops between Loop and the pods. Be very sure that the wire on the antenna does NOT poke out the back side of the printed-circuit board where it could rub against and possibly puncture the battery casing.

After a year of use (and a year of being dropped), the antenna may no longer securely soldered. The solder should be shiny and the antenna base should be firmly attached to the board.

### How long will my RileyLink go between charging?

RileyLinks can go about 30-36 hours on a single charge. There is no way to see the remaining charge level, so most people just get into the habit of charging overnight while they sleep. The actual time to fully recharge is about 1 or 2 hours; you'll know it is fully charged when the red light turns off. After a full charge, the red light will turn off and then periodically turn on for short times while it "tops off" while still on a charger.

### How can I tell how much charge my RileyLink has?

You can't. There is no charge level indicator. Just charge it nightly, and you won't have a problem. Full battery charge should last about 30-36 hours depending on battery health. Charging takes less than 2 hours.

### How long will my RileyLink battery last?

Eventually, Lithium-ion Polymer (LiPo) batteries will lose charging capacity. You would want to replace if you notice the battery not lasting the full day. Many people report using their battery for more than 2 years without issue.

Be aware that if a battery is failing, it may swell. If you notice that the RileyLink battery is swollen, remove the swollen battery from your home and place in a fire-safe area and recycle it properly.  Either order a new battery or pull out your spare.
