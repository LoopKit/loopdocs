## *Loop* data is not showing in *Nightscout*

* This is a&nbsp;_<span translate="no">Loop</span>_&nbsp;and/or *Nightscout* issue, not related to remote configuration
    * Review the [LoopDocs: *Nightscout* with&nbsp;_<span translate="no">Loop</span>_](update-user.md) page
    * Check out links on the [LoopDocs: *Nightscout* Troubleshooting](troubleshoot.md) page
* Make sure the Looper's phone is connected to the internet so it can upload to *Nightscout*

## Remote Commands Stopped Working

This section is for people who were using remote commands and they suddenly stopped working.

If you are using LoopCaregiver, try the remote command directly from Nightscout to see if they work there. If they are not working there as well, check out your account status first before attempting the fixes on the rest of this page.

* Your *Apple Developer* account must be in good standing for the push notifications to work
* Log in to your [*Apple Developer* account](https://developer.apple.com/account) and see if there are agreements you need to accept

## Improper Configuration

### *Nightscout* Config and *Loop* Build Method

Ensure your *Nightscout* version is at least 14.2.6.

Verify that you performed all the [Remote Configuration](remote-config.md) steps for the *Nightscout* site, including sending an override from the&nbsp;_<span translate="no">Loop</span>_&nbsp;phone to *Nightscout*.

#### BadDeviceToken

When the *Nightscout* config var LOOP_PUSH_SERVER_ENVIRONMENT does not match the&nbsp;_<span translate="no">Loop</span>_&nbsp;app build method; the error message contains the phrase `APNs delivery failed: BadDeviceToken`.

* If&nbsp;_<span translate="no">Loop</span>_&nbsp;was installed remotely (typically from TestFlight following GitHub Browser Build), you **must** have *Nightscout* config var `LOOP_PUSH_SERVER_ENVIRONMENT` set to `production`
* If&nbsp;_<span translate="no">Loop</span>_&nbsp;was built using *Mac*, you **cannot** have `LOOP_PUSH_SERVER_ENVIRONMENT` as one of your *Nightscout* config vars

If you attempt to issue a command from *Nightscout* Careportal; after you hit submit and then OK, you will see the error message:

```
Error: APNs delivery failed: BadDeviceToken
```

If you attempt to issue a command using *LoopCaregiver*; after you authenticate the command, you will see the error message listed below and shown in the screenshot.

```
HTTP Error
Status Code: 500
body: APNs delivery failed: BadDeviceToken
```

![site and build method mismatch](img/site-build-mismatch.png){width="300"}
{align="center"}

### *Loop* `REMOTE_OVERRIDES_DISABLED`

You can build Loop with [Build-Time Features](../version/build-time-flag.md) as part of code customization.

If you added this Build-Time Flag: `REMOTE_OVERRIDES_DISABLED`

You will not see any errors, but nothing will happen when you issue any kind of remote command.

**Solution**: Remove `REMOTE_OVERRIDES_DISABLED` from `LoopConfigOverride.xcconfig` file and rebuild the&nbsp;_<span translate="no">Loop</span>_&nbsp;app.

### Incorrect Password (OTP) Error

The references to ‘caregiver’ below refer to the person sending the commands. You must have the&nbsp;_<span translate="no">Loop</span>_&nbsp;phone with you to troubleshoot this problem.

* The Apple clock should be set to automatic on both the Looper's phone and the caregiver’s device.
    * If the clock is incorrect, even slightly, remote commands will fail.
* Check if One-Time Passwords (OTP) align between *LoopCaregiver* and&nbsp;_<span translate="no">Loop</span>_.
    * In&nbsp;_<span translate="no">Loop</span>_: Settings -> Services -> *Nightscout*
    * In *LoopCaregiver* : Settings -> Tap on Looper's Name
    * Observe the 6-digit OTP as they change
* If the OTPs don't match, you can reset it:
    * **Warning**: If there are multiple devices (or people) sending remote commands, this procedure **resets the OTP for all**
    * _<span translate="no">Loop</span>_: Settings -> Services -> *Nightscout* -> One-Time Password -> Tap Reload button
        * The QR code is different as soon as you hit `Reload`
    * *LoopCaregiver*: Delete the Looper's profile from *LoopCaregiver* and add the Looper again by scanning their new QR code
    * Authenticators for every device used to send remote commands must be updated
        * Delete the OTP configuration
        * Add the new QR code

## Undelivered or Expired Commands

Apple push notifications may not always reach your app due to various settings or Apple's intentional limitations. This issue can manifest in several ways:

* The push notification banner never appears on the Looper’s device.
* The push notification banner appears, but nothing happens in&nbsp;_<span translate="no">Loop</span>_&nbsp;(no error or success message afterward).
* An error message in *Nightscout* or *LoopCaregiver* indicates the Password (OTP) is expired.

While&nbsp;_<span translate="no">Loop</span>_&nbsp;cannot control the timely delivery of push notifications, there are several steps you can take to mitigate these issues. Note that rebuilding&nbsp;_<span translate="no">Loop</span>_&nbsp;or *LoopCaregiver* generally will not resolve the problem.

Check these items on the Looper’s phone, not the caregiver's.

1. Reboot the phone.
1. Wait 24 hours as it often takes time for the push notification limits to reset.
1. Limit the number of&nbsp;_<span translate="no">Loop</span>_&nbsp;commands you send in a short period.
    * Apple may throttle notifications if too many are received.
    * Sending no more than 1 or 2 per hour may help.
1. Disable notifications from other apps.
    * It is possible that other apps can cause the system to throttle all notifications, including&nbsp;_<span translate="no">Loop</span>_.
1. Enable Time Sensitive Notifications:
    * Apple Settings -> Notifications ->&nbsp;_<span translate="no">Loop</span>_.
    * Turn on “Allow Notifications”.
    * Turn on “Time Sensitive Notifications”.
1. Upgrade *Nightscout*:
    * *Nightscout* version 15.0 (released late 2023) and greater supports time sensitive notifications.
    * This can help iOS to deliver remote notifications faster.
1. Adjust Focus Modes:
    * For all focus modes, make sure&nbsp;_<span translate="no">Loop</span>_&nbsp;is listed as an app allowing Notifications.
    * Apple Settings -> Focus
    * Select the focus mode (e.g., Do Not Disturb, Sleep).
    * Under “Allow Notifications,” tap “Choose Apps”.
    * Add&nbsp;_<span translate="no">Loop</span>_&nbsp;to the list.
1. Turn on Background App Refresh:
    * Apple Settings -> General -> Background App Refresh
    * Select “On” at the top.
    * Activate the&nbsp;_<span translate="no">Loop</span>_&nbsp;toggle in the list.
1. Try using Wi-Fi instead of cellular if possible:
    * Apple may not deliver notifications on cellular as often as on Wi-Fi.
1. Charge the phone:
    * If the battery is low, iOS may not deliver notifications to save battery life (e.g., while on Low Power mode).

## How to Ask for Help

This is helpful information to share when requested by helpers. If you are not using *LoopCaregiver*, review the response seen on the *Nightscout* site.

1. Activate an override from within&nbsp;_<span translate="no">Loop</span>_. Does *Nightscout* show the active override?
1. Activate an override from *Nightscout*. Does it change the active override in&nbsp;_<span translate="no">Loop</span>_?
1. Do errors show in *LoopCaregiver* or *Nightscout* Careportal when you send a remote command?
    * In both *Nightscout* and *Caregiver*, you can tap on an error to read specific error details.
    * Share screenshots of errors
1. What&nbsp;_<span translate="no">Loop</span>_&nbsp;version are you using? Released (main) or development (dev)? Approximately when did you update last?
    * The minimum version that supports remote bolus and carbs is&nbsp;_<span translate="no">Loop</span>_.
1. What iOS version is being used on the Looper’s device?
1. How did you build&nbsp;_<span translate="no">Loop</span>_?
    * Web browser using GitHub Actions?
    * Xcode?
    * AppCenter or Diawi? A special environment variable must be set: `LOOP_PUSH_SERVER_ENVIRONMENT=production`

Mention which troubleshooting steps you have completed so we know whether to ask about these again.

## Other Errors

Once you've set up remote commands, you may encounter errors when trying to run them via *Nightscout* or iOS Shortcuts.  Below are the most common and typical solutions.

1. **`Error: Loop notification failed: Could not find deviceToken in loopSettings`** You might see this in either *Nightscout* or Shortcuts.  The error is most commonly caused by&nbsp;_<span translate="no">Loop</span>_&nbsp;not pointing to the right *Nightscout* instance or you haven't yet run an override locally (with the&nbsp;_<span translate="no">Loop</span>_ app) before trying to run one remotely.  
    **Solution:** Confirm the *Loop* app is pointing to the right *Nightscout* site (and there are no extra spaces or a slash (`/`) at the end, and always run an override for a few seconds in the *Loop* app before you try to run one remotely.
2. **`Error: cannot POST/api/v2/notifications/loop`** You might see this in iOS Shortcuts.  This means *Nightscout* is not updated correctly and you are running a version of *Nightscout* that doesn't yet support remote overrides.   
   **Solution:** Follow the [Remote Configuration](remote-config.md) documentation.
3. **`Error: {“status”:401,”message”:”Unauthorized”,”description”:Invalid\\/Missing”}`** You might see this in iOS Shortcuts.  This is caused by having an incorrect `API_SECRET` in the shortcut.  
    **Solution:** Double check the `API_SECRET` is correct and that there are no spaces at the end.
4. **`Error: APNs delivery failed: InvalidProviderToken`** You might see this in either *Nightscout* or Shortcuts.  This is caused because your `LOOP_APNS_KEY_ID` and `LOOP_DEVELOPER_TEAM_ID` are swapped in *Heroku*.   
   **Solution:** Double check what's listed in your *Apple Developer Account* and compare it to the config variables in *Heroku*. Your `Team_ID` is next to your name in the top right corner.  The other code is your `Key_ID`. Get the IDs in the correct location in *Heroku* to resolve the error.
