## <span translate="no">Loop Caregiver</span>&nbsp;   ![icon for &nbsp;<span translate="no">Loop Caregiver</span>&nbsp; app](img/lcg-icon.jpg){width="50"}

The &nbsp;<span translate="no">Loop Caregiver</span>&nbsp; app is under development to make remote commands easier to implement and monitor.

### Minimum Requirements:

* <span translate="no">Loop</span>&nbsp; version 3.2.0 or newer
    * version 3.0 works but is not recommended for other reasons
    * version 3.3 and higher offers improved feedback to the &nbsp;<span translate="no">Loop Caregiver</span>&nbsp; user
* iOS 16 or newer for &nbsp;<span translate="no">Loop Caregiver</span>&nbsp;&#39;s phone
* iOS 15.1 with *Loop* 3 for Looper&#39;s phone
* <span translate="no">Nightscout</span>&nbsp; version 14.2.6

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

If you use &nbsp;<span translate="no">Loop Caregiver</span>, please join &nbsp;[<span translate="no">Loop Caregiver App</span>](https://loop.zulipchat.com/#narrow/stream/358458-Loop-Caregiver-App) *Zulipchat* stream.

**As with all development code, monitor *Zulipchat* for announcements, report any problems you experience, be prepared to build frequently, and pay attention.**

## Build &nbsp;<span translate="no">Loop Caregiver</span>

You can build &nbsp;<span translate="no">Loop Caregiver</span>&nbsp; using the &nbsp;<span translate="no">GitHub Browser Build</span>&nbsp; method or the &nbsp;[<span translate="no">Mac-Xcode Build</span>](#mac-xcode-build) method.

### GitHub Browser Build:

The &nbsp;<span translate="no">GitHub Browser Build</span>&nbsp; method is documented on the [Other Apps](../gh-actions/gh-other-apps.md) page.

### Mac-Xcode Build:

A build script is available to assist in building &nbsp;<span translate="no">Loop Caregiver</span>. This should be straightforward for anyone who has previously built &nbsp;<span translate="no">Loop 3</span>&nbsp; using the script.

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

!!! warning "Not &nbsp;_<span translate="no">Loop</span>_"
    The output you see in the Terminal may look very similar to when you build &nbsp;_<span translate="no">Loop 3</span>_&nbsp; from a script.
    
    It is pulling down a clone from a different location (<span translate="no">LoopKit/LoopCaregiver</span>&nbsp;). It uses some modules from *Loop*. The target and scheme are automatically selected for *&nbsp;<span translate="no">Loop Caregiver</span>&nbsp;* and if you follow directions for a paid Developer account, the signing is automatic.

## Use &nbsp;<span translate="no">Loop Caregiver</span>

Some limited directions for using the &nbsp;<span translate="no">Loop Caregiver</span>&nbsp; app are provided - please also read the *Zulipchat* stream to stay up-to-date with improvements - especially if you are using a development branch of &nbsp;<span translate="no">Loop</span>.

### <span translate="no">Loop Caregiver</span>&nbsp; Add Looper

You must add a Looper to continue with &nbsp;<span translate="no">Loop Caregiver</span>&nbsp; as shown in the graphic below.

![add Looper to Loop Caregiver](img/lcg-add-looper.png){width="300"}
{align="center"}

* On the Looper&#39;s phone:
    * Tap on `Loop -> Settings -> Services -> Nightscout`
    * Tap on the `One-Time-Password` row to see the QR code  
    !!! tip "Pro-tip"
        Take a screenshot of the QR code and store it on your computer.
        
        You can then add the QR code to *&nbsp;<span translate="no">Loop Caregiver</span>&nbsp;* without bothering your Looper.

        * Keep the screenshot secure
        * Do not share the QR screenshot when asking for help

* On the &nbsp;<span translate="no">Loop Caregiver</span>&nbsp;&#39;s phone:
    * Tap on &nbsp;<span translate="no">Loop Caregiver</span>&nbsp; -> `Settings`
    * Enter the name of the Looper, the *Nightscout* URL (use &nbsp;<span translate="no"> http**s**://</span>&nbsp;) and `API_SECRET`
    * Touch the QR code row - this opens the camera - point the camera at the QR code from Looper's phone

You can add additional Looper's under settings. (*<span translate="no">Loop Caregiver</span>&nbsp;* can monitor more than one Looper).

### <span translate="no">Loop Caregiver</span>&nbsp; Main Screen

*&nbsp;<span translate="no">Loop Caregiver</span>&nbsp;* uses a lot of features from *Loop* with some Nightscout-like features in the Timeline.

The Timeline:

* Autoscales the vertical display for glucose reported over the last 24 hours (plus the forecast if that is turned on)
    * `Show Prediction` for Timeline is turned off in the graphic below.
* Horizontal display can be adjusted using the dropdown hours selector and scrolling left/right.
* A double tap on the Timeline alternates between 1 and 6 hour display

![main screen of the &nbsp;<span translate="no">Loop Caregiver</span>&nbsp; app](img/lcg-main.jpg){width="300"}
{align="center"}


You can also use the &nbsp;<span translate="no">Loop Caregiver</span>&nbsp; -> `Settings` screen to modify:

* Units used for glucose display: `mg/dL` or `mmol/L`
* Include the &nbsp;*&nbsp;<span translate="no">Loop</span>&nbsp;* forecast display on the Timeline chart as well as the Glucose chart of the main display (`Show Prediction` is turned off in the graphic above)

### Issue Remote Commands with &nbsp;<span translate="no">Loop Caregiver</span>

You issue override, carb, and bolus commands using a toolbar similar to the one seen on *Loop*. In the example graphic above, the carb and bolus entries visible were issued remotely.

Carb and bolus commands each require authorization before they are accepted. The authorization (*FaceID*, Fingerprint, or passcode) matches that required to unlock the &nbsp;<span translate="no">Loop Caregiver</span>&nbsp;&#39;s phone.

The use of *&nbsp;<span translate="no">Loop Caregiver</span>&nbsp;* makes remote commands much easier and more reliable.

Go back and review the details about [Remote Commands](remote-commands.md) before using the app.

### Troubleshooting

Troubleshooting steps are found on the [Remote Errors](remote-errors.md) page.