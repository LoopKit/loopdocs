# Travel and Timezones

## Airports

RileyLinks have no problem going through any of the airport security systems. You can carry it with you in the airplane cabin and it can go through the xray scanner that your carry-on bags go through.

## Airplane Mode

Nothing wrong with airplane mode, but many people forget about it at the time they travel. So, you can do this simple preparation step now:

Turn airplane mode on. Then make sure your Bluetooth is still slid “on”. If Bluetooth isn’t on, then go slide it on again. Now go ahead and turn airplane mode off again.

Why did we just do that? Because airplane mode by default turns Bluetooth off for the first time you ever use it.

But, if you remember to turn Bluetooth back on while in airplane mode, two things happen (1) Dexcom and Loop will work while in airplane and (2) airplane mode will “remember” the next time that you like Bluetooth left on in airplane mode and will not turn it off the next time you slide airplane mode on. So now you’ve just prevented yourself from forgetting to turn Bluetooth on the next time you fly and are in a hurry to meet your lovely seat mate and stow your luggage. You can safely follow cabin instructions and put phone in airplane mode without losing loop or dexcom.


## Changing Timezones and Daylight Savings Time

Loop is built to operate fully across time zone and daylight savings time changes. When traveling, there is no urgency to update the pump's time to match the wall-clocks in your geography. Configuration schedules—basal rates, target ranges, carb ratios, and insulin sensitivities—will all remain in the pump's time zone. The app's graphs and status will always display in the time zone of the iPhone, and Loop will understand the difference in offset between the two, highlighting it when attempting to change configuration schedules.

When you're ready to update the pump's time, simply <u>**use the Loop's "Change Time" command** </u>. This will also shift your configuration schedules to the current time zone.

!!!danger "Medtronic Users Only"
    **Always use RileyLink to change pump time instead of the Medtronic Pump's screen.  If you fail to set the pump time by using the RileyLink, Loop will not function properly.**
    <p align="center">
    <img src="../img/time_change.png" width="400">
    </p>

## iPhone
Loop will assume your iPhone's time (UTC, not timezone) is always correct. This theoretically may not be the case if a nearby cell tower is improperly configured (though there are likely resilience mechanisms in iOS to handle this). Automatic time setting can always be disabled in Settings.

## Minimed Pump and CGM
The Minimed pump doesn't expose a universal clock, instead it exposes the components of a date (YMDHIS). It has no concept of political time zones, and just continues to increment its components on schedule. Therefore, Loop assumes that the pump's date, until changed, remains at a fixed offset from UTC.

That offset is stored by Loop the first time the pump ID is changed, and every time the pump's time is changed using the "Change Time Zone" command.


## Dexcom CGM
No particular input is needed on your part for Loop to work with Dexcom CGM data. All times are UTC.  However for Dexcom receiver users, at time changes you may want to manually change your receiver's time setting just so the time visually appears correct when you are viewing the screen.

