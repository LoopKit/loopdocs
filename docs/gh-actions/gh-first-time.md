## Build Loop using Github Actions

This is only available with Loop 3 and Loop dev branch.

You can build Loop-dev using your github.com account and your (paid) Apple Developer account using a browser. You no longer require a Mac computer.

The first time you build with this method requires significant time to set up your configuration. Count on several hours.

Subsequent builds are very fast.

**You must build Loop every 90 days when you use this github actions.**

## Basic Instructions

The (original) instructions in the link below are basic - please read carefully and use the links provided in these directions.

* [Using Github Actions + FastLane to deploy to TestFlight](https://github.com/LoopKit/LoopWorkspace/blob/dev/fastlane/testflight.md)

## Expanded Instructions

Several people contributed updates to the instructions. The expanded instructions are a work in progress. Refer back to the original instructions if you run into a problem.

Please - review all the instruction before starting and then go through slowly and carefully.

These instructions allow you to build Loop without having access to a Mac. They also allow you to easily install Loop on phones that are not connected to your computer. 

* You can send builds and updates to those you care for easily
* You can access and install Loop if you loose or damage your device
* You do not need to worry about correct Xcode/Mac versions

An app built using this method can be deployed to newer versions of iOS, as soon as they are available.

The setup steps are somewhat involved, but nearly all are one time steps. Subsequent builds are trivial. The initial steps are best done on a computer where you can save and archive files for later use.

Note that TestFlight can be deployed to a child's phone (under age 13) but requires a few extra steps on the phone itself. See [Install Loop for Child](gh-deploy.md#install-loop-for-child).

Your app must be updated once every 90 days, but it's a simple click to make a new build and can be done from anywhere, see [Update Loop using Github Actions](gh-update.md).

For many of the steps on this page, you will need to have access to user names, email addresses, passwords, and in some cases, special parameters. The API Key can only be downloaded one time - you must save it in a safe place. If you loose it, you'll need to generate a new key and update the Match-Secrets repository.

* Record these in a safe place so you can find them when you need them
* A digital copy is best because you will be copying and pasting in different locations


## Prerequisites

There are only two prerequisites to Build Loop with this method.

1. Free Github account
1. Paid Apple Developer account

Once built, you will need to deploy the app to your phone and use a compatible pump and CGM.

For the initial steps, you'll be going back and forth between the github and developer webpages. It is best to open each in a separate window or tab for your browser.

### Free Github Account

If you have a github.com account, you can skip to [Apple Developer Account](#apple-developer-account). Make sure you have your github username and password handy for later.

If you do not already have a github.com account, you need to create one. Be sure to record the email, password and username for your github account.

* Click on this link to sign up for a free account: [github account signup](https://github.com/signup)
    * You will need to enter the **email** you want associated with github
    * You will be asked to enter a **password**
    * You will be asked to enter a **username**
    * You will be asked it you want email, ok to say N for no
    * Solve the puzzle to prove you're a person
    * Check the associated **email** to get the code and enter the code into github to confirm your account
* You should get the Welcome to GitHub screen
    * Indicate it is "Just me" on your team and Continue
    * Don't check anything on the next screen, just tap Continue
    * Select the Free option by selecting "Continue for Free"

The free level comes with plenty of storage and compute time to build loop.

You are done with this step - you can leave the page open or come back later to do the next steps. Just make sure you keep your account information stored so you can return.

### Apple Developer Account

If you have an Apple Developer Account, you need to sign in to your account. There will be links to take you to specific pages in the account website, but you need to be logged in.

If you do not already have a paid Apple Developer account, you need to purchase one ($99 annual fee). It may take a few days for the account to be enabled.

* LoopDocs has an [Apple Developer Program](../build/step6.md) page that explains in detail how to sign up for an account
* This link takes you straight to [Apple Developer account](https://developer.apple.com) to sign up


## Generate App Store Connect API Key

You need specific parameters to set up your certificates for the build process. This section will walk you through the steps summarized below.

The parameters you create in this step will later be copied into your Match-Secrets repository that you will create in the next step. You will be typing in both the Name and the value when you set up your private Match-Secrets repository in github.com with your key information. For now you are generating the values and you'll use them later.

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
    * Record this for use in your Match-Secrets repository
1. Click on this link: [App Store Connect](https://appstoreconnect.apple.com/access/api)
    * Click the "Keys" tab
    * Create a new key with "Admin" access
    * For the name of the key, use "FastLane API Key"
    * After you click the word "Generate", the Keys screen is seen again and should look similar to the graphic below
    * To generate this graphic, a new key was added called LoopDocs-test. Your key should say FastLane API key. It will show the Key ID and show a button to "Download API Key". The Key ID and Issuer ID are obscured in this graphic.
    * Wait until told to press the button to "Download API Key".

    ![App Store Connect Key page](img/dev-api-key.svg){width="700"}
    {align="center"}

1. Record the Key ID found on the line with the key name; this will be used for `FASTLANE_KEY_ID`.
1. Record the Issuer ID above the word Active (this is the same for all keys that you generate with this ID); this will be used for `FASTLANE_ISSUER_ID`. Use the Copy button to make sure you get the full ID.
1. Click on the Download API Key button - you will be warned you can only download this once.

    ![download key only once](img/dev-dl-key-once.png){width="700"}
    {align="center"}

6. Find your AuthKey download in your downloads folder. The name of the file with start with "AuthKey_KeyID.p8" where KeyID matches the value above. Double-click to open it and you will be presented a message asking how you'd like to open it. Click on "Choose Application..." and then select "TextEdit" as your application to open it with.

    ![img/apns-open.png](img/apns-open.png)

    ![img/apns-textedit.png](img/apns-textedit.png)

1. The contents of this file will be used for `FASTLANE_KEY`. Copy the full text, including the "-----BEGIN PRIVATE KEY-----" and "-----END PRIVATE KEY-----" lines.

1. When the file opens, it will look similar to the screenshot below. In a few minutes, after we do a few other steps first, we will need to highlight **ALL OF THE CONTENTS** of that file and copy it because we will be pasting it in Heroku. Yes, allllll of the contents. So, easiest way is to click inside that file and then press `command-a` to highlight all the text and then `command-c` to copy it all to the clipboard. You don't have to do it right now...just keep that window open in the background for now until we need it a little further down. Then we will copy all that text.

![img/apns-copy-key.png](img/apns-copy-key.png)
1. Record the key id; this will be used for `FASTLANE_KEY_ID`.
1. Record the issuer id; this will be used for `FASTLANE_ISSUER_ID`.
1. Click on the Download API Key button
1. Download the API key itself, and open it in a text editor. The contents of this file will be used for `FASTLANE_KEY`. Copy the full text, including the "-----BEGIN PRIVATE KEY-----" and "-----END PRIVATE KEY-----" lines.

## Setup Github

### Create Match-Secrets Repository

Log in to your github account.

1. At the top right of the screen, click on the &plus; sign and select New Repository

![plus sign to add repository](img/create-match-secrets.svg){width="200"}
{align="center"}


1. Create a [new empty repository](https://github.com/new) titled `Match-Secrets`. It should be private.
1. Fork https://github.com/LoopKit/LoopWorkspace into your account.
1. Create a [new personal access token](https://github.com/settings/tokens/new):
    * Enter a name for your token. Something like "FastLane Access Token".
    * 30 days is fine, or you can select longer if you'd like.
    * Select the `repo` permission scope.
    * Click "Generate token".
    * Copy the token and record it. It will be used below as `GH_PAT`.
1. In the forked LoopWorkspace repo, go to Settings -> Secrets -> Actions.
1. For each of the following secrets, tap on "New repository secret", then add the name of the secret, along with the value you recorded for it:
    * `TEAMID`
    * `FASTLANE_KEY_ID`
    * `FASTLANE_ISSUER_ID`
    * `FASTLANE_KEY`
    * `GH_PAT`
    * `MATCH_PASSWORD` - just make up a password for this

## Add Identifiers for Loop App

1. Click on the "Actions" tab of your LoopWorkspace repository.
1. Select "Add Identifiers".
1. Click "Run Workflow", and tap the green button.
1. Wait, and within a minute or two you should see a green checkmark indicating the workflow succeeded.

## Create App Group

If you have already built Loop via Xcode using this Apple ID, you can skip on to [Create Loop App in App Store Connect](#create-loop-app-in-app-store-connect).

1. Go to [Register an App Group](https://developer.apple.com/account/resources/identifiers/applicationGroup/add/) on the apple developer site.
1. For Description, use "Loop App Group".
1. For Identifier, enter "group.com.TEAMID.loopkit.LoopGroup", subsituting your team id for `TEAMID`.
1. Click "Continue" and then "Register".

## Add App Group to Bundle Identifiers

1. Go to [Certificates, Identifiers & Profiles](https://developer.apple.com/account/resources/identifiers/list) on the apple developer site.
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

## Add Time Sensitive Notifications to Loop App ID
1. Go to [Certificates, Identifiers & Profiles](https://developer.apple.com/account/resources/identifiers/list) on the apple developer site.
1. Click on the "Loop" identifier
1. Scroll down to "Time Sensitive Notifications"
1. Tap the check box to enable Time Sensitive Notifications.
1. Click "Save".
1. Click "Confirm".

## Create Loop App in App Store Connect

If you have created a Loop app in App Store Connect before, you can skip this section as well.

1. Go to the [apps list](https://appstoreconnect.apple.com/apps) on App Store Connect and click the blue "plus" icon to create a New App.
    * Select "iOS".
    * Select a name: this will have to be unique, so you may have to try a few different names here, but it will not be the name you see on your phone, so it's not that important.
    * Select your primary language.
    * Choose the bundle ID that matches `com.TEAMID.loopkit.Loop`, with TEAMID matching your team id.
    * SKU can be anything; e.g. "123".
    * Select "Full Access".
1. Click Create

You do not need to fill out the next form. That is for submitting to the app store.

## Create Building Certficates

1. Go back to the "Actions" tab of your LoopWorkspace repository in github.
1. Select "Create Certificates".
1. Click "Run Workflow", and tap the green button.
1. Wait, and within a minute or two you should see a green checkmark indicating the workflow succeeded.

## Build Loop!

1. Click on the "Actions" tab of your LoopWorkspace repository.
1. Select "Build Loop".
1. Click "Run Workflow", select your branch, and tap the green button.
1. You have some time now. Go enjoy a coffee. The build should take about 20-30 minutes.
1. Your app should eventually appear on [App Store Connect](https://appstoreconnect.apple.com/apps).
1. For each phone/person you would like to support Loop on:
    * Add them in [Users and Access](https://appstoreconnect.apple.com/access/users) on App Store Connect.
    * Add them to your TestFlight Internal Testing group.


## Deployment

The [GH Deployment](gh-deploy.md) walks you through the steps to deploy to a phone. The following facts are useful to know before you move on to that page.

After successfully building Loop using Actions in github, here are two important things to know. The next statements might not make sense to you if you have not gone to the link above and reviewed the instructions.

1. Once you have installed TestFlight on your phone and you see your app in the TestFlight screen, tap on it to see an expanded screen with an option to automatically update or not.  You should choose which you prefer.
    * If you leave automatic update enabled (default), then whenever you issue Build Action command on from your LoopWorkspace fork, the version of the app on the phone will be installed.
    * WARNING: If you later want to build using Xcode, you must first disable automatic update or Xcode will not be able to install to your phone.

1. The Apple ID used to sign in for TestFlight on a given phone does not have to match the Apple ID of the phone user. This is important for children. [Loopers Need Their Own Apple ID](../build/step6.md#loopers-need-their-own-apple-id), but children cannot use TestFlight with their ID. If you plan to [Install Loop for Child](#install-loop-for-child), you will need to use your ID on their phone (not the whole phone - just the Media & Purchase portion), so send the TestFlight invitation to the email associated with your ID.

