## Build Loop using GitHub Actions

This is only available with Loop 3 and Loop dev branch.

!!! info "Time Estimate"
    - If you have never built Loop (allow up to one week elapsed time)
        * Requesting and getting an Apple Developer Account: 1-2 days
        * Creating and configuring your GitHub repositories (without Apple Information): 1-2 hours
        * Adding Repository Secrets (requires Apple Developer Account): 1 hour
        * Performing the Action steps: 30 minutes to 2 hours
    - If you have previously built Loop with Xcode you have fewer steps and are probably familiar with some of the concepts
        * Expect 1 to 2 hours

!!! abstract "Summary"
    Once you have Apple Developer and GitHub accounts

    * Apple: Generate an API Key
    * GitHub: Create a Match-Secrets private repository
    * GitHub: Fork a copy of LoopWorkspace and add Repository secrets
    * GitHub: Action: Add Identifiers
    * Apple: Never Built Before? - several steps
    * Apple: Create your version of Loop in App Store (personal use only, not for distribution)
    * GitHub: Action: Create Certificates
    * GitHub: Action: Build Loop
    * Apple: Set up Internal TestFlight Group
    * Phone: Install Loop with TestFlight
    

!!! question "FAQs"
    - **Do I need a Mac computer?** No. This can be done on any browser, although it will be easier using a computer or tablet than just using a phone.
    - **Can I do this on my phone?** Yes, but the graphics shown on this page are from a computer browser.
    - **Isn't it hard to build every 90 days?** The initial setup (this page) and deploy (next page) takes a lot of your focused time. But once you build once, subequent builds take very little of your time to start, then the rest is done automatically.
    - **Can I use this for my child?** You, as the adult, can install using TestFlight on your child's phone. The explict steps are provided.
    - **Can I still use my customizations?** This requires steps not yet documented. If you want customizations, stick with the Mac / Xcode build method for now.

**You must build Loop every 90 days when you use GitHub build method.**


## Configure to use GitHub Build Actions

Review the entire process before starting and then go through slowly and carefully.

These instructions allow you to build Loop without having access to a Mac. They also allow you to easily install Loop on phones that are not connected to your computer.

* You can send builds and updates to those you care for easily
* You can access and install Loop if you lose or damage your device
* You do not need to worry about correct Xcode/macOS versions

The setup steps are somewhat involved, but nearly all are one time steps. Subsequent builds are trivial. The initial steps are best done on a computer where you can save and archive information for later use.

TestFlight can be used to deploy Loop to a child's phone (under age 13 in the US) but requires a few extra steps on the phone itself. See [Install TestFlight Loop for Child](gh-deploy.md#install-testflight-loop-for-child).

Your app must be updated once every 90 days, but it's a simple click to make a new build and can be done from anywhere, see [Update Loop using GitHub Actions](gh-update.md).

### Save Your Information

!!! tip "Archive This Information"
    For many of the steps on this page, you will need to have access to usernames, email addresses, passwords, and in some cases, special parameters. The API Key can only be downloaded one time - you must save it in a safe place. If you loose it, you'll need to generate a new key and update the secret settings in your fork of the LoopWorkspace repository. Same for the GitHub access token you will generate in another step.

    * Record these in a safe place so you can find them when you need them
    * A digital copy is best because you will be copying and pasting in different locations

This list indicates what you need to record (save digitally so you can copy and paste). Notice that some information is created in one place and used in another. The items in all capital letters will be added to the `Repository Secrets` for your LoopWorkspace repository. So they are listed twice in the list below.

!!! tip "A Note about Capitalization and Spaces"
    In places you will be told to give something a name like: FastLane API Key or FastLane Access Token. Please use these names. The `Repository Secrets` that come later will use names that are capitalized and use underscore instead of spaces. Be precise and careful.

     The relationship and creation of each item is explained step-by-step on this page.

* Needed or created at developer.apple.com
    * Email address (this is your username)
    * password
    * TEAMID
    * FASTLANE_KEY_ID
    * FASTLANE_ISSUER_ID
    * FASTLANE_KEY
* Needed or created at github.com
    * Email address
    * password
    * username
    * Your GitHub repository address will be: `https://github.com/username`
    * Your LoopWorkspace repository address will be: `https://github.com/username/LoopWorkspace`
    * GitHub Personal Access Token (GH_PAT)
    * a password - whatever you want (MATCH_PASSWORD)
* Needed when you [Configure Secret Settings](#configure-secret-settings).
    * TEAMID
    * FASTLANE_KEY_ID
    * FASTLANE_ISSUER_ID
    * FASTLANE_KEY
    * GH_PAT
    * MATCH_PASSWORD


## Prerequisites

There are only two prerequisites to Build Loop with this method.

1. Paid Apple Developer account
1. Free GitHub account

You will need TestFlight, from the Apple App Store, installed on your [Compatible Phone](../build/step2.md). You will install Loop on that phone using the TestFlight app.

In order to use Loop, you need a [Compatible Pump](../build/step3.md) and [Compatible CGM](../build/step4.md). For pumps other than Omnipod DASH, you also need a [RileyLink Compatible Device](../build/step5.md).

For the initial steps, you'll be going back and forth between GitHub and Apple Developer webpages. It is best to open each in a separate window or tab for your browser.

## Apple Developer Account

If you have an Apple Developer Account, you need to sign in to your account. There will be links to take you to specific pages in the account website, but you need to be logged in.

If you do not already have a paid Apple Developer account, you need to purchase one ($99 annual fee). It may take a few days for the account to be enabled.

* LoopDocs has an [Apple Developer Program](../build/step6.md) page that explains in detail how to sign up for an account
* This link takes you straight to [Apple Developer account](https://developer.apple.com) to sign up

### Generate API Key

You cannot generate the API Key until you have the paid Apple Developer account set up. If you are still waiting for Apple to enable your account, you can skip ahead to complete part of the GitHub steps but you will need to pause at [Configure Secret Settings](#configure-secret-settings).

This section will walk you through the steps required to gather or create these parameters.

|Name|Description|
|---------|---------|
|TEAMID|10-character identifier|
|FASTLANE_KEY_ID|Key ID generated for you in App Store Connect|
|FASTLANE_ISSUER_ID|The issuer ID is shown when the Key ID is displayed|
|FASTLANE_KEY|Copy the full key from the text file.<br>including the "-----BEGIN PRIVATE KEY-----" and "-----END PRIVATE KEY-----" lines. |

Each step has a link to take you to the specific page you need to do the next step. It is best if you open each link in a separate tab or window so you can refer back to these instructions as you move along.

1. Open this link: [Apple developer portal page](https://developer.apple.com/account/resources/certificates/list).
    * Look at the upper right hand corner of that page
    * The 10-character ID number below your name is your `TEAMID`
    * Record this for use when you configure your secret settings
1. Open this link: [App Store Connect/Access/API](https://appstoreconnect.apple.com/access/api)
    * Click the "Keys" tab
        * If this is your first time here, there will be a dialog for you to follow:

            "Permission is required to access the App Store Connect API. You can request access on behalf of your organization."

            * Click on `Request Access` and follow directions until access is granted

        * Once access is granted, click on the "Generate API Key" button

    * If you did not get routed through the "permission is required" screens click the blue &plus; sign

    ![App Store Connect Key page](img/api-key-initial-screen.svg){width="700"}
    {align="center"}

    * A new "Generate API Key" dialog box will appear as shown in the graphic below

    ![generate api key dialog box](img/dev-generate-key.png){width="500"}
    {align="center"}


    * Enter the name of the key as "FastLane API Key" and choose "Admin" in the access drop down menu. Click on the "Generate" button.
    * The Keys screen is seen again with the additional content shown in the graphic below where key information is blanked out for security
    * Review the graphic and then follow directions below to save more parameters you will need to [Configure Secret Settings](#configure-secret-settings)

    ![App Store Connect Key page](img/api-key-in-process.svg){width="700"}
    {align="center"}

1. Hover to the right of the Key ID and the Copy Key ID button shows up
    * Tap on the Copy Key ID button and save this as `FASTLANE_KEY_ID` 
1. A button labeled Copy is alway adjacent to the Issuer ID above the word Active (this is the same for all keys that you generate with this Apple Developer ID)
    * Tap on the Copy button and save this as `FASTLANE_ISSUER_ID`
1. Click on the Download API Key button - you will be warned you can only download this once.

    ![download key only once](img/dev-dl-key-once.png){width="700"}
    {align="center"}

6. Find your AuthKey download in your downloads folder. The name of the file will be "AuthKey_KeyID.p8" where KeyID matches the value above. Double-click to open it and you will be presented a message asking how you'd like to open it. Click on "Choose Application..." and then select "TextEdit" (on a Mac, any text-only editor on other computers) as your application to open it with.

    ![img/apns-open.png](../nightscout/img/apns-open.png)

1. The contents of this file will be used for `FASTLANE_KEY`. Copy the full text, including the "-----BEGIN PRIVATE KEY-----" and "-----END PRIVATE KEY-----" lines.


    ![img/apns-copy-key.png](../nightscout/img/apns-copy-key.png)

In summary, from this section, you have found or generated the following, and saved copies for later use

* `TEAMID`
* `FASTLANE_KEY_ID`
* `FASTLANE_ISSUER_ID`
* `FASTLANE_KEY`

!!! tip "Time for a Break?"
    This is a good place to pause if you need to. Just note where you are on the page so you can return later.

## GitHub Account

If you have a GitHub account, you can skip to [Setup GitHub](#setup-github). Make sure you know your GitHub associated email, username and password.

If you do not already have a GitHub account, you need to create one. Be sure to record the email, password and username for your GitHub account.

Decide on a couple of usernames that you will be happy with - this will get embedded into your GitHub URL. Your first choice might not be available, so be prepared with several candidates. Your personal URL will be: `https://github.com/username`.

* Click on this link to sign up for a free account: [github account signup](https://github.com/signup)
    * You will need to enter the **email** you want associated your GitHub account
    * You will be asked to enter a **password**
    * You will be asked to enter a **username**
    * You will be asked if you want to receive email, ok to say N for no - you still get important account information with that email
    * Solve the puzzle to prove you're a person
    * Check the associated **email** to get the code and enter the code into github.com to confirm your account
* You should get the Welcome to GitHub screen
    * Indicate it is "Just me" on your team and Continue
    * Don't check anything on the next screen, just tap Continue
    * Select the Free option by selecting "Continue for Free"

The free level comes with plenty of storage and compute time to build loop.

## Setup GitHub

Now you will create one new repository and then fork the LoopWorkspace repository.

### Create Match-Secrets

Open your github.com URL (this is `https://github.com/username`) where you replace username with the name you chose above.

Create a new private repository - you can either click on the link below, or follow the instructions with the first graphic:

* Click on this link: [(https://github.com/new)](https://github.com/new)

or

* At the top right of the screen, click on the &plus; sign and select New Repository

    ![plus sign to add repository](img/create-match-secrets.svg){width="200"}
    {align="center"}

This shows you a screen similar to the following graphic which has 3 regions highlighted:

* In Repository name, type Match-Secrets (use a hyphen between Match and Secrets)
* Be sure the check the box (red circle) to make the repository **private**
* **Please confirm you selected Match-Secrets repository as private.**
* Scroll to the bottom of the pages and tap on "Create Repository"

![first screen for new repository](img/01-gh-create-match-secrets.png){width="600"}
{align="center"}

You will then be shown a screen with a lot of options - you will not do anything on this screen except leave it.

* Click on just your username (as indicated by the red rectangle) to return to your main GitHub URL.

![second screen for new repository](img/02-gh-match-secrets-leave-alone.png){width="600"}
{align="center"}

You will not be interacting with your Match-Secrets repository directly. It needs to exist for other actions to work correctly.

You are done with this part of the set up.

### Fork LoopWorkspace

!!! warning "Existing Fork"
    Some people may already have a fork of LoopWorkspace. Click on [Already Have LoopWorkspace](#already-have-loopworkspace), decide what to do and follow the appropriate link back to these instructions.

1. Open this link [https://github.com/LoopKit/LoopWorkspace](https://github.com/LoopKit/LoopWorkspace) to open the LoopWorkspace repository owned by LoopKit.
1. Review the highlighted locations of the graphic below (yours won't look quite like this yet), but the `Fork` button is in the same place
1. At upper right side of the screen, click on the word Fork
    * If you already have a fork, it will not allow you to proceed, see [Already Have LoopWorkspace](#already-have-loopworkspace)
1. Now your screen should look like the graphic below
    * Your username will be automatically filled in as the Owner
    * LoopWorkspace is automatically filled in as the Repository Name
    * Uncheck the selection that says "Copy the dev branch only" so it looks like the graphic
    * Click on the green `Create fork` button

    ![fork information for LoopWorkspace](img/gh-fork-loopworkspace.png){width="700"}
    {align="center"}

### Successful Fork

After creating the fork, your screen should be similar to the next graphic. You may or may not see the messages you are told to dismiss in the next two bullets. No worries if you don't see them.

* Near the top right, click on the X to dismiss the successfully fetched message
* In the middle, click on the Dismiss button to remove the "Your branch is not protected message"

![after creating the fork LoopWorkspace](img/gh-initial-fork-dismiss.png){width="500"}
{align="center"}

Carefully compare your screen to the graphic below paying attention to the highlighted sections.

* Note that your username is now showing
* The comment under your username indicates where the fork came from (that is a clickable link)
* The branch that is selected is dev - you can modify this with the dropdown, but leave it for now
* The message says "This branch is up to date with LoopKit/LoopWorkspace:dev"

![after creating the fork LoopWorkspace](img/gh-after-fork.png){width="700"}
{align="center"}

!!! tip "Time for a Break?"
    This is a good place to pause if you need to. Just note where you are on the page so you can return later.

### Create Access Token

If you are returning from a break, be sure to log into your GitHub account before starting this step. If you are continuing, you are already logged in.

1. You will be creating a new GitHub Personal Access token and giving it the name "FastLane Access Token"
1. Open this link: [https://github.com/settings/tokens/new](https://github.com/settings/tokens/new)
    * Referring to the graphic, type FastLane Access Token in the Note box
    * The default Expiration time is 30 days - but you should select 90 days (use the drop down menu to select)
        * You get an email when this token is close to expiration
        * Since you must rebuild every 90 days, setting the Expiration time to 90 days acts as a convenient reminder
        * See [GitHub Token](../gh-actions/gh-update.md#github-token) for instructions on regenerating when doing an update
    * Add a check beside the `repo` permission scope
    * Scroll all the way to the bottom and click "Generate token" (it's a long way, ignore all other settings, do not check anything else)

    ![request a new personal access token](img/gh-access-token.png){width="700"}
    {align="center"}


1. A new screen appears showing your access token
    * Copy the token and record it - once you leave this screen you can't see it again
    * You will use this for `GH_PAT` when you set up your Secrets

### Configure Secret Settings

Refer to the list of parameters found in [Save Your Information](#save-your-information). This is the time you will enter these items.

1. Return to your forked copy of LoopWorkspace
    * Click on your personal icon at upper right to see the drop-down menu and select "Your repositories"

    ![drop-down-menu](img/gh-quick-access.png){width="200"}
    {align="center"}

1. You should see (at least) 2 repositories: Match-Secrets and LoopWorkspace
1. Click on LoopWorkspace to open that repository
1. Click on the Settings Icon near the top right of your LoopWorkspace
    * If you don't see `Settings`, make your browser wider or scroll to the right
    * If you still don't see `Settings`, then you are **not** on your fork or you need to sign in to your GitHub account
    * After you click on Settings, your screen should look like the graphic below

        ![settings screen](img/gh-settings.png){width="700"}
        {align="center"}

1. On the left side, find the Secrets dropdown and choose Actions
    * After you select on Actions, your screen should look like the graphic below

        ![action secrets screen](img/gh-actions-secrets.png){width="700"}
        {align="center"}

1. Take a calming breath. This next part requires care. Once you enter and save a secret value, you will not be able to view what you just entered. If you make a mistake, the actions you take in the next sections will fail. So collect the list of information you've gathered so it's handy and make up a password for the MATCH_PASSWORD.
1. For each of the following secrets, tap on the green button at the top right labeled "New repository secret", then add the name of the secret, along with the value you recorded for it:
    * `TEAMID`
    * `FASTLANE_KEY_ID`
    * `FASTLANE_ISSUER_ID`
    * `FASTLANE_KEY` - the entire thing from "-----BEGIN PRIVATE KEY-----" through "-----END PRIVATE KEY-----"
    * `GH_PAT`
    * `MATCH_PASSWORD` - make up a password for this but save it with your other information


Once all six secrets have been added to your LoopWorkspace, you are done with Settings.

![all secrets entered](img/gh-done-adding-secrets.png){width="700"}
{align="center"}

!!! tip "Time for a Break?"
    This is a good place to pause if you need to. Just note where you are on the page so you can return later.

## Add Identifiers for Loop

Near the top middle of your LoopWorkspace fork, there is an Actions tab.

1. Click on the "Actions" tab of your LoopWorkspace repository.
    * The first time you click on `Actions` with this repository you'll be informed that `Workflows aren't being run on this forked repository` as shown in the graphic below
    * Tap on the green button that says: `I understand my workflows, go ahead and enable them`

        ![workflows disabled screen](img/gh-workflows-disabled.png){width="700"}
        {align="center"}

1. The workflows are now displayed: look at the list on the left side as shown in the graphic below (you can dismiss the Actions Enabled message using the X near the upper right side)

    ![workflows displayed](img/gh-workflows-enabled.png){width="700"}
    {align="center"}

1. Select "Add Identifiers".
1. On the right side, click "Run Workflow" to show a drop-down menu and then tap the green button that says "Run workflow".

    ![placeholder alt-text for graphic not prepared: add identifier in process](img/add-identifier.png){width="700"}
    {align="center"}

1. Wait, it seems like nothing happens but then you will see the busy icon followed by a green checkmark indicating the workflow succeeded as displayed in the GIF above.
    * If this action fails, you probably made an error in one of your secrets
    * Try to determine which one was incorrect by clicking on the failed action link to see the full log
    * Go back and enter the secret(s) again
        * You cannot see what you entered, you'll just need to replace it by tapping on the pencil icon
        * You need your GitHub password to change a secret

## Configure Identifiers for Loop

If you have already built Loop via Xcode using this Apple ID, you can skip some steps but first, read this.

In the instructions for people who have never built Loop, they are instructed to look for 4 identifier names and configure them with the App Group associated with their TEAMID. The 4 identifiers that need this association are:

* Loop
* Loop Intent Extension
* Loop Status Extension
* Small Status Widget

When you have already built Loop with Xcode, the Loop identifier is already associated with your App Group with time sensitive capability.  Your existing Loop identifier will have a name that starts with XC as shown below, where your 10-digit team ID is used.

* Name: XC com TEAMID loopkit Loop
* Identifier: com.TEAMID.loopkit.Loop

If you look at [Certificates, Identifiers & Profiles](https://developer.apple.com/account/resources/identifiers/list) and find that name and identifier, you can skip ahead to [Create Loop App in App Store Connect](#create-loop-app-in-app-store-connect). If you've done a lot of building with Xcode, there may be a lot of names here.

### Create App Group

If you have already built Loop via Xcode using this Apple ID, skip ahead to [Create Loop App in App Store Connect](#create-loop-app-in-app-store-connect).

If you have never built Loop, you need to create an App Group associated with your TEAMID.

1. Open this link: [Register an App Group](https://developer.apple.com/account/resources/identifiers/applicationGroup/add/) on the apple developer site.
1. For Description, use "Loop App Group".
1. For Identifier, enter "group.com.TEAMID.loopkit.LoopGroup", subsituting your team id for `TEAMID`.
1. Click "Continue" and then "Register".

### Add App Group to Bundle Identifiers

If you have already built Loop via Xcode using this Apple ID, skip ahead to [Create Loop App in App Store Connect](#create-loop-app-in-app-store-connect).

1. Open this link: [Certificates, Identifiers & Profiles: List](https://developer.apple.com/account/resources/identifiers/list) on the apple developer site.
1. For each of the following identifier names:
    * Loop
    * Loop Intent Extension
    * Loop Status Extension
    * Small Status Widget
1. Click on the identifier's name.
1. On the "App Groups" capabilies, click on the "Configure" button.
1. Select the "Loop App Group"
1. Click "Continue".
1. Click "Save".
1. Click "Confirm".
1. Remember to do this for each of the four identifiers above; only needed for those four.

### Add Time Sensitive Capability

If you have already built Loop via Xcode using this Apple ID, skip ahead to [Create Loop App in App Store Connect](#create-loop-app-in-app-store-connect).

1. Go to [Certificates, Identifiers & Profiles](https://developer.apple.com/account/resources/identifiers/list) on the apple developer site.
1. Click on the "Loop" identifier (only the Loop identifier needs this capability added)
1. Scroll down to "Time Sensitive Notifications"
1. Tap the check box to enable Time Sensitive Notifications.
1. Click "Save".
1. Click "Confirm".

## Create Loop App in App Store Connect

If you built using Xcode with your Apple Developer ID, you were able to skip the steps from the prior few sections - they are already configured.

If you have created a Loop app in App Store Connect before, you can skip this section as well.

If have previously used some kind of remote build, like diawi, you may have your Loop in the App Store but can't see it. Don't worry - there are instructions for this case.

1. Open this link: [App Store Connect / Apps](https://appstoreconnect.apple.com/apps) to view your apps; log in if needed. 
    * If you have never added a app to App Store Connect, you will not see the icons inside the red rectangle and should keep going, although some people report the search icon shows up for them
    *  If you have an app that is not shown, you will see a search icon and the `All Statuses` dropdown. If you get to the step 3 and cannot find your `com.TEAMID.loopkit.Loop` in the Bundle ID drop down, the means you need to follow [Find My Loop](#find-my-loop).

    ![app store connect with deleted apps](img/01-app-store-connect.png){width="600"}
    {align="center"}

1. Click the Add Apps button or the blue "plus" icon and select New App as shown in the graphic below

    ![choose to add a new app](img/new-app-in-store.png){width="300"}
    {align="center"}

1. The New App dialog box opens and should appear similar to the graphic below. Before you fill anything out, make sure your Bundle ID is available in the dropdown menu (it shows as `Choose` in the graphic below). If you do not see `com.TEAMID.loopkit.Loop`, with TEAMID matching your TEAMID in the dropdown menu; back out of this screen and follow the directions in [Find My Loop](#find-my-loop) instead.
    * Select "iOS".
    * Enter a name: this will have to be unique
        * You could start with Loop_ABC where ABC are your initials
        * If that is already taken, you can add a number, for example, Loop_ABC_123
        * This name is what you see on the App Store Connect list and in the TestFlight app
        * Once installed on your phone, you will see Loop with the standard Loop Logo
        * You can [Change the App Store Connect Name](../gh-actions/gh-deploy.md#change-the-app-store-connect-name) later if you want
    * Select your primary language.
    * Choose the bundle ID that matches `com.TEAMID.loopkit.Loop`
    * SKU can be anything; for example "123".
    * Select "Full Access".

    ![create loop app in store connect - with missing bundle id](img/create-app-in-store.png){width="600"}
    {align="center"}

1. Click Create but do not fill out the next form. That is for submitting to the app store and you will not be doing that.

You are done with this activity and can close the browser tab. It's time to head back to your GitHub account and [Create Certificates](#create-certificates)

### Find My Loop

This section is for people who were not able to follow the instructions in the last section because `com.TEAMID.loopkit.Loop`, with TEAMID matching your TEAMID, was not in the dropdown menu for Bundle ID.

There are two possible reasons:

1. You did not complete [Add App Group to Bundle Identifiers](#add-app-group-to-bundle-identifiers) or one of the predecessor steps; review those steps
1. Your app is already in App Store Connect, but you cannot see it

You may have no memory of ever setting up Loop in App Store Connect. If you previously used some kind of remote build, like diawi, your Loop may be there as a Removed App.

* Open this link: [App Store Connect / Apps](https://appstoreconnect.apple.com/apps), look for All Statuses dropdown indicator and select `Removed Apps`

    ![app store connect with deleted apps](img/01-app-store-connect.png){width="600"}
    {align="center"}

* Click on the App name:

    ![find removed apps](img/find-removed-app.png){width="600"}
    {align="center"}

* Insure this is the app you want by selecting on App Information, highlighted on the left side. Examine is Bundle ID (not in view in this graphic) - confirm it is correct. Then scroll down to the bottom and choose `Restore App`.

    ![find removed apps](img/restore-removed-01.png){width="800"}
    {align="center"}

* Make sure User Access is still set to Full Access and click on Restore.

    ![find removed apps](img/restore-removed-02.png){width="800"}
    {align="center"}

* You are done with this step and ready to Create Certificates

## Create Certficates

1. Go back to the "Actions" tab of your LoopWorkspace repository in GitHub.
1. Select "Create Certificates" (on the left).
1. On the right side, click "Run Workflow" to show a drop-down menu and then tap the green button that says "Run workflow".
1. Wait, and within a minute or two you should see a green checkmark indicating the workflow succeeded.

    ![placeholder alt-text for graphic not prepared: create certificates succeeded](img/create-certificates.png){width="700"}
    {align="center"}


## Build Loop

1. Click on the "Actions" tab of your LoopWorkspace repository.
1. Select "Build Loop".
1. On the right side, click "Run Workflow" to show a drop-down menu, choose your branch (dev is right until Loop 3 is released) and then tap the green button that says "Run workflow".
1. You have some time now. Go enjoy a coffee. The build should take about 20-30 minutes.
1. Your app should eventually appear on [App Store Connect](https://appstoreconnect.apple.com/apps).

## Set Up Users and Access (TestFlight)

Once the first build completes, you will be able to configure TestFlight for the app.

You are configuring a private capability for your family using an Internal Testing group (max of 100). You need the Apple ID email address for each adult installing from your build. When building for a child, you will use your own Apple ID, not theirs. See [Install TestFlight Loop for Child](#install-testflight-loop-for-child).

1. First you need to add the email adress(es) to your App Store Connect Access Users list:

    * Open this link: [Users and Access](https://appstoreconnect.apple.com/access/users)
        * You must provide a role for each person - Customer Support is a good choice
        * Once you have added them here, you'll be able to select them in the TestFlight group for your app

    ![add email and role for your users](img/add-users.png){width="700"}
    {align="center"}

1. Open this link: [App Store Connect / Apps](https://appstoreconnect.apple.com/apps) to view your apps; log in if needed. Then select your Loop app. Click on TestFlight tab and the Internal Testing to add a group.

    ![open TestFlight tab for your app](img/setup-testflight-01.png){width="700"}
    {align="center"}
    
1. Fill out the name you want for the Internal Testing group
    * Be sure to enable automatic distribution
    * Create when done (this can always be modified later)

    ![add email and role for your users](img/setup-testflight-02.png){width="700"}
    {align="center"}

1. As soon as you create the group, you'll be asked who should be included
    * Click in the box beside each person you want to include
    * Each person in this group will get an email each time you update (build again) on GitHub
    * Click Add when you are done
    * If building for a child, you will send the invitation to yourself because you will install for your child: See [Install Loop for Child](gh-deploy.md#install-testflight-loop-for-child)

    ![select your users for the testing group](img/setup-testflight-03.png){width="700"}
    {align="center"}

## Deployment

The [GitHub Deployment](gh-deploy.md) walks you through the steps to deploy to a phone.


## Basic Instructions

The (original from Pete Scwhamb) instructions are provided at the link below.

* [Using GitHub Actions + FastLane to deploy to TestFlight](https://github.com/LoopKit/LoopWorkspace/blob/dev/fastlane/testflight.md)

## Already Have LoopWorkspace

Some people may already have a fork of LoopWorkspace. They might even have one that they forked from somewhere other than LoopKit.

Suggestions - choose one of these methods: 

* Update the repository if it is forked from LoopKit
    * Open your LoopWorkspace repository (`https://github.com/username/LoopWorkspace`) where you use your `username` in the URL
    * Review the graphic in the [Successful Fork](#successful-fork) section
        * Make sure all the items highlighted by red rectangles are correct with the possible exception of your fork being up to date
    * If you see a message that your fork is not up to date - tap on the Sync fork button and follow instructions
    * Continue with the [Create Access Token](#create-access-token) section
* Rename or delete that repository if it is from somewhere other than LoopKit or if you just prefer to start fresh
    * Instructions to do this will be added later
    * You just need to make sure that a repository called LoopWorkspace is no longer in your GitHub account
    * Return to [Fork LoopWorkspace](#fork-loopworkspace) and follow all the instructions

