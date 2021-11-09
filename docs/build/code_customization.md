# Code Customizations

Based on Loop users’ experience, there are some customizations that you may want to incorporate ahead of building your Loop app and Apple Watch app.  These customizations must be done prior to building the Loop app onto your iPhone, they cannot be done from within the app itself. If you are an experienced builder - you know what to do.

For new builders, you might want to first build the code and familiarize yourself with the interface.  Later, you can make the customization(s) you desire on the same download as the original build and then build again to the phone.  The second build will be much faster than the first build.  The downloaded code should be fairly recent - don't try to use code you downloaded a year ago - in that case, get a fresh download.  And be sure to read the [Instructions for Finding the Lines](code_customization.md#instructions-for-finding-the-lines).

!!! info "Line numbers may change"
    Every effort will be made to update the line numbers as the code is updated, but there may be times where the screenshots and line numbers differ from the current version of Loop code.

    * You may notice some customizations list line numbers for different branches

    * If you cannot identify a line that looks exactly like the example - do not guess - go to your favorite social media group and ask for help

## Instructions for Finding the Lines

For each customization, you will be given landmarks to find the correct location in the code. You can choose to search using the `Key_Phrase` or navigate to the file in the folder structure and look for (cmd-L #) the line number.

  * Folder: Loop/subfolder1/subfolder2/etc.
  * File: filename.swift, line number(s)
``` title="Key_Phrase"
use the copy button at right, paste into search
```

There may be a figure illustrating the change.

Below the figure, the original, and in some cases, the modified code will be displayed as text.

To search using the `Key_Phrase` (see graphic below for clarification):

* A copy button is available when you hover your mouse in the right-hand side of the block below the title `Key_Phrase`,  click on it to copy the phrase
* In Xcode, tap the Find menu item and select Find in Workspace
* Paste the text into the find search-box that opens on upper left of Xcode screen and hit enter
* A series of options show up underneath the find search-box
* The file in which the line is located is reported and then one or more lines in that file with that word or phrase are listed
* Click on the one you think is correct and it will display in the main middle window of Xcode with the Keyword highlighted on the line you selected
    * The `Key_Phrase` was selected to limit the search to just the relevant line (if possible)
    * In some cases, the `Key_Phrase` gets you close to where you need to make the modifications

![graphic showing how to search using the Key_Phrase](img/code-custom-xcode-search.svg){width="750"}
{align="center"}

<br>

## Disable Authentication for Bolusing

Depending on your iPhone preferences and model, you may have Face ID or Touch ID enabled.  Those security features will also be used to authenticate bolus delivery in Loop.  You can choose to disable authentication (i.e., not require Face ID, Touch ID, or passcode for bolusing) through the following code customization.

  * Folder: Loop/View Controllers
  * File: BolusViewController.swift, Line 529
``` title="Key_Phrase"
canEvaluatePolicy(.deviceOwnerAuthentication
```

 The screenshot below was taken with Loop v2.0 when the line number was 201; with current Loop, that same code is found at line 529. Add the `false &&` as shown in the screenshot below:

![img/custom-id.png](img/custom-id.png){width="750"}
{align="center"}

_Code Before Modification_

    if context.canEvaluatePolicy(.deviceOwnerAuthentication, error: nil) {

_Code After Modification_

    if false && context.canEvaluatePolicy(.deviceOwnerAuthentication, error: nil) {

## Default Carb Absorption Times

![img/carb_screen.png](img/carb_screen.png){width="200"}

Loop’s default carb absorption times are based on the high, medium, and low glycemic index absorption curves presented in *Think Like A Pancreas* by Gary Scheiner.  Currently the lollipop (fast) icon is set for 2 hours, taco (medium) icon for 3 hours, and pizza (slow) icon for 4 hours.  

  * Folder: Loop/LoopCore
  * File: LoopSettings.swift
  * Line: 16 (v2.2.4 master), 41 (v2.2.4 AB), 50 (current)

``` title="Key_Phrase"
defaultCarbAbsorptionTimes: CarbStore.DefaultAbsorptionTimes
```

![img/carb_times.png](img/carb_times.png){width="750"}
{align="center"}

For example, if you wanted to make lollipop a 30 minute absorption and pizza a 5 hour absorption, the edit would look like below:

![img/carb_times_example.png](img/carb_times_example.png){width="750"}
{align="center"}

_Code Before Modification_

    public static let defaultCarbAbsorptionTimes: CarbStore.DefaultAbsorptionTimes = (fast: .hours(2), medium: .hours(3), slow: .hours(4))

_Code After Modification (if you selected 30m, 3hr, and 5hr)_

    public static let defaultCarbAbsorptionTimes: CarbStore.DefaultAbsorptionTimes = (fast: .minutes(30), medium: .hours(3), slow: .hours(5))

## Exponential Insulin Curve

The Exponential Insulin Curve Models (Rapid-Acting Adult, Rapid-Acting Child, and Fiasp) default to an insulin duration of 360 minutes...but the peak activity of the various curves differs, as follows:

* Rapid-acting adult curve peaks at 75 minutes
* Rapid-acting child curve peaks at 65 minutes
* Fiasp peaks curve peaks at 55 minutes

If you wish to customize these values, please make sure you know what you are doing.  This is not a modification recommended for Loop novices.

  * Folder: Loop/LoopCore/Insulin
  * File: ExponentialInsulinModelPreset.swift
  * Lines:
      * actionDuration (20 to 29)
      * peakActivity (31 to 40)
      * effectDelay (42 to 51)

``` title="Key_Phrase"
MARK: - Model generation
```

![img/exponential.png](img/exponential.png){width="750"}
{align="center"}

## Loop Logo

If you want an app logo other than the default green circle for your Loop app, you can easily customize this.  To make it easy to generate the correct sizes of icons, you can use a site like [appicon.build](http://www.appicon.build/) or [appicon.co](https://appicon.co/) and just drag and drop your source image. The source image needs to be 1024 pixels x 1024 pixels.  The site will email you a zip file or automatically download a set of files.  Highlight and copy the contents of the Appicon.appiconset that you are sent, including the Contents.json file

### Custom Icon: Workspace Builds

Use Finder to Navigate to the LoopWorkspace folder. These instructions assume you used the Build-Select Script - if your files are in a different folder, make the appropriate adjustment.

1. Use Finder to navigate to Downloads / BuildLoop and open the folder with the most recent date (e.g., Loop-Master-211006-0524)
1. Double-click on the LoopWorkspace folder
1. Double-click on the AdditionaAssets.xcassets folder
1. Double-click on the CustomLoopIcon.appiconset folder
1. Replace the contents of the Appicon.appiconset with your copied images and Contents.json file.


### Custom Icon: Zip-Download Builds

These instructions are no longer valid for the new Workspace build, but are left for folks who have older code they are still using.

Now navigate to the corresponding Loop folder (DefaultAssessts.xcassets, Appicon.appiconset) as shown below.  

![img/appicon1.png](img/appicon1.png){width="650"}
{align="center"}

Replace the contents of the Appicon.appiconset with your copied images and Contents.json file.

![img/appicon2.png](img/appicon2.png){width="650"}
{align="center"}

You can confirm the successful change by looking in Xcode under Loop -> DefaultAssets.xcassets -> Appicon.  You should see your custom logo in the Appicon set now.  You may also see a yellow alert that there are “unassigned children” depending on the images the app icon generator tool produced. The unassigned children alert will not prevent your app from building, it’s simply because there are more more sizes of images than Loop app uses.  You can just leave the unassigned children alone (wow...how often do you get to say that phrase?).

![img/appicon3.png](img/appicon3.png){width="650"}
{align="center"}

And now you'll be the proud new owner of a custom Loop icon.

![img/unicorn-logo.jpeg](img/unicorn-logo.jpeg){width="350"}
{align="center"}

## Adjust the Watch Crown Sensitivity

The rate of change of the carb and bolus entry pickers when using the digital crown can be altered as can the rotation required to confirm a bolus on the watch.

For the carb and bolus entry pickers, edit two lines in files within the WatchApp Extension>>Controllers folder.  In AddCarbsInterfaceController.swift edit line 249 and in BolusInterfaceController.swift edit line 191. The 1/24 value is the ratio of rotations of the crown to the amount of change in the value. Changing it to 1/12 would mean that twice as many turns would be needed for the same amount of carb or bolus entry.

  * Folder: Loop/WatchApp Extension/Controllers
  * File: AddCarbsInterfaceController.swift, Line: 249

``` title="Key_Phrase"
let rotationsPerIncrement
```

![img/sensitivity2.png](img/sensitivity2.png){width="800"}
{align="center"}

  * Folder: Loop/WatchApp Extension/Controllers
  * File: BolusInterfaceController.swift, Line: 191

``` title="Key_Phrase"
let rotationsPerValue
```

![img/sensitivity1.png](img/sensitivity1.png){width="800"}
{align="center"}

The modification required to reduce the watch crown rotation to confirm a bolus is achieved by changing two additional lines, 311 and 360, in the same file, BolusInterfaceController.swift. For example to change rotation required to 70% of the default, change 1.0 to 0.7 in 3 places on those 2 lines. This `Key_Phrase` returns 3 lines, the second 2 of which are the ones in that file where the change is required:


``` title="Key_Phrase"
abs(accumulatedRotation)
```


## Expiration Notification Customization

An expiration notification feature has been added to Loop. You get a notification when you open the Loop app to alert you that the expiration is approaching. (Not available with version v2.2.4 and earlier.)

* Read [Loop App Expiration Notification](../operation/features/notifications.md#loop-app-expiration-notification) to see the expiration reminder
* Read [Loop App Expiration Date](../operation/features/notifications.md#loop-app-expiration-date) if you have an older version of Loop

If you prefer a different notification time and frequency, there are two lines you can modify:


* Folder: Loop/Managers
* File: ProfileExpirationAlerter.swift
* Line 16: modify how long before expiration you get the FIRST notification
* Line 28: modify how frequently you will be notified

``` title="Key_Phrase"
expirationAlertWindow: TimeInterval
```

``` title="Key_Phrase"
 minimumTimeBetweenAlerts: TimeInterval
```

![Profile expiration notification details](img/expiration-custom.png){width="600"}
{align="center"}

Default code for line 16:
```
    static let expirationAlertWindow: TimeInterval = .days(20)
```

Example modifications to First Notification:

* 30 days: change `.days(20)` to `.days(30)`
* 12 hours: change `.days(20)` to `.hours(12)`

Default code for line 28:

```
    let minimumTimeBetweenAlerts: TimeInterval = timeUntilExpiration > .hours(24) ? .days(2) : .hours(1)
```


Modify Frequency of Repeated Notifications (Three Values):

* This phrase: ```> .hours(24) ? .days(2) : .hours(1)```
* Rewritten as: ```> Time_A ? Frequency_A : Frequency_B```, means:
    * Use Frequency_A if there is more time between now and the expiration date than Time_A
    * Use Frequency_B if there is less time between now and the expiration date than Time_A

You can enter Time or Frequency as ```.days(value)```, ```.hours(value)``` or ```.minutes(value)```.

Free App Users:

An example change that a Free Loop App user (who has to build once a week) might choose is:

```
     > .hours(4) ? .days(10) : .hours(2)
```
Combined with an ```.hours(12)``` on line 16, they would get notified at 12 hours, 4 hours and 2 hours before expiration on the day of expiration and only when the app is opened. Since you'll be building once a week, you can play around with these values until you are happy.


## Additional Customizations

Additional customizations are found on another website. If you did not find the customization you want here on LoopDocs, then try the [Loop and Learn Customization Page](https://www.loopandlearn.org/custom-code). Check that page in case this list is not up to date.

* Add Lyumjev Insulin Model
* Adjust Percent Bolus for Automatic Dosing Strategy
* Adjust Watch Crown Rotation Required for Bolus Confirmation
* Pods: Increase Log File History Hours
* These Require Workspace Builds (which are now standard)
    * Modify Override Sensitivity
    * Medtronic: Disable mySentry (Current Loop removes need for this)
    * Pods: Add Extra Insulin on Insertion
    * Pods: Change Default Expiration Reminder


Note that the other site will point you right back to LoopDocs if the customization is found on this LoopDocs customization page.
