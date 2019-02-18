# Apple Developer Account


The [Apple Developer Program](https://developer.apple.com/programs/how-it-works/) is Apple's system to provide the [tools and resources](https://developer.apple.com/programs/whats-included/) for building, sharing, and using apps for Apple products.  Members of Apple's Developer Program can test apps on their own devices prior to submitting the App Store for distribution or sale.  Developers also get access to beta releases of new OS and iOS versions (but please don't use them if you use Loop, they will be incompatible with Loop while in beta release).

The Loop app is not available for download in the App Store.  It needs to be built and installed by the individual users.  This means Loop users need to enroll as an individual (not an organization) in the Apple Developer Program in order to install the Loop app on their iPhone.  There are two types of individual [enrollment in the Developer Program](https://developer.apple.com/programs/enroll/); free and paid.  You will need to have an Apple ID to sign up for in the Apple Developer Program.

## Free Membership

Free membership comes with an important restriction.  While you can build the Loop app onto your iPhone, the app will expire after 7 days and need to be rebuilt in order to work again.  This means, every 7 days you will need access to an Apple computer, Xcode application, and your iPhone to rebuild the app.

You cannot rebuild the app on day 6 and expect to avoid downtime.  The same app cannot be rebuilt earlier than the 7 days...it will still expire on the 7th day.  You will know your app is expired by the fact that it simply won't open after 7 days.  When you click on it, it will momentarily give you a white screen and then immediately go back to your main iPhone screen.  

Another important distinction is that apps built with a free membership cannot build apps that have Siri capabilities.  Loop has Siri capabilities built-in, so for free developer members, you will have to perform extra steps in order to specifically remove Siri from Loop before building. Those steps are outlined in the Code Customizations section of these docs.

For free memberships, you are also limited to building 10 apps within a 7-day period.

## Paid Membership

Paid membership is $99 per year.  It allows you to build the Loop app and it will remain active for the entire year.  You only need to rebuild the app if you decide you are interested in updating for new features that may be released in subsequent Loop versions.  If you have multiple T1Ds in your household and are building multiple Loop apps, you only need one paid membership account.

## Switching from Free to Paid Memberships

Many Loop users start with a free developer account as they test-drive the Loop.  When you build the app, Xcode will be identifying that specific build of the app using a unique *Bundle Identifier* based on your Developer membership. The great thing about this setup is that when/if you decide to update your Loop app in the future, all of your old Loop app settings and information are saved during the update. Functionally, this is pretty much like you experience when you update any of your existing apps using the iPhone's app store...all the existing info you already had in the app remains unchanged and app just updates right where it was sitting in your iPhone screen.

The magic that makes these seamless updates happen is that *Bundle Identifier*. The *Bundle Identifier* is automatically generated for Loop based on the developer team that you are signing your Loop app with. This means that the *Bundle Identifier* will change when you switch from a free to a paid membership.  Why is this worth mentioning?  Because it affects the transition between using a free membership to a paid membership.

If you start with a free account and build Loop, you'll get a Loop app (let's call it Loop1). When you switch to a paid account and build Loop, you'll be building a totally new and separate Loop app onto your phone (let's call it Loop2). Loop2 will know nothing about the settings and information you had stored in Loop1, so you will need to re-enter all your Loop1 settings (basal rates, ISF, carb ratios, etc.) and configurations into Loop2 when it builds.  After getting your new Loop2 app setup, you should delete your old Loop1 from your iPhone that was based on the free developer account to avoid any conflicts.


## Differentiating between Free and Paid in Xcode

When you build the Loop app in Xcode, you will select a signing "team" and Xcode will automatically generate a Provisioning Profile to "sign" the app...this is Apple's way of tracking the validity and safety of the app.  Free developer accounts will have a signing team that includes a "(Personal Team)" designation in the name. Paid developer accounts will not have "(Personal Team)" in the name.  

<p align="center">
<img src="../img/team.jpg" width="450">
</p>

## Multiple Loop apps

While technically possible, you can have multiple Loop apps built onto the same iPhone.  However, having multiple Loop apps on a single phone may lead to unexpected conflicts that can negatively affect your Loop's ability to stay green (keep looping).  For smooth looping, just keep one Loop app on any phone for looping use. The only time you should have two Loops on a single iPhone is in the event that you are switching signing teams and are temporarily transferring settings and configuration information between the two apps manually. Once that transfer is complete, delete the old Loop app.

