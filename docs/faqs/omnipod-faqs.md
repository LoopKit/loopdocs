# Omnipod FAQs

## Is Omnipod supported on Loop?

Yes.

## Which pods will work with Loop?

* The Eros pods are supported with released versions of Loop.
* The DASH pods are supported in the [dev branch](branch-faqs.md#whats-going-on-in-the-dev-branch).
* The Omnipod 5 pods are not supported with DIY Loop.

## What about Tidepool Loop?

Tidepool is working to bring [DIY Loop through the FDA regulatory process](https://tidepool.org/blog/tidepool-delivering-loop) and Insulet has been announced as the [first pump partner for that project](https://diatribe.org/omnipod-first-insulin-pump-partner-tidepool-loop). Tidepool Loop is being developed to work with a future version of the Omnipod system, no RileyLink required. Tidepool Loop was first [submitted to the FDA in December 2020](https://www.tidepool.org/blog/99-years-closer-about-our-fda-submission-of-tidepool-loop). If you would like to stay informed about Tidepool Loop progress, you can fill out an interest form [here](https://tidepool.org/loop).


## Do I still need a PDM with Omnipod Loop?

No, pods are monogamous little creatures. They will pair with only one device at a time for safety reasons...so a pod is either paired with a PDM or your Loop app on your iPhone. In other words, your PDM can stay in the diabetes closet while you are Looping. You cannot use the PDM for a pod that has been activated with Loop. That doesn't mean you should get rid of your PDM. Instead, keep it for backup situations if you lose your phone. See below for what to do if you lose your phone or RileyLink.

## Can I cancel a bolus?

Yes, you can cancel a bolus in progress. If fact, because it is very easy to cancel - you should make sure your phone is locked prior to being put away or you might inadvertently cancel a bolus. (This behavior is very similar to the Insulet PDM - which also needs to be locked once a bolus has started.)

As soon as a bolus is initiated, look at your phone in portrait orientation.  You will see a bolus message indicating the progress of the bolus. This message is highlighted with a red rectangle in the graphic below. If you tap on this part of the display, the bolus is immediately cancelled.  (This graphic of the Loop display is from Loop-dev.  If you are on Loop v2.2.x, the bolus in progress message looks and behaves the same.)

* The displayed amount `Bolused` is based on the time since the bolus was started
* Loop will present that graphic for the entire time the bolus is in progress with the delivery amount updated based on time
* Once the bolus completes, Loop updates the actual delivery amount based on communication with the pod (taking into account any interruption of that bolus from the user or a pod error)

![graphic showing the bolus in progress - tap to cancel display](img/cancel-bolus.svg){width="300"}
{align="center"}


## Can I cancel a temp basal?

### Cancel Temp Basal with Loop v2.2.x

If you are running Loop v2.2.x, the method for canceling a temp basal is to [suspend the pump and then resume delivery](../operation/loop-settings/pump-commands.md#suspend-delivery).

Be sure to follow up the suspend with the resume command. Insulin will remain suspended until the user either clicks on the "Tap to Resume" command from Loop's main screen or the "resume delivery" command accessed in the pump settings display. Once insulin delivery is resumed, you will be resumed at your scheduled basal rate. If a bolus was interrupted, the bolus will not resume. If you don't turn on open loop mode, within 5 minutes of resuming insulin delivery, your Loop will resume automatic insulin delivery adjustments.

### Cancel Temp Basal with Loop-dev

With Loop-dev, disabling the setting for Closed Loop also changes the basal rate on the pump to the scheduled basal rate, which effectively cancels the temp basal.

!!! warning "Bolus in progress"
    If a bolus is in progress when switching to Open Loop, any active Temp Basal continues until it would expire naturally, unless the user takes further action.

## Can I prime or set my own temp basal on Loop?

No. Loop does not allow you to pick your own temp basal rate or prime insulin (a Medtronic pump trick for adding extra insulin that Loop does not add to IOB).

If you find yourself in a situation where you would like to specify an exact temp basal rate of your own, you would need to (1) change your scheduled basal rate for the time(s) that you'd like that basal rate, (2) cancel any currently running temp basal that Loop has running) and (3) disable Closed Loop in Loop Settings so that you are running in "open loop" mode for the duration of the time you want to use that specific basal rate.

## What if I lose my phone or RileyLink?

For pod users, your pod will finish any currently running temporary basal rate and then revert back to your scheduled basal rate. Without a phone or RileyLink however, you will not be able to affect any pod use; no basal change, suspend, cancel, or bolus. To do anything other than let basals continue, you will need to take action depending on the situation.

* Lost RileyLink only: You can replace your missing RileyLink with one from your backup supplies. No problem to [switch out to a different Rileylink mid-pod session](rileylink-faqs.md#adding-or-changing-rileylink). If you don't have a backup RileyLink to use, then you will need to remove the pod and put on a new pod paired with your PDM until you can get a new RileyLink. In the interim, you are still getting basal from the pod. If you are taking bolus insulin via injection, just add it to Apple Health under insulin, Loop will read it and keep making predictions for you. Once you inject, then add the carbs that go with that injection into Loop.

* Lost iPhone only: You will need to remove the pod and put on a new pod paired with your PDM until you can get a new phone and Loop app built onto it. In the interim, the pod will continue to deliver your scheduled basal until the pod reaches 80 hours. See [Updating FAQs for New Phone](update-faqs.md#what-if-im-changing-phones) for more information.

* Lost both RileyLink and phone: You're having a really bad day. You'll need a hug and follow the same directions as if you lost the phone as shown in the bullet above.

## Is there an increase in pod failures on Loop?

In the early stages of development, there were. Thankfully to the hard work of Pete Schwamb and others, pod failure rate is now no longer increased compared to typical pod use with a PDM.

## What do I do if a pod fails to pair?

The most common time of pod errors on Loop will be during the pairing process. If you get a pod that is failing to pair, please see [this page](../troubleshooting/pod-pairing.md) for steps on how to fix the failure and recover before you lose the pod.

## What do you do to stop a screaming pod?

Screaming pods indicate the pod is out of insulin or out of time (80 hours) or there has been a critical pod fault.  In all these cases, there is no more delivery of insulin.

The first step is to use your phone to `Deactivate` the pod. You may need to go to the pod settings and tap on the Replace Pod row or the app may take you to the screen with a Deactivate button directly. This only works if the app is able to communicate with the pod.  Sometimes this is not possible. After you attempt to deactivate two times, the app will "discard" the pod as active if communication fails and enable you to pair a new pod. But you still need to make that noise go away.

Once you have removed the screaming pod, it can be silenced using a paperclip. Simply put the paperclip in the small hole that is on the bottom (the side opposite where the cannula is) of the pod as shown. Push the paperclip in until you hear a little click, that click is breaking the circuit that connects the speaker to the electronics.

![img/paperclip.jpg](img/paperclip.jpg){width="500"}
{align="center"}
