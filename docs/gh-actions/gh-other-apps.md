## Build Other Apps using a Browser

Once Loop 3 was released with the ability to build using a browser, a lot of other apps in the DIY universe added the same feature. **Only apps that are companions to&nbsp;_<span translate="no">Loop</span>_&nbsp;are included on this page.** If you want to build another DIY app that is not included here, look for the file `fastlane/testflight.md` in the *GitHub* repository associated with that app and open it in a browser. The instruction for that app should be located in that file.

The same technique is used and the same six <code>Secrets</code> are applied to each `repository`. Those secrets are tied to your *Apple* Developer ID and your *GitHub* account.

* _<span translate="no">Loop Caregiver</span>_
* _<span translate="no">Loop Follow</span>_

!!! warning "GH_PAT - NEW RECOMMENDATION"
    It is now recommended that you use a *GitHub* Personal Access Token (GH_PAT) that never expires

    - [Update with Browser: Regenerate Token](gh-update.md#regenerate-token)

### Prerequisites

* If you have already built using the Browser Build method, it is easy to build other apps which use the same method. Skip ahead to [<span translate="no">Fork and Add Secrets</span>](#fork-and-add-secrets)

* If this is the first repository you have built with the Browser Build method, you must first complete the initial steps found on [Configure to Use Browser](../gh-actions/gh-first-time.md). When you reach the point where
    * You have created your Match-Secrets repository
    * You are told to [Configure to Use Browser: <span translate="no">Fork LoopWorkspace</span>](../gh-actions/gh-first-time.md#fork-loopworkspace)
        * Review the directions but don't do it
        * Return here and check the table below
        * Use that table to find the link of the repository you will fork

!!! important "Use the <code>repository</code> for the application you are building"
    Many graphics on this page show&nbsp;<span translate="no">LoopWorkspace</span>, just remember to use the <code>repository</code> for the app you want to build, that is either&nbsp;_<span translate="no">Loop Caregiver</span>_&nbsp;or &nbsp;_<span translate="no">Loop Follow</span>_.

## <span translate="no">Fork and Add Secrets</span>

* You will return to this page after reviewing (but not doing) this step [Configure to Use Browser: <span translate="no">Fork LoopWorkspace</span>](../gh-actions/gh-first-time.md#fork-loopworkspace)
    * Use the same method as that section, but <span>`fork` the `repository` for the app</span> you plan to build
    * _<span translate="no">Loop Caregiver</span>_, expect the `dev branch`
    * _<span translate="no">Loop Follow</span>_, expect the `main branch`

| App | Fork from this Address | Documentation |
|---|---|---|
| <span translate="no">Loop Caregiver</span> | [https://github.com/LoopKit/LoopCaregiver](https://github.com/LoopKit/LoopCaregiver) | [LoopDocs: <span translate="no">Loop Caregiver</span>](../nightscout/loop-caregiver.md) |
| <span translate="no">Loop Follow</span> | [https://github.com/loopandlearn/LoopFollow](https://github.com/loopandlearn/LoopFollow) | [<span translate="no">Loop Follow</span>](https://www.loopandlearn.org/loop-follow)|

## Configure <code>Secrets</code> for this App

After successfully creating your fork of the repository for this app:

* If you have already built Loop using the Browser Build method, skip ahead to [Add Existing <code>Secrets</code>](#add-existing-secrets)

* If this is the first repository you have built with *GitHub*
    * You should follow the detailed steps at [Configure to Use Browser: Configure <code>Secrets</code>](../gh-actions/gh-first-time.md#configure-secrets), except you will apply the <code>Secrets</code> to the repository for the app you are planning to build
    * Once your 6 secrets have been added, return to this page and skip ahead to [Validate <code>Secrets</code>](#validate-secrets) on this page.

### Add Existing <code>Secrets</code>

!!! tip "MATCH_PASSWORD"
    An early version of *GitHub* First-Time had incorrect information about the need to save MATCH_PASSWORD.

    If you did not save your MATCH_PASSWORD in your file with all your <code>Secrets</code>, you will need to delete your Match-Secrets repository, create a new one and then add all your <code>Secrets</code> into all you repositories again and run all the Actions again.

    Instructions are found at [Reset Match-Secrets](gh-errors.md#reset-match-secrets).

Open the text file in which you maintain a copy of your 6 <code>Secrets</code> so you can copy each value into the <code>Secrets</code> for this repository.

1. Click on the repository for your app
1. Click on the Settings Icon near the top right of your repository
    * On the left side, tap on `Secrets and variables` dropdown and choose Actions
    * After you select Actions, your screen should look like the graphic below

    ![action secrets and variables screen](img/gh-actions-secrets.svg){width="700"}
    {align="center"}

1. Tap on `New repository secret` and add each of the 6 <code>Secrets</code>
    * You will notices the New secret dialog looks a little different
    * As soon as you click on the Name* Box, the 6 Secret Names may show up as a dropdown as shown in the graphic below
    * Select each one in turn and paste the secret value into the Secret* box and hit Add secret
    * If they do not appear in a dropdown, enter them exactly as shown (suggest copy / paste from your text file)

    ![dialog for entering a new secret](img/repeat-secret-dialog.png){width="500"}
    {align="center"}

Once all six <code>Secrets</code> are added, you will proceed to the first Action to validate your secrets.

## Validate <code>Secrets</code>

The first action step is to Validate <code>Secrets</code>. Near the top middle of your Repository fork, click on the `Actions` tab.

* The first time you click on `Actions` with this repository you'll be informed that `Workflows aren't being run on this forked repository`
* Tap on the green button that says: `I understand my workflows, go ahead and enable them`

The workflows are now displayed: look at the list on the left side similar to that shown in the graphic below. (You can dismiss the Actions Enabled message using the X near the upper right side if it appears).

* The graphic below is an example from Loop, your screen will show your app and associated repository

This step validates most of your six <code>Secrets</code> and provides error messages if it detects an issue with one or more.

1. Click on the "Actions" tab of your  *Loop Follow*  or  *Loop Caregiver*repository and enable workflows if needed
1. On the left side, click on 1. <code>Validate Secrets</code>
1. On the right side, click `Run Workflow` to show a drop-down menu
    * You will see your default branch (`main` for LoopFollow, `dev` for LoopCaregiver)
    * You can select a different branch, but typically, you run the default
1. Tap the green button that says `Run workflow`.

![add identifiers using github actions](img/action-01-validate-secrets.svg){width="700"}
{align="center"}

The `Validate Secrets` &nbsp;<span class=notranslate>Action</span>&nbsp; should succeed or fail in a few minutes. Do not continue to the next step until this one succeeds.

* If you see the green check (:octicons-check-circle-fill-16:{: .passed })  continue to the next section
* If you see the red `X` (:octicons-x-circle-fill-16:{: .failed }):
    * [Examine the Error](gh-errors.md#examine-the-error) tells how to view the file needed to diagnose your problem.
    * [Action: Validate <code>Secrets</code> Errors](gh-errors.md#action-validate-secrets-errors) tells you what to search for in the file
    * Resolve the error and repeat the Action: [Validate <code>Secrets</code>](#validate-secrets)

## Add Identifiers

Near the top middle of your Repository fork, click on the "Actions" tab.

* The graphic below is an example from Loop, your screen will show your app and associated repository

Refer to the graphic below for the numbered steps:

1. Click on the "Actions" tab of your repository
1. On the left side, click on "Add Identifiers"
1. On the right side, click "Run Workflow" to show a drop-down menu
    * You will see your default branch (`main` for LoopFollow, `dev` for LoopCaregiver)
    * You can select a different branch, but typically, you run the default
1. Tap the green button that says "Run workflow"

    ![add identifiers using github actions](img/action-02-add-identifiers.svg){width="700"}
    {align="center"}

The `Add Identifier` &nbsp;<span class=notranslate>Action</span>&nbsp; should succeed or fail in a few minutes.

* If you see the green check (:octicons-check-circle-fill-16:{: .passed })  continue to the next section
* If you see the red `X` (:octicons-x-circle-fill-16:{: .failed }):
    * [Examine the Error](gh-errors.md#examine-the-error) tells how to view the file needed to diagnose your problem
    * [Action: Add Identifiers Errors](gh-errors.md#action-add-identifiers-errors) tells you what to search for in the file
    * Resolve the error and repeat the Action: [Add Identifiers](#add-identifiers)

## Review App Identifier

Open this link: [Certificates, Identifiers & Profiles: Identifiers List](https://developer.apple.com/account/resources/identifiers/list) on the apple developer site.

After successfully performing the `Add Identifiers Action`, you will see the identifier for your app with a Name and Bundle ID matching that in the table below. You will see your unique TEAMID embedded in the identifier. (If you previously built this App with Xcode, the name may start with XC but the ending should match.)

| App Name | Name | Bundle ID |
| --- | --- | --- |
| <span translate="no">Loop Caregiver</span> | <span translate="no">Loop Caregiver</span> | <span translate="no">com.TEAMID.loopkit.LoopCaregiver</span> |
| <span translate="no">Loop Follow</span> | <span translate="no">LoopFollow</span> | <span translate="no">com.TEAMID.LoopFollow</span> |

Some apps, like the *Loop* app, require updates to the `Identifier` after they are generated.

The *Loop Caregiver* app and the *Loop Follow* app, do not require that extra step. Stay tuned - there may be an update for the *Loop Caregiver* app later that will require modification of the `Identifier`.

## Create App in App Store Connect

You will be following the directions below to create an App in App Store Connect if you don't already have one.

This requires you to provide some information. Examine the table below for the bundle ID associated with your app. 

| App Name | Bundle ID |
| --- | --- |
| <span translate="no">Loop Caregiver</span> | <span translate="no">com.TEAMID.loopkit.LoopCaregiver</span> |
| <span translate="no">Loop Follow</span> | <span translate="no">com.TEAMID.LoopFollow</span> |

1. Open this link: [App Store Connect / Apps](https://appstoreconnect.apple.com/apps) to view your apps; log in if needed. 

1. If this App already exists, you can continue to [Create Certificates](#create-certificates)
1. Click the Add Apps button or the blue "plus" icon and select New App as shown in the graphic below

    ![choose to add a new app](img/new-app-in-store.png){width="300"}
    {align="center"}

1. The New App dialog box opens and should appear similar to the graphic below. Before you fill anything out, make sure your Bundle ID is available in the dropdown menu. If you do not see the Bundle ID for your app; back out of this screen and follow the directions in [Configure to Use Browser: Find My Loop](gh-first-time.md#find-my-loop), where you'll be finding App Name instead of Loop.
    * Select "iOS".
    * Enter a name: this will have to be unique
        * You could start with "App Name ABC" where ABC are your initials
        * If that is already taken, you can add a number, for example, "App Name ABC 123"
        * This name is what you see on the App Store Connect list and in the *TestFlight* app
        * Once installed on your phone, you will see the actual app name
        * You can [Change the App Store Connect Name](../gh-actions/gh-deploy.md#change-the-app-store-connect-name) later if you want
    * Select your primary language.
    * Choose the bundle ID for your app
    * SKU can be anything; for example "123" but must be unique across all your apps, so try 1234 or 12345 depending on how many apps you build with this method
    * Select "Full Access".

    ![create loop app in store connect - with missing bundle id](img/create-app-in-store.png){width="600"}
    {align="center"}

1. Click Create but do not fill out the next form. That is for submitting to the app store and you will not be doing that.

You are done with this activity. Before you close this browser window, note the *TestFlight* tab at the top of the page. You'll be using that tab after you complete the next two actions.

## Create Certificates

* The graphic below is an example from Loop. Your screen will show your app and associated repository.

Refer to the graphic below for the numbered steps:

1. Click on the "Actions" tab of your Repository repository
1. On the left side, click on "Create Certificates"
1. On the right side, click "Run Workflow" to show a drop-down menu
    * You will see your default branch (`main` for LoopFollow, `dev` for LoopCaregiver)
    * You can select a different branch, but typically, you run the default
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
1. On the left side, click on "Build *App Name*".
1. On the right side, click "Run Workflow" to show a drop-down menu
    * You will see your default branch (`main` for LoopFollow, `dev` for LoopCaregiver)
    * You can select a different branch, but typically, you run the default
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

## Add Users to *TestFlight* for App

Once the first build completes, you will be able to configure *TestFlight* for the app - follow the template for setting up *TestFlight* for Loop found in [Configure to Use Browser: Set Up Users and Access (TestFlight)](../gh-actions/gh-first-time.md#set-up-users-and-access-testflight).

## Install on Phone

The [Install on Phone](gh-deploy.md) walks you through the steps to install the app to a phone. When going through those steps, replace your App Name for&nbsp;_<span translate="no">Loop</span>_. Everything else is the same.


