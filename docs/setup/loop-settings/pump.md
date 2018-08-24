# Configuring Loop - Pump Setup

Now that you are done with your Loop's version of your pump settings, you also need to setup your pump similarly.  Generally, the setup of the pump is similar to setting up any pump for non-looping use.  One notable exception: you will need to change those batteries more often with Looping.  Loop will drain pump batteries much faster than regular pump regimes, and Loop failures will increase in frequency as the pump battery gets low.  Roughly, a lithium AAA battery lasts about 15-16 days on an x23 or x54 pump using Loop.

While not every setting NEEDS to match between Loop and pump, it is safer to have them match in case your Loop fails and you revert back to normal pump use.  You should program the pump settings to match for:

* Carb ratio
* Basal rates (Standard schedule)
* Insulin Sensitivity Factor (ISF)
* Maximum bolus
* Maximum basal rate
* BG targets

Basal schedule is the one pump setting that is occassionally used by Loop app during normal looping.  When your Loop app decides that the basal rate scheduled in the Loop app is sufficient (i.e., Loop doesn't need to set a temp basal different than the regularly scheduled basal), Loop will cancel any currently running temp basals and let the pump just implement the scheduled basal.  This method works best when the pump and Loop are consistent with their basal rate schedules.  Loop v1.5.9 maintains consistency between the two by (1) automatically populating Loop's initial basal rates by reading the pump's existing Standard basal rate schedule when you setup Loop app and (2) any subsequent edits to Loop's basal schedule will need to be saved by writing those changes to the pump at the same time.  This ensures that Loop and the pump are always working on the same information for basal rates.  **Therefore, if you change basal rates later...make sure to do those changes in the Loop app and use Loop to save them to the pump.  If you make changes directly in the pump, Loop will not automatically know about those changes and you will cause a mismatch.**

Keep **<font color="orange">max basal and max bolus</font>** consistent between the pump and Loop.  Loop will initially read these Delivery Limits as part of Loop setup, and so consistency will be maintained so long as you use Loop app to make changes to those settings and use Loop to save the changes to the pump.  If you manually lower those settings directly in the pump, bypassing Loop, you will likely cause a Loop failure later when Loop tries to set a maximum basal/bolus higher than the edited pump setting.


!!!info ""
    **Three settings in particular need to be done, OR ELSE YOUR LOOP WON'T WORK:**</br></br>
        * Set **<font color="orange">temp basal type</font>** to `insulin rate (u/h)`</br></br>
        * Set **<font color="orange">Remote Devices</font>** to `ON` and enter any random ID (000000 will work). This settings is found in the pump's Utilities menu (for x23 continue to Connect Devices, Remotes) and turn `ON` the Remote Options.</br></br>
        * Cancel any currently running extended or dual wave boluses.  Loop cannot loop with those running.</br>



