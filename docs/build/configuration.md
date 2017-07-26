# Configuring your Loop

Now that you have the Loop app installed on your iPhone, we need to input the settings so that the Loop can work for you.  In this section, we cover the details and provide information about the Loop displays.  Finally, we will cover some extras like Apple Watch and useful external integrations.

## Health App

Loop app uses the iPhone's Health app to store BG and carbohydrate data.  The Health app will be one of the first prompts that you see as your Loop app is built.  The first prompt will ask if you want to allow the Loop app access to read/write Blood Glucose data into the Health app.  You will want to click on the line that says `Turn All Categories On` and then click on the `Allow` button.

Later in the configuration of your Loop app, when you first setup carb ratios, you will again be prompted whether to allow Loop app access to read/write to the Health app.  This time the access will be for carbohydrate data.  This time you should turn on only the first toggle to allow Loop to write data (not to read data) and click the `Allow` button.  See discussion regarding [Third Party Apps](https://loopkit.github.io/loopdocs/use/carbs/#third-party-apps) for the reasoning behind this selection.

<p align="center">
<img src="../img/healthapp.png" width="450">
</p>

## Settings	 

<p align="center">
<img src="../img/loop_settings.jpg" width="450">
</p> 

Normally, we would start by explaining the displays on an application, but your Loop won’t have much showing initially until we get some basic settings input.  So, let’s start by clicking on the Loop Settings button in the tool bar.  It looks like a little sprocket.


### Loop Version 

<p align="center">
<img src="../img/loop_version.png" width="400">
</p> 

The first graphic at the top of the Loop settings display shows the version of the software, e.g.,  Loop v1.3 in this example.  This can be helpful when working with other users of the software to know what version you are running.

### Closed Loop

The Closed Loop switch controls the Loop operation mode for the application. This operation mode determines whether Loop automatically enacts recommendations (i.e., sets temp basals) to the insulin pump.  

<p align="center">
<img src="../img/open_loop.png" width="400">
</p> 

When the Closed Loop switch is in the (Off&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   ) position, Loop WILL NOT enact recommended temp basals automatically.  Instead, it will display Recommended Temp Basals on the main status display, just above the Glucose graph.  This is called “Open Loop”, and is a good way to understand how Loop will function, and what type of recommendations it would make.  

<p align="center">
<img src="../img/closed_loop.png" width="400">
</p> 

When the Closed Loop switch is in the (&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   On) position, Loop WILL automatically enact recommended temp basals on the configured insulin pump. This is known as a “Closed Loop”.  Typically, Loop will show the recommended temp basal just above the Glucose graph prior to automatically enacting it.  It may take a minute or so for the Loop to enact the recommended basal.  Once the temp basal has been enacted successfully on the pump, the recommended temp basal will disappear from the screen and the new temp basal will be represented in the insulin delivery graphics.

### Preferred Data Source

<p align="center">
<img src="../img/preferred_source.jpg" width="300">
</p> 

If Preferred Data Source is set to “Event History”, then the pump will periodically be polled for treatment events.  This will cause your battery to be used at a faster rate, but there are benefits.  

!!!info ""
    **Event History must be selected for Nightscout to display temp basals, carbs, and boluses from Loop.**  Event History must also be selected in order for prime events to be detected and NOT contribute to iob during site changes.


### Issue Report
If you run into problems or errors with your Loop, the Issue Report can be used to help identify where the problem is occurring.  The Issue Report is automatically generated and you can share it via email.  Frequently, if you go to Gitter or Facebook for help with a technical problem, an Issue Report will provide insight to what the potential problem is.

###Devices
If your RileyLink is turned on and nearby, you will see a RileyLink in this area of the settings (like the first screenshot on this page).  We are going to take care of the RileyLink settings later in this page...for now we are going to skip the RileyLink line.

### Pump ID
Fairly self-explanatory.  You need to enter your pump’s six-digit ID here.  To find your pump ID, press ESC button on the pump, scroll down.  You will find a the six-digit ID as the “S/N#”.  You will also find the same ID on the back of the pump as six numbers beneath the pump’s model number.  There are also explanations so you can identify the pump’s region.  This makes a difference for how the RileyLink will tune its frequency for pump communications.

### Pump Battery Type
Again fairly self-explanatory.  Click which battery type you are using so that the battery percentages are more accurately displayed in your HUD.  The battery displays are designed to give you approximately 8-10 hours notice before looping would fail.  However, every battery manufacturer has its own decay curve for its specific batteries.  Typically, low battery levels will cause looping failures prior to the actual pump failing to delivery insulin. 

### CGM Selection
Select one of the options from the menu:

* Fetch Enlite Data
* G4 Share Receiver
* G5 Transmitter

If you select the G5 Transmitter, you will be prompted to enter the transmitter ID number.  Don't forget to update your transmitter ID when you change transmitters, otherwise your loop will not work.

### Target Range
This is where you set your target blood glucose range.  This is the low and high BG values that Loop will attempt to keep you between.  Click the + in the upper right corner to add target BG range(s).  You can have multiple targets based on time of day, but for safety purposes the first setting of the day should begin at midnight to be consistent with your Medtronic pump.  

Targets will be entered in mg/dl or mmoL automatically based upon how your BG values appear your BG chart. By default they are set to mg/dl, however once BG values arrive in mmoL these settings can be entered in mmoL. If you are planning to use mmoL, be sure to wait to set your target range up until after you have started to receive BG values. If you do these in the wrong order, then your chart may have incorrect Y axis. If you come across this issue, you can also remove all of your target ranges and enter them again. Once you are receiving BG values in mmoL, you can add your Target Range in mmoL.

You can also set the “override” targets here to temporarily use alternate BG targets.  These override targets will only be enacted when you specifically activate “Workout Mode”. 

Target range can be a single number, such as 100-100 mg/dL, but is not necessarily advised or “better”.

### Minimum BG Guard
Minimum BG Guard is a required data entry for successful configuration of Loop. **Your Loop will not turn green without setting this value.**  

Minimum BG Guard allows a user to bolus when their BG is below their target range but not below the value of the Minimum BG Guard.  To help users understand how this setting is affecting their usage of Loop, users will see a new notification icon and details of why there is no recommended bolus if the predicted BG is below the Minimum BG Guard.  

### Insulin Action Duration (DIA)
Enter your insulin action duration here in hours.  This is also called Duration of Insulin Action (DIA).  Typically, close-loopers use between 3-5 hours with good success.  However, your diabetes may vary.  This number is a real number so decimals work here for fractions of hours. Like (3.5) = 3hrs 30 mins

### Basal Rates
Enter your basal rates here.  These should match the values entered in your pump. Entering them here will not override your pump’s values, so make sure they match. This is fairly standard stuff that most T1Ds are already familiar with.  However, if you are new to Medtronic pumps...keep in mind that your insulin needs may change slightly when changing pump systems.  If in doubt, try some basal testing to see if your old basal rates may need adjustments with the switch to Medtronic pumps and infusion sets.

Only one basal pattern may be set in each Loop app.  If you are accustomed to switching between two or more basal patterns frequently, you have two options:

1. manually editing the basal profiles in this area each time you change basals, or
2. installing a duplicate Loop app for each basal pattern and switching when needed.

If you choose to have duplicate Loop apps, you will need to use different MAIN_APP_BUNDLE_IDENTIFIERs for each app.  Additionally, you must remember to close  the unused Loop app (double-click iPhone home button and up-swipe Loop app).  Only one Loop app can run successfully at a time.  When you switch to the new Loop app, it may take 5-15 minutes for the Loop to turn green.  The good news is that all your carb entries, insulin doses and such will automatically populate in the new Loop within a relatively short amount of time and the transition is therefore seamless for Loop functionality.  

### Carb Ratios
Click the + in the upper right to add carb ratios for various times of day. Loop works best if you have tested and optimized your carb ratio settings for accuracy.

The first time you setup carb ratios, you will be prompted to allow Loop app access to write/read data in your iPhone's Health App, choose only the selection for `write` data so that Loop does not inadvertently read third party app's carbohydrate inputs.  See [Carb Entries with Third Party apps](https://loopkit.github.io/loopdocs/use/carbs/#third-party-apps) for more information about this setting.

### Insulin Sensitivities
Click the + in the upper right to add insulin sensitivities for various times of day. Loop works best if you have tested and optimized your ISF settings for accuracy.  Insulin sensitivities can change for many reasons including waiting too long to change your infusion set.  Loop will not auto-detect changes in ISF.

### Maximum Basal Rate
Maximum basal rate is the maximum temporary basal rate that the Loop is allowed to enact to correct to your target BG range.  See the Use section discussion for Close Loop for some suggestions regarding appropriate Maximum Basal Rate.

!!!info ""
    A frequent error for new Loop users is when they set their maximum basal rate here to a value HIGHER than the corresponding setting on the pump.  This will result in an error message that the temp basal failed to enact.  For example, Loop cannot successfully tell the pump to deliver 4 units per hour if the pump’s maximum is set to only 3.8 units per hour.  If you are seeing failures of the Loop to set a high temp basal, check to see if your pump’s maximum basal is at greater than or equal to the Loop’s maximum basal.

### Maximum Bolus
Enter your desired single bolus maximum here.

## Services
The services listed in this section are **OPTIONAL**.  You can choose to leave them empty and your Loop will still work.  

### Nightscout
If you have an existing Nightscout site, add the Site URL and API Secret to have your Loop data transmitted to your Nightscout site. If you can’t remember your API Secret, it can be found under Settings, Reveal Config Vars for Heroku sites (or Application Settings, Connection Strings for Azure sites). 

### mLab
mLab is a cloud-hosted Mongo Database service.  mLab is used by Loop as a remote repository of Loop status data.  This data is very helpful if you having issues with Loop and need to see remotely what Loop is doing and get diagnostics. If you already have a Nightscout site, you can use your existing mLab database.  As the screen shot below shows, this integration will log the errors from your Loop app and help you troubleshoot if you notice a pattern of problems.

<p align="center">
<img src="../img/mlab_errors.jpg" width="500">
</p> 

**To get your database name:**

If you have Nightscout, access your mLab.  If you manually built your mLab database, you can login to mLab [here](http://mlab.com).  If you had Heroku automatically deploy your site, you can access mLab from your Heroku dashboard. Find the screen, like shown below, to get your database name.  The database name is the part after the “dsXXXXXXX/”.  In this case, “annat1d”  

<p align="center">
<img src="../img/mlab_dbname.jpg" width="500">
</p> 

**To obtain your API Key:**


1) Click your username (not the account name) in the upper right-hand corner to open your account user profile

2) If you are already in the account details page, then click on the row with your username in the Account Users section

3) If the status is showing as “Data API Access: Disabled” in the “API Key” section, click the “Enable Data API access” button

4) Once Data API access is enabled, your current API key will be displayed in the “API key”

If you have any problems with integration, you can try regenerating the API key and that should solve the problem.

<p align="center">
<img src="../img/mlab_api.jpg" width="500">
</p> 

### Loggly
[Loggly](https://loggly.com) is a free logging service.  If you sign up for an account, you'll need to go under Source Setup and then Customer Tokens.  Copy and paste your customer token into your Loop App settings for Loggly.

<p align="center">
<img src="../img/loggly.png" width="500">
</p> 

### Amplitude
[Amplitude](https://amplitude.com) is a remote event monitoring service and can be used to quickly identify errors and events with Loop.  Amplitude stores the events and allows you to view those events as points in time.  To retrieve the details of the events you will need to look at corresponding mLab data entries to get a complete picture of the issues.  If you sign up for a free account with Amplitude, you will be given an API Key that you can enter here to have Loop integration setup.

<p align="center">
<img src="../img/amplitude.png" width="500">
</p> 

## RileyLink
RileyLink is turned on with a little switch on the side of the circuit board (little blue lights will flash briefly and then turn off).  The “on” position is with the switch towards the battery plug.  Now that you have it turned on, go back to your Loop settings and under “Devices”, there will be a connection to turn on.  Turn it on (slide to green) and then click on the arrow to the right of the green slider to open the RileyLink settings area.  Your RileyLink will now have a solid green light showing.  The solid green light indicates a working bluetooth connection with your iPhone. 

### Device  
The settings under the Device section are mostly for your information only.  However, you can rename your RileyLink to something more unique.  This is a good idea if you own more than one or are ever in the presence of more than one RileyLink...you will be able to pick out your connection easier amongst a crowd of “RileyLinks”.

The `Signal Strength` showing under this area of the menu is the signal strength of the BT with the iPhone.  It is **not** the signal strength of the radio communications with the pump.

### Pump
The Pump ID should be automatically filled in from the setting you have already entered previously.  The pump model will say unknown until we proceed with “Tune Radio Frequency.” 

### Commands
* Tune Radio Frequency: Choose “Tune Radio Frequency”.  It may take about a minute, but soon you will see a list of frequencies and you can exit back to the main RileyLink settings.  The Command line will now show the frequency (916.xx MHz) in the first command line and the timestamp of the tune.  Now your pump and RileyLink are tuned to talk to each other.  When people suggest "did you retune your RileyLink?" they are referring to this line's command.

(Note: for the rest of these items you may first need to set a Remote ID as discussed in the Pump Setup below.)

* Change Time:  Choose “change time” so that pump and Loop times will match exactly.  

!!!warning ""
    **You should never use the pump itself to set the pump’s time.**  Always use the RileyLink to set pump time.

* MySentry Pair:  MySentry Pairing is for x23 and x54 pumps.  Follow the directions as shown in the RileyLink command screen for MySentry.  You do not have to worry about this command if you are using an x15 or x22 model pump, as they do not have MySentry.  

!!!info ""
    **If you do not perform a MySentry pairing and have an x23 or x54 pump, your loop will only turn green every 15 minutes.**

* Fetch Recent History, Fetch Recent Glucose, Write Glucose History Timestamp, Get Pump Model, and Send Button Press, Read Pump Status, and Read Basal Schedule are all ways of asking the pump for information you might be interested in.  They are not part of setting up the Loop.  Send Button Press can be useful to see if the communication between the RileyLink and pump is working.  If successful, the screen on the pump will light up and Loop will confirm the button press with a “success” message.  Read Pump Status is also nice quick pump read for reservoir volume, pump battery voltage, and pump status (bolusing or suspending).

## Pump Setup
Now that you are done with your Loop app settings, you need to finish setting up your pump for Loop use.  Generally, the setup of the pump is similar to setting up any pump for non-looping use.  One notable exception: you will need to change those batteries more often with Looping.  Loop will drain pump batteries much faster than regular pump regimes, and Loop failures will increase in frequency as the pump battery gets low.}

While not every setting NEEDS to match between Loop and pump, it is safer to have them match in case your Loop fails and you revert back to normal pump use.  You should program the pump settings to match for:

* Basal program(s)
* Carb ratio
* ISF
* Max bolus
* Insulin action duration
* BG targets

!!!info ""
    **Three settings in particular need to be done, OR ELSE YOUR LOOP WON'T WORK:**</br></br>
        * Set “max temp basal” in pump to at least equal to (or slightly greater) than the Loop’s max basal</br></br>
        * Set “temp basal type” to “insulin rate (u/h)”</br></br>
        * Set Remote ID to "on" and enter any random ID (000000 will work). This is found in the pump's Utilities (for x23 continue to Connect Devices, Remotes) and turn ON the Remote Options.</br>


CONGRATS...your Loop is ready for use.  But are you?  Have you read through the algorithm?  Have you watched the pump in open loop mode?  Have you read about how to safely do site changes and priming?  Do you know how to troubleshoot your Loop?  Please take the time to read the other sections of this guide as they will help you navigate safe looping practices.
