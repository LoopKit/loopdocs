## Remote Caregivers

With <span translate="no">Loop</span> 3, a caregiver can provide remote commands to assist in diabetes care, including modifying overrides, issuing remote bolus commands and adding remote carb entries. With <span translate="no">Loop</span> 2, only overrides can be turned on or off remotely.

Remote commands to the <span translate="no">Loop</span> phone go through their <span translate="no">Nightscout</span> site. For security, any command to deliver a bolus or add a carb entry requires a one-time-password (OTP) to be used with each remote command. These codes are unique to your combined <span translate="no">Loop</span> and <span translate="no">Nightscout</span> configuration. An authentication app needs to be installed on the device sending the remote boluses/carbs. The <span translate="no">Loop Caregiver</span> app can be used. It handles authentication requirements and offers a <span translate="no">Loop</span>-like user interface.

### Remote Commanding Requirements:

* <span translate="no">Loop</span> version 3.2.0 or newer
    * version 3.0 works but is not recommended for other reasons
* <span translate="no">Apple Push Notifications</span> (</span>APN</span>) created with the <span translate="no">Apple Developer ID</span> that built the <span translate="no">Loop</span> app
* <span translate="no">Nightscout</span> version 14.2.6 or newer
    * Several configuration variables must be added
* Ability to generate a One-Time-Password (OTP)

!!! question "What about Older Versions?"
    Caregivers for those using older versions of Loop can modify `Overrides` remotely but cannot send remote bolus or carb commands.

    If your <span translate="no">Nightscout</span> site is an older version, you should limit your remote commands to `Overrides`, even with <span translate="no">Loop 3</span>.

!!! tip "<span translate="no">Loop Caregiver</span>"
    There is a new companion app, [<span translate="no">Loop Caregiver</span>](loop-caregiver.md) that makes remote commands and reviewing status of your looper much easier.

## How does this work?

<span translate="no">Loop</span> and <span translate="no">Nightscout</span> work using <span translate="no">Apple Push Notifications</span> (APN).

* The <span translate="no">Apple Developer ID</span> used to build the <span translate="no">Loop</span> app must be configured to enable <span translate="no">Apple Push Notifications</span>
    * If you built <span translate="no">Nightscout</span> and <span translate="no">Loop</span> yourself, follow the directions to set up [Remote Configuration](remote-config.md)
* Most providers who supply `Nightscout as a service` or `Hosted Nightscout` will assist you, if needed, in getting your APN information added to your <span translate="no">Nightscout</span> variables
    * [Nightscout Docs: New User](https://nightscout.github.io/nightscout/new_user)
    * [Nightscout Docs: Comparison Table](https://nightscout.github.io/nightscout/new_user/#vendors-comparison-table)
        * **Warning: examine the `Loop remote carbs/bolus` row: subscription refers to a monthly fee**

## Next Steps

There are a number of steps to follow to set this up. Each page is linked below:

### [Set Up Remote for Nightscout](remote-config.md)

### [Using Remote Commands](remote-commands.md)

### [Remote Errors](remote-errors.md)

### [<span translate="no">Loop Caregiver</span> App](loop-caregiver.md)
