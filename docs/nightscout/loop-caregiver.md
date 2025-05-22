## The *LoopCaregiver* App  ![icon for *LoopCaregiver* app](img/lcg-icon.jpg){width="50"}

The *LoopCaregiver* app is under development to make remote commands easier to implement and monitor.

### Minimum Requirements:

* _<span translate="no">Loop</span>_&nbsp;version 3.3 or newer
* iOS 16 or newer for *LoopCaregiver* phone
* *Nightscout* version 14.2.6

### Prerequisites:

* Complete all 4 steps on the [Remote Configuration](remote-config.md) page:
    * [Step 1: Update the Looper's iPhone settings](remote-config.md#step-1-update-the-loopers-iphone-settings)
    * [Step 2: Apple Push Notifications](remote-config.md#step-2-apple-push-notifications)
    * [Step 3: Add APN to Nightscout](remote-config.md#step-3-add-apn-to-nightscout)
    * [Step 4: Test Remote Overrides](remote-config.md#step-4-test-remote-overrides)
* Read the [Remote Commands](remote-commands.md) page and pay special attention to these 2 sections
    * [FAQs on Remote Overrides](remote-commands.md#faqs-on-remote-overrides)
    * [Warnings on Remote Commands](remote-commands.md#warnings-on-remote-commands)

!!! warning "Older *Nightscout* Versions"
    If you ignore this minimum version requirement - what happens:

    * If you attempt to use the carb entry in the past or future, the *caregiver* app accepts it but the remote commands accepted by the Loopers phone show up at the current time - not when the caregiver intended to insert carbs
    * Please take the time to update your *Nightscout* site to `master`
    * *Nightscout* 14.2.6 was released 30-Sep-2022 as `Classic Liquorice`

If you use *LoopCaregiver*, please join [*LoopCaregiver* App](https://loop.zulipchat.com/#narrow/stream/358458-Loop-Caregiver-App) *Zulipchat* stream.

**As with all development code, monitor *Zulipchat* for announcements, report any problems you experience, be prepared to build frequently, and pay attention.**

## Build the *LoopCaregiver* App

You can build the *LoopCaregiver* app using the [Build with Browser](#build-with-browser) method or the [Build with *Mac*](#build-with-mac) method.

###  Build with Browser

The Build with Browser method is documented on the [Build Other Apps with Browser](../browser/other-apps.md) page.

### Build with *Mac*

A build script is available to assist in building *LoopCaregiver*. This should be straightforward for anyone who has previously built &nbsp;<span translate="no">Loop 3</span>&nbsp; using the script.

- Open a terminal window. 
- Spot the line below that starts with `/bin/bash`
- Click the gray copy button (:material-content-copy:) located near the bottom right side of that line  (should say `Copy to Clipboard` when you hover the mouse over it).  
  Once clicked, a confirmation message that says `Copied to Clipboard` will appear on your screen.
    ``` { .bash .copy  title="Copy and Paste to start the BuildLoopCaregiver script" }
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/loopandlearn/lnl-scripts/main/BuildLoopCaregiver.sh)"
    ```
- Important: Click anywhere in the terminal before trying to paste
- Paste the line into the Terminal window.  
    - on Mac, you can do this in one of the following ways:
        - Press ++command+"V"++ 
        - or Press ++control+++click and select `Paste` from the menu 
        - or select `Edit => Paste` (i.e. click the `Edit` menu at the top of the Mac screen then click `Paste`).
    - on PC (Virtual Mac): 
        - Press ++control+"V"++
- Once the line is pasted, hit Return (++return++) to execute the script. 
- The script displays the directions for downloading and building.    
    Please read them carefully.

!!! warning "Read Carefully"
    The output you see in the Terminal may look very similar to when you build the *Loop* app from a script.
    
    It is pulling down a clone from a different location (`LoopKit/LoopCaregiver`). It uses some modules from `Loop`. The target and scheme are automatically selected for `LoopCaregiver`  and if you follow directions for a paid Developer account, the signing is automatic.

## Use the *LoopCaregiver* App

Some limited directions for using the *LoopCaregiver* app are provided - please also read the *Zulipchat* stream to stay up-to-date with improvements - especially if you are using a development branch of &nbsp;_<span translate="no">Loop</span>_.

### Add Looper to the *LoopCaregiver* App

You must add a Looper to continue with the *LoopCaregiver* app as shown in the graphic below.

![add Looper to LoopCaregiver](img/lcg-add-looper.png){width="300"}
{align="center"}

* On the&nbsp;_<span translate="no">Loop</span>_&nbsp;phone:
    * Tap on `Loop -> Settings -> Services -> Nightscout`
    * Tap on the `One-Time-Password` row to see the QR code  
    !!! tip "Pro-tip"
        Take a screenshot of the QR code and store it on your computer.
        
        You can then add the QR code to *LoopCaregiver*  without bothering your Looper.

        * Keep the screenshot secure
        * Do not share the QR screenshot when asking for help

* On the *LoopCaregiver* phone:
    * Tap on *LoopCaregiver* -> `Settings`
    * Enter the name of the Looper, the *Nightscout* URL (use &nbsp;<span translate="no"> http**s**://</span>&nbsp;) and `API_SECRET`
    * Touch the QR code row - this opens the camera - point the camera at the QR code from Looper's phone

You can add additional more people under settings. (**LoopCaregiver* * can monitor more than one Looper).

### Main Screen of the *LoopCaregiver* App

* *LoopCaregiver* uses a lot of features from&nbsp;_<span translate="no">Loop</span>_&nbsp;with some Nightscout-like features in the Timeline.

The Timeline:

* Autoscales the vertical display for glucose reported over the last 24 hours (plus the forecast if that is turned on)
    * `Show Prediction` for Timeline is turned off in the graphic below.
* Horizontal display can be adjusted using the dropdown hours selector and scrolling left/right.
* A double tap on the Timeline alternates between 1 and 6 hour display

![main screen of the *LoopCaregiver* app](img/lcg-main.jpg){width="300"}
{align="center"}


You can also use the *LoopCaregiver* -> `Settings` screen to modify:

* Units used for glucose display: `mg/dL` or `mmol/L`
* Include the&nbsp;_<span translate="no">Loop</span>_&nbsp;forecast display on the Timeline chart as well as the Glucose chart of the main display (`Show Prediction` is turned off in the graphic above)

### Issue Remote Commands with the *LoopCaregiver* App

You issue override, carb, and bolus commands using a toolbar similar to the one seen on&nbsp;_<span translate="no">Loop</span>_. In the example graphic above, the carb and bolus entries visible were issued remotely.

Carb and bolus commands each require authorization before they are accepted. The authorization (*FaceID*, Fingerprint, or passcode) matches that required to unlock the *LoopCaregiver* &#39;s phone.

The use of *LoopCaregiver* makes remote commands much easier and more reliable.

Go back and review the details about [Remote Commands](remote-commands.md) before using the app.

### Troubleshooting

Troubleshooting steps are found on the [Remote Errors](remote-errors.md) page.