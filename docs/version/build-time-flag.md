## Overview

With Loop 3, some features are enabled or disabled by default but can be modified by adding a "flag" in the LoopConfigOverride.xcconfig file.

## Modify the `Build Time Flags`

The `Build Time Flags` are available for both build methods:

* **Build with Browser**
    * Edit the LoopConfigOverride.xcconfig file in your fork
    * Use the pencil icon in that file to make the modification shown below and commit the change to your fork
    * Do not try to open a pull request to LoopKit/LoopWorkspace - only modify your-github-username/LoopWorkspace version
* **Build with *Mac* Method**
    * You edit the file used to automatically sign all your targets
    * You can edit the version in your LoopWorkspace folder (it shows up as the top item in the Xcode folder view) - or - if you use the build script, you can edit the copy found in ~/Downloads/BuildLoop after the first time you use the script. 
        * If you edit `~/Downloads/BuildLoop/LoopConfigOverride.xcconfig`, the "flags" you add are applied to this download and all subsequent downloads created with the script.

These flags are always capital letters with underscore separating words for clarity, for example `MY_EXAMPLE_FLAG`. If you have more than one flag, they are separated by a space. Do not enter a line break between selections; in other words, do not hit return or enter. Xcode will automatically word-wrap the line for clarity. All values need to be on a single line.

Copy the text below, add it to the end of your LoopConfigOverride.xcconfig file and then insert the desired flags in place of `MY_EXAMPLE_FLAG`. If you want more than one flag, separate them by a space.

``` { .txt .copy title="Lines to add to end of file" }

// Add Build-Time features to compilation conditions
SWIFT_ACTIVE_COMPILATION_CONDITIONS = $(SWIFT_ACTIVE_COMPILATION_CONDITIONS) MY_EXAMPLE_FLAG
```

_Code Before Modification_

```
// Put your team id here for signing
//LOOP_DEVELOPMENT_TEAM = UY678SP37Q
```

The example below is for someone who is using a Free Developer ID - which does not support Siri.

_Code After Modification_

```
// Put your team id here for signing
//LOOP_DEVELOPMENT_TEAM = UY678SP37Q

// Add Build-Time features to compilation conditions
SWIFT_ACTIVE_COMPILATION_CONDITIONS = $(SWIFT_ACTIVE_COMPILATION_CONDITIONS) SIRI_DISABLED
```

## Table of Build Time Flags

|FLAG|PURPOSE|
|---------|---------|
|SIRI_DISABLED|Required to build Loop from Xcode with a free developer account|
|ADULT_CHILD_INSULIN_MODEL_SELECTION_ENABLED|The choice for Child Model is enabled in Therapy Settings. Please read [Enable Child Model](#enable-child-model).|
|REMOTE_OVERRIDES_DISABLED|Remote commands: override, carbs or boluses will not be accepted even if all the [Remote Command](../nightscout/remote-overview.md) requirements are configured<br><br>If you do configure this and later try to set up remote commands, they will not work and there is **no error** message. [Remote Errors: Loop REMOTE_OVERRIDES_DISABLED](../nightscout/remote-errors.md#loop-remote_overrides_disabled)|
|OBSERVE_HEALTH_KIT_CARB_SAMPLES_FROM_OTHER_APPS_ENABLED|Turns on ability for Loop to read third party carb entries. You must also make sure Health permissions allow Loop to read carbs from Health. Be vigilant if you select this; added carbs lead to added insulin dosing when closed loop is enabled|
|SHOW_EVENTUAL_BLOOD_GLUCOSE_ON_WATCH_DISABLED|The Apple Watch screens show current glucose, trend arrow and eventual glucose by default. This flag disables the display of eventual glucose on the watch if you find the display distracting.|
|PREDICTED_GLUCOSE_CHART_CLAMP_ENABLED|[Chart Clamp](#chart-clamp)|
|ALLOW_ALGORITHM_EXPERIMENTS|**dev branch only**<br><br>This is enabled by default to show Algorithm Experiments below the Therapy Settings row. This enables the user to separately enable or disable Glucose Based Partial Application and Integral Retrospective Correction|

### Chart Clamp

What the heck is a chart clamp? It means the range displayed will not be smaller than the clamp but it can be bigger.

Loop automatically scales the glucose charts based on the history shown. Some people don't like to see the vertical axis changing, so they turn on the "clamp".

When the `PREDICTED_GLUCOSE_CHART_CLAMP_ENABLED` build time flag is added:

* the range shown is never smaller than `glucoseChartDefaultDisplayBoundClamped`
* 80 to 240 mg/dL (4.4 to 13.3 mmol/L)

When you do not add that build time flag:

* the range shown is never smaller than `glucoseChartDefaultDisplayBound`
* 100 to 175 mg/dL (5.6 to 9.7 mmol/L)

If glucose within the display history is outside of the bound, the graph range expands to include that glucose level. This prevents glucose readings from being "hidden".

You can customize chart display settings if you want. The original lines of code are shown below. You will need to read the rest of this page to figure out how to modify these to meet what you prefer. If you can't figure this out - reach out for help.

* Module: Loop
* Loop 3
    * Folder: Loop/Models
    * File: LoopConstants.swift
    * Lines: 32 to 45

```
    // MARK - Display settings

    static let minimumChartWidthPerHour: CGFloat = 50

    static let statusChartMinimumHistoryDisplay: TimeInterval = .hours(1)

    static let glucoseChartDefaultDisplayBound =
        HKQuantity(unit: .milligramsPerDeciliter, doubleValue: 100)...HKQuantity(unit: .milligramsPerDeciliter, doubleValue: 175)

    static let glucoseChartDefaultDisplayRangeWide =
        HKQuantity(unit: .milligramsPerDeciliter, doubleValue: 60)...HKQuantity(unit: .milligramsPerDeciliter, doubleValue: 200)

    static let glucoseChartDefaultDisplayBoundClamped =
        HKQuantity(unit: .milligramsPerDeciliter, doubleValue: 80)...HKQuantity(unit: .milligramsPerDeciliter, doubleValue: 240)
```

### Enable Child Model

Loop 3, by default, does not include the concept of child versus adult for rapid-acting insulin, i.e., Humalog, Novalog and Apidra.

* The child model can be enabled following the directions above, adding ADULT_CHILD_INSULIN_MODEL_SELECTION_ENABLED to the LoopConfigOverride.xcconfig file and rebuilding
* Insulin Model is then found in the Therapy Setting section of Loop 3 with Adult selected by default
* Insulin Type continues to be associated with the pump and can be modified in the Pump Settings screen
