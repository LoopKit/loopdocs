# Red Loops

## Red Loop Overview

This page provides help if your Loop icon is red and Loop is not working or only working sometimes? You can click on the Red Loop icon to read an error message that you may or may not understand. If you understand it, great...that should help you fix the problem.

If not, keep reading to identify and fix your problem.

!!! warning "Omnipod Users"

    Do not just pull a pod that isn't responding when there is a red loop. Usually the issue is that the [RileyLink compatible device needs to be reset](#rileylink-compatible-device).

    If you don't fix the current communication problem first, the problem will carry forward into a failed pod-pairing attempt. So, please try getting the device working properly before deciding to ditch a pod because of a red loop.


A Red Loop icon means that Loop has not completed a cycle for 15-minutes or more and this is normally because of a communication break-down with one of the systems listed below. To find out which one, tap on the Red Loop icon, read the message and search this page for that message.

## Typical Causes for Red Loop

Some of the reasons listed below cause Loop to go Red and stay Red until you fix it.  Others will cause intermittent Red Loops that come and go, but can be very annoying.

1. [RileyLink Compatible Device](#rileylink-compatible-device)
1. [Continuous Glucose Monitor (CGM)](#cgm-values-are-not-being-collected-by-loop)
1. [Apple Health](#apple-health)
1. [Background App Refresh](#background-app-refresh) is not enabled for Phone, Loop and/or CGM
1. [Nightscout](#nightscout) (optional service)
1. [Phone Storage is Full](#phone-storage-is-full)

### RileyLink Compatible Device

If the indication is one of these (or something similar), it can probably be fixed by resetting the RileyLink compatible device communication with the phone and pump.

* pump history is too old
* no rileylink could be found
* pod cannot be reached

Do these steps until one of them fixes the issue:

* Turn off Bluetooth on your phone and then turn it right back on again.
* Close your Loop app (upswiping it in the iPhone's app selector) and reopen it.
* Power cycle your phone.
* Turn your RileyLink off/on at its physical power switch located on the side of the RileyLink.
    * If you have a different device, make sure you know how to power-cycle the device.
    * For RileyLink (without wireless charging) use a small pointy object to carefully move the slider away from the charging port and then back up towards the charging port. A paperclip on the keyring can provide the help you need to reach the switch in the recessed case, and double as a [screaming pod silencer tool](../faqs/omnipod-faqs.md#what-do-you-do-to-stop-a-screaming-pod).


    ![img/riley-switch.png](img/riley-switch.png){width="300"}
    {align="center"}


This should restore a green Loop within 5 minutes. If you're impatient, you can issue a "Read Pod Status" for Pod or "Change Time" for Medtronic (button press command is not available with v2.2.6). If this is successful, you've established pump communication again.

If this was not successful, check out the [Pump is Not Responding](#pump-is-not-responding) section.

### CGM Values Are Not Being Collected by Loop

#### New Transmitter

If you recently changed a transmitter, you need to also update your Loop settings to reflect the new transmitter ID. Go to the CGM section of Loop settings and `Delete CGM` (it's a button on the bottom of that page). Then use the `Add CGM` in Loop settings to include the new transmitter ID.

If you fail to update your Transmitter ID in Loop and you also left Share Credentials in Loop (not recommended), you will see messages such as: `Failed to decode SGV` when the Share server cannot be reached. That's your notice to update the Transmitter ID (or if you think you already did - check for typos in data entry).

#### Delete Share Account

Finally, we see a lot of errors reported because people have problems with their Share server information in Loop app. **Please delete your Share account information from within Loop settings.** In other words, the credentials portion of the Share account info, as shown in the screenshot below, should say `Tap to Set` and not have your account info. It is unnecessary to have this portion filled out as local, non-internet spying of a transmitter is the preferred CGM source anyways. In fact, by leaving this information out, it will help you remember to change your transmitter ID when you change transmitters because CGM data won't appear in Loop. By not including Share account in Loop, you will prevent yourself from accidentally becoming internet dependent.

![img/no-share.jpg](img/no-share.jpg){width="450"}
{align="center"}

#### Firefly-style Transmitter

Leaving this in for historical interest only. It illustrates the need to keep Loop up-to-date.  Who knows what the next hardware change will be. Enough time has passed that everyone's Loop code should be newer.

In July 2019, we started to see a new style of Dexcom G6 transmitters on the market. These new transmitters required a rework of some of the Loop's code to continue to "spy" on the transmitter. Without that update, your Loop can not get CGM data unless it is pulling from Share servers (which is not a recommended mode of operation). So, download fresh code for your Loop app if you have a new transmitter type and haven't downloaded since July 2019.

### Apple Health

Make sure both the Loop app and the Dexcom app have permission to write to Apple Health by checking the [Apple Health Permissions](../build/health.md)

In the early days of iOS 14, there were problems with the Apple HealthKit.  The consequence is that some people's database was corrupted.  If you tap on the Heart Icon on your phone to go to Apple Health and display data and it is very slow to respond - or never responds, you probably need to get rid of a corrupted database and start fresh.  Be sure to go Open Loop if this is needed. Please get help from your favorite [Loop Social Media](../index.md#stay-in-the-loop) group or from Apple support in this case.

### Background App Refresh

If you have not enabled background app refresh on your phone, then Loop is likely to stop communicating as soon as the phone is locked.

1. Phone Settings -> General -> Background App Refresh -> enable
1. Then scroll down until you find Loop and make sure the green slider is enabled
1. While you are there - check your CGM app as well

!!! warning ""

    Make sure you never accept Low Power Mode on your phone. Low Power mode will disable apps like Loop when phone is locked.

    Suggestions:

    * Add a charger and cable to your diabetes go-bag
    * Add a power-pack and cable to your diabetes go-bag


For iOS 15, there is a new feature described by [Dexcom](https://www.dexcom.com/faqs/what-are-the-recommended-iphone-settings)

1. Phone Settings -> Screen Time -> choose Always Allowed -> select an app, tap the plus icon to add to Always Allowed list
    - add Dexcom
    - add Loop

### Nightscout

If you added your Nightscout URL to Loop and are uploading information to Nightscout, make sure the communication is working properly.  For short-term interruptions, Loop will store information to upload to Nightscout later.  But if too much information builds up, Loop can slow down and in some cases have a Red Loop.

1. Check to see that internet service (WiFi or Cell) is operating
1. Check that Nightscout database size isn't full (more details below)
1. If Red Loops are resolved by removing the Nightscout URL from Loop; you need to figure out if it's the connection or the database or some other issue

If you opted for the free DIY Nightscout, you will need to clean your database once or twice a year. Follow the [Nightscout Database cleanup steps](https://nightscout.github.io/troubleshoot/troublehoot/#database-full). Make sure you are periodically checking your database size (and that the **dbsize** keyword is in your [ENABLE list](../nightscout/update_user.md#editadd-config-vars) and cleaning it.

### Phone Storage is Full

This was recently reported by a user. His phone storage was almost full and the reported error messages for Loop was:

*  `Sqlite Error: A Sqlite Error Occurred: (13) Database or Disk is Full`

The error message from Dexcom was not as helpful.  If you see this, check your phone storage:

* `The Dexcom G6 app has stopped working. Please delete the app from your device and redownload it from the App Store`

Solution: clear up space on your phone.

## Other Reasons for Red Loop

### Pump is Not Responding

The obvious fix is to make sure the RileyLink compatible device is not so far away from the pump or pod that they cannot communicate. Assuming you've addressed this, then you can move on to other steps.

**Omnipod Loopers**: Following the steps to [reset the RileyLink / Phone](#rileylink-compatible-device) almost always fixes this issue. There has been one report over the last 3 years where the pod really had stopped communicating, but try everything else before burning another pod.

**Medtronic Loopers**: If the pump is not responding with "decoding" errors or various other messages about pump responses. Try the following:

1. Change pump battery. Low pump battery will cause radio communications to fail.
1. Use the `Change Time` command in the pump menu to update the pump's clock. If you've accidentally changed the pump's time in the pump itself or if the pump time has drifted, this will get the Loop app and pump time back in sync.
1. If using a x23 or x54 pump, try deleting all the IDs under the "Other Devices" submenu in the pump's "Connect Devices" menu.  Then go to the RileyLink menu and use the MySentry pairing command to get a fresh ID issued. Follow the directions listed in the MySentry pairing command's screen to scan for devices. A fresh ID can help prevent recurring red loops for x23 and x54 users, particularly if they started to occur after a recent Loop update.
1. Make sure the following are checked in the pump:
    * Your pump cannot be suspended.  Resume insulin deliveries.
    * Temp basal type must be set to unit/hour, not percent, in pump's Basal menu.

## Resolving Frequent Red Loops

Here's some things to check if you have frequent red loops:

* Try deleting your [Nightscout](#nightscout) account from Loop settings and see if your Loop stops having red loops. If it does, then you'll need to assess what's going wrong in your Nightscout site and fix it. Most of the time, your database is getting too big and cleanup is required.

* Is your [RileyLink battery plugged in all the way](../build/step5.md#assemble-rileylink) on the board? One Looper recently posted that her RileyLink battery connection needed to be reseated after several years of service.

* Has your RL been fully charged? Try charging your RL for an hour or two, make sure the red light comes on while charging. Try a new charger or cable.

* Oddly, some people have found that turning off Siri integrations for Loop and Dexcom apps in your iPhone settings has helped. This may be coincidental, but if you're still having trouble, you might want to try it.

* Check for sources of wireless interference. If you have a certain environment that seems to have more drops than others, it is likely that there is a source of wireless communication interfering with your Loop. Lots of Medtronic Loopers in a room together will often interfere with each other and get "cross-talk" red loop error messages. If it is a bedroom at night causing problems, try moving other wireless devices such as routers or baby monitors farther away from where you and your RileyLink compatible device.

* In some cases, you may need to clean out [Apple Health](apple-health), or even reset your phone to factory defaults and reload all your personal information and then rebuild the Loop app. Before you do this, you may want to Post for Help (next section).

## Posting for Help

Before you post on Looped group for help with a red loop, please make sure you've [reset the RileyLink / Phone](#rileylink-compatible-device).

Before you post for help, please also check your Nightscout status including database size. This step is often overlooked and yet solves a lot of problems.

When posting for help, include two screenshots of Loop's main screen; one with the red loop's error message and the other just the plain Loop main screen. Include a detailed description of what you have tried doing from the troubleshooting list above. For example, state if you've double checked the transmitter ID, deleted the Share account info from Loop settings so that we can rule out some of the causes of CGM issues.

## What Else?

There are a few other things to consider:

* RileyLink is broken
* Battery has failed
* OrangeLink has firmware 2.6

### RileyLink is Broken

How can you tell if your RileyLink has a problem? The answer is mostly within the LED lights that display on the board. Some information is listed below, but also review the [FAQs at getrileylink.org](https://getrileylink.org/faq).

If you have a different RileyLink compatible device, please check the appropriate site for troubleshooting help.

**Red light**: comes on during charging and will turn off/on periodically, while still plugged in, after charge is complete.

**Green light**: Indicates an active BT connection with the phone. You want the green light to stay on all the time on the RileyLink. If the green light is not on, then make sure your iPhone's bluetooth is still switched on.

**Blue light**: The blue light will flash off/on periodically when the RileyLink and pump are actively communicating...it should NOT be always on. If your blue light is stuck on, that is an indication of a problem on the board. Try looking for signs of damage or debris that may be causing a short on the board. Clean the board with rubbing alcohol [(unplug the battery first](https://youtu.be/s2qNPLpfwww)). If you still can't get the blue light off, then contact GetRileyLink for help or check out [RileyLink Compatible Devices](../build/step5.md#rileylink-compatible-devices) for replacement options.

### Battery has Failed

Both [RileyLink](https://getrileylink.org/faq) and [EmaLink](https://github.com/sks01/EmaLink/wiki/Battery-swelling) use LiPo batteries.  If they stop holding charge for as long as they used to, or if they swell (often first noticed as bowing of the case), stop using the battery and replace it as soon as possible.

[OrangeLink](https://getrileylink.org/faq) uses regular batteries, so just change them out.

### OrangeLink Firmware

One version of the OrangeLine firmware did not communicate well with Loop (or Android APS).

If you have FW 2.6 on your OrangeLink or OrangeLink Pro, please [upgrade to FW 3.2](../faqs/rileylink-faqs.md#orangelink-firmware) as soon as possible.
