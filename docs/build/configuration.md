# Configuring your Loop app

Now that you have the Loop app installed on your iPhone, we need to input the settings so that the Loop can work for you.  In this section, we cover the details and provide information about the Loop displays.  Finally, we will cover some extras like Apple Watch and useful external integrations.

## Loop Settings	 

Normally, we would start by explaining the displays on an application, but your Loop won’t have much showing initially until we get some basic settings input.  So, let’s start by clicking on the logo at the bottom right of the Loop application.  It looks like a little sprocket.  That’s the Loop settings.

### Loop Version 

The first graphic at the top of the Loop settings display shows the version of the software, e.g.,  LOOP v1.1 in this example.  This can be helpful when working with other users of the software to know what version you are running.


### Closed Loop
The Closed Loop switch controls the Loop operation mode for the application. This operation mode determines whether Loop automatically enacts recommendations (i.e., sets temp basals) to the insulin pump.

When the Closed Loop switch is in the (Off   ) position, Loop WILL NOT enact recommended temp basals automatically.  Instead, it will display Recommended Temp Basals on the main status display, just above the Glucose graph.  This is called “Open Looping”, and is a good way to understand how Loop will function, and what type of recommendations it would make.

When the Closed Loop switch is in the (   On) position, Loop WILL automatically enact recommended temp basals on the configured insulin pump. This is known as a “Closed Loop”.  Typically, Loop will show the recommended temp basal just above the Glucose graph prior to automatically enacting it.  It may take a minute or so for the Loop to enact the recommended basal.  Once the temp basal has been enacted successfully on the pump, the recommended temp basal will disappear from the screen and the new temp basal will be represented in the insulin delivery graphics.

### Preferred Data Source
If Preferred Data Source is set to “Event History”, then the pump will periodically be polled for treatment events.  This will cause your battery to be used at a faster rate, but will allow Loop to upload “treatments” to Nightscout. Event History must be selected for Nightscout to display temp basals, carbs, and boluses from Loop.

Even with Preferred Data Source set to “Event History”, the reservoir volume will still be used to determine IOB, except in a few cases, such as when reservoir volumes have increased (in other words, reservoir was changed or refilled), or when the reservoir history is missing a half hour of data.

Event History = 	More Accurate Treatment Data, and Upload of Treatments to Nightscout

Reservoir = 	Improved pump battery economy by using MySentry data for Reservoir Readings 
		(battery improvement only on x23 and higher pumps with MySentry)

### Issue Report
If you run into problems or errors with your Loop, the Issue Report can be used to help identify where the problem is occurring.  The Issue Report is automatically generated and you can share it via email.  Frequently, if you go to Gitter for help with a technical problem, an Issue Report will provide insight to what the potential problem is.

### Configuration
This section of Loop settings should be fairly familiar for most T1D’s who are familiar with pumping.  

#### Pump ID
Fairly self-explanatory.  You need to enter your pump’s six-digit ID here.  To find your pump ID, press ESC button on the pump, scroll down.  You will find a the six digit ID as the “S/N#”.  You will also find the same ID number on the back of the pump as six numbers beneath the pump’s model number.  There are also explanations so you can identify if the pump’s region.  This makes a difference for how the RileyLink will tune its frequency for pump communications.

#### G5 Transmitter ID
This field only needs to be filled in if you are using a Dexcom G5 system.  You can find your G5 transmitter ID either on the box the transmitter came in, from the Share2 app, or from the G5 receiver menu under Settings>Device Info.  Do not enter a G4 transmitter ID here.  

#### G4 Share Receiver
If you are using a Dexcom G4 system, you can turn the G4 share receiver, allowing Loop to pickup the bluetooth data directly from the receiver’s signal. When functioning correctly this will allow Loop to operate without a data connection (sometimes called Camping Mode).

#### Target Range
This is where you set your target blood glucose range.  This is the low and high BG values that Loop will attempt to keep you between.  Click the + in the upper right corner to add target BG range(s).  You can have multiple targets based on time of day, but for safety purposes the first setting of the day should begin at midnight to be consistent with your Medtronic pump.  

Targets will be entered in mg/dl or mmoL automatically based upon how your BG values appear your BG chart. By default they are set to mg/dl, however once BG values arrive in mmoL these settings can be entered in mmoL. If you are planning to use mmoL, be sure to wait to set your target range up until after you have started to receive BG values. If you do these in the wrong order, then your chart may have incorrect Y axis. If you come across this issue, you can also remove all of your target ranges and enter them again. Once you are receiving BG values in mmoL, you can add your Target Range in mmoL.

You can also set the “override” targets here to temporarily use alternate BG targets.  These override targets will only be enacted when you specifically activate “Workout Mode” (see Section 5.2.4)

When initially setting up the Loop, it may be safer to start with a slightly higher target range than you may normally use.  This safety factor helps prevent lows in case your basals or other T1D-specific inputs were not well-determined prior to using Loop.  Slowly adjust the target BG range as you become more comfortable with the Loop’s performance and refine your T1D inputs.  

Loop uses the target range settings as follows:

Low end of range - Minimum BG Target Guard. If your BG is currently below this number Loop will not suggest a bolus under any circumstance (see Section 5.1.5.5 for configuring this safety feature)

High end of range - Target BG for any bolus wizard recommendation in Loop

Additionally, Loop calculates the middle of your range  [(High end - Low end) / 2] and uses that value as the target BG for any temporary basal suggestions.

Loop will only suggest a temporary basal if your BG is out-of-range or expected to be out-of-range at the end of any currently active IOB. 

Target range can be a single number, such as 100-100 mg/dL, but is not necessarily advised or “better”.
5.1.5.5 Minimum BG Guard (Loop v1.3 or Greater)
Minimum BG Guard is a required data entry for successful configuration of Loop.  This feature was added in Loop version v1.3 and later.  The Minimum BG guard is a Blood Glucose value setting.  When the current or forecasted Blood Glucose is below the set value, Loop will not recommend a bolus, and will issue temp basal rates of 0U/hr.  

Minimum BG Guard allows a user to issue a Bolus when their BG is below their “Target Range” but not below the value of the BG Guard.  To help users understand how this setting is affecting their usage of Loop.  Users will see a new notification icon and details of why there is no Recommended Bolus if the predicted BG is Below the Minimum BG Guard. 


#### Insulin Action Duration (DIA)
Enter your insulin action duration here in hours.  This is also called Duration of Insulin Action (DIA).  Typically, close-loopers use between 3-4 hours with good success.  However, your diabetes may vary.  This number is a real number so decimals work here for fractions of hours. Like (2.5) = 2hrs 30 mins

#### Basal Rates
Enter your basal rates here.  These should match the values entered in your pump. Entering them here will not override your pump’s values, so make sure they match. This is fairly standard stuff that most T1Ds are already familiar with.  However, if you are new to Medtronic pumps...keep in mind that your insulin needs may change slightly when changing pump systems.  If in doubt, try some basal testing to see if your old basal rates may need adjustments with the switch to Medtronic pumps and infusion sets.

Only one basal pattern may be set in each Loop app.  If you are accustomed to switching between two or more basal patterns frequently, you have two options (1) manually editing the basal profiles in this area each time you change basals or (2) installing a duplicate Loop app for each basal pattern.  Which option you choose is a personal choice, both work just fine.

If you choose to have duplicate Loop apps, you will need to use different MAIN_APP_BUNDLE_IDENTIFIERs for each app.  Additionally, you must remember to close (double click iPhone home button and up-swipe) the unused Loop app.  Only one Loop app can run successfully at a time.  When you switch to the new Loop app, it may take 5-15 minutes for the Loop to turn green.  The good news is that all your carb entries, insulin doses and such will automatically populate in the new Loop within a relatively short amount of time and the transition is therefore seamless for Loop functionality.  

#### Carb Ratios
Click the + in the upper right to add carb ratios for various times of day. Loop works best if you have tested and optimized your carb ratio settings for accuracy.

#### Insulin Sensitivities
Click the + in the upper right to add insulin sensitivities for various times of day. Loop works best if you have tested and optimized your ISF settings for accuracy.

Insulin sensitivities can change for many reasons including waiting too long to change your infusion set.  Loop will not auto-detect changes in ISF.

#### Maximum Basal Rate
Maximum basal rate is the maximum temporary basal rate that the Loop is allowed to enact to correct to your target BG range.  

When you are first beginning to use Loop, it is important to be conservative (low) in setting your maximum basal rate.  If your settings are incorrect in other areas (basal rates, carb absorption time, carb ratio, etc), the Loop may enact incorrectly aggressive high temp basals.  Gradually increase your maximum basal rate as your comfort and confidence in Loop increase.  Typically, experienced closed loop users set their max basal rate no more than 3-4 times their average basal rate.  

NOTE:  A frequent error for new Loop users is when they set their maximum basal rate here to a value HIGHER than the corresponding setting on the pump.  This will result in an error message that the temp basal failed to enact.  For example, Loop cannot successfully tell the pump to deliver 4 units per hour if the pump’s maximum is set to only 3.8 units per hour.  If you are seeing failures of the Loop to set a high temp basal, check to see if your pump’s maximum basal is at greater than or equal to the Loop’s maximum basal.

#### Maximum Bolus
Enter your desired single bolus maximum here.

#### Retrospective Correction
There is a separate setting to allow Loop to adjust temporary basal rates based upon a retrospective look back at what Loop thought your BG would be (now) 30 minutes ago. This is default to off.  To learn more and how to turn on, see section 5.2.1.2.1

### Services
The services listed in this section are optional.  You can choose to leave them empty and your Loop will still work.  

#### Dexcom Share
Adding your Dexcom Share account information here will allow Loop to pull CGM data from the Dexcom servers in the event the Loop is not able to pull the data directly from the G4 receiver.  When Loop is receiving CGM data using this option, a little cloud icon will appear on the CGM reading in the Loop’s mainscreen.

#### Nightscout
If you have an existing Nightscout site, add the Site URL and API Secret to have your Loop data transmitted to your Nightscout site. If you can’t remember your API Secret, it can be found under Settings, Reveal Config Vars for Heroku sites (or Application Settings, Connection Strings for Azure sites). 

For additional information about how to configure your Nightscout site for Loop use, please see Section 5.4.1 or the Loop Wiki page for Nightscout with Loop.

#### mLab
Enter your database name and API Key here.  For information about how to set-up mLab, please see Section 5.4.2.

#### Amplitude
Enter your API Key and click “add account”.  For information about how to setup Amplitude, please see Section 5.4.3

### RileyLink Setup
If you ordered your RileyLink preassembled, you should plug in the battery cable.  Please make sure your RileyLink’s battery cable is securely pushed all the way into the socket.  Poor battery cable connection can make the Loop communications fail.

RileyLink with loose battery cable.

RileyLink with properly secured battery cable.

RileyLink is turned on with a little switch on the side of the circuit board (little blue lights will flash briefly and then turn off).  The “on” position is with the switch towards the battery plug.  Now that you have it turned on, go back to your Loop settings and under “Devices”, there will be a connection to turn on.  Turn it on (slide to green) and then click on the arrow to the right of the green slider to open the RileyLink settings area.  {Note: your RileyLink will now have a solid green light showing.  The solid green light indicates a working bluetooth connection with your iPhone.}


#### Device  
The settings under the Device section are mostly for your information only.  However, you can rename your RileyLink to something more unique.  This is a good idea if you own more than one or are ever in the presence of more than one RileyLink...you will be able to pick out your connection easier amongst a crowd of “RileyLinks”

#### Pump
The Pump ID should be automatically filled in from the setting you have already entered previously.  The pump model will say unknown until we proceed with “Tune Radio Frequency.” 

#### Commands
Tune Radio Frequency: Choose “Tune Radio Frequency”. (This may be seen as Settings/Commands/916.65MHz with a right arrow to enter the screen.)  It may take about a minute, but soon you will see a list of frequencies and you can exit back to the main RileyLink settings.  The Command line will now show the frequency (916.60 MHz in this case) in the first command line and the timestamp of the tune.  Now your pump and RileyLink are tuned to talk to each other.

Note:  The strength of the radio communications with the pump is shown by the last number of the tune.  Tuning with -99 means NO communications were established.  Generally, if you have tuning in the -90s, your RileyLink-pump communications will not work.  If you have tuning in the -80s, you may have periodic communication failures.  If your tuning is in the -70s or better, your communications should be pretty stable.

(Note: for the rest of these items you may first need to set a pump Remote ID as per section 5.1.8, if you haven’t already.)

Change Time:  Choose “change time” so that pump and Loop times will match exactly.  You should never use the pump itself to set the pump’s time.  Use the RileyLink and Loop app.

MySentry Pair:  MySentry Pairing is for x23 and x54 pumps.  Follow the directions on the iPhone screen.  You do not have to worry about this command if you are using an x15 or x22 model pump, as they do not have MySentry.

Fetch Recent History, Fetch Recent Glucose, Get Pump Model, and Send Button Press are all ways of asking the pump for information you might be interested in.  They are not part of setting up the Loop.  Send Button Press can be useful to see if the communication between the RileyLink and pump is working.  If successful, the screen on the pump will light up and Loop will confirm the button press with a “success” message.
5.1.8 Insulin Pump Setup
Now that you are done with your Loop app setup, you need to finish setting up your pump for Loop use.  Generally, the setup of the pump is similar to setting up any pump for non-looping use.  {Except, you will need to change those batteries more often with Looping.  Loop will drain pump batteries much faster than regular pump regimes, and Loop failures will increase in frequency as the pump battery gets low.}

While not every setting NEEDS to match between Loop and pump, it is safer to have them match in case your Loop fails and you revert back to normal pump use.  You should program the pump settings to match for:

Basal program(s)
Carb ratio
ISF
Max bolus
Insulin action duration
BG targets

Two settings in particular should be noted:
Set “max temp basal” in pump to at least equal to (or slightly greater) than the Loop’s max basal
Set “temp basal type” to “insulin rate (u/h)”
 
For all pumps, press ACT, scroll down to Utilities (for x23 continue to Connect Devices, Remotes) and turn ON the Remote Options.  Add a Remote ID of any 6 numbers.  It can be “000000”, doesn’t matter.

CONGRATS...your Loop is setup.

Please, as you move forward with Loop use, keep safety and patience in mind.  Moving conservatively, as you learn the way Loop makes its recommendations, is best.  
