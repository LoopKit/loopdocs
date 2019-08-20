# Step 12: Download Loop code

You’ll need to download the Loop code in order to build the app on your computer.  Click on ONE of the links below to download your Loop source code.  Wondering which to choose? Read the discussion below

</br></br>
<p align="center">
[Loop: Master branch](https://github.com/LoopKit/Loop/archive/master.zip)</br></br>
[Loop: Dev branch](https://github.com/LoopKit/Loop/archive/dev.zip)</br></br>
[Loop: Omnipod-testing branch](https://github.com/LoopKit/Loop/archive/omnipod-testing.zip)
</p></br>

## Loop Branches
Master vs Dev?  What is the difference? The Loop code resides in a website called [GitHub](https://github.com/LoopKit/Loop). The various projects in GitHub use "repositories". A repository is kind of like a project's bookshelf, holding various books versions (aka branches) of a project. The master branch is considered a stable version of the project. Any new features or options are first tested in a public feature branch or dev (short for "development") branch of the Loop. If you hear of "new features" being tested, these are things that may be eventually merged into the master branch once any bugs are worked out. If you are choosing to use a testing branch, such as dev or omnipod, please be prepared to update you Loop app to get bug fixes as they are released. 

**Omnipod support in Loop is considered experimental and in-development. If you want to build a version of Loop that supports Omnipod, you will need to select the Omnipod-testing branch download above.** Keep in mind, dev branch represents a greater likelihood of encountering bugs or glitches. As you encounter those, please check the docs first to see if that issue is already answered. If you think you truly are seeing strange behavior, report the bug to Loop's GitHub by [creating a "New Issue" here](https://github.com/loopkit/loop/issues). You can also look through the list of known issues already reported, as there is a chance your issue has already been seen by others.


!!!inote "HELPFUL TIP"
    Best practice is to leave your Loop code in your Downloads folder.  If you store your Loop code in a different folder than Downloads (such as your Documents folder or Desktop), make sure the specified folder is **not** an iCloud drive.  Storing your Loop code in an iCloud drive folder will prevent Loop from building successfully.  How do you know if a folder is an iCloud drive?  Check your System Preferences.  If your System Preferences for iCloud is set as shown below, your Documents and Desktop folders are iCloud drives and **NOT** appropriate places to save your Loop download.
    <p align="center">
    <img src="../img/icloud-drive.png" width="650">
    </p></br>

    Depending on your browser and settings, your Loop download may or may not automatically unzip.  If it does not unzip automatically, you can right-click on the zip file and choose to "Open With" Archive Utility.  This will create a blue folder called `Loop-master`.  HOWEVER, if you already have an existing `Loop-master` folder from a previous download, the name of the next download will be something like `Loop-master (1)`.  The problem with that folder name is that it contains a space...and spaces in the name will cause your Loop build to fail.  So, either delete old copies of Loop before downloading/unzipping or rename the folder(s) to ensure that NO SPACES are in the folder name.
    <p align="center">
    <img src="../img/folder-name.png" width="650">
    </p>


