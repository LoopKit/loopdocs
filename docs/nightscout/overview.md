## Overview

<span translate="no">Nightscout</span>&nbsp; is an excellent tool for remotely viewing &nbsp;<span translate="no">Loop</span>&nbsp; actions. &nbsp;<span translate="no">Nightscout</span>&nbsp; can act as a stand-alone tool or be integrated with &nbsp;<span translate="no">Loop</span>. (<span translate="no">Nightscout</span>&nbsp; also integrates with other open-source hybrid closed loop systems such as OpenAPS, AndroidAPS and iAPS. &nbsp;<span translate="no">LoopDocs</span>&nbsp; focuses on &nbsp;<span translate="no">Loop</span>.)

When integrated with &nbsp;<span translate="no">Loop</span>, &nbsp;<span translate="no">Nightscout</span>&nbsp; provides monitoring of &nbsp;<span translate="no">Loop</span>&nbsp; activities such as viewing history of glucose, carbs, boluses, temp basals and overrides; troubleshooting &nbsp;<span translate="no">Loop</span>&nbsp; errors; and provides extensive reports for analyzing data trends and patterns. These reports assist when &nbsp;<span translate="no">Loop Therapy Settings</span>&nbsp; need to be adjusted.

For caregivers, &nbsp;<span translate="no">Nightscout</span>&nbsp; enables remote monitoring and even the ability to issue remote commands through &nbsp;<span translate="no">Nightscout</span>&nbsp; when both &nbsp;<span translate="no">Loop</span>&nbsp; and &nbsp;<span translate="no">Nightscout</span>&nbsp; are properly configured. There are several pages starting at &nbsp;[<span translate="no">LoopDocs</span>: Remote Overview](remote-overview.md) that provide documentation on this feature. If you are a caregiver, this summary of remote capabilities may encourage you to look into &nbsp;<span translate="no">Nightscout</span>.

!!! info "Remote Commands"
    * <span translate="no">Loop</span>&nbsp; 2.2.x
        * Overrides can be enabled and disabled
    * <span translate="no">Loop</span>&nbsp; 3
        * Overrides can be enabled and disabled
        * Carbs can be entered
        * Boluses can be commanded
        * <span translate="no">Loop Caregiver</span>&nbsp; app (under development, iOS only) enables the following from the caregiver's phone
            * monitor &nbsp;<span translate="no">Loop</span>
            * issue remote commands for carbs, bolus and overrides

<span translate="no">Nightscout</span>&nbsp; is useful for many who use &nbsp;<span translate="no">Loop</span>. Adults who take care of themselves find the reports and analysis methods from the &nbsp;<span translate="no">Nightscout</span>&nbsp; site provide effective tools to monitor their settings and provide reports for their health care provider. It also stores &nbsp;<span translate="no">Loop</span>&nbsp; configurations so they can be reviewed. With &nbsp;<span translate="no">Loop</span>&nbsp; 3, the saved &nbsp;<span translate="no">Nightscout</span>&nbsp; profiles can be downloaded to a new app for quick onboarding, should you ever need to start fresh.

Setting up a &nbsp;<span translate="no">Nightscout</span>&nbsp; site is described in a separate web site: &nbsp;[<span translate="no">Nightscout</span>: Documentation](https://nightscout.github.io).

There are &nbsp;<span translate="no">Nightscout</span>&nbsp; apps in your iPhone App Store that allow you to view the &nbsp;<span translate="no">Nightscout</span>&nbsp; site after you've configured it, or you can use a web browser to view the data. The app alone is not enough - you need to follow the steps to configure your own &nbsp;<span translate="no">Nightscout</span>&nbsp; site and obtain your specific &nbsp;<span translate="no">Nightscout</span>&nbsp; URL.

* <span translate="no">Nightscout</span>&nbsp; is highly recommended for &nbsp;<span translate="no">Loop</span>&nbsp; users, especially those using &nbsp;<span translate="no">Loop</span>&nbsp; as caregivers
* <span translate="no">Nightscout</span>&nbsp; displays are often the easiest way to troubleshoot &nbsp;<span translate="no">Loop</span>&nbsp; settings if you are having problems and seeking input from others
* <span translate="no">Nightscout</span>&nbsp; provides reporting features for longer-term review and preparing information for your physician

## <span translate="no">Nightscout</span>&nbsp; Documentation

There used to be a lot of &nbsp;<span translate="no">Nightscout</span>&nbsp; information found only in &nbsp;<span translate="no">LoopDocs</span>, but that was transferred and subsequently updated in &nbsp;[<span translate="no">Nightscout</span>: Documentation](https://nightscout.github.io). The information that remains in &nbsp;<span translate="no">LoopDocs</span>&nbsp; is &nbsp;<span translate="no">Loop</span>&nbsp; specific. So you may be jumping back and forth between the two sets of documents.

!!! info ""

    * If you see the &nbsp;<span translate="no">Nightscout</span>&nbsp; Owl logo in upper left you are in the &nbsp;<span translate="no">Nightscout</span>&nbsp; website
    * If you see the &nbsp;<span translate="no">LoopDocs</span>&nbsp; green-loop logo in upper left you are in the &nbsp;<span translate="no">LoopDocs</span>&nbsp; website
    * While in the &nbsp;<span translate="no">Nightscout</span>&nbsp; tab of &nbsp;<span translate="no">LoopDocs</span>, most links have a &nbsp;<span translate="no">Nightscout</span>&nbsp; or &nbsp;<span translate="no">LoopDocs</span>&nbsp; in the link name
    * Suggestion: open the &nbsp;[<span translate="no">Nightscout</span>: Documentation](https://nightscout.github.io) in a separate tab or window of your browser for easy access to both websites


## <span translate="no">Nightscout</span>&nbsp; with &nbsp;<span translate="no">Loop</span>

This page provides general discussion about the &nbsp;<span translate="no">Nightscout</span>&nbsp; display, as well as some &nbsp;<span translate="no">Loop</span>&nbsp;-specific display information. Over time, interactions between &nbsp;<span translate="no">Loop</span>&nbsp; and &nbsp;<span translate="no">Nightscout</span>&nbsp; were improved. The information on this page has been updated for &nbsp;<span translate="no">Loop</span>&nbsp; 3 and &nbsp;<span translate="no">Nightscout</span>&nbsp; version 14.2.6 (or later). Older versions may exhibit some differences in display of &nbsp;<span translate="no">Loop</span>&nbsp; information on the &nbsp;<span translate="no">Nightscout</span>&nbsp; site.

### <span translate="no">Loop</span>&nbsp; Uploads to &nbsp;<span translate="no">Nightscout</span>

The &nbsp;<span translate="no">Nightscout</span>&nbsp; display updates when the &nbsp;<span translate="no">Loop</span>&nbsp; phone is connected to the internet via WiFi or cellular service. When the uploads stop, the &nbsp;<span translate="no">Loop</span>&nbsp; pill becomes "stale" (cannot open it) after 15 minutes.

"Pills" are the little information boxes. They are [<span translate="no">Nightscout</span>: Plugins](https://nightscout.github.io/nightscout/setup_variables/#plugins) that must be enabled with configuration variables and then the display for each pill can be turned on or off within your &nbsp;<span translate="no">Nightscout</span>&nbsp; site.

If upload to &nbsp;<span translate="no">Nightscout</span>&nbsp; is interrupted, &nbsp;<span translate="no">Loop</span>&nbsp; stores up to 7 days of &nbsp;<span translate="no">Nightscout</span>&nbsp; information in a local buffer on the phone, and will attempt to upload later when access is restored. Once access is restored, a stale &nbsp;<span translate="no">Loop</span>&nbsp; Pill may require 15 minutes before it will open to display additional &nbsp;<span translate="no">Loop</span>&nbsp; information.

The Carb pill on the &nbsp;<span translate="no">Nightscout</span>&nbsp; site is populated by &nbsp;<span translate="no">Loop</span>&nbsp; when &nbsp;<span translate="no">Loop</span>&nbsp; is actively uploading to &nbsp;<span translate="no">Nightscout</span>&nbsp; - but it may lag the value displayed in the &nbsp;<span translate="no">Loop</span>&nbsp; pill by one loop cycle and it will display 0 COB within 5 to 10 minutes if upload is interrupted. In other words, if the COB pill shows 0 unexpectedly and &nbsp;<span translate="no">Loop</span>&nbsp; pill is active, you can believe the value shown in the &nbsp;<span translate="no">Loop</span>&nbsp; pill.

### <span translate="no">Loop</span>&nbsp; 2 &nbsp;<span translate="no">Red Loop</span>&nbsp; Warning

With &nbsp;<span translate="no">Loop</span>&nbsp; 2.2.9 and earlier versions, when &nbsp;<span translate="no">Loop</span>&nbsp; has a &nbsp;<span translate="no">Nightscout</span>&nbsp; site added in &nbsp;<span translate="no">Loop</span>&nbsp; Services AND is unable to upload messages to that site, it can fill up a buffer of stored upload messages. This may lead to sluggish behavior in &nbsp;<span translate="no">Loop</span>&nbsp; or even cause a &nbsp;<span translate="no">Red Loop</span>. This can happen if the &nbsp;<span translate="no">Nightscout</span>&nbsp; site is "down" or if the database is full so it is not accepting messages.

Step 1: Remove &nbsp;<span translate="no">Nightscout</span>&nbsp; URL from &nbsp;<span translate="no">Loop</span>&nbsp; Services

Step 2: Figure out why the &nbsp;<span translate="no">Nightscout</span>&nbsp; site is not accepting uploads from &nbsp;<span translate="no">Loop</span>&nbsp; and fix that problem.

* [<span translate="no">Nightscout</span>: Troubleshooting](https://nightscout.github.io/troubleshoot/troubleshoot)
* [<span translate="no">Nightscout</span>: Database Management](https://nightscout.github.io/nightscout/admin_tools/#database-maintenance)

Step 3: Add &nbsp;<span translate="no">Nightscout</span>&nbsp; URL to &nbsp;<span translate="no">Loop</span>&nbsp; Services

??? tip "Do you want to know more? (Click to open)"
    For those who want to know more:

    There is a big architectural change between &nbsp;<span translate="no">Loop</span>&nbsp; 2 and &nbsp;<span translate="no">Loop</span>&nbsp; 3 for remote data services like &nbsp;<span translate="no">Nightscout</span>.

    It used to be that Loop would keep trying to upload data to &nbsp;<span translate="no">Nightscout</span>. If a site could not be reached or would not accept data, that could cause large backlogs. &nbsp;<span translate="no">Loop</span>&nbsp; 2 could slow down by trying to keep uploading the backlog. The new system does not allow for this. Uploaders individually keep track of where they are in the upload stream via a lightweight “query handle”, and if the data in &nbsp;<span translate="no">Loop</span>&nbsp; data store expires before upload, that data will be missing in &nbsp;<span translate="no">Nightscout</span>.

    &nbsp;<span translate="no">Loop</span>&nbsp; 3 saves  7 days of information in the data store.

## <span translate="no">Nightscout</span>&nbsp; Dashboard

![img/example.jpg](img/example.jpg){width="600"}
{align="center"}

### Blood Glucose

Glucose readings from the CGM are shown in green, yellow, or red in the main Dashboard of &nbsp;<span translate="no">Nightscout</span>. (The graphic above was generated with Colors enabled in &nbsp;<span translate="no">Nightscout</span>; there are other display options.) You can adjust your high and low glucose alarm thresholds in &nbsp;<span translate="no">Nightscout</span>&nbsp; by modifying configuration variables. This is optional - defaults are provided if you do not set them. The alarm thresholds affect the color of the displayed CGM data points and, if enabled, determine when an audible and visible alarm sounds. The &nbsp;<span translate="no">Nightscout</span>&nbsp; alarm thresholds will not affect &nbsp;<span translate="no">Loop</span>&nbsp; performance. &nbsp;<span translate="no">Loop</span>&nbsp; only uses the glucose correction ranges in the &nbsp;<span translate="no">Loop</span>&nbsp; app settings.

The main dashboard (upper section) for &nbsp;<span translate="no">Nightscout</span>&nbsp; displays the time duration you have selected (in the example above, 12 hours). The bottom of the screen shows the last 48-hours of glucose trends. You can scan backward by dragging the bottom timeline to the left, if you want to review specific &nbsp;<span translate="no">Loop</span>&nbsp; actions or data in the last two days.

### SAGE, CAGE, BAGE pills

The SAGE, CAGE, and BAGE pills are for Sensor Age, Cannula Age, and (pump) Battery Age. These optional pills track the time since your CGM sensor, Pump site, and Pump battery were last changed. You can set up custom alerts to remind you when it is time to change the devices, or simply use the visuals to keep track of your particular timing for site/sensor changes. These fields will not auto-update from pump or CGM devices, instead you will have to update them using &nbsp;<span translate="no">Nightscout</span>&nbsp; Careportal so that the pill information is accurate.

### Carbs

Carbs are automatically uploaded to &nbsp;<span translate="no">Nightscout</span>&nbsp; by the &nbsp;<span translate="no">Loop</span>&nbsp; app. The amount of carbs on board (active carbs or COB) can be seen by clicking the &nbsp;<span translate="no">Loop</span>&nbsp; pill. The size of a white carb dot on the graph is proportional to the amount of carbs entered...bigger meals get bigger dots. &nbsp;<span translate="no">Loop</span>&nbsp; does not read carbs from &nbsp;<span translate="no">Nightscout</span>&nbsp; for use in looping calculations, it only uploads carbs to &nbsp;<span translate="no">Nightscout</span>&nbsp; that have been entered in the &nbsp;<span translate="no">Loop</span>&nbsp; app.


### Boluses

Insulin boluses are automatically uploaded to &nbsp;<span translate="no">Nightscout</span>&nbsp; by the &nbsp;<span translate="no">Loop</span>&nbsp; app. The bolus is shown as a filled-in blue lower-half of the dot, and the specific amount of the bolus is also shown. There may be a separation between the bolus and the carb entry, especially if the user preboluses a meal.

The bolus is uploaded to &nbsp;<span translate="no">Nightscout</span>&nbsp; as soon as it starts and Insulin on board (active insulin or IOB) is updated in the &nbsp;<span translate="no">Loop</span>&nbsp; pill. Should the bolus be interrupted, the &nbsp;<span translate="no">Nightscout</span>&nbsp; information is updated when the &nbsp;<span translate="no">Loop</span>&nbsp; information updates (assuming internet access is active).

### Temp Basals

Your current basal profile is automatically updated to &nbsp;<span translate="no">Nightscout</span>&nbsp; whenever it is changed by &nbsp;<span translate="no">Loop</span>. The dashed blue line represents the scheduled basal profile. The solid blue lines indicate the actual basal amounts set for a given time...so as &nbsp;<span translate="no">Loop</span>&nbsp; sets temp basals higher or lower than your scheduled basal rate. If the graph and &nbsp;<span translate="no">Loop</span>&nbsp; pill do not agree, you should believe the &nbsp;<span translate="no">Loop</span>&nbsp; pill.

### Predicted BG

The purple line to the right of the BG is &nbsp;<span translate="no">Loop</span>&nbsp; predicted BG. Watching the behavior of that purple line can help you understand why &nbsp;<span translate="no">Loop</span>&nbsp; is making decisions regarding high or low temps. You can read more on that topic in the &nbsp;[<span translate="no">LoopDocs</span>: Algorithm](../operation/algorithm/overview.md) section of these docs. If you don't see the prediction (and all other &nbsp;<span translate="no">Nightscout</span>&nbsp; and &nbsp;<span translate="no">Loop</span>&nbsp; settings are configured), tap on the 3 dots to the right of the 24 to reveal the choice to display AR2 prediction or &nbsp;<span translate="no">Loop</span>&nbsp; prediction. Adjust the check boxes to show just the &nbsp;<span translate="no">Loop</span>&nbsp; prediction.

### <span translate="no">Loop</span>&nbsp; pill

The &nbsp;<span translate="no">Loop</span>&nbsp; pill is the little display box which, when hovered over or clicked, will provide additional information about recent &nbsp;<span translate="no">Loop</span>&nbsp; activities and status. Information included is the last time &nbsp;<span translate="no">Loop</span>&nbsp; ran, the temp basal set, IOB, and COB. Looking at the &nbsp;<span translate="no">Loop</span>&nbsp; pill is a quick method for assessing if your loop is currently active, as well.

!!! info "&nbsp;<span translate="no">Loop</span>&nbsp; Pill status indicator symbols"

    <font style='font-size: 1.2em;'>X</font> 
    Error in &nbsp;<span translate="no">Loop</span>

    <font style='font-size: 1.4em;'>ϕ</font> 
    Recommending basal, but not enacting (open loop or pump suspended)

    <font style='font-size: 2em;'>⌁</font> 
    Enacted a new temp basal

    <font style='font-size: 1.5em;'>↻</font> 
    &nbsp;<span translate="no">Loop</span>&nbsp; is continuing with last temp basal, no change

    <font style='font-size: 1.5em;'>⚠</font> 
    Warning indicating &nbsp;<span translate="no">Loop</span>&nbsp; is either red or has failed to upload to &nbsp;<span translate="no">Nightscout</span>&nbsp; for a longer period of time.
Mouse over or Touch the &nbsp;<span translate="no">Loop</span>&nbsp; pill to view a tool tip containing one or more of the latest status messages. The most up-to-date &nbsp;<span translate="no">Nightscout</span>&nbsp; also includes information in the &nbsp;<span translate="no">Loop</span>&nbsp; pill for the minimum and maximum predicted BG, eventual and predicted BG.

![img/loop_pill_message.png](img/loop_pill_message.png){width="750"}</dd>

</dl>
