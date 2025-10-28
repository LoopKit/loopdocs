## Remote Caregivers

If you are a caregiver and want to issue remote commands to the *Loop* app, you have 3 options. All of these require you to configure a [Nightscout site](../nightscout/overview.md){: target="_blank" } for that person.

Once the Nightscout site is configured, you can remotely monitor that person.

In the documentation below, the OTP is a one-time password that changes every 30 seconds.

You can add remote control to:

* modify the Override (Custom Preset)
* add Carbohydrates (requires OTP)
* issue a Bolus (requires OTP)

You have 3 ways in which to do this. The first two require additions to the config vars on your Nightscout site and then you send commands through the Nightscout site either directly (option 1) or using the *LoopCaregiver* app (option 2) to the Looper's phone. The third option (*LoopFollow*) uses direct Apple Push Notifications (APNS) from your phone to the Looper's phone. With that method, the Nightscout site is used for monitoring, not issuing commands.

All of these methods require APNS keys from someone with an Apple Developers License and that must be the same developer who built to *Loop* app.

1. Use the [Careportal at the Nightscout URL](../nightscout/remote-commands.md){: target="_blank" }
    * If the Caregiver uses an Android phone, this is your only option
    * The Nightscout config vars must include APNS keys and the developer ID for the developer who built the Loop app
2. Build the [*LoopCaregiver* app](../nightscout/loop-caregiver.md){: target="_blank" } on the caregiver's iPhone to issue command through the Nightscout site
    * The Caregiver must have an iPhone with iOS 16 or newer
    * The Nightscout config vars must include APNS keys and the developer ID for the developer who built the Loop app
3. Build the [*LoopFollow* app](https://loopfollowdocs.org/remote/remote-control-loop/) on the caregiver's phone to directly issue APNS to the Looper's phone, this can be faster and more reliable
    * The Caregiver must have an iOS phone with iOS 16 or newer
    * The Nightscout site monitors the Looper's phone
    * No additions to the Nightscout config vars are required - this makes it easier when you use Nightscout as a Service

## Customization for Longer OTP Window

May people find the OTP expires too soon when their Looper is on a different network from the Caregiver.

Consider adding the option that allows Loop to accept a remote command that arrives within a 15 minute window.

Please review this carefully before deciding to use this.

* [Increase Remote Window to 15 minutes](https://www.loopandlearn.org/loop-features-in-development/#remote-window)

This customization is for the *Loop* app so works with all three remote methods mentioned in the previous section.
