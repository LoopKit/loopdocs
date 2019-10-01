# Branch FAQs

This page is mostly suited to people who have built the app once already and then are coming back to update. In the course of updating, you may be wondering about the different branches, what the differences are, and such...so let's try to answer some of those questions as best we can.

## What are all these branches?

Yes, there are a lot of "branches" in Loop talk but the concept is simple. I'll use an analogy to help. Basically, they are all slightly different versions of Loop...kind of like different edits of the same book.

To really understand what branches are, we should probably explain a little more about Loop's code and how development works.

Loop developers own an account in GitHub called [LoopKit](https://github.com/LoopKit).  Within that account, the developers have several "repositories" that support Loop in particular. A repository is like a book...let's think of it like a cookbook for now. Within the LoopKit account, there are repositories for Loop itself, LoopDocs, and various other supporting "frameworks" that are helper repositories for Loop to build correctly. For example, Loop's repo has a lot of the info about the app itself; the outward facing things that you interact with. How information is put to you and taken in from you...that's in Loop repository code. But, there's more than just a user interface for Loop. Loop has to do a lot of complex work like Bluetooth communications, algorithm math, pump communications, etc. The Loop app has help from frameworks to do those other parts. CGMBLEkit for some of the transmitter parts of Loop, RileyLink_ios for the pump managers (talking to the pumps and decoding their information), LoopKit for the algorithm about carbs and insulin curves, etc.

When you build Loop, in the background, Loop pulls those other frameworks (7 in total) into the build process using "Carthage".  Carthage is like a personal shopper. You give it a shopping list (the cartfile in Loop code is that shopping list) and it goes and fetches that for you during the build process. Sometimes your computer has an old shopping list...and that can cause build errors. Hence the "carthage update" fix in the Build Errors page...that command updates the shopping list to get the right versions of those frameworks.

<p align="center">
<img src="../img/loopkit.png" width="650">
</p>

Anyways...so now you know about the general structure of Loop and LoopKit in Github. Now we can discuss Loop itself a little deeper.

So let's imagine Loop as a cookbook. The developers are the authors/chefs of the recipes (code) in the cookbook. The authors spend countless hours testing new recipes, taste testing, documenting improvements. They send the drafts to the editor, who makes suggestions and eventually the cookbook is finalized. There are no grammar issues, no typos, the photos are beautiful and the recipes are yummy. They publish the book and you see a gorgeous final product on the shelves. That is called a "release" and it is the master branch. This book has been well-tested and is super stable. Every time you cook with those recipes, you know exactly what you're getting and lots of people have had a chance before you to make sure that it all tastes good. Master branch is stable and tested.

But then...the chefs/developers go on a trip. They are inspired by new cuisine and want to add new recipes to the old cookbook. (Things like omnipod support and overrides are new "recipes" that were developed since the last master release, for example.) But, the process for developing a recipe is arduous. Lots of trial and error involved. Lots of tweaking ingredients (code). The editors try out the new recipes and offer feedback (similar to the [Issues List in GitHub](https://github.com/LoopKit/Loop/issues)). While the recipes are being developed, they have a version of the old cookbook that gets marked up...edited in pencil a lot. Scribbles and notes in the side. Revisions happen frequently, because that's what testing new recipes is all about. These marked-up versions of the cookbook are called "dev" branch. Short for "development" branch. Like the name sounds...this is where new developments are happening, new recipes and tweaks. 

After much testing and tweaking, eventually the recipes get the flavors right (bugs in code are squashed) and enough people have provided feedback and careful observations of results...that the book goes to the publishing house for the next printing. The cookbook is republished with an updated edition number and new recipes are highlighted. When this happens in Loop, Loop's master branch is updated with the new features coming from dev (aka, "dev branch is merged into master branch"). When that happens, master branch gets another "release" version (you can see release history [here](https://github.com/LoopKit/Loop/releases)) and for that one day...dev and master are exactly the same. They stay the same until the Loop developers start working on the next batch of improvements, could be the next hour even or days later, but the process begins again. The developers will start editing the code again and dropping those edits in dev branch for further development.

## So what was/is Omnipod-testing branch?

Omnipod Loop development testing (not talking about the actual hacking work that preceded that) was done by a smaller group of people privately for months and months before public release of the omnipod-testing branch. This smaller group of people (several dozen) were actively watching their Omnipod Loops and capturing bug reports. There was a lot of work put in by the testers and Pete Schwamb (Loop Developer) to get the code fairly stable and reliable. 

When the code got to a stable, reliable state and was ready for a larger audience, omnipod-testing branch was made available as a "public testing" branch. This branch is slightly different than a dev branch. What it means is that it was pretty well tested, but not necessarily going to be perfect for everyone right away. There were expectations that some user-interface requests might be asked for after having a wider audience of users (bolus beeps is a good example of that kind of testing outcome). 

Also, omnipod-testing branch was not going to undergo a lot of active revisions to it when it was released. The intent was to keep it as a fairly known, unchanged product for people rather than a constantly changing code set...that way if people noted a bug, it would be a more "known" code base to work to debug.

So, omnipod-testing branch has undergone very little revision since it was first released. In fact, since its release in late April/early May 2019, there has only been two updates; one for the newer style Dexcom G6 transmitters and one for iOS 13 compatibility. Nothing major has been done in that branch, intentionally. As described above, the branch is serving as a stable platform for users and has helped catch bugs as a result of NOT being changed constantly.

## What is the future of omnipod-testing branch? Will it be updated?

No. Omnipod-testing branch is not going to be "updated" in the way many people are asking about. Little code fixes going in constantly will not happen. The reasons are given above. Omnipod-testing branch was just for that...testing that code in a static, fairly unchanged format to learn the most from it in a clean way.

As I just mentioned, bugs have been found in omnipod-testing branch. Those bugs are being squashed in dev branch and not in omnipod-testing branch. WHY? Because dev branch is the place for new code testing. Like playing a game of Jenga, changing code to squash one bug may result in unintended consequences that cause another bug. So the playground for that kind of testing is most appropriate for dev branch. Omnipod-testing branch is not a place to be testing bug squashes and code changes.

When dev gets more stable and the bugs are squashed/cleaned up, eventually that cleaned up code will be announced as a recommended replacement for omnipod-testing branch. Don't worry...there will be LoopDocs updates, pinned announcements in Looped and Zulipchat, Instagram posts, etc. You shouldn't be able to miss it.

## How can I stay current with what's going on in the branches?

Now we've learned that master and omnipod-testing branches really aren't changing much. They've each had some "hot-fixes" for late-breaking things that were needed for users in a timely fashion; the updated G6 transmitters and iOS update compatibility...but mostly the essential core of the code remains intentionally unchanged in those branches. ("Hot-fixes" are code changes to keep core functions when one of the outside pieces triggered the need. Apple and Dexcom changing their gear represent times when hot-fixes are most likely, but do not represent a major release change. Most people will want to update their Loop apps after a hot-fix is merged into the branch because those help ensure your gear works as expected.)

So it's just dev branch that changes often. The developers need YOU to know that dev is a constantly shifting, moving place. If you choose to come into a dev branch build...you need to be aware that is what dev does...moves, shakes, changes, and will update code frequently and unannounced in the traditional sense that most users in Looped group or Instagram would see. Developers are not helped by people being in a dev branch if those users are mistakenly thinking of it as a stable master branch with lots of detailed docs to go with it. People should only use a dev branch build if they EDUCATE themselves on the expectations and how to properly manage dev information and updates. People using dev branch should also have regular access to a computer to be able to rebuild quickly if a new bug/fix is identified. 

If you choose to use a dev build, you can stay abreast of developments in a number of ways...but they will all require you to do some legwork and keep yourself informed. This is not a situation where you should expect a fancy Loopdocs page updated regularly with current "dev updates"...that's just not the way dev branch works.

### Watch the Loop Repo and Issues list
First, subscribe to the Loop repo's Issues list by "watching" the [Loop repo](https://github.com/LoopKit/Loop). You can choose to watch the repo so that you get emails when new Issues are reported. This is a good way to find out if there's other people reporting odd behavior that you are wondering about. If you use dev and wonder about something you are seeing in Loop, you can check [Issues list](https://github.com/LoopKit/Loop/issues) to see if others are noticing the same. If so, you can help by capturing information and reporting it. Not super helpful to just say "yeah, me too..." but better if you can attach screenshots, Issue Reports from Loop settings, and a thorough description of the problem you are seeing. Be a part of the solution by thoughtfully providing information to help debug.

<p align="center">
<img src="../img/watching.png" width="650">
</p>

### Subscribe to the Zulipchat channels
Second, use [Zulipchat](https://loop.zulipchat.com) forums for Loop. This forum has several "streams" of conversations depending on interest. I highly recommend following the #github channel if you are wanting to watch for code changes. Code changes are called "commits" in GitHub. The #github channel will have an automated post whenever a new commit is made and it will give a brief line description of the commit.

<p align="center">
<img src="../img/zulipchat.png" width="650">
</p>

You can also go directly to the commit history for each of the branches if you'd like.

<a href="https://github.com/LoopKit/Loop/commits/master">Loop master branch commit history</a>

<a href="https://github.com/LoopKit/Loop/commits/dev">Loop dev branch commit history</a>

<a href="https://github.com/LoopKit/Loop/commits/omnipod-testing">Loop omnipod-testing branch commit history</a>

If you click on the commit, you can see exactly what changes to the code were made. It's an interesting learning experience. In red are the code that is old, in green is the updated code. The line numbers and file names of the edited code are also there to help.

<p align="center">
<img src="../img/commit.png" width="650">
</p>

I don't expect many of you would understand exactly what the edits mean, or how the new code might function...but I bring up the topic of commit history so that you can use that to realize just how often dev is updated. Go ahead and look at the number and frequency of commits in that dev branch...that is why there is no way someone is going to keep a "loopdocs" of dev changes. It's just too much a moving target.

### Keep checking Looped group
Third, keep watching Looped group. Major concerns/issues are brought up there...so no harm in scrolling through and seeing what's going on there.

### Become familiar with your data sources
Another useful thing if you'll be on dev branches undergoing a lot of active change...know how Loop works and where to look for additional information about what you are seeing. For example, if you see an IOB value that looks odd, you should know to look at the insulin deliveries are stored in Health app. Knowing to pull an Issue Report when you see a problem so you can provide that if asked. Knowing [how to capture debugging logs if the developers ask for that kind of info](https://youtu.be/Ac4MguvUO7M) is also a good skill. 

## What are the differences in branches now?

Roughly speaking...right now (September 23nd):

* Master: No Omnipod support, only Medtronic users. Stable. No updates planned in near future. The next update will depend on how long dev takes to settle down and get some good testing showing stability.

* Omnipod-testing branch: [known bug for IOB tracking](https://github.com/LoopKit/Loop/issues/1034) that has been discussed a lot in Looped group (go ahead and search group if you want to read up on it) for Pod users. The fix for this bug has been implemented in dev branch...the fix is NOT in omnipod-testing branch for reasons discussed above. Jenga. 

* Dev: Dev branch has a fix for the IOB tracking for Pod users. Dev branch also has new features that have not previously been a part of mainline Loop branches...overrides and Nightscout profile automatic updating. These two features are new and improved versions of the ones previously a part of JoJo branches (if you've tried those).

    Dev branches also has some known bugs still being addressed. For example, when the Loop cancels a temp basal to revert back to scheduled basals...the timestamp below the HUD's temp basal indicator goes back to the time when Loop was first opened. When the next temp basal is set, the timestamp operates properly again. Little stuff like that comes up a lot in dev...and you'll need to do your homework to read up on known issues please. Don't assume that dev branch is supposed to be glitch free...instead look at issues list, scroll through recent posts in Zulipchat and see if others have already noted/discussed the same.

## Should I update to dev branch?

You mean after all that you can't answer that question yourself? Really?

Ask yourself some questions. Are you the type that will have access to a computer? Be willing to update more frequently if needed? Be willing to do some leg work to stay current with possible reported issues? Be willing to watch a little closer after each time you update your Loop app to make sure no code regressions or new bugs came in with the update? If you can't commit to those things, then you should stay on master or omnipod-testing for awhile longer until dev settles down a bit.

## Is dev branch always changing frequently?

Sometimes yes, sometimes no. Right now we just happen to be in a time of a lot of changes. Pod updates, insulin tracking code changes (which get into the very core of Loop code), Nightscout integration updates, iOS updates...there's just a lot going on right now.

## Will JoJo branch be updated? Does it have "a fix"?

JoJo branches are my (me, Katie) personal-use branches that incorporated changes I found useful for our Looping. Those are changes that were pieced together from various sources in the open source community. Other people who coded up particular changes that benefited themselves and I found were useful, too. What JoJo was not designed to be is a branch that bifurcated users and complicated which branch people selected. The unintended consequence of sharing my personal branches over time is that confusion about branches has grown...and I don't enjoy that. I am working with Pete to get the features in my personal branches merged/improved into mainline Loop.

Dev branch already has automatic Nightscout profile updating now...and that is a huge feature that I really grew to depend on. It is nice to verify (without asking) that my daughter (or a caregiver) successfully edited a basal rate or setting the way I'd suggested when adjustments were needed during a school day. 

Dev branch also has overrides included now, in a way that improves upon the original version used in JoJo. Michael Pangburn is the author of that AMAZING set of features and I'll be forever in debt to him for the work he's put into overrides. Those have been a super tool to add to Loop and I'm so happy to see them in dev branch. 

Dev branch is also hopefully getting remote overrides...not sure when, but my fingers are crossed. 

The Integral Retrospective Correction is not in dev branch and may/may not be in the future (I don't know). We only used IRC for a short period of time and I think that it may be undergoing some code revision...so it may be "dormant" for a bit in the near future. Take a deep breath...you will be fine if IRC is dormant.

There are other minor things in Jojo that I expect could get fixed in dev (meter BG uploading to NS for Medtronic Loopers). Insulin delay will probably not be going into dev and instead there's some talk in the development channels about carb modelling improvements which would better address the reason insulin delay was helpful (to the extent it helped improve bolus amounts up-front). Finally, the bolusing below suspend threshold is a one-line code customization that I expect people could do on their own if it is added to LoopDocs. 

So...in short...NO. JoJo will not be updated with any new code. Instead, JoJo will go into retirement and dev branch (and eventually master branch) will have all you'd need...the IOB tracking fix, overrides, NS profile updating, etc.

We have been running dev branch live on Anna (my daughter) for several weeks now on both Pods and Medtronic (she's been going between the two), with regular updates to get new code and test/watch. 

The girl who maintains JoJo branches isn't even using JoJo branches. I think that says something, don't you?  




