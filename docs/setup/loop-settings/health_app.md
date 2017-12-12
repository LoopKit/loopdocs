## Health App

Loop app uses the iPhone's Health app to store BGs, insulin, and carbohydrate data.  You'll need to setup a few basics to allow Loop access to the Health app.  Additional details about how to use the Health app to interpret your longer term looping data can be found [here](https://loopkit.github.io/loopdocs/oepration/features/healthapp.md/) in the Operation section of these docs.

### Blood Glucose data

When you first build the Loop app onto your phone, you will be prompted if you want to allow the Loop app access to read/write Blood Glucose data into the Health app.  You will want to click on the line that says `Turn All Categories On` and then click on the `Allow` button.  If you accidentally said no, you will want to go back into the Health app and change that setting.

<p align="center">
<img src="../img/healthapp.png" width="550">
</p>

You will also want to enable your Dexcom app to write to the Health app.  You can find this in your G5 app's Settings, under Health.  Click on the `Enable` button and then `Turn All Categories On` so that the toggle for allowing dexcom to write data is now a green color.  By enabling this setting, Loop will display BGs older than three hours in the Loop's main BG chart.

<p align="center">
<img src="../img/health_g5.jpg" width="550">
</p>
</br></br>

### Carb data
Later in the configuration of your Loop app, when you first setup carb ratios, you will again be prompted whether to allow Loop app access to read/write to the Health app.

As shown in the first screenshot above, turn on circled the slider for turning on Loop's ability to Write data.

### Insulin data

New to iOS 11, Loop app will now be able to write insulin delivery to your Health app.  This can provide a nice integration for helping you watching total daily insulin use,

When all your settings are input correctly, your Health app settings should look like the following:

<p align="center">
<img src="../img/healthapp.jpg" width="350">
</p>
