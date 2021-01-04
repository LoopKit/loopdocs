# New Nightscout Users

!!!info "Is Nightscout required for Loop?"
    Nope...you don't NEED to have a Nightscout site in order to use Loop. A Nightscout site is completely optional. However, if you want to see Loop's actions anywhere other than the Looper's iPhone...then you will want a Nightscout site. For example, parents of little Loop users may want to see the temporary basal rates Loop is setting, the current insulin on board, or a recent bolus and carb entry.  That's what Nightscout will provide...remote viewing of Loop actions.

There are two options for setting up Nightscout; one option requires a small fee but automates both the setup and periodic updating/cleaning database, the other option is free but requires your effort to build and update. You choose which works best for you. Isn't it nice to have options?

## T1Pal (paid service)

!!! warning "European Nightscout Dexcom Devices"
    T1Pal does NOT support European Dexcom Devices at this time.

[T1Pal is only dedicated NS hosting](https://t1pal.com/) company.  There is a hosting fee required which is used to help ensure Nightscout runs without limits and receives improvements.  Setup is simple and loop plugins are configured automatically during the setup guide.

* Select [Get Started](https://www.t1pal.com/getting-started/starting/home) to register an account at [T1Pal](https://www.t1pal.com/).  You will need to enter your credit card, which helps ensure Nightscout is running correctly.
* Select "visualize treatments" in the setup menu and select "loop."

<p align="center">
<img src="../img/t1pal_configure.png" width="450">
</p>

## Traditional DIY (free, do-it-yourself)

Two options exist for easy DIY hosting of NS; Azure or Heroku. Both hosting services are free.  However,  Azure has data quotas monthly and shorter-term CPU quotas.  If you exceed those quotas, you may be facing a monthly data-use bill or being locked out of NS for about 12 hours until the quotas reset.  As you start to use NS more intensively for alarms, watches, etc…it is possible that you may exceed your monthly data cap on Azure.  Many Loop users have transitioned their old sites from Azure over to Heroku and have found the hosting change to be beneficial.  Heroku also has some memory limits, but those limits have been more than adequate for Loop users.  Therefore, we recommend new users start with Heroku.

There's great news though! The documentation and instructions for building your own Nightscout site have recently been completely overhauled and are WONDERFUL!

Please visit [The Nightscout site](http://nightscout.github.io/nightscout/new_user/) for directions on how to set up your new Nightscout website. 

## Add Nightscout to Loop

Once you finish setting up your new Nightscout site, don't forget to [enter the website into your Loop settings](https://loopkit.github.io/loopdocs/operation/loop-settings/services/#nightscout)! This way Loop will have access to your Nightscout site to upload all the wonderful data.

## Troubleshooting

If your Nightscout site is not showing CGM (and Loop, if you are Looping) data within about 10 minutes of finishing your setup, then please follow these steps [here](https://loopkit.github.io/loopdocs/nightscout/troublehoot/) to troubleshoot.

