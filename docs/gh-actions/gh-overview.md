## Build Loop with a Browser
!!! info "`Github build` = `Browser `build`"
    In this section, `GitHub Build` and `Browser Build` mean the same thing, i.e. building *Loop* with a Web browser.

`GitHub build` can be used with Loop 3 and development versions.

### Advantages of *GitHub* Build

* Mac computer is not required
* Mac computer or PC or tablet are fine for *GitHub* build
* Xcode is not required
    * The time required for the initial setup for *GitHub* may take less time than one macOS and Xcode version update for those using [`Mac-Xcode Build`](../build/overview.md)
* Updates are easy
* Starting an update takes a few minutes of your time; the rest is automatic


### Disadvantages of *GitHub* Build

* After you start *GitHub* Build, the automatic process takes about an hour
    * You will receive an email indicating success (or failure)
    * Loop appears in the *TestFlight* app on the Loop phone, where it can be installed in seconds
* Personalized code customizations are tedious to set up but easy to maintain
    * Instructions are documented at [Customize with *GitHub*](../gh-actions/gh-customize.md)
    * Frequently used customizations are easy to copy and paste as documented at [Loop and Learn: Loop Customization](https://www.loopandlearn.org/custom-code#prepared-custom-list)


## Requirements

* **Loop 3 requires iOS 15.1 or higher.**
* **Temporary: "`Nightscout as a CGM`" only works with iOS 16 and higher for released code (3.2.x); but with iOS 15 and iOS 16 for dev branch.**

To Loop with the *GitHub* Build method, you need:

1. [Compatible iPhone](../build/phone.md)
1. [Compatible Pump](../build/pump.md)
1. [Compatible CGM](../build/step4.md)
1. [RileyLink Compatible Device](../build/step5.md) (not needed for Omnipod DASH)
1. Free *GitHub* account (instructions included in [First-Time with *GitHub* Actions](../gh-actions/gh-first-time.md))
1. [Apple Developer Membership](../build/step6.md)
    * Must be a paid developer account
    * If building for a family member, review this section:
        * [Loopers Need Their Own *Apple* ID](../build/step6.md#loopers-need-their-own-apple-id)
    * If building for a child (age depends on the country), review this section:
        * [Install *TestFlight* Loop for Child](../gh-actions/gh-deploy.md#install-testflight-loop-for-child)

## First-Time *GitHub* Builder

Steps that must be completed the first time are found at:

* [GitHub First-Time](../gh-actions/gh-first-time.md)

## Deploy and Updates

* Instructions to deploy and make updates are found at:
    * [GitHub Deploy](../gh-actions/gh-deploy.md)
    * [GitHub Update](../gh-actions/gh-update.md)
* And of course, an errors page is under construction:
    * [GitHub Errors](../gh-actions/gh-errors.md)
* For those testing the development branch who want to use *GitHub* build:
    * [GitHub Build for dev](../gh-actions/gh-update.md#github-build-for-dev)

## What if I get stuck?

Try to:

* Scroll back in the directions and see if you missed a paragraph or step.
* Compare your display with the graphics in LoopDocs.
    * Is something different or does yours have an error message?
    * Does the error message guide you to the problem and solution?
    * Be aware that *GitHub* often updates where things are - search for *GitHub* directions if your display looks different than LoopDocs.
* If you are still stumped - reach out for help: [How to Find Help](../intro/loopdocs-how-to.md#how-to-find-help).

