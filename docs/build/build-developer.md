# Setup Apple Developer Account

In order to build your own copy of the Loop app onto your iPhone, you will need an Apple developer account.  You will have two options for your individual account; free or paid.

## Free Developer Account

If you decide to use a **FREE** developer account, here's what you need to know:

1. Loop apps signed with a free developer team will expire after 7 days.  On the 7th day, your Loop app will simply turn white when you open it and then immediately close.  To rebuild the Loop app, you will have to find a computer and rebuild the app onto your iPhone again.  You cannot rebuild the app on day 5 (when it is convenient, for example)...hoping to reset the 7-day clock.  The app will still expire on the 7th day from when it was first signed and created.</br></br>
2. If you decide to switch to a paid account after trying out the free account, you will need to rebuild your Loop app in order to sign it with the new paid account.
3. You will have to do a code customization to remove Siri capabilities in order to build with free accounts.

## Paid Developer Account

If you decide to use a **PAID** developer account, here's what you need to know:
    
1. Loop apps signed with a paid developer team will last for a full year.</br></br>
2. The paid developer account is $99 per year and is default set to auto-renew annually.  You can change that selection in your developer account settings at any time.</br></br>
3. If your household has multiple Loop users, only one developer account is needed.  That one developer account can be used to sign multiple Loop apps.</br></br>

## Developer Enrollment
If you have decided to use the free developer account, you don't have to do anything right now.  We will create it a little later in this process. 

!!! info "Action item here!"
    If you've decided to you'd like to use a paid developer account, we need to get you enrolled.  Go to the [Apple Developer website](https://developer.apple.com/programs/enroll/) to enroll in an individual account.

Note: The Apple ID you use to enroll in the developer program does not need to be the same Apple ID as the Loop iPhone uses, for example parent installing Loop on kid's iPhone.  Typically for the developer enrollment, use the Apple ID of the person who will be doing the Loop app building.)   After you enroll, make sure you look for a confirmation email.  Apple says it can take up to 24 hours to confirm and setup a new Apple developer account, however some people have had the process only take minutes.  It can vary.

## Differentiating between Free and Paid in Xcode

This is just an FYI: In later steps when you build the Loop app in Xcode, you will select a signing "team" and Xcode will automatically generate a Provisioning Profile to "sign" the app...this is Apple's way of tracking the validity and safety of the app.  Free developer accounts will have a signing team that includes a "(Personal Team)" designation in the name. Paid developer accounts will not have "(Personal Team)" in the name.  

<p align="center">
<img src="../img/team.jpg" width="450">
</p>

## Switching from Free to Paid Memberships

In summary: This is no problem trying a free account first before you decide to buy a paid developer account. Many Loop users start with a free developer account as they test-drive the Loop. When you build Loop, Xcode will be identifying that specific build of the app using a unique *Bundle Identifier* based on your unique developer account. The great thing about this setup is that when/if you decide to update your Loop app in the future, all of your old Loop app settings and information are saved during the update. Functionally, this is pretty much like you experience when you update any of your existing apps using the iPhone's app store...all the existing info you already had in the app remains unchanged and app just updates right where it was sitting in your iPhone screen.

The magic that makes these seamless updates happen is that *Bundle Identifier*. The *Bundle Identifier* is automatically generated for Loop based on the unique developer team that you are signing your Loop app with. This means that the *Bundle Identifier* will change when you switch from a free to a paid membership because the developer team is different.  Why is this worth mentioning?  Because it affects the transition between using a free membership to a paid membership.

If you start with a free account and build Loop, you'll get a Loop app (let's call it Loop1). When you switch to a paid account and build Loop, you'll be building a totally new and separate Loop app onto your phone (let's call it Loop2). Loop2 will know nothing about the settings and information you had stored in Loop1, so you will need to re-enter all your Loop1 settings (basal rates, ISF, carb ratios, etc.) and configurations into Loop2 when it builds.  After getting your new Loop2 app setup, you should delete your old Loop1 from your iPhone that was based on the free developer account to avoid any conflicts.

## License Agreement
When you enroll in the Developer, you also click a box that you are agreeing to Apple's Develper Program license agreement. Periodically, Apple will update that license agreement and you'll be required to agree to the updates.  When that happens, you'll need to login to your developer account and accept the new license agreement before you can sign a new/updated Loop app again. Not a big deal, just mentioning it for future reference.

Now that you have your Developer Account decision made, and enrolled if you are doing the paid account...you can move onto [Setting up your Xcode](https://loopkit.github.io/loopdocs/build/build-xcode/).
