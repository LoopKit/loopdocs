## Loop Crashes Upon Opening

If your Loop app crashes immediately upon opening, you have a problem that needs to be fixed. What do I mean by "crashes"? Your Loop app immediately turns to a white (light mode) or black (dark mode) screen and then shuts itself down, landing you back at your iPhone's main screen. No amount of tapping will let you keep your Loop app open.

The most likely reason is [Your *Loop* App Expired](#your-loop-app-expired). But there can be other reasons.

* If you just updated your phone from iOS 16 to iOS 17 (or a similar major phone update), *Apple* spends a lot of time indexing your Apple Health data
    * Many people report 5 to 30 minutes during which they cannot open the *Loop* app but they also cannot open *Apple Health*
        * Wait until you can open *Apple Health* and then try to open the *Loop* app again
* If you still can't stop the crashes, see [Other Reasons](#other-reasons) and be sure to save the crash log

## Your *Loop* App Expired

Your Loop app has an expiration date. The expiration date will depend on the build method and may also depend on the type of developer account that signed the app.

* If you build with [Browser Build](#browser-build), your app will expire after 3 months
* If you build with a [Mac using a paid account](#mac-using-a-paid-account-1-year), your app will expire after 12 months
* If you build with a [Mac using a free account](#mac-using-personal-team-7-day), your app will expire after 7 days

### Browser Build

> Update to version 3.4 as soon as possible. The builds will then be automatic. So all you will need to do in install the latest build from *TestFlight* on your phone.

If you are running an older version, you do not get prior warning that the app is about to expire, although you can look in the *TestFlight* app and it will tell you. An in-app warning is supplied with version 3.4.

Please follow these steps to ensure you can build the app again: [How to Update or Rebuild](../browser/bb-update.md#how-to-update-or-rebuild){: target="_blank" }.


### Mac using a Paid account (1 year)

When your app expires after a year, you need to follow the steps on the [Build Updating](../build/updating.md){: target="_blank" } page. Your phone will probably have a new iOS that may require an updated version of Xcode that may require an updated Mac operating system.  All this is explained in the link above.  Give yourself time before expiration to prepare yourself.

To make it easy to build when you **have** to, practice building every 3 to 6 months. This makes the process much lower stress. Also, each time you build, when you follow the link above, you give yourself another full year before rebuilding is **required**. Please review the [Updating FAQS](../faqs/update-faqs.md){: target="_blank" }.

### Mac using Personal Team (7 day)

When your app expires, you simply need to open Xcode, reopen the project: File->Open Recent, plug your phone back into the computer and select it in Xcode and press the play button on your project again. This will rebuild. If you want to change to a paid signing team before rebuilding, please make sure to double-check which signing team is selected before building again.

### Switching From Free to Paid

If you started with a free account and switched to a paid account:

Many people *accidentally* build with their old free account

* How can you tell which you're signing with?
* The free signing team has the `(Personal Team)` listed after your name in the signing team

Remember that switching from free to paid changes the developer name incorporated into your Loop App

* A separate Loop app is created - see [Switching from Free to Paid Membership](../build/apple-developer.md#switching-from-free-to-paid-memberships){: target="_blank" } for more details
* Did you select the new app and enter all your settings into it and then delete the 7-day app?
* The new app issue only happens if you change developer name
* As long as you stick with the same developer ID, updated Loop apps are built over existing apps and all your settings should be maintained

## Other reasons

If you experience a crash for any other reason, please gather all the information you can about what was happening before the crash and report it to your favorite [Loop Social Media](../intro/loopdocs-how-to.md#how-to-find-help){: target="_blank" } help site - you will need to get some personalized help. Please - choose one site for your post and wait for someone to get back to you.  While you are waiting, search on any of the sites and, if on Facebook, read all the announcements.

### Save and Submit your Crash Logs
If you have continuous crashes, please save the crash logs so the developers can look at it. If you can, log into [Zulipchat](https://loop.zulipchat.com/) and post it directly.

* The crash logs can be found under Settings --> Privacy & Security --> Analytics & Improvements --> Analytics Data
* Scroll to find the file Loop_`DateTime`.ips for crash reports
