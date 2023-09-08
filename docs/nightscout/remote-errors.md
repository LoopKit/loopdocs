## Improper Configuration

### Loop Phone

**test this**

-  Without notifications enabled, the person trying to set a remote override will see a message about `"no deviceToken"` and no remote override will actually enact or be canceled
- If Background app refresh is not enabled, the remote overrides will only enact if the *Loop* app is open and the phone is unlocked.

### Nightscout Config and Loop Build Method

When the Nightscout config var LOOP_PUSH_SERVER_ENVIRONMENT does not match the Loop app build method; the error message contains the phrase `APNs delivery failed: BadDeviceToken`.

* If Loop was installed remotely (typically from TestFlight following GitHub Browser Build), you **must** have Nightscout config var `LOOP_PUSH_SERVER_ENVIRONMENT` set to `production`
* If Loop was built using Mac-Xcode, you **cannot** have `LOOP_PUSH_SERVER_ENVIRONMENT` as one of your Nightscout config vars

If you attempt to issue a command from Nightscout Careportal; after you hit submit and then OK, you will see the error message:

```
Error: APNs delivery failed: BadDeviceToken
```

If you attempt to issue a command using Loop Caregiver; after you authenticate the command, you will see the error message listed below and shown in the screen shot.

```
HTTP Error
Status Code: 500
body: APNs delivery failed: BadDeviceToken
```

![site and build method mismatch](img/site-build-mismatch.png){width="400"}
{align="center"}

## Other Errors

Once you've set up remote overrides, you may encounter errors when trying to run them via *Nightscout* or iOS Shortcuts.  Below are the most common and typical solutions.

1. **`Error: Loop notification failed: Could not find deviceToken in loopSettings`** You might see this in either *Nightscout* or Shortcuts.  The error is most commonly caused by *Loop* not pointing to the right *Nightscout* instance or you haven't yet run an override locally (with the Loop app) before trying to run one remotely.  
    **Solution:** Confirm the *Loop* app is pointing to the right *Nightscout* site (and there are no extra spaces or a slash (`/`) at the end, and always run an override for a few seconds in the *Loop* app before you try to run one remotely.
2. **`Error: cannot POST/api/v2/notifications/loop`** You might see this in iOS Shortcuts.  This means *Nightscout* is not updated correctly and you are running a version of *Nightscout* that doesn't yet support remote overrides.   
   **Solution:** Follow the [Remote Configuration](#remote-config.md) documentation.
3. **`Error: {“status”:401,”message”:”Unauthorized”,”description”:Invalid\\/Missing”}`** You might see this in iOS Shortcuts.  This is caused by having an incorrect `API_SECRET` in the shortcut.  
    **Solution:** Double check the `API_SECRET` is correct and that there are no spaces at the end.
4. **`Error: APNs delivery failed: InvalidProviderToken`** You might see this in either *Nightscout* or Shortcuts.  This is caused because your `LOOP_APNS_KEY_ID` and `LOOP_DEVELOPER_TEAM_ID` are swapped in *Heroku*.   
   **Solution:** Double check what's listed in your *Apple Developer Account* and compare it to the config variables in *Heroku*. Your `Team_ID` is next to your name in the top right corner.  The other code is your `Key_ID`. Get the IDs in the correct location in *Heroku* to resolve the error.
