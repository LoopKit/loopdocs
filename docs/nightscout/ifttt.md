# IFTTT Integration

If This, Then That (IFTTT) is a useful Nightscout integration.  By using IFTTT, you can have single button presses that you can deploy from your iPhone to put a note in your NS site, enter low treatments, log a site change, or log a sensor change. 


## IFTTT Setup for phones

* First we need to gather one thing called your "hashed API Secret". In your internet browser, open a console window while viewing your Nightscout site.  Make sure you have "authenticated" your site by using your API secret in the Nightscout settings area (hint: if you see a little padlock in the upper left corner of the site, you haven't authenticated it).  Refresh the site and your hashed secret key will be shown as "apisecrethash: "xxxxxxxxxx...""  For Safari users on Mac, you can open the console window by selecting "Develop" from the Safari top menu, and then "Show Page Source" (if you do not see "Develop" in the top menu, activate it by going to Safari > Preferences... > Advanced, and checking the "Show Develop menu in menu bar" option).  If you're having problems seeing the apisecrethash, click the little grey triangle next to the "status isAuthenticated" line and the objects below it will display (see screenshot).  Your hashed API secret can be copied and pasted from that line, as shown below.  Save that somewhere easy to get to again, because you will be using it later.

<p align="center">
<img src="../img/hashed_API.png" width="550">
</p> 

* Get an [IFTTT account](https://ifttt.com/join) 

<p align="center">
<img src="../img/IFTTT_signup.png" width="550">
</p> 

* Login to your IFTTT.com account and select click [this link](https://ifttt.com/create) to get to the page for creating your first "New Applet". (You can also get to this Applet creation page by selecting your Account icon in the upper right of the IFTTT website, then clicking on "My Applets", then "Get More", then finally scroll down a bit and there's a ridiculously hidden button about a third fo the way down the page that says "Create your own"...it is insane how hard that button is to find now.)

<p align="center">
<img src="../img/IFTTT_newapplet.png" width="550">
</p> 

* In the screen that appears, click on the black "+this" part of the screen

<p align="center">
<img src="../img/IFTTT_this.png" width="550">
</p> 

* In the next screen, type "button" in the search field and then click on the red box labelled "ButtonWidget"

<p align="center">
<img src="../img/IFTTT_button.png" width="550">
</p> 

* Connect the button widget by clicking on the large black"connect" button twice, once on the main screen and then second on the pop-up window that will appear immediately after that. (You will only have to "connect" the widgets for the first applet you make.  After that the widgets will already connected to your IFTTT account.)

<p align="center">
<img src="../img/IFTTT_connect1.png" width="550">
</p> 

* Click on the large red "button press" box 

<p align="center">
<img src="../img/IFTTT_buttonpress.png" width="550">
</p> 

* Click on the black "+that" text

<p align="center">
<img src="../img/IFTTT_that.png" width="550">
</p> 

* Enter "Webhooks" in the search field and click on the Webhooks app

<p align="center">
<img src="../img/webhooks1.png" width="550">
</p> 

* Connect the Webhooks app

<p align="center">
<img src="../img/webhooks2.png" width="550">
</p> 

* Select the blue "Make a Web Request" box

<p align="center">
<img src="../img/webhooks24.png" width="550">
</p> 

*  Now you will have a blank web request template to complete.  Screenshot below is an example of a completed recipe for eating soon IFTTT action. There are four parts you will need to fill in, and they are described below the screenshot.

<p align="center">
<img src="../img/webhooks25.png" width="550">
</p> 

!!!danger "URL"
    `https://yoursite.herokuapp.com/api/v1/treatments.json` for all IFTTT recipes that are NOT remote overrides.</br></br>
    **NOTE: Remote overrides will use**</br> `https://yoursite/herokuapp.com/api/v2/notifications/loop`</br></br>
    Change the "yoursite" to your actual site's info.
    
!!!warning "Method"
    The method will be `POST`

!!!info "Content Type"
    The content type will be `application/json`. 

!!!danger "Body"
    The content of the body will depend on the action that you would like this particular button press to perform. While many recipes are available, any recipe that log carbs to NS will only display the carbs in Nightscout...Loop will not "use" those carbs in treatment or prediction math. The display of carbs in NS though may still be helpful for remote care givers to leave an indication that a low is being noticed and treated.  Some sample content for actions that may be useful in Loop:</br></br>
    **Pump Site Change**</br>
    {"enteredBy": "IFTTT-button", "eventType": "Site Change", "duration": 0, "secret": "your_hashed_api_goes_here!!!"}</br></br>
    **CGM Sensor Start**</br>
    {"enteredBy": "IFTTT-button", "eventType": "Sensor Start", "duration": 0, "secret": "your_hashed_api_goes_here!!!"}</br></br>
    **Note**</br>
    {"enteredBy": "IFTTT-button", "eventType": "Note", "notes": "Hi mom, please don't text me for a bit.  I'm taking a test.", "secret": "your_hashed_api_goes_here!!!"}</br></br>

!!!warning "Remote Override body messages"
     special note about remote overrides and IFTTTT. You could also set overrides in NS using IFTTT, assuming you have followed [the directions for setting up remote overrides](https://loopkit.github.io/loopdocs/nightscout/remote-overrides/). To setup the overrides, you need to match the Body message of the applet with the override already programmed in Loop app. A sample body message would be as follows. Notice how the duration is giving in minutes, and if the override is one that is "enabled indefinitely" then the duration is "infinite". The reason is the name of the override but NO EMOJI, and the reasonDisplay is the override name with the emoji.</br></br>
    **Override named "hormones"**</br>
    {"enteredBy": "IFTTT-button", "eventType": "Temporary Override", "reason": "hormones", "duration": "infinite", "reasonDisplay": "🧟‍♀️ hormones", "secret": "your_hashed_api_goes_here!!!"}</br></br>
    **Override named "running"**</br>
    {"enteredBy": "IFTTT-button", "eventType": "Temporary Override", "reason": "running", "duration": "180", "reasonDisplay": "🏃‍♀️ running", "secret": "your_hashed_api_goes_here!!!"}
    **Override named "Low Treatment"**</br>
    {"enteredBy": "IFTTT-button", "eventType": "Temporary Override", "reason": "Low Treatment", "duration": "60", "reasonDisplay": "🍬 Low Treatment", "secret": "your_hashed_api_goes_here!!!"}


* Click the `Create Action` button on the bottom of the screen when you finish.

* Now is your chance to change the title of your applet now to something meaningful.  You can turn on notifications, too, using the slider shown. If you turn on the notifications, you will get an alert on your phone and pebble watch when the button press has been successfully deployed.  Finish the IFTTT button by clicking on the Finish button that appears.  

<p align="center">
<img src="../img/webhooks26.png" width="550">
</p> 

* Repeat the setup for new applets for as many automated actions/overrides as you would like to setup.

<p align="center">
<img src="../img/webhooks27.png" width="550">
</p>

## Enable IFTTT in your Nightscout site

* Find your Maker Key by going to your IFTTT account, Services and then click on the Webhooks service, settings.

<p align="center">
<img src="../img/webhooks9.png" width="550">
</p> 
********
<p align="center">
<img src="../img/webhooks10.png" width="550">
</p> 

* You will see your Maker Key as the last part of the URL; copy and paste that last part (the red circled part as shown)

<p align="center">
<img src="../img/webhooks11.png" width="550">
</p> 

* Login to your Nightscout site host (azure or heroku) and (1) add your Maker Key to the MAKER_KEY line and (2) add "maker" to your ENABLE line.

<p align="center">
<img src="../img/IFTTT_NSkey.png" width="550">
</p> 

<p align="center">
<img src="../img/IFTTT_enable.png" width="550">
</p> 

## Install IFTTT app on your iPhone/Android

* Download the IFTTT app on your phone and log in.

* You can add homescreen quick buttons.  Click on your IFTTT app and login, click on My Applets in the bottom right corner, and then click on the applet that you'd like to work with.  From the the middle of the applet, click on the Widget Settings, and then click on the Add button for the Homescreen Icon.

<p align="center">
<img src="../img/IFTTT_homescreen.PNG" width="550">
</p> 

* For iPhone users, if you downswipe from the top of your iPhone screen, you will have the Today view or Notifications showing.  They are separate pages; Today view is on the left, Notifications is on the right.  You can left/right swipe to go between them.  Go into the Today view and scroll to the bottom, click "edit". This should show a list of existing widgets, followed by a list of "more widgets" with green + signs.  Click on the IFTTT's green circle and the widget will be moved to the top, active widgets area.  You can hold your finger on the three left lines of the IFTTT widget row to drag it to the top of your widget panel, if you prefer to have it as the top-most widget. 

<p align="center">
<img src="../img/IFTTT_today.PNG" width="550">
</p> 

If you end up with more than four IFTTT applets, they will appear in reverse-order of when they were created...which may not be the same as you'd prefer them to appear on your widget bar.  If you'd like to reorder them:

  * go into your iPhone's IFTTT app
  * click on My Applets
  * click on the gear icon in upper left of screen
  * click on Widgets
  * click on the pencil icon in upper right of screen
  * click and hold the three lines that appear on the right side of the widget that you want to move.  Drag the widget to the order in the list that you'd like it to appear in your widget quickscreen.

<p align="center">
<img src="../img/IFTTT_reorder.png" width="550">
</p> 

## Alexa integration
* Since you have IFTTT/Maker requests working, you can get it to work with anything that supports IFTTT, including Alexa. You will need to add "alexa" to your ENABLE line in your Nightscout host settings (azure) or config vars (heroku).  And then repeat the steps above, but instead of using "ButtonWidget" service we started with earlier (the "+if" part of the setup)...you will use the "AmazonAlexa" service.

<p align="center">
<img src="../img/alexa_maker.png" width="550">
</p> 

  * Alexa requests do not need underscores, FYI.
