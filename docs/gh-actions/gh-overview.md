## Build Loop with a Browser

This is a new method, available starting with the release of Loop 3, as well as for development versions.

This can be used by those who don't own a Mac or want the convenience of TestFlight to support themselves or a family member.

!!! info "Build Every 90 Days"
    This method requires the app to be built once every 90 days.
    
    Rebuilding takes just a few taps in any browser - you can even do it on your phone.

## Requirements

The requirements for building and using the Loop app with this method are given below.

1. [Compatible iPhone/iPod Touch](../build/step2.md)
1. [Compatible Pump](../build/step3.md)
1. [Compatible CGM](../build/step4.md)
1. [RileyLink Compatible Device](../build/step5.md) (not needed for Omnipod DASH)
1. Free github account (instructions included in [First-Time with Github Actions](../gh-actions/gh-first-time.md))
1. [Apple Developer Membership](../build/step6.md)
    * Must be a paid developer account
    * If building for a child, be sure to read [Loopers Need Their Own Apple ID](../build/step6.md#loopers-need-their-own-apple-id)

## First Time Builder

There are a number of steps that must be completed the first time you use this method.

[First-Time with Github Actions](../gh-actions/gh-first-time.md)

### What if I get stuck?

Try to:

* Scroll back in the directions and see if you missed a paragraph or step.
* Compare your screen's display with the graphics in the step. Is something different or does yours have an error message? If you have an error message, does it guide you to the problem and solution?
* If you are still stumped - reach out for help: [How to Find Help](../intro/loopdocs-how-to.md#how-to-find-help).


## Repeat Builders

Once those first time steps are completed, each update is simple. Complete instructions are found at [Github Loop Update](gh-update.md)

1. Update your fork (if needed)
1. Select Actions: Build Loop
1. After Build completes (15 to 30 minutes), install new version on Loopers phone
