# Overview

Nightscout (NS) is an excellent tool to remotely view Loop's actions.  It allows for easy remote monitoring of Loop activities, troubleshooting of Loop errors, history of CGM, carbs, boluses, & temp basals, reports to analyze data trends and patterns. There is a Nightscout app in your iPhone App Store, or you can use a web browser to view the data.  Setting up Nightscout is free and fairly quick.  Once setup, the site can be accessed by anyone that you share your unique Nightscout URL with.  

Nightscout is highly recommended for Loop users, especially those using Loop as caregivers to t1ds.  Nightscout displays are often the easiest way to troubleshoot Loop settings, if you are having problems and seeking input from others.  Below is some discussion about the general Nightscout display, as well as some Loop-specific display information.

<p align="center">
<img src="../img/example.jpg" width="600">
</p> 

</br>
<dl>
<dt>Blood Glucose</dt>
<dd>Your blood glucose (BG) readings from your CGM are shown in green, yellow, or red in the main graph area of NS.  You can adjust your high and low BG targets in NS (when NS alerts will start for high/low BGs), but those will not affect your Loop performance.  Loop only uses the BG targets given in the Loop app settings.  The main screen of BGs is displaying the time duration you have selected (in the example above, 12 hours of BG history).  The bottom of the screen shows the last 48-hours of BG trends.  You can scan backwards by dragging the bottom timeline to the left, if you want to review specific Loop actions or data in the last two days. </dd>
</br>
<dt>Carbs</dt>
<dd>Carbs are automatically uploaded to NS by the Loop app.  The amount of carbs on board (active carbs or COB) can be seen by clicking the Loop pill.  The size of a white carb dot on the graph is proportional to the amount of carbs entered...bigger meals get bigger dots. Loop does not read carbs from NS for use in looping caluclations, it only uploads carbs to NS that have been entered in the Loop app.</dd>
</br>
<dt>Boluses</dt>
<dd>Insulin boluses are also automatically uploaded to NS by the Loop app.  The bolus is shown as a filled in blue lower-half of the dot, and the specific amount of the bolus is also shown.  There may be a slight delay between when the carbs for a meal are uploaded to NS to when the meal bolus appears.  This is because depending on the pump model and size of bolus, the bolus may take a few minutes to actually be given and then Loop has to perform a pump read to verify the reservoir volume has decreased (i.e., the bolus was given).  As shown in the example above, the meal carbs have been uploaded, but the bolus delivery is still in progress.  Insulin on board (active insulin or IOB) is also shown in the Loop pill.</dd>
</br>
<dt>Temp Basals</dt>
<dd>Within your NS profile, you will enter in the scheduled basal for your t1d.  This is not automatically updated when you update the Loop app or your pump; you will have to manually update your basal profile in your NS site if you change your basal profile in Loop and/or pump.  If you don't update the NS basal profile, it doesn't cause any problems in Loop function...you simply won't have accurate VISUAL representation of high/low temp basals within NS. The dashed blue line represents the scheduled basal profile (as entered in your NS profile).  The solid blue lines indicate the actual basal amounts set for a given time...so as Loop sets temp basals higher or lower than your scheduled basal rate, the solid blue line will jump above or below your dashed blue line.  There is a slight delay (up to 2-5 minutes) in the rendering of basal changes on the blue lines, so if you want the accurate current basal rate, you can check the Loop pill.</dd>
</br>
<dt>Predicted BG</dt>
<dd>The purple line to the right of the BG is Loop's predicted BG.  Watching the behavior of that purple line can help you understand why Loop is making decisions regarding high or low temps.  You can read more on that topic in the Algorithm section of these docs.</dd>
</br>
<dt>Loop pill</dt>
<dd>The Loop pill is the little display box which when hovered over, or clicked, will provide additional information about recent Loop activities and status.  Information included is the last time Loop ran, the temp basal set, IOB, and COB.  Looking at the Loop pill is a quick method for assessing if you loop is currently active, as well.  The small symbols to the right of the word Loop have specific meaning.  The small horizontal lightning bolt, shown in this example, is an active loop which recently enacted a temp basal.  You can read the section on Troubleshooting using the Loop Pill for additional information about the various symbols.</dd>
</br>
<dt>SAGE and CAGE pills</dt>
<dd>The SAGE and CAGE pills are for Sensor Age and Cannula Age.  These optional pills track the time since your CGM sensor and Pump site were last changed.  You can set up custom alerts to remind you when it is time to change the devices, or simply use the visuals to keep track of your particular timing for site/sensor changes.</dd>
</dl>
