# Branch and Version FAQs

This page is mostly suited to people who have built the app once already and then are coming back to update. It was originally created when Loop v2.0 was released.

In the course of updating Loop, you may be wondering about the different branches, what the differences are, and such...so let's try to answer some of those questions as best we can.

## What are branches?

There is a lot of discussion about "branches" with Loop but the concept is simple. Basically, they are all slightly different versions of Loop...kind of like different edits of the same book.

To really understand what branches are, we should probably explain a little more about Loop's code and how development works.  You can watch a 30-minute long, classic Katie DiSimone [video explanation about branches](https://www.youtube.com/watch?v=cWqvYs4Azt0&t=4s) created when Loop Version 2.0 was newly released. The information in this video is still generally useful with the last-half focused on automatic-bolus, which is now an established branch offered for download in [Build Step 13](../build/step13.md#download-loop). Loop has moved on to Version 2.2.5 with only one stable branch (master), with dev recommended for developer/testers.

### Loop GitHub Information

Loop developers own an account in GitHub called [LoopKit](https://github.com/LoopKit).  Within that account, the developers have several "repositories" that support Loop in particular. A repository is like a book...let's think of it like a cookbook for now. Within the LoopKit account, there are repositories for Loop itself, LoopDocs, and various other supporting "frameworks" that are helper repositories for Loop to build correctly. For example, Loop's repo has a lot of the info about the app itself; the outward facing things that you interact with. How information is put to you and taken in from you...that's in Loop repository code. But, there's more than just a user interface for Loop. Loop has to do a lot of complex work like Bluetooth communications, algorithm math, pump communications, etc. The Loop app has help from frameworks to do those other parts. CGMBLEkit for some of the transmitter parts of Loop, RileyLink_ios for the pump managers (talking to the pumps and decoding their information), LoopKit for the algorithm about carbs and insulin curves, etc.

When you build Loop, in the background, Loop pulls those other frameworks (7 in total) into the build process using "Carthage".  Carthage is like a personal shopper. You give it a shopping list (the cartfile in Loop code is that shopping list) and it goes and fetches that for you during the build process. Sometimes your computer has an old shopping list...and that can cause build errors. Hence the "carthage update" fix in the Build Errors page...that command updates the shopping list to get the right versions of those frameworks.

![img/loopkit.png](img/loopkit.png){width="650"}
{align="center"}

Anyways...so now you know about the general structure of Loop and LoopKit in Github. Now we can discuss Loop itself a little deeper.

So let's imagine Loop as a cookbook. The developers are the authors/chefs of the recipes (code) in the cookbook. The authors spend countless hours testing new recipes, taste testing, documenting improvements. They send the drafts to the editor, who makes suggestions and eventually the cookbook is finalized. There are no grammar issues, no typos, the photos are beautiful and the recipes are yummy. They publish the book and you see a gorgeous final product on the shelves. That is called a "release" and it is the master branch. This book has been well-tested and is super stable. Every time you cook with those recipes, you know exactly what you're getting and lots of people have had a chance before you to make sure that it all tastes good. Master branch is stable and tested.

But then...the chefs/developers go on a trip. They are inspired by new cuisine and want to add new recipes to the old cookbook. (Things like omnipod support and overrides are new "recipes" that were developed since the last master release, for example.) But, the process for developing a recipe is arduous. Lots of trial and error involved. Lots of tweaking ingredients (code). The editors try out the new recipes and offer feedback (similar to the [Issues List in GitHub](https://github.com/LoopKit/Loop/issues)). While the recipes are being developed, they have a version of the old cookbook that gets marked up...edited in pencil a lot. Scribbles and notes in the side. Revisions happen frequently, because that's what testing new recipes is all about. These marked-up versions of the cookbook are called "dev" branch. Short for "development" branch. Like the name sounds...this is where new developments are happening, new recipes and tweaks.

After much testing and tweaking, eventually the recipes get the flavors right (bugs in code are squashed) and enough people have provided feedback and careful observations of results...that the book goes to the publishing house for the next printing. The cookbook is republished with an updated edition number and new recipes are highlighted. When this happens in Loop, Loop's master branch is updated with the new features coming from dev (aka, "dev branch is merged into master branch"). When that happens, master branch gets another "release" version. For that moment, dev and master are exactly the same. They stay the same until the Loop developers start working on the next batch of improvements, could be the next hour even or days later, but the process begins again. The developers will start editing the code again and dropping those edits in dev branch for further development.

## Loop Releases

The current released version (August 22, 2021) for Loop master is v2.2.5. The dates and contents for Loop releases from v2.0 through v2.2.5 are summarized below in reverse chronological order (so newest release information comes first).

!!! warning "Check Current Release Status"

    Release information is always found on the [GitHub LoopKit/Loop release page](https://github.com/LoopKit/Loop/releases). The information on this LoopDocs page is a summary of that information with a little extra explanation. Be aware that updates to LoopDocs may take some time after a new release comes out.

### Loop v2.2.5

This is an interim release as we prepare for the major changes currently in development. If you are running the previous release, v2.2.4 (master or automatic-bolus branch), or an older version of Loop it is recommended that you update. A summary of modifications with respect to Loop v2.2.4 is listed below.

### New Features:

Automatic Bolus (Experimental)

* Default Dosing Strategy continues to be Temp Basal Only
* Users may now select the Automatic Bolus Dosing Strategy
* Automatic Bolus is marked experimental
    * If you used Loop v2.2.4 automatic-bolus branch, this release will behave the same
    * If you used Loop v2.2.4 master branch, approach this feature with caution; it may require changes to settings
    * Tracking automatic vs manual boluses is not yet implemented in the code and databases

OrangeLink Support Added:

* RileyLink screen: Connection monitoring, battery level alerting, find device, and light/vibration controls for OrangeLink and OrangeLink Pro
* Option to disable MySentry use can trade Medtronic pump battery for longer RileyLink compatible device battery life

Provisioning Profile Expiration Notifications:

* User gets [notified](../operation/features/notifications.md#loop-app-expiration-notification) when Loop app expiration date nears
* Expiration date is [included](../operation/features/notifications.md#loop-app-expiration-notification) in the issue report

Omnipod Features:

* [Pod Settings](../operation/loop-settings/pump-commands.md#omnipod-commands) layout: improved layout and functionality
* Fault Codes: PDM style Ref code displayed for pod faults
* [Confirmation beeps](../operation/loop-settings/pump-commands.md#enable-confirmation-beeps): improved and more uniform implementation
* Pod Suspended: pod beeps once every 5 minutes until delivery is resumed or alarm cleared

### Code Fixes:

Omnipod Code Fixes:

* Make insertion more robust (LoopKit issue #1369)
* Fix “Pod already primed” errors when priming cancelled (rileylink_ios issue #661)
* Prevent 049 pod faults during setup (rileylink_ios issue #627)
* See [RileyLink Pull Request 676](https://github.com/ps2/rileylink_ios/pull/676) for additional details.

Insulin Accounting:

* Reduced occurrences of overlaps in accounting for insulin via reservoir and dose history, which causes temporary overestimation of IOB
* See [Loop Pull Request 344](https://github.com/LoopKit/LoopKit/pull/344) for details

Dexcom Non-US Share:

* Dexcom Share URL for non-US users has been fixed.

For community support, please use one of the [Loop Social Media](../index.md#stay-in-the-loop) help sites.


### Loop v2.2.4

Released October 3, 2020 with "fixes" introduced without renumbering the version number. Last change was on January 19, 2021.

* Revert to previous date pickers (Thanks @novalegra!)
* Pod fault handling improvements (Thanks @itsmojo!)
* Fix issue with pod status screen not allowing new pod pairing or continuing of interrupted pairing.
* October 22, 2020, update travis to make it work with Xcode 12
* January 19, 2021, pin the carthage to 0.36.0.  Users no longer required to install homebrew or carthage (Build Step 7 is now skipped.)

## Older Loop Releases

### Loop v2.2.3

Released September 25, 2020

!!! warning "Warning - Rebuild ASAP for Pods"
    * A bug was introduced in this version, quickly fixed in v2.2.4.
    * If you use pods, please rebuild using v2.2.5.

* Fetch pump and cgm data on manual loop retry (when Loop icon is red or yellow)
* Re-arranged pod status screen to prioritize needed information and actions.
* Pod pairing fixes for more edge cases.
* Translation updates.
* Fix share server integration, pointing to share2.
* Report RSSI and low gain in Read Pod Status command.
* Report failure properly when Play Test Beeps command fails.
* Carthage build fix for Xcode 12.0.1

### Loop v2.2.1

Released August 9, 2020

* Include pending insulin in:
    * forecast uploaded to Nightscout
    * status extension forecast
* Updated translations, fixes for temp override translations, new Arabic translations.
* Omnipod integration fixes:
    * Avoid suspending during deactivation if pod has a fault, is in setup, or already suspended.
    * Show the correct expected address in invalid address error
    * Reuse same address during attempts to pair with same pod
    * Fix for Medtronic only: when a bolus issued via the Loop interface was canceled by issuing a suspend on the pump itself, Loop will incorrectly track the bolus as if the full amount were delivered
    * Updates for omnipod packet parser
    * Suggest moving RileyLink to new area on multiple pairing failures
* Minimed updates:
    * Detect temp basal cancellation performed on pump


### Loop v2.2

Released April 17, 2020

* Updated carb/bolus screens. Thanks @mpangburn!
    * Carbs and boluses are now entered together, which is a more familiar model to many caregivers.
    * Forecast preview while entering bolus allows you to see potential impact of your bolus before delivering.
* Improvements in Watch updates; sleep data being used to update complications when you are awake. Thanks @novalegra!
* Omnipod pairing improvements. Bug fixes, and better error messaging. Thanks @itsmojo!
* Many performance improvements, especially effecting long time Loop users. Delays in rendering graphs during app launch should be fixed.
* New device communication logging facility- Additional logging across pod swaps, and logging of CGM communication.
* Rendering fixes to prevent insulin graph from drawing outside of bounds.
* Bug fix to align use of 10m insulin delay in dose computation and forecast.
* Include current bg in suspend threshold evaluation.

### Loop v2.0

Released December 31, 2019.

!!! danger "For Reference Only"
    Enough time has passed that this version should no longer be on anyone's phones (the one-year expiration time should take care of that).

    There is a lot more detail provided in the Loop v2.0 section because it constituted a significant change to parts of Loop from prior releases. This section and the Omnipod-Testing branch sections are left here for historical interest.

### What was new in Loop v2.0?

This is a highlights reel comparing Loop v2.0 to v1.9.6.

### Uploading of BGs to Nightscout

Loop v2.0 has an option to upload your BG data to Nightscout directly. It is a new slider under the CGM configuration section for Dexcom users. After you add your CGM transmitter ID, go back into the CGM info and you'll see a new slider called "Upload Readings."  Technically, Loop's dev branch had that feature for a hot minute before Loop v2.0 was released...but for almost everyone this will be a brand new feature they haven't had before. This feature can help if/when Dexcom's Share servers ever go through another large outage like we had before. If that happens, you can turn on the "Upload Readings" switch and your CGM data will now be in Nightscout even without Share servers working properly. Good practice would be to temporarily disable your Share bridge in Nightscout while Loop is responsible for CGM uploading so that you don't get duplicate data. You can disable Share bridge by logging into your Heroku account, going to the Settings tab, clicking on "reveal config vars" and then deleting the word "bridge" from the ENABLE line.

### A fix for settings loss

iOS 13 brought about a quirky little bug where you could suddenly lose settings in Loop. But, it wasn't just limited to Loop, sometimes people lost Dexcom app settings too. The issue is most common when the phone goes through a power cycle, but it has happened at other times, too. There's a fix for that new bug in Loop now...so that's a good reason to update. (If you encounter that bug before you have a chance to update your Loop app, simply restart the Loop app and your settings should reappear.)

### Spin for Watch Bolus

To prevent an accidental bolus from your Watch app, don't let your kids hold your watch. Just kidding, we've added an even better option. There is a new "spin" to confirm the bolus after you press the bolus button. You'll see a graphic like below on the watch face. As you spin the digital crown, the two triangles will begin to merge. Once they merge, the bolus is confirmed through a little haptic and a white checkmark will appear on the watch screen.

![img/spin-to-confirm.png](img/spin-to-confirm.png){width="250"}
{align="center"}

### Watch recommended bolus

A common code customization is also now no longer needed. Many people used to edit Loop code to have the Watch app provide 100% of the recommended bolus as the auto-filled quantity in the bolus field (default used to be 75%). Loop now offers the 100% auto-filled recommendation, no code customization needed now.

### Recent carbs list on Watch

You can review the recent carb entries on your Apple Watch now. Simply swipe left to see the blood glucose graph screen on your watch. Scroll down with the digital crown to the "active carbs" row beneath the graph, and tap that row. You can see the list of recent carb entries.

### Fix for Medtronic x15 "bolus may have failed" message

A lot of Medtronic x15 users received "bolus may have failed" messages after each bolus. That issue has been fixed and a patched version of Loop is no longer needed. All good!

### Confirmation beeps expanded

Confirmation beeps have been expanded based on user feedback...we heard parents and school nurses really appreciate hearing a beep for not just boluses, but also for suspend/resume commands and editing basal schedule (so you are sure it saved properly). So, confirmation beeps are now for boluses, suspend/resume, and basal schedule edit saves.

### Read Pod Status added

There's a new command in the RileyLink menu for "Read Pod Status" that is analogous to the existing command for Medtronic users. You can query your Pod for its current status info using that command.

### Bug fixes generally

There are a lot of niggly little bug fixes too which were merged in the last couple weeks. The temp basal timestamp for Medtronic Loop (and for older Omnipod Loops, too) had a bug that when Loop reverted to scheduled basals, the timestamp on the HUD's temp basal icon would switch back to the time the Loop was launched (instead of the time the scheduled basal was started again). There are also some new code improvements for handling uncerain boluses for Pod  Also, there are improvements to handle how Loop marks Pod suspend commands that are initiated by users while an active temp basal is in progress.

### User interface improvements

You'll notice dashed lines in the HUD for the CGM value if the CGM data goes older than 15 min (that way you don't accidentally miss the fact that your CGM has failed). The API Secret is hidden after it is saved in Loop Settings now, and if you accidentally leave a trailing slash on the Nightscout URL...Loop will ignore it.  The bolus progress row is new to master branch now, although many of you have been accustomed to that visual in dev branch for awhile now. The "Scenarios" screen that would sometimes appear when a phone was shaken is also disabled by default now. The Issue Report has more information about your Loop app's build date and version so that you can more easily track its build history.

### Common build error squashed

One common build error was caused if there was a space in the Loop folder name after downloading. This problem has been fixed and you will no longer get build errors if you have a space in your Loop folder name.  Ahhhhh! I love it!!!

### Nightscout profile uploading

Loop will upload your basal schedule, ISFs, carb ratios, and override presets from Loop settings to your Nightscout profile. If you ever lose your phone and need to setup Loop brand new...your settings will be easy to find in Nightscout now.

### New languages

Japanese, Danish, Swedish, Vietnamese, Finnish, Portuguese (Brazilian), Polish, and Romanian languages were added to the regional translations for Loop. There are definitely some missing strings that will still need touchups...we will get those fixed up in Loop v2.1 if you all [help report those when you see them](https://www.facebook.com/groups/TheLoopedGroup/permalink/2454410898108895/). Thanks!!

### Non-linear carb model

All branches (master and dev) now use a "non-linear" carb model, so let's give some info about the change.

Previously, the carb model Loop used had a linear absorption predicted with dynamic carbs adjustments. What this means is that food absorption was modeled as a flat, even effect (like the straight grey graph that you'll see in the [Insulin Counteraction Effects chart](../operation/features/ice.md) after you added a carb entry. But looking at large groups of meals' datasets (and supported by personal, anecdotal experiences), food really has a bit more of a non-linear absorption. Meaning, we usually see more of a food impact up-front than the old carb model in Loop predicted.

What did that mismatch mean for us if the model predicts a linear absorption, but the meal actually behaves differently?

1. Bolusing: You've probably seen smaller upfront boluses for meals than you would have preferred. This is because the insulin was predicted to over-power the linear (slower) carb model soon after a bolus is given.
2. Early low temp basals: You've also probably seen a tendency to have early zero basal or low basals set by Loop for the first 30-60 minutes after a meal bolus if you don't have a significant blood glucose spike immediately after the carb entry. This might have been even more obvious for those of you who are regularly waiting to eat after a bolus, too.

With a non-linear absorption model, the carb absorption will more closely match observed blood glucose impacts we've seen after meals. And when the model is more closely matching actual experience, that means the predicted blood glucose curves will do a better job at providing more upfront bolus and not having the tendency to have overly conservative temp basals soon after a meal.

**What should you expect?** Like the description above, you'll likely see more complete bolus recommendations and less low temping after a bolus. With that in mind, if you've made adjustments to your Loop habits or settings to overcome those issues previously, you may want to undo those habits. Like if you shortened carb absorption times to help get larger boluses upfront, you may want to go back to standard times. Keep an eye on things and you should adjust as needed.

**What if you want to go back to the old model?** You will have to edit a line in LoopKit's LoopKit code [here](https://github.com/LoopKit/LoopKit/blob/dev/LoopKit/CarbKit/CarbStore.swift#L207) to use `.linear` if you wanted to go back to the old carb model. If you want to read more about the model, please check out the [Zulipchat thread here](https://loop.zulipchat.com/#narrow/stream/144111-general/topic/Possible.20Carb.20Model.20Changes). But realize that the code edit for changing models would be easiest done using a [LoopWorkspace](../build/loopworkspace.md) because the edit is in one of the frameworks that Loop uses (rather than Loop code itself), so this is one of those instances where you will have to do some work to learn how to use a LoopWorkspace properly.

### Overrides

Loop v2.0 marks the first time Loop master branch has overrides included. Additionally, this release moves overrides setup from the configurations area of Loop settings to the workout icon in the Loop toolbar. There has also been bug squashing in dev branch for overrides over the recent past, so updating is a good idea even if you already have overrides on your current build. Want to learn more about overrides? Read about them [here](../operation/features/workout.md).

### Retrospective Correction always on

Retrospective correction used to be an optional toggle in the algorithm. It is now on by default all the time. It is an important part of the algorithm (helps Loop look at how good/bad its recent prediction curve has been vs reality), and leaving it on made sense anyways.

### Omnipod support

Yes, most of you are already using Omnipod with your Loop...but this is the first time that Loop master branch supports Omnipod users. Please update if you have been using Omnipod-testing branch especially...it's time to get all the bug fixes that we've done in Loop.

### Dark mode support

iOS 13 brought dark mode for application developers, and Loop's developer was all over that. We now have a wickedly cool dark mode Loop for those who prefer the dark side.

### ISF and correction range guardrails and UI change

Loop v2.0 also brings about the first time master branch has the useful scroll wheel to set values of ISF and correction range. This helps mitigate an old bug where backwards entered correction range values would crash Loop app. Also less prone to fat-finger mistakes on entry.

### Simulator pump and CGM

If you don't have compatible gear yet and just want to test Loop app, the new ability to add a simulated pump and/or CGM is a great new feature.

### New style of Dexcom transmitters supported

Dexcom launched a new style of transmitters this summer. The new transmitters took some work by Loop developer (PETE! YEAH!) to get them working in offline Looping, but the fix was pushed into all branches shortly thereafter in August 2019. If you haven't updated your Loop since August 2019 and use a Dexcom G6, you should update now.

## What happened to Omnipod-testing branch?

Omnipod Loop development testing (not talking about the actual hacking work that preceded that) was done by a smaller group of people privately for months and months before public release of the omnipod-testing branch. This smaller group of people (several dozen) were actively watching their Omnipod Loops and capturing bug reports. There was a lot of work put in by the testers and Pete Schwamb (Loop Developer) to get the code fairly stable and reliable.

When the code got to a stable, reliable state and was ready for a larger audience, omnipod-testing branch was made available as a "public testing" branch. This branch was pretty well-tested prior to public release, but not necessarily going to be perfect for everyone right away. There were expectations that some user-interface requests might be asked for after having a wider audience of users.

Also, omnipod-testing branch was not going to undergo a lot of active revisions to it when it was released. The intent was to keep it as a fairly known, unchanged product for people rather than a constantly changing code set...that way if people noted a bug, it would be a more "known" code base to work to debug.

Omnipod-testing branch has served its purpose as an initial platform to test Pod looping. It has been officially retired now and is no longer needed. Omnipod support has been folded into the normal master and dev branches now.  Thank you, omnipod-testing branch...you served us well. Happy retirement.

## What's going on in the dev branch?

Like we said earlier, master and automatic-bolus branch are stable. You don't really need to watch those for changes.

But, dev branch is a constantly shifting, moving place. If you choose to come into a dev branch build...you need to be aware that is what dev does...moves, shakes, changes, and will update code frequently and unannounced in the traditional sense that most users in Looped group or Instagram would see. Developers are not helped by people being in a dev branch if those users are mistakenly thinking of it as a stable master branch with lots of detailed docs to go with it. People should only use a dev branch build if they EDUCATE themselves on the expectations and how to properly manage dev information and updates. People using dev branch should also have regular access to a computer to be able to rebuild quickly if a new bug/fix is identified.

If you choose to use a dev build, you can stay abreast of developments in a number of ways...but they will all require you to do some legwork and keep yourself informed. This is not a situation where you should expect a fancy Loopdocs page updated regularly with current "dev updates"...that's just not the way dev branch works.

### Watch the Loop Repo and Issues list

First, subscribe to the Loop repo's Issues list by "watching" the [Loop repo](https://github.com/LoopKit/Loop). You can choose to watch the repo so that you get emails when new Issues are reported. This is a good way to find out if there's other people reporting odd behavior that you are wondering about. If you use dev and wonder about something you are seeing in Loop, you can check [Issues list](https://github.com/LoopKit/Loop/issues) to see if others are noticing the same. If so, you can help by capturing information and reporting it. Not super helpful to just say "yeah, me too..." but better if you can attach screenshots, Issue Reports from Loop settings, and a thorough description of the problem you are seeing. Be a part of the solution by thoughtfully providing information to help debug.

![img/watching.png](img/watching.png){width="650"}
{align="center"}

### Subscribe to the Zulipchat channels

Second, use [Zulipchat](https://loop.zulipchat.com) forums for Loop. This forum has several "streams" of conversations depending on interest. I highly recommend following the #github channel if you are wanting to watch for code changes. Code changes are called "commits" in GitHub. The #github channel will have an automated post whenever a new commit is made and it will give a brief line description of the commit.

![img/zulipchat.png](img/zulipchat.png){width="650"}
{align="center"}

You can also go directly to the commit history for each of the branches if you'd like.

[Loop master branch commit history](https://github.com/LoopKit/Loop/commits/master)

[Loop dev branch commit history](https://github.com/LoopKit/Loop/commits/dev)

If you click on the commit, you can see exactly what changes to the code were made. It's an interesting learning experience. In red are the code that is old, in green is the updated code. The line numbers and file names of the edited code are also there to help.

![img/commit.png](img/commit.png){width="550"}
{align="center"}

I don't expect many of you would understand exactly what the edits mean, or how the new code might function...but I bring up the topic of commit history so that you can use that to realize just how often dev is updated. Go ahead and look at the number and frequency of commits in that dev branch...that is why there is no way someone is going to keep a "loopdocs" of dev changes. It's just too much a moving target.

### Keep checking Looped group

Third, keep watching Looped group. Major concerns/issues are brought up there...so no harm in scrolling through and seeing what's going on there.

### Become familiar with your data sources

Another useful thing if you'll be on dev branches undergoing a lot of active change...know how Loop works and where to look for additional information about what you are seeing. For example, if you see an IOB value that looks odd, you should know to look at the insulin deliveries are stored in Health app.

### Generate an Issue Report

Know how to generate an Issue Report when you see a problem so you can provide that if asked. An Issue Report is a log file generated by the Loop app that has a lot of information the developers can parse to figure out what Loop was doing when you were having a problem.

* Loop v2.2.4 and earlier: Loop Settings -> Issue Report
* Loop dev: Loop Settings -> Support -> Issue Report

Do not confuse this with reporting an issue with Loop.  That is done by logging into GitHub and going to the [Issue page](https://github.com/LoopKit/Loop/issues) to report a new issue.  You can read about existing issues without logging in, but to report a new one, you must log in to GitHub.

### Create a Debug Report

This 6-minute long, classic Katie DiSimone video shows how to [capture debugging logs](https://youtu.be/Ac4MguvUO7M). If you are testing a new branch, this is a valuable skill to assist developers in identifying problems. In addition to showing you how to generate and save the debug text information, the video explains a method in which you create a gist of the debug information using your GitHub account and file an official Issue on the Loop GitHub repository. This may be required in some cases.  But start by chatting directly on [zulipchat](https://loop.zulipchat.com) with the developer. What you are experiencing may already be known. If the developers need a new Issue opened, they will say so on zulipchat.

## LoopDashboard.org

You can always check out the [LoopDashboard](https://www.loopdashboard.org) which summarize all the GitHub activities in Loops 7 different repositories for dev and master branches. Here you can always see the latest "news" and  the history of Loop.

On the first page of loopdashboard you can see all the activities in one list, but you can also go to other pages (click on the < or > at bottom of the page) to see more details about commits, issues and pull requests. There are also stats about who is doing the pull requests and commits.

The dashboard is automatically updated every 12 hours.

![img/loopdashboard.png](img/loopdashboard.png){width="550"}
{align="center"}

## What is expected in the future?

The dev branch is where a lot of user interface and setting safety work has been developed with some cross-talk with the open source modifications available from [Tidepool Loop](https://www.tidepool.org/automated-insulin-dosing).

There has been some reorganization of code to make it easier to drop in new pump and CGM modules.  These may not be obvious to the user, but are important for moving forward.

Please continue to [Loop dev Preview](dev-menus.md) for preliminary documentation about Loop dev.
