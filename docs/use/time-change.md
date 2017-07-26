# Time Changes with Loop

Loop is built to fully work across time zone and daylight savings time changes as long as a few basic instructions are followed.

## iPhone
Loop will assume your iPhone's time (UTC, not time zone) is always correct. This theoretically may not be the case if a nearby cell tower is improperly configured (though there are likely resilience mechanisms in iOS to handle this). Automatic time setting can always be disabled in Settings.

## Minimed Pump and CGM
The Minimed pump doesn't expose a universal clock, instead it exposes the components of a date (YMDHIS). It has no concept of political time zones, and just continues to increment its components on schedule. Therefore, Loop assumes that the pump's date, until changed, remains at a fixed offset from UTC.

That offset is stored by Loop the first time the pump ID is changed, and every time the pump's time is changed from the RileyLink Settings screen.

!!! warning ""
    Do not change the pump's time directly on the pump. Instead, always use Loop's RileyLink "Change Pump Time".

<p align="center">
<img src="../img/change_time.png" width="400">
</p> 


## Dexcom CGM
No particular input is needed on your part for Loop to work with Dexcom CGM data. All times are UTC.  However, at time changes you may want to manually change your G4 receiver time setting just so the time visually appears correct when you are viewing the screen.

## Traveling across time zones and daylight savings
When traveling, there is no urgency to update the pump's time to match the wall-clocks in your geography. Configuration schedules—basal rates, target ranges, carb ratios, and insulin sensitivities—will all remain in the pump's time zone. The app's graphs and status will always display in the time zone of the iPhone, and Loop will understand the difference in offset between the two, highlighting it when attempting to change configuration schedules.

When you're ready to update the pump's time, simply use the Loop's RileyLink "Change Pump Time". This will also shift your configuration schedules to the current time zone.
