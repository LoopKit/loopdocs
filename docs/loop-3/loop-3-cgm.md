# CGM Configuration

The CGM configuration can be selected from the Heads-Up-Display ([HUD](loop-3-displays.md#heads-up-display)) or from the [Loop Settings](loop-3-settings.md) screen.

## Add CGM

The HUD will look like the graphic below if no CGM or Pump is configured for Loop:

![Loop HUD when both CGM and Pump have not been added](img/loop-3-hud-add-cgm-add-pump.svg){width="350"}
{align="center"}

With Loop-dev, the user has a new option for CGM, [Nightscout Remote CGM](#nightscout-remote-cgm), in addition to those available with Loop 2.x.x. The Dexcom G4 is no longer available, so is no longer supported by Loop-dev.

* CGM that reside on the same phone (internet not required)
    * [Dexcom G5/G6](../build/step4.md#dexcom-g5-and-g6-cgm)
    * [Minimed Enlite CGM](../build/step4.md#medtronic-cgm) (Medtronic Pump only) 
* CGM that require active internet
    * [Nightscout Remote CGM](#nightscout-remote-cgm)
    * [Dexcom Share](#dexcom-share)

The addition of the Nightscout Remote CGM enables the use of Loop-dev with any sensor that can be uploaded to your Nightscout URL.

### Nightscout Remote CGM

If the user has CGM data available at their Nightscout URL, they can select that as a source for CGM data for Loop. The user must acknowledge they understand the risks of using a remote source that requires internet, as shown in the graphic below.


![Nightscout Remote CGM acknowledgement screen](img/nightscout-cgm-acknowledge.svg){width="350"}
{align="center"}


The user must enter both the URL and the API Secret to ensure the security of the data.

![Nightscout Remote CGM entry screen](img/nightscout-cgm-entry.svg){width="350"}
{align="center"}

When using Nightscout Remote CGM, if the user needs to modify credentials or switch to a different CGM, the user must go through the Loop->Settings->CGM menu.

## CGM Icon

Tapping on the CGM icon in the HUD shows more information about the last CGM reading.

For Dexcom G5/G6 and Share, the same screen is obtained by tapping on Loop Settings->CGM.

For Nightscout Remote CGM, the Nightscout URL is opened when tapping on the CGM icon in the HUD, while the credential sections is shown when tapping on Loop Settings->CGM.

The graphic below shows the result of tapping on the CGM icon when using a Dexcom G6.  It includes the time of the last reading to the nearest second, along with other information about that sensor and transmitter. It also has an option to go to the Dexcom app on the same device.

![dexcom information screen from ](img/dexcom-info-menu.svg){width="250"}
{align="center"}

## Modify CGM

To modify the selected CGM, it must first be deleted. Then a new CGM can be added.  Scroll to the bottom of the current CGM screen and tap `Delete CGM`.

When changing Dexcom Transmitters, you must first `Delete CGM` and then add the CGM back with the new Transmitter serial number.


