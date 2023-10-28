## What do I need to Loop?

Please click on the [Requirements](../intro/requirements.md) link.

## Can I download Loop from the App store?

No. Loop is not available for download. You must build your own Loop app. Loop app will not be available in the Apple App store because that would be distribution of a medical device, and we are not in that "business".  You can build yourself, but we are not distributors.

Each step needed to successfully build your Loop app is found in these docs. The harder part will be having the patience to read all the documents before you start. New Loop users are so excited to get started that they often skip reading all the great info that these docs contain. As you begin the build...please include time to read the documents that follow what happens **after** you successfully build your Loop app.

If you have any questions, use the [Search](../intro/loopdocs-how-to.md#website-search) feature to find topics in LoopDocs.

## Can I use an android phone or iPad for Loop?

Loop requires an Apple device. Older iPads do not support Apple Health which is required for Loop. It may be possible with newer iPads and newer iOS, but this has not been tested.

There is open source software that runs on Android phones. Check out [AndroidAPS Documention](https://androidaps.readthedocs.io/en/latest/).

## Do I have to be "tech-smart" to build Loop?

No. You do not need any experience in code or computers to build Loop. If you have already owned an Apple computer and iPhone, you already have the required level of experience. Beyond that, simply read the directions slowly and diligently...all the information you will need are in these documents.

Often times the non-tech people do better than the tech people in building Loop. Why? Because the non-tech people take the time to read slowly and look at the screenshots in the directions. The tech people often skim read and miss sentences...which then leads to build errors that have to be retraced and fixed.

## Is there a cheat sheet for a school nurse to use?

Sure, you can give this one a try. [School nurse's cheat sheet download](https://github.com/Kdisimone/images/raw/master/school_nurse.pdf)

## How long does it take to build Loop?

The answer is varied, but a few hours from start to finish, depending on where you are starting and how comfortable you are with your computer.

If you'd rather break it up into several shorter bits of effort, the [`Build App`](../build/overview.md) section is divided into convenient stopping points with Time Estimates for each page. You can do one or more pages at a time, depending on what kind of time you have available.

## Does Loop cost money?

Yes, there are some costs, beyond the obvious costs of owning a pump and CGM.

* If you have a pump the requires a [RileyLink Compatible Devices](../build/rileylink.md#rileylink-compatible-devices), expect to spend $150 each (or find a used one). You should have two, one as a spare.
* Most people use a paid Apple Developer Account ($99/year)
    * With a paid developer account, you can build using the [Browser Build](../gh-actions/gh-overview.md); no Mac required
* If you build on a Mac using Xcode [Mac-Xcode Build](../build/overview.md), you need a Mac or a PC with Intel chips on which you include a virtual Mac

There are no other costs, ongoing or initial, to use Loop beyond what you already pay for your CGM, pump supplies and insulin.

## RileyLink Options

This is not required for DASH users.

There are several options for the [RileyLink Compatible Devices](../build/rileylink.md#rileylink-compatible-devices) at this time.  They typically cost around $150. This is a one-time cost and the devices should last for years (unless it goes swimming, goes through the wash, gets run over by a car, etc.). It's fine to buy one device and make sure you want to Loop, but if you can afford it, go on and get two or get two different kinds. Once you Loop, you'll want a backup. Because some of the newer versions have features some people prefer, you may find posts on [The Looped Facebook Group](https://www.facebook.com/groups/TheLoopedGroup) offering to sell their RileyLink for a reduced cost.

## Free Developer Account Options

The Apple Developer License can be done for free, however, you will have to rebuild your Loop app every 7 days and you must use a computer with Xcode, [Mac-Xcode Build](../build/overview.md). That could get very tedious. The $99 annual Apple Developer program enrollment is an excellent investment.

## Do I need to own my own Apple computer?

You no longer need to own an Apple computer - see [Browser Build](../gh-actions/gh-overview.md).

If you chose [Mac-Xcode Build](../build/overview.md), then you still don't **have** to own an Apple computer, but you do need to at least borrow one - or you can build using a virtual Mac if you have a PC with Intel chips (see next section).

If you are borrowing an Apple computer, look at the required minimum settings associated with your iPhone [Compatible Computer](../build/computer.md#macos) and [Xcode Version](../build/xcode-version.md#how-do-all-the-minimum-versions-relate-to-each-other). It would be really good to have longer term ability to borrow that computer again for [updating Loop](../build/updating.md#when-to-update) later, when needed.

## Can I use a PC or Windows computer to build?

You can build Loop using just a browser on any device: [Browser Build](../gh-actions/gh-overview.md).

If you want to use [Mac-Xcode Build](../build/overview.md), there is a hacked way of installing macOS on a Windows computer called a **Virtual Machine**. [This link](https://macosvmware.tech.blog/) provides some helpful information. This **Virtual Machine** method will not work on PCs that have AMD processors, only Intel. Double check that your computer uses an Intel processor before attempting the virtual machine method. If you want to try this, there are mentors on [The Looped Facebook Group](https://www.facebook.com/groups/TheLoopedGroup) who can assist.

## How often do I need to get on the computer for Loop?

When you use the Browser Build method, you need to access a browser at least once every 90 days to [Update with Browser](../gh-actions/gh-update.md). This is simple enough to do that you can do the steps on your phone in just a few minutes. Several people are already working on automated methods so that won't be required, but a manual Build Actions step is required for now.

When you use Mac-Xcode Build: the short answer is (1) when you first build and (2) once per year minimum after that. (If you decide to use a free Apple Developer Account, you will need to get on the computer every 7 days.)

Loop code is updated periodically to include new features and bug fixes. When those updates are released, you'll need access to a browser or an Apple computer again to update your Loop app.  

Loop updates are **not** available through the iPhone's app store...instead you do the app update yourself

* If using Mac-Xcode build: use this link: [update instructions](../build/updating.md)
* If using Browser build: use this link: [Update with Browser](../gh-actions/gh-update.md#how-to-update-or-rebuild) 

In general, there are updates to Loop released a few times a year - these can occur more frequently after a major release.

## Will I need to build a new Loop if I switch between Medtronic and Omnipod?

No. Loop lets you move between different pump types from within the same Loop app.

## Can I use my Apple Developer account to build for others?

If there is more than one Looper in the family, you only need to have one Apple Developer ID and only one annual payment. The adult who builds can use their Apple Dev ID to put the app on the Looper's phone.  The limit is 99 devices (phone and watch both count).  Unless it's a very large family, you should have no problem supporting everyone in your family. Building Loop on the second phone is much faster than the first one. It's a good idea to let someone else in the family know how to build and have access to your Apple password in case you're out of town. It's also a good idea to build Loop on a backup phone especially for travel. The Apple Developer ID and the Apple ID are two different things. PLEASE read this: [Loopers Need Their Own Apple ID](../build/apple-developer.md#loopers-need-their-own-apple-id).

If you used the [Browser Build](../gh-actions/gh-overview.md) method, you just add each Looper to your TestFlight test group and they get updates whenever you issue a new Build Action on github.

## What happens when I switch Apple Developer ID?

The Loop app on the phone is different if the build uses a different Apple Developer ID from the one currently on the phone. So if the Apple Developer ID used for a new Loop build is different from the one used for the existing Loop app, there will be two Loop apps on the phone.  The Looper will have to on-board the new app, enter all the settings again and delete the old app.

## Can I use someone else's Apple Developer account?

It's best that you build your own Loop app using your own Apple Developer ID.

One developer account can only be "linked" to a limited number of devices. So one person "loaning out" their developer license to a lot of people will quickly exceed the number of allowed devices. In those cases, that person will be told they need to revoke the certificates on some devices (essentially dropping old ones to make room for new ones). If they revoke your device certificate (and they can do that without you knowing through their developer portal), your Loop app will immediately stop working and not even open.

Your Loop app will also die immediately if their developer account is not renewed or expires.

Moral of the story, out of all the ways to save money...borrowing someone's developer account is not a good place to save money. You don't want your Loop app to suddenly stop working.


## How can I find a compatible pump? supplies?

There is a [whole page with detailed information about Medtronic pumps](../build/pump.md#check-medtronic-pump-version); how to find them, how to find supplies, and assessing whether your Medtronic pump is compatible. Please check out that page for more info.

You can use some Omnipod pumps with Loop. You do not need the Omnipod Personal Diabetes Manager (PDM), just the pod supplies. Your insurance or pharmacy coverage may cover some of the cost.

Check your app version by tapping on Loop settings and reading it from the top of the screen.

* Version 2.2.x or earlier supports Omnipod Eros pumps and some older Medtronic pumps
* Version 2.3 or later supports Omnipod Eros and DASH pumps and some older Medtronic pumps

!!! info "Alternative Names for Omnipod Eros Pump and Pods"

    **Eros** pump is also known as **Classic**, or **UST400**, or *Omnipod Insulin Management* **System**.  

    Pharmacy sites sometimes may refer to the **Eros pods** as **Gen 3** but they are the same exact pods. 

DASH pumps do not require a RileyLink compatible device.

Omnipod 5 is not supported by any version of Loop.

## Can I pay someone else to do this?

We do not know whether someone who builds the app for you incurs legal responsibility if something goes wrong while you are using a version they built for you.

There are a few companies that provide Loop as a service.

!!! warning "Best Practice: Learn to Build"
    You are strongly encouraged to build Loop for yourself. 

    * No links to providers who build Loop as a service  are found in LoopDocs
    * If you choose to use such a service, before you begin, you should:
        * Read all of LoopDocs
        * Know how to Set up, Operate and Troubleshoot Loop
        * **These steps are important for your safety**

## What if I lose my RileyLink Compatible Device?

For Medtronic users, you simply go back to old school pump use until you get a new RileyLink compatible device. You can either let your temp basal finish by itself (30 minutes or less) or cancel the temp basal on the pump's menu. For bolusing, you'd go back to using the pump's bolus commands. When you get a device (either finding your old one or getting your backup device out) and Loop running again, you'll want to do one thing. Enter in any carbs to Loop that you may have eaten in the recent past that could still be affecting blood glucose. While Loop will read whatever insulin deliveries had happened while the RileyLink compatible device was missing, it will not read any carbs you entered into the pump...so make sure to add those to Loop and backdate them to the time they were eaten. That will help make the transition back to closed loop smoother.

For Pod users, your Pod will finish any currently running temporary basal rate (maximum of 30 minutes) and then revert back to your scheduled basal rate. Without a RileyLink compatible device, you will be receiving normal basals, but will need to pull out pens/syringe for boluses. If you have a backup device, you can simply connect to the new device on the same Loop app and it will work with the existing pod session. If you don't have a backup device, you'll have to remove the pod and start a new pod paired with your PDM until you get a new device.

## What if I lose or get a new iPhone?

If you lose your phone - follow the same dosing protocol as if you lost your [rileylink](#what-if-i-lose-my-rileylink-compatible-device).

When you get a new iPhone, you can plan ahead. The information found in the Update FAQs page, [What if I'm Changing Phones](update-faqs.md#what-if-im-changing-phones) section has more information.

## What about other pumps? When will they Loop?

Hey now...let's be grateful for what we have first. The ability to use Loop is the result of tremendous amounts of effort, time, and sacrifice by volunteers. Cracking the pumps for Loop use is a large undertaking. If and when another set of people spend a large amount of time figuring out other pumps, then they could conceivably be added to Loop. But you don't need to let us know that you'd love to see more pumps compatible with Loop. There is just an awful lot of work that needs to happen and it is neither quick nor easy.

* Tandem pumps are not Loop compatible.
* Omnipod DASH pods will be Loop compatible (when Loop 3 is released).
* Omnipod 5 pods are not Loop compatible.
* Newer Medtronic pumps are not Loop compatible.

## Can I have more than one Loop app on a phone?

Yes, this is technically possible. You can have multiple Loop apps built onto the same iPhone. However, having multiple Loop apps on a single phone may lead to unexpected conflicts that can negatively affect your Loop's ability to stay green (keep looping). Additionally, your Pod will only work on one Loop app at a time anyways. So for smooth looping, just keep one Loop app on any phone for looping use.

## Will I be able to Loop on a plane? Or in the mountains?

Yes. Loop does not require internet or cell coverage to work. So long as the Loop user has Bluetooth enabled on the iPhone, then the Dexcom and RileyLink will still be able to do their work with Loop and your pump/Pod.

One exception - if you've chosen to use a CGM source that does require the internet, you will need to have cell or internet coverage. This ability is provided as a service to folks who cannot get their CGM data any other way. It is also a convenience for people testing the code.

## What happened to FreeAPS?

[FreeAPS](https://www.loopandlearn.org/freeapsdoc) hasn't really had an owner to develop it for several years, but many depended on it. Because of that, the Loop and Learn team kept it on life-support. It was updated to include DASH, but that is the last expected improvement. It is strongly recommended people switch to Loop 3.

Many features people used with FreeAPS are now included in Loop 3 or can be added with customization. The dev branch has Libre support, see [Build Loop Dev](../version/build-dev.md).

The addition of customizations has been simplified with the [Loop and Learn: Customization Select Script](https://www.loopandlearn.org/custom-code). That script can be run stand-alone, selected as an option as part of the Build Select Script when doing a Mac-Xcode build or incorporated in a [GitHub Browser build customization](../gh-actions/gh-customize.md) by editing the build_loop.yml file.

Please do not blindly apply customizations. You should first read [LoopDocs: Customize Your Loop](../build/code-customization.md) and then [Loop and Learn: Code Customization](https://www.loopandlearn.org/custom-code).
