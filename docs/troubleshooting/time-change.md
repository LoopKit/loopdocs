## Time Zones, Daylight Savings Time, Summer Time

Loop operates across time zones and time changes. The phone that is running Loop will automatically update the time, but you choose when to modify the time zone for "pump time".

What Therapy Settings are set by "pump time"?

* Basal Rate Schedule
* CR and ISF Schedule
* Correction Range Schedule

Time Change comments:

* The Pump Settings screen is used to modify time zones
    * Tap on Pump Status Icon from the HUD
    * or Loop->Settings->Pump
* Travel
    * There is no urgency to update the pump time to match the wall-clocks when traveling
    * For short trips, many Loopers just leave the pump time alone
* Time Change (Daylight Savings Time or Summer Time)
    * Most people want to update their pump time immediately after the clocks change
* With Loop 3 there is a Clock Icon added to the HUD Pump Status display

If you want more information, click on this link: [Time Zone](../loop-3/displays_v3.md#time-zone), which provides detail and connects to the Loop 2.2.x or the Loop 3 version sections.

!!! warning "Medtronic Users"

    **Do not use the Medtronic pump menus to change your pump's time when Looping.**


## iPhone

Loop will warn you if your phone does not have time configured to automatically update. The configuration is under iOS Settings -> General -> Time & Date.

**Do not** ever adjust the time manually on your Looping phone to "defeat" time-based rules for a game. Your phone with Loop is now a critical medical device - make sure anyone who uses your phone understands this.

## Minimed Pump and CGM

The Minimed pump doesn't expose a universal clock, instead it exposes the components of a date (YMDHIS). It has no concept of political time zones, and just continues to increment its components on schedule. Therefore, Loop assumes that the pump's date, until changed, remains at a fixed offset from UTC.

That offset is stored by Loop the first time the pump ID is changed, and every time the pump's time is changed using the "Change Time Zone" command.

## Dexcom CGM

No particular input is needed on your part for Loop to work with Dexcom CGM data. All times are UTC.  However for Dexcom receiver users, at time changes you may want to manually change your receiver's time setting just so the time visually appears correct when you are viewing the screen.

## Airports

RileyLinks have no problem going through any of the airport security systems. You can carry it with you in the airplane cabin and it can go through the x-ray scanner that your carry-on bags go through.

## Airplane Mode

Nothing wrong with airplane mode, but many people forget about it at the time they travel. So, you can do this simple preparation step now:

Turn airplane mode on. Then make sure your Bluetooth is still slid “on”. If Bluetooth isn’t on, then go slide it on again. Now go ahead and turn airplane mode off again.

Why did we just do that? Because in older versions of iOS, airplane mode turned off the first time you ever use it.

But, if you remember to turn Bluetooth back on while in airplane mode, two things happen (1) Dexcom and Loop will work while in airplane and (2) airplane mode will “remember” the next time that you like Bluetooth left on in airplane mode and will not turn it off the next time you slide airplane mode on. So now you’ve just prevented yourself from forgetting to turn Bluetooth on the next time you fly and are in a hurry to meet your lovely seat mate and stow your luggage. You can safely follow cabin instructions and put phone in airplane mode without losing Loop or Dexcom.

