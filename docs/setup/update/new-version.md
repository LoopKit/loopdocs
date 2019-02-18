# Loop v1.9.4 Features

As always, there is a [GitHub page](https://github.com/LoopKit/Loop/releases/tag/v1.9.4) with release notes about the features and changes since the previous Loop release.  This page provides a bit more in-depth information and practical tips about the new release. 

## Apple Watch Loop App BG Chart

Loop v1.9.4 brings a BG chart to your Apple Watch's Loop app. If you swipe right-to-left on the Apple Watch's Loop app screen, you will see the new BG chart. Scrolling on the crown in that view will also show information about IOB and COB. 

## Apple Watch Series 4 Complications

Seris 4 watches brought a new set of available complications. Loop v1.9.4 allows for the use of this new complication.

## Siri Shortcut: Add Carbs

You can now use a shortcut phrase, that you'll setup with Siri, to open the "Add Carbs" screen of your Loop app.

Assuming you have Siri enabled, you'll navigate to your iPhone Settings, Siri & Search, Shortcuts, and then record the shortcut phrase you'd like to use to for Siri to open the "add carbs" screen in Loop.

<p align="center">
<img src="../img/siri.PNG" width="850">
</p>

## Bug Fix: Future BG data for G6 users

An intermittent bug was encountered when G6 users would have automatic backfill of missing CGM data.  The bug would record future, errant BG data into Health and therefore Loop would turn red and Looping would stop.

You can read about that bug [here](https://github.com/LoopKit/Loop/issues/834), but if you are experiencing this bug, please update to Loop v1.9.4 to permanently resolve the issue.

## Bug Fix: Missing Glucose data, but Dexcom is working

Users would sometimes see a "Missing data: Glucose data not available" although the Dexcom app showed no gaps and appeared to be otherwise functioning. The issue is discussed [here](https://github.com/LoopKit/Loop/issues/837) but please update your Loop app to avoid/fix this bug.

## Bug Fixes: Missing bolus and insulin data gap

Also bug fixes for these two issues [here](https://github.com/LoopKit/Loop/issues/853) and [here](https://github.com/LoopKit/Loop/issues/852)

In the first bug, the issue happens on x22 medtronic pumps when 1) A (large) bolus is started. 2) A temp basal ends before the bolus finishes. 3) Loop fetches pump history as part of a normal loop before the bolus finishes. Please update to address this bug.

In the second bug, there are small time gaps that were evident in Health data. The identification of this bug was aided by Tidepool Mobile uploading of Health data. This fixes those gaps.

## Added pink color selection for Medtronic pumps

Minor update to include the pink color available for Medtronic pumps.

## CGM source screen updated

The selection of your CGM source in Loop Settings has been updated. The screen will look a little different than you are used to, however will function the same as always.  When a Medtronic pump has been added to Loop settings, a corresponding compatible Medtronic CGM selection will be also be available, in addition to the standard Dexcom selections.

## Known common issues remaining

Because I know you will ask:

* The uploading of meterBG checks to NS using pump-linked Contour Next meters is temporarily not working.  There is an open ticket to get this restored.  We miss our red dots, too.  

* Some x15 pumps will get erroneous "Bolus may not have succeeded.  Pump responded unexpectedly.  Check your pump before retrying" notifications .  This is a known issue, even since before the release of v1.9, discussed [here](https://github.com/LoopKit/Loop/issues/587).  You can read the thread and implement the suggested solution until one has been merged into a Loop release.
