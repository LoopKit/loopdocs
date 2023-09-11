## Two Loop Build Methods

With the release of Loop 3, there are two Build Methods. If you have never built Loop before, you will probably find the GitHub process (also know as Browser Build) easiest. If you are a long time Looper, either method is fine. You only need to follow one of the Build methods, but you can use both methods if you want.

The Build Steps have been split into two tabs:

* [Browser Build](../gh-actions/gh-overview.md)
    * Build Loop using GitHub Actions (no computer required)
* [Mac-Xcode Build](../build/overview.md)
    * Traditional, build Loop on a Mac with Xcode

There are some common requirements and then some different requirements for the two methods.

## Common Requirements

These requirements are independent of how you build the Loop app:

1. [Compatible iPhone](../build/phone.md)
1. [Compatible Pump](../build/step3.md)
1. [Compatible CGM](../build/step4.md)
1. [RileyLink Compatible Device](../build/step5.md) (not needed for Omnipod DASH)
1. [Apple Developer Membership](../build/step6.md)
    * For Browser Build - must be a paid developer account
    * If building for a child, be sure to read [Loopers Need Their Own Apple ID](../build/step6.md#loopers-need-their-own-apple-id)

### Added Requirements for Browser Build

In addition to the paid Apple Developer account, you also need a free GitHub account. The instructions for the GitHub account are included in the [Browser Build](../gh-actions/gh-overview.md) instructions.

### Added Requirements for Mac-Xcode Build

If you plan to build using the Mac-Xcode Build instructions, you also need:

1. [Compatible Computer](../build/computer.md#macos)
1. [Xcode](../build/step8.md) (a free Apple application)


## Getting Ready to Build

Go through the Common Requirements to see what you need to actually Loop.

!!! tip "Simulator Option"
    If you want to test the Loop app without attaching CGM or pump hardware, you can run a simulated CGM or simulated pump. You can use actual CGM data using Dexcom Share or Nightscout as a Remote CGM.

    These simulators are part of the Loop app and are available with either build method you choose.
    
    Check out the [Simulator](../version/simulator.md) page.

Once you have chosen your Build Method, go through the pages for that build method several times before beginning, especially if this is new to you.

When you are ready to proceed, work through the tasks on each page. Take your time. You can do one a day, take a week per page or blaze through them quickly.  Just be sure to read carefully and if you are confused - reach out for help: [How to Find Help](../intro/loopdocs-how-to.md#how-to-find-help).

After you build Loop on your phone, keep following along in the docs as you [Set up](../loop-3/loop-3-overview.md) and [Operate](../operation/loop/open-loop.md) your Loop app.

## Next Steps:

### Review the Common Requirements

Before you start either build method, review the Common Requirements. First one is [Compatible iPhone](../build/phone.md). On each page, keep clicking Next (or n) until you've finished with the Intro pages and are ready to Build.

### Browser Build

Click here if you want to build with GitHub Build Actions: [Browser Build](../gh-actions/gh-overview.md)

### Mac-Xcode Build:

Click here if you want to build on a Mac using Xcode: [Mac-Xcode Build](../build/overview.md)
