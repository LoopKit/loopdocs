# RileyLink Menu

The RileyLink menu is accessed by clicking on the image of your connected pump in Loop settings. From that pump screen, scroll to the bottom and you will see the names of your connected RileyLink(s). (Note: The device searching indicator near the RileyLink's toggle will always be spinning, even after a RileyLink is successfully connected. That is normal behavior.)

Helpful tip: If you are ever going to be near other Loop users, you may want to consider renaming your RileyLink to a new name so that you can pick it out of a crowd.  Click on the RileyLink line, and the RileyLink's menu will be displayed. At the top of this menu is a line for the device name. Click on the that line and you will be able to change the name of your RileyLink. The new name may need to sit for a few seconds before exiting back out of the naming screen for it to save itself. RileyLink must be connected and on to change the name.

Depending on which pump you have connected to your Loop app, your RL menu will look different. On the left below is the typical RL menu when using Medtronic pump, and on the right is with an Omnipod. As you can see, both have in common a section called "Device", but after that only the Medtronic pumps will have additional commands in the RileyLink menu.

<p align="center">
<img src="../img/rl-comp.png" width="450">
</p>

## Device

The settings under the Device section are mostly for your information only. The two most important lines are the Connection Status and Signal Strength.

* The Connections Status should say `connected` if the RileyLink is connected to the iPhone's Bluetooth. If the status says `connecting` or `disconnected` then you should toggle the iPhone's BT and/or RileyLink's power switch off/on to help reconnect.

* The Signal Strength is the strength of the Bluetooth signal between the iPhone and RileyLink.  It is **not** the signal strength of the radio communications with the pump/pod.  The lower the number, the stronger the connection. As you move the RL and iPhone closer/farther apart, you will be able to see the signal strength change. In a pinch, this can be used to help locate a lost RileyLink in the house.

<p align="center">
<img src="../img/RL_bt.jpg" width="350">
</p>

## Pump
The Pump ID and Pump Model will be automatically filled in from your pump. 

## Commands

There are several commands that the RileyLink can issue to a Medtronic pump. Most are simply for gathering information from the pump.

### Tune Radio Frequency

The pump and RileyLink communicate via radio frequency. In order to have the best possible communications, RileyLink will test a range of frequencies in order to see which provides the strongest response with the pump. In the event that pump comms fail for over 14 minutes, Loop will automatically retune the RileyLink to see if perhaps the strongest frequency has changed since it was last tuned.

When you first setup your Loop app, RileyLink will automatically perform a **Tune Radio Frequency** to get pump comms started. You can manually tune your radio frequency at any time by clicking on the command. It may take about a minute, but soon you will see a list of frequencies with the tuning strength results beside each frequency. The signal with the lowest value is the strongest and RileyLink will use that frequency. Exit out of that screen and the command line will now show the frequency (916.xx MHz for North American pumps) and the timestamp of the tune.

!!!info ""
    **A common troubleshooting recommendation is to tune your RL when you have poor pump communications. Just keep in mind that the Loop code has a function that it will automatically retune in the event of poor pump communications within 14 minutes. Loop does this automatically.  Manually retuning is only useful for impatience purposes. If Loop has failed longer than 20 minutes, it will have already likely tried a retune...but knock yourself out if you want to try it again manually.**

### Change Time
Loop automatically prompts you to set your pump time using the Loop app as part of initial Loop setup.  It is important that Loop and your pump share a common time setting, otherwise Looping will fail.  If you are traveling through timezones or dealing with daylight savings time, please read up on [how to safely change your pump time](/troubleshooting/time-change.md#traveling-across-time-zones-and-daylight-savings).

!!!info ""
    **Always use the RileyLink's <font color="orange">Change Time</font> command to change pump time.  If you fail to set the pump time by using the RileyLink, Loop will not function properly.  Do not use the pump menus to change your pump's time when Looping.**

### Other commands
MySentry Pair, Fetch Recent History, Fetch Enlite Glucose, Get Pump Model, Send Button Press, Read Pump Status, and Read Basal Schedule are all ways of asking the pump for information you might be interested in. They are not part of setting up the Loop and will not affect Loop operations. Enable Diagnostic LEDs, Discover Commands, and RileyLink Statistics are commands that are sometimes used by developers to aid in app troubleshooting and debugging. They don't impact Loop operations.

**MySentry Pair** is for x23 and x54 pumps only, and you will have completed this pairing command as part of the original `Add Pump` process. The MySentry pairing process adds a specific ID to your pump in the pump's Connect Devices, Other Devices menu. This pairing allows Loop to get information from x23 and x54 in an efficient manner. If that is not done, Loop will only be green every other loop. If you ever want to re-pair MySentry, you can follow the directions as shown in the RileyLink command screen. You do not have to worry about this command if you are using an x15 or x22 model pump, as they do not have MySentry.

**Fetch Recent History** polls the pump for recent pump events such as boluses, temp basals, primes, rewinds, etc.  The amount of information transmitted for a Fetch Recent History is usually quite large and, as a result, may be more prone to an early failure before it succeeds. If the first Fetch Recent History fails, sometimes it is helpful to use the Send Button Press command to sort of "wake up" the pump in preparation for communications.

**Fetch Enlite Glucose** is only useful for Medtronic CGM users. The Fetch Enlite Glucose command will pull the recent glucose values saved in the pump history. Dexcom users do not store any glucose data in the pump.

**Get Pump Model** simply returns the pump's model.

**Send Button Press** can be useful to see if the communication between the RileyLink and pump is working. If successful, the screen on the pump will light up and Loop will confirm the button press with a `success` message. If pump comms are failing, sending a successful button press can help "wake up" a pump that perhaps has not been communicating well.

**Read Pump Status** is also nice quick pump read for reservoir volume, pump battery voltage, and pump status (bolusing or suspending). For x23 and x54 pump users, this command will provide the exact pump battery voltage instead of the 25/50/75/100% levels that are reported otherwise.

**Read Basal Schedule** will pull the active basal pattern from the pump so you can review what the current settings are without using pump menu.

**Enable Diagnostic LEDs** will turn on more LED flashes on the RileyLink while it is operating. You will see more blue flashing lights as the RileyLink communicates with the pump. If you tried turning on this feature and decide later that you just don't want to see so many flashing lights, simply reboot the RileyLink by turning the power switch off/on.  This will reset the LEDs.

**Discover Commands** just ignore this menu item.

**RileyLink Statistics** tracks how long your RileyLink has stayed successfully operating and gives the developers some useful information about the stability of the RL operations. It really doesn't provide much to the average Loop user, however.
