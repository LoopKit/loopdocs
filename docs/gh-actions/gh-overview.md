## Build Loop with a Browser

The new GitHub build method is available with the release of Loop 3, as well as for development versions.

* Installation on your phone is via TestFlight
* This can be used by those who don't own a Mac but want to Loop
* The GitHub build method can be used even if you do use a Mac - the two methods do not interfere with each other

TestFlight is the only method available for installation to a phone when using the GitHub build method, but can also be used with the Mac/Xcode build method.

Advantages of TestFlight:

* Allows you to install onto a new phone if yours is broken or lost while traveling
* Allows you to support family members who need their Loop app updated while away from home

!!! info "TestFlight - Repeat Every 90 Days"
    When installing Loop on a phone with TestFlight, it must be refreshed every 90 days.

    * Updating Loop and TestFlight takes just a few taps in any browser when using the GitHub build method - you can even do it on your phone.
    * Expect an hour of elapsed time from when you tap on the button to start the build on GitHub to when it is available to install on your phone. Typically about 25 minutes to build, with another 20 minutes for TestFlight processing.

## Requirements

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

## Pros and Cons

### Advantages of GitHub Build

Developer quote: "This frees up the dependency of having the most recent Xcode to build to a [phone with a] new version of iOS. Xcode only needs to support the iOS version on your phone when you are building directly to the phone."

* Mac computer is not required
* Most recent version of Xcode is not required
    * No more updating macOS then updating Xcode
    * One time setup for GitHub may take less time than one macOS/Xcode version update

### Cons

* There are no instructions for applying customizations
* Stick with Mac / Xcode build (for now) if you want to customize
* Hint - when customization instructions are provided - you will be making more forks for every submodule you customize and you will be responsible for keeping those forks up to date

## What if I get stuck?

Try to:

* Scroll back in the directions and see if you missed a paragraph or step.
* Compare your screen's display with the graphics in LoopDocs. Is something different or does yours have an error message? If you have an error message, does it guide you to the problem and solution?
* If you are still stumped - reach out for help: [How to Find Help](../intro/loopdocs-how-to.md#how-to-find-help).

