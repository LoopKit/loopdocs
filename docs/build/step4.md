# Compatible CGM

!!! info "Time Estimate"

    - 10 minutes to read this page

!!! abstract "Summary"

    Loop is compatible with:

    - Dexcom G4 Share, G5, or G6 CGM systems
    - Medtronic sensors connected to a Loop-compatible Medtronic pumps

!!! question "FAQs"

    - **"What about Libre sensors?"** Refer to [CGMs Not Supported in Loop](#cgms-not-supported-in-loop)
    - **"What about Eversense?"** Refer to [CGMs Not Supported in Loop](#cgms-not-supported-in-loop)


## Continuous Glucose Monitor (CGM)

Loop uses your CGM glucose readings, carbohydrate input and therapy settings, to model your current glucose trend, predict future glucose and automatically adjust insulin dosing. A compatible CGM is essential to operation of the Loop app.


## Dexcom G5 and G6 CGM ![img/g5.jpg](img/g5.jpg){width="150"}

The Dexcom G5 and G6 CGM transmits data directly to the Dexcom app on your iPhone via Bluetooth.   If the Dexcom app is on the same device as Loop, Loop can function without an internet connection. See Offline Use below. 

!!! warning "Dexcom G5 Support"

    [Dexcom has stopped supporting the G5 system in the US](https://www.dexcom.com/obsolescence). In the US, and some other countries, the G5 is not available for download from the Apple Store. There are countries in which Dexcom does supply and support G5. The G5 capability will be supported in the next version of Loop (currently under test in the dev branch.)

    There are third party apps, which interface with G4 and G5 transmitters, supported by some forks of Loop. The version of Loop supported by these documents only works with the Dexcom apps.

## Dexcom G4 CGM with Share Receiver ![img/g4_receiver.png](img/g4_receiver.png){width="150"}

!!! warning "Loop 3.0 will not support G4"

    Loop 3 (currently under test in the dev branch) will not support G4 because it is no longer available. If this is a problem for current Loop users, please post on your favorite [social media site](../intro/loopdocs-how-to.md#how-to-find-help).

The Dexcom G4 Share system transmits CGM data from the transmitter to a Dexcom G4 Share Receiver. The receiver, in turn, connects to the Dexcom Share2 app on your iPhone via Bluetooth. The Share2 app uploads CGM data to the Dexcom servers from your phone. For Loop to function without an internet connection, you will need the Dexcom app running on the same device as Loop.

## Medtronic CGM ![img/enlite.png](img/enlite.png){width="150"}

The Minimed Enlite CGM, available with the Medtronic 522/722, 523/723, and 554/754, wirelessly sends glucose readings to the pump. Loop can read the Medtronic CGM data directly from the pump using a RileyLink compatible device.

## Offline Use

"Offline Use" means using Loop when there is no cell data or internet available. Loop does not require any special setup to operate offline.

For offline Loop use, the iPhone's Bluetooth still needs to be active; and for Dexcom users, the Share2, G5, or G6 app also needs to be running on your Loop phone. If you put your iPhone into Airplane mode, remember to turn Bluetooth back on to keep your Loop running. If your offline use is failing, chances are you have forgotten to update your transmitter ID in Loop settings when you changed transmitters.

## Dexcom Share

Loop can download Dexcom Share data for use in modeling BG. However, this is not a typical configuration and requires internet connection for both the phone with the Dexcom app and the phone with the Loop app.  The Loop Set Up Steps for adding a CGM explain that you usually enter the Dexcom transmitter ID and leave the Dexcom Share setting blank.

## CGMs Not Supported in Loop

Loop does not directly support other CGM, such as Libre, Eversense and Medtronic Guardian. When Loop 3 is released, any sensor that can be uploaded to Nightscout can be used with Loop if internet service is available.

To use one of those alternate CGMs for Loop 2.2.x, you will need to look into third-party integrations, such as the FreeAPS fork, for access to the CGM data. First search for previous posts on the topic and then ask questions in a [Loop Social Media](../intro/loopdocs-how-to.md#how-to-find-help) site if you need help. 

Currently, there are no solutions for Eversense or Guardian CGM to be used directly with Loop, but some [Uploaders](https://nightscout.github.io/uploader/uploaders/) to Nightscout are available using an Android phone. The next Loop release, and the current FreeAPS fork, allow the use of Nightscout as a CGM source.

## Next Step

If your compatible pump is Medtronic or Omnipod (not DASH)

* Next step is to [Order a RileyLink Compatible Device](step5.md)

If your compatible pump is Omnipod DASH

* Next step is to enroll in the [Apple Developer Program](step6.md).
