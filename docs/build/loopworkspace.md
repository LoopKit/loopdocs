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

## How do you "get" LoopWorkspace?

In order to use a LoopWorkspace, you need to get a copy of the code (it's different set of code compared to the usual Loop downloads). BUT...don't go to github and simply "download" the code like perhaps you are used to. Instead, we need to open Terminal app and do a set of commands to do a special sort of download called "git clone".

To get that LoopWorkspace code to your computer, you'll need to use a "git clone" command LIKE THIS (but not exactly the same...you're going to edit the "branch-name" part in there):

`git clone --branch=branch-name --recurse-submodules https://github.com/LoopKit/LoopWorkspace`

Now...look carefully and notice two things...that command is getting (1) LoopKit's version of LoopWorkspace and (2) also specifying the branch you want to start working with when the clone is done.

So, you will need to edit that "branch-name" before using the command so that you are getting started with the branch you want. For example:

Automatic-bolus branch command would be: `git clone --branch=automatic-bolus --recurse-submodules https://github.com/LoopKit/LoopWorkspace`

Dev branch command would be: `git clone --branch=dev --recurse-submodules https://github.com/LoopKit/LoopWorkspace`


## Where does the clone go?

A cloned version of Loop doesn't go to your "Downloads" folder like you are used to with the usual version of building Loop app.  Instead, the cloned version of the LoopWorkspace will go into whatever directory you were sitting in in Terminal app when you did the command. Terminal app by default drops you into your User account's home directory when you first open it, so that's a good assumption on where your cloned LoopWorkspace will go.

How can you find your home directory?

1. In Terminal, if you use `cd` that will take you there automatically.</br>
2. In Finder, shift-command-H will open your "home" folder.

</p>
<p align="center">
<img src="../img/root-finder.png" width="750">
</p>

As you can see, I have a lot of cloned things in my home directory from GitHub that involve Loop. You may have fewer...but be aware, you can always delete and reclone if you are in doubt or confused. 

## Non-LoopKit clones

!!!info "Average Loopers can skip this whole section...it's for Developers mostly"
    This whole section about non-LoopKit workspace clones is something almost every Looper can totally skip over. I'm only writing up this section for people who are interested in dabbling in code collaborations/customizations that they would want to maintain separate from LoopKit proper. 

Scenario: You have a friend named DeveloperBob who has his own version of LoopWorkspace that he's customized. DeveloperBob wants you to look at his code customizations and collaborate with him. You need to change the "git clone" command to get DeveloperBob's version, not LoopKit's version. And, you'd want to make sure you specify the branch that the new feature is on, too. DeveloperBob should usually include the branch name when he posts/shares. So, the command line might be edited to something like:

`git clone --branch=new-features --recurse-submodules https://github.com/DeveloperBob/LoopWorkspace`

So...if you are trying to grab someone's LoopWorkspace to use it, you'll need to make sure you get the command correct if they don't specify it for you.
You can't clone mutliple "LoopWorkspaces" into the exact same home directory (because they will have the same name), so you may want to create a subdirectory to put them in. Like you could make a folder called "DeveloperBob" and then move into that directory in Terminal before you clone DeveloperBob's LoopWorkspace. 

How would you do that? Simple `cd && mkdir DeveloperBob` would make the new folder in your home directory. And then `cd DeveloperBob` would move your Terminal app to be working inside the new DeveloperBob folder. So if you wanted to clone DeveloperBob's LoopWorkspace, that would be a good way to keep track of where the code came from.

If you ever get in doubt and can't remember where your code was cloned from, you can `cd LoopWorkspace` to get into the directory and then use `git remote -v` to tell you where it came from.

## Using LoopWorkspace

So to summarize, you need to clone LoopWorkspace by:

1. Open Terminal app and enter the command  `cd` to make sure you are at the root directory.
2. Copy and paste the "git command" of your choosing (making sure to edit the command properly for the branch you want to use) into Terminal app. Press return.
3. Wait a couple minutes as the clone finishes. You'll be back at a plain Terminal prompt when it's done.
4. Close Terminal app.
5. Find that cloned folder, by opening the Finder app. Click `shift-command-H` and Finder will open your "home" or root folder. Scroll down and you'll see a folder called `LoopWorkspace`.
6. From withing the LoopWorkspace folder, double-click on the `Loop.xcworkspace` file to open the project in Xcode.

</p>
<p align="center">
<img src="../img/workspace-file.png" width="550">
</p>

!!!warning "Two things to notice"
    Once you are in LoopWorkspace opened in Xcode, everything is pretty similar for building with only two notable exceptions. You need to click on that blue Loop folder to see the signing targets, and you need to change the build scheme to the left of your phone to "Loop (Workspace)" in order to build properly.

    </p>
    <p align="center">
    <img src="../img/workspace-use.png" width="750">
    </p>

    Oh wait...there is a noticable difference...the speed! LoopWorkspace will build Loop much faster than Loop because of the way it uses submodules. I do rather like that benefit to using LoopWorkspaces too.

## Updating Loop using LoopWorkspace

When you want to update your Loop app using LoopWorkspace, you'll need to use  `git pull --recurse` command while in the LoopWorkspace directory in Terminal. That will grab the lastest updates and then you can build. If you still have signing team filled in, you may get a conflict on the command...so either unsign before the git pull or do a `git stash` and then pull.

And with that ends the super basic "How can I build with a LoopWorkspace?" questions and use for 90% of the users.

So to recap the update process:

1. Open Terminal app
2. Enter `cd && cd LoopWorkspace`
3. Enter `git stash`
4. Enter `git pull --recurse`
5. Open the project in Xcode by double clicking on the `Loop.xcworkspace` file
6. Click on the blue Loop folder and sign four targets
7. Select **Loop (Workspace)** as the build scheme (left of the phone selection) and your phone 
8. Press build button

## Checking out different branches within a LoopWorkspace

More advanced users...I'm not going to explain this in quite so much detail, but yes, you can individually change the branches in a LoopWorkspace. 

There are 2 main ways to do this. 

1. If you're already familiar with Git, the easiest way is to `cd` into the appropriate repository (like `cd rileylink_ios`) and `checkout` the desired branch.


2. If you're not as familiar with Git, if you edit your .gitmodules directory in LoopWorkspace, you can specify other repos to use (and add a line to specify branches, too). Then if you do a `git submodule sync` the workspace will sync to new submodules. Then `git submodule update --init --recursive --remote` will update all the submodules to the right branches and get HEADs detached correctly, etc. 

</p>
<p align="center">
<img src="../img/gitmodules.png" width="750">
</p>

## Pushing commits from LoopWorkspace

So you've got a great idea for a new feature, made those changes to your LoopWorkspace and want to get them into Github. Awesome!

To understand how to do this, we'll need to understand a bit more about how Git keeps track of changes. In Git, developers can have different "branches" (see the [branch FAQs page](https://loopkit.github.io/loopdocs/faqs/branch-faqs/) for more details about what a branch is). There are two different types of branches: remote and local. If you were to fork Loop on Github, then the branches that you can see on Github are "remote" branches - they're hosted on the Github server. On the other hand, you can also create "local" branches that are stored directly on your computer by "checking out" the remote branch. You'll need to "commit" your changes to the local branch, then "push" those changes to the remote branch in order to be able to see them in Github. There are specific commands that you can type into the command line to do all of these actions, but I'm not going to go into detail because there are different ways (like graphic Git editors) that can an easier way to do them.

It's a little easier to think about this with an analogy. Let's say you're working at a company that's creating a cookbook. There's a centralized, production-ready version of the cookbook on their website that all the employees can view. Think of the website version of this cookbook as being like the remote branch. You're assigned to change the pancake recipe in the cookbook. Since the company doesn't want employees to make changes directly to the version of the cookbook that the customers see, you need to make a copy of it on your computer so you can make your changes to the pancake recipe. When you make the personal copy on your computer, it's like "checking out" the remote branch. Your copy is like the local branch - you can make whatever changes you want without having to worry about customers accidentally seeing them. When you make an important change to the recipe (like adding a photo or changing the ingredients), you might want to make a note in the edit history so that you can go back to that version of the recipe in case you accidentally make unintended changes - those notes you make would be "commits". Once you're happy with the recipe, you'll add it back into the production version of the cookbook on the website, which is similar to what you're doing when you "push" your changes. 

Where do the submodules fit in? Each submodule is actually a branch, so when you make changes to multiple submodules, you'll need to commit those changes to their respective branches. Let's say you've made changes to Loop and LoopKit. You'll need to go into Loop and commit + push the changes, then go into LoopKit and commit + push the changes. 

There are a few different ways to keep track of all these different branches. Some people like using the command line (which is what you're using when you do commands like `git clone`) because it's very customizable and has the largest variety of commands. Others like to use graphic Git editors, which make it easier to see changes and be able to do a variety of common actions (like cloning, committing, and pushing) with the push of a button. Everyone has their own preferences, but some methods that Loop contributors have used in the past include the command line, [Gitkraken](https://www.gitkraken.com/), and [SourceTree](https://www.sourcetreeapp.com/).
