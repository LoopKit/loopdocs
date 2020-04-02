# General Loop FAQs

Welcome to LoopDocs - a place for all things Frequently Asked.

## What is Loop?

Click on the image below to watch a short [Introduction to Loop video](https://youtu.be/qw_u1lqboCs).

<a href="https://youtu.be/qw_u1lqboCs" target="_blank"><img src="../img/intro-to-loop.png"  title="Introduction to Loop video" /></a>

## What do I need to Loop?

Loop has both hardware and software requirements. In general, to use Loop you need to have seven components.

- Compatible insulin pump: [Medtronic or Omnipod](https://loopkit.github.io/loopdocs/build/step3/)
- [Compatible CGM](https://loopkit.github.io/loopdocs/build/step4/)
- [RileyLink](https://loopkit.github.io/loopdocs/build/step5/)
- [Compatible iPhone/iPod Touch](https://loopkit.github.io/loopdocs/build/step2/)
- [Apple computer running Mojave macOS 10.14.3 or later](https://loopkit.github.io/loopdocs/build/step1/)
- [Xcode (a free Apple application)](https://loopkit.github.io/loopdocs/build/step8/)
- [Apple Developer Membership](https://loopkit.github.io/loopdocs/build/step6/)

<p align="center">
<img src="../img/loop_gear.jpg" width="500">
</p>

## Can I download Loop from the App store?

No. Loop is not available for download. You must build your own Loop app. Loop app will not be available in the Apple App store because that would be distribution of a medical device, and we are not in that "business".  You can build yourself, but we are not distributors.

Don't worry though, building your Loop app is actually quite easy and that's what these docs are all about. The harder part will be having the patience to read all the documents before you start. New Loop users are so excited to get started that they skip reading all the great info that these docs contain. So, as you begin the build...please include time to read the documents that follow what happens AFTER you successfully build your Loop app.

If you have any questions, these docs have a nice search feature in the dark blue top menu bar that may help you find your answers pretty quickly too.

## Can I use an android phone for Loop?

No, this is purely iPhone or iPod touch.

## Do I have to be "tech-smart" to build Loop?

No. You do not need any experience in code or computers to build Loop. If you have already owned an Apple computer and iPhone, you already have the required level of experience. Beyond that, simply read the directions slowly and diligently...all the information you will need are in these documents.

Often times the non-tech people do better than the tech people in building Loop. Why? Because the non-tech people take the time to read slowly and look at the screenshots in the directions. The tech people often skim read and miss sentences...which then leads to build errors that have to be retraced and fixed.

## Is there a cheat sheet for a school nurse to use?

Sure, you can give this one a try. [School nurse's cheat sheet download](https://github.com/Kdisimone/images/raw/master/school_nurse.pdf)

## How long does it take to build Loop?

The answer is varied, but a few hours from start to finish, depending on where you are starting and how comfortable you are with your computer.

If you'd rather break it up into several shorter bits of effort, the [`Build App`](https://loopkit.github.io/loopdocs/build/step1/) section is divided into convenient stopping points with Time Estimates for each step. You can do one or more steps depending on what kind of time you have available.

## Does Loop cost money?

Yes, there are some costs, beyond the obvious costs of owning a pump and CGM.

The [RileyLink kit](https://getrileylink.org/) costs $150. This is a one-time cost and many people still have their original RileyLinks from nearly 3 years ago running just fine. I highly recommend purchasing two RileyLinks when financially feasible, to have one as a backup in case of accidental damage.

The Apple Developer License can be done for free, however, you will have to rebuild your Loop app every 7 days. That could get very tedious. The $99 annual Apple Developer program enrollment is an excellent investment.

There are no other costs, ongoing or initial, to use Loop.

## Do I need to own my own Apple computer?

You don't have to own your own Apple computer, but you do need to at least borrow one. It would be really good to have longer term ability to borrow that computer again for [updating Loop](https://loopkit.github.io/loopdocs/build/updating/#when-to-update) later, when needed.

If you are borrowing an Apple computer, you should ask the person to (1) update to Mojave and (2) [download Xcode for free](https://developer.apple.com/xcode/) before you get together to build your Loop app. The updates and download of Xcode can take a couple hours depending on the person's internet speed...so best to do those steps well ahead of time to save trouble.

## Can I use a PC or Windows computer to build?

Yes, you can...sort of. There is a hacked way of installing macOS on a Windows computer called "Virtual Machine". [This link](https://macosvmware.tech.blog/) may provide some helpful information for that if you want to learn more...but it's up to you and Google if you hit a road block. This Virtual Machine method will not work on PCs that have AMD processors either, so double check your computer before to confirm you don't have an old AMD processor. These docs do not provide troubleshooting tips for Virtual Machine installation or use.

## How often do I need to get on the computer for Loop?

The short answer is (1) when you first build and (2) once per year minimum after that. (If you decide to use a free Apple Developer Account, you will need to get on the computer every 7 days.)

The longer answer is that Loop code is updated periodically to include new features and bug fixes. When those updates are released, you'll need access to an Apple computer again to update your Loop app.  Loop updates are not available through the iPhone's app store...instead you do the app update yourself with [update instructions here](https://loopkit.github.io/loopdocs/build/updating/). In general, probably a few times a year there are updates to Loop released that you'd want to take the time to install.

## Will I need to build a new Loop if I switch between Medtronic and Omnipod?

No. Loop will have the option to move between different pump types from within the same Loop app. You'll simply use the "Switch from Omnipods" or "Delete Pump" options to move to the other kind of pump.

## Can I use someone else's Apple Developer account for my Loop build?

Technically, yes...however there are major drawbacks. The person's developer account can only be "linked" to a limited number of build computers. So one person "loaning out" their developer license to a lot of people will quickly exceed the number of allowed computers. In those cases, that person will be told they need to revoke the certificates on some computers (essentially dropping old ones to make room for new ones). When they do that, they may have forgotten about your Loop app on your computer. When they revoke your computer's certificate (and they can do that without you knowing through their developer portal), your Loop app will immediately stop working and not even open.

Your Loop app will also die immediately if their developer account is not renewed or expires. Your Loop updates will also not be able to be built unless that person maintains the developer license agreement updates.

Moral of the story, out of all the ways to save money...borrowing someone's developer account is not a good place to save money. You could find yourself unexpectedly without a Loop app without notice.

## Can I use MY Apple Developer account to build for others?

Technically yes...however, there are reasons this is discouraged. When you build for others, you must be careful to not unintentionally revoke the signing certificate that had been used for other people's apps (see note in FAQ above). You also need to let the people know that the MAXIMUM their app will last is 12 months. It will need to be rebuilt no matter what every 12 months.

But the biggest issue with building for others is that they may be left without a decent method of getting Loop updates. There are a lot of new Loopers on Omnipod system and their apps will likely need updating on a regular basis over the first year. Unless you plan on meeting with that person regularly to update their app, you could leave them on an old app that doesn't work as well as the new versions.

## How can I find a compatible pump? supplies?

There is a [whole page with detailed information about Medtronic pumps](https://loopkit.github.io/loopdocs/build/step3/); how to find them, how to find supplies, and assessing whether your Medtronic pump is compatible. Please check out that page for more info.

With the addition of Omnipod support, you can also now use Omnipod suppliers the way you'd normally source them.

## Can I pay someone else to do this?

NOOOO...you really need to figure this out yourself. This is an automated insulin delivery system and you really need to know how to build and operate this yourself.

## What if I lose my RileyLink?

For Medtronic users, you simply go back to old school pump use until you get a new RileyLink. You can either let your temp basal finish by itself (30 minutes or less) or cancel the temp basal on the pump's menu. For bolusing, you'd go back to using the pump's bolus commands. When you get a RileyLink (either finding your old one or getting your backup RileyLink out) and Loop running again, you'll want to do one thing. Enter in any carbs to Loop that you may have eaten in the recent past that could still be affecting blood glucose. While Loop will read whatever insulin deliveries had happened while the RileyLink was missing, it will not read any carbs you entered into the pump...so make sure to add those to Loop and backdate them to the time they were eaten. That will help make the transition smoother to Looping again.

For Pod users, your Pod will finish any currently running temporary basal rate (maximum of 30 minutes) and then revert back to your scheduled basal rate. Without a RileyLink, you will not be able to affect any Pod use other than normal basals. No temp basals, suspends, or boluses will be possible, similar to if you were to lose your PDM. If you have a backup RileyLink, you can simply connect to the new RileyLink on the same Loop app and it will work with the existing pod session. If you don't have a backup RileyLink, you'll have to remove the pod and start a new pod paired with your PDM until you get a new RileyLink.

## What if I lose or get a new iPhone?

When you get a new iPhone, Loop will need to be built onto that new iPhone in the same way that you built on your old iPhone. Loop will not restore from any iCloud or iTunes backups, so make sure you plan on finding an Apple computer to rebuild on before you plan on Looping with the new iPhone.

## What about other pumps? When will they Loop?

Hey now...let's be grateful for what we have first. The ability to use Loop is the result of tremendous amounts of effort, time, and sacrifice by volunteers. Cracking the pumps for Loop use is a large undertaking. If and when another set of people spend a large amount of time figuring out other pumps, then they could conceivably be added to Loop. But, you don't need to let us know that you'd love to see more pumps compatible with Loop. So would we. There is just an awful lot of work that needs to happen and it is not easy nor quick.

Tandem pumps are not Loop compatible.
Animas pumps are not Loop compatible.
DASH pods are not Loop compatible.
And those all likely won't be compatible anytime in the future.

## Can I have more than one Loop app on a phone?

Yes, technically possible. You can have multiple Loop apps built onto the same iPhone. However, having multiple Loop apps on a single phone may lead to unexpected conflicts that can negatively affect your Loop's ability to stay green (keep looping). Additionally, your Pod will only work on one Loop app at a time anyways. So for smooth looping, just keep one Loop app on any phone for looping use. 

## Will I be able to Loop on a plane? Or in the mountains?

Yes. Loop does not require internet or cell coverage to work. So long as the Loop user has Bluetooth turned on on the iPhone (or iPod touch), then the Dexcom and RileyLink will still be able to do their work with Loop and your pump/Pod.

