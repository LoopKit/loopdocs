# RileyLink FAQs

## What is the RileyLink? Do I have to have one?

!!! danger "RileyLink vs radio-link"
    - The RileyLink is the original design for the required radio-link
    - The headers (anchor links) on this page still use RileyLink, but there are multiple options


Yes, a radio-link is a required part of Loop. The radio-link is a little device that helps your iPhone and pump/pod speak to each other. The radio-link is a critical part of the Loop system because the pump needs communications via radio-frequency, and the iPhone needs communications via Bluetooth. The radio-link is like a translator that can speak both formats so that the pump and iPhone can loop together. The radio-link communicates information to/from your pump by radio communications, and to/from your iPhone using Bluetooth.

## Where can I buy a RileyLink?

Purchase information for radio-links is on [Build Step 5](../build/step5.md#radio-link-options)

## Do I have to carry the RileyLink everywhere?

The short answer is yes. If you want your Loop to keep automatically adjusting insulin dosing and issuing commands to your pump, you will need the radio-link so that these communications can happen. Put it in a purse, pocket, SPIbelt. Clip it to a backpack, belt, or bra...but please do bring it with you.

## What are some ideas for carrying the RileyLink?

There is now a topics section on The Looped Facebook group. (Right hand side when you're in the discussion location).

[Link to Topics: Cases Riley Ema Orange](https://www.facebook.com/groups/1782449781971680/post_tags/?post_tag_id=2516136941936290)

You can also use the search feature on the general discussion page of The Looped Facebook group if you already have a case and want more ideas, e.g., "How to carry rileylink".

## How far away can the RileyLink be?

That answer will depend. The environment matters and some radio-links have greater range than listed here. Generally speaking, RileyLink is solid about 10-12 feet away in most environments. In some situations, you could have RileyLink work fine even at 20+feet away. Other times, you may need to get RileyLink closer.

What influences this distance? The biggest influences are (1) body-blocking and (2) "noisy" environments. The human body is a lot of water, and water is an excellent blocker of wireless communication.  So, sleeping on a pod and smothering it entirely with your body will possibly decrease the ability of radio-link to communicate with the pod. Environments with a high concentration of wireless signals can also interfere with radio-link communications and make closer proximity a benefit. Where might those kinds of situations happen? Concerts, conferences, and sporting arenas are pretty prone to interference.

## What happens if I walk away from my RileyLink?

While you are out of the communication range for your radio-link, any running temp basal will keep going until it finishes (the longest temp basal that Loop sets are for 30 minutes duration...so within 30 minutes or less your pump would go back to your regularly scheduled basal). When you come back into range of your radio-link, Loop will pick back up within 5-10 minutes without you needing to do anything.

## What are the differences between Medtronic and Omnipod RileyLinks?

There are two different types of RileyLinks currently; the difference being the antenna is optimized for the pump you are using. Otherwise they are identical. See [Build Step 5: Radio-link Options](../build/step5.md#radio-link-options) for other radio-links.  The OrangeLink has both antennas included in its design and can talk to Medtronic or Omnipod.  The EmaLink requires selection for type of pump.

!!! note ""
    The color of the circuit board is irrelevant.

![components for RileyLink: case, board, battery; Medtronic on left, Omnipod on right](img/two-rl.png){width="650"}
{align="center"}

## What will happen if your radio-link has the wrong antenna?

You can *technically* use that RileyLink with either pump on Loop. But, you will have significant frustrations with the short distances required between the pump/pod and RileyLink when using the "wrong" antenna. With mismatched antenna/pump, the RileyLink needs to be very close (think inches) and in clear line-of-sight to pump/pod. This makes everyday living (and sleeping) a bit hard. If you use the appropriate-antenna-for-your-pump RileyLink, the distances the pump/pod and RileyLink can tolerate from each other is much more "real world" friendly and stable.

In summary, definitely use the appropriate RileyLink with the antenna that matches your pump so that you are less frustrated. In a pinch, your old RileyLink might work as a backup, but you won't love it.

## Can you swap out the old antenna on a RileyLink?

Yes, the antenna swap is not a hard swap if you have basic soldering skills and tools. The old antenna can be removed easily by reheating the solder. New 433MHz antennas and a cap can be found on [GetRileyLink site](https://getrileylink.org/product/433diyupgrade/). Tips: use flux and clean the antenna stub before soldering. Poorly DIY-soldered antennas can lead to a decreased range and frequent communication drops between Loop and the pods. Be very sure that the wire on the antenna does NOT poke out the back side of the printed-circuit board where it could rub against and possibly puncture the battery casing.

One user found the antenna no longer securely soldered after a year of use (and perhaps being dropped).  The solder should be shiny and the antenna base should be firmly attached to the board.

## How long will my RileyLink go between charging?

RileyLinks can go about 30-36 hours on a single charge. There is no way to see the remaining charge level, so most people just get into the habit of charging overnight while they sleep. The actual time to fully recharge is about 1 or 2 hours; you'll know it is fully charged when the red light turns off. After a full charge, the red light will turn off and then periodically turn on for short times while it "tops off" while still on a charger.

## How long will my RileyLink battery last?

Eventually, lithium polymer (LiPo) batteries will lose charging capacity and you would want to replace if you notice the battery not lasting the full day. We've been using our current battery for nearly 2 years without issue.

## How can I tell how much charge my RileyLink has?

You can't. There is no charge level indicator. Just charge it nightly, and you won't have a problem. Full battery charge should last about 30-36 hours depending on battery health. Charging takes less than 2 hours.

## How should I carry the RileyLink? Does it make a difference?

In general, you want to get in the habit of carrying RileyLink with you, yes. A pocket, carabiner, lanyard, SPIbelt...the options are endless. What you don't want to do is put the RileyLink in a blocking bag that has RFID blocking (some travel fanny packs have that). The distance that your RileyLink can be away from your pump will depend heavily on the environment you are in. You may find it works best if you keep it on the same side of your body as your pump.

Both the EmaLink and OrangeLink have reported longer ranges, so they can be kept in a central location - but still need to be "near enough". And don't forget that your radio-link is in that central location and leave the area without it.

## Is RileyLink waterproof?

Nope. Nor is it sweat-proof. Be careful. There are waterproof cases.  See [RileyLink cases](https://www.loopcases.com/), or search on facebook.

## What is the most common issue for RileyLink?

People not pushing the LiPo battery in all the way when they first assemble their RileyLink. It takes quite a bit of push to get the plug inserted far enough. If not secured well, Loop will have more frequent problems. See [Bad-Good photos](../build/step5.md#assemble-rileylink) of the battery connection. A loose battery connection was also reported after normal use over several years.

## When should I power cycle my RileyLink?

The simple answer is - try this if you are having persistent red loops associated with pump communication that are not resolved by toggling phone Bluetooth off then on again. You might need to do this, even if the firmware (next paragraph) is correct.

In Loop settings, tap on your pump, find your device (RileyLink or other) and tap on that menu.  The firmware displayed should match or be a higher version number than what is shown in the figure below, e.g., `subg_rfspy 2.2/ble_rfspy 2.0`. (If you are running with a very old RileyLink from pre-Aug 2018, it might be a lower number. Check it when RL is working well and make a note of what it says.) If not, you should power cycle your RileyLink. Make sure, after power cycling, that the correct firmware is displayed. If several power cycles do not help, contact [GetRileyLink](https://getrileylink.org/contact) for assistance.<br/><br/>

![Expected firmware display under device menu for post-Aug 2018 RileyLink](img/rl-firmware.jpg){width="350"}
{align="center"}

## Can I use more than one RileyLink at a time? Will it improve anything?

Yes, you can have two turned on, but it won't help anything really. Loop only uses one radio-link at a time. If you have several radio-link turned on in Loop settings, your Loop will only look for another radio-link after Loop fails for over 15 minutes on the original radio-link. In my experience, it is rare that Loop would fail for more than 15 minutes and a second radio-link would help in the same environment. If one radio-link gets damaged though and you need to swap out to a second radio-link, there are no issues with that.

## Can I run Loop without a RileyLink?

No, currently DIY Loop only works with certain insulin pumps, all of which require use of a radio-link.
