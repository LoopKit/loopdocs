## Build Loop with a Browser

This is a new method, available starting with the release of Loop 3, as well as for development versions.

* This can be used by those who don't own a Mac but want to Loop
* This can be used even if you do use a Mac
    * It adds the convenience of TestFlight to support you or a family member.
    * It adds recovery from TestFlight in case of an accident with your Loop phone while traveling, no need to travel with a Mac

!!! info "GitHub Build - Repeat Every 90 Days"
    When using the GitHub build method, Loop must be built every 90 days.

    * Rebuilding takes just a few taps in any browser - you can even do it on your phone.
    * The actual build time (how long from when you start the build to when it is available to install on your phone) is longer than using a Mac. Typically about 25 minutes, with another 20 minutes for TestFlight processing.

    When using the Mac method, Loop expires in 1 year, assuming provisioning profiles were cleared before the build.


## Requirements

The requirements for building and using the Loop app with the GitHub Build Actions method are given below.

1. [Compatible iPhone/iPod Touch](../build/step2.md)
1. [Compatible Pump](../build/step3.md)
1. [Compatible CGM](../build/step4.md)
1. [RileyLink Compatible Device](../build/step5.md) (not needed for Omnipod DASH)
1. Free github account (instructions included in [First-Time with GitHub Actions](../gh-actions/gh-first-time.md))
1. [Apple Developer Membership](../build/step6.md)
    * Must be a paid developer account
    * If building for a family member, review this section:
        * [Loopers Need Their Own Apple ID](../build/step6.md#loopers-need-their-own-apple-id)
    * If building for a child (age depends on the country), review this section:
        * [Install TestFlight Loop for Child](../gh-actions/gh-deploy.md#install-testflight-loop-for-child)

## First-Time GitHub Builder

There are a number of steps that must be completed the first time you use this method.

* The instructions are at this link: [GitHub First-Time](../gh-actions/gh-first-time.md).
* Plan to spend about 2 hours if you are fairly comfortable with a computer
* It make take longer for some

### Advantages of GitHub Build

Developer quote: "This frees up the dependency of having the most recent Xcode to build to a [phone with a] new version of iOS. Xcode only needs to support the iOS version on your phone when you are building directly to the phone."

* Mac computer is not required
* Most recent version of Xcode on a Mac computer is not required
    * No more updating Mac then updating Xcode
    * One time setup for GitHub probably takes less time than one Mac/Xcode update

### What if I get stuck?

Try to:

* Scroll back in the directions and see if you missed a paragraph or step.
* Compare your screen's display with the graphics in LoopDocs. Is something different or does yours have an error message? If you have an error message, does it guide you to the problem and solution?
* If you are still stumped - reach out for help: [How to Find Help](../intro/loopdocs-how-to.md#how-to-find-help).


## Repeat Builders

Once those first-time steps are completed, subsequent updates are simple. Complete instructions are found on the [GitHub Update](gh-update.md) page of LoopDocs. 
