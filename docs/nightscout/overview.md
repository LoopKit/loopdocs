## Overview

<span translate="no">Nightscout</span> is an excellent tool for remotely viewing <span translate="no">Loop</span> actions. <span translate="no">Nightscout</span> can act as a stand-alone tool or be integrated with <span translate="no">Loop</span>. (<span translate="no">Nightscout</span> also integrates with other open-source hybrid closed loop systems such as OpenAPS, AndroidAPS and iAPS. <span translate="no">LoopDocs</span> focuses on <span translate="no">Loop</span>.)

When integrated with <span translate="no">Loop</span>, <span translate="no">Nightscout</span> provides monitoring of <span translate="no">Loop</span> activities such as viewing history of glucose, carbs, boluses, temp basals and overrides; troubleshooting <span translate="no">Loop</span> errors; and provides extensive reports for analyzing data trends and patterns. These reports assist when <span translate="no">Loop Therapy Settings</span> need to be adjusted.

For caregivers, <span translate="no">Nightscout</span> enables remote monitoring and even the ability to issue remote commands through <span translate="no">Nightscout</span> when both <span translate="no">Loop</span> and <span translate="no">Nightscout</span> are properly configured. There are several pages starting at [<span translate="no">LoopDocs</span>: Remote Commands](remote-overview.md). If you are a caregiver, this summary of remote capabilities may encourage you to look into <span translate="no">Nightscout</span>.

!!! info "Remote Commands"
    * <span translate="no">Loop</span> 2.2.x
        * Overrides can be enabled and disabled
    * <span translate="no">Loop</span> 3
        * Overrides can be enabled and disabled
        * Carbs can be entered
        * Boluses can be commanded
        * <span translate="no">Loop Caregiver</span> app (under development, iOS only) enables the following from the caregiver's phone
            * monitor <span translate="no">Loop</span>
            * issue remote commands for carbs, bolus and overrides

<span translate="no">Nightscout</span> is useful for many who use <span translate="no">Loop</span>. Adults who take care of themselves find the reports and analysis methods from the <span translate="no">Nightscout</span> site provide effective tools to monitor their settings and provide reports for their health care provider. It also stores <span translate="no">Loop</span> configurations so they can be reviewed. With <span translate="no">Loop</span> 3, the saved <span translate="no">Nightscout</span> profiles can be downloaded to a new app for quick onboarding, should you ever need to start fresh.

Setting up a <span translate="no">Nightscout</span> site is described in a separate web site: [<span translate="no">Nightscout</span>: Documentation](https://nightscout.github.io).

There are <span translate="no">Nightscout</span> apps in your iPhone App Store that allow you to view the <span translate="no">Nightscout</span> site after you've configured it, or you can use a web browser to view the data. The app alone is not enough - you need to follow the steps to configure your own <span translate="no">Nightscout</span> site and obtain your specific <span translate="no">Nightscout</span> URL.

* <span translate="no">Nightscout</span> is highly recommended for <span translate="no">Loop</span> users, especially those using <span translate="no">Loop</span> as caregivers
* <span translate="no">Nightscout</span> displays are often the easiest way to troubleshoot <span translate="no">Loop</span> settings if you are having problems and seeking input from others
* <span translate="no">Nightscout</span> provides reporting features for longer-term review and preparing information for your physician

## <span translate="no">Nightscout</span> Documentation

There used to be a lot of <span translate="no">Nightscout</span> information found only in <span translate="no">LoopDocs</span>, but that was transferred and subsequently updated in [<span translate="no">Nightscout</span>: Documentation](https://nightscout.github.io). The information that remains in <span translate="no">LoopDocs</span> is <span translate="no">Loop</span> specific. So you may be jumping back and forth between the two sets of documents.

!!! info ""

    * If you see the <span translate="no">Nightscout</span> Owl logo in upper left you are in the <span translate="no">Nightscout</span> website
    * If you see the <span translate="no">LoopDocs</span> green-loop logo in upper left you are in the <span translate="no">LoopDocs</span> website
    * While in the <span translate="no">Nightscout</span> tab of <span translate="no">LoopDocs</span>, most links have a <span translate="no">Nightscout</span> or <span translate="no">LoopDocs</span> in the link name
    * Suggestion: open the [<span translate="no">Nightscout</span>: Documentation](https://nightscout.github.io) in a separate tab or window of your browser for easy access to both websites


## <span translate="no">Nightscout</span> with <span translate="no">Loop</span>

This page provides general discussion about the <span translate="no">Nightscout</span> display, as well as some <span translate="no">Loop</span>-specific display information. Over time, interactions between <span translate="no">Loop</span> and <span translate="no">Nightscout</span> were improved. The information on this page has been updated for <span translate="no">Loop</span> 3 and <span translate="no">Nightscout</span> version 14.2.6 (or later). Older versions may exhibit some differences in display of <span translate="no">Loop</span> information on the <span translate="no">Nightscout</span> site.

### <span translate="no">Loop</span> Uploads to <span translate="no">Nightscout</span>

The <span translate="no">Nightscout</span> display updates when the <span translate="no">Loop</span> phone is connected to the internet via WiFi or cellular service. When the uploads stop, the <span translate="no">Loop</span> pill becomes "stale" (cannot open it) after 15 minutes.

"Pills" are the little information boxes. They are [<span translate="no">Nightscout</span>: Plugins](https://nightscout.github.io/nightscout/setup_variables/#plugins) that must be enabled with configuration variables and then the display for each pill can be turned on or off within your <span translate="no">Nightscout</span> site.

If upload to <span translate="no">Nightscout</span> is interrupted, <span translate="no">Loop</span> stores up to 7 days of <span translate="no">Nightscout</span> information in a local buffer on the phone, and will attempt to upload later when access is restored. Once access is restored, a stale <span translate="no">Loop</span> Pill may require 15 minutes before it will open to display additional <span translate="no">Loop</span> information.

The Carb pill on the <span translate="no">Nightscout</span> site is populated by <span translate="no">Loop</span> when <span translate="no">Loop</span> is actively uploading to <span translate="no">Nightscout</span> - but it may lag the value displayed in the <span translate="no">Loop</span> pill by one loop cycle and it will display 0 COB within 5 to 10 minutes if upload is interrupted. In other words, if the COB pill shows 0 unexpectedly and <span translate="no">Loop</span> pill is active, you can believe the value shown in the <span translate="no">Loop</span> pill.

### <span translate="no">Loop</span> 2 <span translate="no">Red Loop</span> Warning

With <span translate="no">Loop</span> 2.2.9 and earlier versions, when <span translate="no">Loop</span> has a <span translate="no">Nightscout</span> site added in <span translate="no">Loop</span> Services AND is unable to upload messages to that site, it can fill up a buffer of stored upload messages. This may lead to sluggish behavior in <span translate="no">Loop</span> or even cause a <span translate="no">Red Loop</span>. This can happen if the <span translate="no">Nightscout</span> site is "down" or if the database is full so it is not accepting messages.

Step 1: Remove <span translate="no">Nightscout</span> URL from <span translate="no">Loop</span> Services

Step 2: Figure out why the <span translate="no">Nightscout</span> site is not accepting uploads from <span translate="no">Loop</span> and fix that problem.

* [<span translate="no">Nightscout</span>: Troubleshooting](https://nightscout.github.io/troubleshoot/troubleshoot)
* [<span translate="no">Nightscout</span>: Database Management](https://nightscout.github.io/nightscout/admin_tools/#database-maintenance)

Step 3: Add <span translate="no">Nightscout</span> URL to <span translate="no">Loop</span> Services

??? tip "Do you want to know more? (Click to open)"
    For those who want to know more:

    There is a big architectural change between <span translate="no">Loop</span> 2 and <span translate="no">Loop</span> 3 for remote data services like <span translate="no">Nightscout</span>.

    It used to be that data would be “held on” to be uploaded, and a non functional service could cause large backlogs. The new system does not allow for this. Uploaders individually keep track of where they are in the upload stream via a lightweight “query handle”, and if the data in <span translate="no">Loop</span> data stores expires before they upload, then they’ll just not be able to upload that data.

    The default data store for <span translate="no">Loop</span> 3 is 7 days.

## <span translate="no">Nightscout</span> Dashboard

![img/example.jpg](img/example.jpg){width="600"}
{align="center"}

### Blood Glucose

Glucose readings from the CGM are shown in green, yellow, or red in the main Dashboard of <span translate="no">Nightscout</span>. (The graphic above was generated with Colors enabled in <span translate="no">Nightscout</span>; there are other display options.) You can adjust your high and low glucose alarm thresholds in <span translate="no">Nightscout</span> by modifying configuration variables. This is optional - defaults are provided if you do not set them. The alarm thresholds affect the color of the displayed CGM data points and, if enabled, determine when an audible and visible alarm sounds. The <span translate="no">Nightscout</span> alarm thresholds will not affect <span translate="no">Loop</span> performance. <span translate="no">Loop</span> only uses the glucose correction ranges in the <span translate="no">Loop</span> app settings.

The main dashboard (upper section) for <span translate="no">Nightscout</span> displays the time duration you have selected (in the example above, 12 hours). The bottom of the screen shows the last 48-hours of glucose trends. You can scan backward by dragging the bottom timeline to the left, if you want to review specific <span translate="no">Loop</span> actions or data in the last two days.

### SAGE, CAGE, BAGE pills

The SAGE, CAGE, and BAGE pills are for Sensor Age, Cannula Age, and (pump) Battery Age. These optional pills track the time since your CGM sensor, Pump site, and Pump battery were last changed. You can set up custom alerts to remind you when it is time to change the devices, or simply use the visuals to keep track of your particular timing for site/sensor changes. These fields will not auto-update from pump or CGM devices, instead you will have to update them using <span translate="no">Nightscout</span> Careportal so that the pill information is accurate.

### Carbs

Carbs are automatically uploaded to <span translate="no">Nightscout</span> by the <span translate="no">Loop</span> app. The amount of carbs on board (active carbs or COB) can be seen by clicking the <span translate="no">Loop</span> pill. The size of a white carb dot on the graph is proportional to the amount of carbs entered...bigger meals get bigger dots. <span translate="no">Loop</span> does not read carbs from <span translate="no">Nightscout</span> for use in looping calculations, it only uploads carbs to <span translate="no">Nightscout</span> that have been entered in the <span translate="no">Loop</span> app.


### Boluses

Insulin boluses are automatically uploaded to <span translate="no">Nightscout</span> by the <span translate="no">Loop</span> app. The bolus is shown as a filled-in blue lower-half of the dot, and the specific amount of the bolus is also shown. There may be a separation between the bolus and the carb entry, especially if the user preboluses a meal.

The bolus is uploaded to <span translate="no">Nightscout</span> as soon as it starts and Insulin on board (active insulin or IOB) is updated in the <span translate="no">Loop</span> pill. Should the bolus be interrupted, the <span translate="no">Nightscout</span> information is updated when the <span translate="no">Loop</span> information updates (assuming internet access is active).

### Temp Basals

Your current basal profile is automatically updated to <span translate="no">Nightscout</span> whenever it is changed by <span translate="no">Loop</span>. The dashed blue line represents the scheduled basal profile. The solid blue lines indicate the actual basal amounts set for a given time...so as <span translate="no">Loop</span> sets temp basals higher or lower than your scheduled basal rate. If the graph and <span translate="no">Loop</span> pill do not agree, you should believe the <span translate="no">Loop</span> pill.

### Predicted BG

The purple line to the right of the BG is <span translate="no">Loop</span> predicted BG. Watching the behavior of that purple line can help you understand why <span translate="no">Loop</span> is making decisions regarding high or low temps. You can read more on that topic in the [<span translate="no">LoopDocs</span>: Algorithm](../operation/algorithm/overview.md) section of these docs. If you don't see the prediction (and all other <span translate="no">Nightscout</span> and <span translate="no">Loop</span> settings are configured), tap on the 3 dots to the right of the 24 to reveal the choice to display AR2 prediction or <span translate="no">Loop</span> prediction. Adjust the check boxes to show just the <span translate="no">Loop</span> prediction.

### <span translate="no">Loop</span> pill

The <span translate="no">Loop</span> pill is the little display box which, when hovered over or clicked, will provide additional information about recent <span translate="no">Loop</span> activities and status. Information included is the last time <span translate="no">Loop</span> ran, the temp basal set, IOB, and COB. Looking at the <span translate="no">Loop</span> pill is a quick method for assessing if your loop is currently active, as well.

!!! info "<span translate="no">Loop</span> Pill status indicator symbols"

    <font style='font-size: 1.2em;'>X</font> &nbsp;
    Error in <span translate="no">Loop</span>

    <font style='font-size: 1.4em;'>ϕ</font> &nbsp;
    Recommending basal, but not enacting (open loop or pump suspended)

    <font style='font-size: 2em;'>⌁</font> &nbsp;
    Enacted a new temp basal

    <font style='font-size: 1.5em;'>↻</font> &nbsp;
    <span translate="no">Loop</span> is continuing with last temp basal, no change

    <font style='font-size: 1.5em;'>⚠</font> &nbsp;
    Warning indicating <span translate="no">Loop</span> is either red or has failed to upload to <span translate="no">Nightscout</span> for a longer period of time.
Mouse over or Touch the <span translate="no">Loop</span> pill to view a tool tip containing one or more of the latest status messages. The most up-to-date <span translate="no">Nightscout</span> also includes information in the <span translate="no">Loop</span> pill for the minimum and maximum predicted BG, eventual and predicted BG.

![img/loop_pill_message.png](img/loop_pill_message.png){width="750"}</dd>

</dl>
