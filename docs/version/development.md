## Overview

The early history of the *Loop* app was touched on in the introductory [*LoopDocs* Overview: Development History](../intro/overview-intro.md#development-history) section.

The [*Loop* Releases](../version/releases.md) page lists releases since version 2.0 in reverse chronological order.

The next version of the *Loop* app is developed using branch(es), independent of the released *Loop* version, which is found in <span>the `main` branch</span>. <span>The `dev` branch</span> is used by the developers to push out changes for users to test. You should only test a development branch if you are willing to be both an active participant with the developers to monitor announcements and provide feedback and to build frequently to obtain the latest feature or bug-fix that is being tested. If you are willing to help out - this is the way the next release of *Loop* is improved.

If you choose to use `dev`, you accept that this code is not released.

Please read this entire page before using any version of *Loop* other than the released code.

## Updates in `dev`

This section provides an overview of changes to `dev` compared to `Loop 3.8.x`. 
  
Please check the [development channel in zulipchat](https://loop.zulipchat.com/#narrow/channel/144182-development) for notifications when an update to the `dev` branch is expected so you will be prepared. Do this **before** you install a `dev` build from TestFlight.

With the `dev` branch, version 3.9.3, there are now differences between `dev` and `main`. In addition, there are some feature branches.

| <div style="width:140px"> branch | version # | comments |
|:--|:--|:--|
| main | 3.8.2 | release |
| dev | 3.9.3 | Adds Live Activity, Browser Build improvement, translation and other updates <br>See [v3.9.3 `dev`](#v393-dev) |
| [feat/pod-keep-alive](#feature-branch-pod-keep-alive-feature)<br>- SHA `c84fc3a` | 3.9.3 | - identical to dev v3.9.3 except uses the OmniBLE pod-keep-alive branch to support users of iPhone 16 phones with InPlay BLE (-Atlas) DASH pods<br>  - SHA for OmniBLE is `a9b63fa` |
| [feat/dev-dana-medtrum](#feature-branch-medtrum-and-dana-support) <br>- SHA `de1109f`| 3.9.3 | - identical to dev v3.9.3, with addition of experimental support for Dana and Medtrum pumps<br>- this branch is ready for expert testers to evaluate and report back<br>  - SHA for DanaKit is `08b6623c`<br>  - SHA for MedtrumKit is `9958befc` |
| release/3.8.1 | 3.8.1 | - copy of the main release at version 3.8.1 that included Dana support<br>- please build the feat/dev-dana-medtrum branch instead and test it<br>- this branch was a stop-gap measure to support people already using Dana with v3.8.1 who understood how to manage the issues with that version; it will be deleted soon<br>  - SHA for DanaKit is `3e606b8` |

!!! question "What is SHA?"
    SHA-1 means Secure Hash Algorithm 1. This is used to generate an alphanumeric code to identify which version of a repository is used. 

    Each time you save a change to your&nbsp;<span translate="no">GitHub repository</span>, a unique SHA-1 is created. That identifier is used to tell *GitHub* a specific change that you want applied or identifies a specific version for that <code>repository</code>. These work for any compatible <code>fork</code> from the original&nbsp;<span translate="no">GitHub repository</span>.

    The SHA-1 20-character value is abbreviated as SHA and typically only the first 7 or 8 characters are presented to identify the commit for a particular repository.

### Version Number Plan

Please see [`Loop` Version Numbering](releases.md#loop-version-numbering) for the current method for version numbering for the `main` and `dev` branches.

The idea of having a feature branch is not new for the *Loop* app but hasn't been used for a few years. At this point, we have two feature branches.

Moving forward, the version number in the feature branch will match the `dev` branch version number. 

* In other words, a diff between `dev` and the feature branch is just the updates added to support the feature compared to that version of `dev`
* As appropriate, `dev` will be merged into the feature branch and at that time, the version number for the feature branch will also be bumped
* Updates to the feature branch to support the feature will not be updated with a new version number associated with the features
    * When updates for the feature are added, the SHA for that submodule will be reported in the table above and can be found by examining the LoopWorkspace repository for that feature branch

### v3.9.3 `dev`

The details of the additions to the `dev` branch for v3.9.3 are found in LoopWorkspace Pull Request 358:

*   [Update dev to 3.9.3](https://github.com/LoopKit/LoopWorkspace/pull/358)

!!! important "New Minimum Requirements"
    **The minimum iOS required to build this version is iOS 16; but not all features are supported by iOS 16 - specifically the Live Activity / Dynamic Island / CarPlay features**

    * Correction, you can still build onto an iOS 15 phone with this version, but because the use of String Catalogs for languages don't work well for iOS 15 and Live Activity is not supported, expect the next dev version will force a minimum iOS 16 for building

    **Live Activity, Dynamic Island and CarPlay**

    * The dynamic island is only available for iPhone versions 14 pro and newer; but Live Activity on the Lock Screen is supported for older phones running iOS 16 or newer
    * iOS 18 and watchOS 10 or newer are required for Live Activity to appear in the Smart Stack on the Apple Watch
    * iOS 26 or newer is required to have Live Activity appear in the CarPlay view


#### Live Activities

This update adds Live Activity to Loop with [Loop PR 2919](https://github.com/LoopKit/Loop/pull/2191#issuecomment-3565473537). Many people have been using this as a customization. If you used the customization - you need to stop selecting `live_activity` as a customization or your build will fail.

* The configuration for the Live Activity widget on the lock screen is found under Loop, Settings, Notifications, Live Activity
* You must also enable Live Activity under iPhone settings, Loop, tap on Live Activites and enable Allow Live Activites and More Frequent Update

#### Mac-Xcode Builders

One change with this PR is to modify the Build Order selected in Xcode from the deprecated `Manual Order` to the preferred `Dependency Order`.

* If you start with a fresh download - this will not affect you
* If you update an existing clone on your computer with the `git pull --recurse` command, you will need to perform a `Product: Clean Build Folder` in Xcode, close the workspace in Xcode and reopen it
    * If there are still build errors, then quit out of Xcode, issue the following command and try again
    * `rm -rf ~/Library/Developer/Xcode/DerivedData`

### Feature Branch: Pod Keep Alive Feature

For more information about using the `feat/pod-keep-alive` branch with an iPhone 16 and InPlay BLE DASH pods, please refer to the README file for the OmniBLE `pod-keep-alive` branch:

* [Workaround for InPlay Pods](https://github.com/LoopKit/OmniBLE/tree/8c4740468949cf6ca787e232f885a535b2bb3e8f?tab=readme-ov-file#omnible)


### Feature Branch: Medtrum and Dana Support

**Updates are believed to have fixed the active insulin issues reported for both Dana and Medtrum, but this should be tested by experts to confirm pumps are working well with Loop.**

!!! important "Experts Only"
    Please only use the `feat/dev-dana-medtrum` branch if you are prepared to follow along in zulipchat and are willing to test an experimental branch to help test and resolve issues.

    * Please ensure you have the latest version of this branch:
        * `feat/dev-dana-medtrum`
        * SHA `de1109f`

## Older updates

### Updates from v3.6 to v3.8

The updates developed in the `dev` branch before the release of v3.8.0, are provided in reverse chronological order.

#### v3.7.7

The changes are to maintenance scripts and to translations with no change to the function of the code:

* There are some updates to translated strings that people who use Loop in other languages may notice
    * The DanaKit pump translations now work
    * Parts of the Favorite Foods sections are now translated
    * Many common keys used in more than one submodule are linked so they only need to be translated one time to appear in the app
* With v3.6.2, the method to Add Identifiers when using Browser Build for the *Loop* app changed. 
    * The new method requires the time-sensitive capability be added manually
    * This change was captured in LoopDocs but not in testflight.md
    * The instructions found in testflight.md were updated
* For developers who might want to know, this update included
    * conversion to use String Catalogs for localization in the submodules with associated tweaks to Xcode configuration
    * updates to the CircleCI configurations

#### v3.7.6

* Updated some localization (strings translated to different languages)
    * Added scripts to make localization more streamlined
* Cleaned up some code
    * Fixed a bolus problem with iOS 26
    * Discarded some unneeded files
    * Updated to Xcode 16.4 for browser build and CircleCI quality testing

#### v3.7.5

* Added support for Dana-i and DanaRS-v3 pump models

#### v3.7.0 through v3.7.4

* `dev` v3.7.x was same as [`main` v3.6.x](releases.md#loop-v364).

### Updates from v3.4 to v3.6

All updates are reported in [`Loop 3.6.0`](releases.md#loop-v360){: target="_blank" }

Check [Version History](releases.md#loop-3-version-history) for minor updates found in 3.6.x.

### Updates from v3.2 to v3.4

Features new with v3.4, originally in the Updates in `dev` section before the release, have been inserted into the appropriate part of the *LoopDocs* website (indicated by the up-right arrow after the link). The links below are left to assist people in finding the features.

* [Support for Libre Sensors](../loop-3/add-cgm.md#libre){: target="_blank" }
* [Pump or CGM Simulator on Phone](simulator.md#pump-or-cgm-simulator-on-phone){: target="_blank" }
* [Algorithm Experiments](../loop-3/settings.md#algorithm-experiments){: target="_blank" }
    * [<span translate="no">Glucose Based Partial Application</span> Factor](../loop-3/features.md#glucose-based-partial-application-gbpa){: target="_blank" }
    * [<span translate="no">Integral Retrospective Correction</span>](../loop-3/features.md#integral-retrospective-correction-irc){: target="_blank" }
* [Favorite Foods](../loop-3/settings.md#favorite-foods){: target="_blank" }
* [<span translate="no">TestFlight Expiration Warning</span>](../operation/features/notifications.md#loop-app-expiration-notification){: target="_blank" }

- - -

## What are Git Branches?

There is a lot of discussion about *branches* with *Loop* but the concept is simple. Basically, they are all slightly different versions of *Loop*...kind of like different edits of the same book.

To really understand what branches are, we should probably explain a little more about the software and how development works.  You can watch a 30-minute long, classic Katie DiSimone [video explanation about branches](https://www.youtube.com/watch?v=cWqvYs4Azt0&t=4s) created when *Loop* Version 2.0 was newly released. Keep in mind while watching the video:


Details that are different:

* The way the code is organized has changed: see [LoopWorkspace](loopworkspace.md){: target="_blank" }
* The default branch name used to be `master` - but is now `main`
* `carthage` is no longer used to determine which submodules (frameworks) are pulled in to build Loop (see [LoopWorkspace](#loopworkspace))

The information in this video is still generally useful with the last half focused on automatic-bolus - the automatic-bolus dosing strategy has now been incorporated into <span>*Loop* `main` branch</span>. *Loop* has moved on to using only one stable branch (`main`), with `dev` suggested for developers/testers.

### `Loop` GitHub Information

*Loop* developers own an account in *GitHub* called [LoopKit](https://github.com/LoopKit).  Within that account, the developers have several <code>repositories</code> that support *Loop* in particular. A repository&#8203; is like a book...let's think of it like a cookbook for now. Within the `LoopKit` account, there are `repositories` for Loop&#8203; itself, *LoopDocs*, and various other supporting "frameworks" that are <span>helper &#8203;repositories&#8203; for *Loop*</span> to build correctly. For example, Loop&#39;s &#8203;repository&#8203; has a lot of info about the app itself; the outward-facing things that you interact with. How information is put to you and taken in from you...that's in *Loop* <code>repository</code> code. But, there's more than just a user interface for Loop. *Loop* has to do a lot of complex work like Bluetooth communications, algorithm math, pump communications, etc. The *Loop* app has help from frameworks to do those other parts. `CGMBLEkit`&nbsp; for some of the transmitter parts of *Loop*, `RileyLink_ios` for the pump managers (talking to the pumps and decoding their information), `LoopKit` for the algorithm about carbs and insulin curves, etc.

When you build *Loop*, you actually start with LoopWorkspace which points to all the other repositories needed for a complete *Loop* app.

> Note - this graphic is outdated - you download the *LoopWorkspace* repository and use the workspace to get the right version of the *Loop* repository and the other necessary code.


![img/loopkit.png](img/loopkit.png){width="650"}
{align="center"}

Anyways...so now you know about the general structure of *Loop* and *LoopKit* in *GitHub*. Now we can discuss *Loop* itself a little deeper.

So let's imagine *Loop* as a cookbook. The developers are the authors/chefs of the recipes (code) in the cookbook. The authors spend countless hours testing new recipes, taste testing, and documenting improvements. They send the drafts to the editor, who makes suggestions and eventually, the cookbook is finalized. There are no grammar issues, and no typos, the photos are beautiful and the recipes are yummy. They publish the book and you see a gorgeous final product on the shelves. That is called a release&#8203, and it is the `main` branch. This book has been well-tested and is super stable. Every time you cook with those recipes, you know exactly what you're getting and lots of people have had a chance before you to make sure that it all tastes good. The `main` branch is stable and tested.

But then...the chefs/developers go on a trip. They are inspired by new cuisine and want to add new recipes to the old cookbook. (Things like Omnipod&#8203; support and the overrides are new "recipes" that were developed since the last `main` release, for example.) But, the process of developing a recipe is arduous. There was a lot of trial and error involved. Lots of tweaking ingredients (code). The editors try out the new recipes and offer feedback (similar to the [Issues List on GitHub](https://github.com/LoopKit/Loop/issues)). While the recipes are being developed, they have a version of the old cookbook that gets marked up...edited in pencil a lot. Scribbles and notes in the side. Revisions happen frequently because that's what testing new recipes is all about. These marked-up versions of the cookbook are called the `dev` branch. Short for "development" branch. Like the name sounds...this is where new developments are happening, new recipes, and tweaks.

After much testing and tweaking, eventually, the recipes get the flavors right (bugs in code are squashed) and enough people have provided feedback and careful observations of results...that the book goes to the publishing house for the next printing. The cookbook is republished with an updated edition number and new recipes are highlighted. When this happens in *Loop*,  <span>Loop&#39;s `main` branch</span> is updated with the new features coming from `dev` (aka, the `dev` branch is merged into the `main` branch). When that happens, the `main` branch gets another `release` version. At this point, `dev` and `main` are identical. They remain so until the development team for *Loop*&nbsp; starts working on the next batch of improvements, which could be in the next hour or even days later, but then the cycle starts again.  The developers will start editing the code again and dropping those edits in the `dev` branch for further development.

## What's going on in the `dev` branch?

The `dev` branch is where the next version of *Loop* is being developed and tested.

If you choose to build *Loop* using a `dev` branch, you need to be aware that the `dev` branch may update code frequently and unannounced in the traditional sense that most users in the  *Looped* group or *Instagram* would see. Developers are not helped by people being in a `dev` branch if those users mistakenly think of it as a stable `main` branch with lots of detailed docs to go with it. People should only use a `dev` branch build if they EDUCATE themselves on the expectations and how to properly manage `dev` information and updates. People using the `dev` branch should also have regular access to a computer to be able to rebuild quickly if a new bug/fix is identified.

If you choose to use a `dev` build, you can stay abreast of developments in a number of ways...but they will all require you to do some legwork and keep yourself informed. This is not a situation where you should expect a fancy *Loopdocs* page updated regularly with current "`dev` updates"...that's just not the way the `dev` branch works (at least normally).

### Subscribe to the Zulipchat channels

Use [Zulipchat](https://loop.zulipchat.com) forums for *Loop*.  
This forum has several streams of conversations (`streams`) depending on interest. I highly recommend following all the streams so you do not miss conversations.  You can select by stream and by topic within a stream to focus on a given conversation.  

!!! tip "Zulip Chat Streams"
    - If you are using the **dev** branch, you **must** be in the **[#development](https://loop.zulipchat.com/#narrow/stream/144182-development)** stream.  
    - If you want to know when **LoopDocs** gets updated, follow the **[#documentation](https://loop.zulipchat.com/#narrow/stream/270362-documentation)** stream.  
    - **Code changes** are called commits in GitHub.  
      The **[#github](https://loop.zulipchat.com/#narrow/stream/144191-github)** stream will have an automated post whenever a new commit is made and it will give a brief line description of the commit.

![img/zulipchat.png](img/zulipchat.png){width="650"}
{align="center"}

You can also go directly to the git commit history for each of the branches if you'd like.

- [`Loop` **`main`** branch: git commit history](https://github.com/LoopKit/Loop/commits/main)
- [`Loop` **`dev`** branch: git commit history](https://github.com/LoopKit/Loop/commits/dev)

If you click on the commit, you can see exactly what changes to the code were made. It's an interesting learning experience. In red is the old code, and in green is the updated code. The line numbers and file names of the edited code are also there to help.

![img/commit.png](img/commit.png){width="550"}
{align="center"}

I don't expect many of you would understand exactly what the edits mean, or how the new code might function. However, I bring up the topic of git commit history so that you can use that to realize just how often the `dev` branch is updated. Go ahead and look at the number and frequency of commits in that branch.  That's why no one would want to maintain a documentation list of the changes in the `dev` branch. It's just too much of a moving target.

### Watch the `Loop Repository` and `Issues List`

Open the [`Loop repository`](https://github.com/LoopKit/Loop) and subscribe to the `Issues`. 

You can choose to watch the `repository` so that you get emails when new `Issues` are reported. This is a good way to find out if other people are reporting odd behavior that you are wondering about. If you use `dev` and wonder about something you are seeing in *Loop*, you can check [`Issues` list](https://github.com/LoopKit/Loop/issues) to see if others are noticing the same. If so, you can help by capturing information and reporting it. Not super helpful to just say "Yeah, me too..." but better if you can attach screenshots, `Issue Reports` from *Loop* settings, and a thorough description of the problem you are seeing. Be a part of the solution by thoughtfully providing information to help debug.

![img/watching.png](img/watching.png){width="650"}
{align="center"}

### Become familiar with your data sources

Another useful thing if you'll be on `dev` branches undergoing a lot of active change...know how *Loop* works and where to look for additional information about what you are seeing. For example, if you see an IOB value that looks odd, you should know to look at the insulin deliveries stored in the *Health* app.

### Generate an Issue Report

Know how to generate an `Issue Report` when you see a problem so you can provide that if asked. An `Issue Report` is a log file generated by the *Loop* app that has a lot of information the developers can parse to figure out what *Loop* was doing when you were having a problem.

* `Loop Settings` and then scroll almost to the bottom and select `Issue Report`

Do not confuse this with reporting an issue with *Loop*.  That is done by logging into *GitHub* and going to the [`Issue` page](https://github.com/LoopKit/Loop/issues) to report a new issue.  You can read about existing issues without logging in, but to report a new one, you must log in to *GitHub*.

### Create a Debug Report

This 6-minute long, classic Katie DiSimone video shows how to [capture debugging logs](https://youtu.be/Ac4MguvUO7M). If you are testing a new branch, this is a valuable skill to assist developers in identifying problems. In addition to showing you how to generate and save the debug text information, the video explains how to create a <code>gist</code> with the debug information using your *GitHub* account and file an official Issue on the *Loop* *GitHub* <code>repository</code>. This may be required in some cases.  But start by chatting directly on [Zulipchat](https://loop.zulipchat.com) with the developer. What you are experiencing may already be known. If the developers need you to open a new `Issue`, they will say so on *Zulipchat*.


## `Repositories` and Code

If you're a developer looking for direct links to the **code and documentation** in *GitHub*:

* [`LoopWorkspace`](https://github.com/LoopKit/LoopWorkspace)
* [`LoopDocs`](https://github.com/LoopKit/Loopdocs)

For more information on **how to contribute code to the *Loop* project**, please review:

  * [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
  * the [LICENSE](https://github.com/LoopKit/Loop/blob/main/LICENSE.md)
  * the  [CODE_OF_CONDUCT](https://github.com/LoopKit/Loop/blob/main/CODE_OF_CONDUCT.md)

If you want to contribute **code improvements**, please join [*Loop Zulipchat*](https://loop.zulipchat.com) and be sure to subscribe to all the channels. Meet the developers and testers who make this app, and learn about what is coming next.
