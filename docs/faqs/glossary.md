# Loop Build: Advent style

## Day 1: Check Computer

You need an Apple computer that has at least macOS 10.14 installed. This macOS is called Mojave. To find out if you have Mojave installed, click on the little Apple icon in your computer's upper left corner and select the `About this Mac`. It doesn't matter if the computer is a MacBook, iMac, macMini, etc...just so long as it has macOS Mojave. If your computer does not have Mojave, you'll need to check the `Software Update` button on that screen to see if you can update to Mojave.

<p align="center">
<img src="https://loopkit.github.io/loopdocs/setup/requirements/img/macosx.png" width="500">
</p>

If your computer does not give you the option to upgrade to Mojave...it is quite possible that Apple has decided your computer is too old to run Mojave. How old is too old? That will depend on your computer model and year as shown below:

<p align="center">
<img src="https://loopkit.github.io/loopdocs/setup/requirements/img/mojave-minimum.png" width="750">
</p>

!!!warning "Day 1: FAQs"
    * **"Can I use a PC or Windows computer? I don't own an Apple computer."** Yes...sort of. Please see [this FAQ about using Virtual Machine](https://loopkit.github.io/loopdocs/faqs/FAQs/#can-i-use-a-virtualmachine-to-build).
    * **"What can I do if my computer is too old to be upgraded to Mojave?"** You could take a look at using [Mojave Patcher](http://dosdude1.com/mojave/), but this is totally on your own and not part of these instructions. Just offering the answer to the FAQ...it is up to you to read about the patcher tool and what risks it may involve for you.
    * **"Can I borrow someone else's Apple computer?"** Yes, please see [this FAQ about borrowing a computer](https://loopkit.github.io/loopdocs/faqs/FAQs/#do-i-need-to-own-my-own-apple-computer) to learn more.

!!!info "Day 1: Work Summary"
    * Check your macOS and make sure it is Mojave.
    * Do use any of the beta macOS versions. (If you don't know what that means, don't worry...that means you aren't using one.)
    * If your macOS is not Mojave, check to see if you can up update your macOS to Mojave and do so.
    * If you cannot upgrade your existing computer to Mojave, you'll need to check into a borrowed computer, patcher tool, or perhaps a new/used computer compatible with Mojave.
    * Check the `Software Update` to see if your Mojave version has any updates available since you first installed it.


## Day 2: Compatible iPhone or iPod touch

Loop is compatible with iPhone and iPod touch devices that can run iOS 12 or newer. Therefore, compatible devices include:

* iPhone X, XS, XR, XS Max

* iPhone 8, 8+

* iPhone 7, 7+

* iPhone 6, 6+, 6s, 6s+

* iPhone SE

* iPhone 5s

* iPod Touch, 6th generation or newer

Technically, the iPhone SE and iPhone 5s will likely not be able to update to iOS 13 which will be coming out in the near future. So, they could be incompatible with Loop in the future. Loop users have reported that the iPhone 5s is more prone to be slow on display updates and Dexcom connection is less stable. 

Your phone's iOS version can be found under the Settings app, General, About as shown below.

<p align="center">
<img src="https://loopkit.github.io/loopdocs/setup/requirements/img/ios.png" width="300">
</p>

!!!warning "Day 2: FAQs"
    * **"Can I use an android?"** No.
    * **"But why not?"** Because Loop is written in Apple's Swift language, which does not compile onto Android operating systems.
    * **"Can I use an iPad?"** No. iPads do not support Apple Health and that is an important part of Loop's inner workings.
    * **"Does my iPhone need cell plan?"** No. Loop can work without an internet connection...however you will not have Dexcom Follow data or Nightscout data if you choose to use a device that doesn't have internet connection. In other words Loop will work, but remotely watching followers won't see Looping data.

!!!info "Day 2: Work Summary"
    * Check your iOS version and make sure you have 12.0 minimum.
    * Do not use any of the beta iOS versions. (Don't worry...if you don't know what that means, then you aren't using one.)
    
## Day 3: Compatible Pump

This is pretty simple...check that you have a compatible pump to use Loop.

* Medtronic 515 or 715 (any firmware)
* Medtronic 522 or 722 (any firmware)
* Medtronic 523 or 723 (firmware 2.4 or older)
* Medtronic Worldwide Veo 554 or 754 (firmware 2.6A or lower)
* Medtronic Canadian/Australian Veo 554 or 754 (firmware 2.7A or lower)

* Omnipod "Eros" pods

So by default that means any pump NOT mentioned above is NOT compatible. Your Medtronic 530G, 670G, etc are not Loop compatible. Nor is your Tandem, Omnipod DASH, Animas, Roche Combo, Dana-RS, etc.

Wondering how to find where the firmware is listed? Check out [this page's info](https://loopkit.github.io/loopdocs/setup/requirements/mdt-pump/#pump-firmware).

!!!warning "Day 3: FAQs"
    * **"But what about the other pumps?"** Too bad, so sad.
    * **"Can I change the firmware of my Medtronic pump?"** Do you work at Medtronic with insider access to the secret tools and firmware versions to do that? Might lose your job, but I'd bet you could then. We don't have access to that though.

!!!info "Day 3: Work Summary"
    * If you have a big clunky PDM with built-in BG meter...you can use your pods for Loop.
    * If you have a slim touch screen android-looking PDM...you can NOT use your pods for Loop.
    * If you have a Medtronic, check the list above to ensure compatible model/firmware.

## Day 4: Order a RileyLink

Today is an easy day. You need to order a RileyLink from the [GetRiley website](https://getrileylink.org). 

The RileyLink is a non-optional part of the Looping gear. Why do you need it? RileyLink is a communication bridge between the pump and your Loop app on your phone. The RileyLink speaks Bluetooth to your iPhone on one side, and speaks Radio Frequency to your pump on the other side.  Without the RileyLink, the pump cannot receive commands from the Loop app.

There are two types of RileyLinks; [one for Omnipod](https://getrileylink.org/product/rileylink433) users and [one for Medtronic](https://getrileylink.org/product/rileylink916) users. Order the RileyLink specifically for the pump you'll be Looping with. 

!!!warning "Day 4: FAQs"
    * **"What happens if I lose my RileyLink or walk away from it?"** Good question...answered [here](https://loopkit.github.io/loopdocs/faqs/rileylink-faqs/#what-happens-if-i-walk-away-from-my-rileylink).
    * **"Can I use an Omnipod RileyLink with a Medtronic pump? or vice versa?"** Good question...answered [here](https://loopkit.github.io/loopdocs/faqs/rileylink-faqs/#what-will-happen-if-you-use-a-916mhz-antenna-rileylink-with-an-omnipod-or-vice-versa).
    * **"Can I swap out RileyLinks at any time?"** Yes, you can. RileyLinks can be replaced quite simply without needing to start a new pod or rebuild Loop app. There's a place in Loop settings that you'd simply find your new RileyLink's name and turn "on" the Bluetooth connection to start using it."
    * **"How close does the RileyLink need to be to me? Do I have to carry it with me?"** Good questions...answered [here](https://loopkit.github.io/loopdocs/faqs/rileylink-faqs/#do-i-have-to-carry-the-rileylink-everywhere).
    * **"Why is it named RileyLink?"** Riley is the name of Pete Schwamb's daughter and he's the guy that created the RileyLink.
    * **"Can I make my own RileyLink?"** Technically yes, however it is not an easy project. You'll need specialized tools and patience. If you want to explore doing that, I'd highly recommend checking out [Zulipchat](https://loop.zulipchat.com/#narrow/stream/148542-RileyLink) from the other people who have done their own builds successfully over the last several years. Only 3 people have built their own RileyLinks so far...but I guess that technically means it is possble.
    
!!!info "Day 4: Work Summary"
    * Order your [Omnipod RileyLink](https://getrileylink.org/product/rileylink433) or [Medtronic RileyLink](https://getrileylink.org/product/rileylink916).

## Day 5: Download Xcode
 
Today is an easy one, but probably takes the longest of most of any of the days in terms of time...only because the download takes awhile. The good news is that you don't have to watch this. Instead, you can start the download and simply walk away for the rest of it.

Xcode is a free application for Apple computers. Xcode will turn the Loop "raw" code into an iOS application and install it onto your iPhone/iPod. **Make sure you have updated your macOS to Mojave AND checked the `Software Updates` button before proceeding...in other words, make sure you did Loop Advent Day 1's work.**

Open the App Store application on your computer (it is in your Applications folder). Search for Xcode and click on the link to download/install Xcode for free. The most current version of Xcode is 10.3. Do not download the Xcode beta program, just get the regular version of the program. The file size is fairly large so expect about 45 minutes, or even multiple hours, to download depending on your internet speed. 

If you already had a previous installation of Xcode, you can just check your App Store for Xcode updates.

<p align="center">
<img src="https://loopkit.github.io/loopdocs/build/img/xcode1.png" width="550">
</p>

!!!warning "Day 5: FAQs"
    * **"Why isn't my Xcode installing?"** I can't see your computer to know exactly why...but the two most common reasons are (1) lack of internet connection or (2) not enough free space on the computer's hard drive. Xcode is a pretty beefy sized download...and needs even a little more space to properly unpack itself and install. Best to try to have about 12-15GB of free space on your hard drive before starting to be on the safe side. If you get below 5GB of free space, I've seen installation failures around then. You can check your free space by clicking on the `About this Mac` (like in Day 1) and clicking the `Storage` tab.
    
!!!info "Day 5: Work Summary"
    * After making sure your Mojave is up-to-date, download Xcode from your computer's App Store application.

## Day 6: Enroll in Apple Developer Program

In order to build your own copy of the Loop app onto your iPhone/iPod touch, you will need an Apple developer account.  You will have two options for your individual account; free or paid.

### Free Developer Account

If you decide to use a **FREE** developer account, here's what you need to know:

1. Loop apps signed with a free developer team will expire after 7 days.  On the 7th day, your Loop app will simply turn white when you open it and then immediately close. To rebuild the Loop app, you will have to find a computer and rebuild the app onto your iPhone again. You cannot rebuild the app on day 5 (when it is convenient, for example)...hoping to reset the 7-day clock.  The app will still expire on the 7th day from when it was first signed and created.</br></br>
2. If you decide to switch to a paid account after trying out the free account, you will need to rebuild your Loop app in order to sign it with the new paid account.</br></br>
3. You will have to do an extra step during the build process to remove Siri capabilities in order to build with free accounts.</br></br>
4. This is just an FYI: In later steps when you build the Loop app in Xcode, you will select a signing "team" and Xcode will automatically generate a Provisioning Profile to "sign" the app...this is Apple's way of tracking the validity and safety of the app.  Free developer accounts will have a signing team that includes a "(Personal Team)" designation in the name.

<p align="center">
<img src="https://loopkit.github.io/loopdocs/build/img/team.jpg" width="450">
</p>

### Paid Developer Account

If you decide to use a **PAID** developer account, here's what you need to know:

1. Loop apps signed with a paid developer team will last for a full year.</br></br>
2. The paid developer account is $99 per year and is default set to auto-renew annually. You can change that selection in your developer account settings at any time.</br></br>
3. If your household has multiple Loop users, only one developer account is needed.  That one developer account can be used to sign multiple Loop apps.</br></br>

### Switching from Free to Paid Memberships

In summary: This is no problem trying a free account first before you decide to buy a paid developer account. If you start with a free account, you'll build a Loop app (let's call it FreeLoop). When you switch to a paid account, you'll be building a totally new and separate Loop app onto your phone (let's call it PaidLoop). The two apps will look identical on your phone, but they will be functionally separate from each other...ideally you want to delete the FreeLoop app before using the PaidLoop app.

PaidLoop will know nothing about the settings and information you had stored in FreeLoop, so you will need to re-enter all your settings (basal rates, ISF, carb ratios, etc.) and configurations into the new PaidLoop. It will also not connect or control any pods you are currently using with the old FreeLoop you had installed.

So, when switching from Free to Paid Loop builds...try to remember that you'll have the best luck by (1) timing it at pod change time and (2) take screenshots of your old app's settings so that you can enter them into the new app.

!!!warning "Day 6: FAQs"
    * **"Can I use someone else's Apple Developer account?"** Great question...answer is [here](https://loopkit.github.io/loopdocs/faqs/FAQs/#can-i-use-someone-elses-apple-developer-account).
    * **"Do I use my Apple ID or my kid's Apple ID to create the Apple Developer account?"** The Apple ID you use to enroll in the developer program does not need to be the same Apple ID as the Loop iPhone or Looper uses, for example a parent installing Loop on kid's iPhone. Typically for the developer enrollment, use the Apple ID of the person who will be doing the Loop app building. 
    * **"How long does it take to have my Apple Development account active after I enroll?"** After you enroll, make sure you look for a confirmation email. Apple says it can take up to 24-48 hours to confirm and setup a new Apple developer account, however some people have had the process only take minutes. It can vary. One SURE way to make it take longer? Use a different credit card to pay for the Apple Developer account enrollment than is already associated with the Apple ID you'll be enrollng with. When you do that, I've heard Apple makes you send in a xerox copy of your driver's license and a bunch of other hassle.

!!!info "Day 6: Work Summary"
    * If you've decided to you'd like to use a paid developer account, we need to get you enrolled. Go to the [Apple Developer website](https://developer.apple.com/programs/enroll/) to enroll in an individual account.
    * If you've decided you'd liek too use a free developer account, you don't need to do anything now. We'll get you covered later.

## Day 7: Install Homebrew

Breath deep...today's work looks kind of "programmer code" weirdness. BUT, it isn't. Well, it is...but we will be just smply copying and pasting one line of the weirdness and then walking away. We don't actually have to know much about Homebrew itself.

Homebrew is a program that will allow us to install the needed packages to build Loop. Open the Terminal application on your computer. Open your Applications folder and then look in the Utilities subfolder for the Terminal application.

<p align="center">
<img src="https://loopkit.github.io/loopdocs/build/img/terminal.png" width="550">
</p>

Terminal app is very plain looking when you open it. That is normal. Copy and paste the line in the little grey box below into Terminal prompt.  Press return after you paste it in.

`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

There will be a prompt asking if you want to continue.  Press return to continue, then it will prompt for your password.  <u>The password is your computer's password.</u>

**<u><font color = "red">Don't freak out that you can't see your password while you type. That is normal. Terminal app doesn't show keystrokes when you enter passwords, but it is still recording your password entry. If you think you messed up because you were confused, press the delete key a bunch of times and then start fresh with the password entry.</font></u>**  

Wait while the script does its thing...you’ll see info scroll by and then it will pause for awhile. Eventually, it will be done and you’ll see something that says “Installation successful” and you’ll have a ready Terminal prompt again.</br></br>

<p align="center">
<img src="https://loopkit.github.io/loopdocs/build/img/carthage.jpg" width="450">
</p>
</br>

You can close the Terminal application now. You’re done with it. You do not need to do these steps again for any subsequent Loop builds. This is one of those "just do it once" installations. If you get a new computer though, you will have to repeat this step for the new computer.

!!!warning "Day 7: FAQs"
    * **"What if I don't get an "Installation successful" message?"** If you don't see an installation successful message, then please try again. If you fail to get Homebrew installed, your Loop build will also fail. You can't just skip this step. The most common cause of errors are failing to copy the ENTIRE line of code ...people sometimes fail get that last `"` at end of the line. Also, you need to be using a user account on the computer that has "admin" rights, since this process is installing a program on the computer.
    
!!!info "Day 7: Work Summary"
    * Install Homebrew by simply copying and pasting that long line of gibberish into the ugly Terminal application.

## Day 8: Add Developer Account to Xcode

Since you've been working in order, you will now have Xcode installed on your computer from Day 5. You will also have enrolled in the Apple Developer program with a paid account, if that was your selection, in Day 6. Now we need to tell Xcode about your Developer Account.

Open Xcode from your Applications folder. 

### Command Line Tools
There may be a short delay the very first time you open Xcode because it will install a package of "Command Line Tools". Don't close that window out, let it finish...we will need those Command Line Tools. Helpful tip: When the Command Line Tools installation is done and the pop-up window closes, check that your Command Line Tools installed correctly. Open Xcode's Preferences by clicking on the word **`Xcode` ** in the top menu bar (just to the right of the Apple icon in upper left corner) and selecting `Preferences` in the drop down menu. The keyboard shortcut to open Xcode Preferences is `command-comma` if that's easier for you. Then select the `Locations` tab of Preferences window and you'll see the dropdown menu for Command Line Tools. Make sure that Xcode 10.3 (or newer) is selected there.
<p align="center">
<img src="https://loopkit.github.io/loopdocs/build/img/command-line-error-3.png" width="550">
</p>

### Add Apple ID
Go to the Xcode Preferences window from above, click on the `Accounts` tab and then press the `+` in the lower left corner to add an Apple ID account.

<p align="center">
<img src="https://loopkit.github.io/loopdocs/build/img/xcode_account.png" width="750">
</p>

If you want to use a free developer account, you will simply enter your Apple ID in this section and Xcode will automatically enroll your Apple ID in the free developer program. If you enrolled in the paid account already and have confirmation that your account is active, enter the Apple ID of the paid developer account. The screenshot below shows the labeling of team names based on whether from free account vs. paid account. Free teams will have `(personal team)` after the name.

<p align="center">
<img src="https://loopkit.github.io/loopdocs/build/img/apple_id.png" width="750">
</p>

You are now done setting up Xcode.  Great job!  You will not need to redo the account setup steps on any subsequent builds or updates of your Loop app.  Xcode will remember these settings.

!!!warning "Day 8: FAQs"
    * **"I still only see an account with `(personal team)` beside it even though I enrolled in the paid Developer Account program...what should I do?"** You should check your spam email box in case Apple sent you an email there. Make sure you've waited the 48 hours that Apple says it may take to get your account approved. If it's been 48 hours and you still don't see anything in your email, contact Apple support and ask them about the status of your enrollment. It may be held up by something on their end.
    
!!!info "Day 8: Work Summary"
    * Open Xcode Preferences and add your Apple ID under the Accounts tab.
    * Verify that Command Line Tools has been properly installed under Xcode Preferences under the Locations tab.
    
## Day 9: Test Settings

Loop is just a fancy calculator underneath the hood. The math problems that it is solving depend on some settings that you will be providing it. A good idea is to make sure you do a bit of settings testing before using Loop.

**Basal rates**, if properly set, will keep your blood glucose steady without food present. You can test your basals by having a relaxing set of 4-6 hours without eating at least two hours before you begin the test. Does your blood sugar stay steady? Or do you climb and need a correction? Or do you go low and need to eat? Setting basals is a HUGE important step to setting yourself up for Loop success.

**Insulin Sensitivity Factor** (sometimes called Correction Factor) is how much one unit of insulin will bring down your blood sugar. The higher the value of this setting, the more sensitive to insulin you are. An ISF of 30 means one unit of insulin bring your blood sugar down 30 mg/dL. You can test this setting after you get good basals set and tested. Simply bring yourself to a higher BG with a glucose tab or other small quick carbs. Wait until you see yourself plateau again at the higher BG, then take a correction. Wait 4-6 hours (again no food) and see where your correction lands your blood sugar. Divide the BG drop by the amount of correction insulin you delivered...that’s your ISF. 

**Carb Ratio** is the amount of carbs covered by one unit of insulin. Ideally a good carb ratio will bring your BG back to starting point within 2-3 hours* of the meal. (*High fat/protein meals may cause BGs to be impacted longer.) If you are spiking higher than you’d like after a meal but still coming back to starting BG, consider prebolusing your meal by 15-20 minutes rather than changing carb ratio. 

Check [LoopTips.org](https://looptips.org) for a discussion on how to [check all these settings](https://kdisimone.github.io/looptips/settings/settings/) and [why they are important](https://kdisimone.github.io/looptips/settings/overview/). If you’re fascinated by this topic, read the book <i>Think Like A Pancreas</i> for a really great discussion. Finally remember settings can change periodically. Hormone cycles, steroids, illness, etc may lead to a [need to change settings](https://kdisimone.github.io/looptips/settings/adjust/).

## Day 10: Make Plans for your data

Ok, technically this step could wait until after you build Loop app...but I have your attention now, so I'm taking advantage of it.

With Loop use, you will no longer be using your PDM (if you use Omnipods) and your pump (if you use Medtronic) will so full of temp basals that the endos will have nothing to download at your next visit. This [lack of data](https://kdisimone.github.io/looptips/data/overview/) will cause a little friction with the health care industry; not good for your insurance records, not good for your endo to feel comfortable, and not good for you to know how your Loop use might be improved with settings tweaks.

So let's explore options for your Loop data. There are three great options for where your Loop data can be stored and retrieved:

* [Apple Health app](https://kdisimone.github.io/looptips/data/health/)
* [Nightscout](https://kdisimone.github.io/looptips/data/nightscout/)
* [Tidepool](https://kdisimone.github.io/looptips/data/tidepool/)

All of the options are free and easy to setup. Take some time to familiarize yourself with these options and setup your preferred system(s). Personally, I use all three for various aspects of my data's story to me...Nightscout being the most useful day-to-day as a remote caregiver of a young Looper.

!!!warning "Day 10: FAQs"
    * **"Do I have to set one of these up?"** No. But, your health care provider really does need data. Insurance companies definitely demand data too...so make them happy.
    * **"Do I need all three?"** No, you can mix-and-match. Apple Health is already built into your iPhone, so there's no setup involved anyways. Nightscout setup is really actually quite easy and Loopdocs has a [complete set of instructions for Loop users](https://loopkit.github.io/loopdocs/nightscout/new_user/). Nightscout has a lot of useful alarms and alerts, too. Tidepool is frree and easy to setup, and many clinics already have Tidepool integration.

!!!info "Day 10: Work Summary"
    * Review the three major systems that can store and show your Loop data. 
    * Setup either Tidepool or Nightscout prior to your next endo appointment in order to provide them Looping data to review.
    
## Day 11: Read LoopDocs

Read Read Read

And then Read Read more

Loopdocs.org and Looptips.org

## Day 12: Build Loop app

OH MY GOSH...the day has arrived. You're ready to build the app.


