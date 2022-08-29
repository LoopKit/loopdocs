# Updating/Rebuilding Loop FAQs

First, please take a minute to understand what the words mean.

* "Updating Loop" is the process downloading a new version of Loop code 

* "Rebuilding Loop" is the process of using your existing download of Loop code

In both cases, you build the code with Xcode to install over an existing app on your phone or onto a new device.

For the rest of this page, the word Update is used. For most people, it is simplest just the use the build select script which automatically downloads fresh code every time.

If you have a very slow download speed or if you do a lot of customizations, it may be worth your time to decide if you need a new download.

* Use Finder to check the date of your last download by looking in the Downloads/BuildLoop folder
* Check the date of the last Loop release at [GitHub LoopKit/Loop release page](https://github.com/LoopKit/Loop/releases)
* If the date in Finder is after the release date, [double click on the Loop.xcworkspace file using these instructions](../build/code_customization.md#find-my-dowloaded-loop-code)

## When Should I Update?

* **Best Practice**
    * Build if a serious bug-fix is reported
    * Build, using the [Updating Instructons](../build/updating.md), two to four times a year so that it becomes easier and you are ready in case of an emergency
    * Each time you build, the app expiration date is bumped out a full year from your build date
* **Required**
    * When your one-year expiration date forces you
    * Do not wait until the app expires - it will stop working; see [Loop is No Longer Available](../build/updating.md#loop-is-no-longer-available)
    * Hint - start a few weeks early and take your time
* **Optional**
    * A new version of Loop is released and you want to install it
    * You want to try a different branch or fork of Loop

### Steps to Update

Updating Loop is the same idea as what happens to your other apps on your iPhone when you update them from the App Store on the phone. A refreshed version of the same app appears on the phone, simply updating-in-place the same Loop you were using with an updated version.

* Do **NOT** delete your current app from your phone - even if it says "Loop is No Longer Available"
* There are files stored on your phone that will be read in as soon as the new Loop app is installed
* If you deleted your app, then you have to enter all your settings again
    * This is a good time to configure your phone to avoid accidental deletion
    * Do an internet search like this: "iOS 15.4 prevent app deletion" where you use your current phone iOS version number and follow the instructions

#### Typical Apple Update Schedule:

* Each September, Apple releases a major iOS version which typically works with the current macOS but requires a new Xcode version
* Each September, Apple releases a major macOS version (but doesn't require you to update your Mac, yet)
* Each March, you must update to the current macOS (major version) to continue building applications

## Where should I start when I want to update my Loop?

**ALWAYS start with the [Update Loop page](../build/updating.md) before any new build that you'd be doing.** That page is important because it will offer information on the updates you need to do before building, as well as information that might need to be considered.

Do not simply build with your old downloaded folder from months ago. There is a high likelihood that your original code from awhile ago is outdated and might not build with the current phone iOS. Grab new code and you will get the compatible version that has all the latest and greatest features and bug fixes.


## Will I have to delete my old Loop app?

No. Do not delete your old Loop. In fact, that is a bad idea as you will lose your currently paired pod and/or settings if you do that. So, don't delete.

**The exception to the rule is if you build Loop dev on your phone and want to return to Loop 2.2.x or any FreeAPS fork.**

* Refer to [What if I change the branch or fork?](#what-if-i-change-the-branch-or-fork)

## Does updating make a separate, second Loop app?

No. Loop is simply updated in-place, written right over the old version.

The only exception to this is if you update/build using a different developer signing team than your current Loop app.

* The app's identity on your phone is defined by the developer ID.
* If you change that unique ID, your phone interprets that as a unique app as well...giving you two Loop apps on the phone.
    * Therefore, if changing developer accounts...you will get a new Loop app, and you would need a new Pod.
    * You'll need to transfer your settings manually to the new app and delete your old app.

## Will my settings be saved when I update?

Yes. That's why we don't delete the app. Your settings will be saved so long as you use the same developer ID.

## Will my pod still work when I update?

Yes. So long as you use the same developer ID as you originally built the app with before.

## How can I confirm what version was installed?

The Loop version is given at the top of the Loop settings page.

There is more detailed information about how the Loop app was built at the top of the Issue Report (Loop -> Settings -> Issue Report) as shown in the graphic in the next section.

## How can I confirm Xcode version I used?

The information in the graphic below includes the Xcode version number used for the build. In this case, the major version for Xcode is 12 and the minor version is 5 (E is the 5th letter of the English alphabet).  The main thing to notice for this example is the Loop app was built with Xcode version 12.5. If this phone was subsequently upgraded to iOS 15, the Loop app would continue to work.

**DO NOT INSTALL iOS 15 if the Xcode version on your Loop build is 12D or earlier - the Loop app will immediately stop working and you will have to rebuild Loop.**

![top of issue report showing loop, xcode and expiration](img/loop-version.svg){width="500"}

!!! info "Profile Expiration"

    * The profile expiration will not be shown for Loop v2.2.4 or earlier.
    * For this example, the profile expires much sooner than 12 months after the Loop app was built
        * [Updating: Step 4A ](../build/updating.md#step-4a-delete-old-provisioning-profiles) provides instructions to delete your old provisioning profile when building your Loop app - this gives you a full year after you build

## What if I change the branch or fork?

Does not matter. Changing the branch and even the fork is an "updating Loop" action. Nothing about the information above changes with the following exception.

**The exception to the rule is if you build Loop dev on your phone and want to return to Loop 2.2.x or any FreeAPS fork.**

* In this case, the database storage is different between Loop 3 and Loop 2.2.x
* Loop dev can read the data stored by Loop 2.2.x, but the reverse is not true
* If you are downgrading from Loop dev to Loop 2.2.x or FreeAPS, you need to first record settings, delete the old app and then build the desired app, enter your settings and add your pump (new pod required for Omnipod)

## What if I'm changing phones?

Changing phones is a little different than just [updating](../build/updating.md).

!!! abstract "New Phone Checklist"

    * When you change phones, Apple will force you to the latest iOS version
    * Make sure you can build to that iOS version before trying to transfer Loop to the new phone
    * You can use the old phone as your looping phone until you get the new one ready
        * When turning the old phone in for a rebate, you typically have a week or two before you have to turn it in
        * When you transfer information from your old phone to your new phone, all the Loop settings files get copied to the new device including information about the pod (if one is running)
        * You then need to build Loop on the new phone and it remembers those settings
        * It's a good idea to do this at pod change time, just in case, and to record (or screenshot) all your settings
    * Once the transfer is completed check [all your settings and all your permissions](../operation/overview.md) on the new phone

You can find the instructions written up in this [article](https://www.loopandlearn.org/new-device).

## How long does it take?

Assuming your macOS and Xcode updates are done, then plan on about 30 minutes.
