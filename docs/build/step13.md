# Step 13: Download Loop Code

!!! danger "Time Estimate"
    - 10 minutes to read this page
    - 1 minute to download Loop code

!!! info "Summary"
    - Download the zip file from the master branch link below

!!! warning "FAQs"
    - **"What the heck is a branch?"** That's a great question. We have a page all about [Branch FAQs](../faqs/branch-faqs.md)
    - **"When do I need to download new Loop code?"** Anytime you want to update your Loop app to get new features, you'll simply download the code again by clicking on the links below. The links always go to the most recent version of each of the branches. It's a good idea is to delete your old downloads before making a new one, just to avoid confusion. If you're paranoid, rename the older folder old-loop and wait to delete it after you have a fresh new build on your phone.

## Download Loop

You’ll need to download the Loop code. You will then build the app on your computer with Xcode, which will transfer the app to your phone or ipod.

### Xcode 13, iOS 15 changes

!!! warning "DO NOT UPDATE your phone to iOS 15 without reading this"

    Any Loop app built with Xcode version prior to Xcode 12.5 runs the risk of their Loop app immediately failing when the phone is updated to iOS 15. (Any one who last built with Catalina should not install iOS 15 without following "safe steps" below.)

    If you don't know what version of Xcode was used to build your app, do NOT update to iOS 15.

    Safe steps to keep Loop going if you want to install iOS 15

    * update your macOS
    * update your Xcode to version 13
    * build the Loop app on your phone
    * update phone to iOS 15

Modifications to building Loop with Xcode 13:

* iOS 15 requires Xcode version 13 to build
* You must use the LoopWorkspace method to build the master branch with Xcode 13
* The old download the zip method will not work once you update your Xcode to version 13
* You can use the [Build Select Script](https://www.loopandlearn.org/build-select/) webpage, which has instructions on how to use a script to download Loop Master

### Xcode 12

If you are running Xcode version 12, suitable for iOS versions 14.x and earlier, you can still click on the master branch link below to download Loop code and then follow the rest of the steps until you have a new version on your device. (This link always points to the most recent version of the code.)

However, the [Build Select Script](https://www.loopandlearn.org/build-select/) is easy to use (just different) and gets you the same Loop app version built on your phone. It is still worth reading Step 14 but some of the steps are done for you by the script.

---

**WARNING** - Temporary issue with zip download build (Sep 25, 2021) - it will not build without errors

- [Loop: master branch](https://github.com/LoopKit/Loop/archive/master.zip)

---

If you are an experienced Looper who really wants to use the zip download now and not wait for this issue to be fixed, you can change the last line of the carthage.resolved file in the Loop-master directory. (This is only for Xcode 12 building onto iOS 14 or earlier devices.  Devices with iOS 15 must use Xcode 13 and must use the workspace build.)

Last line of `carthage.resolved` in the Loop-master folder should say:

`github "ps2/rileylink_ios" "15d19970f589d1678a486a9b7cfa2430111ee3ea"`


---

- [Advanced Users Only](#advanced-users-only)

---

!!! danger "What happened to the automatic-bolus branch?"
    - The automatic-bolus branch was retired when the Dosing Strategy feature became part of the master branch
    - Please check out [Branch FAQs for v2.2.6 and v2.2.5](../faqs/branch-faqs.md#loop-v226)


## Store and Name Your Download Properly

It is best practice to leave your Loop code in your Downloads folder. If you store your Loop code in a different folder than Downloads (such as your Documents folder or Desktop), make sure the specified folder is **not** an iCloud drive. Storing your Loop code in an iCloud drive folder will prevent Loop from building successfully.  How do you know if a folder is an iCloud drive? Check your System Preferences. If your System Preferences for iCloud is set as shown below, your Documents and Desktop folders are iCloud drives and **NOT** appropriate places to save your Loop download.

![img/icloud-drive.png](img/icloud-drive.png){width="650"}
{align="center"}

Depending on your browser and settings, your Loop download may or may not automatically unzip. If it does not unzip automatically, you can right-click on the zip file and choose to "Open With" Archive Utility. This will create a blue folder called `Loop-master`.  HOWEVER, if you already have an existing `Loop-master` folder from a previous download, the name of the next download will be something like `Loop-master (1)`.

## Next Step: Build Loop App

Now you are ready to move onto Step 14 to [Build Loop App](step14.md).

## Advanced Users Only

If you are an advanced user who wants to build the dev branch - this section is for you.

!!! warning "Advanced Users Only"

    **Only build the dev branch if you're a developer/advanced user**

    Please read [What's going on in the dev branch?](../faqs/branch-faqs.md#whats-going-on-in-the-dev-branch) before deciding to test the dev branch.

    - Note, the dev branch requires a minimum of iOS 14 on your device
    - Once you install the dev branch on a device, you must delete the app to return to master or automatic-bolus, which means all settings will need to be entered and a new pod started
    - The dev branch user interface is different, i.e., the documentation in LoopDocs does not always match the screens you will see when you use the Loop app built from the dev branch
    - [Loop dev Preview](../faqs/dev-menus.md) is found in the FAQs section with some preliminary documentation

    The dev branch requires using LoopWorkspace and requires installation of carthage 0.36.0 on your Mac.  The links below are to the wiki for LoopWorkspace, the LoopDocs page on building with LoopWorkspace and the instructions for installing carthage 0.36.0 (not needed for master or automatic-bolus branches)  


    * [LoopWorkspace README](https://github.com/LoopKit/LoopWorkspace#readme): Replace "<branch\>" in "git clone" line with "dev"

    * LoopDocs page on [LoopWorkspace](loopworkspace.md)

    * LoopDocs page, ["Skip Step 7"](step7.md) for installing carthage 0.36.0

    New trick (dev branch only):

    * Edit the LoopConfigOverride.xcconfig
    * Uncomment the line starting with `LOOP_DEVELOPMENT_TEAM = `
    * Insert your developer ID
    * Build the Loop(Workspace) - all targets are signed automatically
