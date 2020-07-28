# Step 5: Order a RileyLink

!!!danger "Time Estimate"
    * 15 minutes to order a RileyLink
    * 15-20 minutes to assemble the RileyLink once you get it in the mail
    * 15-20 minutes to read about the RileyLink

!!!info "Summary"
    * Order your [Omnipod RileyLink](https://getrileylink.org/product/rileylink433) or [Medtronic RileyLink](https://getrileylink.org/product/rileylink916).
    * Assemble the RileyLink, after hugging the postman
    * Read the "extra details" to learn about RileyLink lights, charging, range, etc.

!!!warning "FAQs"
    * **"Do I need a RileyLink?"** Yes. Loop will not work without a RileyLink. Omnipod users will not be able to bolus from their looping pod without a RileyLink.
    * **"What happens if I lose my RileyLink or walk away from it?"** Good question...answered [here](https://loopkit.github.io/loopdocs/faqs/rileylink-faqs/#what-happens-if-i-walk-away-from-my-rileylink).
    * **"Can I use an Omnipod RileyLink with a Medtronic pump? or vice versa?"** Good question...answered [here](https://loopkit.github.io/loopdocs/faqs/rileylink-faqs/#what-will-happen-if-you-use-a-916mhz-antenna-rileylink-with-an-omnipod-or-vice-versa).
    * **"Can I swap out RileyLinks at any time?"** Yes, you can. RileyLinks can be replaced quite simply without needing to start a new pod or rebuild Loop app. There's a place in Loop settings that you'd simply find your new RileyLink's name and turn "on" the Bluetooth connection to start using it.
    * **"How close does the RileyLink need to be to me? Do I have to carry it with me?"** Good questions...answered [here](https://loopkit.github.io/loopdocs/faqs/rileylink-faqs/#do-i-have-to-carry-the-rileylink-everywhere).
    * **"Why is it named RileyLink?"** Riley is the name of Pete Schwamb's daughter and he's the guy that created the RileyLink.
    * **"Can I make my own RileyLink?"** Technically yes, however it is not an easy project. You'll need specialized tools and patience. If you want to explore doing that, I'd highly recommend checking out [Zulipchat](https://loop.zulipchat.com/#narrow/stream/148542-RileyLink) from the other people who have done their own builds successfully over the last several years. Only 3 people have built their own RileyLinks so far...but I guess that technically means it is possible. The PCB files and software, with instructions on how to build your own hardware module can be found at the [RileyLink Github repo](https://github.com/ps2/rileylink).

## What is RileyLink
The RileyLink (RL) is an open-source hardware device that can bridge Bluetooth Low Energy (BLE) to 916MHz or 433MHz wireless communication. What does that mean to you? It means RileyLink is the communication highway between your insulin pump, CGM, and iPhone.</br></br>

<p align="center">Loop will not work without the RileyLink.</b></p></br></br>

<p align="center">
<img src="../img/rl_diag.png" width="450">
</p>

## Order RileyLink
This is an easy step. You need to order a RileyLink from the [GetRiley website](https://getrileylink.org). 

There are two types of RileyLinks; [one for Omnipod](https://getrileylink.org/product/rileylink433) users and [one for Medtronic](https://getrileylink.org/product/rileylink916) users. Order the RileyLink specifically for the pump you'll be Looping with. 

## Assemble RileyLink

Your RL will come with the battery disconnected and the parts not already inside the case. It will be up to you to put the RL in the case and attach the battery.

Make sure the lipo battery is well-plugged into the connection. Line up the little ridge appropriately, and push fairly firmly to get the connection tight.  Poor battery cable connection can make the Loop communications fail.  See photos below, for example.

!!!info "Common new user errors"
    The most common two errors for new RL owners are (1) not fully pushing in the lipo battery cable connection and (2) failing to charge the RL. Compare your lipo battery cable with the photos; it takes a bit of oomph to push that plug fully in like the photos shown below. Remember to charge your RL each night.

<p><figure align="center">
<img src="../img/battery-cables.jpg" width="400">
<figcaption>Loose battery cable on left, Proper battery cable on right</figcaption>
</figure></p>

Finally, the board and the battery fit into the slim case fairly tightly as well.  Click on the image below to watch a helpful [assembly video](https://www.youtube.com/watch?v=-GHxxEJMCZc&feature=youtu.be).

<a href="https://www.youtube.com/watch?v=-GHxxEJMCZc&feature=youtu.be" target="_blank"><img src="../img/slimcase.png"  title="RileyLink assembly video" /></a>

## Extra Details about RileyLink

### Radio communications

The RL communicates with the pump through radio frequency communications.  Numerous factors can influence how well those communications can function...interferences from other devices, temperature, physical blocking, etc.

When your RL and pump are first paired, Loop performs a series of tests that you won't see...they are tuning tests. Basically, RL sends little test messages to the pump and waits for a response. The RL tries this same "ping" to the pump a range of various radio frequencies. The range of radio frequencies it tries is based on the pump you've told RL to expect (Omnipod, Medtronic NA/CA, or Medtronic WW).  RL will then record the radio frequencies that provided the strongest response and use that frequency for future pump communications.

Usually this best frequency is pretty constant for any given pump+RL, but during temperature changes it may be that the best frequency is not the one currently set. In the event that RL has problems communicating with the pump, Loop has code built-in that will automatically tell the RL "Hey, try that tuning pump thing again...maybe there's a better frequency we need to try." This retuning is started automatically if pump communications fail for 14 minutes (in other words, two looping cycles).

### Bluetooth communications

RL communicates with your iPhone and Loop app through Bluetooth (BT).  

!!!info Bluetooth Troubleshooting
If your iPhone has BT issues, your Loop will have failures.  There have been reports of BT audio devices (such as BT pairings in your car or home audio BT speakers) interfering with the Loop.  If you are finding Loop failures frequently happening at a particular location, you may try to troubleshoot if there are BT problems in the area.

Your BT signal strength can be seen in the Loop settings, under the RL menu, on the `Signal Strength` line. As you move closer and further away from your phone, you can watch that number dynamically change. This line is **not** displaying the signal strength of your pump communications discussed above.

<p align="center">
<img src="../img/RL_bt.jpg" width="400">
</p>

### Lights

RL has several lights that you may notice from time to time. There is no 'power' light. If you suspect that your RL is not being powered, try turning it off and on using the small sliding switch. You should see lights in the middle of the board flash when you do this.  If they flash, that means the board has power.

* Red light: Charging light. The red light will remain on while RL is charging, and it will turn off when charging is complete. You may notice the red light turn on periodically even after charging is complete...it's just "topping off".

* Green light: Bluetooth connection light. The green light will remain on while you have a BT connection with your iPhone.  If that green light fails to stay on, you should troubleshoot your BT connections. Try restarting BT on your iPhone and/or turning the RL off/on by its power switch.

* Blue light: Pump communications.  If you have an older firmware on your RL, some of the blue lights will flash periodically as it communicates with the pump. It's just letting you know that it is busy talking and collecting info. You will also see increased blue flashes if you have "Enabled Diagnostic LEDs" for MDT users that have the RLs with updated firmware (shipping since late August 2018).

A solid blue light that consistently remains lit on the board could mean one of two things:

* A temporary issue that can be resolved by rebooting the RL physically (turning the switch off/on), or

* An electrical short or damage to the board.  Sweat and moisture are most likely culprits, so try to keep case free from those environments. Don't keep RL in sports bras or waistband next to skin, for example, while exercising.

If your blue light remains on despite trying a restart, it is time to pull out your backup RL.

### Charging

The battery that comes with RL is not likely charged completely when it is shipped, so feel free to charge it up.  You'll need a [mini-USB cable](https://www.amazon.com/AmazonBasics-USB-2-0-Cable--Male/dp/B00NH13S44) and [0.5A USB charging power supply](https://www.amazon.com/Cellet-Powered-Charger-iPhones-Smartphones-/dp/B00FE8WFCO) like your iPhone power supply.  RL takes about 2 hours to fully charge (the red light will turn off when fully charged, read note above about red light patterns) and should easily last at least a full day of constant Loop use.  Typically, it can go into the 30-hour range without any problems.  Most people charge their RL each night when they are sleeping.  You don't have to worry about leaving the RL plugged in "too long" for charging.  It will automatically stop charging the battery when it is fully charged.

Since the best practice is to charge your RL overnight while you sleep, and the battery lasts safely over 24 hours, there is no battery level indicator for the RL.  The RL's charge level is not viewable on Nightscout, nor within the Loop app.  If you forget to charge your RL overnight, you can recharge it with a portable USB battery in a pinch.  A [short mini-USB cable](https://www.adafruit.com/product/899) could be a good addition to a small gear bag.

### Range

The range that your RL will function is **heavily** dependent on the environment that you are in. Most people wear the RL in a pocket or carry a belt holster during the day. The radio frequency communications will have a shorter range than the BT communications, therefore RL will do better closer to the pump rather than the iPhone if you are deciding on options for carrying gear. 

Problematic environments will be places like technical conferences, sports arenas, and other places where wireless communications are heavy and plenty.

### Lipo Battery

Keep your RL and lipo battery protected from damage.  Lipo batteries are unsafe when damaged or punctured, so the case is an important part of safe Looping. If your battery is damaged in some way, please disconnect it immediately, and dispose of it (they should be recycled). You can order new batteries on the [GetRileyLink website](http://getrileylink.org/)

### Removing Lipo Battery

To remove the lipo battery from the RL, please do so slowly and patiently. Work the battery connection side to side slowly to loosen it from the plug. Some people have reported success using small, curved needle-nose pliers such as hemostats. Others have used small flathead screwdrivers as shown in [this video](https://youtu.be/s2qNPLpfwww).

<a href="https://youtu.be/s2qNPLpfwww" target="_blank"><img src="../img/rileylink_battery_removal.png"  title="RileyLink assembly video" /></a>

## Waiting for RileyLink

Yes, waiting for RL to arrive is extremely difficult if they are backorder.  PLEASE be patient, since Loop CANNOT work without RL.

If you're really dying to do something while RL ships, you can proceed with finishing these build directions all the way through Step 14...but after that you'll have to wait for the RileyLink.  You can't properly enter any settings or pump info in Loop app without the RileyLink.

## Next Step: Enroll in Apple Developer Program

Now you are ready to move onto Step 6 to [enroll in the Apple Developer Program](https://loopkit.github.io/loopdocs/build/step6/).
