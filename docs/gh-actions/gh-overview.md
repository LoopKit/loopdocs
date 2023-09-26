## Build &nbsp;<span translate="no">Loop</span>&nbsp;with a Browser
!!! info "<span translate="no">GitHub Build</span>&nbsp;= &nbsp;<span translate="no">Browser Build</span>"
    In &nbsp;<span translate="no">LoopDocs</span>, &nbsp;<span translate="no">GitHub Build</span>&nbsp;and &nbsp;<span translate="no">Browser Build</span>&nbsp;mean the same thing, i.e. building your app with a Web browser on the &nbsp;<span translate="no">GitHub</span>&nbsp;site.

<span translate="no">GitHub Browser Build</span>&nbsp;requires Loop 3.

### Advantages of &nbsp;<span translate="no">GitHub</span>&nbsp;Build

* Mac computer is not required
    * Anything with a browser works: PC, Tablet, Mac or iPad
    * It could be done with a phone, but the steps may be hard to navigate
* Xcode is not required
    * The time required for the initial setup for &nbsp;<span translate="no">GitHub</span>&nbsp;may take less time than one macOS and Xcode version update for those using [`Mac-Xcode Build`](../build/overview.md)
* Updates are easy
    * Starting an update takes a few minutes of your time; the rest is automatic
    * With the release of Loop 3.4, your app is automatically built at least once a month and is checked for updates once a week


### Considerations for &nbsp;<span translate="no">GitHub</span>&nbsp;Build

* The app is delivered to your phone via the &nbsp;<span translate="no">TestFlight</span>&nbsp;app
    * These apps are considered "Beta" by &nbsp;<span translate="no">Apple</span>&nbsp;and expire after 90 days
    * With Loop 3.4, once you succeed in building, the automatic process starts a build at least every 30 days
* After the &nbsp;<span translate="no">GitHub Build</span>&nbsp;starts, the automatic process takes about an hour to complete
    * You will receive an email indicating success (or failure)
    * Loop appears in the *TestFlight* app on the Loop phone, where it can be installed in seconds
* Frequently used customizations are easy to copy and paste as documented at [Loop and Learn: Loop Customization](https://www.loopandlearn.org/custom-code#custom-list)
* Personalized code customizations are tedious to set up but easy to maintain
    * Instructions are documented at [Customize with &nbsp;<span translate="no">GitHub</span>](../gh-actions/gh-customize.md)


## Requirements

* **Loop 3 requires iOS 15.1 or higher.**

To build the &nbsp;<span translate="no">Loop</span>&nbsp;app using &nbsp;<span translate="no">GitHub</span>, you need:

1. Free &nbsp;<span translate="no">GitHub</span>&nbsp;account (instructions included in [First-Time with &nbsp;<span translate="no">GitHub</span>&nbsp;Actions](../gh-actions/gh-first-time.md))
1. [Apple Developer Membership](../build/apple-developer.md)
    * Must be a paid developer account
    * If building for a family member, review this section:
        * [Loopers Need Their Own *Apple* ID](../build/apple-developer.md#loopers-need-their-own-apple-id)
    * If building for a child (age depends on the country), review this section:
        * [Install *TestFlight* Loop for Child](../gh-actions/gh-deploy.md#install-testflight-loop-for-child)

Once you have the &nbsp;<span translate="no">Loop</span>&nbsp;app in TestFlight, you need:

1. [Compatible iPhone](../build/phone.md)
1. [Compatible Pump](../build/pump.md)
1. [Compatible CGM](../build/cgm.md)
1. [RileyLink Compatible Device](../build/rileylink.md) (not needed for Omnipod DASH)

## First-Time &nbsp;<span translate="no">GitHub</span>&nbsp;Builder

Steps that must be completed the first time are found at:

* [GitHub First-Time](../gh-actions/gh-first-time.md)

## Deploy and Updates

* Instructions to deploy and make updates are found at:
    * [GitHub Deploy](../gh-actions/gh-deploy.md)
    * [Update with Browser](../gh-actions/gh-update.md)
* And of course, there is an errors page:
    * [GitHub Errors](../gh-actions/gh-errors.md)
* For those testing the development branch who want to use &nbsp;<span translate="no">GitHub</span>&nbsp;build:
    * [Browser Build for dev](../gh-actions/gh-update.md#github-build-for-dev)

## What if I get stuck?

Try to:

* Scroll back in the directions and see if you missed a paragraph or step.
* Compare your display with the graphics in LoopDocs.
    * Is something different or does yours have an error message?
    * Does the error message guide you to the problem and solution?
    * Be aware that &nbsp;<span translate="no">GitHub</span>&nbsp;often updates where things are - search for &nbsp;<span translate="no">GitHub</span>&nbsp;directions if your display looks different than LoopDocs.
* If you are still stumped - reach out for help: [How to Find Help](../intro/loopdocs-how-to.md#how-to-find-help).

