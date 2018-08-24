# Configuring Loop - Services

</br></br>
!!!info ""
    The services listed in this section are **OPTIONAL**.  You can choose to leave them empty and your Loop will still work.

## Nightscout
If you have an existing Nightscout site, add the Site URL and API Secret to have your Loop data transmitted to your Nightscout site. If you can’t remember your API Secret, it can be found under Settings, Reveal Config Vars for Heroku sites (or Application Settings, Connection Strings for Azure sites). 

The two most common errors in filling out this section are:

1. Failure to use `https://`  in the site URL.  If you use `http://` (see how that doesn't have the "s" at the end?), you will get an error message about a App Transport Security policy.  Take a look at the example site in the field before you start filling in that line, if you want an example.</br></br>
2. Having a trailing slash on the end of the URL.  If you copy and paste from a web browser, make sure to delete the trailing slash on the URL entry.

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


