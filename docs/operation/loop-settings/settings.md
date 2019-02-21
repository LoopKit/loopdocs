# Configuring Loop

Now that you have the Loop app installed on your iPhone, we need to input the settings so that the Loop can work for you. 

Your Loop won’t have much showing initially until we get some basic settings input. Let’s start by clicking on the Loop Settings button in the tool bar at the bottom of your Loop app. It looks like a little sprocket. On the settings screen that opens, click on Add Pump.

<p align="center">
<img src="../img/loop_settings.png" width="450">
</p></br>

!!! warning "Medtronic Users: MUST DO"
    Before you begin the rest of the setup process, go to your Medtronic pump menu and:</br></br>
    1. Turn off Patterns under the basal menu settings. </br></br>2. Make sure your basal rate schedule is up-to-date and accurate.</br></br>3. Set your pump's `Temp Basal Type` to `Absolute (U/hr)`. Do NOT use percentage. Your Loop will not run unless your temp basal type is set to units/hour.</br></br>4. Make sure your maximum basal rate and maximum bolus (those are particular settings in the pump) are reasonably set for your particular needs. For new Loop users, a maximum basal rate equal to approximately 2-4 times your highest scheduled basal rate is a good starting point as you learn Loop and dial in your other settings. You can adjust as your comfort and use of Loop develop.</br></br>

## Add Pump

You will now need to do a few simple steps:

1. Make sure your RileyLink is turned on and nearby, then you will see a RileyLink listed in this area of the settings.  Actually, you will see a list of any RileyLinks that are in the nearby area. Slide on the toggle for your RileyLink.</br></br>
2. Add your pump's region, color and serial number.</br></br>
3. Click the `Continue` button to finish the addition of your pump.</br></br>

<p align="center">
<img src="../img/add_pump.png" width="750">
</p>

!!! info "For x23 and x54 Medtronic pump users only"
    <table>
    <th><p align="inline"><img src="../img/pump_broadcasts.png" width="550"></p></th>
    <td>For x23 and x54 Medtronic pump users, there is a packet of information special to those pumps called MySentry messages. If you have never setup this part of the pump previously, you may see a screen, called "Pump Broadcasts", at this point in the setup process.</br></br>Follow the directions on the screen. They will require you to take some manual steps on your pump to "pair" it with your Loop app.</br></br>Basically, you will need to go to your pump's main menu, scroll down to Utilities, then Connect Devices, then Other Devices, turn that setting On, and then select Find Device. Once you do that, click on the `Continue` button in Loop app and the pairing will take place. This will allow those MySentry packets of information to flow to Loop app.</td>
    </table>
    
Now that your pump is paired with Loop, you will be finishing these steps:

1. Change your pump time using the Loop app (and read all the info on that screen)</br></br>
2. Import your pump's basal rate schedule, maximum basal rate, and maximum bolus (maximums are collectively called "delivery limits" in Loop)</br></br>
3. Select your pump's battery type (lithium or alakine)</br></br>
4. Leave the Preferred Data Souce on Event History </br></br>

**Event History must be selected for Nightscout to display temp basals, carbs, and boluses from Loop.**  Event History must also be selected in order for prime events to be detected and NOT contribute to iob during site changes. </br></br>
    
<p align="center">
<img src="../img/add_pump2.png" width="750">
</p>
 
 Once you finish those steps, click on the settings button in the upper left corner to take you back to the Loop's settings menu.  If you ever need to change the pump time or access the RileyLink menus, you will be clicking on the pump's image in Loop settings to come back to this area.
 
## CGM Selection
Now we need to add a CGM source so that Loop has BG data. The standard selections available will be:

* Dexcom G6
* Dexcom G5
* Dexcom G4
* Dexcom Share

If you added a compatible Medtronic pump earlier in the setup process, then you will also see an option for the compatible Medtronic sensor that works with that same pump.

* The Dexcom G5 and G6 options only require the addition of the active transmitter ID at a minimum. You do not have to add your Dexcom Share account credentials, but if you do, make sure they match what you originally entered into your Dexcom app on the iPhone. You will have to remember to update your transmitter ID in this section when you swap out your active transmitter. If you don't update your transmitter ID, your Loop will be forced to go to your Share account to get your CGM data and will not work without cell or wifi connection. When Loop is using data from Dexcom Share servers, a small cloud will appear above the BG reading in Loop and should tip you off that maybe you forgot to update your transmitter ID.

* Dexcom G4 users will need the Dexcom G4 Share2 app active on their iPhone and paired to their Dexcom G4 Share receiver.

* The Dexcom Share selection is primarily for people who wish to test Loop function without a local CGM source. This selection will require login access to a Dexcom Share account with live data and active internet connection in order to work.

For all selections, the Share account login is the same as what you used to login to the active Dexcom app on your iPhone. **Dexcom Share account is not always the same login info as your Dexcom Clarity account.** For G4 users, the Share account is found in the account tab on the app. For G5/G6 users, unfortunately, there is no information in the app displaying what your account name is. The information is entered when you first login to the app and then is never displayed again, nor visible under any information screens. If you have forgotten your G5/G6 account info, you can delete the Dexcom app and redownload it to try logging in again. This will not cause a restart of any sensor sessions in progress.
    
!!!info "Spike Users"
    Users who are using Spike app to access other CGM types (or to avoid using the Dexcom app), you will need to follow the directions contained within the Spike app in order to build/modify Loop with Spike. Loop does not natively support Spike app and does not currently plan to. You are responsible for modifying or adapting Loop in order to use Spike so that it is an available option as a CGM source.

## Correction Range
This is where you set your blood glucose range that you would like Loop to correct to. Correction range is not necessarily the same target blood glucose range that you have discussed with your endocrinologist; generally the doctor's range may be much wider. For example, you may keep a correction target of 100-110 for Loop to aim to, but use a desired BG target range of 80-180 when discussing things with your endo about "time in range".

<p align="center">
<img src="../img/premeal_entry.jpg" width="250">
</p>
</br></br>

Click the + in the upper right corner to add correction BG range(s). You can have multiple ranges based on time of day, but the first setting of the day needs to begin at midnight.

Ranges will be entered in mg/dL or mmoL automatically, based upon how your blood glucose values are received. By default they are set to mg/dL, however once CGM values arrive in mmol/L these Loop settings can be entered in mmol/L. **If you are planning to use mmol/L, be sure to wait to set your correction range until after you have started to receive CGM values in Loop.** If you do these in the wrong order, then your chart may have incorrect units. If you come across this issue, you can also remove all of your target ranges and enter them again. Once you are receiving CGM values in mmol/L, you can add your correction range(s) in mmol/L.

Correction ranges can be a single number, such as 100-100 mg/dL.  Generally, you don't want to keep correction ranges too wide otherwise Loop will be sluggish to correct. Most users keep correction range no wider than about 0 to 30 mg/dL between the min and max values.

### Override Ranges
Set the override ranges for temporary alternate correction ranges. These override ranges will only be enacted when you specifically activate pre-meal or workout mode using the buttons on the main Loop display or watchface. While active, they replace the correction range for Loop's recommendations. If the override ranges are not entered in this section, the buttons will remain grey and unusable on the main screen.

**<font color="black">Pre-Meal:</font>**
The pre-meal override target is designed to be used to as an easy way to get a small amount of insulin delivered before a meal in order to help control post-meal blood glucose spikes.

If your normal target is 100-100 mg/dL and pre-meal target is 80-80 mg/dL, for example, Loop will give you an extra push to get you to the lower target number before the meal. This early insulin brings you into the meal with a mini-prebolus. The pre-meal target, when activated by pressing on the icon, will stay active for one hour, until carbs are entered, or until it is manually cancelled...whichever comes first.

Loop will adjust any insulin bolus as needed based on the extra insulin provided during this pre-meal time.

**<font color="black">Workout Mode:</font>**
Workout override target is designed to temporarily set your target higher in anticipation of exercise or other activities which tend to make the user more insulin sensitive or need less insulin. By setting a higher temp target ahead of activity, Loop will recommend less basal rate(s) than normally scheduled in order to to bring blood glucose up to the higher target.

The success of this strategy will be dependent on how far in advance of activity the override target is set. Generally, users set the target approximately 1-2 hours in advance of planned activities, but the optimal timing will depend on the activity, duration, and intensity.  Additionally, any insulin on board from recent boluses may overwhelm the Loop's ability to counteract exercise-induced lows through lower temp basals alone. Please see LoopTips.org for additional information about [exercise and Loop](https://kdisimone.github.io/looptips/how-to/exercise/).

## Suspend Threshold
The suspend threshold must be set up for successful configuration of Loop. **Your Loop will not turn green without setting this value.**  This value affects both bolus and basal recommendations by Loop.

#### Bolus

* If you are trying to bolus a meal while any part of the predicted BG curve is below this suspend threshold value, Loop will not recommend a bolus.  Instead, you will need to wait until your prediction curve is above the suspend threshold value in order to bolus.

#### Basal

* If your current or any point on your predicted BG curve is below the suspend threshold, Loop will always recommend a temporary basal rate of 0 U/hr.

Reasonable settings for suspend threshold will depend on user preference, but recommended not set lower than 65 mg/dL.

## Basal Rates

Your basal rates have already been initially populated from the pump's standard basal schedule as part of your initial setup, above.  Only one basal schedule may be set in each Loop app.  If you need to edit your basal schedule, simply make the edits as needed and then click on `Save to Pump...` button.  As a safety precaution, Loop will not allow you to only save the edits to the Loop app alone...you must successfully save the changes back to the pump to ensure Loop and the pump are in sync.  

!!!info ""
    If you make any basal edits and simply use the `Settings` button to go back to the menu without successfully saving to pump, the changes you made will not be saved in Loop app.  Loop makes saving to pump a mandatory step to successfully editing basal rates.

## Delivery Limits

The maximum basal rate and maximum bolus settings are collectively refered to as Delivery Limits. Your Loop will read these from the pump as part of adding a Medtronic pump to Loop. For safety, similar to basal schedule, you must keep these values the same on both the Loop app and within the pump settings. If you edit these settings in Loop app, always use the `Save to Pump...` button similar to the basal rate edits discussed above.

#### **Maximum Basal Rate**
Maximum basal rate will cap the the maximum temporary basal rate that the Loop is allowed to enact to meet your correction range. When you are first beginning to use Loop, it is wise to start conservative (low) in setting your maximum basal rate. If your settings are incorrect in other areas (basal rates, insulin sensitivity, carb ratio, etc), you may need time to identify where settings need to be adjusted. This process is easier if Loop is given less latitude to set high basal rates. Gradually increase your maximum basal rate as your comfort and confidence in Loop increases. Typically, experienced Loop users set their maximum basal rate around 3-4 times their highest scheduled basal rate. If you need help with your settings adjustment, head over to LoopTips for some [initial settings help](https://kdisimone.github.io/looptips/settings/settings/)

#### **Maximum Bolus**
Enter your desired single bolus maximum here. For safety, don't set a maximum bolus limit any higher than your typical large meal bolus.

## Insulin Model
There are four insulin models to choose from; Walsh, Rapid-Acting Adults, Rapid-Acting Children, and Fiasp. If you want to read the nitty-gritty discussion that went into the development of the Rapid-Acting and Fiasp curves (collectively called "exponential insulin models"), you can see that in GitHub [here](https://github.com/LoopKit/Loop/issues/388#issuecomment-317938473).

We highly recommend selecting one of the exponential insulin models (aka not the Walsh). A common new Loop user error is to select Walsh model in order to easily shorten their insulin duration (DIA) to one like they used prior to Looping. This almost invariably leads to insulin stacking. If you would like to read more about why the duration of insulin action is important in Loop vs how you've traditionally used it, please click [here](https://seemycgm.com/2017/08/09/why-dia-matters/) to read a blog post about the subject. In summary, choosing Walsh curve just to shorten your DIA will lead to insulin stacking and less than desired bolusing recommendations.

You can click on each model and see what each model's insulin activity curve looks like, active one selected in blue. 

<p align="center">
<img src="../img/models.jpg" width="350">
</p>

The differences between the three exponential models (two Rapid-Acting and Fiasp) models has to do with the timing of the peak insulin activity timing. Not surprising, since Fiasp is marketed as the "faster acting" insulin. Currently all the exponential models are defaulted to an insulin duration of 6 hours, but the peak activity of the curves differs:

* Rapid-acting adult curve peaks at 75 minutes
* Rapid-acting child curve peaks at 65 minutes
* Fiasp peaks curve peaks at 55 minutes

## Carb Ratios
Click the + in the upper right to add carb ratios for various times of day. Loop works best if you have [tested and optimized](https://kdisimone.github.io/looptips/settings/settings/) your carb ratio settings for accuracy.

!!!info "Beware of other apps writing carbs to Health app"
    If you are using a third-party app (such as Spike or MyFitness) that can write carbohydrates to the phone's Health app, you will need to edit the permissions to make sure Loop doesn't double carb entries.  You should disable the third-party app's permissions in Health so that they can only `read` and not `write`.  See [Carb Entries with Third Party apps](https://loopkit.github.io/loopdocs/operation/features/carbs/#third-party-apps) for more information about this setting.

## Insulin Sensitivities
Click the + in the upper right to add insulin sensitivities for various times of day. Loop works best if you have [tested and optimized](https://kdisimone.github.io/looptips/settings/settings/) your ISF settings for accuracy. Insulin sensitivities can change for many reasons including waiting too long to change your infusion set. Loop will not auto-detect changes in ISF.

Incorrectly set ISF is the most common cause of roller coaster BGs for new Loop users. You will need to raise (increase) your ISF value/number to help smooth a roller coaster BG trend. You can read about that topic more over in LoopTips [here](https://kdisimone.github.io/looptips/settings/settings/#3rd-insulin-sensitivity-factor). 

## Closed Loop

The Closed Loop switch controls whether Loop automatically enacts its recommended temporary basal adjustments (closed loop operation) or whether you have to manually tap to enact the recommendations (open loop mode).  

<p align="center">
<img src="../img/open_loop.png" width="400">
</p> 

When the Closed Loop switch is in the (Off&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   ) position, Loop WILL NOT enact recommended temp basals automatically. Instead, Loop will display recommended temp basals on the main status display, just above the blood glucose graph.  This is called **open loop**, and is a good way to understand how Loop will function, and what type of recommendations it would make. If you click on the recommended temp basal line while in open loop mode, Loop will implement the temp basal.

<p align="center">
<img src="../img/closed_loop.png" width="400">
</p> 

When the Closed Loop switch is in the (&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   On) position, Loop WILL automatically enact recommended temp basals on the configured insulin pump. This is known as **closed loop**. Typically, Loop will show the recommended temp basal just above the blood glucose graph prior to automatically enacting it. It may take a minute or so for the Loop to enact the recommended basal. Once the temp basal has been enacted successfully on the pump, the recommended temp basal will disappear from the screen and the new temp basal rate will be represented in the insulin delivery graphs.

## Issue Report
If you run into problems or errors with your Loop, an Issue Report can be used to help identify where the problem is occurring. The Issue Report is automatically generated and you can share it via email. Frequently, if you go to Gitter or Facebook for help with a technical problem, an Issue Report will provide insight to what the potential problem is.


