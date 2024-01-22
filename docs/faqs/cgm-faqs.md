## What CGMs does Loop work with?

The next release of Loop and the current [Loop-dev branch](../version/build-dev.md) includes Libre support in addition to the CGM listed below.

Loop 3 supports G5, G6, G7, Dexcom ONE, Dexcom Share, Nightscout and the Medtronic CGM systems compatible with Looping pumps.

Libre Support (for some Libre sensors):

* [Loop dev](../version/build-dev.md) adds [LibreTransmitter](https://github.com/dabear/LibreTransmitter#libretransmitter-for-loop){: target="_blank" }
* [Loop and Learn: Loop Customization](https://www.loopandlearn.org/custom-code){: target="_blank" }

Loop 2.2.x supports Dexcom G4 with share, G5, G6, Dexcom ONE, Dexcom Share and the Medtronic CGM systems compatible with Looping pumps.

There are more details on the [Compatible CGM](../build/cgm.md) page.

## Do I need wait for a new sensor session to start Loop?

No, you can start Looping mid-sensor session. There's no need to do anything special with regards to your CGM session when starting or ending Loop use.

## What do I do when sensor is in warm-up?

Loop will stop automatically adjusting insulin when the most recent glucose value is older than 15 minutes.  This is indicated by seeing three dashes in place of the glucose reading on the HUD.

* With Loop 3, a HUD status row message of `No Recent Glucose` is displayed, making it easier to add the fingerstick value directly in Loop, which also saves it in Apple Health

* With Loop 2.2.x or Loop 3, enter a fingerstick glucose value in Apple Health to enable Loop to provide updated projections and loop briefly

With no recent glucose readings, your pump returns to the scheduled basal delivery (within 30 min or less).

Loop continues to accept manual bolus commands. With Loop 3 only, [Manual Temp Basal](../loop-3/omnipod.md#manual-temp-basal) can also be commanded.

## What do I do when I switch Dexcom transmitters?

When you change transmitters (prior to Dexcom G7), you will need to update the transmitter ID in your Loop settings. The instructions for Dexcom are provided below:

* In Loop, select the `Delete CGM` button at the very bottom of the CGM info page
    * You cannot just edit the line with your old transmitter ID
* It's a good idea to go into your phone Bluetooth settings and delete the old Dexcom transmitter
    * The transmitter starts with Dexcom and ends with the last 2 characters of your old transmitter ID
    * Tap on the (i) next to `Not Connected` and select `Forget This Device`
* Follow the Dexcom instructions for pairing the new transmitter
* After pairing completes with Dexcom:
    * In Loop, add CGM and select the Dexcom system again
    * Enter the new transmitter ID
    * If you're unsure where to find your transmitter ID, see [Where to get the Transmitter ID for Dexcom G6?](../loop-3/add-cgm.md#where-to-get-the-transmitter-id-for-dexcom-g6)

![img/delete-cgm.jpg](img/delete-cgm.jpg){width="400"}
{align="center"}

If you don't update your transmitter ID when you change active transmitters, and you included your Dexcom share credentials, then Loop uses your Dexcom Share server to get your CGM data and will not work without cell or wifi connection. When Loop is using data from Dexcom Share servers, a small cloud will appear above the BG reading in Loop and should tip you off that maybe you forgot to update your transmitter ID. It's best not to enter Share Credentials. This makes it really obvious that you need to update the CGM settings in Loop at transmitter change time.

### Dexcom G7

With Dexcom G7, Loop automatically picks up the active sensor/transmitter pair from the Dexcom G7 app on the phone. Once Dexcom G7 is added to Loop as the CGM, the Looper does not need to do anything to Loop after selecting the new sensor/transmitter pair in the Dexcom G7 app.

### Dexcom G5, G6 and ONE

The diagram below illustrates the steps needed to **switch transmitters on Dexcom G5, G6, and ONE**. This typically needs to be done every three months when a new transmitter is started.

```mermaid
sequenceDiagram
    actor       user     as User
    participant dexcom   as Dexcom App
    participant loop_app as Loop App

    autonumber
    user     ->>  loop_app: Delete CGM
    user     ->>  dexcom:   Stop old Sensor
    activate      dexcom
    Note over     dexcom:   Switching sensors and transmitters... ⏱️
    user     -->> user:     Remove old Sensor and old Transmitter
    user     ->>  dexcom:   Enter/Scan new Transmitter ID
    user     ->>  dexcom:   Enter/Scan new Sensor Code
    user     -->> user:     Insert new Sensor then attach new transmitter
    user     ->>  dexcom:   Pair then Start new Sensor
    deactivate    dexcom
    dexcom   -->> user:     New Sensor warming up... 
    activate      dexcom
    Note over     dexcom:   New sensor warmup... ⏱️
    user     ->>  loop_app: Add CGM
    user     ->>  loop_app: Enter new Transmitter Serial Number
    user     ->>  loop_app: Enable Remote Upload
    dexcom   -->> user:     New Sensor operational
    deactivate dexcom
```


## Can I use Libre sensors with a reader like Miao Miao?

If you use Loop dev code, then any Libre sensor supported by [LibreTransmitter](https://github.com/dabear/LibreTransmitter#libretransmitter-for-loop){: target="_blank" } can be used with Loop.

See [What CGMs does Loop work with?](#what-cgms-does-loop-work-with).

## Can I use Eversense?

Eversense does not write to Apple Health. The BT communications protocol been not been reverse engineered as was done with Dexcom. There is a method to upload Eversense to Nightscout using an Android phone.

With Loop 3, you can use Nightscout as a CGM to Loop with Eversense, but that requires internet access.

## Can Loop read CGM data from Nightscout?

The released version of Loop can read CGM data from Nightscout.

The older Loop 2.2.x does not read CGM data from Nightscout.

## What other CGM apps can be used to Loop?

If you are willing to build a development version of Loop, the dev branch incorporates [LibreTransmitter](https://github.com/dabear/LibreTransmitter/blob/main/readme.md){: target="_blank" } into the Loop app itself. Please read about [Loop Development](../version/development.md) before [building dev](../version/build-dev.md) and using the dev app.

You can add xDrip4iOS and GlucoseDirect as a CGM option to Loop by applying a code customization.

Please read the docs for [xDrip4iOS](https://xdrip4ios.readthedocs.io/en/latest/){: target="_blank" } and [Glucose Direct](https://github.com/creepymonster/GlucoseDirect#readme){: target="_blank" }. You must build these apps yourself to Loop; you cannot use the TestFlight pre-built versions.
