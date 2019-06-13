# Setup Troubleshooting

If you have just tried to setup your Nightscout site and have problems with seeing all your data, please checkout the information below.

## Dexcom data not showing

If you are using a Dexcom system, and your data is not appearing in Nightscout, there are only a limited number of reasons for that. You should check your (1) Heroku settings and (2) Dexcom Share.

NOTE: The #1 reason why BGs aren't showing is because you have mismatched password and user names in Heroku settings and Dexcom. Please see blue box below for that error.

### Heroku Settings

From within Heroku settings, under `Config Vars` double check the following:

1. You must use the same `BRIDGE_PASSWORD` or `BRIDGE_USER_NAME` that your Dexcom mobile app is using.
2. You must have `bridge` and/or `careportal` on the ENABLE line in Heroku settings (you can have other values there...but don't forget these two).
3. If you are outside the USA, you must add `BRIDGE_SERVER` set to `EU` in Heroku settings.
4. Your `careportal` must be one word in the ENABLE line, sometimes autocorrect makes it two words.
5. If using `mmol`, make sure you have spelled that value correctly in the `DISPLAY_UNITS`.

<p align="center">
<img src="../img/bridge-settings.jpg" width="800">
</p> 

!!!info "About your Bridge password and user name"
    The `BRIDGE_PASSWORD` and `BRIDGE_USER_NAME` are NOT visible from within your Dexcom mobile app or online account. The values of them are what you entered into your Dexcom mobile app when you VERY FIRST logged into that app however long ago. If you have double-checked everything else that could be incorrect and BGs still aren't showing in Nightscout, then you likely have those Bridge values incorrect. To fix that, delete your Dexcom app (don't stop the session before deleting the app...just keep it going). Download the app again from the iPhone's App store and login to the freshly-downloaded Dexcom app. **Take note** that deleting the app will not stop your session, your session will pick right back up once the transmitter pairs again. The `BRIDGE_USER_NAME` is not an email address. Use that exact same login now in your Heroku settings.

### Dexcom Share
Make sure you have Dexcom Share turned ON in your Dexcom app. In the Dexcom app's main screen, find the triangle made of dots. If the dots are grey, you do not have Share turned on. Tap the triangle, and follow the directions to add a follower (yourself if you don't have someone else you'd like to invite) and turn on Share.

<p align="center">
<img src="../img/sharing.jpg" width="250">
</p>

## Loop data not showing

If your Loop data is not showing in Nightscout, please delete your Nightscout account in Loop settings area. Enter the information in freshly. Make sure to use `https://` to start the site URL. Make sure you have `loop` on the ENABLE line in Heroku settings. Finally, make sure your Loop app is still set to `Event History` from within the pump's section in Loop settings.
