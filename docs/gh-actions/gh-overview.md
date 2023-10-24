## Build with a Browser

* <span translate="no">Loop 3</span>&nbsp;can be built with a web browser using <span translate="no">GitHub Actions</span>
* The app is then installed remotely on the phone using *TestFlight*

### Advantages of Building with a Browser

* *Mac* computer is not required to build or install the app
    * Anything with a browser works to build the *Loop* app: PC, Tablet, Mac or iPad
    * The *TestFlight* app is used to install the *Loop* app on your iPhone
* Xcode is not required
    * The time required for the initial setup for building with a browser may take less time than one *macOS* and *Xcode* version update for those using [*Mac-Xcode* Build](../build/overview.md)
* Updates are easy
    * Starting an update takes a few minutes of your time; the rest is automatic
    * Planned for the next release: app will build automatically at least once a month and is checked for updates once a week

### Considerations for Building with a Browser

* The app is delivered to your phone via *TestFlight*
    * The app is considered "Beta" by  *Apple* and expires after 90 days
    * With the next release, which includes automatic builds, this will be even easier than it is now
* After the&nbsp;<span translate="no">*GitHub* Build</span>&nbsp;starts, the process takes about an hour to complete
    * You receive an email indicating success (or failure)
    * The&nbsp;_<span translate="no">Loop</span>_&nbsp;app appears in the *TestFlight* app on the phone, where it can be installed in seconds
* Frequently used customizations are easy to copy and paste as documented at&nbsp;[_<span translate="no">Loop and Learn: Loop Customization</span>_](https://www.loopandlearn.org/custom-code#custom-list)
* Personalized code customizations are tedious to set up but easy to maintain
    * Instructions are documented at [Customize using Browser](../gh-actions/gh-customize.md)

## Requirements

* **Loop 3 requires iOS 15.1 or higher on the phone.**

To build the&nbsp;_<span translate="no">Loop</span>_&nbsp;app using a browser, you need:

1. Free *GitHub* account (instructions included in [Configure to use Browser](gh-first-time.md))
1. [*Apple* Developer Membership](../build/apple-developer.md)
    * Must be a paid developer account
    * If building for a family member, review this section:
        * [Loopers Need Their Own *Apple* ID](../build/apple-developer.md#loopers-need-their-own-apple-id)
    * If building for a child (age depends on the country), review this section:
        * [*TestFlight* for a Child](../gh-actions/gh-deploy.md#testflight-for-a-child)

Once you have the&nbsp;_<span translate="no">Loop</span>_&nbsp;app in *TestFlight*, you need:

1. [Compatible iPhone](../build/phone.md)
1. [Compatible Pump](../build/pump.md)
1. [Compatible CGM](../build/cgm.md)
1. [RileyLink Compatible Device](../build/rileylink.md) (not needed for Omnipod DASH)

## Configuration to Build with a Browser

Steps that must be completed to configure for building with a browser are found at:

* [Configure to use Browser](gh-first-time.md)

## Install on Phone

Instructions to install on your phone are found at:

* [Install on Phone](gh-deploy.md)

## Update the App

Instructions to make updates are found at:

* [Update with Browser](gh-update.md)

## Errors while Building

If you get an error, please consult:

* [Errors with Browser](gh-errors.md)

## Building the development version of the app

For experienced and/or advanced users who want to build the development version of the app, there is additional information at the link below. If you have not built using the browser build method before, it is strongly recommended you first build the released version. Once you have a successful build, then follow the steps for the development version. Building the app is independent of installing the app on your phone from *TestFlight*.

* [Build Development Version](gh-update.md#build-development-version)

## What if I get stuck?

Try to:

* Scroll back in the directions and see if you missed a paragraph or step
* Compare your display with the <span>graphics in *LoopDocs*</span>
    * Is something different or does yours have an error message?
    * Does the error message guide you to the problem and solution?
    * Be aware that *GitHub* sometimes updates displayed names or locations for menu items - search for *GitHub* directions if your display looks different than our documentation
* If you are still stumped - reach out for help: [How to Find Help](../intro/loopdocs-how-to.md#how-to-find-help)
    * Remember - to get help with Browser Build, all we need is your *GitHub* username and a brief description of your problem
