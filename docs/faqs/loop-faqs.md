## What do I need to Loop?

Please click on the [Requirements](../intro/requirements.md#common-requirements){: target="_blank" } link.

## Can I download the *Loop* app from the App store?

No. The *Loop* app is not available for download. You must build your own *Loop* app. The *Loop* app app will not be available in the *Apple* App store because that would be distribution of a medical device, and we are not in that "business".  You can build yourself, but we are not distributors.

Each step needed to successfully build your *Loop* app is found in these docs. The harder part will be having the patience to read all the documents before you start. New *Loop* users are so excited to get started that they often skip reading all the great info that these docs contain. As you begin the build...please include time to read the documents that follow what happens **after** you successfully build your *Loop* app.

If you have any questions, use the [Search](../intro/loopdocs-how-to.md#website-search) feature to find topics in LoopDocs.

## Can I use an android phone or iPad for Loop?

Loop requires an *Apple* device. Older iPads do not support *Apple* Health which is required for Loop. It may be possible with newer iPads and newer iOS, but this has not been tested.

There is open source software that runs on Android phones. Check out [AndroidAPS Documention](https://androidaps.readthedocs.io/en/latest/){: target="_blank" }.

## Do I have to be "tech-smart" to build Loop?

No. You do not need any experience in code or computers to build Loop. If you already own a computer or tablet and an iPhone, you already have the required level of experience. Beyond that, simply read the directions slowly and diligently...all the information you will need are in these documents.

Often times the non-tech people do better than the tech people in building Loop. Why? Because the non-tech people take the time to read slowly and look at the screenshots in the directions. The tech people often skim and miss steps...which then leads to build errors that have to be retraced and fixed.

## Is there a cheat sheet for a school nurse to use?

Sure, you can give this one a try. [School nurse's cheat sheet download](https://github.com/Kdisimone/images/raw/master/school_nurse.pdf){: target="_blank" }

## How long does it take to build Loop?

The answer is varied, but a few hours from start to finish, depending on where you are starting and how comfortable you are with your computer.

Start at the [Requirements Overview](../intro/requirements.md){: target="_blank" } to decide which build method you wish to use. Each method starts with an overview page.

Once you choose your method, you can break the required steps into shorter bits of effort.

* The Browser Build method has suggested breakpoints as you work through configuring for the first time
* The *Mac* Build method is broken into different pages for steps needed for the *Mac* and the actual build process


## Does the *Loop* app cost money?

Yes, there are some costs, beyond the obvious costs of owning a pump and CGM.

* If you have a pump that requires a [RileyLink Compatible Device](../build/rileylink.md#rileylink-compatible-devices), expect to spend $150 each (or find a used one). You should have two, one as a spare.
* Most people use a paid *Apple* Developer Account ($99/year)
    * With a paid developer account, you can build using the [Build with Browser](../browser/bb-overview.md); no *Mac* required
* If you build on a *Mac* using *Xcode* [Build with *Mac*](../build/overview.md), you need a *Mac* or a PC with Intel chips on which you include a virtual Mac
    * The *Mac* must be kept up to date with recent operating system
    * The *Xcode* app (from from Apple) must also be updated regular

There are no other costs, ongoing or initial, to use the *Loop* app beyond what you already pay for your CGM, pump supplies and insulin.

## RileyLink Options

**This is not required for DASH users.**

There are several options for [RileyLink Compatible Devices](../build/rileylink.md#rileylink-compatible-devices) at this time.  They typically cost around $150. This is a one-time cost and the devices should last for years (unless it goes swimming, goes through the wash, gets run over by a car, etc.). It's fine to buy one device and make sure you want to Loop, but if you can afford it, go on and get two or get two different kinds. Once you Loop, you'll want a backup.

Many used devices are available in the community. You may find posts for resale on this Facebook Group [Looping in a time of covid](https://www.facebook.com/groups/1087611668259945){: target="_blank" }. This is a private FB group where you must agree to the rules.

!!! warning ""
    Posts offering to buy or sell items in the support FB groups like The Looped Group, Loop and Learn or Little Loopers will be immediately taken down, or you will be directed to the appropriate location and comments will be turned off. FB can shut down groups without warning if they detect sales and the support groups are too important to risk.

## Free Developer Account Options

The *Apple* Developer License can be done for free, however, you will have to rebuild your *Loop* app every 7 days and you must use a computer with Xcode, [Build with *Mac*](../build/overview.md). That could get very tedious. The $99 annual *Apple* Developer program enrollment is an excellent investment.

## Do I need to own my own *Apple* computer?

You no longer need to own an *Apple* computer - see [Build with Browser](../browser/bb-overview.md).

If you chose [Build with *Mac*](../build/overview.md), then you still don't **have** to own an *Apple* computer, but you do need to at least borrow one - or you can build using a virtual *Mac* if you have a PC with Intel chips (see next section).

If you are borrowing an *Apple* computer, look at the required minimum settings associated with your iPhone [Compatible Computer](../build/computer.md#check-your-macos-version)) and [Xcode Version](../build/xcode-version.md#how-do-all-the-minimum-versions-relate-to-each-other). It would be really good to have the longer-term ability to borrow that computer again for [updating Loop](../build/updating.md#when-to-update-loop) later when needed.

## Can I use a PC or Windows computer to build?

You can build the *Loop* app using just a browser on any device: [Build with Browser](../browser/bb-overview.md).

If you want to use [Build with *Mac*](../build/overview.md), there is a hacked way of installing macOS on a Windows computer called a **Virtual Machine**. [This link](https://macosvmware.tech.blog/){: target="_blank" } provides some helpful information. This **Virtual Machine** method will not work on PCs that have AMD processors, only Intel. Double-check that your computer uses an Intel processor before attempting the virtual machine method. If you want to try this, there are mentors on [The Looped Facebook Group](https://www.facebook.com/groups/TheLoopedGroup){: target="_blank" } who can assist.

## How often do I need to get on the computer for Loop?

When you use the Browser Build method, you need to access a browser at least once every 90 days to [Update with Browser](../browser/bb-update.md). This is simple enough to do that you can do the steps on your phone in just a few minutes. Several people are already working on automated methods so that won't be required, but a manual Build Actions step is required for now.

When you use Build with *Mac*: the short answer is (1) when you first build and (2) once per year minimum after that. (If you decide to use a free *Apple* Developer Account, you will need to get on the computer every 7 days.)

Loop code is updated periodically to include new features and bug fixes. When those updates are released, you'll need access to a browser or an *Apple* computer again to update your *Loop* app.  

Loop updates are **not** available through the iPhone's app store...instead you do the app update yourself

* If using Browser build method: use this link: [Update with Browser](../browser/bb-update.md#how-to-update-or-rebuild) 
* If using build with *Mac* method: use this link: [update instructions](../build/updating.md)

In general, there are updates to the *Loop* app released a few times a year - these can occur more frequently after a major release.

## Will I need to build a new *Loop* app if I switch between Medtronic and Omnipod?

No. The *Loop* app lets you move between different pump types from within the same *Loop* app. See [Change Pump Type](../loop-3/add-pump.md#change-pump-type){: target="_blank" }.

## Can I use my *Apple* Developer account to build for others?

If there is more than one Looper in the family, you only need to have one *Apple* Developer ID and only one annual payment. The developer must be an adult.

* With the [Build with Browser](../browser/bb-overview.md) method, you just add each Looper to your TestFlight test group and they get updates whenever you Build a new version on GitHub.

* With the [Build with Mac]() method, you just plug into your computer each phone on which you want to build the *Loop* app. (New *Xcode* and newer *iOS* phones allow you to build across WiFi after the initial connection with *Xcode*.)

It's a good idea to let someone else in the family know how to build and have access to your *Apple* password (and for Browser Build, your GitHub password) in case you're out of town. It's also a good idea to build the *Loop* app on a backup phone especially for travel. 

The *Apple* Developer ID and the *Apple* ID are two different things. PLEASE read this: [Loopers Need Their Own *Apple* ID](../build/apple-developer.md#loopers-need-their-own-apple-id).


## What happens when I switch *Apple* Developer ID?

The *Loop* app on the phone is different if the build uses a different *Apple* Developer ID from the one currently on the phone. So if the *Apple* Developer ID used for a new *Loop* build is different from the one used for the existing *Loop* app, there will be two *Loop* apps on the phone.  The Looper will have to on-board the new app, enter all the settings again and delete the old app.

## Can I use someone else's *Apple* Developer account?

It's best that you build your own *Loop* app using your own *Apple* Developer ID.

One developer account can only be "linked" to a limited number of devices. So one person "loaning out" their developer license to a lot of people will quickly exceed the number of allowed devices. In those cases, that person will be told they need to revoke the certificates on some devices (essentially dropping old ones to make room for new ones). If they revoke your device certificate (and they can do that without you knowing through their developer portal), your *Loop* app will immediately stop working and not even open.

Your *Loop* app will also die immediately if their developer account is not renewed or expires.

Moral of the story, out of all the ways to save money...borrowing someone's developer account is not a good place to save money. You don't want your *Loop* app to suddenly stop working.


## How can I find a compatible pump? supplies?

You can use Omnipod DASH and Eros pumps with the *Loop* app. You do not need the Omnipod Personal Diabetes Manager (PDM), just the pod supplies. Your insurance or pharmacy coverage may cover some of the cost. See [Which pods work with the *Loop* app?](omnipod-faqs.md#which-pods-work-with-the-loop-app) for more details.

There is a [whole page with detailed information about Medtronic pumps](../build/pump.md#check-medtronic-pump-version); how to find them, how to find supplies, and assessing whether your Medtronic pump is compatible. Please check out that page for more info.

Some Looping equipment can be found on this Facebook Group [Looping in a time of covid](https://www.facebook.com/groups/1087611668259945){: target="_blank" }. This is a private FB group where you must agree to the rules.

## Can I pay someone else to do build the app for me?

We do not know whether someone who builds the app for you incurs legal responsibility if something goes wrong while you are using a version they built for you.

There are a few companies that provide the *Loop* app as a service.

!!! warning "Best Practice: Learn to Build"
    You are strongly encouraged to build the *Loop* app for yourself. 

    * No links to providers who build the *Loop* app as a service  are found in LoopDocs
    * If you choose to use such a service, before you begin, you should:
        * Read all of LoopDocs
        * Know how to Set up, Operate and Troubleshoot Loop
        * **These steps are important for your safety**

## What if I lose my RileyLink Compatible Device?

For Medtronic users, you simply go back to old school pump use until you get a new RileyLink compatible device. You can either let your temp basal finish by itself (30 minutes or less) or cancel the temp basal on the pump's menu. For bolusing, you'd go back to using the pump's bolus commands. When you get a device (either finding your old one or getting your backup device out) and the *Loop* app running again, you'll want to do one thing. Enter in any carbs to the *Loop* app that you may have eaten in the recent past that could still be affecting blood glucose. While the *Loop* app will read whatever insulin deliveries had happened while the RileyLink compatible device was missing, it will not read any carbs you entered into the pump...so make sure to add those to the *Loop* app and backdate them to the time they were eaten. That will help make the transition back to closed loop smoother.

For Pod users, your Pod will finish any currently running temporary basal rate (maximum of 30 minutes) and then revert back to your scheduled basal rate. Without a RileyLink compatible device, you will be receiving normal basals, but will need to pull out pens/syringe for boluses. If you have a backup device, you can simply connect to the new device on the same *Loop* app and it will work with the existing pod session. If you don't have a backup device, you'll have to remove the pod and start a new pod paired with your PDM until you get a new device.

## What if I lose or get a new iPhone?

If you lose your phone - follow the same dosing protocol as if you lost your [rileylink](#what-if-i-lose-my-rileylink-compatible-device).

When you get a new iPhone, you can plan ahead. There's a whole FAQs page about transferring your *Loop* information to a new phone. [New Phone](new-phone.md).

## What about other pumps? When will they Loop?

Hey now...let's be grateful for what we have first. The ability to use the *Loop* app is the result of tremendous amounts of effort, time, and sacrifice by volunteers. Cracking the pumps for the *Loop* app use is a large undertaking. If and when another set of people spend a large amount of time figuring out other pumps, then they could conceivably be added to Loop. But you don't need to let us know that you'd love to see more pumps compatible with Loop. There is just an awful lot of work that needs to happen and it is neither quick nor easy.

* Tandem pumps are not compatible
* Omnipod DASH pods are compatible
* Omnipod 5 pods are not compatible
* Newer Medtronic pumps are not compatible

## Can I have more than one *Loop* app on a phone?

Yes, this is technically possible. You can have multiple *Loop* apps built onto the same iPhone. However, having multiple *Loop* apps on a single phone may lead to unexpected conflicts that can negatively affect your Loop's ability to stay green (keep looping). Additionally, your Pod will only work on one *Loop* app at a time anyways. So for smooth looping, just keep one *Loop* app on any phone for looping use.

## Will I be able to the *Loop* app on a plane? Or in the mountains?

Yes. The *Loop* app does not require internet or cell coverage to work. So long as the *Loop* user has Bluetooth enabled on the iPhone, then the CGM and DASH pod (or RileyLink for Eros or Medtronic pumps) will still be able to do their work with the *Loop* app and your pump/Pod.

One exception - if you've chosen to use a CGM source that does require the internet, you will need to have cell or internet coverage. This ability is provided as a service to folks who cannot get their CGM data any other way. It is also a convenience for people testing the code.

## What happened to FreeAPS?

[FreeAPS](https://www.loopandlearn.org/freeapsdoc){: target="_blank" } hasn't really had an owner to develop it for several years, but many depended on it. Because of that, the *Loop and Learn* team kept it on life-support. It was updated in early 2023 to include DASH, but that was the last improvement. It is strongly recommended people switch to `Loop 3` or `Trio`. Do not use an application without an owner.

Many features people used with FreeAPS are now included in `Loop 3` or can be added with customization. The `dev` branch has Libre support, see [Build *Loop* Dev](../version/build-dev.md).

The addition of customizations has been simplified.

* If you build with a browser, refer to [Customize with Browser](../browser/custom-browser.md)
* If you build with a *Mac*, refer to [Customize with *Mac*](../build/custom-mac.md)

Please do not blindly apply customizations. First read the documentation provided at the links above carefully.
