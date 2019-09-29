# CGM FAQs

## What CGMs does Loop work with?

Loop works Dexcom G4 with share, G5, G6, Share and the Medtronic CGM systems
compatible with Looping pumps.

Read the details [here](https://loopkit.github.io/loopdocs/build/step4/).

## Can I use Libre sensors with a reader like Miao Miao?

If you want to use a Libre sensor you will need to modify Loop to accomplish
that use. Loop code does not natively support that sensor, nor readers.

## Can I use Eversense?

Nope. Eversense does not write to Apple Health nor has the BT communications
protocol been reverse engineered the way it has been done with Dexcom.

## Can Loop read CGM data from Nightscout?

Loop does not read from, nor upload to, CGM data for Nightscout. You would need
to use a solution such as NightscoutShareServer and make changes to Loop code in
order to do that. Please search the Looped group on Facebook for posts regarding
that option, as it is not a part of standard Loop use and is a community-based
modification. You will need to do your homework and research to make that
happen. At this time, there is not an active version of a modified Loop that
appears to support this option easily.

## Can Spike or Xdrip be used with Loop?

Spike and Xdrip are not supported by Loop. You will need to implement
community-based modifications to Loop in order to use those apps with Loop.
Helpful tip: Use `spike loop` as a search term in Looped group for additional
info about community-modified Loop versions for Spike. Links to those modified
Loop versions are not provided in these LoopDocs because we (the LoopDocs
maintainers and Loop developers) do not actively watch those versions to ensure
they are up-to-date.
