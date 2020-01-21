# Loop Workspace

This page is for the "advanced" user. Well, maybe there is a better word for it. Adventurous? Curious? But, if you are a newbie and not into crazy stuff...everything in here is completely and totally just optional. Using or not using LoopWorkspace does not affect your looping nor access to Loop. This page is about me finding an efficient way to answer questions about a topic that takes a lot of words to answer usually...so I'm saving time by making this page.

Traditionally, Loopdocs has only told you about the option of downloading Loop as a zip file through those links. But, there's another way of getting that code to your computer called "git". Git is a system of "distributed version control" that allows remotely (as in not located in same place) collaborating people to work on one project and still track their changes to the same place. For example, if I sent 5 people one document to proof-read at the same time...it is quite possible that the edits I will get back from those 5 people would conflict with each other. Bob may have entirely deleted a sentence while Mary would have added words to that sentence. Git lets these remotely collaborating people deal with "resolving conflict" between versions more easily and merging suggestions (pull requests) into a coordinated space.

So, in using Git, we can do things with "git commands". Like "Hey git...make me an exact copy of that guy's work over there." or "Hey git, I'd like to compare my version of this page with Joe's version of the same page." Or using my old cookbook analogy..."Hey git, I'd like to start a new cookbook called Italian Desserts."

But yes, git commands take awhile to properly use. And they are not plain english friendly. Or any kind of friendly really, at least not to very many people. Therefore, we have emphasized the downloading of a zip file to make you not have to use git.

## Why this page?

So why am I about to tell you about a Loop repo that involves git? The answer is because LoopWorkspace is a pretty nice feature that you may run across if you are testing new features. And if you do, I do not want to be answering these How To questions in Zulipchat and Facebook repeatedly...so let's consolidate the info here.

!!!info "You can still download zips"
    You do not have to use LoopWorkspace. Just to be clear, everything still works like it used to. LoopWorkspace is just a different option to save the amount of git and cartfile work that you would have to do otherwise. Depending on what you'd like to do, it may be a good option. Usually that "good option" is if you are trying new code that involves edits to the Loop frameworks.

## What is LoopWorkspace?

I'm going to retread some info that you may have read in the Branches FAQs page earlier, but is really important to this discussion on LoopWorkspace. Loop developers own an account in GitHub called [LoopKit](https://github.com/LoopKit).  Within that account, the developers have several "repositories" that support Loop in particular. A repository is like a book...let's think of it like a cookbook for now. Within the LoopKit account, there are repositories for Loop itself, LoopDocs, and various other supporting "frameworks" that are helper repositories for Loop to build correctly. For example, Loop's repo has a lot of the info about the app itself; the outward facing things that you interact with. How information is put to you and taken in from you...that's in Loop repository code. But, there's more than just a user interface for Loop. Loop has to do a lot of complex work like Bluetooth communications, algorithm math, pump communications, etc. The Loop app has help from frameworks to do those other parts. CGMBLEkit for some of the transmitter parts of Loop, RileyLink_ios for the pump managers (talking to the pumps and decoding their information), LoopKit for the algorithm about carbs and insulin curves, etc.

When you build Loop, in the background, Loop pulls those other frameworks (7 in total) into the build process using "Carthage".  Carthage is like a personal shopper. You give it a shopping list (the cartfile in Loop code is that shopping list) and it goes and fetches that for you during the build process. The cartfile shows where the various frameworks are (exactly which GitHub account) and which branch to use. This is an example of what the cartfile looks like for dev branch right now.

</p>
<p align="center">
<img src="../img/cartfile.png" width="750">
</p>

Many of the frameworks also have their own cartfiles embedded in them. So, when developers are doing code changes in one of those frameworks, it gets to be a nest of effort to keep the cartfiles pointing to the right places and consistent in the embedded cartfiles for the various frameworks. 

And this is where LoopWorkspace comes in. LoopWorkspace uses submodules instead of cartfiles to define how the frameworks are coordinated for building. The workspace puts all the frameworks closer together and this makes the development process a LOT easier than managing cartfiles. A LOT EASIER. So, as new features might come out for testing, you may see LoopWorkspaces offered for that testing option instead of simply a downloaded zip. The ease of using workspace for developers is the reason why.

## How do you "get" LoopWorkspace(s)?

In order to use a LoopWorkspace, you need to start using git commands in the Terminal app. The main LoopWorkspace is [here in the LoopKit account](https://github.com/LoopKit/LoopWorkspace).  To get that to your computer, you'll need to "clone" it with this command:

`git clone --branch=dev --recurse-submodules https://github.com/LoopKit/LoopWorkspace`

Now...look carefully...that is getting LoopKit's version of LoopWorkspace and grabbing the dev branch as the one you want to start working with.

If DeveloperBob had forked a copy of LoopKit's LoopWorkspace and made some changes he wanted to test, and then you wanted to grab them...you'd need to change the command to get DeveloperBob's version. And, you'd want to make sure you specify the branch that the new feature is on, too. DeveloperBob should usually include the branch name when he posts/shares. So, it might be something like:

`git clone --branch=bitching-new-feature --recurse-submodules https://github.com/DeveloperBob/LoopWorkspace`

So...if you are trying to grab someone's LoopWorkspace to use it, you'll need to make sure you get the command correct if they don't specify it for you.

## Where does the clone go?

The cloned version of the LoopWorkspace will go into whatever directory you were sitting in in Terminal app when you did the command. Terminal app by default drops you into your User account's home directory when you first open it, so that's a good assumption on where your cloned LoopWorkspace will go.

How can you find your home directory?

1. In Terminal, if you use `cd` that will take you there automatically.</br>
2. In Finder, shift-command-H will open your "home" folder.

</p>
<p align="center">
<img src="../img/root-finder.png" width="750">
</p>

As you can see, I have a lot of cloned things in my home directory from GitHub that involve Loop. You may have fewer...but be aware, you can always delete and reclone if you are in doubt or confused. You can't clone mutliple "LoopWorkspaces" into the exact same home directory (because they will have the same name), so you may want to create a subdirectory to put them in. Like you could make a folder called "DeveloperJane" and then move into that directory in Terminal before you clone DeveloperJane's LoopWorkspace. 

How would you do that? Simple `cd && mkdir DeveloperJane` would make the new folder in your home directory. And then `cd DeveloperJane` would move your Terminal app to be working inside the new DeveloperJane folder. So if you wanted to clone DeveloperJane's LoopWorkspace, that would be a good way to keep track of where the code came from.

If you ever get in doubt and can't remember where your code was clone from, you can `cd LoopWorkspace` to get into your cloned directory and then use `git remote -v` to tell you where it came from.

## Using LoopWorkspace

Once you get your workspace cloned, you simply find that cloned folder (wherever you cloned it to...use Finder to find it) and double-click on the Loop.xcworkspace file to open the project in Xcode.

</p>
<p align="center">
<img src="../img/workspace-file.png" width="550">
</p>

Once you are in LoopWorkspace, everything is pretty similar for building with only two notable exceptions. You need to click on that blue Loop folder to see the signing targets, and you need to change the build scheme to the left of your phone to "Loop (Workspace)" in order to build properly.

</p>
<p align="center">
<img src="../img/workspace-use.png" width="750">
</p>

Oh wait...there is a noticable difference...the speed! LoopWorkspace will build Loop much faster than Loop because of the way it uses submodules. I do rather like that benefit to using LoopWorkspaces too.

## Updating Loop using LoopWorkspace

When you want to update your Loop app using LoopWorkspace, you'd just do a `git pull --recurse` while in the LoopWorkspace directory in Terminal. That will grab the lastest updates and then you can build. If you still have signing team filled in, you may get a conflict on the command...so either unsign before the git pull or do a `git stash` and then pull.

And with that ends the super basic "How can I build with a LoopWorkspace?" questions and use for 90% of the users.

## Pushing commits from LoopWorkspace

More advanced users...I'm not going to explain this in quite so much detail, but yes, you can push commits from your forked/cloned LoopWorkspace to your various repos in your own GitHub account. 

In short, if you edit your .gitmodules directory in LoopWorkspace, you can specify other repos to use (and add a line to specify branches, too). This way the cartfiles being mismatched is not a problem while using submodules, for example:

</p>
<p align="center">
<img src="../img/gitmodules.png" width="750">
</p>


Then if you do a `git submodule sync` the workspace will sync to new submodules. Then `git submodule update --init --recursive --remote` will update all the submodules to the right branches and get HEADs detached correctly, etc. From there you can work as you'd like. When you are ready to commit changes, just cd into the directory you'd like to make the commits/pushes in (aka `cd rileylink_ios`) and you'll be good to go.
