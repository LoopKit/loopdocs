## Remote Caregivers

With&nbsp;_<span translate="no">Loop</span>_&nbsp;3, a caregiver can provide remote commands to assist in diabetes care, including modifying overrides, issuing remote bolus commands and adding remote carb entries.

Remote commands to the&nbsp;_<span translate="no">Loop</span>_&nbsp;phone go through their *Nightscout* site. For security, any command to deliver a bolus or add a carb entry requires a one-time-password (OTP) to be used with each remote command. These codes are unique to your combined&nbsp;_<span translate="no">Loop</span>_&nbsp;and *Nightscout* configuration. An authentication app needs to be installed on the device sending the remote boluses/carbs. The *LoopCaregiver* app can be used. It handles authentication requirements and offers a&nbsp;_<span translate="no">Loop</span>_&nbsp;-like user interface.

### Remote Commanding Requirements:

* &nbsp;_<span translate="no">Loop</span>_&nbsp;version 3..0 or newer
    * version 3.0 works but is not recommended for other reasons
* <span translate="no">Apple Push Notifications</span>&nbsp; (</span>&nbsp;APN</span>&nbsp;) created with the &nbsp;<span translate="no">Apple Developer ID</span>&nbsp; that built the&nbsp;_<span translate="no">Loop</span>_&nbsp;app
* *Nightscout* version 14.2.6 or newer, but the released version 15.0.2 is recommended
    * Several configuration variables must be added
* Ability to generate a One-Time-Password (OTP)

!!! question "What about Older Versions?"
    Caregivers for those using older versions of Loop can modify `Overrides` remotely but cannot send remote bolus or carb commands.

    If your *Nightscout* site is an older version, you should limit your remote commands to `Overrides`, even with &nbsp;<span translate="no">Loop 3</span>.

!!! tip "&nbsp;*LoopCaregiver*"
    There is a new companion app, &nbsp;[*LoopCaregiver*](loop-caregiver.md) that makes remote commands and reviewing the status of your looper much easier.

## How does this work?

_<span translate="no">Loop</span>_&nbsp;and *Nightscout* work using &nbsp;<span translate="no">Apple Push Notifications</span>&nbsp; (APN).

* The &nbsp;<span translate="no">Apple Developer ID</span>&nbsp; used to build the&nbsp;_<span translate="no">Loop</span>_&nbsp;app must be configured to enable &nbsp;<span translate="no">Apple Push Notifications</span>
    * If you built *Nightscout* and&nbsp;_<span translate="no">Loop</span>_&nbsp;yourself, follow the directions to set up [Remote Configuration](remote-config.md)
* Most providers who supply `Nightscout as a service` or `Hosted Nightscout` will assist you, if needed, in getting your APN information added to your *Nightscout* variables
    * [Nightscout Docs: New User](https://nightscout.github.io/nightscout/new_user){: target="_blank" }
    * [Nightscout Docs: Comparison Table](https://nightscout.github.io/nightscout/new_user/#vendors-comparison-table){: target="_blank" }
        * **Warning: examine the `Loop remote carbs/bolus` row: subscription refers to a monthly fee**

## Warning: *Nightscout* Remote Carbohydrate Entries

!!! warning "Use unique times for remote carbohydrate entries"
    Instead of adding a second remote carbohydrate entry at an identical time, add one minute to the second entry.

    This ensures that *Nightscout* keeps both entries.

For more information, see:

* [Use Unique Times for Remote Carbohydrate Entries](remote-commands.md#use-unique-times-for-remote-carbohydrate-entries){: target="_blank" }


## Next Steps

There are several steps to follow to set this up. Each page is linked below:

### [Set Up Remote for Nightscout](remote-config.md)

### [Using Remote Commands](remote-commands.md)

### [Remote Errors](remote-errors.md)

### [*LoopCaregiver* App](loop-caregiver.md)
