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
      <td>•	Be patient, usually self-resolves within 15 minutes

•	Retune in RileyLink; send button press to verify

•	Check/change pump battery

•	Check if remote ID is on in pump settings</td>
    </tr>
    <tr>
      <th>rF comms failure (Unable to set TempBasal)</th>
      <td>Pump settings are not allowing or comms are poor</td>
      <td>•	Check if max temp basal in pump > Loop’s max temp basal

•	Check if temp basal type is set to u/hr in pump

•	Go through steps in “unknownResponse” above
</td>
    </tr>
    <tr>
      <th>staleDataError</th>
      <td>Loop can’t complete because either the CGM or pump data are old</td>
      <td>•	Check the error to see which data has the older date.  

•	If it is pump data that is old, try fetching event history and “unknownResponse” steps.  Set pump date using RileyLink

•	If it is CGM data that is old, troubleshoot dexcom (does it have ???, did transmitter quit, did your session end, update transmitter ID in Loop if new)
</td>
    </tr>
    <tr>
      <th>RL timeout</th>
      <td>RileyLink or iPhone's Bluetooth isn’t working</td>
      <td>•	Toggle RL on/off switch  (physical switch)

•	Check battery connection in RileyLink

•	Charge RileyLink

</td>
    </tr>
  </tbody>
</table>
