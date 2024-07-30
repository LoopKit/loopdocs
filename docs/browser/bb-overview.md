## Build with a Browser

* <span translate="no">Loop 3</span>&nbsp;can be built with a web browser using <span translate="no">GitHub Actions</span>
* The app is then installed by you on your phone using the *TestFlight* app

### Advantages of Building with a Browser

* *Mac* computer is not required to build or install the app
    * Anything with a browser works to build the *Loop* app: PC, Tablet, Mac or iPad
    * The *TestFlight* app is used to install the *Loop* app on your iPhone
* Compatible version of *Xcode* is provided by *GitHub*
    * The time required for the initial setup to build with a browser may take less time than one *macOS* and *Xcode* version update for those using [Build with *Mac*](../build/overview.md)
* Automatic Updates are loaded into *TestFlight*
    * With version 3.4, builds are automatically prepared at least once a month
    * You choose when to install the new app from TestFlight onto your phone
* Manual Updates are easy
    * Starting an update takes a few minutes of your time; it can be done from your phone; the rest is automatic and is done in about an hour

### Considerations for Building with a Browser

* After the *GitHub* Build starts, your app is ready to install on your *iPhone* in about an hour
* The app is delivered to your phone via *TestFlight*
    * The app is considered "Beta" by  *Apple* and expires after 90 days
    * <span translate="no">Loop 3.4</span>&nbsp; and later versions provide automatic build as the default
* Customization methods are documented at [Customize with Browser](custom-browser.md){: target="_blank" }

## Requirements

* **Loop 3 requires iOS 15.1 or higher on the phone.**

To build the&nbsp;_<span translate="no">Loop</span>_&nbsp;app using a browser, you need:

1. Free *GitHub* account (instructions included in [New *GitHub* Account](secrets.md#new-github-account){: target="_blank" })
1. [*Apple* Developer Membership](../build/apple-developer.md){: target="_blank" }
    * Must be a paid developer account
    * If building for a family member, review this section:
        * [Loopers Need Their Own *Apple* ID](../build/apple-developer.md#loopers-need-their-own-apple-id){: target="_blank" }
    * If building for a child (age depends on the country), review this section:
        * [*TestFlight* for a Child](../browser/phone-install.md#testflight-for-a-child){: target="_blank" }

Once you have the&nbsp;_<span translate="no">Loop</span>_&nbsp;app in *TestFlight*, you need:

1. [Compatible iPhone](../build/phone.md){: target="_blank" }
1. [Compatible Pump](../build/pump.md){: target="_blank" }
1. [Compatible CGM](../build/cgm.md){: target="_blank" }
1. [RileyLink Compatible Device](../build/rileylink.md){: target="_blank" }
    * Needed for Medtronic and Omnipod Eros only
    * Not needed for Bluetooth enabled pumps like DASH and Dana

## Instructions to Build with a Browser

### How-to Video to Build with a Browser

In addition to the pages linked above, there is a narrated video of each step needed to build using a browser. (This video shows build steps for version 3.2.3 or older. Some items are simplified for version 3.4.1 and newer.)

* [How to Build the *Loop* App With a Web Browser](https://www.youtube.com/watch?v=kiu5ho0MTW8){: target="_blank" }

Click in the comments for a full index of topics.  If you have issues with a step, use the index to  advance to the relevant part of the video. Subtitles are  in English. You can choose a different language but the automatic translation feature may provide translations that are not completely accurate.

### Configuration Pages

Steps that must be completed to build an app using the browser build method are grouped under the Configure to use Browser heading:

There is an introduction and summary page that should be read first. This has a table of all the steps with links to each step.

* [Introduction and Summary](intro-summary.md){: target="_blank" }

The rest of the pages in this section detail the required configuration steps needed:

* [Collect Secrets](secrets.md){: target="_blank" }
* [Prepare Fork](prepare-fork.md){: target="_blank" }
* [Identifiers](identifiers.md){: target="_blank" }
* [Prepare App](prepare-app.md){: target="_blank" }
* [Create Certificates](certs.md){: target="_blank" }
* [Build the *Loop* App](build-yml.md){: target="_blank" }

## Install on Phone

Once the app is built the first time:

* You need to set up [TestFlight Users](tf-users.md){: target="_blank" } who can then install that app on their phone
* This is true even if the only *TestFlight* user is you

Instructions to install on a phone are found at:

* [Install on Phone](phone-install.md){: target="_blank" }

## Update the App

Instructions to make updates are found at:

* [Update with Browser](bb-update.md){: target="_blank" }

There is also a helpful video for this process. Once again, this was prepared for an earlier version 3.2.3 or older. With version 3.4.1 and newer, the update and build is automatic:

* [How to Update and Rebuild DIY Loop with a Web Browser](https://www.youtube.com/watch?v=0ipTsiqbbrQ){: target="_blank" }

## Errors while Building

If you get an error, please consult:

* [Errors with Browser](bb-errors.md){: target="_blank" }

## Building the Development Version of the App

For experienced and/or advanced users who want to build the development version of the app, there is additional information at the link below. If you have not built using the browser build method before, it is suggested you first build the released version. Once you have a successful build, then follow the steps for the development version. Building the app is independent of installing the app on your phone from *TestFlight*.

* [Build Development Version](build-dev-browser.md){: target="_blank" }

## What if I get stuck?

Try to:

* Scroll back in the directions and see if you missed a paragraph or step
* Compare your display with the <span>graphics in *LoopDocs*</span>
    * Is something different or does yours have an error message?
    * Does the error message guide you to the problem and solution?
    * Be aware that *GitHub* sometimes updates displayed names or locations for menu items - search for *GitHub* directions if your display looks different than our documentation
* If you are still stumped - reach out for help: [How to Find Help](../intro/loopdocs-how-to.md#how-to-find-help)
    * Remember - to get help with Browser Build, all we need is your *GitHub* username and a brief description of your problem
