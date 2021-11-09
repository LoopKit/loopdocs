# Step 6: Enroll in Apple Developer Program

!!! info "Time Estimate"
    - 15-20 minutes to complete the enrollment forms
    - up to 2 days to wait for confirmation email that enrollment has been activated

!!! abstract "Summary"

    There are two options: Paid ($99/year) or Free (re-build weekly)

    - Paid Developer Account: Go to the [Apple Developer website](https://developer.apple.com/programs/enroll/) to enroll in an individual account.
    - Free: No action required at this time.

!!! question "FAQs"
    - **"Can I use someone else's Apple Developer account?"** Please refer to this [Answer](../faqs/FAQs.md#can-i-use-someone-elses-apple-developer-account).
    - **"Do I use my Apple ID or my child's Apple ID to enroll in the Apple Developer program?"** The Apple ID you use to enroll in the developer program does not need to be the same Apple ID as the Looper uses on their iPhone. For example, a parent installing Loop on their child's iPhone should configure a separate Apple ID for their child, but should use their own Apple ID to build the Loop app for that child. Typically for the developer enrollment, use the Apple ID of the person who will be building the app.
    - **"How long does it take to have my Apple Development account active after I enroll?"** After you enroll, make sure you look for a confirmation email. Apple says it can take up to 24-48 hours to confirm and setup a new Apple developer account. However, some people have had the process take minutes. One SURE way to make it take longer is to use a different credit card to pay for the Apple Developer account enrollment than is already associated with that Apple ID. When you do that, finishing the enrollment process may be a hassle.

## Loopers Need Their Own Apple ID

It is important to understand that the Apple ID is distinct from the Apple Developer ID.

!!! warning "Apple ID"
    Parents should set up a **different** Apple ID for each of their looper children and looper children should **not** use the parent Apple ID. [Please use Apple's Instructions for adding an Apple ID for your child.](https://support.apple.com/en-us/HT201084)

    Sharing the Apple ID prevents Apple Health features from working properly.  Sharing an Apple ID among two or more loopers can cause safety issues. You don't want Sally to be dosed for Joe's lunch in addition to her own and vice versa. In fact, the recommendation for [Health Permissions](health.md#loop-permissions) has changed because this has happened.

    The Apple Health record is a convenient record of blood glucose, insulin and carbohydrates and should be associated with only one individual.


To build your Loop app, you will need to use an Apple developer account.  You have two options for an individual account: free or paid.

## Free Developer Account

If you decide to use a **FREE** developer account, here's what you need to know:

1. Loop apps signed with a free developer account will expire after 7 days.  On the 7th day, your Loop app will simply turn white when you open it and then immediately close. To rebuild the Loop app, you will have to find a computer and rebuild the app onto your iPhone again. You cannot rebuild the app on day 5 (when it is convenient, for example), hoping to reset the 7-day clock.  The app will still expire on the 7th day from when it was first signed and created.
2. If you decide to switch to a paid account after trying out the free account, you will need to rebuild your Loop app to sign it with the new paid account. Furthermore, switching from a [Free to a Paid](step6.md#switching-from-free-to-paid-memberships) account requires entering all the settings again (and starting a fresh pod).
3. You will have to do an extra step during the build process to remove Siri and Apple Push capabilities to build with free accounts. Because free accounts do not have access to Apple Push notifications, you will also not be able to use remote overrides through Nightscout.

## Paid Developer Account

If you decide to use a **PAID** developer account, here's what you need to know:

1. Loop apps signed with a paid developer account will last for a full year.
2. The paid developer account is $99 per year. The default setting is to auto-renew annually. You can change that selection in your developer account settings at any time.
3. If your household has multiple Loop users, only one developer account is needed.  That one developer account can be used to sign multiple Loop apps.

## Switching from Free to Paid Memberships

There is no problem trying a free account first before you decide to buy a paid developer account. If you start with a free account, you'll build a Loop app (let's call it FreeLoop). When you switch to a paid account, you'll be building a totally new and separate Loop app onto your phone (let's call it PaidLoop). The two apps will look identical on your phone, but they will be functionally separate from each other. Make sure you are successful building the PaidLoop app before deleting the FreeLoop app from your phone. Use the search feature on your phone to find both apps.  One will have your configuration settings (FreeLoop), the other will not (PaidLoop).

Before deleting the FreeLoop, either record all the settings or take screen shots of all the relevant settings screens.

PaidLoop will know nothing about the settings and information you had stored in FreeLoop, so you will need to re-enter all your settings (basal rates, ISF, carb ratios, etc.) and configurations into the new PaidLoop. It will also not connect or control any pods you are currently using with the old FreeLoop app. The one exception is Nightscout credentials, which are stored in your keychain. If you entered your Nightscout credentials into FreeLoop, they will persist across app removal and be used by PaidLoop.


## Enrolling

Paid account enrollment is all done through Apple's Developer Program website. Go to the [Apple Developer website](https://developer.apple.com/programs/enroll/) to enroll in an individual paid account.

If you choose to use the free account, you don't have to do anything on that website. You'll just wait for Step 8 Xcode Preferences and we will get your free account then.

## Next Step: Install Xcode

Now you are ready to skip to Step 8 to [Install Xcode](step8.md). And if you've been counting - yes, Step 7 is no longer required.
