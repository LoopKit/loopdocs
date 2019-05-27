# Pod Pairing Failure

At the end of a pod life, you will deactivate your pod and then start the procedure for starting a new pod. You'll fill the new pod and it will start sending out periodic beeps while looking to establish a new pairing with your Loop. If during the pod pairing, you encounter troubles in Loop, here's some steps to take:

### Check RileyLink
First, let's make sure everything is ok as far as the RileyLink goes:

1. RileyLink is charged and nearby, and
2. RileyLink has a green LED light lit (indicating a bluetooth connection with your iPhone), and
3. Try toggling the RileyLink off/on at its physical switch if the green light is not on.

### Deactivate and Pair Fresh

Assuming the RileyLink is ok, the most common cause of a pod failure is that Loop kind of incorrectly "halfway" pairs. Imagine if you will that the pod is calling out "I'm here...over here. My name is Cassandra." And the Loop says "Oh...I hear you! Hi Cassie! Let's get together!!" Except the pod is actually Cassandra, not Cassie. So the pod will not pair. And worse...when you try to get another pod, Jane, in to replace Cassandra...that won't work either. Now there's Cassandra and Jane both screaming out for someone to pair with and your Loop app is still looking for Cassie. Two pods down and no closer to a pairing. (Obviously, I'm simplifying the description for ease of explanation.)

So...here's how to fix that. We need to get the Loop to stop looking for Cassie without insulting Cassandra. What we are going to do is leave Cassandra and Jane (and any other pods you've tried as well) out of the room, far away.

1. Take your RileyLink and iPhone and walk far away from all the beeping pods (Cassandras and Janes) looking to pair. How far away? Far enough away that there's no chance the beeping pods will hear the Loop app. We do not want the beeping pods to connect to the RileyLink or hear the commands we are about to do. (If you want, you could put the pods in a faraday bag or your microwave to shield them similar to what you might already do for Dexcom restarts.)

2. While you are out-of-range from the beeping pods, click on the `cancel` button in the upper right corner of the pairing screen you've been stuck on.

<p align="center">
<img src="../img/pod-pair-fail.jpg" width="300">
</p>

3. On the next screen, click on the button to `Deactivate Pod`. This will make the Loop app forget about the "Cassie" it has been trying to use to pair with, leaving Loop free to make a fresh pairing.

4. After you finish that deactivation, now come back into range of ONE of your beeping pods....just one of them. Pull that pod close to RileyLink and do the usual steps for pairing in Loop again. This should now give the pod and Loop a chance to get their pairing done properly.
