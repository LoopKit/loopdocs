## Why are there so many Omnipod Pump Manager versions?

The code used to control Pods is undergoing a lot of modifications in the summer of 2026. 

You can skip ahead to the [Table of OmnipodKit Versions](#table-of-omnipodkit-versions), or keep reading for more details.

### OS-AID Omnipod History

For Loop versions 3.14.2 and newer, all Omnipod pump manager control code is found in a single repository: **OmnipodKit**.

Before that, there were two repositories with a lot of common code; often requiring updates for each repository to provide a single improved feature.

To make development easier moving forward and to facilitate adding Omnipod 5 Pod support, the OmnipodKit repository was created to replace the two older submodules, which are now removed from Loop.

#### OmniKit

OmniKit was used to communicate with Classic (also known as Eros or Generation 3) Pods using a RileyLink

* This is now replaced with **OmnipodKit**

#### OmniBLE

OmniBLE was used to communicate with DASH Pods with direct Bluetooth connection

* This is now replaced with **OmnipodKit**
* The method developed for DASH pods originally used a *keep-connected* method
* Three minutes after the last message exchange between the phone and Pod, the Pod would initiate a disconnect from the Bluetooth channel (a characteristic of those Pods)
* The 3-minute disconnect could be detected and an immediate reconnect be initiatied by iOS giving a 3-minute heartbeat for these pods
* We now believe that keeping the DASH Pods connected may lead to heavier battery load with potentially more Faults
    * This began to be critical when the new version of DASH Pods, using Atlas cards, began to be delivered in spring of 2025, see: [Increase in DASH Faults](#increase-in-dash-faults)
* Furthermore, several iPhone models, iPhone 16/17e, were very slow to make connection with Atlas DASH pods: [Keep Alive: Atlas or InPlay DASH Pods](#keep-alive-atlas-or-inplay-dash-pods)


#### OmnipodKit

OmnipodKit replaces the need for OmniKit and OmniBLE submodules and provides support for Classic, DASH and Omnipod 5 Pods

* The intial version with Omnipod 5 support used the Bluetooth *keep-connected* method; but this did not provide a heartbeat for Omnipod 5 Pods
* When developing a new method, connect on demand for the iOS/Pod pair, not only was a heartbeat developed for Omnipod 5 Pods, but this new technique appears to greatly reduce the 203 Fault frequency for Atlas DASH Pods
    * This new version: nicknamed *ble-heartbeat* was a move in the right direction
    * Because the Bluetooth connection is only opened when the app wants to communicate with the Pod, the interaction appears slower to the user: only a few seconds, but noticeable
* The next version, nicknamed *eager-connect*, arose from analysis of what is going wrong with iPhone 16/17e models when initiating a Bluetooth connection to Atlas Pods
    * There are a lot of technical details but the short version is that with iPhone 16/17e the Bluetooth connection could get stuck and it could take seconds to minutes for nominal communication to begin
        * If you read the PR, you may see language about the system getting "wedged" where the iOS and Pod states were not communicating and suffered from a very-long timeout before trying again
    * The *eager-connect* method, senses if the connection is taking too long and restarts the process
        * With iPhone 16/17e, the connection is much faster: a few seconds instead of seconds to minutes
        * For all other phones, the *eager-connection* is ready to communicate with the pod in a few seconds, so the user can still notice a slight connection delay compared to the *keep-connected* method, but faster than with *ble-heartbeat* method


### Table of OmnipodKit Versions

For details about the different Bluetooth connection methods nicknamed *keep-connected*, *ble-heartbeat* and *eager-connect*, please read [OS-AID Omnipod History](#os-aid-omnipod-history). Some of the Loop versions listed below are works-in-progress suitable only for expert testers.

| Loop | Status |Pod Pump Manager | BLE Method | Supports |
|:--|:--|:--|:--|:--|
| before Loop 3.14.2 | released | OmniKit<br>OmniBLE | *keep-connected*| Classic, DASH |
| Loop 3.14.2 | released |  OmnipodKit | *keep-connected* | Classic, DASH |
| Loop 3.14.6 | dev | OmnipodKit | *ble-heartbeat* | Classic, DASH, Omnipod 5 |
| Loop 3.15.2 | next-dev | OmnipodKit | *eager-connect* | Classic, DASH, Omnipod 5 |

#### Map of OmnipodKit SHA

Users do not need this but developers may find this helpful in selecting which version of OmnipodKit to use for their release and development branches.

**OmnipodKit Branches / SHA as of 2026-09-12**

* subject to modification - be sure to check [GitHub](https://github.com/loopandlearn/OmnipodKit/branches)
* all these branch support Classic, DASH, and Omnipod 5 Pods
* all these branches support a connect on demand Bluetooth method

**At this snapshot in time**, the OmnipodKit `main` and `dev` branches have the same code with two different SHA. There are open PR to modify `dev` so that additional *eager-connect* testing can start. The `next-dev` branch is where most of the early testing happens. Both the `dev` and `next-dev` branches are subject to rapid change. 

**The `main` branch is the stable version of *ble-heartbeat* and will be in the next Loop release (v3.14.6).**

| Branch | Date | SHA | BLE Method |
|:--|:--|:--|:--|
| main | 11 Sep 2026 |  `aee61f9` | *ble-heartbeat* |
| dev | 11 Sep 2026 |  `176a42d` |*ble-heartbeat* |
| next-dev | 9 Sep 2026 | `7511203` | *eager-connect* |

## Is Omnipod 5 available for open-beta testing?

Yes it is.

* We encourage anyone interested in participating in the Omnipod 5 Open Beta to read [these FAQs](https://nightscout.github.io/omnipod-five/open-beta.html)

Specific information about using Omnipod 5 Pods with Loop is found in LoopDocs.

### Is this version less secure than using the PDM

The security layer that Insulet added to Omnipod 5 is fully preserved.

The method used by Open-Source Automated Insulin Delivery (OS-AID) systems retains all the security that users want in their devices; secure authorization and privacy of comms.

This is all handled for you automatically. You simply need to ensure you have internet access for your first Omnipod 5 Pod.

### Should I switch to Omnipod 5 now?

Don't be in a rush, the open beta testing is almost completed and Omnipod 5 will be in released code soon

### How can I switch to Omnipod 5?

!!! important "You need to be comfortable building a development branch, updating frequently, and reporting problems."

If you decide to test: help us by [reporting any problems](#how-do-i-report-problems).

#### Build the correct version of code

To get access to Omnipod 5, build the `dev` branch for Loop.

* Please read: [Updates in dev](../version/development.md#updates-in-dev)
* Please follow along in zulipchat at [Loop-dev status](https://loop.zulipchat.com/#narrow/channel/144182-development/topic/Loop-dev.20Status/with/606368226)

#### Perform a one-time step to support Omnipod 5

There is a one-time step to get a certificate needed for you to use an Omnipod 5 Pod. This is pretty automatic, but this is new code so be prepared to handle issues if they happen. 

This step requires you to have **internet access**. After this step is done, you can pair an Omnipod 5 Pod with this phone and this app with no need for internet access.

!!! important "Do not fill your first Omnipod 5 Pod before you reach the Pair Pod screen"

**First Omnipod 5 Pod Only**

When you deactivate a Pod, you can cancel out of the Pair Pod screen, scroll to the bottom and choose to [Switch Pod Type](../loop-3/omnipod.md#switch-pod-type){: target="_blank" } and choose Omnipod 5. As soon as you confirm Omnipod 5 as your selection, you are automatically routed to a service that provides you with the certificate you need. You will see several progress screens finishing in this final screen.


![sucess screen after downloading an Omnipod 5 certificate](../loop-3/img/omnipod-5-setup-success.png){width="300"}
{align="center"}

At this point, you can tap Continue and will be taken to the Pair Pod screen. It is now safe to fill your Omnipod 5 Pod with insulin and pair it.

Because of the extra exchanges required to handle the security added to Omnipod 5 Pods, the pairing and some of the insulin dosing commands may seem slow compared to a DASH Pod. This is normal.

### How do I report problems?

* You can report problems (and compliments) in the [Loop Open Beta for Omnipod 5](https://loop.zulipchat.com/#narrow/channel/144182-development/topic/Loop.20Open.20Beta.20for.20Omnipod.205/with/607418710) topic in zulipchat.

Please report any Fault you experience and upload your [Loop Report](../loop-3/settings.md#issue-report){: target="_blank" } that contains the Fault using the [OmnipodKit Testing Log form](https://docs.google.com/forms/d/e/1FAIpQLSeuclLr4jU-5Vr5oF1vYgmUv_FoN12nxXR0-Bzu_JW1J3bn5w/formResponse).

You are not required to upload a Loop Report following each successful Pod change, although if you do - that successful report will be processed and added to our statistics.


### What are the known issues?

These are known issues for the `dev` branch of Loop.

* The `dev` branch uses a connect-on-demand method for connecting to both DASH and Omnipod 5 Pods so you may notice a slight delay in connecting, getting status and then responding to a command from Loop
    * This is normal, be patient
* [Will I still get 203 errors?](#will-i-still-get-203-errors) - there have always been some reports of 203 faults with DASH that ramped up significantly with the Atlas version of DASH. Early testing indicates reduced frequency of 203 faults for Atlas DASH Pods with the newer Bluetooth protocols.
* If you are using an iPhone 16/17e, the connection delay is variable and can be quite severe (up to minutes to connect)
    * Use the [Pod Keep Alive Feature](../loop-3/omnipod.md#pod-keep-alive-feature){: target="_blank" } - unless you have a RileyLink device, select the Silent Tune option for Atlas DASH pods with an iPhone 16/17e

#### Updates in `next-dev` branch only

A new BLE management protocol is under test in the `next-dev` branch. This branch fixes the following issues:

* [Will I still get 203 errors?](#will-i-still-get-203-errors) - there have always been some reports of 203 faults with DASH that ramped up significantly with the Atlas version of DASH. Early testing indicates reduced frequency of 203 faults for Atlas DASH Pods with the newer Bluetooth protocols.
* If you are using an iPhone 16/17e, the connection delay has been dramatically redused using the new *eager-connect* connect-on-demand method
    * Early testing indicates the Pod Keep Alive option might not be needed, but it is available if you have difficulty with the iPhone 16/17e plus Atlas DASH combination

#### No Pump Heartbeat

* An early implementation (dev v3.14.3) did not provide an Omnipod 5 heartbeat; please rebuild if your CGM does not provide a hearbeat

### Will I still get 203 errors?

Both the `dev` and `next-dev` branches use a new connect-on-demand method that appears to reduce the frequency of 203 faults for Atlas DASH pod.  In addition, no 203 faults have been observed to date by any of the Omnipod 5 testers.

## Which Pods work with the *Loop* app?

You can use Omnipod 5 (under test), DASH and Eros Pods with the *Loop* app.

* The Omnipod 5 is only available in the development branches while in open beta testing

You do not need the Omnipod Personal Diabetes Manager (PDM), just the pod supplies. Your insurance or pharmacy coverage may cover some of the cost. The PDM may be needed in some countries to get replacements for failed Pods.

!!! info "Alternative Names for Omnipod Pods"

    All three types of Pods can be packaged five to a box, don't let the 5-pack indication confuse you. 

    * **Eros** Pods are also known as **Classic** or **UST400**
        * The Reference number on the boxes should be similar to POD-ZXP425
        * They have a clear needle cap
        * Pharmacy sites sometimes may refer to the **Eros Pods** as **Gen 3** but they are the same Pods

    * **DASH** Pods have DASH in the name
        * The Reference number on the box should be similar to POD-BLE-P1-525
        * They have a blue needle cap

    * **Omnipod 5** Pods have 5 in the name
        * The Reference number on the box should be similar to POD-OMNI-I1-6720
        * They have a clear needle cap

DASH and Omnipod 5 pumps communicate with the phone via Bluetooth so they do not require a RileyLink compatible device.
You may find the Omnipod 5 a little slower when pairing than the DASH because of the extra layer of security added to these Pods.

**To date, no iPhone model specific issues have been found with Omnipod 5 Pods variants tested.**

### Increase in DASH Faults

There have been a number of lots of Atlas DASH Pods that exhibit an increase in the frequency of certain DASH Faults when used with iOS Open-Source Automated Insulin Delivery Systems (OS-AID). This is different from the Bluetooth connection issues for some iPhone models: see [Keep Alive: Atlas or InPlay DASH Pods](#keep-alive-atlas-or-inplay-dash-pods).

It took a while, but we are testing (in `dev` and `next-dev` branches) a different method of connecting to Pods that appears to reduce the frequency of 203 Faults.  There are faults that can happen with any pods, including 203, but the Atlas DASH pods exhibited almost 20 times the rate of 203 faults as earlier pods and that particular problem is improved.

#### Status for released code

This section remains valid for folks using released code, v3.14.2 or earlier, which used the *keep-connected* method for Bluetooth between the phone and pod. The new methods under test, which connect on demand, provide reduced frequency for 203 faults.

People who have boxes that fail early find most Pods in that box fail early.

* The 203 fault is the most common one to exhibit an increase in frequency; occuring on the third day of Pod life
* The 016 fault also exhibits an increased frequency and this one happens early in Pod life
* You may be able to get Insulet to replace these, but there is no guarantee

We have looked at the analytics reported from Loop users who [share their data](../loop-3/onboarding.md#usage-data-sharing){: target="_blank" }. The increase in fault rate appears to go along with the increased used of Atlas Pods. Reports from users that their Pods failed early started in November/December of 2025 and continues to increase through at least May 2026. Note that 203 and 016 faults have been around for a long time. The increased fault rate (almost 20 times more likely for 203 and 4 times more likely for 016) is associated with the Atlas DASH Pods which use a different internal card with different firmware.

### Keep Alive: Atlas or InPlay DASH Pods

!!! warning "iPhone 16 (all models) and 17e model with Omnipod DASH"
    **iPhone 16 all models** and **iPhone 17e model only** can be slow to reconnect to Atlas versions of DASH Pods. This can cause delays to automatic and manual insulin dosing.

    **Other phones, including iPhone 17 models other than 17e, do not have the reconnection problems with InPlay DASH Pods** - but see [Increase in DASH Faults](#increase-in-dash-faults) when using the *keep-connected* Bluetooth method which affects all phone models and seems to be box specific.

> * Note that the BLE Management modifications found in the `dev` branch, known as *ble-heartbeat*. cannot fix the slow reconnection time for Atlas DASH Pods using iPhone 16 and 17e. 

> * The `next-dev` code offers yet another version of connect on demand, nicknamed *eager-connect*. It senses if the connection is taking too long, quits the attempt and retries until the connection goes through. For iPhone 16/17e, this can still be a few seconds, but much faster than before. 

Beginning in 2025, DASH Pods began using the newer version of chips and firmware. The only way to tell the difference before use is to examine the paper cover over the Pods inside the box for the word `Atlas` (newer) or `SAW` (older) as shown in the graphic below. These `Atlas` Pods, which report electronically as `InPlay BLE`, are the new version.

**If you do not already own an iPhone 16 or a 17e, it is strongly suggested you choose an older (iPhone 15 or SE or older) or newer (iPhone 17 that is not the 17e) phone.**

* The left images show the SAW marking for `TWI Board` DASH Pods
* The right images show the Atlas marking for `InPlay BLE` DASH Pods
* The exact location of the marking varies according to manufacture location and date but the `SAW` or `Atlas` notation indicates the internal BLE configuration for that pod

![identifying marks for SAW and Atlas DASH Pods](img/saw-atlas-identifiers.svg){width="750"}
{align="center"}

#### Characteristics of Atlas with iPhone 16 or 17e

* The Atlas DASH Pods, which advertise a Bluetooth Device name of `InPlay BLE` and indicate `-Atlas` in small print on the paper pod cover are fully compatible with all iPhone models except iPhone 16 and iPhone 17e
* Although `InPlay` Pods do work with the iPhone 16 and 17e you may notice some communication issues
    * It can take many attempts to get the pod to initially connect when pairing; just keep hitting retry
    * Once the pod disconnects itself from the phone Bluetooth, the phone is slow to reconnect the pod to the *Loop* app
        * Pod firmware initiates the disconnect 3 minutes after the last message exchange
        * With other models, the reconnect happens in about 1 sec
        * With iPhone 16 or 17e, this can take many seconds and sometimes a few minutes
    * When the pod is not connected, neither automatic nor manual commands can be sent to the pod to modify insulin delivery
    * No solution to this issue is known
    * There is a work-around to keep these Pods more connected by issuing a keep-alive message before the 3-minute BLE disconnect; but it uses extra battery for the phone. 
        * Although it does increase the number of messages to the pod slightly, this is not thought to be a big issue. Pods with marginal batteries are as likely to fault without this feature as with the feature.
        * If you are forced to use an iPhone 16 or 17e with InPlay Pods, please read the [Pod Keep Alive Feature](../loop-3/omnipod.md#pod-keep-alive-feature){: target="_blank" } section. This used to be found only in a feature branch but as of v3.14.0 is part of the released Loop code

> DASH Pods that advertise a Bluetooth Device name of `TWI Board` and indicate `-SAW` in small print on the paper pod cover are fully compatible with all phones including the iPhone 16 and 17e.

> The earliest `Atlas` DASH Pods noticed by the OS-AID community were manufactured in Feb 2025. Some TWI DASH Pods were manufactured in May 2025. Later in 2025, `Atlas` DASH Pods with July 2025 and later manufacture dates were seen. 

**The *eager-connect* method, currently under test, may be a fix for the iPhone 16/17e connection issue.**

- - -

## What about *Tidepool Loop*?

*Tidepool Loop* was approved by the FDA in Jan 2023. In 2025, the [Sequel twiist pump](https://www.twiist.com/) became available with *Tidepool Loop*. Check their site to see if it available in your area.

There is no arrangement for using an FDA cleared version of the Loop app with Omnipod. You must still build it yourself to use Omnipod Eros or DASH Pods.

- - -

## Do I still need a PDM with Omnipod Loop?

You don't need a PDM to use Pods with your OS-AID system but you are likely to need a PDM serial number registered to your Insulet account to get replacements for failed Pods.

Pods are monogamous little creatures. They will pair with only one device at a time for safety reasons...so a pod is either paired with a PDM or your *Loop* app on your iPhone. In other words, your PDM can stay in the diabetes closet while you are Looping. You cannot use the PDM for a pod that has been activated with the *Loop* app. That doesn't mean you should get rid of your PDM if you have one. Instead, keep it for backup situations if you lose your phone. See below for what to do if you lose your phone or RileyLink.

- - -

## Can I cancel a bolus?

Yes, you can cancel a bolus in progress. In fact, because it is very easy to cancel, make sure your phone is locked prior to being put away to avoid inadvertently cancelling a bolus. (This behavior is very similar to the Insulet PDM - which also needs to be locked once a bolus has started.)

As soon as a bolus is initiated, look at your phone in portrait orientation.  You will see a bolus message indicating the progress of the bolus. This message is highlighted with a red rectangle in the graphic below. If you tap on this part of the display, the bolus is immediately cancelled.

* The displayed amount `Bolused` is based on the time since the bolus was started
* The *Loop* app will present that graphic for the entire time the bolus is in progress with the delivery amount updated based on time
* Once the bolus completes, the *Loop* app updates the actual delivery amount based on communication with the pod (taking into account any interruption of that bolus from the user or a pod error)

![graphic showing the bolus in progress - tap to cancel display](img/cancel-bolus.svg){width="300"}
{align="center"}

- - -

## Can I cancel a temp basal?

### Cancel Temp Basal with the *Loop* app

With *Loop* 3, disabling the setting for Closed-Loop immediately restores the basal rate on the pump to the scheduled basal rate, which effectively cancels the temp basal.

You can tap on disable Closed-Loop and then immediately tap on enable Closed-Loop if all you want to do is cancel the current temp basal. If you do restore Closed-Loop, then *Loop* will resume automatic insulin delivery adjustments within 5 minutes.

!!! tip "Bolus in progress"
    Even if a bolus is in progress, you can still switch to Open-Loop and restore scheduled basal. The current bolus continues unless you separately cancel the bolus.

- - -

## Can I set my own temp basal on Loop?

With version 3, the *Loop* app provides a [Manual Temp Basal](../loop-3/omnipod.md#manual-temp-basal) feature.

- - -

## How much insulin is left when Pod reservoir say zero or 0 U?

When the Pod reports 0 U in the reservoir, there can be up to 4 U more delivered.

* You will not see a report of these units on the reservoir icon or on the Pod screen
* The pod keeps track of how many units are delivered after it reports 0 U in the reservoir and it will stop when it delivers 4 more units
* The pod also keeps track of whether insulin is being delivered and it will start to scream when there is not any more

Do **not** count on those 4 U, but be aware that they might be available.

The Event Log for dose delivery keeps track of what was actually delivered. The Insulin on Board (IOB) for the app updates if a bolus is interrupted because the pod runs out of insulin or hits the 4 U below zero limit.

- - -

## What if I lose my phone or RileyLink?

Most users are now on DASH and no longer need a RileyLink, but you might still walk away from your phone - we just hope you didn't lose it.

For pod users, your pod will finish any currently running temporary basal rate and then revert back to your scheduled basal rate. Without a phone (or RileyLink with Eros pod), however, you will not be able to affect any pod use; no basal change, suspend, cancel, or bolus. To do anything other than let basals continue, you will need to take action depending on the situation.

* Lost RileyLink only: You can replace your missing RileyLink with one from your backup supplies. No problem to [switch out to a different Rileylink mid-pod session](rileylink-faqs.md#adding-or-changing-rileylink). If you don't have a backup RileyLink to use, then you will need to remove the pod and put on a new pod paired with your PDM until you can get a new RileyLink. In the interim, you are still getting basal from the pod. If you are taking bolus insulin via injection, just add it to Apple Health under insulin. The *Loop* app will read it and keep making predictions for you. Once you inject, then add the carbs that go with that injection into Loop.

* Lost iPhone only: You will need to remove the pod and put on a new pod paired with your PDM or a backup phone (with a copy of the *Loop* app on it). You cannot use the old pod with a new device. In the interim, the pod will continue to deliver your scheduled basal until the pod reaches 80 hours. See [New Phone](new-phone.md) for more information.

* Lost both RileyLink and phone: You're having a really bad day. You'll need a hug and to follow the same directions as if you lost the phone as shown in the bullet above.

- - -

## Is there an increase in pod failures on Loop?

This section used to be accurate. But there is an issue with some Atlas DASH pods that we don't understand, but we have statistics indicating a big increase in frequency of faults (Pods starting to scream). See [Increase in DASH Faults](#increase-in-dash-faults).

There is more communication between the pod and the controller (your *Loop* phone) than is typical with the PDM (Insulet provided controller). This increases the load on the pod battery. Most people have no increase in pod failures, but there are steps to take to limit "extra pod battery use". Every time the *Loop* app requests an update of the pod state or issues a command (bolus, basal schedule, temp basal), messages are exchanged with the pod.

* Set your correction range to be 10 to 20 mg/dL (0.5 to 1.1 mmol/L) instead of a single number
    * The number of commands will be reduced
* The pod state is updated every 3 minutes for DASH and every 5 minutes for Eros
* If uncertain communications are detected such that the *Loop* app cannot determine if a dosing command sent to the pod was actually received, the app will try once a minute to get a response
    * The combination of Eros Pods with a RileyLink device with poor signal leading to uncertain comms may cause excessive battery use and contribute to pod faults

- - -

## What do I do if a pod fails to pair?

If you get a pod that is failing to pair, please see [this page](../troubleshooting/pod-pairing.md){: target="_blank" } for steps on how to fix the problem. Follow these steps before filling and trying another pod. If the pod is not screaming, you can probably recover it.

- - -

## What do you do to stop a screaming pod?

Screaming pods indicate the pod is out of insulin or out of time (80 hours) or there has been a critical pod fault.  In all these cases, there is no more delivery of insulin.

The first step is to use your phone to `Deactivate` the pod. You may need to go to the pod settings and tap on the Replace Pod row or the app may take you to the screen with a Deactivate button directly. This only works if the app is able to communicate with the pod.  Sometimes this is not possible. After you attempt to deactivate two times, the app will "discard" the pod as active if communication fails and enable you to pair a new pod. But you still need to make that noise go away.

If you are **not** successful at deactivating a pod and you've tried the steps at [Reset-Loop-to-Pump-Communications](../troubleshooting/red-loop.md#reset-loop-to-pump-communications), make sure the old pod is removed from the area before trying to connect a new pod. (Placing it in a microwave temporarily prevents the phone from detecting that pod.) The paperclip trick (next paragraph) only breaks the sound connection, the pod electronics is still active.

Once you have removed the screaming pod, it can be silenced using a paperclip. Simply put the paperclip in the small hole that is on the bottom (the side opposite where the cannula is) of the pod as shown. Push the paperclip in until you hear a little click, that click is breaking the circuit that connects the speaker to the electronics.

![img/paperclip.jpg](img/paperclip.jpg){width="500"}
{align="center"}

- - -

## What Are the Pod Priming and Start Delays?

- You have 2 hours after you fill the Pod with insulin to do a successful prime (this happens when you tap on `Pair Pod` on the Omnipod screen)
- You have 1 hour after the prime completes to insert the cannula

If you exceed these time limits, the pod becomes useless.  


!!! info "Omnipod User Manual on Pod Start Delay"
    
     page 85:  
    > **Note**: After filling the Pod, continue to the next step immediately.  
    > If two hours pass before activating the filled Pod, the Pod becomes unusable.
    
     page 86:  
    > **Note**: After activating, the Pod beeps every 5 minutes until you apply it.  
    > If you do not apply it and do not begin insulin delivery within 60 minutes after activating, the Pod becomes unusable.  

Window                      | Delay
---                         | ---
Filling to Priming          | 2 Hours
Priming to Canula Insertion | 1 Hour

Below is a *state diagram* that will give you a more **visual** representation.

```mermaid
stateDiagram-v2
    state 2h_timeout_reached <<choice>>
    state 1h_timeout_reached <<choice>>
    filled: Pod Filled
    primed: Pod Primed
    inserted: Pod Canula Inserted
    2h_window: 2-Hour Window
    2h_timeout: Exceeded 2-Hour Limit?
    1h_window: 1-Hour Window
    1h_timeout: Exceeded 1-Hour Limit?
    pod_useless: Pod is Useless

    [*]    --> filled
    filled --> 2h_window
    state 2h_window {
      [*] --> 2h_timeout
    }
    2h_window --> 2h_timeout
    2h_timeout --> 2h_timeout_reached
    2h_timeout_reached  --> pod_useless: Yes
    2h_timeout_reached  --> primed: No

    primed --> 1h_window
    state 1h_window {
        [*] --> 1h_timeout
    }
    1h_timeout --> 1h_timeout_reached
    1h_timeout_reached  --> pod_useless: Yes
    1h_timeout_reached  --> inserted: No

    inserted --> [*]
```

!!! tip "What to do if the Pod becomes useless?"
    - Be sure to [break the sound card connection](#what-do-you-do-to-stop-a-screaming-pod) before discarding the Pod - it will scream after 80 hours, if not sooner.  
    - Be sure to move the old Pod far away before attempting to pair a new Pod.
        - You can put the old Pod in the microwave to shield it while pairing the new one - be sure to take it out before you start the microwave
        - Breaking the connection to the sound card does **not** deactivate the Pod communications - it only stops the noise
