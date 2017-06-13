# Loop fails to turn green?

If you are initially starting the Loop app, wait about 15-30 minutes for the Loop to turn green and start working.  If the Loop remains grey, there are several possible causes for this:

## Check your CGM
* CGM updates drive loop. If you're not getting fresh CGM data, Loop will not run.
* Check the time on the latest CGM reading in loop on the top of the status screen.

## Check your Pump
* Your max basal setting on your pump needs to be equal to (or greater than) the max basal setting in Loop.  
* Your temp basal type needs to be set to units/hr, not %.
* Your Remote ID options on your pump needs to be "on" with a code (any code) entered.
* Your pump cannot be suspended.  Resume insulin deliveries.
* Your pump battery may be low.  Replace the battery.

## Check your RileyLink
* Your RileyLink battery needs to be securely plugged in, check those connections.
* Your RileyLink battery needs adequate charge (usually for first time users...batteries aren't shipped fully charged)
* Double check your Pump ID (serial number) is correct
* Double check that your G5 transmitter ID is correct (remember to update this when you change transmitters)
* Loop may be having trouble communicating with the pump. Try tuning.  Move RileyLink closer to pump.
* Check that the iPhone has a bluetooth connection with RL. The RL's green light should remain on when BT is connected with iPhone.

## Check your Loop
* Check that you have the Minimum BG Guard value set in Loop app settings
* Check that you don't have another Loop app running at the same time on same iPhone (for users who install multiple Loop apps)
* If a recommended basal is showing, and this is your first loop, try clicking on the recommendation to enact it.

## Patience
* It may be that everything is working properly, but you need to wait for the next cgm data to arrive **and** for Loop to fetch latest dose data from the pump; this is normally 5 minutes, but if something happens, it could be 10-15 minutes.

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
•	Is something interfering with the RileyLink's RF radio antenna. That component should not be any metal touching or surrounding it.</br></br>
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
