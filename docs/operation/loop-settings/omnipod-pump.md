# Omnipod Users

Your Loop won’t have much showing initially until we get some basic settings
input. The beginning step will be to add a pump to your Loop. If you are using
an Omnipod pump, you can follow along for the rest of this page. If, however,
you are using a Medtronic pump, please head over to
[this page](https://loopkit.github.io/loopdocs/operation/loop-settings/mdt-pump/)
instead.

## Select Pump Type

Let’s start by clicking on the Loop Settings button in the toolbar at the bottom
of your Loop app. It looks like a little sprocket. On the settings screen that
opens, click on `Add Pump` and select the **Omnipod** option that appears.

<p align="center">
<img src="../img/loop_settings_add_pump.png" width="650">
</p></br>

## Select RileyLink

A list of all RileyLinks in the nearby area will display in the RileyLink Setup
screen. Select your RileyLink by sliding the toggle to display green and then
press the blue `Continue` button at the bottom of the screen. If your RileyLink
does not appear, make sure that its switch is turned on (switch slide up toward
the case's keyring) and lipo is charged.

<p align="center">
<img src="../img/pod-rl.png" width="250">
</p></br>

## Delivery Limits and Basals

The next screen will offer two areas where you will need to enter information:

- Delivery Limits: Delivery Limits are both your maximum basal rate and your
  maximum bolus amount. Your maximum basal rate will limit how aggressive your
  Loop will be able to set temporary basals to treat high blood glucose.
  Typically, new users should set this value conservatively around 3 times your
  highest scheduled basal rate until your comfort and experience with Loop
  develops.

- Basal Rates: Enter your scheduled basal rates, beginning at midnight.
  Consistent with PO use, the scheduled basal rates have a maximum of 24
  entries, no 0 u/hr entries allows, and rate increments of 0.05 u/hr.

<p align="center">
<img src="../img/pod-settings-screen.png" width="650">
</p></br>

When you finish entering these values, press the blue `Continue` button on the
bottom of the POD Settings screen to continue with the next steps of POD setup.

## Pair POD

1. Place the POD near RileyLink
2. Fill the POD with insulin until it beeps (minimum fill is 80 units)
3. Click the `Pair` button
4. Wait while the progress bar for priming completes
5. Press the `Continue` button when the blue checkmark confirms priming is
   complete

<p align="center">
<img src="../img/pod-setup-01-pair.png" width="650">
</p></br>

## Insert Cannula

1. Prepare your insertion site
2. Remove the POD's needle cap and adhesive backing
3. If the cannula is safely tucked away, apply the POD to your desired infusion
   site. If cannula is sticking out, press `cancel` in the upper right corner of
   the screen and try a new POD.
4. Press the `Insert Cannula` button.
5. Listen to the clicks filling the cannula, wait for insertion and the progress
   bar to complete. The number of clicks to insertion is not consistent. The
   cannula will deploy before the progress bar is completed.
6. Confirm cannula has deployed by looking through the peep-hole on the POD.
7. Press the `Continue` button

<p align="center">
<img src="../img/pod-setup-02-insert.png" width="650">
</p></br>

## Expiration Reminder

Finish the setup with using the default expiration reminder time (2 hours before
a full 3-days usage) or set the expiration notification to a more convenient
time to your liking which will show up in your locked screen and vibrates at
that time. Setup is complete and your POD is ready for use when you press the
final button.

<p align="center">
<img src="../img/pod-setup-03-complete.png" width="650">
</p></br>

## POD Settings

After the POD setup is completed, you will be on the POD Settings screen. This
screen will provide a variety of important information about your POD. You can
always come back to this screen later by tapping on the Omnipod image in your
Loop settings.

<p align="center">
<img src="../img/long-pod-settings.jpeg" width="250">
</p></br>

#### Device Information

The first section has information regarding how long the POD has been active,
expiration date and time, POD identifying information (if you have to call in
for a POD failure).

#### POD commands

There are two commands that you can issue through Loop to the POD.

- Suspend Delivery: This command will suspend all insulin delivery; basals, temp
  basals, and boluses in progress. When you press suspend delivery, all insulin
  delivery will stop indefinitely.

<p align="center">
<img src="../img/pod-settings-resume.png" width="250">
</p>

A banner notice will appear on the Loop's main screen when insulin delivery is
suspended.

<p align="center">
<img src="../img/pod-hud-suspended.png" width="250">
</p>

You will need to press `Tap to Resume` in the banner or the `Resume Delivery`
button in the POD settings to resume your scheduled basal rate and let Loop get
back to action. Bolus deliveries will not be resumed, if they were interrupted.

- Replace POD: This command should be used to deactivate a POD prior to
  replacing it.

<p align="center">
<img src="../img/pod-settings-replace-pod.png" width="250">
</p>

#### Configuration

- Expiration Reminder: With the Expiration Reminder you can set a convenient
  time to get a notification to replace your POD. Using the standard setting,
  Loop sets the default to a full 3 days. You can set the reminder to any day
  and time up until 80 hours. This changes the PDM default which sets the alert
  always to 2 hours before a full 3-day (72 hours) run. This assumes you will
  not have run out of insulin before that time. In the event your POD runs out
  of insulin, then you will get a "POD empty" notification.

<p align="center">
<img src="../img/pod-settings-screen-expiration-reminder.png" width="250">
</p></br>

- Change Time Zone: If you are traveling for short periods of time, you do not
  have to worry about changing the time on your POD. However, if you are going
  to be away from home for longer periods of time, you will want to update your
  POD's basal schedule to match local time by selecting the `Change Time Zone`
  command when convenient. Using this command will move your basal schedule on
  your current POD to the new time. If you start a new POD session the new time
  zone will be used. Please wait until you see `Succeeded` appear on the page to
  ensure the command has successfully been received by the POD.

<p align="center">
<img src="../img/pod-change-timezone.png" width="250">
</p>

- Test Command: This command is used only by the developers to test Omnipod
  commands in Loop. It currently issues a "get status" command and can be used
  to update your screen details if needed or force a fault error to generate in
  the issue report after getting a screaming POD.

#### Status

This section provides information about your POD's status.

- Bolus Delivery: This line will let you know the % progress of any ongoing
  bolus.

<p align="center">
<img src="../img/pod-settings-bolus-status.png" width="250">
</p>

- Basal Delivery: This line will let you know what is active: The normal basal
  _schedule_,the _U/hour_ of a 30 minute Temp Basal or if the POD is
  _suspended_.

<p align="center">
<img src="../img/pod-settings-basal-delivery.png" width="250">
</p>

- Alarms: If your POD is screaming or beeping an alarm, this line will display
  information about the alarm. By clicking on this line, you can clear or
  "snooze" the alarm status.

<p align="center">
<img src="../img/pod-settings-alarms.png" width="250">
</p>

- Reservoir: Pods do not report the volume of insulin remaining in the reservoir
  until there are less than 50 units remaining. So, typically you will see "50+
  U" in this line for quite a while with a new POD.

<p align="center">
<img src="../img/pod-settings-reservoir.png" width="250">
</p>

- Insulin Delivered: This line is the total amount of insulin, both basal and
  bolus, delivered by the POD since it was activated.

<p align="center">
<img src="../img/pod-settings-insulin-delivered.png" width="250">
</p>

## Next Step: Add CGM

Congrats! You've added your POD to your Loop app. Now, click on the `Done`
button in the upper right corner of your Pump Settings screen to take you back
to the Loop's settings. Your next step is to
[Add CGM](https://loopkit.github.io/loopdocs/operation/loop-settings/cgm/) to
your Loop app. After all, without CGM data, your Loop won't loop.
