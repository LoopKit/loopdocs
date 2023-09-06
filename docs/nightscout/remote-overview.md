## Remote Caregivers

With Loop 3, a caregiver can provide remote commands to assist in diabetes care, including modifying overrides and issuing remote bolus commands and adding remote carb entries.

Remote Commanding requires:

* <span translate="no">Nightscout</span> version 14.2.6 or newer
* *Apple Push Notifications* (</span>APN</span>) created with the *Apple Developer ID* used to build the *Loop* app
* Several configuration variables added to your Nightscout site

!!! question "What about Older Versions?"
    Caregivers for those using older versions of Loop can modify `Overrides` remotely but cannot send remote bolus or carb commands.

    If your <span translate="no">Nightscout</span> site is an older version, you should limit your remote commands to `Overrides`, even with `Loop 3`.

!!! tip "<span translate="no">Loop Caregiver</span>"
    There is a new companion app, [<span translate="no">Loop Caregiver</span>](loop-caregiver.md) that makes remote commands and reviewing status of your looper much easier.

## How does this work?

The <span translate="no">Loop</span> code and <span translate="no">Nightscout</span> code work together to provide this capability. However, remote commands and override control requires *Apple Push Notifications* (APN).

* The Apple Developer ID used to build the Loop app must be used to set up the push notifications
    * If you built Nightscout and the Loop app yourself, follow the directions to set up [Remote Configuration](remote-configuration.md)
* Some providers who supply `Nightscout as a service` or `Hosted Nightscout` can assist you in getting your APN information added to your Nightscout variables if you need help
    * [Nightscout Docs: New User](https://nightscout.github.io/nightscout/new_user)
    * [Nightscout Docs: Comparison Table](https://nightscout.github.io/nightscout/new_user/#vendors-comparison-table)
        * Warning: examine the `Loop remote carbs/bolus` row

!!! important "Remote Build"
    There are several methods for building remotely for your family members (or even yourself).

    * [*LoopDocs*: *GitHub Build* Actions](../gh-actions/gh-overview.md) (new with Loop 3) allows you to build on a browser (no need for a Mac) and send *Loop* to your phone using *TestFlight*
    * [*LoopDocs*: *TestFlight* from *Xcode*](../build/testflight.md) allows you to build using Mac-Xcode and then send *Loop* to your phone using *TestFlight*
    * [*Loop and Learn*: Remote Build with *Diawi*](https://www.loopandlearn.org/remote-build/) allows you to save a build created by *Xcode*, store it in the cloud, and then download and install it on your phone later
    
    Any remote build method requires this [*Nightscout*: Config Var](https://nightscout.github.io/nightscout/setup_variables/#nightscout-config-vars) to be added to *Nightscout*:
    
    `LOOP_PUSH_SERVER_ENVIRONMENT = production`
    
    Be aware that if you then return to building directly from *Xcode*, you must disable that config var from *Nightscout* and restart the server.
    
    Note - this is covered in detail on the next page.

## Next Steps

There are a number of steps to follow to set this up. Each are now found on separate pages, linked below:

### [Set Up Remote for Nightscout](remote-config.md)

### [Using Remote Commands](remote-commands.md)

### [Common Errors](remote-errors.md)

### [<span translate="no">Loop Caregiver</span> App](loop-caregiver.md)
