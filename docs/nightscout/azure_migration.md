# Migrating from Azure to Heroku

If you are a current Azure user who wants to move to Heroku, but not lose all your old NS data, you will need do the following steps:

* update your repository in GitHub
* create a new heroku nightscout site
* migrate your mLab database to new site

## Updating your repository in GitHub

* Copy, paste, and goto the one of the following links depending on which branch of cgm-remote-monitor you are currently running (replace `yourgithubname` with your actual GitHub user name)

for **master** branch deployments:

`https://github.com/yourgithubname/cgm-remote-monitor/compare/master...nightscout:master`

For **dev** branch deployments:

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

## Heroku Nightscout Site Setup

* Create an account at [Heroku](https://www.heroku.com) and choose the Primary Development Language to be Node.js when you create your account.  You’re going to use a free account, but you will still need to enter credit card information for your account setup.  Don’t forget to check your email to confirm your Heroku account.

<p align="center">
<img src="../img/heroku_signup.jpg" width="450">
</p> 

* Go to your Nightscout cgm-remote-monitor repository in GitHub (https://github.com/yourGitHubname/cgm-remote-monitor)

* Scroll down until you see the purple `Deploy to Heroku` button.  Click that button.


<p align="center">
<img src="../img/deploy_heroku.jpg" width="450">
</p> 

* Give your app a name, this will be the prefix of your NS site’s URL. For example, `https://yourappname.herokuapp.com`

* Fill out the information lines in the `Config Variables` Section of that page, as shown below.  Some of the lines can stay with the default entries already provided.

<table>
<thead>
<tr>
<th>KEY</th>
<th>VALUE</th>
</tr>
</thead>
<tbody>
<tr>
<th>API_SECRET</th>
<td>Create your own API_SECRET…this is like the password to your NS site.  Please write it down somewhere safe or commit it to memory, you will be using it in the future.  It needs to be at least 12 characters long and should NOT use the `@` symbol.</td>
</tr>
<tr>
<th>DISPLAY_UNITS</th>
<td>enter either mg/dl or mmol</td>
</tr>
<tr>
<th>ENABLE</th>
<td>bridge loop pump iob cob basal careportal sage cage</br></br>(Enter all of the words without commas.  Just a single space between each word. Make sure autocorrect does not add space between careportal)</td>
</tr>
<tr>
<th>DISABLE</th>
<td>Leave blank</td>
</tr>
<tr>
<th>ALARM_TYPES</th>
<td>simple</td>
</tr>
<tr>
<th>BG_HIGH</th>
<td>Enter the numeric value of BG you’d like as an urgent high alarm.</td>
</tr>
<tr>
<th>BG_TARGET_TOP</th>
<td>Enter the numeric value of the top of your target BG.</td>
</tr>
<tr>
<th>BG_TARGET_BOTTOM</th>
<td>Enter the numeric value of the bottom of your target BG.</td>
</tr>
<tr>
<th>BG_LOW</th>
<td>Enter the numeric value of the BG you’d like as an urgent low alarm.</td>
</tr>
<tr>
<th>PUSHOVER lines</th>
<td>Can be left blank for now.   See PUSHOVER section if you want to integrate PUSHOVER notifications with NS later.</td>
</tr>
<tr>
<th>CUSTOM_TITLE</th>
<td>This will be the text displayed in the upper left part of the NS website.</td>
</tr>
<tr>
<th>THEME</th>
<td>change from default to colors</td>
</tr>
<tr>
<th>BRIDGE_USER_NAME</th>
<td>Enter your Dexcom Share Account login name.  This should be the same account name used in the Share2 or G5 Mobile app.</td>
</tr>
<tr>
<th>BRIDGE_PASSWORD</th>
<td>Enter your Dexcom Share Account password.</td>
</tr>
<tr>
<th>BG_TARGET TOP</th>
<td>Enter the numeric value of the top of your target BG.</td>
</tr>
<tr>
<th>BG_TARGET_BOTTOM</th>
<td>Enter the numeric value of the bottom of your target BG.</td>
</tr>
</tbody>
</table>

**The remaining variables can be left at their default values.**</br></br>

* Click the purple `Deploy` button at the bottom of screen

<p align="center">
<img src="../img/deploy_button.jpg" width="450">
</p> 

* Wait a little bit while Heroku builds your NS app.  You’ll see some text scroll by in the Build App box, and then finally, you will have a message that the NS app was successfully deployed.

<p align="center">
<img src="../img/deploy_success.jpg" width="450">
</p> 

* You can verify your site’s successful build by clicking `View` (you should see black site with a profile warning).  You will be redirected to a profile set-up page.  (If it doesn't redirect automatically, refresh your webpage).  

<p align="center">
<img src="../img/no_profile.jpg" width="450">
</p> 

You do not have to enter all the information in the profile if you are using Loop (since Loop will be providing the information for IOB and COB rather than letting NS calculate them), but you do have to fill out the `Basal Profile` and `TimeZone` at a minimum in order to have your temp basals properly display.  Click `Save` when you have entered the information.  You will be prompted to authenticate, if it is the first time you’ve used the device to make changes in your profile.  Click on the `Authenticate` link at the bottom of the site, and enter your API_SECRET to complete the authentication.

<p align="center">
<img src="../img/profile.jpg" width="450">
</p> 

* Assuming your previous browser tab is still open for "Create a new App | Heroku", let's go back to that tab.  This time instead of choosing the `View` option, we are going to select the `Manage App` button. Then, select the `Settings` tab near the top of the screen on your Heroku app.

<p align="center">
<img src="../img/settings_heroku.jpg" width="450">
</p> 

* Click on `Reveal Config  Vars`. Scroll down the bottom of the Config Vars lines until you find the last blank one.  You are going to add several additional lines of config vars for Loop use; the DEVICESTATUS_ADVANCED is a required line, the others just make Nightscout more useful when Looping.

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

The remaining variables can be left at their default values.</br></br>

* Click on `Open App` in the top right corner of your Heroku site.

<p align="center">
<img src="../img/open_app.jpg" width="450">
</p> 

* Click on the settings (those three horizontal lines in upper right corner).  Now check that your basal render is selected to either default or icicle (personal preference for how the temp basals show as blue lines in NS site), check the boxes that you’d like display pills in the SHOW PLUGINS (usually all of them), and then press save. Your new Nightscout site is all set-up.  Congrats!

<p align="center">
<img src="../img/settings_ns.jpg" width="450">
</p> 


## Migrate mLab database

If you’d like to seamlessly keep all your old Azure NS data showing in your new Heroku NS site, you’ll need to copy and paste your old `MONGODB` string from your Azure site.  Find it in either Application Settings or Connection strings in your Azure control panel and then go to Heroku’s `MONGODB_URI` line.  Replace the content with your copied string from Azure.  Double check that your Azure collection used the “entries” name…if it doesn’t, then you will need to update that variable in Heroku to match as well.

<p align="center">
<img src="../img/mongo.jpg" width="450">
</p> 

## EVENT HISTORY

Don't forget to keep you Loop App's Preferred Source set to `Event History` if you want your NS site to smoothly integrate.  Preferred Source set to `Reservoir` will result in carbs not being uploaded and temp basals not being displayed.







