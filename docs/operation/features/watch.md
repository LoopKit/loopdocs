## Apple Watch

The Loop user can directly enter carbs and boluses and turn on or off premeal or override settings from the watch, without needing to access the iPhone.

![img/watch.png](../../img/watch_updated_loop.svg){width="300"}
{align="center"}

There are two screens in the Loop watch app. By swiping left or right, the other screen is displayed.

The screen in the left side of graphic above shows Loop status, current BG, arrow, eventual BG (can be turned on and off as a feature in Loop 3), carb tool, bolus tool, premeal icon and override icon. If necessary, use the crown (or swipe up and down) to see the full display.

After tapping on the carb or bolus tools, you can adjust the entries using the crown to dial in more/less.

* The carb tool allows you to choose the amount, absorption time using the standard icons and adjust the time the carbs are planned to be consumed. After tapping continue on the carb screen, the meal bolus screen is displayed - carbs are only saved after selecting Save or Save and Bolus on the meal bolus screen.
* The bolus tool displays the recommended bolus. If you want to decrease/increase from the recommended amount, use the digital crown or tap on +/- icons to modify.
* Once the bolus button is tapped, the bolus command is only delivered after the user turns the digital crown (as directed) to align the two triangles.
* If you tap Save and Bolus on the bolus screen when entered from the carb screen AND then fail to turn the digital crown to confirm the bolus, that means the bolus was not delivered but the carbs were saved.

If you swipe the Apple Watch Loop screen from right-to-left, a second screen, as displayed on the right side of the graphic above, is available.  This second screen displays a graph of recent BG and predicted BG data.  The crown can be turned to display IOB, COB, Net Basal Rate (with respect to scheduled rate) and in some cases Reservoir Units.  (A recently changed pod may show the reservoir level from the prior pod - just ignore that. It goes away within 24 hours.)

A loop complication exists to show BG on the watch face but the update rate is limited by Apple. If you have a Loop complication installed in the watch face, you can simply tap the complication to open Loop's watch app.

## Watch Hardware and OS Requirements

If you add an Apple Watch after building Loop using Xcode on a computer, you will need to pair your watch to your iPhone and then rebuild Loop to enable the Loop watch app to show up as an available watch app.

Loop is currently supported with all released versions of the Apple Watch and Apple watchOS 4.1 and newer.

The next version of Loop, currently Loop-dev, will require newer versions of the watch and require watchOS 8 as a minimum.

### watchOS 8 compatibility:

watchOS 8 requires iPhone 6s or later with iOS 15 or later and one of the following Apple Watch models:

* Apple Watch Series 3.
* Apple Watch Series 4.
* Apple Watch Series 5.
* Apple Watch SE.
* Apple Watch Series 6.
* Apple Watch Series 7.
* Not all features are available on all devices.

