# Configuring Loop - Services

</br></br>
!!!info ""
    The services listed in this section are **OPTIONAL**.  You can choose to leave them empty and your Loop will still work.

## Nightscout
If you have an existing Nightscout site, add the Site URL and API Secret to have your Loop data transmitted to your Nightscout site. If you can’t remember your API Secret, it can be found under Settings, Reveal Config Vars for Heroku sites (or Application Settings, Connection Strings for Azure sites). 

## mLab
This service integration will add an extra collection to your existing Nightscout mLab for Loop error messages in particular.  The messages stored are the same messages as the Loop user could see on their Loop screen (press the red loop to see your error message), or a  remote parent could see by tapping the Loop pill in Nightscout.  This integration just stores and saves all the error messages throughout time.  As the screen shot below shows, this integration will log the errors from your Loop app and help you troubleshoot if you notice a pattern of problems.

<p align="center">
<img src="../img/mlab_errors.jpg" width="500">
</p> 

**To get your database name:**

If you have Nightscout, access your mLab.  If you manually built your mLab database, you can login to mLab [here](http://mlab.com).  If you had Heroku automatically deploy your site, you can access mLab from your Heroku dashboard. Find the screen, like shown below, to get your database name.  The database name is the part after the “dsXXXXXXX/”.  In this case, “annat1d”  

<p align="center">
<img src="../img/mlab_dbname.jpg" width="500">
</p> 

**To obtain your API Key:**


1) Click your username (not the account name) in the upper right-hand corner to open your account user profile

2) If you are already in the account details page, then click on the row with your username in the Account Users section

3) If the status is showing as “Data API Access: Disabled” in the “API Key” section, click the “Enable Data API access” button

4) Once Data API access is enabled, your current API key will be displayed in the “API key”

If you have any problems with integration, you can try regenerating the API key and that should solve the problem.

<p align="center">
<img src="../img/mlab_api.jpg" width="500">
</p> 

## Loggly
[Loggly](https://loggly.com) is a free logging service.  If you sign up for an account, you'll need to go under Source Setup and then Customer Tokens.  Copy and paste your customer token into your Loop App settings for Loggly.

<p align="center">
<img src="../img/loggly.png" width="500">
</p> 

## Amplitude
[Amplitude](https://amplitude.com) is a remote event monitoring service and can be used to quickly identify errors and events with Loop.  Amplitude stores the events and allows you to view those events as points in time.  To retrieve the details of the events you will need to look at corresponding mLab data entries to get a complete picture of the issues.  If you sign up for a free account with Amplitude, you will be given an API Key that you can enter here to have Loop integration setup.

<p align="center">
<img src="../img/amplitude.png" width="500">
</p> 


