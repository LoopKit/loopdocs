## Quick-Start Page for Browser Build with GitHub Actions

The instructions for building Loop with a Browser using GitHub Actions can appear overwhelming when every step is fully detailed including graphics.

* It can be difficult to see the forest for the trees
* This page lists the top level steps and includes links to detailed steps on other pages

!!! info "Time Estimate"
    - If you have never built Loop (allow up to one week elapsed time)
        * Requesting and getting an Apple Developer Account: 1-2 days
        * Creating and configuring your GitHub repositories (without Apple Information): 1-2 hours
        * Adding Secrets (requires Apple Developer Account): 1 hour
        * Performing the Action steps: 30 minutes to 2 hours
    - If you have previously built Loop with Xcode you have fewer steps and are probably familiar with some of the concepts
        * Expect 1 to 2 hours

!!! abstract "Summary"
    Once you have Apple Developer and GitHub accounts:

    * Apple: Generate an API Key
    * GitHub:
        * Create an access token (GH_PAT)
        * Create a Match-Secrets private repository
        * Fork a repository (copy of LoopWorkspace)
        * Add Secrets to your repository
        * Action: 1. Verify Secrets
        * Action: 2. Add Identifiers
    * Apple:
        * Configure Identifiers for Loop
        * Create your version of Loop in App Store (personal use only, not for distribution)
    * GitHub:
        * Action: 3. Create Certificates
        * Action: 4. Build Loop
    * Apple: Set up Internal TestFlight Group
    * Phone: Install Loop with TestFlight

!!! question "FAQs"
    - **Do I need a Mac computer?** No. This can be done on any browser, although it will be easier using a computer or tablet than just using a phone.
    - **Can I do this on my phone?** Yes, but the graphics shown on this page are from a computer browser.
    - **Isn't it hard to build every 90 days?** The initial setup and deployment take a lot of your focused time. But once you build once, subsequent builds take very little of your time to start, then the rest is done automatically.
    - **Can I use this for my child?** You, as the adult, can install using TestFlight on your child's phone. The explicit steps are provided at [GitHub Deploy: Install TestFlight Loop for Child](gh-deploy.md#install-testflight-loop-for-child).
    - **Can I still use my customizations?** Yes. [Customize with GitHub](gh-customize.md)

**You must build Loop every 90 days when you use GitHub build method.**

* We recommend you configure your GitHub personal access token to never expire
    * If you have one that expires, go to [GitHub Update: Regenerate GitHub Token](gh-update.md#regenerate-github-token) to generate a new token that does not expire
* Building a new version literally takes seconds once open your browser and go to your GitHub account

## Quick-Start List

Each link below takes you to a more detailed section for you to review if desired. At the end of each detailed section, there is a `Return to Quick-Start` link to return you to this page.

### [Prerequisites](gh-first-time.md#prerequisites)

Click the link above to read more detailed information about the prerequisites required to Build, Install and Use the Loop app. 

The prerequisites are:

* A [GitHub account](https://github.com/signup). The free level comes with plenty of storage and free compute time to build loop, multiple times a day, if you wanted to.
* A paid [Apple Developer account](https://developer.apple.com).

### [New Terms with GitHub Build](gh-first-time.md#new-terms-with-github-build)

Click the link above to read about some new terms that you may not be familiar with.

### [Summary of Browser Build Steps](gh-first-time.md#summary-of-browser-build-steps)

Click on the link above if you want to know what you are going to do before you do any of it.

If you just want to do the steps, keep going.

### [Save Six Secrets](gh-first-time.md#save-your-information)

Click on the link above if you want more detailed information about the information you will be creating and saving.

You require 6 Secrets (alphanumeric items) to use the GitHub build method and if you use the GitHub method to build more than Loop, e.g., Loop Follow or LoopCaregiver, you will use the same 6 Secrets for each app you build with this method. Each secret is indentified below by `ALL_CAPITAL_LETTER_NAMES`.

* Four Secrets are from your Apple Account
* Two Secrets are from your GitHub account
* Be sure to save the 6 Secrets in a text file using a text editor
    - Do **NOT** use a smart editor, which might auto-correct and change case, because these Secrets are case sensitive

### [Collect the Four Apple Secrets](../gh-actions/gh-first-time.md#generate-api-key)

Click the link above for detailed instructions for obtaining the four Secrets needed from Apple.

This step is common for all GitHub Browser Builds; do this step only once. You will be saving 4 Secrets from your Apple Account in this step.

1. Sign in to the [Apple developer portal page](https://developer.apple.com/account/resources/certificates/list).
1. Copy the Team ID from the upper right of the screen. Record this as your `TEAMID`.
1. Go to the [App Store Connect](https://appstoreconnect.apple.com/access/api) interface, click the "Keys" tab, and create a new key with "Admin" access. Give it the name: "FastLane API Key".
1. Record the issuer id; this will be used for `FASTLANE_ISSUER_ID`.
1. Record the key id; this will be used for `FASTLANE_KEY_ID`.
1. Download the API key itself, and open it in a text editor. The contents of this file will be used for `FASTLANE_KEY`. Copy the full text, including the "-----BEGIN PRIVATE KEY-----" and "-----END PRIVATE KEY-----" lines.

### Collect the Two GitHub Secrets

* Click here for detailed information about creating a [New GitHub Account](../gh-actions/gh-first-time.md#new-github-account)

* Click here for more detailed information on how to [Create GitHub Personal Access Token](../gh-actions/gh-first-time.md#create-github-personal-access-token)

Otherwise, keep going.

### Create GitHub Personal Access Token

Log into your GitHub account to create a personal access token; this is one of two GitHub secrets needed for your build. (Right click on the link below to open the required webpage.)

1. (Right click on link) to create a [new personal access token](https://github.com/settings/tokens/new):
    * Enter a name for your token, use "FastLane Access Token".
    * Change the Expiration selection to `No expiration`.
    * Select the `repo` and `workflow` permission scopes.
    * Click "Generate token".
    * Copy the token and record it. It will be used below as `GH_PAT`.

### Make up a Password

This is the second of two GitHub secrets needed for your build.

The first time you build with the GitHub Browser Build method for any DIY app, you will make up a password and record it as `MATCH_PASSWORD`. Note, if you later lose `MATCH_PASSWORD`, you will need to delete and make a new Match-Secrets repository (next step).

### [Setup GitHub Match-Secrets Repository](../gh-actions/gh-first-time.md#create-match-secrets)

Click on the link above if you need detailed instructions with graphics for creating your Match-Secrets Repository. Otherwise, follow the instructions below.

The creation of the Match-Secrets repository is a common step for all GitHub Browser Builds; do this step only once. You must be logged into your GitHub account.

1. (Right click on link) to create a [new empty repository](https://github.com/new) titled `Match-Secrets`. It should be private.

Once created, you will not take any direct actions with this repository; it needs to be there for the GitHub to use as you progress through the steps.

### [Setup GitHub LoopWorkspace Repository](../gh-actions/gh-first-time.md#fork-loopworkspace)

Click on the link above if you need detailed instructions with graphics for creating your LoopWorkspace Repository. Otherwise, follow the instructions below.

1. Fork [https://github.com/LoopKit/LoopWorkspace](https://github.com/LoopKit/LoopWorkspace) into your account.
1. In the forked LoopWorkspace repo, go to Settings -> Secrets and variables -> Actions.

### [Configure Secrets](../gh-actions/gh-first-time.md#configure-secrets)

Click on the link above if you need detailed instructions with graphics to configure your secrets. These secrets must be added to each repositiory but apply to all branches for a given repositisory. In other words - do this for LoopWorkspace and then you might also repeat this step for LoopCaregiver. You add the same 6 secrets every time.

For each of the following secrets, tap on "New repository secret", then add the name of the secret, along with the value you recorded for it:

* `TEAMID`
* `FASTLANE_ISSUER_ID`
* `FASTLANE_KEY_ID`
* `FASTLANE_KEY`
* `GH_PAT`
* `MATCH_PASSWORD`

### [Validate repository secrets](../gh-actions/gh-first-time.md#validate-secrets)

Click on the link above if you need detailed instructions with graphics for running a GitHub Action (all 4 actions use the same procedure). 

Otherwise, follow the instructions below.

This step validates most of your six Secrets and provides error messages if it detects an issue with one or more.

1. Click on the "Actions" tab of your LoopWorkspace repository and enable workflows if needed
1. On the left side, select "1. Validate Secrets".
1. On the right side, click "Run Workflow", and tap the green `Run workflow` button.
1. Wait, and within a minute or two you should see a green checkmark indicating the workflow succeeded.
1. The workflow will check if the required secrets are added and that they are correctly formatted. If errors are detected, please check the run log for details.

## Add Identifiers for Loop App

1. Click on the "Actions" tab of your LoopWorkspace repository.
1. On the left side, select "2. Add Identifiers".
1. On the right side, click "Run Workflow", and tap the green `Run workflow` button.
1. Wait, and within a minute or two you should see a green checkmark indicating the workflow succeeded.

### [Create App Group](../gh-actions/gh-first-time.md#create-app-group)

Click on the link above if you need detailed instructions with graphics for creating and applying the App Group, otherwise, follow the instructions below.

If you have already built Loop via Xcode using this Apple ID, you can skip on to [Add App Group to Bundle Identifiers](#add-app-group-to-bundle-identifiers).

1. Go to [Register an App Group](https://developer.apple.com/account/resources/identifiers/applicationGroup/add/) on the apple developer site.
1. For Description, use "Loop App Group".
1. For Identifier, enter "group.com.TEAMID.loopkit.LoopGroup", subsituting your team id for `TEAMID`.
1. Click "Continue" and then "Register".

## [Add App Group to Bundle Identifiers](../gh-actions/gh-first-time.md#add-app-group-to-bundle-identifiers)

Click on the link above if you need detailed instructions with graphics for add the App Group to the other bundle identifiers, otherwise, follow the instructions below.

Note 1 - If you previously built with Xcode, the `Names` listed below may be different, but the `Identifiers` will match. A table is provided below the steps to assist. The Add Identifier Action that you completed above generates 6 identifiers, but only 4 need to be modified as indicated in this step.

Note 2 - Depending on your build history, you may find some of the Identifiers are already configured - and you are just verifying the status; but in other cases, you will need to configure the Identifiers.

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

#### Table with Name and Identifier for Loop 3

| NAME | IDENTIFIER |
|-------|------------|
| Loop | com.TEAMID.loopkit.Loop |
| Loop Intent Extension | com.TEAMID.loopkit.Loop.Loop-Intent-Extension |
| Loop Status Extension | com.TEAMID.loopkit.Loop.statuswidget |
| Small Status Widget | com.TEAMID.loopkit.Loop.SmallStatusWidget |
| WatchApp | com.TEAMID.loopkit.Loop.LoopWatch |
| WatchAppExtension | com.TEAMID.loopkit.Loop.LoopWatch.watchkitextension |


### [Create Loop App in App Store Connect](../gh-actions/gh-first-time.md#create-loop-app-in-app-store-connect)

Click on the link above if you need detailed instructions with graphics for creating the Loop App in App Store Connect, otherwise, follow the instructions below.

If you have created a Loop app in App Store Connect before, you can skip this section.

1. Right click on the link [apps list](https://appstoreconnect.apple.com/apps) top open App Store Connect and click the blue "plus" icon to create a New App.
    * Select "iOS".
    * Select a name: this will have to be unique, so you may have to try a few different names here, but it will not be the name you see on your phone, so it's not that important.
    * Select your primary language.
    * Choose the bundle ID that matches `com.TEAMID.loopkit.Loop`, with TEAMID matching your team id.
    * SKU can be anything; e.g. "123".
    * Select "Full Access".
1. Click Create

You do not need to fill out the next form. That is for submitting to the app store.

### [Create Certficates](../gh-actions/gh-first-time.md#create-certificates)

Click on the link above if you need detailed instructions with graphics for creating the certificates needed to build the Loop app, otherwise, follow the instructions below.

1. Go back to the "Actions" tab of your LoopWorkspace repository in GitHub.
1. On the left side, select "3. Create Certificates".
1. On the right side, click "Run Workflow", and tap the green `Run workflow` button.
1. Wait, and within a minute or two you should see a green checkmark indicating the workflow succeeded.

## Create a branch named "alive"

!!! tip "For dev only at this time"
    The automatic rebuild only works for the dev branch at this time. Work is in process to automatically create the alive branch if it does not exist.

    If you are using main (released) branch, skip ahead to [Build Loop](#build-loop)

TestFlight builds expire after 90 days. This process you are implementing here will update and rebuild Loop periodically, and requires that you create a branch named "alive" so that GitHub will not inactivate the scheduled rebuild if no code updates are made.

The "alive" branch will only receive some additional commits to its history, and is not used for building the app.

1. Go to the "Code" tab of your LoopWorkspace repository.
1. Click the branch selection dropdown button, and then `View all branches`.
1. Click the green "New branch" button (upper right).
1. Type `alive` in the  "New branch name" field.
1. Select `LoopKit/LoopWorkspace` as "Source".
1. Select `dev` in the branch dropdown.
1. Click the green "Create new branch" button.

## [Build Loop](../gh-actions/gh-first-time.md#build-loop)

Click on the link above if you need detailed instructions with graphics to build the Loop app, otherwise, follow the instructions below.

1. Click on the "Actions" tab of your LoopWorkspace repository.
1. On the left side, select "4. Build Loop".
1. On the right side, click "Run Workflow", and tap the green `Run workflow` button.
1. You have some time now. Go enjoy a coffee. The build should take about 20-30 minutes.
1. Your app should eventually appear on [App Store Connect](https://appstoreconnect.apple.com/apps).
1. For each phone/person you would like to support Loop on:
    * Add them in [Users and Access](https://appstoreconnect.apple.com/access/users) on App Store Connect.
    * Add them to your TestFlight Internal Testing group.

## TestFlight and Deployment Details

Please refer to:

* [LoopDocs: Set Up Users](https://loopkit.github.io/loopdocs/gh-actions/gh-first-time/#set-up-users-and-access-testflight)
* [LoopDocs: Deploy](https://loopkit.github.io/loopdocs/gh-actions/gh-deploy/)

