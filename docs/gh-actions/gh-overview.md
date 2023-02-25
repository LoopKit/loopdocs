## Build Loop with a Browser

The new GitHub build method is available with the release of Loop 3, as well as for development versions.

* Installation on your phone is via TestFlight
* This can be used by those who don't own a Mac but want to Loop
* The GitHub build method can be used even if you do use a Mac - the two methods do not interfere with each other

TestFlight is the only method available for installation to a phone when using the GitHub build method, but it can also be used as a remote build option with the Mac-Xcode build method - see [TestFlight from Xcode](../build/testflight-xcode.md).

## Pros and Cons

### Advantages of GitHub Build

* Mac computer is not required
* Most recent version of Xcode is not required
    * No more updating macOS then updating Xcode for certain iOS upgrades
    * The time required for the initial setup for GitHub may take less time than one macOS/Xcode version update
* Updates take a few minutes of your time to start and are ready to install on your phone in about an hour

### Cons

The customization process is more involved. One set of commonly requested customizations is available, as explained at [Loop and Learn: Loop Customization](https://www.loopandlearn.org/github-lnl-patches).

* Stick with Mac-Xcode build (for now) if you want to do your own customizations
    * You can still use [TestFlight with your Mac-Xcode build](../build/testflight-xcode.md)
* There are no instructions for applying customizations
    * Hints:
    * You need to make a fork for every submodule you want to customize
    * You need to update your LoopWorkspace Fork to point to your submodule forks
    * You are responsible for keeping those forks up to date

## Requirements

**Loop 3 requires iOS 15.1 or higher**

The requirements for building and using the Loop app with the GitHub Build Actions method are given below.

1. [Compatible iPhone/iPod Touch](../build/step2.md)
1. [Compatible Pump](../build/step3.md)
1. [Compatible CGM](../build/step4.md)
1. [RileyLink Compatible Device](../build/step5.md) (not needed for Omnipod DASH)
1. Free GitHub account (instructions included in [First-Time with GitHub Actions](../gh-actions/gh-first-time.md))
1. [Apple Developer Membership](../build/step6.md)
    * Must be a paid developer account
    * If building for a family member, review this section:
        * [Loopers Need Their Own Apple ID](../build/step6.md#loopers-need-their-own-apple-id)
    * If building for a child (age depends on the country), review this section:
        * [Install TestFlight Loop for Child](../gh-actions/gh-deploy.md#install-testflight-loop-for-child)

## First-Time GitHub Builder

There are a number of steps that must be completed the first time you use this method.

* [GitHub First-Time](../gh-actions/gh-first-time.md)

## Deploy and Updates

* Instructions to deploy and make updates are found at:
    * [GitHub Deploy](../gh-actions/gh-deploy.md)
    * [GitHub Update](../gh-actions/gh-update.md)
* And of course, an errors page is under construction:
    * [GitHub Errors](../gh-actions/gh-errors.md)
* For those testing the development branch who want to use GitHub build:
    * [GitHub Build for dev](../gh-actions/gh-update.md#github-build-for-dev)

## What if I get stuck?

Try to:

* Scroll back in the directions and see if you missed a paragraph or step.
* Compare your screen's display with the graphics in LoopDocs. Is something different or does yours have an error message? If you have an error message, does it guide you to the problem and solution?
* If you are still stumped - reach out for help: [How to Find Help](../intro/loopdocs-how-to.md#how-to-find-help).

