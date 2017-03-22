# Remote notifications

While Loop app currently sends notifications locally on Loop user's iPhone, parents and caregivers likely want those messages on their phones, too.

Currently we can achieve this via 2 options:

* Pushover service, or
* [Loop Follow app](https://github.com/amazaheri/Loop-Follow)

## Pushover

Pushover is a paid service (but has a free 7-day trial period).  The cost is currently $4.99 flat, one-time fee per platform.  You can use it across all your personal devices (iPhones, iPads, etc) for the one fee per platform .  Android and iPhones and Desktop computers are on separate platforms.  So if your house has both Androids and iPhones that you wanted to receive notifications on, you would have to pay two flat fees.  

You can follow this [guide](http://www.nightscout.info/wiki/labs/pushover-in-funnel-cake) for general Pushover setup with NS.  You will have to make some specific modifications for Loop-related alarms.

1. Signup for a [Pushover Account](http://pushover.net)

2. Verify your account from the email they will send you

3. Download the Pushover App to your iPhone or Android and allow notifications from the app

4. Add `pushover` to your existing ENABLE line on NS connection strings

5. Add any alerts you'd like to your connection strings (Azure) or config vars (Heroku), if you haven't already.

6. Add the `PUSHOVER_ANNOUNCEMENT_KEY` and `PUSHOVER_API_TOKEN` from your Pushover account to the lines in your connection strings in order to determine what types of notifications you would like to receive.  Screenshot below has a brief description of the various alerts you enable by having the line populated...you can customize as you wish.  The example shows the `PUSHOVER_USER_KEY` line as being populated, but for Loop users this means you would get a notification every time a temp basal is set by Loop.  Most Loopers would probably get notification fatigue by that...so if you leave that line blank, you will not get those notifications (and that's a good thing).

<p align="center">
<img src="../img/pushover.jpg" width="700">
</p> 

<p align="center">
<img src="../img/warn.jpg" width="200">
</p> 


## Loop Follow
The Loop Follow application is a simple iOS app written in Swift that accepts notifications from Loop and is powered by Azure. The setup for the Loop Follow application iOS portion is a little more involved than setting up the Loop application.  

For more background read this [blog post](https://blogs.msdn.microsoft.com/alimaz/2016/09/22/azure-logic-apps-azure-sql-and-loop-better-together-part-ii/)

![](https://msdnshared.blob.core.windows.net/media/2016/09/20160922_152515000_iOS-169x300.png)
![](https://msdnshared.blob.core.windows.net/media/2016/09/20160921_044556000_iOS-169x300.png)

It's more challenging to setup Loop-Follow due to the nature of using Push notifications and requiring some special provisioning on both the iOS side and the Azure configuration so they talk to each other.

For future releases, the Loop Follow developers are planning to use a shared Push notification service hosted on NightScout Foundation Azure subscription to simplify the process and make it available to Loop users not using Azure and also a free service comparing to Push Over with more flexibility!

For instructions go to [wiki](https://github.com/amazaheri/Loop-Follow/wiki) or join the conversation on [gitter](https://gitter.im/LoopKit/Follow)


