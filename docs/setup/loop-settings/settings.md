# Configuring Loop - Pump 

Now that you have the Loop app installed on your iPhone, we need to input the settings so that the Loop can work for you.  In this section, we cover the details and provide information about the Loop displays.  Finally, we will cover some extras like Apple Watch and useful external integrations.

Normally, we would start by explaining the displays on an application, but your Loop won’t have much showing initially until we get some basic settings input.  So, let’s start by clicking on the Loop Settings button in the tool bar.  It looks like a little sprocket.

<p align="center">
<img src="../img/loop_settings.jpg" width="450">
</p>

## Loop Version

The first graphic at the top of the Loop settings display shows the version of the software, e.g.,  Loop v1.3 in this example.  This can be helpful when working with other users of the software to know what version you are running.

<p align="center">
<img src="../img/loop_version.jpg" width="400">
</p> 

## Closed Loop

The Closed Loop switch controls the Loop operation mode for the application. This operation mode determines whether Loop automatically enacts recommendations (i.e., sets temp basals) to the insulin pump.  

<p align="center">
<img src="../img/open_loop.png" width="400">
</p> 

When the Closed Loop switch is in the (Off&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   ) position, Loop WILL NOT enact recommended temp basals automatically.  Instead, it will display Recommended Temp Basals on the main status display, just above the Glucose graph.  This is called **<font color="orange">Open Loop</font>**, and is a good way to understand how Loop will function, and what type of recommendations it would make.  If you click on the recommended temp basal line while in Open Loop mode, Loop will implement the temp basal.

<p align="center">
<img src="../img/closed_loop.png" width="400">
</p> 

When the Closed Loop switch is in the (&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   On) position, Loop WILL automatically enact recommended temp basals on the configured insulin pump. This is known as **<font color="orange">Closed Loop</font>**.  Typically, Loop will show the recommended temp basal just above the Glucose graph prior to automatically enacting it.  It may take a minute or so for the Loop to enact the recommended basal.  Once the temp basal has been enacted successfully on the pump, the recommended temp basal will disappear from the screen and the new temp basal will be represented in the insulin delivery graphics.

## Preferred Data Source

<p align="center">
<img src="../img/preferred_source.jpg" width="300">
</p> 

If Preferred Data Source is set to **<font color="orange">Event History</font>**, then the pump will periodically be polled for treatment events.  This will cause your pump battery to be used at a slightly faster rate, but there are benefits which generally outweigh that negative.

!!!info ""
    **Event History must be selected for Nightscout to display temp basals, carbs, and boluses from Loop.**  Event History must also be selected in order for prime events to be detected and NOT contribute to iob during site changes.


## Issue Report
If you run into problems or errors with your Loop, the Issue Report can be used to help identify where the problem is occurring.  The Issue Report is automatically generated and you can share it via email.  Frequently, if you go to Gitter or Facebook for help with a technical problem, an Issue Report will provide insight to what the potential problem is.

## Devices
Make sure your RileyLink is turned on and nearby, then you will see a RileyLink listed in this area of the settings.  Actually, you will see a list of any RileyLinks that are in the nearby area.  Slide the switch on and RileyLink will connect.

Side Note: The device searching indicator (circle on the right of Devices line) will always be spinning, even after a RileyLink is successfully connected.  That is an indicator of a healthy Loop app operation.

If you are ever going to be near other Loop users, you may want to consider renaming your RileyLink to a new name (like this one is renamed ToughRL) so that you can pick it out of a crowd.  Click on the RileyLink line, and the RileyLink's menu will be displayed.  At the top of this menu is a line for the device name.  Click on the that line and you will be able to change the name of your RileyLink.  (Sometimes it takes a couple tries to change the name...so if it doesn't take the first time, try a couple more times. RileyLink must be connected and on to change the name.)

<p align="center">
<img src="../img/rileylink_on.jpg" width="300">
</p>


## Pump ID
You need to enter your pump’s six-digit ID here.  To find your pump ID, press ESC button on the pump, scroll down.  You will find a the six-digit ID as the “S/N#”.  You will also find the same ID on the back of the pump as six numbers beneath the pump’s model number.  If your pump has **NA** or **CA** in the model number's REF line, then choose North America.  If the REF line contains **WW**, then choose World-Wide.  This selection adjusts the tuning frequency range the RileyLink will use for pump communications.

## Pump Battery Type
Click which battery type, alakine or lithium, you are using so that the battery percentages are more accurately displayed in your Loop display.  The battery displays are designed to give you approximately 8-10 hours notice before looping would fail.  However, every battery manufacturer has its own decay curve for its specific batteries.

Do not trust your pump screen's battery level indicator as a set-point for changing battery when using Loop.  **<u>Low pump battery will cause loop failures, due to failed pump communications, prior to the actual pump failing to delivery insulin.</u>**  Additionally, the pump's battery level warnings are not calibrated to lithium batteries.

## CGM Selection
Select one of the options from the menu:

* Sof-Sensor/Enlite
* G4 Share Receiver
* G5 Transmitter

If you select the G5 Transmitter, you will be prompted to enter the transmitter ID number.  Don't forget to update your transmitter ID when you change transmitters, otherwise your loop will not work.

If you are a G4 or G5 user, don't forget to enter your Dexcom Share information (this will be the same as your Nightscout Bridge username and password, too).  By entering your Dexcom Share account info, Loop will be able to fetch from the Dexcom servers via the internet when local BG readings from spying on the receiver/transmitter directly are not working.  The switch between local readings to server data pull will happen automatically when needed.  When Loop is using data from Dexcom servers, a small cloud will appear above the BG reading in Loop.

!!!info ""
    The Share account login is the same as what you used to login to your Share/G5 app on your iPhone.  Dexcom Share account is not always the same login info as your Dexcom Clarity account.  For G4 users, the Share account is found in the account tab on the app.  For G5 users, unfortunately, there is no information in the app displaying what your account name is.  The information is entered when you first login to the app and then is never displayed again, nor visible under any information screens.  If you have forgotten your G5 account info, you can delete the G5 app and redownload it to try logging in again.  This will not cause a restart of any sensor sessions in progress.  Alternatively, you can try the [Dexcom Store](https://uam1.dexcom.com//index.html#/forgotInfo) to retrieve the information using your email address.

## Correction Range
This is where you set your blood glucose range that you would like Loop to correct to. Correction Range is not necessarily what your target BG range that you have discussed with your endocrinologist; generally that range will be much wider.  For example, you may keep a correction target of 100-100 for Loop to aim to, but use a desired BG target range of 90-150 when discussing things with your endo about "time in range".


<p align="center">
<img src="../img/premeal_entry.jpg" width="250">
</p>
</br></br>

Click the + in the upper right corner to add  correction BG range(s).  You can have multiple ranges based on time of day, but the first setting of the day needs to begin at midnight to be consistent with your Medtronic pump.

Ranges will be entered in mg/dl or mmoL automatically based upon how your BG values appear your BG chart. By default they are set to mg/dl, however once BG values arrive in mmoL these settings can be entered in mmoL. If you are planning to use mmoL, be sure to wait to set your correction range until after you have started to receive BG values. If you do these in the wrong order, then your chart may have incorrect Y axis. If you come across this issue, you can also remove all of your target ranges and enter them again. Once you are receiving BG values in mmoL, you can add your correction range(s) in mmoL.

Correction ranges can be a single number, such as 100-100 mg/dL.  Generally, you don't want to keep correction ranges too wide otherwise Loop will be sluggish to correct.  Most users keep correction range no wider than about 0 to 20 mg/dl between the min and max values.

### Override Ranges
Set the “override” ranges for temporary alternate correction ranges.  These override ranges will only be enacted when you specifically activate "Pre-Meal or “Workout Mode” using the buttons on the main Loop display.  While active, they replace the correction range for Loop's recommendations.  If the override ranges are not entered in this section, the buttons will remain grey and unusable on the main screen.

**<font color="orange">Pre-Meal</font>**
The pre-meal target is designed to be used to as an easy way to get a small amount of insulin delivered before a meal (similar to the "eating-soon" mode discussed in OpenAPS) in order to help control post-meal BG spikes.

If your normal target is 100-100 and pre-meal target is 80-80 mg/dl, for example, Loop will give you an extra push to get you to the lower target number before the meal.  The pre-meal target, when activated by pressing on the icon, will stay active for one hour, until carbs are entered, or until it is manually cancelled...whichever comes first.

Loop will adjust any insulin bolus as needed based on the insulin provided during this pre-meal time.

**<font color="orange">Workout Mode</font>**
Workout Mode override targets are designed to temporarily set targets higher in anticipation of exercise or other activities which tend to make the Looper more insulin sensitive or need less insulin.  By setting a higher temp target ahead of activity, Loop will recommend less basal rate(s) than normally scheduled in order to to bring BGs up to the higher target.

The success of this strategy will be dependent on how far in advance of activity the temp target is set.  Generally, users set the target approximately 1-2 hours in advance of planned activities...but the optimal timing will depend on the activity, duration, and intensity.  Additionally, any insulin on board from recent boluses may overwhelm the Loop's ability to counteract exercise-induced lows through lower temp basals alone.

## Suspend Threshold
Suspend Threshold is a required data entry for successful configuration of Loop. **<font color="blue">Your Loop will not turn green without setting this value.</font>**  This value affects both bolus and basal recommendations by Loop.

### Bolus

* If you are trying to bolus a meal while any part of the predicted BG curve is below this suspend threshold value, Loop will not recommend a bolus.  Instead, you will need to wait until your prediction curve is above the suspend threshold value in order to bolus.

### Basal

* If your current or forecasted BG is below the suspend threshold, Loop will always recommend a temp basal rate of 0 u/hr.

## Insulin Model
There are four Insulin Models to choose from; Walsh, Rapid-Acting Adults, Rapid-Acting Children, and Fiasp.  If you want to read the nitty-gritty discussion that went into the development of these new curves, you can see that in GitHub [here](https://github.com/LoopKit/Loop/issues/388#issuecomment-317938473).

You can click on each model and see what each model's insulin activity curve looks like.  If you select the Walsh model, and adjust the insulin action duration (DIA default is 6 hours), the curve will be adjusted accordingly based on your selection.

<p align="center">
<img src="../img/models.jpg" width="350">
</p>

The differences between the new (Rapid-Acting and Fiasp) models have to do with the timing of the Peak Activity of the insulin.  Currently, all the models are defaulted [in the code]( to an insulin duration of 360 minutes...but the peak activity of the various curves differs:

* Rapid-acting adult curve peaks at 75 minutes
* Rapid-acting child curve peaks at 65 minutes
* Fiasp peaks curve peaks at 55 minutes

As the peak time decreases, the Loop will expect a quicker insulin impact on BG AND the tail of the insulin dose will be slightly less agressive compared to a curve with a later peak time.  In other words, Fiasp will be more powerful soon after a bolus and less powerful 5 hours later than an equal amount of insulin modeled using the other models.

The Walsh model's insulin duration can be set by the user from within the app.  The peak time of the Walsh curve is 100 min at a DIA of 4 hours.  As user adjusts DIA, the peak time will be dynamically adjusted.

## Basal Rates
Enter your basal rates here.  These should match the values entered in your pump. Entering them here will not override your pump’s values, so make sure they match. This is fairly standard stuff that most T1Ds are already familiar with.  However, if you are new to Medtronic pumps...keep in mind that your insulin needs may change slightly when changing pump systems.  If in doubt, try some basal testing to see if your old basal rates may need adjustments with the switch to Medtronic pumps and infusion sets.

Only one basal pattern may be set in each Loop app.  If you are accustomed to switching between two or more basal patterns frequently, you have two options:

1. manually editing the basal profiles in this area each time you change basals, or
2. installing a duplicate Loop app for each basal pattern and switching when needed.

If you choose to have duplicate Loop apps, you will need to use different MAIN_APP_BUNDLE_IDENTIFIERs for each app.  Additionally, you must remember to close  the unused Loop app (double-click iPhone home button and up-swipe Loop app).  Only one Loop app can run successfully at a time.  When you switch to the new Loop app, it may take 5-15 minutes for the Loop to turn green.  The good news is that all your carb entries, insulin doses and such will automatically populate in the new Loop within a relatively short amount of time and the transition is therefore seamless for Loop functionality.  

## Carb Ratios
Click the + in the upper right to add carb ratios for various times of day. Loop works best if you have tested and optimized your carb ratio settings for accuracy.

The first time you setup carb ratios, you will be prompted to allow Loop app access to write/read data in your iPhone's Health App, choose only the selection for `write` data so that Loop does not inadvertently read third party app's carbohydrate inputs.  See [Carb Entries with Third Party apps](/operation/features/carbs.md#third-party-apps) for more information about this setting.

## Insulin Sensitivities
Click the + in the upper right to add insulin sensitivities for various times of day. Loop works best if you have tested and optimized your ISF settings for accuracy.  Insulin sensitivities can change for many reasons including waiting too long to change your infusion set.  Loop will not auto-detect changes in ISF.

## Maximum Basal Rate
Maximum basal rate is the maximum temporary basal rate that the Loop is allowed to enact to correct to your target BG range.  See the Use section discussion for [Close Loop](/operation/loop/close-loop.md) for some suggestions regarding appropriate Maximum Basal Rate.

!!!info ""
    A frequent error for new Loop users is when they set their maximum basal rate here to a value HIGHER than the corresponding setting on the pump.  This will result in an error message that the temp basal failed to enact.  For example, Loop cannot successfully tell the pump to deliver 4 units per hour if the pump’s maximum is set to only 3.8 units per hour.  If you are seeing failures of the Loop to set a high temp basal, check to see if your pump’s maximum basal is at greater than or equal to the Loop’s maximum basal.

## Maximum Bolus
Enter your desired single bolus maximum here.  Same caution applies here...you max bolus on the pump will need to be at least as great as the Loop's max bolus setting.


