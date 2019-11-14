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

Roughly speaking...right now (November 14th):

* Master: No Omnipod support, only Medtronic users. Stable. The next update will depend on how long dev takes to settle down and get some good testing showing stability.

* Omnipod-testing branch: [known bug for IOB tracking](https://github.com/LoopKit/Loop/issues/1034) that has been discussed a lot in Looped group (go ahead and search group if you want to read up on it) for Pod users. The fix for this bug has been implemented in dev branch...the fix is NOT in omnipod-testing branch for reasons discussed above.

* Dev: Dev branch has the following noticeable differences from omnipod-testing and master braches
    * fix for the IOB tracking for Pod users
    * [Overrides](https://loopkit.github.io/loopdocs/operation/loop-settings/overrides/)
    * [Remote Overrides](https://loopkit.github.io/loopdocs/nightscout/remote-overrides/)
    * Nightscout profile automatic updating when you update basals, carb ratios, or ISF in Loop
    * Updated carb absorption model (called non-linear)
</br>

Known issues in Dev branch currently:

* [Settings can sometimes temporarily "disappear"](https://github.com/LoopKit/Loop/issues/1170)
* [Medtronic users timestamp for scheduled basals in HUD may be wrong](https://github.com/LoopKit/Loop/issues/1110)
    
Remember to use the [LoopKit Github Issues page](https://github.com/LoopKit/Loop/issues) to check for any reported issues that might resemble things you are wondering about. If you'd like to report a bug, check the list and see if someone has already opened an issue for it.

## Carb Model changes in Dev

Dev branch has recently been updated with a new carb model. Let's give some info about the carb model update.

Previously, the carb model Loop used (and still uses in Master branch now) had a linear absorption predicted. What this means is that food absorption was modeled like a triangle, with food absorption ramping up evenly, and then peaking before decreasing in a mirror-image to the increase. But looking at large groups of meals' datasets (and supported by personal, anecdotal experiences), food really has a bit more of a non-linear absorption. Meaning, we usually see more of a food impact up-front than the old carb model in Loop predicted.

What did that mismatch mean for us if the model predicts a linear absorption, but the meal actually behaves differently? 

1. Bolusing: You've probably seen smaller upfront boluses for meals than you would have preferred. This is because the insulin was predicted to over-power the linear (slower) carb model soon after a bolus is given.
2. Early low temp basals: You've also probably seen a tendency to have early zero basal or low basals set by Loop for the first 30-60 minutes after a meal bolus if you don't have a significant blood glucose spike immediately after the carb entry. This might have been even more obvious for those of you who are regularly waiting to eat after a bolus, too.

With a non-linear absorption model (that is now in dev), the carb absorption will more closely match observed blood glucose impacts we've seen after meals. And when the model is more closely matching actual experience, that means the predicted blood glucose curves will do a better job at providing more upfront bolus and not having the tendency to have overly conservative temp basals soon after a meal.

What do you have to do to use the new model? Nothing. It is baked into the dev branch now. Simply update your Loop app using dev branch code and you will be using the new model.

What if you want to go back to the old model? You will have to edit a line in LoopKit's LoopKit code [here](https://github.com/LoopKit/LoopKit/blob/dev/LoopKit/CarbKit/CarbStore.swift#L207) to use `.linear` if you wanted to go back to the old carb model. If you want to read more about the models, please check out the [Zulipchat thread here](https://loop.zulipchat.com/#narrow/stream/144111-general/topic/Possible.20Carb.20Model.20Changes) and [ here, too](https://loop.zulipchat.com/#narrow/stream/144111-general/topic/Possible.20Carb.20Model.20Changes/near/180762097). But realize that the code edit for changing models would be easiest done using a [LoopWorkspace](https://loopkit.github.io/loopdocs/build/loopworkspace/) because the edit is in one of the frameworks that Loop uses (rather than Loop code itself), so this is one of those instances where you will have to do some work to learn how to use a LoopWorkspace properly.




