# Code Customizations

Based on Loop users’ experience, there are some customizations that you may want to incorporate ahead of building your Loop app and Apple Watch app.  These customizations must be done prior to building the Loop app onto your iPhone, they cannot be done from within the app itself.

!!!info "Line numbers may change"
    Every effort will be made to update the line numbers as the code is updated, but there may be times where the screenshots and line numbers differ from the current version of Loop code. These instructions have been updated for Loop v2.2.4 master branch. If you don't see an exact match on the line number listed, then use the Xcode / Find / Find in Project (or Workspace) menu to search for a Keyword or Phrase shown in the associated line. If you cannot identify a line that looks exactly like the example - do not guess - go to your favorite social media group and ask for help.

## Disable Authentication for Bolusing

Depending on your iPhone preferences and model, you may have Face ID or Touch ID enabled.  Those security features will also be used to authenticate bolus delivery in Loop.  You can choose to disable authentication (i.e., not require Face ID, Touch ID, or passcode for bolusing) through the following code customization:

 Modify Line 529 in the Loop>>View Controllers>>BolusViewController.swift.  This is a perfect example of how line numbers might be different.  The screenshot below was taken with Loop v2.0 when the line number was 201; with v2.2.4, that same code is found at line 529. Add the `false &&` as shown in the screenshot below:

![img/custom-id.png](img/custom-id.png){width="750"}
{align="center"}

## Default Carb Absorption Times

![img/carb_screen.png](img/carb_screen.png){width="200"}

Loop’s default carb absorption times are based on the high, medium, and low glycemic index absorption curves presented in *Think Like A Pancreas* by Gary Scheiner.  Currently the lollipop (fast) icon is set for 2 hours, taco (medium) icon for 3 hours, and pizza (slow) icon for 4 hours.  

If you would like to modify those defaults, you can do so in the Loop Core>>LoopSettings.swift Line 16.

![img/carb_times.png](img/carb_times.png){width="750"}
{align="center"}

For example, if you wanted to make lollipop a 30 minute absorption and pizza a 5 hour absorption, the edit would look like below:

![img/carb_times_example.png](img/carb_times_example.png){width="750"}
{align="center"}

## Exponential Insulin Curve

The Exponential Insulin Curve Models (Rapid-Acting Adult, Rapid-Acting Child, and Fiasp) default to an insulin duration of 360 minutes...but the peak activity of the various curves differs, as follows:

* Rapid-acting adult curve peaks at 75 minutes
* Rapid-acting child curve peaks at 65 minutes
* Fiasp peaks curve peaks at 55 minutes

If you wish to customize these values, you can adjust them on Lines 34-38 in the LoopCore>>Insulin>>ExponentialInsulinModelPreset.swift.

![img/exponential.png](img/exponential.png){width="750"}
{align="center"}

## Loop Logo

If you want an app logo other than the default green circle for your Loop app, you can easily customize this.  To make it easy to generate the correct sizes of icons, you can use a site like [appicon.build](http://www.appicon.build/) or [appicon.co](https://appicon.co/) and just drag and drop your source image. The source image needs to be 1024 pixels x 1024 pixels.  The site will email you a zip file or automatically download a set of files.  Highlight and copy the contents of the Appicon.appiconset that you are sent, including the Contents.json file

Now navigate to the corresponding Loop folder (DefaultAssessts.xcassets, Appicon.appiconset) as shown below.  

![img/appicon1.png](img/appicon1.png){width="650"}
{align="center"}

Replace the contents of the Appicon.appiconset with your copied images and Contents.json file.

![img/appicon2.png](img/appicon2.png){width="650"}
{align="center"}

You can confirm the successful change by looking in Xcode under Loop -> DefaultAssets.xcassets -> Appicon.  You should see your custom logo in the Appicon set now.  You may also see a yellow alert that there are “unassigned children” depending on the images the app icon generator tool produced. The unassigned children alert will not prevent your app from building, it’s simply because there are more more sizes of images than Loop app uses.  You can just leave the unassigned children alone (wow...how often do you get to say that phrase?).

![img/appicon3.png](img/appicon3.png){width="650"}
{align="center"}

And now you'll be the proud new owner of a custom Loop icon.

![img/unicorn-logo.jpeg](img/unicorn-logo.jpeg){width="350"}
{align="center"}

## Adjust the sensitivity of Watch's digital crown for carb and bolus entry

The rate of change of the carb and bolus entry pickers when using the digital crown can be altered. You'll need to edit two lines in files within the WatchApp Extension>>Controllers folder.  In BolusInterfaceController.swift edit line 191, and in AddCarbsInterfaceController.swift edit line 249. The 1/24 value is the ratio of rotations of the crown to the amount of change in the value. Changing it to 1/12 would mean that twice as many turns would be needed for the same amount of carb or bolus entry.

![img/sensitivity1.png](img/sensitivity1.png){width="800"}
{align="center"}

![img/sensitivity2.png](img/sensitivity2.png){width="800"}
{align="center"}
