## Compatible CGM

!!! info "Time Estimate"

    - 10 minutes to read this page

!!! abstract "Summary"

    Loop is compatible with:

    - Dexcom G4 Share, G5, G6 or ONE CGM systems
        * Dexcom ONE is available in some countries
    - Dexcom G7
    - Medtronic sensors connected to a Loop-compatible Medtronic pumps

!!! question "FAQs"

    - **"What about Libre sensors?"** A [fork of Loop](https://www.loopandlearn.org/main-lnl-patches) is available with added Libre support
    - **"What about Eversense?"** Refer to [CGMs Not Supported in Loop](#cgms-not-supported-in-loop)


## Continuous Glucose Monitor (CGM)

Loop uses your CGM glucose readings, carbohydrate input and therapy settings, to model your current glucose trend, predict future glucose and automatically adjust insulin dosing. A compatible CGM is essential to operation of the Loop app.


## Dexcom G5, G6 and ONE CGM ![img/g5.jpg](img/g5.jpg){width="150"}

The Dexcom G5, G6 and ONE CGM transmits data directly to the Dexcom app on your iPhone via Bluetooth.

The Dexcom ONE, available in some countries, acts just like the G6 as far as Loop is concerned. The Dexcom ONE app does not provide some features, such as Dexcom Share, that come with the G6. When you set up Loop, select Dexcom G6 as your CGM to use Dexcom ONE CGM with the Dexcom ONE app installed on your phone.

If the Dexcom app is on the same device as Loop, Loop can function without an internet connection. See Offline Use below.

!!! warning "Dexcom G5 Support"

    [Dexcom has stopped supporting the G5 system in the US](https://www.dexcom.com/obsolescence). In the US, and some other countries, the G5 is not available for download from the Apple Store. There are countries in which Dexcom does supply and support G5. The G5 capability will continue to be supported in Loop.

    There are third party apps, which interface with G4 and G5 transmitters, supported by some forks of Loop. The version of Loop supported by these documents only works with the Dexcom apps.

## Dexcom G7 CGM

Dexcom G7 is supported with Loop 3.



## Medtronic CGM ![img/enlite.png](img/enlite.png){width="150"}

The Minimed Enlite CGM, available with the Medtronic 522/722, 523/723, and 554/754, wirelessly sends glucose readings to the pump. Loop can read the Medtronic CGM data directly from the pump using a RileyLink compatible device.

## Offline Use

"Offline Use" means using Loop when there is no cell data or internet available. Loop does not require any special setup to operate offline.

For offline Loop use, the iPhone's Bluetooth still needs to be active; and for Dexcom users, the G5, G6 or G7 app also needs to be running on your Loop phone. If you put your iPhone into Airplane mode, remember to turn Bluetooth back on to keep your Loop running. If your offline use is failing, chances are you have forgotten to update your transmitter ID in Loop settings when you changed transmitters.

## Dexcom Share

Loop can download Dexcom Share data for use in modeling glucose. However, this is not a typical configuration and requires internet connection for both the phone with the Dexcom app and the phone with the Loop app.  The Loop Set Up Steps for adding a CGM explain that you usually enter the Dexcom transmitter ID and leave the Dexcom Share setting blank.

!!! warning "Dexcom ONE"
    The Dexcom ONE app does not support Share.

## Nightscout as a Remote CGM

Loop 3 can use Nightscout as a remote source for CGM data. This requires cell or WiFi connection.


## CGMs Not Supported in Loop

Loop does not directly support some CGM such as Libre, Eversense and Medtronic Guardian.

* A [fork of Loop](https://www.loopandlearn.org/main-lnl-patches) is available with added Libre support
    * GitHub Build: Refer to the link above for instructions to build this fork
    * Mac-Xcode Build: Select the Loop with Patches option in the [Build Select Script](step14.md)

With Loop 3.0 and later, any sensor that can be uploaded to Nightscout can be used with Loop if internet service is available.

To use some Libre sensors with Loop 3 without need for internet service, you will need to install the version with patches (option 2 in the Build Select Script) and install your chosen app with the same Apple Developer ID. This uses the Shared App Group to share glucose. Not ideal but it works until Libre support is added to Loop.

Currently, there are no solutions for Eversense or Guardian CGM to be used directly with Loop, but some [Uploaders](https://nightscout.github.io/uploader/uploaders/) to Nightscout are available using an Android phone. Loop 3.0 and later allows the use of Nightscout as a CGM source.

## Next Step

If your compatible pump is Medtronic or Omnipod (not DASH)

* Next step is to [Order a RileyLink Compatible Device](step5.md)

If your compatible pump is Omnipod DASH

* Next step is to enroll in the [Apple Developer Program](step6.md).
