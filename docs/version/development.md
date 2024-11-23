## Overview

The early history of the *Loop* app was touched on in the introductory [*LoopDocs* Overview: Development History](../intro/overview-intro.md#development-history) section.

The [*Loop* Releases](../version/releases.md) page lists releases since version 2.0 in reverse chronological order.

The next version of the *Loop* app is developed using branch(es), independent of the released *Loop* version, which is found in <span>the `main` branch</span>. <span>The `dev` branch</span> is used by the developers to push out changes for users to test. You should only test a development branch if you are willing to be both an active participant with the developers to monitor announcements and provide feedback and to build frequently to obtain the latest feature or bug-fix that is being tested. If you are willing to help out - this is the way the next release of *Loop* is improved.

If you choose to use `dev`, you accept that this code is not released.

Please read this entire page before using any version of *Loop* other than the released code.

## Updates in `dev`

This section is an early look at major features added to dev since Loop 3.4 was released.

Right now it is empty.

## Updates from 3.2 to 3.4

Most features, originally in the Updates in `dev` section before the release of version 3.4, have been inserted into the appropriate part of the *LoopDocs* website (indicated by the up-right arrow after the link). A few items are still in this section.

* [Support for Libre Sensors](../loop-3/add-cgm.md#libre){: target="_blank" }
* [Pump or CGM Simulator on Phone](simulator.md#pump-or-cgm-simulator-on-phone){: target="_blank" }
* [Algorithm Experiments](../loop-3/settings.md#algorithm-experiments){: target="_blank" }
    * [<span translate="no">Glucose Based Partial Application</span> Factor](../loop-3/features.md#glucose-based-partial-application-gbpa){: target="_blank" }
    * [<span translate="no">Integral Retrospective Correction</span>](../loop-3/features.md#integral-retrospective-correction-irc){: target="_blank" }
* [Favorite Foods](../loop-3/settings.md#favorite-foods){: target="_blank" }
* [<span translate="no">TestFlight Expiration Warning</span>](../operation/features/notifications.md#loop-app-expiration-notification){: target="_blank" }
* [<span translate="no">GitHub Browser Build</span> Updates](#github-browser-build-updates)
* [Miscellaneous Code Fixes](#miscellaneous-code-fixes)

### <span translate="no">GitHub Browser Build</span>&nbsp; Updates

The `dev` branch has several updates merged that make it easier to find errors in configuration and that make the &nbsp;<span translate="no">GitHub Browser Build</span>&nbsp; automatic.

Note that the automatic build feature is opt-out. In other words, unless you take specific steps, the &nbsp;<span translate="no">GitHub Browser Build</span>&nbsp; for&nbsp;_<span translate="no">Loop</span>_&nbsp;will:

* Automatically build a new version once a month, with automatic update included
* Automatically update your fork of LoopWorkspace once a week if updates are available

It is suggested that all users of the released code (main branch), maintain this automatic schedule so they are never without a valid and up-to-date&nbsp;_<span translate="no">Loop</span>_&nbsp;in their  *TestFlight*  app.

In addition to the easier to read error messages found with these updates, these additional simplifications include:

* Actions are broken into logical components, each of which provides an easy to understand error message if it fails which includes a suggested fix
* A new builder no longer needs to create the &nbsp;<span translate="no">Match-Secrets repository</span>
    * If it does not exist, one is created for you
    * Only the App Group ID must be added to the Identifiers; all other App services are    automatically added
* For new builders and current 3.2.3 users updating to the next release
    * The branches with `alive` in the name required to enable automatic update and building are created automatically
    * Make sure your GitHub repository is in sync with the LoopKit/LoopWorkspace repository

These sections are still useful for version 3.5.0 `dev` users:

* [Browser Build for dev](../browser/build-dev-browser.md): How to use &nbsp;<span translate="no">GitHub Browser Build</span>&nbsp; for `dev` branch
* [Browser Build: One-Time Changes](../browser/build-dev-browser.md#one-time-changes): New steps and dates at which the new steps were added

### Miscellaneous Code Fixes

#### G7 Sensors: Duplicate CGM Values

Fixed with [PR 16: Fix parsing of age field of message](https://github.com/LoopKit/G7SensorKit/pull/16){: target="_blank" }

* Most sensors report the time with very little offset between time of arrival and time of sensing
* If the time discrepancy is large, the error (using one byte instead of two for age of the reading) could cause CGM values to appear as duplicate readings in Loop

#### Remote Services Update

The code that feeds Loop data to remote services like Tidepool and Nightscout have been improved to be more robust.

## What are Git Branches?

There is a lot of discussion about *branches* with *Loop* but the concept is simple. Basically, they are all slightly different versions of *Loop*...kind of like different edits of the same book.

To really understand what branches are, we should probably explain a little more about the software and how development works.  You can watch a 30-minute long, classic Katie DiSimone [video explanation about branches](https://www.youtube.com/watch?v=cWqvYs4Azt0&t=4s){: target="_blank" } created when *Loop* Version 2.0 was newly released. Keep in mind while watching the video:


Details that are different:

* The way the code is organized has changed: see [LoopWorkspace](#loopworkspace)
* The default branch name used to be `master` - but is now `main`
* `carthage` is no longer used to determine which submodules (frameworks) are pulled in to build Loop (see [LoopWorkspace](#loopworkspace))

The information in this video is still generally useful with the last half focused on automatic-bolus - the automatic-bolus dosing strategy has now been incorporated into <span>*Loop* `main` branch</span>. *Loop* has moved on to using only one stable branch (`main`), with `dev` suggested for developers/testers.

### `Loop` GitHub Information

*Loop* developers own an account in *GitHub* called [LoopKit](https://github.com/LoopKit){: target="_blank" }.  Within that account, the developers have several <code>repositories</code> that support *Loop* in particular. A repository&#8203; is like a book...let's think of it like a cookbook for now. Within the `LoopKit` account, there are `repositories` for Loop&#8203; itself, *LoopDocs*, and various other supporting "frameworks" that are <span>helper &#8203;repositories&#8203; for *Loop*</span> to build correctly. For example, Loop&#39;s &#8203;repository&#8203; has a lot of info about the app itself; the outward-facing things that you interact with. How information is put to you and taken in from you...that's in *Loop* <code>repository</code> code. But, there's more than just a user interface for Loop. *Loop* has to do a lot of complex work like Bluetooth communications, algorithm math, pump communications, etc. The *Loop* app has help from frameworks to do those other parts. `CGMBLEkit`&nbsp; for some of the transmitter parts of *Loop*, `RileyLink_ios` for the pump managers (talking to the pumps and decoding their information), `LoopKit` for the algorithm about carbs and insulin curves, etc.

When you build *Loop*, in the background, *Loop* pulls those other frameworks (7 in total) into the build process using `Carthage`.  `Carthage`&nbsp;  is like a personal shopper. You give it a shopping list (the cart file in *Loop* code is that shopping list) and it goes and fetches that for you during the build process. Sometimes your computer has an old shopping list...and that can cause build errors. Hence the `carthage update` fix in the Build Errors page...that command updates the shopping list to get the right versions of those frameworks.

![img/loopkit.png](img/loopkit.png){width="650"}
{align="center"}

Anyways...so now you know about the general structure of *Loop* and *LoopKit* in *GitHub*. Now we can discuss *Loop* itself a little deeper.

So let's imagine *Loop* as a cookbook. The developers are the authors/chefs of the recipes (code) in the cookbook. The authors spend countless hours testing new recipes, taste testing, and documenting improvements. They send the drafts to the editor, who makes suggestions and eventually, the cookbook is finalized. There are no grammar issues, and no typos, the photos are beautiful and the recipes are yummy. They publish the book and you see a gorgeous final product on the shelves. That is called a release&#8203, and it is the `main` branch. This book has been well-tested and is super stable. Every time you cook with those recipes, you know exactly what you're getting and lots of people have had a chance before you to make sure that it all tastes good. The `main` branch is stable and tested.

But then...the chefs/developers go on a trip. They are inspired by new cuisine and want to add new recipes to the old cookbook. (Things like Omnipod&#8203; support and the overrides are new "recipes" that were developed since the last `main` release, for example.) But, the process of developing a recipe is arduous. There was a lot of trial and error involved. Lots of tweaking ingredients (code). The editors try out the new recipes and offer feedback (similar to the [Issues List on GitHub](https://github.com/LoopKit/Loop/issues){: target="_blank" }). While the recipes are being developed, they have a version of the old cookbook that gets marked up...edited in pencil a lot. Scribbles and notes in the side. Revisions happen frequently because that's what testing new recipes is all about. These marked-up versions of the cookbook are called the `dev` branch. Short for "development" branch. Like the name sounds...this is where new developments are happening, new recipes, and tweaks.

After much testing and tweaking, eventually, the recipes get the flavors right (bugs in code are squashed) and enough people have provided feedback and careful observations of results...that the book goes to the publishing house for the next printing. The cookbook is republished with an updated edition number and new recipes are highlighted. When this happens in *Loop*,  <span>Loop&#39;s `main` branch</span> is updated with the new features coming from `dev` (aka, the `dev` branch is merged into the `main` branch). When that happens, the `main` branch gets another `release` version. At this point, `dev` and `main` are identical. They remain so until the development team for *Loop*&nbsp; starts working on the next batch of improvements, which could be in the next hour or even days later, but then the cycle starts again.  The developers will start editing the code again and dropping those edits in the `dev` branch for further development.

## What's going on in the `dev` branch?

The `dev` branch, currently v3.5.0, is where the next version of *Loop* is being developed and tested.

If you choose to build *Loop* using a `dev` branch, you need to be aware that the `dev` branch may update code frequently and unannounced in the traditional sense that most users in the  *Looped* group or *Instagram* would see. Developers are not helped by people being in a `dev` branch if those users mistakenly think of it as a stable `main` branch with lots of detailed docs to go with it. People should only use a `dev` branch build if they EDUCATE themselves on the expectations and how to properly manage `dev` information and updates. People using the `dev` branch should also have regular access to a computer to be able to rebuild quickly if a new bug/fix is identified.

If you choose to use a `dev` build, you can stay abreast of developments in a number of ways...but they will all require you to do some legwork and keep yourself informed. This is not a situation where you should expect a fancy *Loopdocs* page updated regularly with current "`dev` updates"...that's just not the way the `dev` branch works (at least normally).

### Subscribe to the Zulipchat channels

Use [Zulipchat](https://loop.zulipchat.com){: target="_blank" } forums for *Loop*.  
This forum has several streams of conversations (`streams`) depending on interest. I highly recommend following all the streams so you do not miss conversations.  You can select by stream and by topic within a stream to focus on a given conversation.  

!!! tip "Zulip Chat Streams"
    - If you are using the **dev** branch, you **must** be in the **[#development](https://loop.zulipchat.com/#narrow/stream/144182-development){: target="_blank" }** stream.  
    - If you want to know when **LoopDocs** gets updated, follow the **[#documentation](https://loop.zulipchat.com/#narrow/stream/270362-documentation){: target="_blank" }** stream.  
    - **Code changes** are called commits in GitHub.  
      The **[#github](https://loop.zulipchat.com/#narrow/stream/144191-github){: target="_blank" }** stream will have an automated post whenever a new commit is made and it will give a brief line description of the commit.

![img/zulipchat.png](img/zulipchat.png){width="650"}
{align="center"}

You can also go directly to the git commit history for each of the branches if you'd like.

- [`Loop` **`main`** branch: git commit history](https://github.com/LoopKit/Loop/commits/main){: target="_blank" }
- [`Loop` **`dev`** branch: git commit history](https://github.com/LoopKit/Loop/commits/dev){: target="_blank" }

If you click on the commit, you can see exactly what changes to the code were made. It's an interesting learning experience. In red is the old code, and in green is the updated code. The line numbers and file names of the edited code are also there to help.

![img/commit.png](img/commit.png){width="550"}
{align="center"}

I don't expect many of you would understand exactly what the edits mean, or how the new code might function. However, I bring up the topic of git commit history so that you can use that to realize just how often the `dev` branch is updated. Go ahead and look at the number and frequency of commits in that branch.  That's why no one would want to maintain a documentation list of the changes in the `dev` branch. It's just too much of a moving target.

### Watch the `Loop Repository` and `Issues List`

Open the [`Loop repository`](https://github.com/LoopKit/Loop){: target="_blank" } and subscribe to the `Issues`. 

You can choose to watch the `repository` so that you get emails when new `Issues` are reported. This is a good way to find out if other people are reporting odd behavior that you are wondering about. If you use `dev` and wonder about something you are seeing in *Loop*, you can check [`Issues` list](https://github.com/LoopKit/Loop/issues){: target="_blank" } to see if others are noticing the same. If so, you can help by capturing information and reporting it. Not super helpful to just say "Yeah, me too..." but better if you can attach screenshots, `Issue Reports` from *Loop* settings, and a thorough description of the problem you are seeing. Be a part of the solution by thoughtfully providing information to help debug.

![img/watching.png](img/watching.png){width="650"}
{align="center"}

### Keep checking `Looped` group

Keep watching [`The Looped Group`](https://www.facebook.com/groups/TheLoopedGroup){: target="_blank" } on  *Facebook*. Major concerns/issues are brought up there...so it doesn't hurt to scroll through and see what's going on there.

### Become familiar with your data sources

Another useful thing if you'll be on `dev` branches undergoing a lot of active change...know how *Loop* works and where to look for additional information about what you are seeing. For example, if you see an IOB value that looks odd, you should know to look at the insulin deliveries stored in the *Health* app.

### Generate an Issue Report

Know how to generate an `Issue Report` when you see a problem so you can provide that if asked. An `Issue Report` is a log file generated by the *Loop* app that has a lot of information the developers can parse to figure out what *Loop* was doing when you were having a problem.

* *<span translate="no">Loop v2.2.9</span>*&nbsp; and earlier:` Loop Settings -> Issue Report`
* *<span translate="no">Loop 3</span>*&nbsp; and later: `Loop Settings -> Support -> Issue Report`

Do not confuse this with reporting an issue with *Loop*.  That is done by logging into *GitHub* and going to the [`Issue` page](https://github.com/LoopKit/Loop/issues){: target="_blank" } to report a new issue.  You can read about existing issues without logging in, but to report a new one, you must log in to *GitHub*.

### Create a Debug Report

This 6-minute long, classic Katie DiSimone video shows how to [capture debugging logs](https://youtu.be/Ac4MguvUO7M){: target="_blank" }. If you are testing a new branch, this is a valuable skill to assist developers in identifying problems. In addition to showing you how to generate and save the debug text information, the video explains how to create a <code>gist</code> with the debug information using your *GitHub* account and file an official Issue on the *Loop* *GitHub* <code>repository</code>. This may be required in some cases.  But start by chatting directly on [Zulipchat](https://loop.zulipchat.com){: target="_blank" } with the developer. What you are experiencing may already be known. If the developers need you to open a new `Issue`, they will say so on *Zulipchat*.


## `Repositories` and Code

If you're a developer looking for direct links to the **code and documentation** in *GitHub*:

* [`Loop`](https://github.com/LoopKit/Loop){: target="_blank" }
* [`LoopDocs`](https://github.com/LoopKit/Loopdocs){: target="_blank" }

For more information on **how to contribute code to the *Loop* project**, please review:

  * [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/){: target="_blank" }
  * the [LICENSE](https://github.com/LoopKit/Loop/blob/main/LICENSE.md){: target="_blank" }
  * the  [CODE_OF_CONDUCT](https://github.com/LoopKit/Loop/blob/main/CODE_OF_CONDUCT.md){: target="_blank" }

If you want to contribute **code improvements**, please join [*Loop Zulipchat*](https://loop.zulipchat.com){: target="_blank" } and be sure to subscribe to all the channels. Meet the developers and testers who make this app, and learn about what is coming next.
