# Apple Watch

<p align="center">
<img src="../img/watch.png" width="150">
</p>


If you add an Apple Watch after building Loop, you will need to pair your watch to your iPhone and then rebuild Loop to enable the Loop watch app to show up as an available watch app.

Loop is currently supported with all released versions of the Apple Watch and Apple watchOS 4.  Cool factor is increased since the Loop user can directly enter carbs and boluses straight from the watch, without needing to access the iPhone.  The Loop watch app shows the Loop status, current BG, eventual BG, carb tool, and bolus tool.

By tapping on the carb or bolus tools, you can adjust the entries using the crown to dial in more/less.  The default installation of the Loop's watch app autofills in 75% of the recommended bolus, and you can manually scroll to get the full bolus amount.  Please check the [Apple Watch customizations section](/setup/build/code_customization.md#apple-watch-customizations) if you wish to change that to 100% recommended bolus as the initial autofill.

A loop complication exists to show BG on the watchface but the update rate is limited to ~30mins due to limitations imposed by apple to increase battery life. If constant, real-time monitoring is desired, you should use the Loop app as the main screen. This can be achieved by setting the watch to always show last opened app on wake. Loop will always have to be the last app opened for this to work.  (Note: recent watchOS seems to be a bit flakey on actually bringing up the last app used, and instead often defaults to the user's watchface instead.  If you have a Loop complication installed in the watchface, you can simply tap the complication to open Loop's watch app.)


