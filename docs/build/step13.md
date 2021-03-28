# Step 13: Download Loop code

!!! danger "Time Estimate"
    - 1 minute to download Loop code
    - 10 minutes to read this page

!!! info "Summary"
    - All branches of Loop support both Medtronic and Omnipod pump users
    - master and automatic-bolus are at Loop v2.2.4

!!! warning "FAQs"
    - **"What the heck is a branch?"** That's a great question. We have a page all about [Branch FAQs](../faqs/branch-faqs.md)
    - **"How can I tell which version I have downloaded if I'm unsure?"** The downloaded Loop folder's name will give you an indication of which branch you downloaded. The folder name will be in the format `Loop-BranchName`.
    - **"When do I need to download new Loop code?"** Anytime you want to update your Loop app to get new features, you'll simply download the code again by clicking on the links below. The links always go to the most recent version of each of the branches. It's a good idea is to delete your old downloads before making a new one, just to avoid confusion.

## Pick a branch to download

You’ll need to download the Loop code in order to build the app on your computer. Various versions of Loop code are available. Both master and automatic-bolus are pretty stable and widely used.  The [Compare Version](https://www.loopnlearn.org/compare-branches/) webpage explains the differences between master and automatic-bolus.

Click on one of the links below to download Loop code and then follow the rest of the steps until you have a new version on your device. (These links always point to the most recent version of the code.)

---

- [Loop: master branch](https://github.com/LoopKit/Loop/archive/master.zip)

- [Loop: automatic-bolus branch](https://github.com/LoopKit/Loop/archive/automatic-bolus.zip)

---

- [Dev branch---please only build if you're a developer/advanced user interested in testing](https://github.com/LoopKit/Loop/archive/dev.zip)
    - Note that dev will soon require iOS 14 on your device
    - Once you install dev on a device, you might have to delete the app to return to master or automatic-bolus


---

## Store and name your download properly

It is best practice to leave your Loop code in your Downloads folder. If you store your Loop code in a different folder than Downloads (such as your Documents folder or Desktop), make sure the specified folder is **not** an iCloud drive. Storing your Loop code in an iCloud drive folder will prevent Loop from building successfully.  How do you know if a folder is an iCloud drive? Check your System Preferences. If your System Preferences for iCloud is set as shown below, your Documents and Desktop folders are iCloud drives and **NOT** appropriate places to save your Loop download.

![img/icloud-drive.png](img/icloud-drive.png){width="650"}
{align="center"}

Depending on your browser and settings, your Loop download may or may not automatically unzip. If it does not unzip automatically, you can right-click on the zip file and choose to "Open With" Archive Utility. This will create a blue folder called `Loop-master`.  HOWEVER, if you already have an existing `Loop-master` folder from a previous download, the name of the next download will be something like `Loop-master (1)`.

## Next Step: Build Loop app

Now you are ready to move onto Step 14 to [Build Loop app](step14.md).
