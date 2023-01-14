## Code Customizations

**This page is only relevant is you used the [Mac Build](../build/overview.md) method to build your code**

**At the current time, customizations for [Browser Build](../gh-actions/gh-overview.md) are not included in LoopDocs.**

Based on Loop users’ experience, there are some customizations that you may want to incorporate ahead of building your Loop app and Apple Watch app.  These customizations must be done prior to building the Loop app onto your iPhone, they cannot be done from within the app itself. If you are an experienced builder - you know what to do.

## Build then Customize

For new builders, please build the code before you make any changes. Start with Open Loop and familiarize yourself with the interface.  Later, you can make the customization(s) you desire (using Xcode as your editor) on the same download as the original build and then build again to the phone.  The second build will be much faster than the first build.  

When applying a customization, the downloaded code should be fairly recent. If you are not sure, get a fresh download. If you know your downloaded code is the [Current Release](../version/releases.md#current-release), you can skip the download and use the same folder as last time.  

### Find My Dowloaded Loop Code

Refer to the graphic below.  The Downloads folder in Finder is highlighted on the upper left. The full path to Loop.xcworkspace is highlighted along the bottom.

* Open Finder
* Navigate to Downloads/BuildLoop and look for your download by name and date
* Open that folder, for example, Downloads/BuildLoop/Loop-220803-1145, and inside that folder open the LoopWorkspace folder
* Inside the Downloads/BuildLoop/Loop-220803-1145/LoopWorkspace folder, double-click on Loop.xcworkspace
* Xcode automatically opens to that particular download
* You can then make the customizations and build to your phone

![how to use finder to find the correct download and open xcode](img/finding-loopworkspace.svg){width="750"}
{align="center"}

!!! tips "Experienced Builders"
    Experienced builders will often build a fresh download to a simulator for their phone iOS (not their phone) to ensure download is good and is compatible with macOS, Xcode and phone iOS. Once the build is successful, they apply their customizations and build again to the simulator. Last step is to build the customized version to their real phone.

Be sure to read the [Instructions for Finding the Lines](code_customization.md#instructions-for-finding-the-lines).

!!! info "Line numbers may change"
    Every effort will be made to update the line numbers as the code is updated, but there may be times where the screenshots and line numbers differ from the current version of Loop code.

    * You may notice some customizations list line numbers for different branches

    * If you cannot identify a line that looks exactly like the example - do not guess - go to your favorite social media group and ask for help

!!! abstract "Loop 2.2.x vs Loop 3"

    * Loop 3 has been released but there are still many people using older code.
    * The labels below indicate Loop 2.2.x or Loop 3, if they are different
    * Users of Loop 2.2.9 (or earlier) or FreeAPS should refer to the Loop 2.2.x examples.
    * Users of Loop 3 should refer to the Loop 3 examples.
        * Note that some changes are in a different file for Loop 3 (part of the architecture upgrade for the app).

## Build-Time Features

Build-time features are not available with Loop 2.2.x.

With Loop 3, some features are enabled or disabled by default but can be modified by adding a "flag" to a particular line in the LoopConfigOverride.xcconfig file. This is the same file used to automatically sign all your targets. You can edit the version in your LoopWorkspace folder (it shows up as the top item in the Xcode folder view) - or - if you use the build script, you can edit the copy found in ~/Downloads/BuildLoop after the first time you use the script. For that second case, the "flags" you add in ~/Downloads/BuildLoop/LoopConfigOverride.xcconfig are applied to all downloads created with the script.

These flags are always upper case with underscore separating words for clarity. They are inserted anywhere after the word `$(inherited)` and before the `//`. The `//` indicates the flags to the right are not included. In the line shown below, simulators are enabled but debug features are turned off. Each flag is separated by a space. Do not enter a return between selections - Xcode will word-wrap the line for clarity, but all values need to be on a single line.

_Code Before Modification_

```
// Features
SWIFT_ACTIVE_COMPILATION_CONDITIONS = $(inherited) SIMULATORS_ENABLED //DEBUG_FEATURES_ENABLED
```

The example below is for someone who is using a Free Developer ID - which does not support Siri.

_Code After Modification_

```
// Features
SWIFT_ACTIVE_COMPILATION_CONDITIONS = $(inherited) SIRI_DISABLED SIMULATORS_ENABLED //DEBUG_FEATURES_ENABLED
```

List of some flags and what they do:

|FLAG|PURPOSE|
|---------|---------|
|SIRI_DISABLED|Required to build Loop from Xcode with a free developer account|
|ADULT_CHILD_INSULIN_MODEL_SELECTION_ENABLED|The choice for Child Model is enabled in Therapy Settings. Please read [Enable Child Model](#enable-child-model).|
|REMOTE_OVERRIDES_DISABLED|Remote commands: override, carbs or boluses will not be accepted even if all the [Remote Command](../nightscout/remote-overrides.md) requirements are configured|
|OBSERVE_HEALTH_KIT_CARB_SAMPLES_FROM_OTHER_APPS_ENABLED|Turns on ability for Loop to read third party carb entries. You must also make sure Health permissions allow Loop to read carbs from Health. Be vigilant if you select this; added carbs lead to added insulin dosing when closed loop is enabled|
|SHOW_EVENTUAL_BLOOD_GLUCOSE_ON_WATCH_DISABLED|The Apple Watch screens show current glucose, trend arrow and eventual glucose by default. This flag disables the display of eventual glucose on the watch if you find the display distracting.|

## Instructions for Finding the Lines

There are other customizations where the user goes into a particular file and makes a specific change to the code.

For each customization, you will be given landmarks to find the correct location in the code. You can choose to search using the `Key_Phrase` or navigate to the file in the folder structure and look for (cmd-L #) the line number. Note that the folder is listed with respect to the LoopWorkspace directory.

**For each change you make in Xcode - be sure to save the file - otherwise the modification does not get built into your app.**

``` title="Key_Phrase"
use the copy button at right, paste into search
```

  * Folder: Loop/subfolder1/subfolder2/etc.
  * File: filename.swift, line number(s)

There may be a figure illustrating the change.

Below the figure, the original, and in some cases, the modified code will be displayed as text.

* Most customizations show the original line of code that you will be changing
    * Sometimes that line is long and you may need to use the scroll bar to see the entire line in LoopDocs
    * In most cases, an example customization is shown to assist you in deciding how to edit the line to meet your needs

To search using the `Key_Phrase` (see graphic below for clarification):

* A copy button is available when you hover your mouse in the right-hand side of the block below the title `Key_Phrase`;  click on it to copy the phrase
* In Xcode, tap the Find menu item and select `Find in Workspace`
* Paste the text into the Find search-box that opens on upper left of Xcode screen and hit enter
* You should see a message `1 result in 1 file` (for most cases)
    * Some customizations will show more than one result, but that will be explained in the directions for that customization
* The file in which the line is located is reported showing the line in that file containing the `Key_Phrase`
* Click on the one you think is correct and it will display in the main middle window of Xcode with the Keyword highlighted on the line you selected
    * The `Key_Phrase` was selected to limit the search to just the relevant line (if possible)
    * In some cases, the `Key_Phrase` gets you close but not exactly on the line where you need to make the modifications - please read carefully

![graphic showing how to search using the Key_Phrase](img/code-custom-xcode-search.svg){width="750"}
{align="center"}

<br>

### Folders and Icons

The folders listed in the code customization steps below are the actual directory names as stored on your computer.  However, a shortened name is used for some folders when being displayed as icons in Xcode. Some people prefer to search through the folder icons to find a file instead of using the `Find in Workspace` feature.

In the graphic below, the user searched for an item found for both Eros and DASH pods (in two different files).  The top part of the graphic shows the result of the search with user clicking on one instance.  On the right side of the top graphic (highlighted by red rectangle) is the name of the selected file on the computer with the full directory name.

* Inset 1: User clicked on the folder icon (highlighted by red square) to see the list of icons for folders included in the LoopWorkspace
* Inset 2: User opens folders under RileyLink icon to open OmniKit, then OmnipodCommon to find the Pod.swift file

![graphic showing folder icons vs folder names](img/xcode-folder-names.svg){width="750"}
{align="center"}

These folder icon names are different from the directory names on the computer:

|  Folder Icon Name |  Directory Name | |
|:--|:--||
| ShareClient | dexcom-share-client-swift | 
| RileyLink | rileylink_ios | 
| Amplitude | Amplitude-iOS | 

All other icons and directory names match.


## Disable Authentication for Bolusing

Depending on your iPhone preferences and model, you may have Face ID or Touch ID enabled.  Those security features will also be used to authenticate bolus delivery in Loop.  You can choose to disable authentication (i.e., not require Face ID, Touch ID, or passcode for bolusing) through the following code customization.

!!! warning "Loop 3"
    For Loop 3, this controls the authorization requirement to modify Therapy Settings as well as to confirm bolus delivery.

``` title="Key_Phrase"
canEvaluatePolicy(.deviceOwnerAuthentication
```

* Loop 2.2.x
    * Folder: Loop/View Controllers
    * File: BolusViewController.swift, Line 529
* Loop 3
    * Folder: LoopKit/LoopKitUI/Extensions/
    * File: Environment+Authenticate.swift, Line 20

 The screenshot below was taken with Loop v2.0 when the line number was 201; with Loop 2.2.x versions, that same code is found at line 529. Add the `false &&` as shown in the screenshot below:

![img/custom-id.png](img/custom-id.png){width="750"}
{align="center"}

#### Loop 2.2.x

_Code Before Modification_

    if context.canEvaluatePolicy(.deviceOwnerAuthentication, error: nil) {

_Code After Modification_

    if false && context.canEvaluatePolicy(.deviceOwnerAuthentication, error: nil) {

#### Loop 3

_Code Before Modification_

    if context.canEvaluatePolicy(.deviceOwnerAuthentication, error: &error) {

_Code After Modification_

    if false && context.canEvaluatePolicy(.deviceOwnerAuthentication, error: &error) {

## Default Carb Absorption Times

![img/carb_screen.png](img/carb_screen.png){width="200"}
{align="center"}

Loop’s default carb absorption times are based on the high, medium, and low glycemic index absorption curves presented in *Think Like A Pancreas* by Gary Scheiner.  With Loop 2.2.x, the lollipop (fast) icon is set for 2 hours, taco (medium) icon for 3 hours, and pizza (slow) icon for 4 hours. This is modified for Loop 3 to 30 minutes, 3 hours and 5 hours respectively.

``` title="Key_Phrase"
defaultCarbAbsorptionTimes: CarbStore.DefaultAbsorptionTimes
```

* Loop 2.2.x
    * Folder: Loop/LoopCore
    * File: LoopSettings.swift
    * Line: 16 (2.2.4 master), 41 (2.2.4 AB), 50 (2.2.5 and later)

* Loop 3
    * Folder: Loop/LoopCore
    * File: LoopCoreConstants.swift
    * Line: 16


For example, if you wanted to modify Loop 2.2.9 so that lollipop represents a 30 minute absorption and pizza a 5 hour absorption, the edit would be as follows:


_Code Before Modification for Loop 2.2.x_

    public static let defaultCarbAbsorptionTimes: CarbStore.DefaultAbsorptionTimes = (fast: .hours(2), medium: .hours(3), slow: .hours(4))

_Code After Modification or default for Loop 3_

    public static let defaultCarbAbsorptionTimes: CarbStore.DefaultAbsorptionTimes = (fast: .minutes(30), medium: .hours(3), slow: .hours(5))

Note that if you change from 2 hours to 30 minutes, you must also change the indication before the parentheses.

## Adjust Percent Bolus for Automatic Bolus

If you are mostly happy with the Dosing Strategy of Automatic Bolus but wish it delivered more or less insulin during every Loop interval, then this customization is for you.

This customization changes the percent of the recommended bolus used for automatic delivery. The method for calculating that recommendation is not changed by this modification.  The default value is 40% (0.4).  It is recommended you take small changes of 0.1 at a time.  Once you modify it once and try it out for a while, it’s easy to go back and change it again.

With Loop 2.2.x, the end of the line has a comment `// %`, whereas with Loop 3, there is an explanatory comment (line starting with `//`) before the line.

**Change just the number and double check that the value is less than 1.**

``` title="Key_Phrase"
let bolusPartialApplicationFactor
```

* Loop 2.2.x
    * Folder: Loop/LoopCore
    * File: LoopSettings.swift
    * Line: 89 (2.2.5 and later)

* Loop 3
    * Folder: Loop/Loop/Models
    * File: LoopConstants.swift
    * Line: 44

_Code Before Modification_

    public let bolusPartialApplicationFactor = 0.4

_Code After Modification to 50% of recommended insulin_

    public let bolusPartialApplicationFactor = 0.5


!!! warning "Do not exceed 1.0"
    This number should never be bigger than 1 (you’d be getting more than Loop recommends). If you think you need more than 1, consider your settings and meal entries.

## Modify Override Sensitivity

Some people want finer settings on the override sensitivity picker and may want to limit the overall range for overrides – especially for children.

!!! tip "1% Settings Available without Customization"
    With the advent of Loop 3, the Override Sensitivity values are not limited by the default picker values of 10%.

    * Not available in Loop 2.2.x
    * Not available in FreeAPS (based off Loop 2.2.x)
    * [Select 1% Sensitivity](../operation/features/workout.md#select-1-sensitivity)

Any override more than a factor of 2 from 100% can cause Loop predictions to be wrong – especially if a carb count is entered. (An [override](../operation/features/workout.md) is NOT the same as a manual temp basal - it changes insulin sensitivity factor and carb ratio in addition to the basal rate needed for zero change in IOB for the duration of the override.)

This example customization changes the lower bound for sensitivity to 50% (factor of 2 smaller than 100%) and provides 5% steps.

``` title="Key_Phrase"
let allScaleFactorPercentages
```

* Loop 2.2.x and Loop 3
    * Folder: LoopKit/LoopKitUI/Views
    * File: InsulinSensitivityScalingTableViewCell.swift, Line 19

_Code Before Modification_

    private let allScaleFactorPercentages = Array(stride(from: 10, through: 200, by: 10))

_Code After Modification to 50% to 200% by steps of 5%_

    private let allScaleFactorPercentages = Array(stride(from: 50, through: 200, by: 5))


## Modify Maximum and Warning Carb Entry

### Loop 3 Carb Entry Variables

During the development of Loop 3, a warning screen was added to the carb entry interface when the entered meal is between 100 and 250 grams, inclusive. The variables that control when the warning screen is shown and that limit the overall maximum for carb entries are stored in the LoopConstants file, where they are used by both direct interaction with the Loop phone and by the remote carb entry checking code.

``` title="Key_Phrase"
let warningCarbEntryQuantity =
```

If you do not find the Key Phrase `warningCarbEntryQuantity` in the code - you do not have Loop 3 code. Use the [Loop 2.2.x Max Carb Entry](#loop-22x-max-carb-entry) version.

If you do find that Key Phrase in the code, you have the newer version of Loop 3. The max and warning values can be modified in LoopConstants. The variable `maxCarbEntryQuantity` is found in LoopConstants, two lines earlier than `warningCarbEntryQuantity`.

_Code Before Modification_

    static let maxCarbEntryQuantity = HKQuantity(unit: .gram(), doubleValue: 250) // cannot exceed this value

    static let warningCarbEntryQuantity = HKQuantity(unit: .gram(), doubleValue: 99) // user is warned above this value

This first example might be used by a parent for a child with very small carb entries.

_Code After Modification to enable the warning at lower levels and limit maximum_

    static let maxCarbEntryQuantity = HKQuantity(unit: .gram(), doubleValue: 99) // cannot exceed this value

    static let warningCarbEntryQuantity = HKQuantity(unit: .gram(), doubleValue: 49) // user is warned above this value

This second example might be used by a person who routinely enters large meals and does not want to be warned with every meal.

_Code After Modification to warn if entry is between 201 and 300g_

    static let maxCarbEntryQuantity = HKQuantity(unit: .gram(), doubleValue: 300) // cannot exceed this value

    static let warningCarbEntryQuantity = HKQuantity(unit: .gram(), doubleValue: 200) // user is warned above this value



### Loop 2.2.x Max Carb Entry

Users of Loop 2.2.9 and earlier or FreeAPS must use the following method for modifying maximum carb entry:

Some people want to limit the maximum number of carbs that can be entered in one entry – especially for children or folks who eat lower carb. This helps prevent accidental typos, e.g., entry of 115 g instead of 15 g for a meal.


``` title="Key_Phrase"
maxQuantity =
```

As shown in the graphic below, this phrase shows up in 2 places, only the first one should be modified.

![xcode display showing the key phrase found in 2 places](img/xcode-modify-max-carb-entry.svg){width="700"}
{align="center"}


* Loop 2.2.x and Loop 3
    * Folder: Loop/Loop/View Controllers
    * File: CarbEntryViewController.swift, Line 33 (Loop 2.2.x) or 36 (Loop 3)

_Code Before Modification_

    var maxQuantity = HKQuantity(unit: .gram(), doubleValue: 250)

_Code After Modification to limit carb entry to 99 g_

    var maxQuantity = HKQuantity(unit: .gram(), doubleValue: 99)



## Pods: Add Extra Insulin on Insertion

The default value is 0.0 u of extra insulin.  If you use this customization, start with a small number and work your way up. If you are coming from manual podding and routinely gave yourself an extra bolus with your PDM at pod change time, you may not need nearly as much with Loop - be conservative.

Note that Loop does not include the amount of insulin in the prime or insertion steps in your IOB. The pod reports every pulse that it delivers to Loop. If you look in the Pod Settings insulin delivered row, that is the total delivered by the pod minus the (prime plus insertion) amounts. The only way to know that you successfully made this change is to count the clicks.  Normal insertion is 0.5 U (0.5 U / 0.05 U per click = 10 clicks). So if you add 0.35 U to the "extra" value, you should get 0.35 / 0.05 = 7 extra clicks. In other words, 17 total clicks after you press insert.

This code change is found in one location for Eros Pods (called Omnipod throughout the app) and DASH Pods (called Omnipod Dash throughout the app). I tend to change both files, but if you're only using one kind of pod, that is really not necessary.

``` title="Key_Phrase"
let cannulaInsertionUnitsExtra
```

* Loop 2.2.x: Eros Pod (ones that require a RileyLink compatible device)
    * Folder: rileylink_ios/OmniKit/Model
    * File: Pod.swift, Line 72 (Loop 2.2.x)
* Eros or DASH Pod (Loop 3 only)
    * Folder: rileylink_ios/OmniKit/OmnipodCommon (Eros)
    * Folder: OmniBLE/OmniBLE/OmnipodCommon (DASH)
    * File: Pod.swift, Line 87 (Eros); Line 82 (DASH)
    
_When finding the file using the folder icons in Xcode, instead of using the `Key_Phrase` in `Find in Workspace`, the RileyLink icon represents the rileylink_ios folder name on the computer._

_Code Before Modification_

    public static let cannulaInsertionUnitsExtra = 0.0 // edit to add a fixed additional amount of insulin during cannula insertion

_Code After Modification to add 0.35 U_

    public static let cannulaInsertionUnitsExtra = 0.35 // edit to add a fixed additional amount of insulin during cannula insertion

## Modify the Guardrails

The [Therapy Setting Guardrails](../loop-3/therapy-settings.md#guardrails-for-settings) are for Loop 3 only.

If you build Loop 3 over a version of Loop 2.2.x or FreeAPS where the Correction Range is lower than the default value of 87 mg/dL (4.8 mmol/L), your app requires you to satisfy the new guardrail before you can save that Therapy Setting when you onboard.


``` title="Key_Phrase"
Guardrail(absoluteBounds:
```

* Loop 3 only
    * Folder: LoopKit/Extensions
    * File: Guardrail+Settings.swift
    * Line: 12 for suspendThreshold
    * Line: 26 for correctionRange

_Code Before Modification_

    static let suspendThreshold = Guardrail(absoluteBounds: 67...110, recommendedBounds: 74...80, unit: .milligramsPerDeciliter, startingSuggestion: 80)

and

    static let correctionRange = Guardrail(absoluteBounds: 87...180, recommendedBounds: 100...115, unit: .milligramsPerDeciliter, startingSuggestion: 100)

Modify the 67 for suspendThreshold or 87 for correctionRange to the desired value.  Loop automatically converts from mg/dL. So you must enter values reasonable for mg/dL (18 times higher than for mmol/L).

## Adjust Future Carbs Time Interval

Loop 3 limits the future time change allowed to 1 hour.

``` title="Key_Phrase"
cell.datePicker.maximumDate = date.addingTimeInterval
```

* Loop 3 only:
    * Folder: Loop/Loop/View Controllers
    * File:CarbEntryViewController.swift
    * Line: 361
    * Default shown below (for maximum and minimum):

_Code Before Modification_

    cell.datePicker.maximumDate = date.addingTimeInterval(.hours(1))
    cell.datePicker.minimumDate = date.addingTimeInterval(.hours(-12))

Change the maximumDate to the number of hours in the future you desire. Remember that Loop may increase insulin dosing for future carbs - make sure that they actually arrive. 

The minimumDate is how far back in the past you can modify time.  The default is 12 hours in the past.

## Adjust the Watch Crown Sensitivity

The rate of change of the carb and bolus entry pickers when using the digital crown can be altered as can the rotation required to confirm a bolus on the watch. If you are running an older series watch - you may want to make these customizations. When I switched from Series 3 to Series 7 watch - it was amazing. I got a graph on the main watch screen I didn't even know existed and the bolus acceptance was a breeze!

There are a number of places where you need to make changes (2 for sensitivity and 2 for bolus confirmation for Loop 2.2.x), so walk though them one at a time. For the `Watch Crown Sensitivity`, the 1/24 value is the ratio of rotations of the crown to the amount of change in the value. Changing it to 1/12 would mean that half as many turns would be needed for the same amount of carb or bolus entry.

* The Loop 2.2.x customizations are throughly tested by many users.
* The Loop 3 customization is provided from code inspection and one test - use with care.

### Loop 2.2.x Sensitivity


``` title="Key_Phrase"
let rotationsPerIncrement
```

* Folder: Loop/WatchApp Extension/Controllers
* File: AddCarbsInterfaceController.swift, Line: 249
* Initial Value: 1/24; try 1/12 to increase change in picker value for a given motion

![img/sensitivity1.png](img/sensitivity2.png){width="800"}
{align="center"}

``` title="Key_Phrase"
let rotationsPerValue
```

* Folder: Loop/WatchApp Extension/Controllers
* File: BolusInterfaceController.swift, Line: 191
* Initial Value: 1/24; try 1/12 to increase change in picker value for a given motion

![img/sensitivity1.png](img/sensitivity1.png){width="800"}
{align="center"}

### Loop 2.2.x Bolus Confirmation

In order to reduce the amount the user has to spin the watch crown to confirm a bolus, there are 3 numbers on 2 lines that must be modified. You will be working in the same file you just used to modify the watch sensitivity to adjusting the bolus amount, BolusInterfaceController.swift.

For example to change rotation required to 70% of the default, change 1.0 to 0.7 in 3 places on those 2 lines. This `Key_Phrase` returns 3 lines, the second 2 of which are the ones in that file where the change is required:


``` title="Key_Phrase"
abs(accumulatedRotation)
```

* Folder: Loop/WatchApp Extension/Controllers
* File: BolusInterfaceController.swift, Lines: 311 and 360
* Initial Value: 1.0; try 0.7 to decrease how much is needed to confirm bolus

### Loop 3 Digital Crown Adjustments

These are new instructions and the user should take care - and please [report back](../intro/loopdocs-how-to.md#how-to-find-help) if you have problems.

First - try it with no customization. Then make small changes.

This key phrase will indicate three different files in the same folder as shown in the graphic below - you can adjust each in turn as you desire. When you click on the line, the quantity you change is a few lines below where you find the `Key_Phrase`, except for the CarbAndDateInput file.

``` title="Key_Phrase"
.digitalCrownRotation
```

* Folder: Loop/WatchApp Extension/Views/Carb Entry & Bolus

![use a single Key_Phrase to identify all lines needed to customize sensitivity with loop 3](img/digital-crown-rotation.svg){width="800"}
{align="center"}

#### Modify Bolus Confirmation Motion

* File: BolusConfirmationView.swift, line 59
* Initial Value for `scalingRotationBy` is 4
* Decrease to require less motion to confirm bolus (use whole numbers only), start with 3

#### Modify Bolus Picker Sensitivity

* File: BolusInput.swift, line 53
* Initial Value for `rotationsPerIncrement` is 1/24
* A change to 1/12 increases the change in picker value for a given motion

#### Modify Carb and Time Picker Sensitivity

* File: CarbAndDateInput.swift, line 68
* Initial Value for `rotationsPerIncrement` is 1/24
* A change to 1/12 increases the change in picker value for a given motion


## Expiration Notification Customization

An expiration notification feature has been added to Loop. You get a notification when you open the Loop app to alert you that the expiration is approaching. (Not available with version v2.2.4 and earlier.)

* Read [Loop App Expiration Notification](../operation/features/notifications.md#loop-app-expiration-notification) to see the expiration reminder
* Read [Loop App Expiration Date](../operation/features/notifications.md#loop-app-expiration-date) if you have an older version of Loop

If you prefer a different notification time and frequency, there are two lines you can modify:

* Loop 2.2.x and Loop 3
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

## Exponential Insulin Curve

### Enable Child Model

Loop 3, by default, does not include the concept of child versus adult for rapid-acting insulin, i.e., Humalog, Novalog and Apidra.

* The child model can be enabled following the directions in [Build-Time Features](#build-time-features), adding ADULT_CHILD_INSULIN_MODEL_SELECTION_ENABLED to the LoopConfigOverride.xcconfig file and rebuilding
* Insulin Model is then found in the Therapy Setting section of Loop 3 with Adult selected by default
* Insulin Type continues to be associated with the pump and can be modified in the Pump Settings screen

### Insulin Model Customization

Each exponential model has 3 parameters that can be adjusted:

* actionDuration: Duration of insulin activity (minutes)
* peakActivity: Peak of insulin activity (minutes)
* delay: Delay before insulin begins to acts after delivery starts (minutes)

Please read the nitty-gritty discussion that went into the development of the "exponential insulin models" in this [GitHub Issue Comment](https://github.com/LoopKit/Loop/issues/388#issuecomment-317938473).

If you wish to customize these values, please make sure you know what you are doing.  This is not a modification recommended for Loop novices.

``` title="Key_Phrase"
MARK: - Model generation
```

* Loop 2.2.x
    * Folder: Loop/LoopCore/Insulin
    * File: ExponentialInsulinModelPreset.swift
    * Lines:
        * actionDuration (20 to 29)
        * peakActivity (31 to 40)
        * effectDelay (42 to 51)
* Loop 3
    * Folder: LoopKit/LoopKit/Insulin/ << NOTE new location
    * File: ExponentialInsulinModelPreset.swift
    * Lines:
        * actionDuration (19 to 32)
        * peakActivity (34 to 47)
        * delay (49 to 62)

![img/exponential.png](img/exponential.png){width="750"}
{align="center"}

This Loop 3 table of default values is provided for convenience. The times are all in minutes.

|Model|DIA|Peak|Delay|
|---------|---------|---------|---------|
|rapidActingAdult|360|75|10|
|rapidActingChild|360|65|10|
|fiasp|360|55|10|
|lyumjev|360|55|10|
|afrezza|300|29|10|


## Loop Logo

If you want an app logo other than the default green circle for your Loop app, you can easily customize this.  To make it easy to generate the correct sizes of icons, you can use a site like [appicon.build](http://www.appicon.build/) or [appicon.co](https://appicon.co/) and just drag and drop your source image. The source image needs to be 1024 pixels x 1024 pixels.  The site will email you a zip file or automatically download a set of files.  Highlight and copy the contents of the Appicon.appiconset that you are sent, including the Contents.json file

Use Finder to Navigate to the LoopWorkspace folder. These instructions assume you used the Build Select Script - if your files are in a different folder, make the appropriate adjustment.

For Loop 2.2.x:

1. Use Finder to navigate to Downloads / BuildLoop and open the folder with the most recent date (e.g., Loop-Master-211006-0524)
1. Double-click on the LoopWorkspace folder
1. Double-click on the AdditionaAssets.xcassets folder
1. Double-click on the CustomLoopIcon.appiconset folder
1. Delete the contents of the CustomLoopIcon.appiconset folder and copy/paste your new images and Contents.json file.
1. Rebuild your app

For Loop 3:

1. Make sure Xcode is closed
1. Use Finder to navigate to Downloads / BuildLoop and open the folder with the most recent date (e.g., Loop-230114-1153)
1. Double-click on the LoopWorkspace folder
1. Double-click on the OverrideAssetsLoop.xcassets folder
1. Double-click on the AppIcon.appiconset folder
1. Delete the contents of the Appicon.appiconset and copy/paste your new images and Contents.json file.
1. Rebuild your app

You may see a yellow warning that there are “unassigned children” depending on the images the app icon generator tool produced. The unassigned children alert will not prevent your app from building, it’s simply because there are more sizes of images than Loop app uses.  You can just leave the unassigned children alone (wow...how often do you get to say that phrase?).

And now you'll be the proud new owner of a custom Loop icon.


## Additional Customizations

Additional customizations may be found on another website, especially for older versions of the app. If you did not find the customization you want here on LoopDocs, then try the [Loop and Learn Customization Page](https://www.loopandlearn.org/custom-code). Check that page in case this list is not up to date.

* Add Lyumjev Insulin Model (this is only needed for Loop 2.2.x, included in Loop 3)
* Pods: Increase Log File History Hours (only needed for Loop 2.2.x)
* Medtronic: Disable mySentry (only needed for older versions of Loop 2.2.x)
* Pods: Change Default Expiration Reminder (only needed for Loop 2.2.x)
* Emoji Modifications
* Disable Suspend Beeps (only needed for Loop 2.2.x)

Note that the other site has an index that points back to LoopDocs if the customization is found on this page.

## Additional Customizations for Loop 3

The customizations below only work with the Loop 3. 

* You should be comfortable typing commands in a terminal
* You should be comfortable with manipulations (as directed) with Xcode
* You will need to open a terminal in the LoopWorkspace folder of the code that you previously downloaded
    * The next section provides instructions on opening the terminal in the correct place

### Open a Terminal in LoopWorkspace Folder

Refer to the graphic below.  The Downloads folder in Finder is highlighted on the upper left. The full path to Loop.xcworkspace is highlighted along the bottom. Double clicking on that file opens Xcode; but to apply customizations, you need to type commands in the terminal.

* Open Finder
* Navigate to Downloads/BuildLoop and look for your download by name and date
* Open that folder, for example, Downloads/BuildLoop/Loop-220803-1145
* Find the LoopWorkspace folder icon (dashed-blue rectangle)
* Hold down the CTRL key and click (or right-click) LoopWorkspace
* A menu appears - select `New Terminal at Folder` (near the bottom of the list)

This new terminal window is ready to accept commands as needed when the instructions say to start a terminal in the LoopWorkspace folder.

To confirm you are in the correct location, type `pwd` and return in the terminal. The response must end in LoopWorkspace. For example, using the graphic below, the response to `pwd` should be similar to:

`
/Users/marion/Downloads/BuildLoop/Loop-20220803-1145/LoopWorkspace
`

![how to use finder to find the correct download and open xcode](img/finding-loopworkspace.svg){width="750"}
{align="center"}


### Custom Type One LoopPatches

Several items have been consolidated into a set of patches found at [CustomTypeOne/LoopPatches](https://github.com/CustomTypeOne/LoopPatches#readme). These patches only work with Loop 3 (main branch) - note that the README file has not been updated post release of Loop 3 - it will be. You can use the same instructions that worked just before the release when branch of Loop was dev. Ignore the instruction on that page for downloading fresh code with BuildLoopFixedDev.sh. Please download fresh Loop 3 (main) code instead.

Please read the LoopPatches documentation, follow the installation directions carefully and then test any patch that you enable - every time you build. These patches don't have the nice guardrails found in Loop 3.

### Add Libre App to Loop Phone

This method only works for Loop 3 (main branch) and only for some Libre sensors. The US versions for Libre 2 cannot be read with an iPhone.

There are several options for code that will read the raw Libre values and convert them into glucose readings. You must do your own research to decide which code to use. Be aware that you must perform careful calibrations to maintain accurate glucose estimates.

These are the Libre iOS app options.

* xDrip4iOS: [Documentation](https://xdrip4ios.readthedocs.io/en/latest/)
    * Check to see if your sensor is [compatible](https://xdrip4ios.readthedocs.io/en/latest/#compatible-sensors)
    * To use this code with Loop, you must "build it yourself" with the same developer ID as you use with Loop (directions are in the documentation)
    * If you use the TestFlight installation method, you will not be able to use this with Loop (on your phone without needing an internet connection)
* GlucoseDirect: [README file on github repository](https://github.com/creepymonster/GlucoseDirect#glucose-direct)
    * If you use the TestFlight installation method, you will not be able to use this with Loop
* LibreTransmitter for Loop: [README file on github repository](https://github.com/dabear/LibreTransmitter#libretransmitter-for-loop)
    * LibreTransmitter is incorporated into Loop directly, so there not a separate app to be installed
    * Refer to [Modify Loop to use Libre](#modify-loop-to-use-libre)


Once you have chosen the desired app, you need to install it on your Loop phone using the same developer ID as was used for the Loop app and then you must modify the Loop 3 code that you previously downloaded.

### Modify Loop to use Libre

None of these methods have been tested by the LoopDocs team. This information is copied from zulipchat conversations (shown in links below).

!!! warning "Open Loop Suggested during Warmup of New Sensor"
    It is recommended that you use Open Loop during warmup until the new sensor begins to provide reasonable data. This is especially important with European Libre 2 using direct bluetooth connection.

For your selected app to read the Libre, you must also add a client to Loop 3 to interface with the "reader" app. You only need to add the client for the app you've chosen for accessing your Libre sensor. However, you may find watching the video for GlucoseDirectClient and reading the step-by-step instructions for xdrip-client-swift or LibreTransmitter may together give you a better idea how to incorporate your preferred app with Loop 3.

Add a client that interfaces with xDrip4iOS:

* [Add xdrip-client-swift to Loop 3](https://github.com/JohanDegraeve/xdrip-client-swift-1#readme)
    * Note - there are extra details visible when you click on the black arrow icons in this file
    * [zulipchat converstation](https://loop.zulipchat.com/#narrow/stream/144182-development/topic/Libre/near/292280110)


Add a client that interfaces with GlucoseDirect:

* [Add GlucoseDirectClient](https://github.com/creepymonster/GlucoseDirectClient)
    * [zulipchat conversation](https://loop.zulipchat.com/#narrow/stream/144182-development/topic/Libre/near/292307629)
    * The instructions are in the video on the GlucoseDirectClient repo page

Add LibreTransmitter to Loop as a plugin:

* LibreTransmitter for Loop: [README file on github repository](https://github.com/dabear/LibreTransmitter#libretransmitter-for-loop)
    * LibreTransmitter is incorporated into Loop directly, so there not a separate app to be installed
    * [zulipchat conversation](https://loop.zulipchat.com/#narrow/stream/312259-Omnipod-DASH/topic/Libre.20support/near/279078872)
    * The required GetGlucoseFromRaw.swift file is not included in the repository due to legal concerns, so you have to get it from elsewhere
