# Step 13: Download Loop code

!!!danger "Time Estimate"
    * 1 minute to download Loop code
    * 10 minutes to read this page
    
!!!info "Summary"
    * Master branch of Loop has been recently updated to Loop v2.0
    * All branches of Loop support both Medtronic and Omnipod pump users.
    
!!!warning "FAQs"
    * **"What the heck is a branch?"** That's a great question. We have a page all about [Branch FAQs](https://loopkit.github.io/loopdocs/faqs/branch-faqs/)
    * **"How can I tell which version I have downloaded if I'm unsure?"** The downloaded Loop folder's name will give you an indication of which branch you downloaded. The folder name will be in the format `Loop-BranchName`. 
    * **"When do I need to download new Loop code?"** Anytime you want to update your Loop app to get new features, you'll simply download the code again by clicking on the links below. The links always go to the most recent version of each of the branches. It's a good idea is to delete your old downloads before making a new one, just to avoid confusion.

## Pick a branch to download
You’ll need to download the Loop code in order to build the app on your computer. Various versions of Loop code are stored in "branches". You have a choice of branches to build from...you'll pick one to download. Not sure what a branch is or what it means? You can read more details on the [Branch FAQs page](https://loopkit.github.io/loopdocs/faqs/branch-faqs/).

Master vs Dev vs some other branch? Generally speaking, most users should stick to using Master branch. Experimental features and new code changes will be testing in the dev branch first...so that dev branch can be prone to having periodic glitches or regressions as the new features are developed. If you aren't a developer or debugging, stick to Master branch.  Click on ONE of the links below to download Loop code...hint hint...**<u>click on the Master branch for 99% of users</u>**.

</br></br>
<p align="center">
[Loop: Master branch](https://github.com/LoopKit/Loop/archive/master.zip)</br></br>
********************

[Dev branch---in very rough shape right now, please only build if developer interested in debugging](https://github.com/LoopKit/Loop/archive/dev.zip)</br></br>
[Automatic-bolus branch---do your research before using as well, if you are asking what it is then you haven't researched enough yet](https://github.com/LoopKit/Loop/archive/automatic-bolus.zip)</br></br>

*********************

## Store and name your download properly
It is best practice to leave your Loop code in your Downloads folder. If you store your Loop code in a different folder than Downloads (such as your Documents folder or Desktop), make sure the specified folder is **not** an iCloud drive. Storing your Loop code in an iCloud drive folder will prevent Loop from building successfully.  How do you know if a folder is an iCloud drive? Check your System Preferences. If your System Preferences for iCloud is set as shown below, your Documents and Desktop folders are iCloud drives and **NOT** appropriate places to save your Loop download.
<p align="center">
<img src="../img/icloud-drive.png" width="650">
</p></br>

Depending on your browser and settings, your Loop download may or may not automatically unzip. If it does not unzip automatically, you can right-click on the zip file and choose to "Open With" Archive Utility. This will create a blue folder called `Loop-master`.  HOWEVER, if you already have an existing `Loop-master` folder from a previous download, the name of the next download will be something like `Loop-master (1)`.

## Next Step: Build Loop app

Now you are ready to move onto Step 14 to [Build Loop app](https://loopkit.github.io/loopdocs/build/step14/).
