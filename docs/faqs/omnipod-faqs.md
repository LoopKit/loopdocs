# Omnipod FAQs

## Is Omnipod supported on Loop?

YES IT IS!!! WOOHOO!!

## Which pods will work with Loop?

The Loop system described in these documents (aka DIY Loop) works with Eros pods...these are the current pods on the market in wide release. The newer DASH pods are not compatible with DIY Loop. Tidepool has begun a process to bring [DIY Loop through FDA approval](https://tidepool.org/blog/tidepool-delivering-loop) and Insulet has been announced as the [first pump partner for that project](https://diatribe.org/omnipod-first-insulin-pump-partner-tidepool-loop). Tidepool Loop will be using DASH pods, no RileyLink required.  If you would like to stay informed about Tidepool Loop progress, you can fill out an interest form [here](https://tidepool.org/loop). 

Summary of eventual systems:

* DIY Loop + Eros pods + RileyLink</br></br>
* Tidepool Loop + DASH pods (no RileyLink)

## Do I still need a PDM with Omnipod Loop?

No, pods are monogamous little creatures. They will pair with only one device at a time for safety reasons...so a pod is either paired with a PDM or your Loop app on your iPhone. In other words, your PDM can stay in the diabetes closet while you are Looping. You cannot use the PDM for a pod that has been activated with Loop. That doesn't mean you should get rid of your PDM. Instead, keep it for backup situations if you lose your phone. See below for what to do if you lose your phone or RileyLink. 

## Can I cancel a temp basal Loop sets? How about a bolus?

Yes, you can cancel a temp basal or a bolus in progress. There is a "suspend delivery" command that is easy to access by tapping on the [pod age icon in your Heads Up Display, upper right area](https://loopkit.github.io/loopdocs/operation/loop-settings/displays/#pod-age-omnipod-users). Suspending insulin delivery will cancel any running temp basal or bolus in progress. The suspend command will run indefinitely. A banner notification will be displayed on the Loop main screen while insulin delivery is suspended.

<p align="center">
<img src="../img/pump-suspend-banner.png" width="300">
</p>

Insulin will remain suspended until the user either clicks on the "Tap to Resume" command from Loop's main screen or the "resume delivery" command accessed by tapping the pod age icon. Once insulin delivery is resumed, you will be resumed at your scheduled basal rate. If a bolus was interrupted, the bolus will not resume. If you don't turn on open loop mode, within 5 minutes of resuming insulin delivery, your Loop should resume automatic temp basal adjustments.

## Can I prime or set my own temp basal on Loop?

No. Loop does not allow you to pick your own temp basal rate or prime insulin in. 

If you find yourself in a situation where you would like to specify an exact temp basal rate of your own, you would need to (1) change your scheduled basal rate for the time(s) that you'd like a temp basal rate to run, and (2) suspend/resume insulin delivery (in order to cancel any currently running temp basal that Loop has running) and then (3) turn the slider so that you are running in "open loop" mode for the duration of the time you want to use that specific basal rate. 

## What if I lose my phone or RileyLink?
For pod users, your pod will finish any currently running temporary basal rate and then revert back to your scheduled basal rate. Without a phone or RileyLink however, you will not be able to affect any pod use; no basal change, suspend, cancel, or bolus. To do anything other than let basals continue, you will need to take action depending on the situation.

* Lost RileyLink only: You can replace your missing RileyLink with one from your backup supplies. No problem to switch out to a different Rileylink mid-pod session. If you don't have a backup RileyLink to use, then you will need to remove the pod and put on a new pod paired with your PDM until you can get a new RileyLink.

* Lost iPhone only: You will need to remove the pod and put on a new pod paired with your PDM until you can get a new phone and Loop app built onto it.

* Lost both RileyLink and phone: You're having a really bad day. You'll need a hug and follow the same directions as if you lost the phone as shown in the bullet above.

## Is there an increase in pod failures on Loop?
In the early stages of development, there were. Thankfully to the hard work of Pete Schwamb and others, pod failure rate is now no longer increased compared to typical pod use with a PDM.

## What do I do if a pod fails to pair?

The most common time of pod errors on Loop will be during the pairing process. If you get a pod that is failing to pair, please see [this page](https://loopkit.github.io/loopdocs/troubleshooting/pod-pairing/) for steps on how to fix the failure and recover before you lose the pod.

## What do you do to stop a screaming pod?
Screaming pods can be silenced by carrying a paperclip. Simply put the paperclip in the small hole that is on the bottom (the side opposite where the cannula is) of the pod as shown. Push the paperclip in until you hear a little click, that click is breaking the circuit that lets the audible scream go. 

<p align="center">
<img src="../img/paperclip.jpg" width="500">
</p>
