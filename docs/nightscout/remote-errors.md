## Improper Configuration

Error messages if Looper's phone is not configured correctly:

-  Without notifications, the person trying to set a remote override will see a message about `"no deviceToken"` and no remote override will actually enact
- If Background app refresh is not enabled, the remote overrides will only enact if the *Loop* app is open and the phone is unlocked.

## Known Issues

Just a brief mention so you are aware:

1. The override pill will display information about what override is currently active in the Looper&#39;s phone. BUT, there can be a slight delay as that information is only transmitted every 5 minutes at best (it is tied to <span>*Loop* runs</span> and *Nightscout* upload events in *<span translate="no">Loop</span>*). So, wait 5 minutes to see that the information has gone through a refresh cycle before assuming the override message failed to enact.
2. When you add a new override preset in *Loop*, that preset has to be uploaded to *Nightscout* before it will be available as a remote override. To trigger that upload, you can simply enact that new override for a few seconds and turn it off again. That will get the *Nightscout* upload going.

## Common Errors

Once you've set up remote overrides, you may encounter errors when trying to run them via *Nightscout* or iOS Shortcuts.  Below are the most common and typical solutions.

1. **`Error: Loop notification failed: Could not find deviceToken in loopSettings`** You might see this in either *Nightscout* or Shortcuts.  The error is most commonly caused by *Loop* not pointing to the right *Nightscout* instance or you haven't yet run an override locally (with the Loop app) before trying to run one remotely.  
    **Solution:** Confirm the *Loop* app is pointing to the right *Nightscout* site (and there are no extra spaces or a slash (`/`) at the end, and always run an override for a few seconds in the *Loop* app before you try to run one remotely.
2. **`Error: cannot POST/api/v2/notifications/loop`** You might see this in iOS Shortcuts.  This means *Nightscout* is not updated correctly and you are running a version of *Nightscout* that doesn't yet support remote overrides.   
   **Solution:** Follow the steps above again on how to update to the version of *Nightscout* that supports remote overrides.
3. **`Error: {“status”:401,”message”:”Unauthorized”,”description”:Invalid\\/Missing”}`** You might see this in iOS Shortcuts.  This is caused by having an incorrect `API_SECRET` in the shortcut.  
    **Solution:** Double check the `API_SECRET` is correct and that there are no spaces at the end.
4. **`Error: APNs delivery failed: InvalidProviderToken`** You might see this in either *Nightscout* or Shortcuts.  This is caused because your `LOOP_APNS_KEY_ID` and `LOOP_DEVELOPER_TEAM_ID` are swapped in *Heroku*.   
   **Solution:** Double check what's listed in your *Apple Developer Account* and compare it to the config variables in *Heroku*. Your `Team_ID` is next to your name in the top right corner.  The other code is your `Key_ID`. Get the IDs in the correct location in *Heroku* to resolve the error.
