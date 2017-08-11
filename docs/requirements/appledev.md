# Apple Developer Account


The [Apple Developer Program](https://developer.apple.com/programs/how-it-works/) is Apple's system to provide the [tools and resources](https://developer.apple.com/programs/whats-included/) for building, sharing, and using apps for Apple products.  Members of Apple's Developer Program can test apps on their own devices prior to submitting the App Store for distribution or sale.  Developers also get access to beta releases of new OS and iOS versions.  

The Loop app is not available for download in the App Store.  It needs to be built and installed by the individual users.  This means Loop users need to enroll as an individual (not an organization) in the Apple Developer Program in order to install the Loop app on their iPhone.  There are two types of individual [enrollment in the Developer Program](https://developer.apple.com/programs/enroll/); free and paid.  You will need to have an Apple ID to sign up for in the Apple Developer Program.

Sometimes, Apple will send an email requiring confirmation before enrollment can be activated.  Other times, you may have to login to your developer account to confirm enrollment.  Be sure to check for those items if you are having problems when trying to add your Apple ID and developer account in Xcode preferences during build.

## Free membership

Free membership comes with an important restriction.  While you can build the Loop app onto your iPhone, the app will expire after 7 days and need to be rebuilt in order to work again.  This means, every 7 days you will need access to an Apple computer, Xcode application, and your iPhone to rebuild the app.

You cannot rebuild the app on day 6 and expect to avoid downtime.  The same app cannot be rebuilt earlier than the 7 days...it will still expire on the 7th day.  You will know your app is expired by the fact that it simply won't open after 7 days.  When you click on it, it will momentarily give you a white screen and then immediately go back to your main iPhone screen.  

For free memberships, you are also limited to building 10 apps within a 7-day period.  Each new Main App Bundle Identifier that you use will "count" towards that limit.

## Paid membership

Paid membership is $99 per year.  It allows you to build the Loop app and it will remain active for the entire year.  You only need to rebuild the app if you decide you are interested in updating for new features that may be released in subsequent Loop versions.

## License Agreement

Periodically, Apple will have updates to their Developer license agreements.  Your Loop app will fail to sign properly until your accept the new license agreement.  If you see the warning sign under your app signing, go to your [Developer Account](https://developer.apple.com/account/), sign in, and accept the new terms.


## App IDs

Many Loop users start with a free developer account as they test-drive the Loop.  When you build the app, you will be identifying that specific build of the app using a unique *Main App Bundle Identifier* and signing the app with a "Team Name" associated with your Developer membership.  That Main App Bundle Identifier cannot be used again when you switch to a paid account provisioning profile.  Why is this worth mentioning?  If you start with a free account and build Loop...when you switch to a paid account and build Loop, you will need to use an new Main App Bundle Identifier, new paid account team name for signing, and you will need to re-enter all your Loop settings (basal rates, ISF, carb ratios, etc.).

When you build the Loop app in Xcode, you will select a signing "team" and Xcode will automatically generate a Provisioning Profile to "sign" the app...this is Apple's way of tracking the validity and safety of the app.  Free developer accounts will have a signing team that includes a "(Personal Team)" designation in the name.  Paid developer accounts will not have "(Personal Team)" in the name.  

<p align="center">
<img src="../img/team.jpg" width="450">
</p>

## Multiple Loop apps

You can have multiple Loop apps built onto the same iPhone.  Many people who have the need to swtich between different profiles on a regular basis (such as t1ds who need school vs weekend profiles) use two different Loop apps to track the different profiles.  To build two Loop apps onto same phone, you simply need to use two different Main App Bundle Identifiers.  When switching between Loop apps, simply remember to close the unused Loop app so that the RileyLink can connect properly in the desired Loop app.  You can enable "Patterns" in your Medtronic pump to also switch quickly between basal profile patterns that correspond to the active Loop app.

Users of multiple Loop apps find it is helpful to rename the apps and use different app icons to differentiate between the two Loop apps.  Customizing app icons can be done following the instructions in the Build section of these docs.  

