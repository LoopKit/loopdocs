# Configuring Loop - Pump Setup

Now that you are done with your Loop's version of your pump settings, you also need to setup your pump similarly.  Generally, the setup of the pump is similar to setting up any pump for non-looping use.  One notable exception: you will need to change those batteries more often with Looping.  Loop will drain pump batteries much faster than regular pump regimes, and Loop failures will increase in frequency as the pump battery gets low.  Roughly, a lithium AAA battery lasts about 15-16 days on an x23 or x54 pump using Loop.

While not every setting NEEDS to match between Loop and pump, it is safer to have them match in case your Loop fails and you revert back to normal pump use.  You should program the pump settings to match for:

* Carb ratio
* Basal schedule
* ISF
* Max bolus
* Insulin action duration (5 hours is reasonable, this setting won't be used by Loop anyways...Loop uses its own Insulin curves)
* BG targets

Basal schedule the one pump setting that is occassionally used by Loop app during normal looping.  When your Loop app decides that the basal rate scheduled in the Loop app is sufficient (i.e., Loop doesn't need to set a temp basal different than the regularly scheduled basal), Loop will cancel any currently running temp basals and let the pump just implement the scheduled basal.  You can force the Loop to instead set the matching temp basal, rather than let Loop cancel the currently running temp basal.  To do this, you need to follow the directions for [Code Customization](/../setup/build/code_customization) for Neutral Temp Basals.

IF your pump's basal schedule doesn't match the Loop's basal schedule (and you don't have neutral temp basals customized), this could result in your insulin delivery being different than Loop expected.  This won't be dangerous if the rates are fairly close, as Loop will read the reservoir volumes to determine actual insulin deliveries and adjust accordingly on the next pump read.

!!!info ""
    **Three settings in particular need to be done, OR ELSE YOUR LOOP WON'T WORK:**</br></br>
        * Set **<font color="orange">max basal</font>** in pump to at least equal to (or slightly greater) than the Loop’s max basal</br></br>
        * Set **<font color="orange">temp basal type</font>** to `insulin rate (u/h)`</br></br>
        * Set **<font color="orange">Remote Devices</font>** to `ON` and enter any random ID (000000 will work). This settings is found in the pump's Utilities menu (for x23 continue to Connect Devices, Remotes) and turn `ON` the Remote Options.</br>



