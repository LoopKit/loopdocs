# Configuring your Loop

Now that you have the Loop app installed on your iPhone, we need to input the settings so that the Loop can work for you.  In this section, we cover the details and provide information about the Loop displays.  Finally, we will cover some extras like Apple Watch and useful external integrations.

## Settings	 
<p align="center">
<img src="img/toolbar.jpg" width="400">
</p> 

Normally, we would start by explaining the displays on an application, but your Loop won’t have much showing initially until we get some basic settings input.  So, let’s start by clicking on the Loop Settings button in the tool bar.  It looks like a little sprocket.

### Loop Version 

<p align="center">
<img src="img/loop_version.jpg" width="400">
</p> 

The first graphic at the top of the Loop settings display shows the version of the software, e.g.,  Loop v1.1 in this example.  This can be helpful when working with other users of the software to know what version you are running.

### Closed Loop

The Closed Loop switch controls the Loop operation mode for the application. This operation mode determines whether Loop automatically enacts recommendations (i.e., sets temp basals) to the insulin pump.  

<p align="center">
<img src="img/open_loop.png" width="400">
</p> 

When the Closed Loop switch is in the (Off   ) position, Loop WILL NOT enact recommended temp basals automatically.  Instead, it will display Recommended Temp Basals on the main status display, just above the Glucose graph.  This is called “Open Loop”, and is a good way to understand how Loop will function, and what type of recommendations it would make.  

<p align="center">
<img src="img/closed_loop.png" width="400">
</p> 

When the Closed Loop switch is in the (   On) position, Loop WILL automatically enact recommended temp basals on the configured insulin pump. This is known as a “Closed Loop”.  Typically, Loop will show the recommended temp basal just above the Glucose graph prior to automatically enacting it.  It may take a minute or so for the Loop to enact the recommended basal.  Once the temp basal has been enacted successfully on the pump, the recommended temp basal will disappear from the screen and the new temp basal will be represented in the insulin delivery graphics.

### Preferred Data Source

<p align="center">
<img src="img/preferred_source.jpg" width="300">
</p> 

If Preferred Data Source is set to “Event History”, then the pump will periodically be polled for treatment events.  This will cause your battery to be used at a faster rate, but will allow Loop to upload “treatments” to Nightscout. **Event History must be selected for Nightscout to display temp basals, carbs, and boluses from Loop.**

Even with Preferred Data Source set to “Event History”, the reservoir volume will still be used to determine IOB, except in a few cases, such as when reservoir volumes have increased (in other words, reservoir was changed or refilled), or when the reservoir history is missing at least 30 minutes of continuous readings.

Event History = More Accurate Treatment Data, and Upload of Treatments to Nightscout

Reservoir = Improved pump battery economy by using MySentry data for Reservoir Readings (x23 pumps only) 

### Issue Report
If you run into problems or errors with your Loop, the Issue Report can be used to help identify where the problem is occurring.  The Issue Report is automatically generated and you can share it via email.  Frequently, if you go to Gitter or Facebook for help with a technical problem, an Issue Report will provide insight to what the potential problem is.

### Pump ID
Fairly self-explanatory.  You need to enter your pump’s six-digit ID here.  To find your pump ID, press ESC button on the pump, scroll down.  You will find a the six digit ID as the “S/N#”.  You will also find the same ID number on the back of the pump as six numbers beneath the pump’s model number.  There are also explanations so you can identify if the pump’s region.  This makes a difference for how the RileyLink will tune its frequency for pump communications.

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

When initially setting up the Loop, it may be safer to start with a slightly higher target range than you may normally use.  This safety factor helps prevent lows in case your basals or other T1D-specific inputs were not well-determined prior to using Loop.  Slowly adjust the target BG range as you become more comfortable with the Loop’s performance and refine your T1D inputs.   

Target range can be a single number, such as 100-100 mg/dL, but is not necessarily advised or “better”.

### Minimum BG Guard (Loop v1.3 or newer)
Minimum BG Guard is a required data entry for successful configuration of Loop.  This feature was added in Loop version v1.3 and later.  **Your Loop will not turn green without setting this value.**  

Minimum BG Guard allows a user to bolus when their BG is below their “Target Range” but not below the value of the Minimum BG Guard.  To help users understand how this setting is affecting their usage of Loop, users will see a new notification icon and details of why there is no recommended bolus if the predicted BG is below the Minimum BG Guard.  

### Insulin Action Duration (DIA)
Enter your insulin action duration here in hours.  This is also called Duration of Insulin Action (DIA).  Typically, close-loopers use between 3-4 hours with good success.  However, your diabetes may vary.  This number is a real number so decimals work here for fractions of hours. Like (2.5) = 2hrs 30 mins

### Basal Rates
Enter your basal rates here.  These should match the values entered in your pump. Entering them here will not override your pump’s values, so make sure they match. This is fairly standard stuff that most T1Ds are already familiar with.  However, if you are new to Medtronic pumps...keep in mind that your insulin needs may change slightly when changing pump systems.  If in doubt, try some basal testing to see if your old basal rates may need adjustments with the switch to Medtronic pumps and infusion sets.

Only one basal pattern may be set in each Loop app.  If you are accustomed to switching between two or more basal patterns frequently, you have two options:

1. manually editing the basal profiles in this area each time you change basals, or
2. installing a duplicate Loop app for each basal pattern and switching when needed.

If you choose to have duplicate Loop apps, you will need to use different MAIN_APP_BUNDLE_IDENTIFIERs for each app.  Additionally, you must remember to close  the unused Loop app (double-click iPhone home button and up-swipe Loop app).  Only one Loop app can run successfully at a time.  When you switch to the new Loop app, it may take 5-15 minutes for the Loop to turn green.  The good news is that all your carb entries, insulin doses and such will automatically populate in the new Loop within a relatively short amount of time and the transition is therefore seamless for Loop functionality.  

### Carb Ratios
Click the + in the upper right to add carb ratios for various times of day. Loop works best if you have tested and optimized your carb ratio settings for accuracy.

### Insulin Sensitivities
Click the + in the upper right to add insulin sensitivities for various times of day. Loop works best if you have tested and optimized your ISF settings for accuracy.  Insulin sensitivities can change for many reasons including waiting too long to change your infusion set.  Loop will not auto-detect changes in ISF.

### Maximum Basal Rate
Maximum basal rate is the maximum temporary basal rate that the Loop is allowed to enact to correct to your target BG range.  

When you are first beginning to use Loop, it is important to be conservative (low) in setting your maximum basal rate.  If your settings are incorrect in other areas (basal rates, carb absorption time, carb ratio, etc), the Loop may enact incorrectly aggressive high temp basals.  Gradually increase your maximum basal rate as your comfort and confidence in Loop increase.  Typically, experienced closed loop users set their max basal rate no more than 3-4 times their average basal rate.  

NOTE:  A frequent error for new Loop users is when they set their maximum basal rate here to a value HIGHER than the corresponding setting on the pump.  This will result in an error message that the temp basal failed to enact.  For example, Loop cannot successfully tell the pump to deliver 4 units per hour if the pump’s maximum is set to only 3.8 units per hour.  If you are seeing failures of the Loop to set a high temp basal, check to see if your pump’s maximum basal is at greater than or equal to the Loop’s maximum basal.

### Maximum Bolus
Enter your desired single bolus maximum here.

## Services
The services listed in this section are optional.  You can choose to leave them empty and your Loop will still work.  

#### Dexcom Share
Adding your Dexcom Share account information here will allow Loop to pull CGM data from the Dexcom servers in the event the Loop is not able to pull the data directly from the G4 receiver.  When Loop is receiving CGM data using this option, a little cloud icon will appear on the CGM reading in the Loop’s mainscreen.

#### Nightscout
If you have an existing Nightscout site, add the Site URL and API Secret to have your Loop data transmitted to your Nightscout site. If you can’t remember your API Secret, it can be found under Settings, Reveal Config Vars for Heroku sites (or Application Settings, Connection Strings for Azure sites). 

For additional information about how to configure your Nightscout site for Loop use, please see the Nightscout section of these docs.

#### mLab
Enter your database name and API Key here.  

#### Amplitude
Enter your API Key and click “add account”.

## RileyLink
If you ordered your RileyLink preassembled, you should plug in the battery cable.  Please make sure your RileyLink’s battery cable is securely pushed all the way into the socket.  Poor battery cable connection can make the Loop communications fail.

RileyLink with loose battery cable.

RileyLink with properly secured battery cable.

RileyLink is turned on with a little switch on the side of the circuit board (little blue lights will flash briefly and then turn off).  The “on” position is with the switch towards the battery plug.  Now that you have it turned on, go back to your Loop settings and under “Devices”, there will be a connection to turn on.  Turn it on (slide to green) and then click on the arrow to the right of the green slider to open the RileyLink settings area.  {Note: your RileyLink will now have a solid green light showing.  The solid green light indicates a working bluetooth connection with your iPhone.}

### Device  
The settings under the Device section are mostly for your information only.  However, you can rename your RileyLink to something more unique.  This is a good idea if you own more than one or are ever in the presence of more than one RileyLink...you will be able to pick out your connection easier amongst a crowd of “RileyLinks”

### Pump
The Pump ID should be automatically filled in from the setting you have already entered previously.  The pump model will say unknown until we proceed with “Tune Radio Frequency.” 

### Commands
* Tune Radio Frequency: Choose “Tune Radio Frequency”. (This may be seen as Settings/Commands/916.65MHz with a right arrow to enter the screen.)  It may take about a minute, but soon you will see a list of frequencies and you can exit back to the main RileyLink settings.  The Command line will now show the frequency (916.60 MHz in this case) in the first command line and the timestamp of the tune.  Now your pump and RileyLink are tuned to talk to each other.

Note:  The strength of the radio communications with the pump is shown by the last number of the tune.  Tuning with -99 means NO communications were established.  Generally, if you have tuning in the -90s, your RileyLink-pump communications will not work.  If you have tuning in the -80s, you may have periodic communication failures.  If your tuning is in the -70s or better, your communications should be pretty stable.

(Note: for the rest of these items you may first need to set a pump Remote ID as per section 5.1.8, if you haven’t already.)

* Change Time:  Choose “change time” so that pump and Loop times will match exactly.  You should never use the pump itself to set the pump’s time.  Use the RileyLink and Loop app.

* MySentry Pair:  MySentry Pairing is for x23 and x54 pumps.  Follow the directions on the iPhone screen.  You do not have to worry about this command if you are using an x15 or x22 model pump, as they do not have MySentry.

* Fetch Recent History, Fetch Recent Glucose, Get Pump Model, and Send Button Press are all ways of asking the pump for information you might be interested in.  They are not part of setting up the Loop.  Send Button Press can be useful to see if the communication between the RileyLink and pump is working.  If successful, the screen on the pump will light up and Loop will confirm the button press with a “success” message.

## Pump Setup
Now that you are done with your Loop app settings, you need to finish setting up your pump for Loop use.  Generally, the setup of the pump is similar to setting up any pump for non-looping use.  {Except, you will need to change those batteries more often with Looping.  Loop will drain pump batteries much faster than regular pump regimes, and Loop failures will increase in frequency as the pump battery gets low.}

While not every setting NEEDS to match between Loop and pump, it is safer to have them match in case your Loop fails and you revert back to normal pump use.  You should program the pump settings to match for:

* Basal program(s)
* Carb ratio
* ISF
* Max bolus
* Insulin action duration
* BG targets

**Three settings in particular need to be done, OR ELSE YOUR LOOP WON'T WORK:
* Set “max temp basal” in pump to at least equal to (or slightly greater) than the Loop’s max basal
* Set “temp basal type” to “insulin rate (u/h)”
* Set Remote ID to "on" and enter any random ID (000000 will work). This is found in the pump's Utilities (for x23 continue to Connect Devices, Remotes) and turn ON the Remote Options.
**

CONGRATS...your Loop is ready for use.  But are you?  Have you read through the algorithm?  Have you watched the pump in open loop mode?  Have you read about how to safely do site changes and priming?  Do you know how to troubleshoot your Loop?  Please take the time to read the other sections of this guide as they will help you navigate safe looping practices.
