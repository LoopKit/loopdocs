## Build Loop with a Browser

This is a new method, available starting with the release of Loop 3, as well as for development versions.

* This can be used by those who don't own a Mac but want to Loop
* This can be used even if you do use a Mac
    * It adds the convenience of TestFlight to support you or a family member.
    * It adds recovery from TestFlight in case of an accident with your Loop phone while traveling, no need to travel with a Mac

!!! info "GitHub Build - Repeat Every 90 Days"
    When using the GitHub build method, Loop must be built every 90 days.

    * Rebuilding takes just a few taps in any browser - you can even do it on your phone.
    * The actual build time (how long from when you start the build to when it is available to install on your phone) is longer than using a Mac. Typically about 25 minutes.

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

## First Time Builder

There are a number of steps that must be completed the first time you use this method.

* The instructions are at this link: [First-Time with GitHub Actions](../gh-actions/gh-first-time.md).
* Plan to spend about 2 hours if you are fairly comfortable with a computer
* It make take longer for some
* The link above contains added graphics and details from the original instructions (warning - these instructions are a work in progress)

Those original instructions can be found at this link: [Basic Instructions](../gh-actions/gh-first-time.md#basic-instructions).


### What if I get stuck?

Try to:

* Scroll back in the directions and see if you missed a paragraph or step.
* Compare your screen's display with the graphics in LoopDocs. Is something different or does yours have an error message? If you have an error message, does it guide you to the problem and solution?
* If you are still stumped - reach out for help: [How to Find Help](../intro/loopdocs-how-to.md#how-to-find-help).


## Repeat Builders

Once those first time steps are completed, subsequent updates are simple. Complete instructions are found on the [GitHub Update](gh-update.md) page of LoopDocs.

1. Log in to github and find your LoopWorkspace repository
1. Update your fork (if needed)
1. Select Actions: Build Loop
1. After Build completes (15 to 30 minutes)
    * Loop is automatically updated on the phone if automatic installation is selected in TestFlight (default) for that phone
    * Install new version on phone if automatic installation is not selected in TestFlight  for that phone
