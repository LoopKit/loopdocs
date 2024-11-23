## Build Other Apps using a Browser

Once Loop 3 was released with the ability to build using a browser, a lot of other apps in the DIY universe added the same feature.

**Only apps that are companions to&nbsp;_<span translate="no">Loop</span>_&nbsp;are included on this page.**

* _<span translate="no">LoopCaregiver</span>_
* _<span translate="no">LoopFollow</span>_

If you want to build another DIY app that is not included here, look for the file `fastlane/testflight.md` in the *GitHub* repository associated with that app and open it in a browser. The instructions for that app should be located in that file.

The same technique is used and the same six <code>Secrets</code> are applied to each `repository`. Those secrets are tied to your *Apple* Developer ID and your *GitHub* account.

### Updating / Rebuilding Other Apps

If you are coming to this page to update one of the other apps, follow the [How to Update or Rebuild](bb-update.md#how-to-update-or-rebuild){: target="_blank" } instructions provided for the *Loop* app, but substitute the repository name for the app you want to rebuild for all references to&nbsp;*<span translate="no">LoopWorkspace</span>*.

### Optional Build Method

!!! tip "Optional - Set up a Organization Account"
    If you are going to be building a lot of different apps, you can choose to set up a free organization account with *GitHub* and use that to build.

    Pros:

    * The 6 <code>Secrets</code> can be added to the organization one-time and apply to every repository

    Cons:

    * The displays for an organization are slightly different than for a personal account but are not hard to navigate if you are computer literate and feel comfortable using a browser

    For more information, see [Use a *GitHub* Organization Account](#use-a-github-organization-account).

### Multiple Copies of `LoopFollow`

For the convenience of caregivers who use `LoopFollow` to monitor multiple people, updates were added in v2.1.2 to make this more convenient. This works regardless of the build method. (Build with Browser or [Build with *Mac*](https://www.loopandlearn.org/loop-follow#lf-script){: target="_blank" }).

* Build up to three instances of `LoopFollow`
* Customize the name of the app that appears on your phone
* Display the custom name in the main `LoopFollow` screen

### Prerequisites

* If you have already built using the Browser Build method, it is easy to build other apps which use the same method. Skip ahead to [<span translate="no">Fork and Add Secrets</span>](#fork-and-add-secrets).

* If this is the first repository you have built with the Browser Build method

    * Begin reading at [Configure to Use Browser: Introduction and Summary](intro-summary.md){: target="_blank" }
    * Follow all the instructions on the [Collect Secrets](secrets.md){: target="_blank" } page
    * After all your secrets are collected, continue on this page with [<span translate="no">Fork and Add Secrets</span>](#fork-and-add-secrets).

## <span translate="no">Fork and Add Secrets</span>
    
!!! important "Use the <code>repository</code> for the application you are building"
    Many graphics show&nbsp;<span translate="no">LoopWorkspace</span>. You need to replace that with the <code>repository</code> for the app you want to build. You may need to adjust the App Name, the Shared App Group and look for different Identifiers.
    
    Instructions for&nbsp;_<span translate="no">LoopCaregiver</span>_&nbsp;or &nbsp;_<span translate="no">LoopFollow</span>_ are found on this page.
    
    Other apps such as xDrip4iOS and Trio can also be built with this method. Refer to the repository associated with those other apps, examine the fastlane folder and open the testflight.md file in your browser to get specific details for building that app.

You will return to this page after reviewing (but not doing) this step [Configure to Use Browser: <span translate="no">Fork LoopWorkspace</span>](prepare-fork.md#fork-loopworkspace)

* Use the same method as that section, but <span>`fork` the `repository` for the app</span> you plan to build
* _<span translate="no">LoopCaregiver</span>_, expect the `dev branch`
* _<span translate="no">LoopFollow</span>_, expect the `main branch`

### Table of App `Repositories`

| App | Fork from this Address | Documentation |
|---|---|---|
| <span translate="no">LoopCaregiver</span> | [https://github.com/LoopKit/LoopCaregiver](https://github.com/LoopKit/LoopCaregiver){: target="_blank" } | [LoopDocs: <span translate="no">LoopCaregiver</span>](../nightscout/loop-caregiver.md) |
| <span translate="no">LoopFollow</span> | [https://github.com/loopandlearn/LoopFollow](https://github.com/loopandlearn/LoopFollow){: target="_blank" } | [<span translate="no">LoopFollow</span>](https://www.loopandlearn.org/loop-follow){: target="_blank" }|

The two repositories below are only if you need to follow a second or third looper. All others should use just the table above. The instructions for the second and third looper are otherwise identical to the first looper. Note that `LoopCaregiver` can follow multiple Loopers; you select the person inside the app.

| Special Case | Fork from this Address |
|---|---|
| <span translate="no">LoopFollow for a Second Looper</span> | [https://github.com/loopandlearn/LoopFollow_Second](https://github.com/loopandlearn/LoopFollow_Second){: target="_blank" } |
| <span translate="no">LoopFollow for a Third Looper</span> | [https://github.com/loopandlearn/LoopFollow_Third](https://github.com/loopandlearn/LoopFollow_Third){: target="_blank" } |

## Configure <code>Secrets</code> for this App

> If you choose to use the optional *GitHub* organization method, you can skip this section:

> * All `repositories` in your *GitHub* organization use the organization <code>Secrets</code>
> * Make sure you complete [Add <code>Secrets</code> to your *GitHub* Organization](#add-secrets-to-your-github-organization) instead of this section
> * Skip ahead to [Validate <code>Secrets</code>](#validate-secrets)

After successfully creating your fork of the repository for this app:

* If you have already built Loop using the Browser Build method, skip ahead to [Add Existing <code>Secrets</code>](#add-existing-secrets)

* If this is the first repository you have built with *GitHub*
    * You should follow the detailed steps at [Configure to Use Browser: Configure <code>Secrets</code>](../browser/prepare-fork.md#configure-secrets){: target="_blank" }, except you will apply the <code>Secrets</code> to the repository for the app you are planning to build
    * Once your 6 secrets have been added, return to this page and skip ahead to [Validate <code>Secrets</code>](#validate-secrets) on this page.

### Add Existing <code>Secrets</code>

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

Once all six <code>Secrets</code> are added, proceed to the first Action to validate your secrets.

## Validate <code>Secrets</code>

The first action step is to Validate <code>Secrets</code>. Near the top middle of your Repository fork, click on the `Actions` tab.

* The first time you click on `Actions` with this repository you'll be informed that `Workflows aren't being run on this forked repository`
* Tap on the green button that says: `I understand my workflows, go ahead and enable them`

The workflows are now displayed: look at the list on the left side similar to that shown in the graphic below. (You can dismiss the Actions Enabled message using the X near the upper right side if it appears).

* The graphic below is an example from Loop, your screen will show your app and associated repository

This step validates most of your six <code>Secrets</code> and provides error messages if it detects an issue with one or more.

1. Click on the "Actions" tab of your  *LoopFollow*  or  *LoopCaregiver*repository and enable workflows if needed
1. On the left side, click on 1. <code>Validate Secrets</code>
1. On the right side, click `Run Workflow` to show a dropdown menu
    * You will see your default branch (`main` for LoopFollow, `dev` for LoopCaregiver)
    * You can select a different branch, but typically, you run the default
1. Tap the green button that says `Run workflow`.

![add identifiers using github actions](img/action-01-validate-secrets.svg){width="700"}
{align="center"}

The `Validate Secrets` &nbsp;<span class=notranslate>Action</span>&nbsp; should succeed or fail in a few minutes. Do not continue to the next step until this one succeeds.

* If you see the green check (:octicons-check-circle-fill-16:{: .passed })  continue to the next section
* If you see the red `X` (:octicons-x-circle-fill-16:{: .failed }):
    * [Examine Annotation](bb-errors.md#examine-annotation){: target="_blank" } tells how to view the file needed to diagnose your problem.
    * [Action: Validate <code>Secrets</code> Errors](bb-errors.md#action-validate-secrets-errors){: target="_blank" } tells you what to search for in the file
    * Resolve the error and repeat the Action: [Validate <code>Secrets</code>](#validate-secrets)

## Add Identifiers

Near the top middle of your Repository fork, click on the "Actions" tab.

* The graphic below is an example from Loop, your screen will show your app and associated repository

Refer to the graphic below for the numbered steps:

1. Click on the "Actions" tab of your repository
1. On the left side, click on "Add Identifiers"
1. On the right side, click "Run Workflow" to show a dropdown menu
    * You will see your default branch (`main` for LoopFollow, `dev` for LoopCaregiver)
    * You can select a different branch, but typically, you run the default
1. Tap the green button that says "Run workflow"

    ![add identifiers using github actions](img/action-02-add-identifiers.svg){width="700"}
    {align="center"}

The `Add Identifier` &nbsp;<span class=notranslate>Action</span>&nbsp; should succeed or fail in a few minutes.

* If you see the green check (:octicons-check-circle-fill-16:{: .passed })  continue to the next section
* If you see the red `X` (:octicons-x-circle-fill-16:{: .failed }):
    * [Examine Annotation](bb-errors.md#examine-annotation){: target="_blank" } tells how to view the file needed to diagnose your problem
    * [Action: Add Identifiers Errors](bb-errors.md#action-add-identifiers-errors){: target="_blank" } tells you what to search for in the file
    * Resolve the error and repeat the Action: [Add Identifiers](identifiers.md#add-identifiers)

## Review App Identifier

Open this link: [Certificates, Identifiers & Profiles: Identifiers List](https://developer.apple.com/account/resources/identifiers/list){: target="_blank" } on the apple developer site.

After successfully performing the `Add Identifiers Action`, you will see the identifier for your app with a Name and Bundle ID matching that in the table below. You will see your unique TEAMID embedded in the identifier. (If you previously built this App with Xcode, the name may start with XC but the ending should match.)

| App Name | Name | Bundle ID |
| --- | --- | --- |
| <span translate="no">LoopCaregiver</span> | <span translate="no">LoopCaregiver</span> | <span translate="no">com.TEAMID.loopkit.LoopCaregiver</span> |
| <span translate="no">LoopFollow</span> | <span translate="no">LoopFollow</span> | <span translate="no">com.TEAMID.LoopFollow</span> |

> If you build from a second or third `repository` for `LoopFollow`, the Name will end in `Second` or `Third` and Bundle ID will have `.Second` or `.Third` at the end.

The *LoopCaregiver* app requires updates to the `Identifiers` after they are generated.

The *LoopFollow* app does not require this extra step. You can skip ahead to [Create App in App Store Connect](#create-app-in-app-store-connect).

## Add `App Group` to `LoopCaregiver`

As of 2023 December 8, the *LoopCaregiver* app requires the addition of an `App Group` to an expanded list of `Identifiers`. Follow these steps one time to be able to build the *LoopCaregiver* app after this update.

### Check if `App Group` Exists

Open this link to view your `applicationGroup` `Identifiers`: [`App Group Identifiers`](https://developer.apple.com/account/resources/identifiers/list/applicationGroup){: target="_blank" }

* No action is required if there is already an identifier with the `NAME` of `LoopCaregiver App Group` and the `IDENTIFIER` contains your `TEAMID` in this format: `group.com.TEAMID.loopkit.LoopCaregiverGroup`
* In that case, you can skip ahead to [Add `App Group` to `Identifiers`](#add-app-group-to-identifiers)

### Create `App Group` for the *LoopCaregiver* App

Open this link: [Register an App Group](https://developer.apple.com/account/resources/identifiers/applicationGroup/add/){: target="_blank" } on the *Apple Developer* site.

1. For **`Description`**, use `LoopCaregiver App Group`
1. For **`Identifier`**, enter `group.com.TEAMID.loopkit.LoopCaregiverGroup`, substituting your team id for `TEAMID`.
1. Double-check the spelling - your `TEAMID` must be correct and the `LoopCaregiverGroup` *App Group* must match the format shown above
    * A mistake here means you will not be able to build the *LoopCaregiver* app until you fix it
1. Click `Continue` and then `Register`.

### Add `App Group` to `Identifiers`

Click to open this link in a new tab: [`Certificates, Identifiers & Profiles: Identifiers List`](https://developer.apple.com/account/resources/identifiers/list){: target="_blank" } on the *Apple Developer* site.


#### Table with Name and Identifier for `LoopCaregiver`

All five of these identifiers should be found after running the `Add Identifier` action on *GitHub*.

If you do not see them, please sync your `LoopCaregiver` repository and then run the [`Add Identifier` action](identifiers.md#add-identifiers). The **`NAME`** might begin with an `XC` if you previously built with Xcode. However, the **`IDENTIFIER`** column value should match.

| `NAME` | `IDENTIFIER` |
|-------|------------|
| `LoopCaregiver` | `com.TEAMID.loopkit.LoopCaregiver` |
| `LoopCaregiverIntentExtension` | `com.TEAMID.loopkit.LoopCaregiver.IntentExtension` |
| `LoopCaregiverWatch` | `com.TEAMID.loopkit.LoopCaregiver.watchkitapp` |
| `LoopCaregiverWatchWidgetExtension` | `com.TEAMID.loopkit.LoopCaregiver.watchkitapp.WidgetExtension` |
| `LoopCaregiverWidgetExtension` | `com.TEAMID.loopkit.LoopCaregiver.WidgetExtension` |

### Add `LoopCaregiverGroup` to each Identifier

Find and click on the row for the `LoopCaregiver` on the [Certificates, Identifiers & Profiles: Identifiers List](https://developer.apple.com/account/resources/identifiers/list){: target="_blank" } page. Look in the **`IDENTIFIER`** column to find `com.TEAMID.loopkit.LoopCaregiver`. The **`NAME`** might begin with an `XC` if you previously built with Xcode. However, the **`IDENTIFIER`** column value should match.

| `NAME` | `IDENTIFIER` |
|-------|------------|
| `LoopCaregiver` | `com.TEAMID.loopkit.LoopCaregiver` |

The `Edit Your App ID Configuration` screen will open.

1. In the `App Services` column, scroll down to the `App Groups` row
    * Ensure the check box (under the `Capabilities` column) for `App Groups` is checked
    * Tap on the word `Edit` or `Configure`, whichever shows up
        * This opens the `App Group Assignment` screen
        * Check the box by `LoopCaregiver` *App Group* that uses your `TEAMID` in `group.com.TEAMID.loopkit.LoopCaregiver` 
        * If the box by `Loop App Group` is checked, you should uncheck it
        * Your screen should be similar to the graphic below
        * If you made any changes, tap `Continue`, otherwise, tap `Cancel`

    ![select the loopcaregiver app group](img/lcg-app-group.png){width="600"}
    {align="center"}

2. If you modified settings for an *identifier*, the `Save` button at the top right will become active. Click on `Save` before leaving this page - otherwise, the change does not take effect.

    * Tap on `Save`
    * This opens the `Modify App Capabilities` confirmation screen
    * Click on `Confirm`

3. If you did not need to make changes, the `Save` button will not be active.

    * Tap on the `< All Identifiers` link at the top left

4. The full list of Identifiers should be displayed again.

5. Continue down the list until every identifier in the table below has the `App Group` for `LoopCaregiver App Group` added to it. (DO NOT SELECT the `Loop App Group`) If you miss any, the *GitHub* action to `3. Create Certificates` will succeed but the *GitHub* action to `4. Build LoopCaregiver` will fail.

| `NAME` | `IDENTIFIER` |
|-------|------------|
| `LoopCaregiver` | `com.TEAMID.loopkit.LoopCaregiver` |
| `LoopCaregiverIntentExtension` | `com.TEAMID.loopkit.LoopCaregiver.IntentExtension` |
| `LoopCaregiverWatch` | `com.TEAMID.loopkit.LoopCaregiver.watchkitapp` |
| `LoopCaregiverWatchWidgetExtension` | `com.TEAMID.loopkit.LoopCaregiver.watchkitapp.WidgetExtension` |
| `LoopCaregiverWidgetExtension` | `com.TEAMID.loopkit.LoopCaregiver.WidgetExtension` |

## Create App in App Store Connect

!!! abstract "Same procedure as for the *Loop* app"
    You will follow the same procedure as you did with the *Loop* app.

    You will also want to edit your new app once you create it to [Remove Apple Vision Pro](prepare-app.md#remove-apple-vision-pro){: target="_blank" }.

You will be following the directions below to create an App in App Store Connect if you don't already have one.

This requires you to provide some information. Examine the table below for the bundle ID associated with your app. 

| App Name | Bundle ID |
| --- | --- |
| <span translate="no">LoopCaregiver</span> | <span translate="no">com.TEAMID.loopkit.LoopCaregiver</span> |
| <span translate="no">LoopFollow</span> | <span translate="no">com.TEAMID.LoopFollow</span> |

> If you build from a second or third `repository` for `LoopFollow`, the Bundle ID will have `.Second` or `.Third` at the end.

1. Open this link: [App Store Connect / Apps](https://appstoreconnect.apple.com/apps){: target="_blank" } to view your apps; log in if needed. 

1. If this App already exists, you can continue to [Create Certificates](#create-certificates)
1. Click the Add Apps button or the blue "plus" icon and select New App as shown in the graphic below

    ![choose to add a new app](img/new-app-in-store.png){width="300"}
    {align="center"}

1. The New App dialog box opens and should appear similar to the graphic below. Before you fill anything out, make sure your Bundle ID is available in the dropdown menu. If you do not see the Bundle ID for your app; back out of this screen and follow the directions in [Configure to Use Browser: Find My Loop](prepare-app.md#find-my-loop), where you'll be finding App Name instead of Loop.
    * Select "iOS". For LoopFollow you can also select "macOS" if you own a Mac with macOS 11 or later.
    * Enter a name: this will have to be unique
        * You could start with "App Name ABC" where ABC are your initials
        * If that is already taken, you can add a number, for example, "App Name ABC 123"
        * This name is what you see on the App Store Connect list and in the *TestFlight* app
        * Once installed on your phone, you will see the actual app name
        * You can [Change the App Store Connect Name](../browser/phone-install.md#change-the-app-store-connect-name) later if you want
    * Select your primary language.
    * Choose the bundle ID for your app
    * SKU can be anything; for example "123" but must be unique across all your apps, so try 1234 or 12345 depending on how many apps you build with this method
    * Select "Full Access".

    ![create loop app in store connect - with missing bundle id](img/create-app-in-store.png){width="600"}
    {align="center"}

1. Click Create but do not fill out the next form. That is for submitting to the app store and you will not be doing that.

1. Edit your new app to [Remove Apple Vision Pro](prepare-app.md#remove-apple-vision-pro){: target="_blank" }

You are done with this activity. Before you close this browser window, note the *TestFlight* tab at the top of the page. You'll be using that tab after you complete the next two actions.

## Create Certificates

* The graphic below is an example from Loop. Your screen will show your app and associated repository.

Refer to the graphic below for the numbered steps:

1. Click on the "Actions" tab of your Repository repository
1. On the left side, click on "Create Certificates"
1. On the right side, click "Run Workflow" to show a dropdown menu
    * You will see your default branch (`main` for LoopFollow, `dev` for LoopCaregiver)
    * You can select a different branch, but typically, you run the default
1. Tap the green button that says "Run workflow".

    ![create certificates using github actions](img/action-03-create-certs.svg){width="700"}
    {align="center"}

1. Wait a minute or two for the action to finish
    * If this action fails, head over to [Action: Create Certificates Errors](bb-errors.md#action-create-certificates-errors)
    * Once you've resolved the error, repeat the Actions [Add Identifiers](identifiers.md#add-identifiers) and then Create Certificates. (The Add Identifiers might not be required but it is fast and should be done as a matter of routine.)

## Build App

The graphic below is an example from Loop, your screen will show your app and associated repository

If you are building the *LoopCaregiver* app, skip ahead to [Build Action](#build-action).

### Display Name Customization for `LoopFollow`

> If you build `LoopFollow` for one, two or three loopers, you may choose to customize your `fork` or `forks` to insert a custom display name.

> * Find and click on the file `LoopFollowDisplayNameConfig.xcconfig`
> * Tap the pencil icon so you can edit the file
> * The last line says `display_name = LoopFollow` (or `LoopFollow_Second` or `LoopFollow_Third`)
> * Insert your custom name so the last line says `display_name = LF custom name`
> * Click on commit changes and chose to commit directly into the `main` branch

> Continue to build as instructed below. After you install the app on your phone, iPad or Mac via *TestFlight*, that custom name is what is displayed. The prefix LF is suggested to make it easier to find the custom named `LoopFollow` app in the list of apps, but is not required.

### Build Action

Refer to the graphic below for the first four steps:

1. Click on the "Actions" tab of your Repository repository.
1. On the left side, click on "Build *App Name*".
1. On the right side, click "Run Workflow" to show a dropdown menu
    * You will see your default branch (`main` for LoopFollow, `dev` for LoopCaregiver)
    * You can select a different branch, but typically, you run the default
1. Tap the green button that says "Run workflow".

    ![build loop using github actions](img/action-04-build-loop.svg){width="700"}
    {align="center"}

1. Wait a few minutes to make sure there is not an early failure
    * If this action fails, head over to [Action: Build Loop Errors](bb-errors.md#action-build-loop-errors)
    * Once you've resolved the error, it's a good idea to repeat all three steps in this order:
        * [Add Identifiers](identifiers.md#add-identifiers)
        * Create Certificates
        * Build Loop
1. If the process appears to be happening without an error, go do something else for a while. The build should take about 20-30 minutes.
1. Your app should eventually appear on [App Store Connect](https://appstoreconnect.apple.com/apps){: target="_blank" }.

### Build Errors

Refer to the [Browser Build: Build Errors](bb-errors.md){: target="_blank" } to find your error.

Please do not remove an existing app if you have trouble building a new one. Your build error is not cause by any existing app.

!!! Important "Removing App Warning"
    If you remove an app and later want to restore that app, you might not be able to.

    For more information, see [Do Not Remove an App](bb-errors.md#do-not-remove-an-app){: target="_blank" }.


## Add Users to *TestFlight* for App

Once the first build completes, you will be able to configure *TestFlight* for the app - follow the template for setting up *TestFlight* for Loop found in [Configure to Use Browser: *TestFlight* Users Overview](../browser/tf-users.md#testflight-users-overview).

## Install on Phone

The [Install on Phone](phone-install.md) walks you through the steps to install the app to a phone. When going through those steps, replace your App Name for&nbsp;_<span translate="no">Loop</span>_. Everything else is the same.

## Use a *GitHub* Organization Account

This section is optional. It is provided to assist:

* Users who are using *GitHub* for other reasons and want to segregate their DIY app building from their existing accounts
* Mentors who want to do a lot of testing of many DIY apps to support people and get tired of entering the 6 <code>Secrets</code> repeatedly
* Users who are comfortable with the *GitHub* web interface who want the convenience of entering the 6 <code>Secrets</code> just one time instead of entering them for each <code>repository</code> individually

### Set up a Free *GitHub* Organization

Prerequisite: You need a personal *GitHub* account.

In the instructions below, use your *GitHub* username instead of `my-name`.

1. Follow the directions below to create a new *GitHub* organization account with a username of `my-name-org` (of course naming is up to you)
    * There is documentation at this link, [New *GitHub* Organization](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch){: target="_blank" }, or you can follow the bullets below
    * Log into `my-name` and click on your icon (at upper right) and choose Settings
    * On the left side-bar, click on Organizations
    * In the new view, click on New Organization and choose Free for the plan by clicking on  `Create a free organization`.
    * In the `Set up your organization` screen:
        * Enter `my-name-org` into the `Organization name` box
        * Enter the same email you use for `my-name` account
        * Select this organization belongs to `My personal account`
        * Check the box to accept the terms of service
        * Tap on the next button
2. You now see a Welcome screen
    * Unless you plan to collaborate with others, just tap `Complete setup`
    * You can always add others at a later time
3. Confirm access by entering the same password as you use for `my-name`

???+ tip "GH_PAT comes from personal `my-name` account"
    The *GitHub* personal access token used as one of the 6 <code>Secrets</code> is associated with your personal account (`my-name`); so if you already have one, you just keep using it.

### Use the Free *GitHub* Organization

There are three steps to using this account moving forward:

1. One-time only: You need to add your 6 <code>Secrets</code> to this organization account (instructions are in next section)

1. One-time only: Create a `Match-Secrets` repository in the `my-name-org` account
    * Not required for version 3.4 or later of the *Loop* app but it may be required for other apps if you haven't already built the *Loop* app
    * Start out at the top-level of your organization (`github.com/my-name-org`)
    * Click on `Repositories`
    * Click on `New repository`
    * Choose `my-name-org` as owner and enter `Match-Secrets` as the name
    * Make sure to choose `Private` and tap on the `Create` button
    * If you want to see graphics for the steps above, refer to the instructions written for a personal (instead of organization) account in [Create `Match-Secrets`](bb-errors.md#create-match-secrets)

1. For each repository: you need to `fork` for each app you wish to build to the new `my-name-org` account

    * When you do the fork, there will be a dropdown menu under Owner for you to select the account for the `fork`
    * Choose the organization account
    * Other than that extra step, follow the standard `fork` directions
        * This link provides instructions to [`Fork LoopWorkspace`](prepare-fork.md#fork-loopworkspace)
        * Refer to the [Table of App `Repositories`](#table-of-app-repositories) when building apps other than the *Loop* app

Then, for every build, you will use just the organization account. The original account is maintained to give you access to *GitHub* and holds your *GitHub* personal access token.

> WARNING - If you have `forks` of DIY apps in your original `my-name` account that are configured to build automatically, you want to disable that and have only the `my-name-org` account be configured for automatic building. Refer to [Disable Building for Personal *GitHub* account](#disable-building-for-personal-github-account).

### Add <code>Secrets</code> to your *GitHub* Organization

Adding the <code>Secrets</code> to an organization is similar to adding them to each <code>repository</code> for a personal *GitHub* account. The difference is you add them at the organization level and then they are available to each <code>repository</code> in that organization.

Follow the directions below to prepare to add secrets to the organization and then skip (when provided the link) to the per-repository directions for more details about adding each secret.

Make sure you are in the organization for *GitHub*:

* Click on your icon at upper right of *GitHub* browser
* Select `Your Organizations`
* In the new screen, select `my-name-org`
* Make sure the URL is `github.com/my-name-org`
* Click on Settings (it is optional to fill in the information shown under general)
* In the left pane, scroll down to find `Secrets and variables` and click on the dropdown symbol and choose `Actions`
* Your screen should look like the graphic below

![add secrets at organization level](img/add-secrets-org.png)

* At this point, tap on `New organization secret`
    * Refer the instructions at this link, [Enter the <code>Secrets</code>](prepare-fork.md#enter-the-secrets), for adding <code>Secrets</code>
    * Those instructions show the graphics for a personal `repository` and indicate the button will says `New repository secret` - your screen will show `New organization secret`
    * Continue until all six <code>Secrets</code> are entered for your organization account `my-name-org`
* Once the organization <code>Secrets</code> are entered, they are used by every repository you fork with this organization as the owner

The *GitHub* personal access token used as one of the 6 <code>Secrets</code> is associated with your personal account (`my-name`); so if you already have one, you just keep using it. If not, follow [these instructions](secrets.md#create-github-personal-access-token) to get or configure a new one.

### Disable Building for Personal *GitHub* account

Once you have your apps building as you expected from the `my-name-org` organization account, you should configure your personal account to stop any automatic building that may be taking place.

#### Option 1: Delete `repository`

You can delete the DIY repositories from your personal account

* Pro: You can't get confused about where you should be building
* Cons:
    * If you have already generated some customizations there, it is safest to not delete the repository
    * If you have pull requests open from your personal account, DO NOT DELETE that repository - that would automatically close those open PR
* Here are the instructions if you decide to delete the repositories
    * Click on your icon at upper right of *GitHub* browser
    * Select `Your Repositories`
    * Notice the github address now says `my-name` instead of `my-name-org`
    * Select the repository you wish to delete and follow these instructions
    * [GitHub Docs: Delete a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository){: target="_blank" }


#### Option 2: Disable Build Action

You can disable the build actions from the repositories in your personal account

* Pro: You leave any work you previously did alone in your personal account
* Con: You might get confused and try to build in your personal account instead of your organization account
* Here are the instructions to disable the build actions:
    * Click on your icon at upper right of *GitHub* browser
    * Select `Your Repositories`
    * Notice the github address now says `my-name` instead of `my-name-org`
    * Select the repository you wish to disable build actions for and follow these instructions
    * [GitHub Directions to Disable and Enable a Workflow](https://docs.github.com/en/actions/using-workflows/disabling-and-enabling-a-workflow#disabling-a-workflow){: target="_blank" }
    * It is the Build action that kicks off the update and build steps, so simply disabling the one action is sufficient
