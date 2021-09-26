# Updating/Rebuilding Loop FAQs

First, please take a minute to understand what the words mean.

"Updating Loop" is the process of getting a new download of Loop's code and using that to update your Loop by building the code with Xcode and then installing the new app on your phone. You do this

* When your one-year expiration date forces you (hint - start a few weeks early and take your time)
* A new version of Loop is released and you want to install it
* You want to try a different branch or fork of Loop (this used to be much more common several years ago when new features and improvements were being offered for testing prior to release in Loop)

Updating Loop is the same idea as what happens to your other apps on your iPhone when you update them from the App Store on the phone. A refreshed version of the same app appears on the phone, simply replacing-in-place the same Loop you were using with an updated version.

* Do NOT delete your current app from your phone - even if it says "Loop" is No Longer Available
* There are files stored on your phone that will be read in as soon as the new Loop app is installed
* If you deleted your app, then you have to enter all your settings again

## Where should I start when I want to update my Loop?

**ALWAYS start with the [Update Loop page](../build/updating.md) before any new build that you'd be doing.** That page is important because it will offer information on the updates you need to do before building, as well as any late breaking things that might need to be considered.

Do not simply build with your old downloaded folder from months ago. There is a high likelihood that your original code from awhile ago is outdated. Grab new code and you will get the version that has all the latest and greatest features and bug fixes.

## When do I have to update/rebuild?

Absolute minimum:

* 1 year from when you last built (paid account).

Good ideas:

* When Apple releases a new iOS version, check to see if that requires an update to [Xcode](../build/step8.md#how-do-all-the-minimum-versions-relate-to-each-other) and if that update to Xcode requires a macOS update
* Best practice - update your computer before you update your phone iOS so you can always be ready to build if necessary
* Good practice - build to a phone (it doesn't need to be the Looper's phone) a couple of times year just so you don't forget how - this makes the one year rebuild much easier
* If on [dev branch](branch-faqs.md#whats-going-on-in-the-dev-branch): Please follow the loop zulipchat forum so you can update when appropriate.

Issue specific minimum:

* There are also times where you may need to update for "hot-fixes" to keep your Loop working when other things change.

For example, after Dexcom G6 transmitters had been in-use for a while, a new style Dexcom G6 transmitters began to be shipped with a different Bluetooth protocol. Loop's code was updated quickly to interface with the new transmitters (this enables offline looping instead of requiring use of Dexcom Share). But you only got that update to Loop by rebuilding the app.


## Will I have to delete my old Loop app?

No. Do not delete your old Loop. In fact, that is a bad idea as you will lose your currently paired pod and/or settings if you do that. So, don't delete (except for two situations below):

1. You broke it: There used to be a glitch in Loop where if you entered the target correction range backwards, then your Loop app stopped working. You can't do that anymore, but it's always possible something else might require you to delete your app.

2. Moving from [dev branch back down to master branch](#what-if-im-changing-branches-does-that-matter). The new dev branch requires you to delete your dev build prior to returning to master.

## Does updating make a separate, second Loop app?

No. Loop is simply updated in-place, written right over the old version.

The only exception to this is if you update/build using a different developer signing team than your original Loop app was built with. The app's identity on your phone is defined by the developer team that you signed the app with. That team has a unique ID to identify the app. So, if you change that unique ID, your phone interprets that as a unique app as well...giving you two Loop apps on the phone. Therefore, if changing developer accounts...you will get a new Loop app, and you would need a new Pod. You'll need to transfer your settings manually to the new app and delete your old app.

## Will my settings be saved when I update?

Yes. That's why we don't delete the app. Your settings will be saved.

## Will my pod still work when I update?

Yes. So long as you use the same developer team as you originally built the app with before.

## How can I confirm what version was installed?

The Loop version is given at the top of the Loop settings page.

There is more detailed information about how the Loop app was built at the top of the Issue Report (Loop -> Settings -> Issue Report) as shown in the graphic in the next section.

## How can I confirm Xcode version I used?

The information in the graphic below includes the Xcode version number used for the build. In this case, the major version for Xcode is 12 and the minor version is 5 (E is the 5th letter of the English alphabet).  The main thing to notice for this example is the Loop app was built with Xcode version 12.5. If this phone was subsequently upgraded to iOS 15, the Loop app would continue to work.

**DO NOT INSTALL iOS 15 if the Xcode version on your Loop build is 12D or earlier - the Loop app will immediately stop working and you will have to rebuild Loop.**

![top of issue report showing loop, xcode and expiration](img/loop-version.svg){width="500"}

!!! danger "Profile Expiration"

    * The profile expiration will not be shown for Loop v2.2.4 or earlier.
    * For this example, the profile expires much sooner than 12 months after the Loop app was built
        * [Updating: Step 4A ](../build/updating.md#step-4a-delete-old-provisioning-profiles) provides instructions to delete your old provisioning profile when building your Loop app - this gives you a full year after you build

## What if I'm changing branches? Does that matter?

Does not matter. Moving between branches and forks is an "updating Loop" action. Nothing about the information above changes.

**The exception to the rule is if you build the dev branch on your phone and want to return to master. In this case, the database storage is different between dev and master. It's a one-way trip.  The dev branch can read the data stored by master, but master cannot read the data stored by dev. If you are downgrading from dev to master, you need to first record settings, delete the old app, build master, enter your settings and (if using Omnipod), start at new pod.**

## What if I'm changing phones?

Changing phones is a little different than updating. You can find the instructions written up in this [article](https://www.loopandlearn.org/new-device/).

## How long does it take?

Assuming your macOS and Xcode updates are done, then plan on about 30 minutes.
