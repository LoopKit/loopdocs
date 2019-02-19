## Code Customizations
Based on Loop users’ experience, there are some customizations that you may want to incorporate ahead of building your Loop app and Apple Watch app.  These customizations must be done prior to building the Loop app onto your iPhone, they cannot be done from within the app itself.

!!!info ""
    Note: Every effort will be made to update the line numbers as the code is updated, but there may be times where the screenshots and line numbers are slightly different than the current version of Loop code.  These instructions have been updated for Loop v1.9.4.
    

### Disable Siri Capabilities

Free developer accounts will not be able to build Loop app while Siri capabilities are turned on.  In order to turn those features off, you will need to remove the Siri entitlements manually.

In the upper left toolbar of Xcode is a "find" option (magnifying glass just below the build - play button), search for 'Siri'.  Two files will be returned; Loop.entitlements and WatchApp Extension.entitlements.  For each of those files, you will need to click on the file name and then delete the Siri Entitlements files by clicking on the minus sign to the right of the word "Siri". Once you delete the Siri entitlement in those two files, you'll be able to sign the four targets and build with the free developer account.

<p align="center">
<img src="../img/siri-free.png" width="750">
</p>

### Disable Authentication for Bolusing

Depending on your iPhone preferences and model, you may have Face ID or Touch ID enabled.  Those security features will also be used to authenticate bolus delivery in Loop.  You can choose to disable authentication (i.e., not require Face ID, Touch ID, or passcode for bolusing) through the following code customization:

 Modify Line 191 in the Loop>>View Controllers>>BolusViewController.swift.  Add the `false &&` as shown in the screenshot below:

<p align="center">
<img src="../img/custom-id.png" width="750">
</p>

### Workout Range Duration

<img style="float: right;" width="200" src="../img/workout_default.png">
If you’d like more than just the standard 1 or 2 hour duration for the Workout Range, you can add or modify the code to add another time interval or edit the existing ones.

Go to the Loop>>Extensions>>UIAlertController.swift and modify Line 32.  The default has 1 and 2 hours as shown where the arrow is pointing in the screenshot.  You can edit those to whatever duration you want (in units of hours) and add a duration if you prefer.  If you’d like 1, 2, and 3 hours options...simply edit the numbers in the brackets to read [1, 2, 3]. It is possible to enter less than 1 hour intervals such as 15 min, 30 min, 45 min by editing the brackets to read [0.25, 0.5, 0.75].

<p align="center">
<img src="../img/workout_add.png" width="750">
</p>

### Default Carb Absorption Times

<img style="float: right;" width="200" src="../img/carb_screen.png">

Loop’s default carb absorption times are based on the high, medium, and low glycemic index absorption curves presented in <i>Think Like A Pancreas</i> by Gary Scheiner.  Currently the lollipop icon is set for 2 hours, taco icon for 3 hours, and pizza icon for 4 hours.  

You can modify these defaults to suit your needs, however modification of these values it not as helpful/common as previous Loop versions.  Ever since Loop v1.4, Loop has included dynamic carb absorption means that Loop will start with your entered carb absorption time, multiply it by 1.5, and then dynamically adjust the absorption time (either shorter or longer) based on the observed BG impacts.  So, typically, most people are finding that modification of the default carb absorption times is no longer necessary.

If you would like to modify those defaults, you can do so in the Loop>>Managers>>LoopDataManager.swift Lines 65-67.  Note the times are in hours, not minutes, in the code.

<p align="center">
<img src="../img/carb_times.png" width="750">
</p>

### Neutral Temp Basals

With the default installation, when Loop calculates that the recommended temp basal matches the basal rate in your Loop basal rate schedule (aka "neutral temp basal") rather than setting a temp basal, Loop will cancel any currently running temp basal and let the pump just run the scheduled basal.  Assuming you are using Loop v1.9.3 and the "save to pump..." command to make basal rate schedule edits, Loop and the pump will be matching and this will not cause any issues.

If you would like Loop to instead set neutral temp basals, you can edit lines 151 and 155 in the Loop>>Managers>>DoseMath.swift file to read `return self` as shown in screenshot below.  This will result in Loop setting neutral temp basals when the recommended temp basal matches the Loop's basal schedule.  The potential downsides are slightly more battery consumption, and slightly greater opportunity for temp basal failures as it is a longer pump communication than simply canceling a temp basal.

<p align="center">
<img src="../img/neutral_temp.png" width="750">
</p>

### Exponential Insulin Curve
The Exponential Insulin Curve Models (Rapid-Acting Adult, Rapid-Acting Child, and Fiasp) are defaulted to an insulin duration of 360 minutes...but the peak activity of the various curves differs:

* Rapid-acting adult curve peaks at 75 minutes
* Rapid-acting child curve peaks at 65 minutes
* Fiasp peaks curve peaks at 55 minutes

If you wish to customize these values, you can adjust them on Lines 22-38 in the Common>>Models>>Insulin>>ExponentialInsulinModelPreset.swift file

<p align="center">
<img src="../img/exponential.png" width="750">
</p>

### Loop Logo
If you want an app logo other than the default green circle for your Loop app, you can easily customize this.  To make it easy to generate the correct sizes of icons, you can use a site like [appicon.build](http://www.appicon.build/) and just drag and drop your source image. The source image needs to be 1024 pixels x 1024 pixels.  The site will email you a zip file.  Double click the zip file, choose the “ios” folder, and copy the contents of the Appicon.appiconset as shown highlighted below.

<p align="center">
<img src="../img/appicon1.jpg" width="450">
</p>

Now navigate to the corresponding Loop folder as shown below.  Replace the contents of the Appicon.appiconset with your copied images.

<p align="center">
<img src="../img/appicon2.jpg" width="450">
</p>

You can confirm the successful change by looking in Xcode.  You should see your custom logo in the Appicon set now.  You will also likely see a yellow alert that there are “unassigned children”.  This alert will not prevent your app from building, it’s simply because the zip file contained more sizes of images than Loop app uses.  You can just leave the unassigned images as is.

<p align="center">
<img src="../img/appicon3.jpg" width="450">
</p>

### Apple Watch Customizations

#### Recommended Bolus Autofill
The Apple Watch's default is to autofill to 75% of the recommended bolus.  If you wish, you can customize so that the watch autofills a different percentage. To do this, the multiplier can be changed from 0.75 to a value of your choice. A value of 1 will autofill 100% of the recommended bolus. A value of 0 will autofill 0% of the recommended bolus.   Go to the Watchapp Extension>>Controllers>>BolusInterfaceController.swift. Edit the section of line 96 for your customization.

<p align="center">
<img src="../img/watch_bolus.png" width="750">
</p>

#### Adjust sensitivity of digital crown for carb and bolus entry
The rate of change of the carb and bolus entry pickers when using the digital crown can be altered. You'll need to edit two lines in files within the WatchApp Extension>>Controllers folder.  In BolusInterfaceController.swift edit line 174, and in AddCarbsInterfaceController.swift edit line 215. The 1/24 value is the ratio of rotations of the crown to the amount of change in the value. Changing it to 1/12 would mean that twice as many turns would be needed for the same amount of carb or bolus entry.

<p align="center">
<img src="../img/sensitivity1.png" width="800">
</p>

<p align="center">
<img src="../img/sensitivity2.png" width="800">
</p>


