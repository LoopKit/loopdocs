# Setup Troubleshooting

If you have just tried to set up your Nightscout site and have problems with seeing all your data, please check out the [Nightscout General Troubleshooting pages](https://nightscout.github.io/troubleshoot/troublehoot).

## Dexcom data not showing

If you use a Dexcom and everything was working but the Dexcom data stops showing, please review the [Nightscout: No Data in NS Troubleshooting section](https://nightscout.github.io/troubleshoot/troublehoot/#no-data-in-nightscout).

As part of that troubleshooting, you may need to remove the Nightscout service credentials from Loop.  You may need to remove Dexcom credential from all third-party apps that get data from Dexcom Share.  Be sure to add them back after the CGM data to Nightscout is restored.


## Loop data not showing

If your BG data is showing, but Loop data is not (like Loop pill is empty and carbs and boluses are not showing), please delete your Nightscout account in Loop settings area. Enter the information in fresh. Make sure to use `https://` to start the site URL. Make sure there is no trailing slash at the end of the URL. Enter your API Secret correctly. Make sure you have `loop` on the ENABLE line in Heroku settings.
