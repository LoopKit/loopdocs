# Step 4: Compatible CGM

!!!danger "Time Estimate"
    * 10 minutes to read through this page
    
!!!info "Summary"
    * If you use a Dexcom G4 Share, G5, or G6 CGM system...you are good to use Loop.
    * If you use a Medtronic sensor compatible with a Loop-compatible Medtronic pump...you are good to use Loop.
    * If you have an Eversense...you cannot use Loop with that CGM.
    * If you use Libre...you will need to seek out a modified Loop

!!!warning "FAQs"
    * **"What about Libre sensors?"** Libre sensors are not designed to be continuous glucose monitors. All use of Libre sensors as continuous glucose monitors involves the use of third-party applications (Xdrip or Spike) and reader devices (BluCon or Miao Miao). Loop developers have not seen data demonstrating sufficient safeguards from those readers and applications to feel comfortable adding main line Loop integration for those devices. If you use a Libre sensor, you'll have to use a "not-main line" branch of Loop that someone (or yourself) has modified to allow for use with those sensors/applications.
    * **"What about Eversense?"** Eversense's application does not integrate with Apple Health, nor has the communications protocols for Eversense been reverse engineered. Therefore, Eversense is not compatible with Loop use currently.

A continuous glucose monitor (CGM) provides Loop with current blood glucose readings. These readings allow Loop to predict what the current glucose trend is, and predict future blood glucose based on carbohydrate input and your Loop settings. The following are the types of CGMs compatible with Loop. CGM readings are a required part of looping. If your Loop is unable to retrieve BG data, it will not be able to loop.

## Dexcom G5 and G6 CGM <img src="../img/g5.jpg" width="150" alt="G5">

Dexcom G5 and G6 receives CGM data directly to the Dexcom app on your iPhone via Bluetooth. Neither of these two systems require the use of a stand-alone receiver. For Loop to function, you will need the Dexcom app running.

## Dexcom G4 CGM with Share Receiver <img src="../img/g4_receiver.png" width="150" alt="G4 With Receiver">

Dexcom G4 Share system transmits CGM data from the transmitter to a Dexcom G4 Share Receiver. The receiver, in turn, connects to the Dexcom Share2 app on your iPhone via Bluetooth. The Share2 app uploads CGM data to the Dexcom servers. For Loop to function, you will need the Dexcom app running.

## Medtronic CGM <img src="../img/enlite.png" width="150" alt="Enlite">

The Minimed Enlite CGM, available with the Medtronic 522/722, 523/723, and 554/754, wirelessly sends blood glucose readings to the pump. Loop can read the Medtronic CGM data directly from the pump using the RileyLink.

## Offline Use

Offline use means using Loop when there is no cell data or internet available. Loop does not require any special setup to operate offline. You will not need to do anything special if you go camping or find yourself out in the wilderness. For offline Loop use, the iPhone's Bluetooth still needs to be active; and for Dexcom users, the Share2, G5, or G6 app also still needs to be open (but don't have to be actively "sharing" to the internet). If you put your iPhone into Airplane mode, remember to turn Bluetooth back on to keep your Loop running. If your offline use is failing, chances are you have forgotten to update your transmitter ID in Loop settings when you changed transmitters.

## Dexcom Servers

In some rare instances, the Loop may fail to eavesdrop on the Bluetooth transmissions of the CGM systems.  When that happens, the Loop can pull directly from Dexcom Servers to get the data (assuming you have entered your Share account information in the Loop settings and have Share turned on). When Loop is operating in this mode, you will see a small cloud in the CGM reading in the Loop app. Operating in this mode requires a working internet or cell connection.

## CGMs not natively supported in Loop

Libre (with BluCon or Miao Miao), Eversense, Medtronic Guardian sensors, etc.  Yes, there are other CGM systems available out there. Loop does not natively support those CGMs.  If you would like to use one of those alternate CGMs and Loop...you will need to look into third-party integrations to allow Loop to access the blood glucose data.  These docs do not cover the alternate methods of unsupported CGM systems or apps like Spike.

## Next Step: Order a RileyLink

Now you are ready to move onto Step 5 to [Order a RileyLink](https://loopkit.github.io/loopdocs/build/step5/).
