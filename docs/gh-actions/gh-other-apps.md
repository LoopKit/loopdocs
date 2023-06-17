## Using GitHub to Build Other Apps

Once Loop 3 was released with the ability to build using a browser, a lot of other repositories in the DIY universe began to add the same feature.

The same technique is used and the same six Secrets are applied to each repository. Those secrets are tied to your Apple Developer ID and your GitHub account. As other apps are updated, they will be added to this page and the list below will be updated.

* LoopCaregiver
* Loop Follow

!!! warning "GH_PAT - NEW RECOMMENDATION"
    It is now recommended that you use a GitHub Personal Access Token (GH_PAT) that never expires

    - [GitHub Update: Regenerate GitHub Token](gh-update.md#regenerate-github-token)

    If you choose a GitHub personal access token that expires, you will get an email to renew it about 6 days ahead. You will paste your updated GH_PAT into the secrets for each repository you use and initiate the Build Action for that app. This will ensure continued availability of all your apps that you build with this method.

### Prerequisites

Wait until the repository you are interested in adds the capability of GitHub build. Many of the steps for each repository are the same as what you used (or would use) for Loop, but you need to take some unique steps. The directions are structured to minimize the need to jump between the pages.

* If you have already built using this GitHub method, it is easy to build the next repository. Skip ahead to [Fork and Add Secrets](#fork-and-add-secrets)

* If this is the first repository you have built with GitHub, you must first complete the initial steps found on [GitHub First-Time](../gh-actions/gh-first-time.md). When you reach the point where
    * You have created your Match-Secrets repository
    * You are told to [GitHub First-Time: Fork LoopWorkspace](../gh-actions/gh-first-time.md#fork-loopworkspace)
        * Review the directions but don't do it
        * Return here and check the table below
        * Use that table to find the link of the repository you will fork

Many graphics on this page show LoopWorkspace, just remember to use the repository for the app you want to build.

## Fork and Add Secrets

* You will return to this page after reviewing (but not doing) this step [GitHub First-Time: Fork LoopWorkspace](../gh-actions/gh-first-time.md#fork-loopworkspace)
    * Use the same method as that section, but fork the repository for the app you plan to build
    * If there is no row for an app, then wait until one is added - that repository is probably not ready yet

| App | Fork from this Address | Documentation |
|---|---|---|
| LoopCaregiver | [https://github.com/LoopKit/LoopCaregiver](https://github.com/LoopKit/LoopCaregiver) | [LoopDocs: LoopCaregiver](../nightscout/remote-overrides.md#loopcaregiver) |
|Loop Follow | [https://github.com/jonfawcett/LoopFollow](https://github.com/jonfawcett/LoopFollow) | [Loop Follow](https://github.com/jonfawcett/LoopFollow#loop-follow)|


## Configure Secrets for this App

After successfully creating your fork of the repository for this app:

* If you have already built Loop using GitHub, skip ahead to [Add Existing Secrets](#add-existing-secrets)

* If this is the first repository you have built with GitHub
    * You should follow the detailed steps at [GitHub First-Time: Configure Secrets](../gh-actions/gh-first-time.md#configure-secrets), except you will apply the Secrets to the repository for the app you are planning to build
    * Once your 6 secrets have been added, return to this page and skip ahead to [Action: Add Identifiers](#action-add-identifiers) on this page.

### Add Existing Secrets

!!! tip "MATCH_PASSWORD"
    An early version of GitHub First-Time had incorrect information about the need to save MATCH_PASSWORD.

    If you did not save your MATCH_PASSWORD in your file with all your Secrets, you will need to delete your Match-Secrets repository, create a new one and then add all your Secrets into all you repositories again and run all the Actions again.

Open the text file in which you maintain a copy of your 6 Secrets so you can copy each value into the Secrets for this repository.

1. Click on the repository for your app
1. Click on the Settings Icon near the top right of your repository
    * On the left side, tap on `Secrets and variables` dropdown and choose Actions
    * After you select Actions, your screen should look like the graphic below

    ![action secrets and variables screen](img/gh-actions-secrets.svg){width="700"}
    {align="center"}

1. Tap on `New repository secret` and add each of the 6 Secrets
    * You will notices the New secret dialog looks a little different
    * As soon as you click on the Name* Box, the 6 Secret Names show up as a dropdown as shown in the graphic below
    * Select each one in turn and paste the secret value into the Secret* box and hit Add secret

    ![dialog for entering a new secret](img/repeat-secret-dialog.png){width="500"}
    {align="center"}

Once all six Secrets are added, you will either continue to add the identifiers (LoopCaregiver) or use the updated method to first validate your secrets (Loop Follow).

## Action: Validate Secrets

The first action step is to Validate Secrets.

![actions shown for Loop 3.1 and newer versions](img/gh-actions-3.1.png){width="200"}
{align="left"}

When building LoopCaregiver, the new steps are not yet available, so you'll skip ahead to [Action: Add Identifiers](#action-add-identifiers).

Near the top middle of your Repository fork, click on the "Actions" tab.

* The first time you click on `Actions` with this repository you'll be informed that `Workflows aren't being run on this forked repository`
* Tap on the green button that says: `I understand my workflows, go ahead and enable them`

The workflows are now displayed: look at the list on the left side similar to that shown in the graphic below. (You can dismiss the Actions Enabled message using the X near the upper right side if it appears).

This step validates most of your six Secrets and provides error messages if it detects an issue with one or more.

1. Click on the "Actions" tab of your LoopWorkspace repository and enable workflows if needed
1. On the left side, select "1. Validate Secrets".
1. On the right side, click "Run Workflow", and tap the green `Run workflow` button.
1. Wait, and within a minute or two you should see a green checkmark indicating the workflow succeeded.
1. The workflow will check if the required secrets are added and that they are correctly formatted. If errors are detected, please check the run log for details.

Until LoopCaregiver is also updated, the instructions for the rest of this page won't include the numbers for the successive steps.

## Action: Add Identifiers

Near the top middle of your Repository fork, click on the "Actions" tab.

* The first time you click on `Actions` with this repository you'll be informed that `Workflows aren't being run on this forked repository`
* Tap on the green button that says: `I understand my workflows, go ahead and enable them`

The workflows are now displayed: look at the list on the left side similar to that shown in the graphic below. (You can dismiss the Actions Enabled message using the X near the upper right side if it appears).

* The graphic below is an example from Loop, your screen will show your app and associated repository

![workflows displayed](img/gh-workflows-enabled.png){width="700"}
{align="center"}

### Add Identifiers

* The graphic below is an example from Loop, your screen will show your app and associated repository

Refer to the graphic below for the numbered steps:

1. Click on the "Actions" tab of your repository
1. On the left side, click on "Add Identifiers"
1. On the right side, click "Run Workflow" to show a drop-down menu
    * You will see your default branch (should be `main`)
    * If you have additional branches, you can change the branch, for example, select `dev` for the development branch
1. Tap the green button that says "Run workflow".

    ![add identifiers using github actions](img/action-02-add-identifiers.svg){width="700"}
    {align="center"}

The Add Identifier Action should complete (succeed or fail) in a few minutes.

* If you see the green check continue to the next section
* If you see the red X
    * [Examine the Error](gh-errors.md#examine-the-error) tells you how to download the file needed to diagnose your problem.
    * [Action: Add Identifiers Errors](gh-errors.md#action-add-identifiers-errors) lets you know what to search for in the downloaded file
    * Once you've resolved the error, repeat the [Add Identifiers](#add-identifiers) step

## Review App Identifier

Open this link: [Certificates, Identifiers & Profiles: Identifiers List](https://developer.apple.com/account/resources/identifiers/list) on the apple developer site.

After successfully performing the Add Identifiers Action, you will see the identifier for your app with a Name and Bundle ID matching that in the table below. You will see your unique TEAMID embedded in the identifier. (If you previously built this App with Xcode, the name may start with XC but the ending should match.)

| App Name | Name | Bundle ID |
| --- | --- | --- |
| LoopCaregiver | LoopCaregiver | com.TEAMID.loopkit.LoopCaregiver |
| Loop Follow | LoopFollow | com.TEAMID.LoopFollow |

Some apps, like Loop, require updates to the Identifiers after they are generated.

Other apps, like LoopCaregiver and Loop Follow, do not require updates to Identifiers after they are generated.

!!! warning "LoopCaregiver is under development"
    This app is proving very useful already, but it is still under development. When you fork this from the repository, you will notice that dev branch is the default.

    Please follow the discussion in the [Loop Caregiver App](https://loop.zulipchat.com/#narrow/stream/358458-Loop-Caregiver-App) zulipchat stream.

If your app is not listed in the Update Required section, skip ahead to [Create App in App Store Connect](#create-app-in-app-store-connect).

### Update Required

This is the list of apps that require you to modify the Identifier(s) before continuing.

#### App Name

There are no apps in this section yet.

## Create App in App Store Connect

You will be following the directions below to create an App in App Store Connect if you don't already have one.

This requires you to provide some information. Examine the table below for the bundle ID associated with your app. 

| App Name | Bundle ID |
| --- | --- |
| LoopCaregiver | com.TEAMID.loopkit.LoopCaregiver |
| Loop Follow | com.TEAMID.LoopFollow |

1. Open this link: [App Store Connect / Apps](https://appstoreconnect.apple.com/apps) to view your apps; log in if needed. 

1. If this App already exists, you can continue to [Create Certificates](#create-certificates)
1. Click the Add Apps button or the blue "plus" icon and select New App as shown in the graphic below

    ![choose to add a new app](img/new-app-in-store.png){width="300"}
    {align="center"}

1. The New App dialog box opens and should appear similar to the graphic below. Before you fill anything out, make sure your Bundle ID is available in the dropdown menu. If you do not see the Bundle ID for your app; back out of this screen and follow the directions in [GitHub First-Time: Find My Loop](gh-first-time.md#find-my-loop), where you'll be finding App Name instead of Loop.
    * Select "iOS".
    * Enter a name: this will have to be unique
        * You could start with "App Name ABC" where ABC are your initials
        * If that is already taken, you can add a number, for example, "App Name ABC 123"
        * This name is what you see on the App Store Connect list and in the TestFlight app
        * Once installed on your phone, you will see the actual app name
        * You can [Change the App Store Connect Name](../gh-actions/gh-deploy.md#change-the-app-store-connect-name) later if you want
    * Select your primary language.
    * Choose the bundle ID for your app
    * SKU can be anything; for example "123" but must be unique across all your apps, so try 1234 or 12345 depending on how many apps you build with this method
    * Select "Full Access".

    ![create loop app in store connect - with missing bundle id](img/create-app-in-store.png){width="600"}
    {align="center"}

1. Click Create but do not fill out the next form. That is for submitting to the app store and you will not be doing that.

You are done with this activity. You can close the browser tab, but before you do, note the TestFlight tab at the top of the page. You'll be using that tab after you complete the next two actions.

## Create Certificates

* The graphic below is an example from Loop, your screen will show your app and associated repository

Refer to the graphic below for the numbered steps:

1. Click on the "Actions" tab of your Repository repository
1. On the left side, click on "Create Certificates"
1. On the right side, click "Run Workflow" to show a drop-down menu
    * You will see your default branch (should be `main`)
    * If you have additional branches, you can change the branch, for example, select `dev` for the development branch
1. Tap the green button that says "Run workflow".

    ![create certificates using github actions](img/action-03-create-certs.svg){width="700"}
    {align="center"}

1. Wait a minute or two for the action to finish
    * If this action fails, head over to [Action: Create Certificates Errors](gh-errors.md#action-create-certificates-errors)
    * Once you've resolved the error, repeat the Actions [Add Identifiers](#add-identifiers) and then Create Certificates. (The Add Identifiers might not be required but it is fast and should be done as a matter of routine.)


## Build App

* The graphic below is an example from Loop, your screen will show your app and associated repository

Refer to the graphic below for the first four steps:

1. Click on the "Actions" tab of your Repository repository.
1. On the left side, click on "Build App Name".
1. On the right side, click "Run Workflow" to show a drop-down menu
    * You will see your default branch for this app
1. Tap the green button that says "Run workflow".

    ![build loop using github actions](img/action-04-build-loop.svg){width="700"}
    {align="center"}

1. Wait a few minutes to make sure there is not an early failure
    * If this action fails, head over to [Action: Build Loop Errors](gh-errors.md#action-build-loop-errors)
    * Once you've resolved the error, it's a good idea to repeat all three steps in this order:
        * [Add Identifiers](#add-identifiers)
        * Create Certificates
        * Build Loop
1. If the process appears to be happening without an error, go do something else for a while. The build should take about 20-30 minutes.
1. Your app should eventually appear on [App Store Connect](https://appstoreconnect.apple.com/apps).

## Add Users to TestFlight for App

Once the first build completes, you will be able to configure TestFlight for the app - follow the template for setting up TestFlight for Loop found in [GitHub First-Time: Set Up Users and Access (TestFlight)](../gh-actions/gh-first-time.md#set-up-users-and-access-testflight)

## Deployment

The [GitHub Deployment](gh-deploy.md) walks you through the steps to deploy to a phone. When going through those steps, replace your App Name for Loop. Everything else is the same.


