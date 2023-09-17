## Remote Caregivers

With &nbsp;<span translate="no">Loop</span>&nbsp; 3, a caregiver can provide remote commands to assist in diabetes care, including modifying overrides, issuing remote bolus commands and adding remote carb entries. With &nbsp;<span translate="no">Loop</span>&nbsp; 2, only overrides can be turned on or off remotely.

Remote commands to the &nbsp;<span translate="no">Loop</span>&nbsp; phone go through their &nbsp;<span translate="no">Nightscout</span>&nbsp; site. For security, any command to deliver a bolus or add a carb entry requires a one-time-password (OTP) to be used with each remote command. These codes are unique to your combined &nbsp;<span translate="no">Loop</span>&nbsp; and &nbsp;<span translate="no">Nightscout</span>&nbsp; configuration. An authentication app needs to be installed on the device sending the remote boluses/carbs. The &nbsp;<span translate="no">Loop Caregiver</span>&nbsp; app can be used. It handles authentication requirements and offers a &nbsp;<span translate="no">Loop</span>&nbsp;-like user interface.

### Remote Commanding Requirements:

* <span translate="no">Loop</span>&nbsp; version 3.2.0 or newer
    * version 3.0 works but is not recommended for other reasons
* <span translate="no">Apple Push Notifications</span>&nbsp; (</span>&nbsp;APN</span>&nbsp;) created with the &nbsp;<span translate="no">Apple Developer ID</span>&nbsp; that built the &nbsp;<span translate="no">Loop</span>&nbsp; app
* <span translate="no">Nightscout</span>&nbsp; version 14.2.6 or newer
    * Several configuration variables must be added
* Ability to generate a One-Time-Password (OTP)

!!! question "What about Older Versions?"
    Caregivers for those using older versions of Loop can modify `Overrides` remotely but cannot send remote bolus or carb commands.

    If your &nbsp;<span translate="no">Nightscout</span>&nbsp; site is an older version, you should limit your remote commands to `Overrides`, even with &nbsp;<span translate="no">Loop 3</span>.

!!! tip "&nbsp;<span translate="no">Loop Caregiver</span>"
    There is a new companion app, [<span translate="no">Loop Caregiver</span>](loop-caregiver.md) that makes remote commands and reviewing status of your looper much easier.

## How does this work?

&nbsp;<span translate="no">Loop</span>&nbsp; and &nbsp;<span translate="no">Nightscout</span>&nbsp; work using &nbsp;<span translate="no">Apple Push Notifications</span>&nbsp; (APN).

* The &nbsp;<span translate="no">Apple Developer ID</span>&nbsp; used to build the &nbsp;<span translate="no">Loop</span>&nbsp; app must be configured to enable &nbsp;<span translate="no">Apple Push Notifications</span>
    * If you built &nbsp;<span translate="no">Nightscout</span>&nbsp; and &nbsp;<span translate="no">Loop</span>&nbsp; yourself, follow the directions to set up [Remote Configuration](remote-config.md)
* Most providers who supply `Nightscout as a service` or `Hosted Nightscout` will assist you, if needed, in getting your APN information added to your &nbsp;<span translate="no">Nightscout</span>&nbsp; variables
    * [Nightscout Docs: New User](https://nightscout.github.io/nightscout/new_user)
    * [Nightscout Docs: Comparison Table](https://nightscout.github.io/nightscout/new_user/#vendors-comparison-table)
        * **Warning: examine the `Loop remote carbs/bolus` row: subscription refers to a monthly fee**

## Next Steps

There are a number of steps to follow to set this up. Each page is linked below:

### [Set Up Remote for Nightscout](remote-config.md)

### [Using Remote Commands](remote-commands.md)

### [Remote Errors](remote-errors.md)

### [<span translate="no">Loop Caregiver</span>&nbsp; App](loop-caregiver.md)
