# Getting a Green Loop

**Troubleshooting tips for when your Loop fails to turn green.**

If you are initially starting the Loop app, wait about 15-30 minutes for the Loop to turn green and start working.  If the Loop remains grey, there are several possible causes for this. Use the sections below to help determine which part of the system is causing the problem.

!!! info ""
    To see the latest Loop status messages, touch the Loop Status circle on the main screen. If an error message is available it will appear in a dialog window. Additional information may be available from the Nightscout [Loop pill](/nightscout/loop_pill/).

## Check your CGM
CGM updates drive Loop. Without fresh CGM data, Loop cannot run.

* Loop needs glucose data from your CGM.
* The latest glucose timestamp must be less than 5 minutes old.
* A **yellow alert symbol** indicates the glucose data is older than 5 minutes.
* A **cloud symbol** indicates that Loop is trying to retrieve glucose values from Nightscout.

### Troubleshoot your CGM
* Verify your CGM device is operating properly.
* Verify your CGM data is available on your phone (if applicable).
* Verify your CGM device has a Bluetooth connection to your phone (if applicable).
* Verify you have enabled the correct [CGM Selection](/build/configuration/#cgm-selection) in Loop settings.
* Verify Bluetooth is turned on and your device is connected.
* For Dexcom 5, verify your [transmitter ID](/build/configuration/#cgm-selection) is set correctly in Loop settings.
* For Dexcom 4, verify the Dexcom Share app is running on your phone and that your [Dexcom Share]](/build/configuration/#dexcom-share) settings are correct.

## Check your Pump
Reliable communication with your pump is required so that Loop knows about all insulin delivered, as well as other pump settings.

* The latest insulin reservoir timestamp must be less than 5 minutes old.
* If you set Event History as your [Preferred Data Source](/build/configuration/#preferred-data-source), the pump's event history is frequently retrieved from the pump. While this is the recommended setting, this command can take a while and therefore may increase failures if you are already having communication problems with your pump.


### Troubleshoot your pump
* Your pump maximum basal rate setting on your pump needs to be equal to (or greater than) the [Maximum Basal Rate]((/build/configuration/#maximum-basal-rate) setting in Loop.  
* Your pump temporary basal type needs to be **set to units/hr (aka absolute)**, not % (percentage).
* Your Remote ID options on your pump needs to be "on" with a code (any code) entered.
* Your pump cannot be suspended.  Resume insulin deliveries.
* Your pump battery may be low.  Replace the battery.
* Try [Tuning the Radio](rileylink/?#tuning-the-radio)
* Try running the [Fetch Event History](rileylink/?#commands) command. Some people have found it helpful to run it a second time if it fails.

## Check your RileyLink
Bluetooth and Radio communication is orchestrated by the RileyLink device.

* Your RileyLink battery needs adequate charge.
* A Bluetooth connection to your phone is required.
* Your RileyLink device must be turned on under **Devices** in the Loop settings screen.
* Your [Pump ID](/build/configuration/#pump-id) (serial number) must be set in Loop settings.

### Troubleshoot your RileyLink
* Your RileyLink battery needs to be securely plugged in, check those connections.
* Your batteries must be fully charged.
* Verify your Pump ID (serial number) is correct
* Verify your [G5 transmitter ID](/build/configuration/#cgm-selection) is correct. Remember to update this when you change transmitters.
* Loop may be having trouble communicating with the pump. Try [Tuning the Radio](rileylink/?#tuning-the-radio).  Move RileyLink closer to pump.
* Check that the iPhone has a bluetooth connection with RL. The RL's green light should remain on when BT is connected with iPhone.
* Check that the correct RL devices on the Settings screen are turned on. Running multiple RL devices at the same time can work, but turn on only one at a time when troubleshooting a problem.

## Check your Loop
A green circle (notched for open loop, and complete for closed loop) indicates Loop is operating properly.

### Troubleshoot your Loop
* Touch the Loop Status circle to retrieve the latest error message. If there are no message available, none are displayed.
* Check that you have the [Minimum BG Guard](/build/configuration/#minimum-bg-guard) value set in Loop app settings.
* Check that you don't have another Loop app running at the same time on same iPhone (for users who install multiple Loop apps).
* If a recommended basal is showing, and this is your first loop, try clicking on the recommendation to enact it.

## Patience
It may be that everything is working properly, but you need to wait for Loop to update.

* CGM data is retrieved every 5 minutes.
* Pump event history data is retrieved every 5 minutes.
* Intermittent errors can cause this cycle to be 10-15 minutes or longer.
* If all else fails after verifying the settings above, you can:
    * Close and restart the Loop app
    * Restart the iPhone
    * Restart the RileyLink

## Common Problems

<table>
<thead>
<tr>
<th>Problem / Error Message</th>
<th>Possible Cause</th>
<th>Troubleshooting Ideas</th>
</tr>
</thead>
<tbody>
<tr>
<th>unknownResponse (xxxx “Sent Pump Message”…)</th>
<td>Pump communications are not working</td>
<td>
•	Be patient, usually self-resolves within 15 minutes</br></br>
•	Retune in RileyLink; check tune strength</br></br>
•	Check/change pump battery</br></br>
•	Move RileyLink closer to the pump</br></br>
•	Check if Remote ID is on in pump settings</br></br></td>
</tr>
<tr>
<th>rF comms failure (Unable to set TempBasal)</th>
<td>Pump settings are not allowing temp basal</td>
<td>
•	Check if max temp basal in pump > Loop’s max temp basal</br></br>
•	Check if temp basal type is set to u/hr in pump</br></br>
•	Go through steps in “unknownResponse” above</br></br>
</td>
</tr>
<tr>
<th>staleDataError</th>
<td>Loop can’t complete because either the CGM or pump data are old</td>
<td>
•	Check the error to see which data has the older date.</br></br>
•	If it is pump data that is old, try fetching event history and “unknownResponse” steps.  Set pump date using RileyLink</br></br>
•	If it is CGM data that is old, troubleshoot CGM device (does it have ???, did transmitter quit, did your session end, update transmitter ID in Loop if new)</br></br>
</td>
</tr>
<tr>
<th>RL timeout</th>
<td>RileyLink or iPhone's Bluetooth isn’t working</td>
<td>
•	Toggle RL on/off switch  (physical switch)</br></br>
•	Check battery connection in RileyLink</br></br>
•	Charge RileyLink</br></br>
•	Toggle iPhone's BT off and then on</br></br>
</td>
</tr>
<tr>
<th>Loop works intermittently</th>
<td>Communications are not stable or reliable</td>
<td>
•	Is something interfering with the RileyLink's RF radio antenna. That component should not have any metal touching or surrounding it.</br></br>
•	Has MySentry Pair <a href='/build/configuration/?#commands'>Command</a> been run? (x23 and x54 pumps only).</br></br>
</td>
</tr>
<tr>
<th>Some other problem</th>
<td></td>
<td>
•	Are errors being logged to mLab errors collection?</br></br>
•	Has mLab database quota been exceeded?</br></br>
•	Are two Loop applications running?</br></br>
</td>
</tr>
</tbody>
</table>
