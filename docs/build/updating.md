# How to Update Loop

When a new version of Loop is released, you can click [HERE](https://github.com/LoopKit/Loop/releases) to read what features or fixes were a part of the new release.  If you decide you'd like to update to the new version, your upgrade process will depend on how you initially installed Loop.

## Direct download
If you used a direct download of the .zip file from GitHub (aka Option 1 Super Easy), then you will simply do the same again.  

* Directly download the current version's zip file [HERE (for master branch)](https://github.com/LoopKit/Loop/archive/master.zip) or [HERE (for dev branch)](https://github.com/LoopKit/Loop/archive/dev.zip)

* Follow the guide for installation as you did before, beginning with the changing of the MAIN_APP_BUNDLE_IDENTIFIER.  If you wish to keep your existing Loop app's settings, then use the same MAIN_APP_BUNDLE_IDENTIFIER as you used in the first installation.  If you can't remember it, you can open your old folder on your computer and check what it was.  Or alternatively, open your Loop settings, open up the Issue Report and look for a line titled `appGroupName`.  

<p align="center">
<img src="../img/app_group_name.jpg" width="400">
</p>

* Make any customizations you are interested.

* Build Loop onto iPhone and you've completed your upgrade.  Your old Loop app will have been updated to the new version and your settings will carry forward to the new version.

## Xcode Source Control and GitHub git
If you used Clone with GitHub (Option 2 Sorta Easy) or GitHub Desktop (Option 3 Advanced), you will want to `cd` into your Loop repository on your local computer and `git pull https://github.com/LoopKit/Loop.git` to update your Loop repository.  Then you can navigate to the Loop.xcodeproj and update as described above.

