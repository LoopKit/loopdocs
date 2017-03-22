# Troubleshooting using Loop Pill in Nightscout

The Loop pill in Nightscout has a symbol displayed that helps provide information as to the status of the Loop.

X  	= error in Loop (see below for troubleshooting)</br>
ϕ 	= recommending basal, but not enacting (open loop or pump suspended)</br>
⌁ 	= enacted a new temp basal</br>
↻ 	= Loop is continuing with last temp basal, no change</br>
⚠ 	= warning (Loop has not completed since since the time set on your LOOP_WARN setting in NS)</br>

<table>
  <thead>
    <tr>
      <th>Loop Pill message</th>
      <th>Possible Cause</th>
      <th>Troubleshoot</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>unknownResponse (xxxx “Sent Pump Message”…)</th>
      <td>Pump communications are not working</td>
      <td>•	Be patient, usually self-resolves within 15 minutes</br></br>
•	Retune in RileyLink; check tune strength</br></br>
•	Check/change pump battery</br></br>
•	Move RileyLink closer to the pump</br></br>
•	Check if Remote ID is on in pump settings</br></br></td>
    </tr>
    <tr>
      <th>rF comms failure (Unable to set TempBasal)</th>
      <td>Pump settings are not allowing temp basal</td>
      <td>•	Check if max temp basal in pump > Loop’s max temp basal</br></br>
•	Check if temp basal type is set to u/hr in pump</br></br>
•	Go through steps in “unknownResponse” above</br></br>
</td>
    </tr>
    <tr>
      <th>staleDataError</th>
      <td>Loop can’t complete because either the CGM or pump data are old</td>
      <td>•	Check the error to see which data has the older date.</br></br>
•	If it is pump data that is old, try fetching event history and “unknownResponse” steps.  Set pump date using RileyLink</br></br>
•	If it is CGM data that is old, troubleshoot dexcom (does it have ???, did transmitter quit, did your session end, update transmitter ID in Loop if new)</br></br>
</td>
    </tr>
    <tr>
      <th>RL timeout</th>
      <td>RileyLink or iPhone's Bluetooth isn’t working</td>
      <td>•	Toggle RL on/off switch  (physical switch)</br></br>
•	Check battery connection in RileyLink</br></br>
•	Charge RileyLink</br></br>
•	Toggle iPhone's BT off and then on</br></br>

</td>
    </tr>
  </tbody>
</table>

## If these steps do not resolve your problem, try shutting down Loop app and restarting
