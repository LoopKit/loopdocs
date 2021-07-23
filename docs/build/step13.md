# Step 13: Download Loop Code

!!! danger "Time Estimate"
    - 10 minutes to read this page
    - 1 minute to download Loop code

!!! info "Summary"
    - There are two branches suitable for new Loopers

!!! warning "FAQs"
    - **"What the heck is a branch?"** That's a great question. We have a page all about [Branch FAQs](../faqs/branch-faqs.md)
    - **"How can I tell which version I have downloaded if I'm unsure?"** The downloaded Loop folder's name will give you an indication of which branch you downloaded. The folder name will be in the format `Loop-BranchName`.
    - **"When do I need to download new Loop code?"** Anytime you want to update your Loop app to get new features, you'll simply download the code again by clicking on the links below. The links always go to the most recent version of each of the branches. It's a good idea is to delete your old downloads before making a new one, just to avoid confusion.

## Pick a Branch to Download

You’ll need to download the Loop code. You will then build the app on your computer with Xcode, which will transfer the app to your phone or ipod.

Various versions of Loop code are available. Both master and automatic-bolus are stable and widely used.  The [Compare Version](https://www.loopandlearn.org/compare-branches/#which-loop) webpage explains the differences between master and automatic-bolus. (Hint - if you build automatic-bolus, it acts just like master until you modify the Dosing Strategy selection under Settings.  So you can switch back and forth between master, Temp Basal only, and automatic-bolus strategies without a rebuild.)

Click on one of the links below to download Loop code and then follow the rest of the steps until you have a new version on your device. (These links always point to the most recent version of the code.)

---

- [Loop: master branch](https://github.com/LoopKit/Loop/archive/master.zip)

- [Loop: automatic-bolus branch](https://github.com/LoopKit/Loop/archive/automatic-bolus.zip)

---

!!! warning "Advanced Users Only"

    **Only build the dev branch if you're a developer/advanced user**

    - Note, the dev branch requires a minimum of iOS 14 on your device
    - Once you install the dev branch on a device, you must delete the app to return to master or automatic-bolus, which means all settings will need to be entered and a new pod started
    - The dev branch user interface is different, i.e., the documentation in LoopDocs does not match the screens you will see when you use the Loop app built from the dev branch

    The dev branch requires using LoopWorkspace and requires installation of carthage 0.36.0 on your Mac.  The links below are to the wiki for LoopWorkspace, the LoopDocs page on building with LoopWorkspace and the instructions for installing carthage 0.36.0 (not needed for master or automatic-bolus branches)  


    * [LoopWorkspace wiki](https://github.com/LoopKit/LoopWorkspace#loopworkspace): Replace "<branch\>" in "git clone" line with "dev"

    * LoopDocs page on [LoopWorkspace](loopworkspace.md)

    * LoopDocs page, ["Skip Step 7"](step7.md) for installing carthage 0.36.0


---

## Store and Name Your Download Properly

It is best practice to leave your Loop code in your Downloads folder. If you store your Loop code in a different folder than Downloads (such as your Documents folder or Desktop), make sure the specified folder is **not** an iCloud drive. Storing your Loop code in an iCloud drive folder will prevent Loop from building successfully.  How do you know if a folder is an iCloud drive? Check your System Preferences. If your System Preferences for iCloud is set as shown below, your Documents and Desktop folders are iCloud drives and **NOT** appropriate places to save your Loop download.

![img/icloud-drive.png](img/icloud-drive.png){width="650"}
{align="center"}

Depending on your browser and settings, your Loop download may or may not automatically unzip. If it does not unzip automatically, you can right-click on the zip file and choose to "Open With" Archive Utility. This will create a blue folder called `Loop-master`.  HOWEVER, if you already have an existing `Loop-master` folder from a previous download, the name of the next download will be something like `Loop-master (1)`.

## Next Step: Build Loop App

Now you are ready to move onto Step 14 to [Build Loop App](step14.md).
