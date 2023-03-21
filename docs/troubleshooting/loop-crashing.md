## Loop Crashes Upon Opening

If your Loop app crashes immediately upon opening, you have a problem that needs to be fixed. What do I mean by "crashes"? Your Loop app immediately turns to a white (light mode) or black (dark mode) screen and then shuts itself down, landing you back at your iPhone's main screen. No amount of tapping will let you keep your Loop app open.

* If you just built Loop 3.0.0 or just updated the iOS while running Loop 3.0.0
    * The most likely cause is the "[Apple Health Glitch](#apple-health-glitch)"
    * This problem was fixed in Loop 3.2.0 so update as soon as possible
* If you are running Loop 2.2.x:
    * The most likely cause of this is your [Loop App Expired](#loop-app-expired)

## Apple Health Glitch

With Loop version 3.0.0, there is a known glitch that is fixed in the development (dev) branch and thus will be fixed in the next Loop release.

### Solution

Long term solution, build Loop 3.2.x or newer version.

Short term solution if the Loop app crashes following a update to version 3.0.0 or an iOS update:

1. Turn **off** Apple Health permissions for Loop
    * Tap on iOS Settings
    * Tap on Health (:heart: icon)
    * Tap on Data Access & Devices
    * Tap on Loop
    * Tap on `Turn Off All`
1. Return to phone main screen and open Loop
1. Loop app should now open without issue
1. Turn **on** Apple Health permissions for Loop
    * Tap on iOS Settings
    * Tap on Health (:heart: icon)
    * Tap on Data Access & Devices
    * Tap on Loop
    * Tap on `Turn On All`

Loop 3 has a data store that contains all Looping information for 7 full days. So there will be no loss of Loop information stored in Apple Health by taking this action - so long as permissions are restored.

!!! note "More Details - if you are interested"
    After an iOS update, the phone goes through a new indexing process, which Apple warns can slow down performance and increase battery usage over the first few hours.

    Starting with iOS 16.2, the Apple Health Glitch with Loop was observed by some users. The anchor that Loop uses to correlate an item in its data store with that same item stored Apple Health was sometimes "lost". The way Loop handled that "took too long" to resolve and the app would be closed by the operating system. The work-around shown above fixes this for Loop 3.0.0.

    Later versions of Loop use a modification for the handling of anchors, so this will be transparent to the user.

## Loop App Expired

Your Loop app has an expiration date. The expiration date will depend on the type of developer account that signed the app.

* If you build with a paid account, your app will expire after 12 months.
* If you build with a free account, your app will expire after 7 days.

### Paid account (1 year)

When your app expires after a year, you need to follow the steps on the [Build Updating](../build/updating.md) page. Your phone will probably have a new iOS that may require an updated version of Xcode that may require an updated Mac operating system.  All this is explained in the link above.  Give yourself time before expiration to prepare yourself.

To make it easy to build when you **have** to, practice building every 3 to 6 months. This makes the process much lower stress. Also, each time you build, when you follow the link above, you give yourself another full year before rebuilding is **required**. Please review the [Updating FAQS](../faqs/update-faqs.md)

### Personal Team (7 day)

When your app expires, you simply need to open Xcode, reopen the project: File->Open Recent, plug your phone back into the computer and select it in Xcode and press the play button on your project again. This will rebuild. If you want to change to a paid signing team before rebuilding, please make sure to double-check which signing team is selected before building again.

### Switching From Free to Paid

If you started with a free account and switched to a paid account:

Many people *accidentally* build with their old free account

* How can you tell which you're signing with?
* The free signing team has the `(Personal Team)` listed after your name in the signing team

Remember that switching from free to paid changes the developer name incorporated into your Loop App

* A separate Loop app is created - see [Switching from Free to Paid Membership](../build/step6.md#switching-from-free-to-paid-memberships) for more details
* Did you select the new app and enter all your settings into it and then delete the 7-day app?
* The new app issue only happens if you change developer name
* As long as you stick with the same developer ID, updated Loop apps are built over existing apps and all your settings should be maintained

## Other reasons

If you experience a crash for any other reason, please gather all the information you can about what was happening before the crash and report it to your favorite [Loop Social Media](../intro/loopdocs-how-to.md#how-to-find-help) help site - you will need to get some personalized help. Please - choose one site for your post and wait for someone to get back to you.  While you are waiting, search on any of the sites and, if on Facebook, read all the announcements.
