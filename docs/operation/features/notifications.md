# Notifications in Loop

Loop provides discrete notifications on the iPhone and Watch which will appear on the (locked) screen and vibrate, depending on your notification settings of Loop.

* <font color ="orange">**Omnipod**</font>  Most beep alarms are replaced. Only the fill beep, deactivate beep and a screaming pod (when reaching 80hours or a fault/occlusion happens) are the sounds which are currently used.

## Notication settings for Loop

Location of notifications in the Settings App of the iPhone:
<p align="center">
<img src="../img/iphone-settings-notifications.png" width="250">
</p> 

Settings of Loop:
<p align="center">
<img src="../img/iphone-notifications-loop.png" width="250">
</p> 

## Loop Failure

At 20, 40, 60, and 120 minutes, there is a Loop Failure notification.
This mostly happens when the connection is lost for a longer period of time between the CGM or the Rileylink and Loop.

<p align="center">
<img src="../img/loop_notifications.png" width="250">
</p> 

## Bolus Failure
If Loop detects that a bolus was not able to be delivered, it will provide a notification.  Bolus failures are usually due to stale pump data.  Try fetching recent history from the RileyLink menu to update pump data.  Loop will also notify of partial bolus deliveries.

<p align="center">
<img src="../img/loop-bolus-failure.png" width="250">
</p> 

## Low Reservoir

* <font color ="orange">**Medtronic**</font>  
At 20% and 10% remaining reservoir volume, there is a Low Reservoir notification.

* <font color ="orange">**Omnipod**</font>  
At <30U, <20U, <10U  

<p align="center">
<img src="../img/pod-reservoir-10U.png" width="250">
</p> 


## Empty Reservoir

Loop will notify when the reservoir is empty. Loop will notify you every minute with this notification. 

* <font color ="orange">**Omnipod**</font>  
Normally you will have 5-30 minutes to replace the pod, but do know the pod can [scream](https://soundcloud.com/eelke-jager/1f-nibble-f) at any moment from this point on.

<p align="center">
<img src="../img/loop-reservoir-empty.png" width="250">
</p> 

## Pod Expiration (Omnipod)
 
You can customise the time of notification when to replace your pod any time up to 3 days and 8 hours [after staring a new pod](https://loopkit.github.io/loopdocs/operation/loop-settings/omnipod-pump/#expiration-reminder) or you change the time later in the [pod configuration settings](https://loopkit.github.io/loopdocs/operation/loop-settings/omnipod-pump/#configuration).

<p align="center">
<img src="../img/pod-expiration-notice.png" width="250">
</p> 

## Low Battery (Medtronic)

Loop will notify when battery levels have approximately 8-10 hours of battery life remaining.


## Remote Notifications

Loop does not have remote notification to other devices.  If you are a remotely monitoring parent, you will want to read [here](https://loopkit.github.io/loopdocs/nightscout/pushover/#pushover) about setting up pushover alerts using your Nightscout site if you want proactive notifications of looping related information.
