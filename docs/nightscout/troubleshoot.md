## Setup Troubleshooting

If you have just tried to set up your Nightscout site and have problems with seeing all your data, please check out the [Nightscout: Troubleshooting](https://nightscout.github.io/troubleshoot/troubleshoot)  page.

## Dexcom data not showing

If you use a Dexcom and get your CGM data into Nightscout using Dexcom Share (bridge in Nightscout) and everything is working but the Dexcom data stops showing, please review [Nightscout: Dexcom bridge Troubleshooting](https://nightscout.github.io/troubleshoot/dexcom_bridge/).

As part of that troubleshooting, you may need to remove the Nightscout service credentials from Loop. You may need to remove Dexcom credentials from all third-party apps that get data from Dexcom Share. Be sure to add them back after the CGM data to Nightscout is restored.

You do not need to use Share or bridge with Nightscout. You can choose to have Loop update your CGM readings to Nightscout directly. There's a check box in the Loop CGM setting screen to select this. You must select that check box every time you update your transmitter for Dexcom G5 or G6.

## Loop data not showing

If your BG data is showing, but Loop data is not (like Loop pill is empty and carbs and boluses are not showing), please delete your Nightscout account in Loop settings area. Enter the information in Loop again. Make sure to use `https://` to start the site URL. Make sure there is no trailing slash at the end of the URL. Enter your API_SECRET correctly. Make sure you have `loop` on the ENABLE line in Heroku settings.
