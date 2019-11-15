# Step 13: Download Loop code

!!!danger "Time Estimate"
    * 1 minute to download Loop code
    * 10 minutes to read this page
    
!!!info "Summary"
    * If you want to use Omnipod Loop, you should use the dev branch
    * Medtronic pumps are supported on all branches of Loop
    
!!!warning "FAQs"
    * **"What the heck is a branch?"** That's a great question. We have a page all about [Branch FAQs](https://loopkit.github.io/loopdocs/faqs/branch-faqs/)
    * **"How can I tell which version I have downloaded if I'm unsure?"** The downloaded Loop folder's name will give you an indication of which branch you downloaded. The folder name will be in the format `Loop-BranchName`. 
    * **"When do I need to download new Loop code?"** Anytime you want to update your Loop app to get new features, you'll simply download the code again by clicking on the links below. The links always go to the most recent version of each of the branches. It's a good idea is to delete your old downloads before making a new one, just to avoid confusion.

You’ll need to download the Loop code in order to build the app on your computer.  **If you want to build a version of Loop that supports Omnipod, you should select the dev branch download, because Master branch only supports Medtronic pumps currently.** 

</br></br>
<p align="center">
[Loop: Master branch](https://github.com/LoopKit/Loop/archive/master.zip)</br></br>
[Loop: Dev branch](https://github.com/LoopKit/Loop/archive/dev.zip)</br></br>

## Loop Branches
Master vs Dev? Wondering which to choose? For now, if you are a pod user, you should choose dev branch. If you are a Medtronic user, you can choose either Master or Dev. To learn about the differences, please see the [Branch FAQs page](https://loopkit.github.io/loopdocs/faqs/branch-faqs/).

## Store and name your download properly
It is best practice to leave your Loop code in your Downloads folder. If you store your Loop code in a different folder than Downloads (such as your Documents folder or Desktop), make sure the specified folder is **not** an iCloud drive. Storing your Loop code in an iCloud drive folder will prevent Loop from building successfully.  How do you know if a folder is an iCloud drive? Check your System Preferences. If your System Preferences for iCloud is set as shown below, your Documents and Desktop folders are iCloud drives and **NOT** appropriate places to save your Loop download.
<p align="center">
<img src="../img/icloud-drive.png" width="650">
</p></br>

Depending on your browser and settings, your Loop download may or may not automatically unzip. If it does not unzip automatically, you can right-click on the zip file and choose to "Open With" Archive Utility. This will create a blue folder called `Loop-master`.  HOWEVER, if you already have an existing `Loop-master` folder from a previous download, the name of the next download will be something like `Loop-master (1)`.  The problem with that folder name is that it contains a space...and spaces in the name will cause your Loop build to fail. So, either delete old copies of Loop before downloading/unzipping -OR- rename the folder(s) to ensure that NO SPACES are in the folder name.
<p align="center">
<img src="../img/folder-name.png" width="650">
</p>

## Next Step: Build Loop app

Now you are ready to move onto Step 14 to [Build Loop app](https://loopkit.github.io/loopdocs/build/step14/).
