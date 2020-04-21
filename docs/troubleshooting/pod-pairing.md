# Pod Pairing Failures

At the end of a pod life, you will deactivate your pod and then start the procedure for pair a new pod. The most typical problem when activating a new pod is a no response error during the initial pod pairing.

<p align="center">
<img src="../img/pod-pair-fail.jpg" width="300">
</p>

During pairing a number of possible errors can leave the pod in an apparent non-responding state. This is because the pod is in a particularly vulnerable state during the delicate pairing process and it's a very particular process that requires all steps to go back-and-forth correctly. We've been working hard on improvements to prevent various problems from happening and automatically recover from them if they do happen, but there are also things can be done to reduce the probability of this from happening and recover when they do occur.

### Verify the RileyLink

First, let's make sure everything is ok as far as the RileyLink goes:

1. RileyLink is charged and nearby, and
2. RileyLink has a green LED light lit (indicating a Bluetooth connection with your iPhone), and
3. Try toggling the RileyLink off/on at its physical switch if the green light is not on.

### Deactivate old Pod

Make sure you've deactivated your old pod. If you had issues deactivating your pod, you likely may have some RileyLink issues going on...so make sure to see the steps above. If you have a problem with deactivating a pod, go ahead and proceed with the "Switch from Omnipods" option. You should also remove that old pod from your vicinity. Put it in a microwave or throw it over the fence into the neighbor's backyard (kidding, obviously...but outside trashcan is a good idea).

### Beeping Pods

Once a new pod is powered-up by the insertion of at least 85 units of insulin, the Ppod will emit reminder beeps every 5 or 10 minutes until the pod activation process has completed. This pairing process must be completed within 60 minutes of beeps starting, or the pod will give up and never pair. These activation reminder beeps do not actually indicate that any pod communication is being attempted, just that the activation has not yet been completed and your 60 minute timer is counting down.

It is very important to not have two pods giving reminder beeps at the same time as this can cause even more confusion for you and for Loop. Continue to work with a single pod at a time, retrying the **Pair** multiple times if needed and trying the Pod Pairing Recovery sequence. 

If you cannot get the pairing to complete with the suspect pod (after trying following the Pod Pairing Recovery procedure described below a few times with multiple **Pair** during each try), then you should completely abandon that the pod before attempting to pair using another pod. "Completely abandon" means take that failed loser pod far, far away or in a microwave after doing the "switch from omnipods" or "deactivation" step. You do not want that beeping pod or failed pod to be any way able to plague your next pod's communications with Loop during the pairing process for next pod.

### Check the RileyLink and Pod Pairing Placement

The placement of the pod and the RileyLink relative to each other is crucial because the pod operates in a low power radio mode during pairing which can lead to a number of potential faulty and half-paired pod situations, particularly with older versions of Loop. The RileyLink should be as close to the **side** of the pod as possible, **but not any closer than a pinkie finger's width away** or the pairing might not be able to complete! An ideal way to keep the minimum spacing is to leave the pod in its plastic tray after filling with insulin and then placing the RileyLink standing up touching the left side of the tray with the antenna toward the cannula end as shown.

<p align="center">
<img src="../img/pod-rileylink-positioning.jpg" width="300">
</p>

The tray is not required for pairing, but it is an easy way to ensure close placement while maintaining the minimum spacing requirement. The important thing to remember is to position the RileyLink at least a pinkie finger's distance away from the *side* of the body of the pod and to position the RileyLink antenna *towards* the cannula (rounded) end. If the no response condition persists during subsequent **Pair** attempts, try adjusting the RileyLink position a bit and trying at least a few different times. Trying again with slightly different positioning can sometimes be enough for a successful pairing.

### What Happened?

Assuming the RileyLink is ok, the most common cause of a pod failure is that Loop incorrectly "halfway" pairs with the pod due to some problems during the fragile pairing process, perhaps aggravated the placement of the RileyLink and the pod, wireless communications interference, and/or incorrect handling of some fault and retry conditions which is especially true in earlier versions of Loop. These pairing problems can leave Loop and the pod in a state where the only possible recovery is to start the pairing process over from the very beginning.

## Pod Pairing Recovery

When you have a pod that continues to appear non-responsive after several retries **Pair** attempts while trying to properly reposition the RileyLink, it may be possible to recover by forcing Loop to start the pairing process from the beginning. This is particularly needed when running with Loop versions older than Loop v2.2 (April 2020) which are more susceptible to these types of problems. Loop v.2.2 has some improvements to the pairing code that should help reduce instances of some causes of pairing failures. 

Let's walk through the the steps of doing a Pod Pairing recovery assuming you've retried a number of times and you're still stuck getting no response errors on each **Pair** attempt.

<p align="center">
<img src="../img/pod-pair-no-response.png" width="300">
</p>

Starting from this Pod Pairing with no response screen, touch **Cancel** in the upper right corner which will take you back to the *Pod Settings* page.

<p align="center">
<img src="../img/pod-settings-switch-pumps.png" width="300">
</p>

Next select **Switch from Omnipod Pumps** in red which confirm that you want to stop using the Omnipod.

<p align="center">
<img src="../img/delete-omnipod-confirmation.png" width="300">
</p>

None of your Loop settings including the basal schedule and delivery limits will be lost deleting the Omnipod pump manager. Select **Delete Omnipod** to proceed which will take you back to the Loop home screen.  From here, select the gear icon at the bottom right to go the Loop `Settings` page.

<p align="center">
<img src="../img/settings.png" width="300">
</p>

Next select **Add Pump** in blue and then select **Omnipod** from the `Add Pump` list displayed.

<p align="center">
<img src="../img/add-pump-list.png" width="300">
</p>

 Verify that the green LED on the RileyLink goes on and off as you touch the switch for RileyLink you are using indicating a successful Bluetooth connection between the RileyLink and your iPhone. Leave the RileyLink enabled with its green LED and slider turned on, and then touch the **Continue** button on the bottom.

<p align="center">
<img src="../img/rileylink-setup-on.png" width="300">
</p>

The Pod Settings screen should have the previous Basal Rates and Delivery Limits in effect from your previous run which can be verified at this time. Once ready, select **Continue** on the bottom of the screen.

<p align="center">
<img src="../img/pod-settings-delivery-Limits.png" width="300">
</p>

Finally, you will be back to the `Pod Pairing` screen.

<p align="center">
<img src="../img/pod-pairing.png" width="300">
</p>

Instead of filling a new pod with insulin, attempt to pair again using the original pod which was previously filled but was unable to complete the pairing process successfully. That pod should still be beeping. Make sure to position the pod optimally with the flat pod surface up from the surface and the rounded side of the pod facing away from you and the RileyLink facing upwards on the left side of the pod with the RileyLink edge parallel to left side of the pod adhesive maintaining at least a 1 cm gap and the RileyLink antenna towards the cannula side of the pod. If possible, use the original plastic tray to hold the pod and to provide the optimal spacing.

<p align="center">
<img src="../img/pod-rileylink-positioning-no-tray.jpg" width="300">
</p>

Now hit the **Pair** button at the bottom of the screen and hopefully Loop will be able to successfully pair this time after starting the pairing from a clean slate. 

If you cannot get the pairing to complete with the pod (after trying following the Pod Pairing Recovery procedure described above a few times with multiple **Pair** during each try), then you should completely abandon that the pod before attempting to pair using another pod. "Completely abandon" means take that failed loser pod far, far away or in a microwave after doing the "switch from omnipods". You do not want that beeping pod or failed pod to be any way able to plague your next pod's communications with Loop during the pairing process for next pod.

### What about other pod start-up failures?

If you have a pod that has already started the priming operation and then has problems either finishing the priming operation or the cannula insertion, then forcing a pod pairing recovery is not possible. If a pod fails during priming or cannula insertion, the pod is no good and it should be deactivated and disposed of properly.

### What about that insulin?

If you have the misfortune of losing a pod during pairing, you can opt to not waste the insulin in that pod. Simply use the same syringe and same fill port on the pod to suck the insulin OUT of the loser pod. 

If you do that, good practice is to make sure that you get that loser pod far away from the process as you go forward. Mark a big "X" on the failed pod and put it in a microwave, or very far away from you, so that it can't interfere with subsequent pod pairing attempts.

### How can you help improve pod pairing process?

To help fix pairing bugs, some improvements have also been made in our ability to save the communications between the pods and Loop app during the pairing process. So, please help us leverage these new improvements and better squash bugs.

If you are using Loop v2.2 (April 2020) or later and you run into any pairing problems which required "Switch from Omnipod" pod pairing recovery to be able to pair or a pod that had to be abandoned, it would be helpful to generate an "Issue Report" after you finally get a pod paired (whether is was the original pod or if a different pod) and then submitting the resulting "Loop Report" on [Zulipchat here](https://loop.zulipchat.com/#narrow/stream/144111-general/topic/Omnipod.20Pairing.20Issues) with a short explanation of what happened.


