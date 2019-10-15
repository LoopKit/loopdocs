# Setup Remote Overrides

!!!warning "PLEASE READ"
    Remote overrides in Loop is in its initial testing. **This is by no means bug-free.** If you choose to do this, there are some special setup steps for deploying a special branch of Nightscout and using a testing branch of Loop called "remote-overrides". If you do not feel you are capable of doing these special steps right now, please wait until some more testing is done by others. This page is created only to help answer questions in bulk...NOT AS AN ANNOUNCEMENT THAT REMOTE OVERRIDES IS PRIME-TIME READY. REPEAT: This is still an initial testing branch...if things work out though, the only part of these directions that will change is Step 3: Update Nightscout Site will be slightly different procedure, but will still need to be done. You'd still need to update your Loop, you'd still need to create a key for Apple Push Notification services.

You can now use your Nightscout site to remotely set and cancel your override presets in your Loop app.

What?! Yes, really...you can set/cancel an override remotely for your child's Loop.

Here's the breaking information on this:

1. You will need to update your Loop app. 

2. You will need to create a Key for an Apple Push Notifications service (APNs)

3. You will then need to update your Nightscout site and add some "config vars" lines in your Heroku settings.

## Step 1: Updating Loop for remote-overrides

Remote overrides are in dev branch now (as of October 13th), so you'll have to update your Loop to use this upated dev branch if you want to get this feature working.  Be sure to review all the steps for updating your Loop app [here](https://loopkit.github.io/loopdocs/build/updating/).


## Step 2: Apple Push Notifications
The next part of this will help your Loop app give permissions to your Nightscout site to remotely interact with it.</br></br>
1. Login to your [Apple developer account](https://developer.apple.com/account/) with the Apple ID associated with your developer team that you used to sign your Loop app.</br></br>
2. Click on "Certificates, Indentifiers & Profiles" and then, on the next page, click on "Keys" (located on the left-hand column). Click on the blue "Create a new key" **OR** the "+" icon to add a new key. 

<p align="center">
<img src="https://loopkit.github.io/loopdocs/nightscout/img/apns-add-key.png" width="550">
</p> 
</br></br>
3. In the form that appears, click the checkbox for enabling "Apple Push Notifications service (APNs)" and enter a name for the key such as "Nightscout". Then click the "Continue" button in the upper right of the screen.

<p align="center">
<img src="https://loopkit.github.io/loopdocs/nightscout/img/key-apns.png" width="550">
</p> </br></br>
4. In the screen that follows, click the blue "Register" button.

<p align="center">
<img src="https://loopkit.github.io/loopdocs/nightscout/img/apns-register.png" width="550">
</p> </br></br>
5. In the screen that follows, click the blue "Download" button. This step will download a file with a name that starts with "AuthKey" and ends with ".p8".

<p align="center">
<img src="https://loopkit.github.io/loopdocs/nightscout/img/apns-download.png" width="550">
</p> </br></br>
6. Find your AuthKey download in your downloads folder. Double-click to open it and you will be presented a message asking how you'd like to open it. Click on "Choose Application..." and then select "TextEdit" as your application to open it with.

<p align="center">
<img src="https://loopkit.github.io/loopdocs/nightscout/img/apns-open.png" width="550">
</p> </br></br>

<p align="center">
<img src="https://loopkit.github.io/loopdocs/nightscout/img/apns-textedit.png" width="550">
</p> </br></br>
7. When the file opens, it will look similar to the screenshot below. In a few minutes, after we do a few other steps first, we will need to highlight **ALL OF THE CONTENTS** of that file and copy it because we will be pasting it in Heroku. Yes, allllll of the contents. So, easiest way is to click inside that file and then press `command-a` to highlight all the text and then `command-c` to copy it all to the clipboard. You don't have to do it right now...just keep that window open in the background for now until we need it a little further down. Then we will copy all that text.

<p align="center">
<img src="https://loopkit.github.io/loopdocs/nightscout/img/apns-copy-key.png" width="550">
</p> </br></br>

## Step 3: Update Nightscout site

This step may take some of you into uncomfortable territory just because it looks weird, but we need to use a special branch of Nightscout for now to test the remote overrides features. Eventually, this special branch should be merged into the regular Nightscout repository on GitHub, but for testing purposes it is separate for now. Just keep that in mind...this is a temporary situation. And these instructions will change when that merge happens...likely in a few days or so.

To get this new branch to your GitHub's cgm-remote-monitor, we need to do some special steps. 

!!!danger "Terminal and passwords"
    At some point in this process, you may be asked for your GitHub login information if you have never cloned to your computer before. Terminal app does not show your keystrokes when you type your password but it is logging them. So just keep typing even though you won't see the evidence of typing. Secondly, if you have two factor authentication turned on in Github, you will need to use your personal access token rather than your github password when you enter your "password" in Terminal. Yes, that's not obvious...agreed.

1. Open Terminal app in your computer and enter this command, **replacing "your-account" with your actual account name**: `cd && git clone https://github.com/your-account/cgm-remote-monitor.git`  This command makes a copy of your GitHub repository onto your computer's root directory.  **Note:** This is your GitHub account name.  Be sure to include that, not your Heroku account name.

2. Next command is `cd cgm-remote-monitor`  This command changes into the directory we just cloned ont your computer.

3. Next command is `git fetch https://github.com/ps2/cgm-remote-monitor remote-loop-overrides:remote-loop-overrides`  This command grabs a copy of Pete's test branch of Nightscout, called remote-loop-overrides, that we will need to use.

4. Next command is `git checkout remote-loop-overrides`  This command switches the local clone to the new branch.

5. Next command is `git push --set-upstream origin remote-loop-overrides`  This command will push your new branch up to your online GitHub account so we can use it in Heroku.

6. [Login to your Heroku account](https://id.heroku.com/login),  Find your "Deploy" tab and click it. Now scroll to the very bottom of the page and find the Manual Deploy section. Choose "remote-loop-overrides" in the drop down menu of the branches and then press the black deploy button. (If you don't have a black deploy button...then click on the Github icon to connect to your Github account and cgm-remote-monitor repo.)

<p align="center">
<img src="https://loopkit.github.io/loopdocs/nightscout/img/deploy-remotes.png" width="750">
</p> </br></br>
7. Final step is to add the variables needed in Heroku settings. Select the `Settings` tab near the top of the screen on your Heroku app and then click on `Reveal Config Vars`.  

<p align="center">
<img src="../img/heroku5.png" width="650">
</p> </br></br>
Scroll down the bottom of the Config Vars lines until you find the last blank one.  You are going to add three new rows of config vars for remote overrides as shown below:

<p align="center">
<img src="../img/add_vars.jpg" width="650">
</p> 
<table>
<thead>
<tr>
<th>KEY</th>
<th>VALUE</th>
</tr>
</thead>
<tbody>
<tr>
<th>LOOP_APNS_KEY</th>
<td>enter ENTIRE contents of the downloaded .ps file including the BEGIN and END lines. Here's where you can use the `command-a` and `command-c` to hightlight and copy all the text in that file so you can paste it into Heroku here for this new variable you are creating.
<p align="center">
<img src="https://loopkit.github.io/loopdocs/nightscout/img/apns-copy-key2.png" width="550">
</p> </br></br></td>
</tr>
<tr>
<th>LOOP_APNS_KEY_ID</th>
<td>string of characters on the .ps download file immediately following the underscore (  _  ), or you can get it from your saved key in your developer account as shown next step, too
<p align="center">
<img src="https://loopkit.github.io/loopdocs/nightscout/img/apns-open2.png" width="550">
</p> </br></br>
</td>
</tr>
<tr>
<th>LOOP_DEVELOPER_TEAM_ID</th>
<td>get this value from Loop app signing or in your developer account's top right corner under your name
<p align="center">
<img src="https://loopkit.github.io/loopdocs/nightscout/img/apns-vars.png" width="750">
</p> </br></br>
</td>
</tr>
</tbody>
</table>

When executed properly, you should have something that looks like this for your three new variables that you added:

<p align="center">
<img src="https://loopkit.github.io/loopdocs/nightscout/img/override_vars_complete.png" width="650">
</p> </br></br>

## Step 4: FAQs on Remote Overrides

Don't forget to read Loopdocs pages about how regular overrides work. For remote overrides in particular:

1. **Can I set different override in Nighscout than I have programmed into Loop app?** Answer: No. You will only be able to enact override presets already programmed into the Loop app.
2. **If I didn't start the override in Nightscout (it was started in Loop itself), can I still use Nightscout to cancel it?** Answer: Yes. You can cancel a Loop-set override with a Nightscout-set cancel "temporary override" command in careportal.
3. **"Can I override a Loop-set override with a Nightscout-set override?"** Answer: Yes. 
3. **If I have multiple Nightscout sites because I have multiple kiddos with T1D looping, do I need multiple APNs Keys?** Answer: No. If you have multiple kids looping, you can use the one APNs key in each of their Nightscout sites. 
4. **What if I see glitches?** Answer: report it in Zulipchat for now [here](https://loop.zulipchat.com/#narrow/stream/144182-development/topic/Remote.20overrides), but do be aware that Nightscout still needs some work. In particular, sometimes the grey bars showing where an override is active can "leave a residue", even after you cancel them, until you refresh the display.
5. **How can I tell if it worked?** Answer: You should see your override pill in Nightscout, with the NEXT Loop cycle, reflecting that the desired override action took place. If you are near the Loop app, you should see the new override within less than 30 seconds or so.

## Step 5: Using Remote Overrides

There are three ways you can trigger your override presets remotely; careportal, Shortcuts, and IFTTT.

### Careportal
To use remote overrides, I'm assuming you've setup your Nightscout site according to the directions [here](https://loopkit.github.io/loopdocs/nightscout/new_user/#step-4-setup-your-heroku-nightscout-app) in Loopdocs. Especially the part about your ENABLE line including "override careportal loop" (in addition to other variables you'd be interested in). You'll also need to have your site authenticated so that your careportal is active to send remote overrides. You can authenticate your site by selecting the three horizontal lines in the upper right corner of your Nightscout site and scrolling to the bottom of the settings. There's an "authenicate" link at the very bottom. Once authenticated by entering your API Secret, then there will be a `+` in the upper right corner of your site. That is your careportal. Tap the careportal `+` and then scroll down in the "event type" menu to find "Temporary Override". Within there you will find all your Loop override presets already loaded for you.

<p align="center">
<img src="https://loopkit.github.io/loopdocs/nightscout/img/careportal-overrides.PNG" width="350">
</p> </br></br>

The Looper will see a banner notification that an override has been set (or canceled, as the case may be).

<p align="center">
<img src="https://loopkit.github.io/loopdocs/nightscout/img/override_notification.jpeg" width="550">
</p> </br></br>

Canceling an override through Nightscout careportal is as simple as selecting the event type "Temporary Override Cancel" and submitting. 

### Shortcuts
If you want to make your life SUPER AMAZING, check out using the iPhone's Shortcuts app. The Shortcuts app is for making little automations (like mini apps) that can integrate parts of your life. In this case, we've written a couple shortcuts for you that integrate Loop overrides with Nightscout. 

!!!info "Important note"
    Before you click that download below...save some trouble. Download the Shortcuts app if you don't have it yet and choose to run any shortcut from the Gallery. It can be the laundry timer...I don't care, just pick one and run it.  THEN go to download the shortcut of your choice below. The shortcuts that aren't run through the Gallery option are called "untrusted". And you need a slider in your iPhone to trust the "untrusted" shortcuts you would be downloading here. But...in lovely iOS glitch...that slider doesn't appear unless you've run a trusted shortcut first. So, run one now. Then you'll have the slider in iPhone Settings, Shortcuts app to turn "Allow Untrusted Shortcuts" on when you will see a message "This shortcut cannot be opened because your Shortcuts security system settings don't allow untrusted shortcuts."

Click these links on your iphone and you'll be prompted to download the premade shortcuts (assuming you open the links in Safari browser in iPhone):

[Loop Shortcut...includes Set Remote Override, Cancel Override, Loop Troubleshooting Tips, Quick Text options, Manual BG entry, Bookmarks to websites, etc.](https://www.icloud.com/shortcuts/9b3ec245bbe24dee846529a7c27d6ed1)

And if you want to save one click to get to these one functions more directly: these shortcuts are simplified to offer only one function:

[Set Remote Override only shortcut](https://www.icloud.com/shortcuts/d52d7aefb62b47c1b2e71d3724a3b5ab)

[Cancel Override only shortcut](https://www.icloud.com/shortcuts/27be8282bce3433b83b4751cd8c43f6e)

**A couple notes about these shortcuts:**

1. You will need iOS 13 on the phone you'd like to trigger these shortcuts from. Looper's phone can still be lower than iOS 13, but your phone as the shortcut user would need iOS 13.
2. You need to open those links in the Safari browser on your iPhone. When you do that click the button to get the shortcut. Then wait a bit, and the shortcut's inner guts will be there...scroll ALL the way down to the bottom to click the button to save the untrusted shortcut.
3. When you enter your Nightscout URL in the "URL" field of the Loop shortcut setup, make sure you don't include a trailing "/" or the API calls to Heroku will error out. 
4. When a remote override is set properly, you'll see an "ok" message displayed. If there is an error, you'll see an error message. Most errors will be that you have an API secret wrong (make sure there isn't a space at the end of you API Secret that you don't see) or you failed to do the steps to setup NS and update your Loop app as described in steps 1-3 above.
5. You can absolutely customize these bits and pieces within the shortcut. Change the text messages, change the links...totally up to you.


### IFTTT

If you want to walk uphill both ways in the snow carrying bags of uneven groceries, you can also set overrides remotely by [setting up IFTTT](https://loopkit.github.io/loopdocs/nightscout/ifttt/), too.

## Step 6: Known Issues

Just a brief mention so you are aware:

1. The override pill will display information about what override is currently active in the Looper's phone. BUT, there can be a slight delay as that information is only transmitted every 5 minutes at best (it is tied to Loop runs and Nightscout upload events in Loop). So, wait 5 minutes to see that the information has gone through a refresh cycle before assuming the override message failed to enact.
2. When you add a new override preset in Loop, that preset has to be uploaded to Nightscout before it will be available as a remote override. To trigger that upload, you can simply enact that new override for a few seconds and turn it off again. that will get the Nightscout upload going.
