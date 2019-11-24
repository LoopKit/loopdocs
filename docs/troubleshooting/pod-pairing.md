# Pod Pairing Failure

At the end of a pod life, you will deactivate your pod and then start the procedure for starting a new pod. You'll fill the new pod and it will start sending out periodic beeps while looking to establish a new pairing with your Loop. If during the pod pairing, you encounter troubles in Loop, here are some steps to take:

### Check RileyLink
First, let's make sure everything is ok as far as the RileyLink goes:

1. RileyLink is charged and nearby, and
2. RileyLink has a green LED light lit (indicating a Bluetooth connection with your iPhone), and
3. Try toggling the RileyLink off/on at its physical switch if the green light is not on.

### What is the Failure?

Assuming the RileyLink is ok, the most common cause of a pod failure is that Loop kind of incorrectly "halfway" pairs with a pod and leaves you in a glitch. To understand this better, let's walk through the pairing process as if these are people and not pods.

Imagine if you will that the new pod, freshly filled with insulin, is beeping out "I'm here...over here. My name is Cassandra. Come pair with me!" It's going to beep for the next 60 minutes looking for a friend to pair with. When Cassandra hears her named called back from someone, she will pair with it.

<p align="center">
<img src="../img/pod-pair-fail2.png" width="400">
</p>

And now you press the pair button to tell Loop to go find a pod. Loop listens for a beeping pod to find a new pod to pair with, but he accidentally screws up when he hears Cassandra's beeping. Instead of hearing "Cassandra" as the name, he thought he heard the pod saying it was named "Cassie". So now Loop is looking for Cassie to pair with.  He's calling out "Oh...I heard you, Cassie! Let's finish this pairing!! Call me back!" Except Cassandra won't answer because Loop's only calling out for Cassie. Eventually, Loop tells you that the pod (Cassie) isn't responding after all. Sad face. And Cassandra is left hanging without a friend.

<p align="center">
<img src="../img/pod-pair-fail-cassie.jpg" width="300">
</p>

And worse some people blame the pod without realizing understanding what just happened. And the error message kinda blames the pod..so logically some people assume a new pod will fix it. But that won't work either. Jane and Cassandra are both outta luck because Loop is bound and determined that it has a friend named Cassie somewhere around, and it will not stop looking for Cassie in particular. Two pods down and no closer to a pairing. 

<p align="center">
<img src="../img/cass-and-jane.png" width="300">
</p>

## What is the fix?

So...here's how to fix that issue. **We need to get Loop to stop looking for Cassie** without insulting all the other pods that are still looking for a friend. What we are going to do is leave Cassandra and Jane (and any other pods you've tried as well) out of communication range. We are going to make Loop breakup with Cassie and we don't want the other pods accidentally hearing.

1. Take the beeping pod(s) (Cassandra, and Jane if you have a Jane) far away from you. How far away? Far enough away that there's no chance the beeping pod(s) will hear the Loop app. We do not want the beeping pod(s) to connect to the RileyLink or hear the commands we are about to do. Putting the beeping pod(s) in a microwave is a great place to put pods out of communication range...it's an effective silence box for wireless communications.)

2. After the beeping pod(s) are hidden away, click on the `cancel` button in the upper right corner of the pairing screen you've been stuck on. Click `cancel` as many times as it takes to get to a screen with `Deactivate Pod` button at the bottom...that's the next screen we are interested in getting to.

<p align="center">
<img src="../img/pod-pair-fail.jpg" width="300">
</p>

3. Click on the button to `Deactivate Pod`. This will make the Loop app forget about "Cassie", leaving Loop free to make new friends (i.e., pair with a new pod). Click `Deactivate Pod` a couple times and you'll might see a failure of that, too. Totally normal because it's trying to deactivate Cassie and she doesn't exist.

4. So, after all this, if you hit `cancel` for the deactivation screen you will eventually be put back at a `pair new pod` or `add pump` screen again (depending on how far back you go in the process). That's good. That means that Loop has finally forgotten about Cassie and we can start fresh with making a new friend.

5. Now we want to pull just ONE of your beeping, insulin-containing pods from the microwave Get to the screen in the pairing process that has the `Pair` button and push it. The pod and Loop now have a fresh chance to get their pairing/name recognition done properly this time. More than likely Loop will hear the pod's name properly this time and you'll get through the pairing process just fine.
