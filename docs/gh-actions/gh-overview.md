## Build <span translate="no">Loop</span> with a Browser
!!! info "<span translate="no">GitHub Build</span> = <span translate="no">Browser Build</span>"
    In <span translate="no">LoopDocs</span>, <span translate="no">GitHub Build</span> and <span translate="no">Browser Build</span> mean the same thing, i.e. building your app with a Web browser on the <span translate="no">GitHub</span> site.

<span translate="no">GitHub Browser Build</span> requires Loop 3.

### Advantages of <span translate="no">GitHub</span> Build

* Mac computer is not required
* Mac computer or PC or tablet are fine for <span translate="no">GitHub</span> build
* Xcode is not required
    * The time required for the initial setup for <span translate="no">GitHub</span> may take less time than one macOS and Xcode version update for those using [`Mac-Xcode Build`](../build/overview.md)
* Updates are easy
* Starting an update takes a few minutes of your time; the rest is automatic
* With the release of Loop 3.4, your app is automatically built at least once a month and is checked for updates once a week


### Considerations for <span translate="no">GitHub</span> Build

* The app is delivered to your phone via the <span translate="no">TestFlight</span> app
    * These apps are considered "Beta" by <span translate="no">Apple</span> and expire after 90 days
    * With Loop 3.4, once you succeed in building, the automatic process starts a build at least every 30 days
* After the <span translate="no">GitHub Build</span> starts, the automatic process takes about an hour to complete
    * You will receive an email indicating success (or failure)
    * Loop appears in the *TestFlight* app on the Loop phone, where it can be installed in seconds
* Personalized code customizations are tedious to set up but easy to maintain
    * Instructions are documented at [Customize with <span translate="no">GitHub</span>](../gh-actions/gh-customize.md)
    * Frequently used customizations are easy to copy and paste as documented at [Loop and Learn: Loop Customization](https://www.loopandlearn.org/custom-code#custom-list)


## Requirements

* **Loop 3 requires iOS 15.1 or higher.**

To build the <span translate="no">Loop</span> app using <span translate="no">GitHub</span>, you need:

1. Free <span translate="no">GitHub</span> account (instructions included in [First-Time with <span translate="no">GitHub</span> Actions](../gh-actions/gh-first-time.md))
1. [Apple Developer Membership](../build/apple-developer.md)
    * Must be a paid developer account
    * If building for a family member, review this section:
        * [Loopers Need Their Own *Apple* ID](../build/apple-developer.md#loopers-need-their-own-apple-id)
    * If building for a child (age depends on the country), review this section:
        * [Install *TestFlight* Loop for Child](../gh-actions/gh-deploy.md#install-testflight-loop-for-child)

Once you have the <span translate="no">Loop</span> app in TestFlight, you need:

1. [Compatible iPhone](../build/phone.md)
1. [Compatible Pump](../build/pump.md)
1. [Compatible CGM](../build/cgm.md)
1. [RileyLink Compatible Device](../build/rileylink.md) (not needed for Omnipod DASH)

## First-Time <span translate="no">GitHub</span> Builder

Steps that must be completed the first time are found at:

* [GitHub First-Time](../gh-actions/gh-first-time.md)

## Deploy and Updates

* Instructions to deploy and make updates are found at:
    * [GitHub Deploy](../gh-actions/gh-deploy.md)
    * [GitHub Update](../gh-actions/gh-update.md)
* And of course, there is an errors page:
    * [GitHub Errors](../gh-actions/gh-errors.md)
* For those testing the development branch who want to use <span translate="no">GitHub</span> build:
    * [GitHub Build for dev](../gh-actions/gh-update.md#github-build-for-dev)

## What if I get stuck?

Try to:

* Scroll back in the directions and see if you missed a paragraph or step.
* Compare your display with the graphics in LoopDocs.
    * Is something different or does yours have an error message?
    * Does the error message guide you to the problem and solution?
    * Be aware that <span translate="no">GitHub</span> often updates where things are - search for <span translate="no">GitHub</span> directions if your display looks different than LoopDocs.
* If you are still stumped - reach out for help: [How to Find Help](../intro/loopdocs-how-to.md#how-to-find-help).

