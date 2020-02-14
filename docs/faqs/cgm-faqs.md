# CGM FAQs

## What CGMs does Loop work with?

Loop works Dexcom G4 with share, G5, G6, Share and the Medtronic CGM systems compatible with Looping pumps.

Read the details [here](https://loopkit.github.io/loopdocs/build/step4/).

## Do I need wait for a new sensor session to start Loop?

No, you can start Looping mid-sensor session. There's no need to do anything special with regards to your CGM session when starting or ending Loop use.

## What do I do when sensor is in warm-up?

While the CGM is in warm-up, Loop will return to your scheduled basal delivery (within 30 min or less). You won't get temp basal adjustments during the warm-up period. If you need to bolus during this time, you will need to do a finger check and enter the blood glucose value into Apple Health app manually if you'd like Loop to offer a bolus recommendation. Loop will read that value from the Health app to provide you a bolus recommendation. If you are really ambitious, some people do frequent (15 min or so) finger checks and enter those into Health during warmup. This could allow Loop to do a bit of looping during warmup, albeit on blood glucose values that are spread pretty far apart compared to normal.

## What do I do when I switch transmitters?

When you change transmitters, you will need to update the transmitter ID in your Loop settings. This is pretty simple task. 

When you change transmitters, select the `Delete CGM` button at the very bottom of the CGM info page in Loop. Then you will select your Dexcom system again and add the new transmitter ID. You cannot just tap on your old transmitter ID to update it.

<p align="center">
<img src="../img/delete-cgm.jpg" width="400">
</p>

If you don't update your transmitter ID when you change active transmitters, your Loop will be forced to go to your Dexcom Share server to get your CGM data and will not work without cell or wifi connection. When Loop is using data from Dexcom Share servers, a small cloud will appear above the BG reading in Loop and should tip you off that maybe you forgot to update your transmitter ID.

## Can I use Libre sensors with a reader like Miao Miao?

If you want to use a Libre sensor you will need to modify Loop to accomplish that use. Loop code does not natively support that sensor, nor readers.

## Can I use Eversense?

Nope. Eversense does not write to Apple Health nor has the BT communications protocol been reverse engineered the way it has been done with Dexcom.  

## Can Loop read CGM data from Nightscout?

Loop does not read CGM data from Nightscout. You would need to use a solution such as NightscoutShareServer and make changes to Loop code in order to do that. Please search the Looped group on Facebook for posts regarding that option, as it is not a part of standard Loop use and is a community-based modification. You will need to do your homework and research to make that happen. At this time, there is not an active version of a modified Loop that appears to support this option easily.

## Can Spike or Xdrip be used with Loop?

Spike and Xdrip are not supported by Loop. You will need to implement community-based modifications to Loop in order to use those apps with Loop. Helpful tip: Use `spike loop` as a search term in Looped group for additional info about community-modified Loop versions for Spike. Links to those modified Loop versions are not provided in these LoopDocs because we (the LoopDocs maintainers and Loop developers) do not actively watch those versions to ensure they are up-to-date.


