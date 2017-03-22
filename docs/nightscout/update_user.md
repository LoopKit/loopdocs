# UPDATING NIGHTSCOUT SITE

If you are new to Loop and haven’t updated your NS site since before December 1, 2016, you will want to update your NS site.  You can run either the "master" or "dev" branches of cgm-remote-monitor with Loop.  To check what version your Nightscout site is running, go to your Nightscout site and pull open the site settings by clicking on the three horizontal lines at the top right of the screen.  Scroll down and see if you are running 0.9.2-dev-20161201 or newer for "dev" branch.  Notice the “dev” branch is date stamped 0.9.x-dev-YYYMMDD; or you’ll see version 0.9.2 for "master" branch deployments.

If you are a current NS user and simply want to update your site, this procedure will work as well.

## Updating your repository in GitHub

* Copy, paste, and goto the one of the following links depending on which branch of cgm-remote-monitor you are currently running (replace `yourgithubname` with your actual GitHub user name)

for master branch deployments:

`https://github.com/yourgithubname/cgm-remote-monitor/compare/master...nightscout:master`

For dev branch deployments:

`https://github.com/yourgithubname/cgm-remote-monitor/compare/dev...nightscout:dev`


<p align="center">
<img src="../img/compare_repo.jpg" width="450">
</p> 

* Click the big green `Create pull request` button. Another screen will appear, fill in a title and click button to create the pull request, and then you can `Merge pull request`, and finally `Confirm merge`.
*********
<p align="center">
<img src="../img/update1.jpg" width="450">
</p> 
*********
<p align="center">
<img src="../img/update2.jpg" width="550">
</p> 
**********
<p align="center">
<img src="../img/update3.jpg" width="550">
</p> 
**********

* Your cgm-remote-monitor repository is now up-to-date.  Nice work.

* If you don’t have your Heroku set-up to automatically update when your repository is updated, you may have to go into your Heroku `Deploy` section and manually deploy your branch now that your repository has been updated.  Make sure you are connected to your GitHub cgm-remote-monitor repository.

<p align="center">
<img src="../img/deploy_branch.jpg" width="450">
</p>

## New Loopers Variables

For new Loopers (but old Nightscout users), you will need to add some variables to your Heroku site to Loop.  

* Login to your Heroku site, select the `Settings` tab near the top of the screen on your Heroku app.

<p align="center">
<img src="../img/settings_heroku.jpg" width="450">
</p> 

* Click on `Reveal Config  Vars`.  Scroll down the bottom of the Config Vars lines until you find the last blank one.  You are going to add several additional lines of config vars for Loop use; the DEVICESTATUS_ADVANCED and ENABLE lines are required, the others just make Nightscout more useful when Looping.

<p align="center">
<img src="../img/add_vars.jpg" width="450">
</p> 

<table>
<thead>
<tr>
<th>KEY</th>
<th>VALUE</th>
</tr>
</thead>
<tbody>
<tr>
<th>DEVICESTATUS_ADVANCED</th>
<td>true</td>
</tr>
<tr>
<th>PUMP_FIELDS</th>
<td>battery reservoir clock status</td>
</tr>
<tr>
<th>PUMP_RETRO_FIELDS</th>
<td>battery reservoir clock status</td>
</tr>
<tr>
<th>SHOW_FORECAST</th>
<td>loop</td>
</tr>
<tr>
<th>SHOW_PLUGINS</th>
<td>loop pump cob iob sage cage careportal</td>
</tr>
<tr>
<th>PUMP_ENABLE_ALERTS</th>
<td>true</td>
</tr>
<tr>
<th>PUMP_URGENT_BATT_U</th>
<td>30</br></br>(This is the pump battery percentage that will trigger a red, urgent alert in NS.)</td>
</tr>
<tr>
<th>PUMP_URGENT_BATT_V</th>
<td>1.25</br></br>(This is the pump battery voltage that will trigger a red, urgent alert in NS.)</td>
</tr>
<tr>
<th>PUMP_URGENT_RES</th>
<td>10</br></br>(This is the reservoir volume that will trigger a red, urgent alert in NS.)</td>
</tr>
<tr>
<th>PUMP_URGENT_CLOCK</th>
<td>30</td>
</tr>
<tr>
<th>LOOP_ENABLE_ALERTS</th>
<td>true</td>
</tr>
<tr>
<th>LOOP_WARN</th>
<td>20</br></br>(This is the minutes since Loop last successfully looped, the t1d will have a similar notification at this time through the Loop app.  This will be a yellow alert in NS.)</td>
</tr>
<tr>
<th>LOOP_URGENT</th>
<td>60</br></br>(Same as the alert above, but will be red in color and have a shorter snooze option.)</td>
</tr>
</tbody>
</table>

* Click on `Open App` in the top right corner of your Heroku site.

<p align="center">
<img src="../img/open_app.jpg" width="450">
</p> 

* Click on the settings (those three horizontal lines in upper right corner).  Now check that your basal render is selected to either default or icicle (personal preference for how the temp basals show as blue lines in NS site), check the boxes that you’d like display pills in the SHOW PLUGINS (usually all of them), and then press save.  Your NIGHTSCOUT site is all set-up.  Congrats!

<p align="center">
<img src="../img/settings_ns.jpg" width="450">
</p> 

* Double check that your NS Profile settings are current and that you have a basal profile entered, if you want to see the temp basals that Loop is setting.

## EVENT HISTORY

Don't forget to keep you Loop App's Preferred Source set to `Event History` if you want your NS site to smoothly integrate.  Preferred Source set to `Reservoir` will result in carbs not being uploaded and temp basals not being displayed.

