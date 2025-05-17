## Build with a Browser

* <span translate="no">Loop 3</span>&nbsp;can be built with a web browser using <span translate="no">GitHub Actions</span>
* The app is then installed by you on your phone using the *TestFlight* app
* If you prefer to use *Xcode* on your *Mac*, head over to [Build with *Mac*](../build/overview.md){: target="_blank" }
* As long as you use the same *Apple Developer* account, the app you build is the same regardless of build method
    * When you install the app on your phone, settings and history are preserved; pump and CGM remain attached; selected Services are maintained

## Requirements

### Phone, CGM and Pump

To use the *Loop* app, you need:

* [Compatible Phone](../build/phone.md){: target="_blank" }
* [Compatible CGM](../build/cgm.md){: target="_blank" }
* [Compatible Pump](../build/pump.md){: target="_blank" }
    * For pumps that do not support Bluetooth communications (older Medronic and Omnipod Eros), you also need a [RileyLink Compatible Device](../build/rileylink.md){: target="_blank" }

### Accounts

To build the&nbsp;_<span translate="no">Loop</span>_&nbsp;app using a browser, you need:

1. Free *GitHub* account: (instructions found at [New *GitHub* Account](secrets.md#new-github-account){: target="_blank" })
1. Paid *Apple* Developer account: ($99/year; instructions found at [*Apple* Developer Account](../build/apple-developer.md){: target="_blank" })

## Instructions to Build with a Browser

### The Short Version

Complete instructions are found at this link for those comfortable with using *GitHub* and navigating the *Apple Developer* and *Apple App Connect* pages.

* [Using GitHub Actions + FastLane to deploy to TestFlight](https://github.com/LoopKit/LoopWorkspace/blob/main/fastlane/testflight.md)

### How-to Video to Build with a Browser

In addition to the pages linked below in [Configure to use Browser](#configure-to-use-browser), there is a narrated video of each step needed to build using a browser. (This video shows build steps for version 3.2.3 or older. Some items are simplified for version 3.4.1 and newer.)

* [How to Build the *Loop* App With a Web Browser](https://www.youtube.com/watch?v=kiu5ho0MTW8)

### Configure to use Browser

The steps on these pages must be completed for you to build an app using a browser:

1. [Introduction and Summary](intro-summary.md){: target="_blank" }
1. [Collect Secrets](secrets.md){: target="_blank" }
    * Some from *Apple*
    * Some from *GitHub*
1. [Prepare Fork](prepare-fork.md){: target="_blank" }
1. [Prepare Identifiers](identifiers.md){: target="_blank" }
1. [Prepare App](prepare-app.md){: target="_blank" }
1. [Prepare *TestFlight* Group](tf-users.md){: target="_blank" }
1. [Build the *Loop* App](build-yml.md){: target="_blank" }

The pages of instructions listed above give detailed steps on how to build the *Loop* app. If you are building a different app, you can follow the detailed instructions but will need to know the Fork, App Name, Identifiers and in some cases App Group for the App you intend to build. Once you build one app, subsequent apps are much easier to build.

* [Build Other Apps with Browser](other-apps.md){: target="_blank" }

## Install on Phone

Instructions to install on a phone are found at:

* [Install on Phone](phone-install.md){: target="_blank" }

## What if I get stuck?

!!! important "How to Ask for Help"
    First time setup should take several hours, but if you are having trouble:

    * [Click here to find help](bb-errors.md#help-with-errors){: target="_blank" }.

If you want to solve it yourself, try to:

* Scroll back in the directions and see if you missed a paragraph or step
    * Be sure you are copying the exact **names** needed for each step or clicking on the **link** associated with a particular step - many pages look similar
* Compare your display with the <span>graphics in *LoopDocs*</span>
    * Is something different or does yours have an error message?
    * Does the [Error](bb-errors.md){: target="_blank" } message guide you to the problem and solution?
    * Be aware that *GitHub* sometimes updates displayed names or locations for menu items - search for *GitHub* directions if your display looks different than our documentation

## Errors while Configuring and Building

If you get an error that you cannot figure out, reach out for help before you get frustrated or begin to delete things - let a mentor help you:

* General instructions: [How to Find Help](../intro/loopdocs-how-to.md#how-to-find-help)
* Browser Build instructions:
    * [Help with Errors](bb-errors.md#help-with-errors){: target="_blank" }
    * [Most Common Mistakes](bb-errors.md#most-common-mistakes){: target="_blank" }
    * With Browser Build, post your *GitHub* LoopWorkspace link and a brief description of your problem

* [Errors with Browser](bb-errors.md){: target="_blank" }

## Update the App

Instructions to make updates are found at:

* [Update with Browser](bb-update.md){: target="_blank" }

There is also a helpful video for this process. Once again, this was prepared for an earlier version 3.2.3 or older. With version 3.4.1 and newer, the update and build is automatic if your *Apple* Developer account is active, agreements are signed and certificates are valid:

* [How to Update and Rebuild DIY Loop with a Web Browser](https://www.youtube.com/watch?v=0ipTsiqbbrQ)

> With `Loop 3.6.0`, certificates are automatically created and renewed. You no longer need to renew certificates as a separate step.

## Other Topics

### Building the Development Version of the App

For experienced and/or advanced users who want to build the development version of the app, there is additional information at the link below. If you have not built using the browser build method before, it is suggested you first build the released version. Once you have a successful build, then follow the steps for the development version. Building the app is independent of installing the app on your phone from *TestFlight*.

* [Build Development Version](build-dev-browser.md){: target="_blank" }

### Mac vs Browser

These considerations were prepared when most people were using a Mac computer to build the *Loop* app.

* *Mac* computer is not required to build or install the app
    * Anything with a browser works to build the *Loop* app: PC, Tablet, Mac or iPad
    * The *TestFlight* app is used to install the *Loop* app on your iPhone
* Compatible version of *Xcode* is provided by *GitHub*
    * The time required for the initial setup to build with a browser may take less time than one *macOS* and *Xcode* version update for those using [Build with *Mac*](../build/overview.md){: target="_blank" }
* Automatic Updates are loaded into *TestFlight*
    * With version 3.4 and newer, builds are automatically prepared at least once a month
    * You choose when to install the new app from TestFlight onto your phone
    * **WARNING:** starting May 2025, [Manual Action for Automatic Build](automatic.md#manual-action-for-automatic-build){: target="_blank" } may be required - be sure to check monthly to see if you need to start a build manually
* Manual Updates are easy
    * Starting an update takes a few minutes of your time; it can be done from your phone; the rest is automatic and is done in about an hour
* After the *GitHub* Build starts, your app is ready to install on your *iPhone* in about an hour
* The app is delivered to your phone via *TestFlight*
    * The app is considered "Beta" by  *Apple* and expires after 90 days
    * <span translate="no">Loop 3.4</span>&nbsp; and newer versions provide automatic build as the default
* Customization methods are documented at [Customize with Browser](custom-browser.md){: target="_blank" }

