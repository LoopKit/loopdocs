# Step 13: Download Loop code

!!!danger "Time Estimate"
    * 1 minute to download Loop code
    * 10 minutes to read this page
    
!!!info "Summary"
    * If you want to use Omnipod Loop, you should use the omnipod-testing branch
    * Dev branch technically has Omnipod support now, but is still considered less stable than omnipod-testing branch for the average user
    * Medtronic pumps are supported on all branches of Loop
    
!!!warning "FAQs"
    * **"What the heck is a branch?"** Let's use an analogy of when a book is published, sometimes a little later the author decides to make edits to the published book. They will have a "mark-up" copy of the original version and make edits. In this analogy, `master branch` is a published book. It is considered a stable, well-reviewed and tested version of the Loop app. As new features and improvements are made, they are made into the "mark-up copy" called `dev branch`. The dev branch will likely have some bugs and changes on a more frequent basis as the new editts are tested and revised. Other people may also have their own branches, based on the original published book since this is an open source project, beyond just the Loop developers. There are no documents that track all the "unofficial" branches of Loop that others may have...there could be an endless amount, updated randomly, and not all of them in good working order so would be pointless to try to track them all.
    * **"How can I tell which version I have downloaded in case I'm unsure?"** The downloaded Loop folder's name will give you an indication of which branch you downloaded. The folder name will be in the format `Loop-BranchName`. 
    * **"When do I need to download new Loop code?"** Anytime you want to update your Loop app to get new features, you'll simply download the code again by clicking on the links below. The links always go to the most recent version of each of the branches. A good idea is to delete your old downloads before making a new one, just to avoid confusion.

You’ll need to download the Loop code in order to build the app on your computer.  Wondering which to choose? Read the discussion below **BEFORE** clicking on one of the links to download.

</br></br>
<p align="center">
[Loop: Master branch](https://github.com/LoopKit/Loop/archive/master.zip)</br></br>
[Loop: Dev branch](https://github.com/LoopKit/Loop/archive/dev.zip)</br></br>
[Loop: Omnipod-testing branch](https://github.com/LoopKit/Loop/archive/omnipod-testing.zip)
</p></br>

## Loop Branches
Master vs Dev? The Loop code resides in a website called [GitHub](https://github.com/LoopKit/Loop). The various projects in GitHub use "repositories". A repository is kind of like a project's bookshelf, holding various books versions (aka branches) of a project. The master branch is considered a stable version of the project. Any new features or options are first tested in a public feature branch or dev (short for "development") branch of the Loop. If you hear of "new features" being tested, these are things that may be eventually merged into the master branch once any bugs are worked out. 

**If you want to build a version of Loop that supports Omnipod, you should select the Omnipod-testing branch download above.** Technically the dev branch can work for Omnipod loopers now, but there are a lot of bugs actively being addressed in dev branch. It is considered more unstable than omnipod-testing branch at this time. You should only choose dev branch if you are able to watch your Loop carefully and have no problem updating often (like several times a week at the moment). 

If you are choosing to use a testing branch, such as dev or omnipod-testing, please be prepared to update your Loop app to get bug fixes as they are released. As you encounter any bugs or glitches, please check the docs first to see if that issue is already answered. If you think you truly are seeing strange behavior, report the bug to Loop's GitHub by [creating a "New Issue" here](https://github.com/loopkit/loop/issues). You can also look through the list of known issues already reported, as there is a chance your issue has already been seen by others. 

Ok, now that you've read about the various branches, go ahead and pick a link to download.

## What about "other branches"

There are other branches and features (JoJo, IRC, Spike-Loop, etc) that other Loop users may develop from time to time. Those users may choose to share their work publicly or keep their work more quietly on their Github accounts. If someone develops a new feature for their own Loop use and they think it has wider value to others, they may submit a "Pull Request" asking the Loop developers to consider the new feature/code into Loop officially. A submittal of a Pull Request does not guarantee that the feature/code will eventually be incorporated into the main Loop versions.

These docs only refer to Loop branches maintained and reviewed by the Loop developers. It would be too difficult to track and index (much less test and explain) all the possible customized personal branches that could be out there for all the Loop users. **If you are interested in one of the non-official Loop branches, PLEASE use the search tool in Looped Group to find links where you can learn about those personal branches.**

One note: I (Katie) have shared my JoJo branches in Looped Group on Facebook for quite sometime. JoJo branches have features that other people have created and I've simply packaged them together for my own personal use. I do expect that soon there will be no more JoJo branches and they will be retired, as the important core features will hopefully be available in Loop official branches. No promises, but we are working towards that. It will be so much easier to have no JoJo branch in the future...I'm really looking forward to that.

## Store and name your download properly
Best practice is to leave your Loop code in your Downloads folder. If you store your Loop code in a different folder than Downloads (such as your Documents folder or Desktop), make sure the specified folder is **not** an iCloud drive. Storing your Loop code in an iCloud drive folder will prevent Loop from building successfully.  How do you know if a folder is an iCloud drive? Check your System Preferences. If your System Preferences for iCloud is set as shown below, your Documents and Desktop folders are iCloud drives and **NOT** appropriate places to save your Loop download.
<p align="center">
<img src="../img/icloud-drive.png" width="650">
</p></br>

Depending on your browser and settings, your Loop download may or may not automatically unzip. If it does not unzip automatically, you can right-click on the zip file and choose to "Open With" Archive Utility. This will create a blue folder called `Loop-master`.  HOWEVER, if you already have an existing `Loop-master` folder from a previous download, the name of the next download will be something like `Loop-master (1)`.  The problem with that folder name is that it contains a space...and spaces in the name will cause your Loop build to fail. So, either delete old copies of Loop before downloading/unzipping -OR- rename the folder(s) to ensure that NO SPACES are in the folder name.
<p align="center">
<img src="../img/folder-name.png" width="650">
</p>

## Next Step: Build Loop app

Now you are ready to move onto Step 14 to [Build Loop app](https://loopkit.github.io/loopdocs/build/step14/).
