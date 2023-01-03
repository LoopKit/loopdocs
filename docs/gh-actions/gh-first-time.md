## Build Loop using GitHub Actions

This is only available with Loop 3 and Loop dev branch.

You can build Loop-dev using your github.com account and your (paid) Apple Developer account using a browser. You no longer require a Mac computer.

The first time you build with this method requires significant time to set up your configuration. Count on several hours.

Subsequent builds take about half hour to complete, but very little time on your part. Most of that time is taken by github completing the build for you.

**You must build Loop every 90 days when you use github actions.**


## Configure to use GitHub Build Actions

!!! warning "These instructions are under construction"
    The original instructions for using GitHub Build Actions are provided at a link at the bottom of this page.

    Enhanced instructions with more hand-holding and graphics are being developed. This enhanced set of instructions contains all the information from the original instructions, but gets very terse near the end (where it is identical to the original instructions.)

Review the entire process before starting and then go through slowly and carefully.

These instructions allow you to build Loop without having access to a Mac. They also allow you to easily install Loop on phones that are not connected to your computer.

* You can send builds and updates to those you care for easily
* You can access and install Loop if you lose or damage your device
* You do not need to worry about correct Xcode/Mac versions

The setup steps are somewhat involved, but nearly all are one time steps. Subsequent builds are trivial. The initial steps are best done on a computer where you can save and archive files for later use.

TestFlight can be used to deploy Loop to a child's phone (under age 13 in the US) but requires a few extra steps on the phone itself. See [Install TestFlight Loop for Child](gh-deploy.md#install-testflight-loop-for-child).

Your app must be updated once every 90 days, but it's a simple click to make a new build and can be done from anywhere, see [Update Loop using GitHub Actions](gh-update.md).

### Save Your Information

!!! tip "Archive This Information"
    For many of the steps on this page, you will need to have access to usernames, email addresses, passwords, and in some cases, special parameters. The API Key can only be downloaded one time - you must save it in a safe place. If you loose it, you'll need to generate a new key and update the secret settings in your fork of the LoopWorkspace repository. Same for the github access token you will generate in another step.

    * Record these in a safe place so you can find them when you need them
    * A digital copy is best because you will be copying and pasting in different locations

This list indicates what you need to record (save digitally so you can copy and paste). Notice that some information is created in one place and used in another. The items in all capital letters will be added to the `Secret Settings` for your LoopWorkspace repository. So they are listed twice in the list below.

* At developer.apple.com
    * Email address (this is your username)
    * password
    * TEAMID
    * FASTLANE_KEY_ID
    * FASTLANE_ISSUER_ID
    * FASTLANE_KEY
* At github.com
    * Email address
    * password
    * username
    * Your github repository address will be: `https://github.com/username`
    * Your LoopWorkspace repository address will be: `https://github.com/username/LoopWorkspace`
    * github access token (GH_PASS)
    * a password - whatever you want (MATCH_PASSWORD)
* Needed when you [Configure Secret Settings](#configure-secret-settings).
    * TEAMID
    * FASTLANE_KEY_ID
    * FASTLANE_ISSUER_ID
    * FASTLANE_KEY
    * GH_PASS
    * MATCH_PASSWORD


## Prerequisites

There are only two prerequisites to Build Loop with this method.

1. Paid Apple Developer account
1. Free GitHub account

You will need TestFlight, from the Apple App Store, installed on your [Compatible Phone](../build/step2.md); you will install Loop using TestFlight. In order to use Loop, you need a [Compatible Pump](../build/step3.md) and [Compatible CGM](../build/step4.md). For pumps other than Omnipod DASH, you also need a [RileyLink Compatible Device](../build/step5.md).

For the initial steps, you'll be going back and forth between the github and developer webpages. It is best to open each in a separate window or tab for your browser.

## Apple Developer Account

If you have an Apple Developer Account, you need to sign in to your account. There will be links to take you to specific pages in the account website, but you need to be logged in.

If you do not already have a paid Apple Developer account, you need to purchase one ($99 annual fee). It may take a few days for the account to be enabled.

* LoopDocs has an [Apple Developer Program](../build/step6.md) page that explains in detail how to sign up for an account
* This link takes you straight to [Apple Developer account](https://developer.apple.com) to sign up

### Generate API Key

You cannot generate the API Key until you have the paid Apple Developer account set up. If you are still waiting for Apple to enable your account, you can skip ahead to complete part of the github steps but you will need to pause at [Configure Secret Settings](#configure-secret-settings).

This section will walk you the steps required to gather or create these parameters.

|Name|Description|
|---------|---------|
|TEAMID|10-character identifier|
|FASTLANE_KEY_ID|Key ID generated for you in App Store Connect|
|FASTLANE_ISSUER_ID|The issuer ID is shown when the Key ID is displayed|
|FASTLANE_KEY|Copy the full key from the text file.<br>including the "-----BEGIN PRIVATE KEY-----" and "-----END PRIVATE KEY-----" lines. |

Each step has a link to take you to the specific page you need to do the next step. It is best if you open each link in a separate tab or window so you can refer back to these instructions as you move along.

1. Click on this link: [Apple developer portal page](https://developer.apple.com/account/resources/certificates/list).
    * Look at the upper right hand corner of that page
    * The 10-character ID number below your name is your `TEAMID`
    * Record this for use when you configure your secret settings
1. Click on this link: [App Store Connect/Access/API](https://appstoreconnect.apple.com/access/api)
    * If this is your first time here, there will be a dialog for you to follow:

        "Permission is required to access the App Store Connect API. You can request access on behalf of your organization."

        * Click on `Request Access` and follow directions until access is granted

    * Click the "Keys" tab and then click the blue &plus; sign
    * A new "Generate API Key" dialog box will appear in which you enter the name of the key as "FastLane API Key" and choose "Admin" in the access drop down menu. Click on the "Generate" button.
    * The Keys screen is seen again and should look similar to the graphic below - yours will have only one Active key
    * To generate this graphic, a new key was added called LoopDocs-test. Your key should say FastLane API key. It will show the Key ID and show a button to "Download API Key". The Key ID and Issuer ID are obscured in this graphic.
    * Wait until told to press the button to "Download API Key".

    ![App Store Connect Key page](img/dev-api-key.svg){width="700"}
    {align="center"}

1. Record the Key ID found on the line with the key name; this will be used for `FASTLANE_KEY_ID`. When you hover over the key, the instructions `Copy Key ID` will show up beside the key. If you click on that, the key is copied to your paste buffer.
1. Record the Issuer ID above the word Active (this is the same for all keys that you generate with this Apple Developer ID); this will be used for `FASTLANE_ISSUER_ID`. Use the Copy button to make sure you get the full ID.
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

## GitHub Account

If you have a github.com account, you can skip to [Create GitHub Repositories](#setup-github). Make sure you know your github associated email, username and password.

If you do not already have a github.com account, you need to create one. Be sure to record the email, password and username for your github account.

Decide on a couple of usernames that you will be happy with - this will get embedded into your github URL. Your first choice might not be available, so be prepared with several candidates. Your personal github URL will be: `https://github.com/username`.

* Click on this link to sign up for a free account: [github account signup](https://github.com/signup)
    * You will need to enter the **email** you want associated with github
    * You will be asked to enter a **password**
    * You will be asked to enter a **username**
    * You will be asked if you want email, ok to say N for no
    * Solve the puzzle to prove you're a person
    * Check the associated **email** to get the code and enter the code into github to confirm your account
* You should get the Welcome to GitHub screen
    * Indicate it is "Just me" on your team and Continue
    * Don't check anything on the next screen, just tap Continue
    * Select the Free option by selecting "Continue for Free"

The free level comes with plenty of storage and compute time to build loop.

## Setup GitHub

Now you will create one new repository and then fork the LoopWorkspace repository.

### Create Match-Secrets

Open your github URL (this is `https://github.com/username`).

1. At the top right of the screen, click on the &plus; sign and select New Repository

    ![plus sign to add repository](img/create-match-secrets.svg){width="200"}
    {align="center"}

1. Create a [new empty repository](https://github.com/new) titled `Match-Secrets`.
    * Be sure the check the box to make the repository private (you will be storing your keys here)
    * Scroll to the bottom of the pages and tap on "Create Repository"
    * You'll be shown a new screen with a lot of options - just ignore this

You will not be interacting with your Match-Secrets repository directly. It needs to exist for other actions to work correctly. You are done with this part of the set up.

### Fork LoopWorkspace

1. Open this link [https://github.com/LoopKit/LoopWorkspace](https://github.com/LoopKit/LoopWorkspace) to open the LoopWorkspace repository owned by LoopKit.
1. At upper right side of the screen, click on the word Fork, it should open the screen shown below.
    * Uncheck the selection that says "Copy the dev branch only" so it looks like the graphic

    ![fork information for LoopWorkspace](img/gh-fork-loopworkspace.png){width="700"}
    {align="center"}

1. Tap the Create Fork button

### Create Access Token

1. You will be creating a new token and giving it the name "FastLane Access Token"
1. Open this link: [https://github.com/settings/tokens/new](https://github.com/settings/tokens/new)
    * In the box below Note, enter "FastLane Access Token".
    * 30 days is fine
    * Select the `repo` permission scope (check the box to the left of repo)
    * Scroll all the way to the bottom and click "Generate token"
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
    * On the left side, find the Secrets dropdown and choose Actions
    * Your screen should look like the graphic below

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

Now that all six secrets have been added to your LoopWorkspace, you are done with Settings. The next section will be working with the Actions tab that you see at the top middle of the display (not the one in the settings list on the left side).


## Add Identifiers for Loop

Near the top middle of your LoopWorkspace fork, there is an Actions tab.

1. Click on the "Actions" tab of your LoopWorkspace repository.
    * You'll be informed that Workflows were disabled on your fork
    * Tap on the green button that says: "I understand my workflows, enable them"
    * The workflows are now displayed: look at the list on the left side
1. Select "Add Identifiers".
1. On the right side, click "Run Workflow" to show a drop-down and tap the green button.
1. Wait, and within a minute or two you should see a green checkmark indicating the workflow succeeded.
    * If this action fails, you probably made an error in one of your secrets
    * Try to determine which one was incorrect by clicking on the failed action link to see the full log
    * Go back and enter the secret(s) again - you will need your github password to change a secret

## Configure Identifiers for Loop

If you have already built Loop via Xcode using this Apple ID, you can skip some steps but first, read this.

In the instructions for people who have never built Loop, they are instructed to look for 4 identifier names and configure them with the App Group associated with their TEAMID. The 4 identifiers that need this association are:

* Loop
* Loop Intent Extension
* Loop Status Extension
* Small Status Widget

When you have already built Loop with Xcode, the Loop identifier is already associated with your App Group with time sensitive capability.  Your existing Loop identifier will have a name that starts with XC as shown below, where your 10-digit team ID is used.

* Name: XC com TEAMID loopkit Loop
* Indentifier: com.TEAMID.loopkit.Loop

If you look at [Certificates, Identifiers & Profiles](https://developer.apple.com/account/resources/identifiers/list) and find that name and identifier, you can skip ahead to [Create Loop App in App Store Connect](#create-loop-app-in-app-store-connect). If you've done a lot of building with Xcode, there may be a lot of names here.

### Create App Group

1. Open this link: [Register an App Group](https://developer.apple.com/account/resources/identifiers/applicationGroup/add/) on the apple developer site.
1. For Description, use "Loop App Group".
1. For Identifier, enter "group.com.TEAMID.loopkit.LoopGroup", subsituting your team id for `TEAMID`.
1. Click "Continue" and then "Register".

### Add App Group to Bundle Identifiers

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
1. Remember to do this for each of the identifiers above.

### Add Time Sensitive Capability

1. Go to [Certificates, Identifiers & Profiles](https://developer.apple.com/account/resources/identifiers/list) on the apple developer site.
1. Click on the "Loop" identifier
1. Scroll down to "Time Sensitive Notifications"
1. Tap the check box to enable Time Sensitive Notifications.
1. Click "Save".
1. Click "Confirm".

## Create Loop App in App Store Connect

If you built using Xcode with your Apple Developer ID, you were able to skip the steps from the prior few sections - they are already configured.

If you have created a Loop app in App Store Connect before, you can skip this section as well.

1. Open this link: [apps list](https://appstoreconnect.apple.com/apps) on App Store Connect and click the blue "plus" icon to create a New App.
    * Select "iOS".
    * Select a name: this will have to be unique, so you may have to try a few different names here. It will not be the name you see on the app on your phone, but it is the name you see in TestFlight when you install it on your phone.
    * Select your primary language.
    * Choose the bundle ID that matches `com.TEAMID.loopkit.Loop`, with TEAMID matching your team id.
    * SKU can be anything; e.g. "123".
    * Select "Full Access".
1. Click Create

Do not fill out the next form. That is for submitting to the app store and you will not be doing this.

You are done with this activity and can close the browser tab.

## Create Building Certficates

1. Go back to the "Actions" tab of your LoopWorkspace repository in github.
1. Select "Create Certificates" (on the left).
1. Click "Run Workflow" on the right, and tap the green button in the drop down.
1. Wait, and within a minute or two you should see a green checkmark indicating the workflow succeeded.

## Build Loop

1. Click on the "Actions" tab of your LoopWorkspace repository.
1. Select "Build Loop".
1. Click "Run Workflow", select your branch, and tap the green button.
1. You have some time now. Go enjoy a coffee. The build should take about 20-30 minutes.
1. Your app should eventually appear on [App Store Connect](https://appstoreconnect.apple.com/apps).
1. For each phone/person you would like to support Loop on:
    * Add them in [Users and Access](https://appstoreconnect.apple.com/access/users) on App Store Connect.
    * Add them to your TestFlight Internal Testing group
    * If building for a child, you will send the invitation to yourself because you will install for your child: See [Install Loop for Child](gh-deploy.md#install-testflight-loop-for-child)]

## Deployment

The [GitHub Deployment](gh-deploy.md) walks you through the steps to deploy to a phone.


## Basic Instructions

The (original) instructions are provided at the link below.

* [Using GitHub Actions + FastLane to deploy to TestFlight](https://github.com/LoopKit/LoopWorkspace/blob/dev/fastlane/testflight.md)