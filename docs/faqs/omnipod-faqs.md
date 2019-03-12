# Omnipod FAQs

## Is Omnipod supported on Loop?

No, not yet. Omnipod has been in the process of being "hacked" for several years now and this has been a tremendous amount of work. The work has been fruitful...but it is not ready for public release yet. When it is ready, we promise to update these documents with instructions and information about Omnipod Loop.

## Which pods will work with Loop?

The Loop system described in these documents (aka DIY Loop) will work with Eros pods...these are the current pods on the market in wide release.  The newer DASH pods will not be compatible with DIY Loop.  Tidepool has begun a process to bring [DIY Loop through FDA approval](https://tidepool.org/blog/tidepool-delivering-loop) and Insulet has been announced as the [first pump partner for that project](https://diatribe.org/omnipod-first-insulin-pump-partner-tidepool-loop). Tidepool Loop will be using DASH pods, no RileyLink required.  If you would like to stay informed about Tidepool Loop progress, you can fill out an interest form [here](https://tidepool.org/loop). 

Summary of eventual systems:

* DIY Loop + Eros pods + RileyLink</br></br>
* Tidepool Loop +DASH pods (no RileyLink)

## Do I still need a PDM with Omnipod Loop?

No, pods are monogamous little creatures. They will pair with only one device at a time for safety reasons...so a pod is either paired with a PDM or your Loop app on your iPhone. When Loop is ready for Omnipod, it will not use a PDM...and in fact you cannot use a PDM for a pod that has been activated with Loop. That doesn't mean you should get rid of your PDM. You should still keep it around in case your lose your phone or lose your RileyLink. You'd want to swap out to a new pod and pair it with the PDM if you lose a critical part of your Omnipod Loop gear.

## Can I cancel a temp basal Loop sets? How about a bolus?

Yes, you will be able to cancel a temp basal or a bolus in progress. There is a "suspend delivery" command that is easy to access by tapping on the [pod age icon in your Heads Up Display, upper right area](https://loopkit.github.io/loopdocs/operation/loop-settings/displays/#pod-age-omnipod-users). Suspending insulin delivery will cancel any running temp basal or bolus in progress. The suspend command will run indefinitely. A banner notification will be displayed on the Loop main screen while insulin delivery is suspended.

<p align="center">
<img src="../img/pump-suspend-banner.png" width="300">
</p>

Insulin will remain suspended until the user either clicks on the "Tap to Resume" command from Loop's main screen or the "resume delivery" command accessed by tapping the pod age icon. Once insulin delivery is resumed, you will be resumed at your scheduled basal rate. If a bolus was interrupted, the bolus will not resume. If you don't turn on open loop mode, within 5 minutes of resuming insulin delivery, your Loop should resume automatic temp basal adjustments.

## What if I lose my phone or RileyLink?
For pod users, your pod will finish any currently running temporary basal rate and then revert back to your scheduled basal rate. Without a phone or RileyLink however, you will not be able to affect any pod use; no basal change, suspend, or bolus. You will need to remove the Loop pod and put on a new pod paired with your PDM until you can get a new RileyLink and/or phone. If you only have lost the RileyLink (not the phone) and have a backup RileyLink, you can simply connect to the new RileyLink on the same Loop app and it will work with the existing pod session.

## Is there an increase in pod failures on Loop?
Yes, likely there will be an increase in your usual pod failure ("screaming pod") rate. The pod communications are a bit "neurotic" and full of safety checks to make sure the pod and PDM/phone are on the same page. Recreating these safety checks and communications have been the reason why the development of this pump on Loop has been so long and cumbersome. There are built-in pod errors within the pod's firmware so that it errors (screams) anytime it is uncertain of its status. With Loop communicating every 5 minutes with the pod, this increases the chances of a pod "scream". You should make sure you have adequate pod supplies long term to cover this potential increase in failure. As well, you should make sure to travel with backup pods day-to-day (although you are probably already doing that).

## What do you do to stop a screaming pod?
Screaming pods can be silenced by carrying a paperclip. Simply put the paperclip in the small hole that is on the bottom (the side opposite where the cannula is) of the pod as shown. Push the paperclip in until you hear a little click, that click is breaking the circuit that let's the audible scream go.

<p align="center">
<img src="../img/paperclip.jpg" width="500">
</p>
