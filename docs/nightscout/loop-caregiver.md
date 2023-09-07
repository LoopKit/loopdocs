## <span translate="no">Loop Caregiver</span>   ![icon for <span translate="no">Loop Caregiver</span> app](img/lcg-icon.jpg){width="50"}

The *<span translate="no">Loop Caregiver</span>* app is under development to make remote commands easier to implement and monitor.

* Minimum Requirements
    * iOS 16 for <span translate="no">Loop Caregiver</span>&#39;s phone
    * iOS 15.1 with *Loop* 3 for Looper&#39;s phone
    * *<span translate="no">Nightscout</span>* 14.2.6
* Complete all 3 steps on the [Remote Configuration](remote-config.md) page:
    * [Step 1: Update the Looper's iPhone settings](remote-config.md#step-1-update-the-loopers-iphone-settings)
    * [Step 2: Apple Push Notifications](remote-config.md#step-2-apple-push-notifications)
    * [Step 3: Add APN to Nightscout](remote-config.md#step-3-add-apn-to-nightscout)
* Safety First - Read these 2 sections again
    * [FAQs on Remote Overrides](remote-commands.md#faqs-on-remote-overview)
    * [Warnings for Remote Commands](remote-commands.md#warnings-for-remote-commands)

!!! warning "Older *Nightscout* Versions"
    If you ignore this minimum version requirement - what happens:

    * If you attempt to use the carb entry in the past or future, the *caregiver* app accepts it but the remote commands accepted by the Loopers phone show up at the current time - not when the caregiver intended to insert carbs
    * Please take the time to update your *Nightscout* site to `master`
    * *Nightscout* 14.2.6 was released 30-Sep-2022 as `Classic Liquorice`

If you plan to use *<span translate="no">Loop Caregiver</span>*, please join [Loop Caregiver App](https://loop.zulipchat.com/#narrow/stream/358458-Loop-Caregiver-App) *Zulipchat* stream.

**As with all development code, monitor *Zulipchat* for announcements, report any problems you experience, be prepared to build frequently, and pay attention.**

## Build *<span translate="no">Loop Caregiver</span>*

A build script is available to assist in building *<span translate="no">Loop Caregiver</span>*. This should be straightforward for anyone who has previously built &nbsp;*<span translate="no">Loop 3</span>*&nbsp; using the script. You may also choose to build it with the GitHub build method as documented on the Browser Build: [Other Apps](../gh-actions/gh-other-apps.md) page.

- Open a terminal window. 
- Spot the line below that starts with `/bin/bash`
- Click the gray copy button (:material-content-copy:) located near the bottom right side of that line  (should say `Copy to Clipboard` when you hover the mouse over it).  
  Once clicked, a confirmation message that says `Copied to Clipboard` will appear on your screen.
    ``` { .bash .copy  title="Copy and Paste to start the Build<span translate="no">Loop Caregiver</span>.sh script" }
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/loopandlearn/lnl-scripts/main/Build<span translate="no">Loop Caregiver</span>.sh)"
    ```
- Important: Click anywhere in the terminal before trying to paste
- Paste the line into the Terminal window.  
    - on Mac, you can do this in one of the following ways:
        - Press ++command+"V"++ 
        - or Press ++control+++click and select `Paste` from the menu 
        - or select `Edit => Paste` (i.e. click the `Edit` menu at the top of the Mac screen then click `Paste`).
    - on PC: 
        - Press ++control+"V"++
- Once the line is pasted, hit Return (++return++) to execute the script. 
- The script displays the directions for downloading and building.    
    Please read them carefully.

!!! warning "Not &nbsp;*<span translate="no">Loop</span>*"
    The output you see in the Terminal may look very similar to when you build &nbsp;*<span translate="no">Loop 3</span>*&nbsp; from a script.
    
    It is pulling down a clone from a different location (<span translate="no">LoopKit/Loop Caregiver</span>). It uses some modules from *Loop*. The target and scheme are automatically selected for *<span translate="no">Loop Caregiver</span>* and if you follow directions for a paid Developer account, the signing is automatic.

## Use *<span translate="no">Loop Caregiver</span>*

Some limited directions for using the *<span translate="no">Loop Caregiver</span>* app are provided - please also read the *Zulipchat* stream.

### *<span translate="no">Loop Caregiver</span>*&nbsp; Main Screen

*<span translate="no">Loop Caregiver</span>* uses a lot of features from *Loop* with some Nightscout-like features in the Timeline.

The Timeline:

* Autoscales the vertical display for glucose reported over the last 24 hours (plus the forecast if that is turned on)
    * `Show Prediction` for Timeline is turned off in the graphic below.
* Horizontal display can be adjusted with spreading/pinching and scrolling.
* A double tap on the Timeline provides a factor of 2 expansion horizontally if at default
* A double tap on the Timeline returns the display to default if expanded


![main screen of the <span translate="no">Loop Caregiver</span> app](img/lcg-main.jpg){width="300"}

### Add a *Looper* to *<span translate="no">Loop Caregiver</span>*

You add each Looper under settings. (*<span translate="no">Loop Caregiver</span>* can monitor more than one Looper).

* On the Looper&#39; phone:
    * Tap on `Loop -> Settings -> Services -> Nightscout`
    * Tap on the `One-Time-Password` row to see the QR code  
    * !!! tip "Pro-tip"
           Take a screenshot and store it on your computer.  
           You can then add view the QR code in *<span translate="no">Loop Caregiver</span>* without bothering your Looper.
* On the <span translate="no">Loop Caregiver</span>&#39; phone:
    * Tap on `<span translate="no">Loop Caregiver</span> -> Settings`
    * Tap on the plus sign :material-plus-thick: to add a Looper
    * Enter the name of the Looper, the *Nightscout* URL (use <span translate="no"> http**s**://</span>) and `API_SECRET`
    * Touch the QR code row - this opens the camera - point the camera at the QR code from Looper's phone

You can also use <span>the `<span translate="no">Loop Caregiver</span> -> Settings` screen</span> to modify:

* Units used for glucose display: `mg/dL` or `mmol/L`
* Include the &nbsp;*<span translate="no">Loop</span>* forecast display on the Timeline chart as well as the Glucose chart of the main display (`Show Prediction` is turned off in the graphic above)

### Issue Remote Commands with &nbsp;*<span translate="no">Loop Caregiver</span>*

You issue override, carb, and bolus commands using a toolbar similar to the one seen on *Loop*. In the example graphic above, the carb and bolus entries visible were issued remotely.

Carb and bolus commands each require authorization before they are accepted. The authorization (*FaceID*, Fingerprint, or passcode) matches that required to unlock the <span translate="no">Loop Caregiver</span>&#39;s phone.

The use of *<span translate="no">Loop Caregiver</span>* makes remote commands much easier and more reliable.

Go back and review the details about [Remote Commands](remote-commands.md) before using the app.


