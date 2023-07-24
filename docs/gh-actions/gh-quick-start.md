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

### Save 6 Secrets

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

### [Collect the Two GitHub Secrets](../gh-actions/gh-first-time.md#create-github-personal-access-token)

Click on the link above if you need more detailed information, otherwise, follow the steps below.

### Create GitHub Personal Access Token

Log into your GitHub account to create a personal access token; this is one of two GitHub secrets needed for your build.

1. Create a [new personal access token](https://github.com/settings/tokens/new):
    * Enter a name for your token, use "FastLane Access Token".
    * Change the Expiration selection to `No expiration`.
    * Select the `repo` and `workflow` permission scopes.
    * Click "Generate token".
    * Copy the token and record it. It will be used below as `GH_PAT`.

### Make up a Password

This is the second one of two GitHub secrets needed for your build.

The first time you build with the GitHub Browser Build method for any DIY app, you will make up a password and record it as `MATCH_PASSWORD`. Note, if you later lose `MATCH_PASSWORD`, you will need to delete and make a new Match-Secrets repository (next step).

### [Setup GitHub Match-Secrets Repository](../gh-actions/gh-first-time.md#create-match-secrets)

Click on the link above if you need detailed instructions with graphics for creating your Match-Secrets Repository. Otherwise, follow the instructions below.

The creation of the Match-Secrets repository is a common step for all GitHub Browser Builds; do this step only once. You must be logged into your GitHub account.

1. Create a [new empty repository](https://github.com/new) titled `Match-Secrets`. It should be private.

Once created, you will not take any direct actions with this repository; it needs to be there for the GitHub to use as you progress through the steps.

### [Setup GitHub LoopWorkspace Repository](../gh-actions/gh-first-time.md#fork-loopworkspace)

Click on the link above if you need detailed instructions with graphics for creating your LoopWorkspace Repository. Otherwise, follow the instructions below.

1. Fork [https://github.com/LoopKit/LoopWorkspace](https://github.com/LoopKit/LoopWorkspace) into your account.
1. In the forked LoopWorkspace repo, go to Settings -> Secrets and variables -> Actions.
1. For each of the following secrets, tap on "New repository secret", then add the name of the secret, along with the value you recorded for it:
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

## Create App Group

If you have already built Loop via Xcode using this Apple ID, you can skip on to [Add App Group to Bundle Identifiers](#add-app-group-to-bundle-identifiers).

1. Go to [Register an App Group](https://developer.apple.com/account/resources/identifiers/applicationGroup/add/) on the apple developer site.
1. For Description, use "Loop App Group".
1. For Identifier, enter "group.com.TEAMID.loopkit.LoopGroup", subsituting your team id for `TEAMID`.
1. Click "Continue" and then "Register".

## Add App Group to Bundle Identifiers

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


## Create Loop App in App Store Connect

If you have created a Loop app in App Store Connect before, you can skip this section.

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

1. Go back to the "Actions" tab of your LoopWorkspace repository in GitHub.
1. On the left side, select "3. Create Certificates".
1. On the right side, click "Run Workflow", and tap the green `Run workflow` button.
1. Wait, and within a minute or two you should see a green checkmark indicating the workflow succeeded.

## Create a branch named "alive"

TestFlight builds expire after 90 days. This process you are implementing here will update and rebuild Loop periodically, and requires that you create a branch named "alive" so that GitHub will not inactivate the scheduled rebuild if no code updates are made.

The "alive" branch will only receive some additional commits to its history, and is not used for building the app.

1. Go to the "Code" tab of your LoopWorkspace repository.
1. Click the branch selection dropdown button, and then `View all branches`.
1. Click the green "New branch" button (upper right).
1. Type `alive` in the  "New branch name" field.
1. Select `LoopKit/LoopWorkspace` as "Source".
1. Select `dev` in the branch dropdown.
1. Click the green "Create new branch" button.

## Build Loop

1. Click on the "Actions" tab of your LoopWorkspace repository.
1. On the left side, select "4. Build Loop".
1. On the right side, click "Run Workflow", and tap the green `Run workflow` button.
1. You have some time now. Go enjoy a coffee. The build should take about 20-30 minutes.
1. Your app should eventually appear on [App Store Connect](https://appstoreconnect.apple.com/apps).
1. For each phone/person you would like to support Loop on:
    * Add them in [Users and Access](https://appstoreconnect.apple.com/access/users) on App Store Connect.
    * Add them to your TestFlight Internal Testing group.

## TestFlight and Deployment Details

Please refer to [LoopDocs: Set Up Users](https://loopkit.github.io/loopdocs/gh-actions/gh-first-time/#set-up-users-and-access-testflight) and [LoopDocs: Deploy](https://loopkit.github.io/loopdocs/gh-actions/gh-deploy/)

### [Apple Developer Account](../gh-actions/gh-first-time.md)

Click on the link above for detailed instructions or follow the sparse directions below.

If you do not already have a paid Apple Developer account, you need to purchase one ($99 annual fee). It may take a few days for the account to be enabled.

* LoopDocs has an [Apple Developer Program](../build/step6.md) page that explains in detail how to sign up for an account
* This link takes you straight to [Apple Developer account](https://developer.apple.com) to sign up

### Generate API Key

You cannot generate the API Key until you have the paid Apple Developer account set up. If you are still waiting for Apple to enable your account, you can skip ahead to complete part of the GitHub steps (see [New GitHub Account](#new-github-account) or [Setup GitHub](#setup-github)), but you will need to pause at [Configure Secrets](#configure-secrets).

This section will walk you through the steps required to gather or create these parameters.

|Name|Description|
|---------|---------|
|<code>TEAMID</code>|This 10-character identifier is associated with your Apple Developer ID and never changes|
|<code>FASTLANE_ISSUER_ID</code>|The issuer ID is associated with your Apple Developer ID and never changes|
|<code>FASTLANE_KEY_ID</code>|Key ID provided when you create an API key in App Store Connect; it is associated with the <code>FASTLANE_KEY</code>|
|<code>FASTLANE_KEY</code>|Copy the full key from the text file you downloaded when generating the API key - Filename has <code>FASTLANE_KEY_ID</code> value embedded in it.<br>Include everthing in the file from <br>`-----BEGIN PRIVATE KEY-----`<br>and ending in <br>`-----END PRIVATE KEY-----`<br> |

Each step has a link to take you to the specific page you need to do the next step. It is best if you open each link in a separate tab or window so you can refer back to these instructions as you move along.

1. Open this link: [Apple developer portal page](https://developer.apple.com/account/resources/certificates/list).
    * Look at the upper right hand corner of that page
    * The 10-character ID number below your name is your <code>TEAMID</code>
        * If all you see are icons, click on the [Membership Details](https://developer.apple.com/account#MembershipDetailsCard) icon
    * Record this for use when you configure your Secrets and when you configure your unique <span class="notranslate">App Group</span>
    * Stop a moment and double check - if you get this wrong, you will have errors later
        * Do not "type" what you think you see; copy and paste from the `Team ID` from the webpage. (Avoid the wrong number of characters; avoid typing an `8` when it should be a `B`.)
1. Open this link: [`App Store Connect/Access/API`](https://appstoreconnect.apple.com/access/api)
    * Click the `Keys` tab
        * If this is your first time here, there will be a dialog for you to follow:

            "`Permission is required to access the App Store Connect API. You can request access on behalf of your organization.`"

            * Click on `Request Access` and follow directions until access is granted

        * Once access is granted, click on the `Generate API Key` button

    * If you did not get routed through the `permission is required` screens click the blue &plus; sign

    ![App Store Connect Key page](img/api-key-initial-screen.svg){width="700"}
    {align="center"}

    * A new `Generate API Key` dialog box will appear as shown in the graphic below

    ![generate api key dialog box](img/dev-generate-key.png){width="500"}
    {align="center"}


    * Enter the name of the key as "`FastLane API Key`" and choose `Admin` in the access drop-down menu
    * Confirm the name and that "`Admin`" is selected and then click on the "`Generate`" button.

### Copy API Key Secrets

The `Keys` screen is seen again with the additional content similar to that shown in the graphic below; the key information is blanked out for security.

* Review the graphic and then follow the directions below to save more parameters you will need to [Configure Secrets](#configure-secrets)

    ![App Store Connect Key page](img/api-key-in-process.svg){width="700"}
    {align="center"}

1. A button labeled Copy is always adjacent to the `Issuer ID` above the word Active (this is the same for all keys that you generate with this Apple Developer ID)
    * Tap on the `Copy` button - this copies the `Issuer ID` into your paste buffer
    * In the file where you are saving information, paste this with the indication that it is for  `FASTLANE_ISSUER_ID`
1. Hover to the right of the `Key ID` and the `Copy Key ID` button shows up
    * Tap on the `Copy Key ID` button - this copies the `Key ID` into your paste buffer
    * In the file where you are saving information, paste this with the indication that it is for  `FASTLANE_KEY_ID`
1. Click on the `Download API Key` button - you will be warned you can only download this once.

    ![download key only once](img/dev-dl-key-once.png){width="700"}
    {align="center"}

6. Find your `AuthKey` download in your downloads folder. The name of the file will be "`AuthKey_KeyID.p8`" where `KeyID` matches your `FASTLANE_KEY_ID`

    * Double-click to open it and you will be presented a message asking how you'd like to open it (message shown is for a Mac - translate these directions to whatever computer you are using)
    * Click on "`Choose Application...`" and then select "`TextEdit`" (on a Mac, NotePad on a PC, or any text-only editor you prefer)

    ![img/apns-open.png](../nightscout/img/apns-open.png)

1. The contents of this file will be used for `FASTLANE_KEY`

    * Copy the full text, including the "`-----BEGIN PRIVATE KEY-----`" and "`-----END PRIVATE KEY-----`" lines
        * On a **Mac**, use ++command+"A"++, then ++command+"C"++  to copy all the contents
        * On a **PC**, use ++control+"A"++ , then ++control+"C"++ to copy all the contents
    * In the file where you are saving information, paste this with the indication that it is for  `FASTLANE_KEY`

    ![img/apns-copy-key.png](../nightscout/img/apns-copy-key.png)

### Do Not Confuse Your Keys

!!! danger "API Key vs APN Key"
    If you use [Remote Commands with Nightscout](../nightscout/remote-overrides.md), you may notice the Application Programming Interface (API) key has the same type of format as the Apple Push Notification (APN) key. The keys for both of these purposes are p8 keys, but they should not be confused with each other.

    The Secrets for building with GitHub use the API Key.

    The config vars for Nightscout use the APN Key.

    * If you are using remote commands with Nightscout and building with the GitHub build, you must also add the config var of `LOOP_PUSH_SERVER_ENVIRONMENT` with a value of `production` to your Nightscout site or the remote commands will not work.

### Done with Apple Secrets

In summary, from this section, you have found or generated the following, and saved copies for later use

* <code>TEAMID</code>
* <code>FASTLANE_ISSUER_ID</code>
* <code>FASTLANE_KEY_ID</code>
* <code>FASTLANE_KEY</code>

!!! tip "Time for a Break?"
    This is a good place to pause if you need to. Just note where you are on the page so you can return later.

#### Lost FASTLANE_KEY

!!! danger "I can't find my FASTLANE_KEY"
    If you cannot find where you stored your information, you can get a new key. You cannot recover an old one. Return to [Generate API Key](#generate-api-key), but add this initial step.

    When you use the link in the Generate API Key step, you will see an Active key. You must first click Edit by the Active section, revoke your "`FastLane API Key`" and then follow the directions to generate a new one. You will have to update the <code>Secrets</code> for every App repository when you take this step.

    The <code>FASTLANE_KEY_ID</code> and <code>FASTLANE_KEY</code> must both be updated.

## New GitHub Account

If you have a GitHub account, you can skip to [Setup GitHub](#setup-github). Make sure you know your GitHub associated email, username (`username`), and password.

If you do not already have a GitHub account, you need to create one. Be sure to record the email, password, and username for your GitHub account.

Decide on a couple of usernames that you will be happy with - this will get embedded into your GitHub URL. Your first choice might not be available, so be prepared with several candidates. Your personal URL will be: `https://github.com/username`.

* Click on this link to sign up for a free account: [github account signup](https://github.com/signup)
    * You will need to enter the **email** you want associated your GitHub account
    * You will be asked to enter a **password**
    * You will be asked to enter a **username**
    * You will be asked if you want to receive email, ok to say `N` for no - you still get important account information with that email
    * Solve the puzzle to prove you're a person
    * Check the associated **email** to get the code and enter the code into github.com to confirm your account
* You should get the Welcome to GitHub screen
    * Indicate it is "Just me" on your team and Continue
    * Don't check anything on the next screen, just tap `Continue`
    * Select the `Free` option by selecting `Continue for Free`

The free level comes with plenty of storage and compute time to build Loop.

## Setup GitHub

Now you will configure a personal access token (<code>GH_PAT</code>), create one new repository and then fork the `LoopWorkspace` repository.

### Create GH_PAT

You must be logged into your GitHub account before starting this step. If you are continuing, you are already logged in.

1. You will be creating a new GitHub `Personal Access Token` and giving it the name "`FastLane Access Token`"
1. Open this link: [https://github.com/settings/tokens/new](https://github.com/settings/tokens/new)
    * Referring to the graphic
        * Note that `Tokens (classic)` is highlighted
        * Most Looper will use the `classic Token`
            * If you are a developer who needs to use fine-grained `tokens`, that is fine
        * Edit the note box to be `FastLane Access Token`
    * The default Expiration time is 30 days - but you should select `No expiration` (use the drop down menu to select)
        * GitHub will show a yellow warning when you do this
        * It is ok to ignore the warning
    * Add a check beside the `workflow` permission scope
    * A check will automatically appear in the `repo` scope as well - this is normal
    * Scroll all the way to the bottom and click `Generate token` (it's a long way, ignore all other settings, do not check anything else)

    ![request a new personal access token](img/gh-access-token.svg){width="700"}
    {align="center"}

1. A new screen appears showing your access token
    * Copy the `token` and record it - once you leave this screen you can't see it again
    * You will use this for `GH_PAT` when you set up your Secrets
    * You can [Regenerate GitHub Token](gh-update.md#regenerate-github-token) for `GH_PAT` if you lose it, but best to keep it safe

    ![copy fastlane access token on github](img/gh-token-to-copy.png){width="600"}
    {align="center"}


### Create Match-Secrets

Open your github.com URL (this is `https://github.com/username`), where you replace `username` with the name you chose above.

Create a new private repository - you can either click on the link below or follow the instructions with the first graphic:

* Click on this link: [(https://github.com/new)](https://github.com/new)

or

* At the top right of the screen, click on the &plus; sign and select `New Repository`

    ![plus sign to add repository](img/create-match-secrets.svg){width="200"}
    {align="center"}

This shows you a screen similar to the following graphic which has 3 regions highlighted:

* In `Repository name`, type `Match-Secrets` (use a hyphen between `Match` and `Secrets`)
* Be sure to check the  box **`Private`**  (red circle) to make the repository **private**
* **Please confirm you selected `Match-Secrets` repository as private.**
* Scroll to the bottom of the page and tap on "`Create repository`"

![first screen for new repository](img/01-gh-create-match-secrets.png){width="600"}
{align="center"}

You will then be shown a screen with a lot of options - you will not do anything on this screen except leave it.

* Click on just your username (as indicated by the red rectangle) to return to your main GitHub URL.

![second screen for new repository](img/02-gh-match-secrets-leave-alone.png){width="600"}
{align="center"}

You will not be interacting with your `Match-Secrets` repository directly. It needs to exist for other actions to work correctly.

You are done with this part of the setup.

### Fork LoopWorkspace

!!! warning "Existing Fork"
    Some people may already have a fork of `LoopWorkspace`. Click on [Already Have LoopWorkspace](#already-have-loopworkspace), decide what to do, and follow the appropriate link back to these instructions.

1. Open this link [https://github.com/LoopKit/LoopWorkspace](https://github.com/LoopKit/LoopWorkspace) to open the `LoopWorkspace` repository owned by `LoopKit`.
1. Review the highlighted locations of the graphic below (yours won't look quite like this yet), but the `Fork` button is in the same place
1. At the upper right side of the screen, click on the word `Fork`
    * If you already have a fork, it will not allow you to proceed, see [Already Have LoopWorkspace](#already-have-loopworkspace)
1. Now your screen should look like the graphic below
    * Your username will be automatically filled in as the owner (`Owner`)
    * `LoopWorkspace` is automatically filled in as the repository name (`Repository Name`)
    * Leave the selection that says "`Copy the main branch only`" checked
    * Click on the green `Create fork` button

    ![fork information for LoopWorkspace](img/gh-fork-loopworkspace.svg){width="700"}
    {align="center"}

### Successful Fork

After creating the <span class="notranslate">fork</span>, your screen should be similar to the next graphic - it will say `main` for the branch instead of `dev` because this graphic was prepared before the release of Loop 3. You may or may not see the messages you are told to dismiss in the next two bullets. No worries if you don't see them.

* Near the top right, click on the close button :octicons-x-16: (`x`) to dismiss the `Successfully fetched` message
* In the middle, click on the `Dismiss` button to remove the "`Your branch is not protected`" message

![after creating the fork LoopWorkspace](img/gh-initial-fork-dismiss.png){width="500"}
{align="center"}

Carefully compare your screen to the graphic below paying attention to the highlighted sections.

* Note that your username is now showing
* The comment under your username indicates where the <span class="notranslate">fork</span> came from (that is a clickable link)
* The branch that is selected :octicons-git-branch-16: is `main`
* The message says "`This branch is up to date with LoopKit/LoopWorkspace:main`"

![after creating the fork LoopWorkspace](img/gh-after-fork.svg){width="700"}
{align="center"}

!!! tip "Time for a Break?"
    This is a good place to pause if you need to. Just note where you are on the page so you can return later.

### Configure Secrets

!!! tip "Secrets can be used for Other Apps"
    * There are 6 <span class="notranslate">Secrets</span> that must be added to your fork of `LoopWorkspace`
    * These <span class="notranslate">Secrets</span> work for any branch in your fork (`main` or `dev`, for example)
    * These same <span class="notranslate">Secrets</span> would be added to your <span class="notranslate">fork</span> of a repository for [Other Apps](gh-other-apps.md)

You need to be logged into GitHub.

1. Return to your forked copy of `LoopWorkspace`
    * Click on your personal icon at the upper right to see the drop-down menu and select "`Your repositories`"

    ![drop-down-menu](img/gh-quick-access.png){width="200"}
    {align="center"}

1. You should see (at least) 2 repositories: `Match-Secrets` and `LoopWorkspace`
1. Click on `LoopWorkspace` to open that repository
1. Click on the Settings Icon near the top right of your LoopWorkspace
    * If you don't see ⚙️ `Settings`, make your browser wider or scroll to the right
    * If you still don't see ⚙️ `Settings`, then you are **not** on your fork or you need to sign in to your GitHub account
    * After you click on ⚙️ `Settings`, your screen should look like the graphic below

        ![settings screen](img/gh-settings.svg){width="700"}
        {align="center"}

1. On the left side, find the `Secrets and variables` dropdown and choose <code>Actions</code>
    * After you select on <code>Actions</code>, your screen should look like the graphic below

        ![action secrets and variables screen](img/gh-actions-secrets.svg){width="700"}
        {align="center"}

1. Tap on the green button at the top right of your screen labeled `New repository secret` (refer to the graphic above where the button is highlighted)
    * A new dialog screen appears as shown in the graphic below
    * Do not do anything yet - first read what you will do in the next section
        * In the `Name *`  box where it says `YOUR_SECRET_NAME`, you will click in the box and paste one of the 6 secret names, as directed in [Enter Each Secret](#enter-each-secret)
        * In the `Secret *` box, you will click in the box and paste the value for that secret
        * Once you click on `Add Secret`, the secret will be added

![dialog for entering a new secret](img/new-secret-dialog.png){width="700"}
{align="center"}

#### Enter Each Secret

Refer to the list of parameters found in [Save Your Information](#save-your-information). This is the time you will enter these items.

:person_in_lotus_position: Take a calming breath. This next part requires care.

* Once you enter and save a secret value, you will not be able to view what you just entered, so check carefully before you hit `Add Secret` to save it
    * You can replace the value for any secret later - you just can't see what you entered before
* If you make a mistake, the actions you take in the next sections will fail, but the error messages help you figure out which secrets you need to fix
* So collect the list of information you've gathered so it's handy and make up a password for the `MATCH_PASSWORD` and save that in your secrets archive file
* Confirm, one more time, that your `TEAMID` is correct
    * If it is not, all will appear fine until you try to Build Loop and then you will get failures

For each of the following secrets, follow the directions below - this list is configured with a copy button when you hover to the right of each word - this helps avoid spelling errors.
``` { .text .copy }
TEAMID
```
``` { .text .copy }
FASTLANE_ISSUER_ID
```
``` { .text .copy }
FASTLANE_KEY_ID
```
``` { .text .copy }
FASTLANE_KEY
```
``` { .text .copy }
GH_PAT
```
``` { .text .copy }
MATCH_PASSWORD
```

* For the `FASTLANE_KEY` value, copy the entire contents from<br>`-----BEGIN PRIVATE KEY-----`<br> through<br>`-----END PRIVATE KEY-----`<br>
* For `MATCH_PASSWORD` value - make up a password for this and save it for later use
    * The `MATCH_PASSWORD` must be the same for any repository using this method ([Other Apps](gh-other-apps.md))

Once all six secrets have been added to your `LoopWorkspace`, you are done with Settings. Your screen should look similar to the graphic below.

* Take a moment to be sure all of your secrets are spelled correctly
* If you notice a mistake, just delete the one that is not spelled correctly and add a `New repository secret` with the correct name

![all secrets entered](img/gh-done-adding-secrets.png){width="700"}
{align="center"}

!!! tip "Time for a Break?"
    :fontawesome-regular-circle-pause: This is a good place to pause if you need to. Just note where you are on the page so you can return later.

## Validate Secrets

This step checks that the Secrets you added are correct. Some things cannot be validated at this point, but most can and a relatively clear error message is provided.

This will be updated soon, but for now - follow the instructions under "Add Identifiers for Loop", but do the first action: "1 Validate Secrets".

## Add Identifiers for Loop

Near the top middle of your `LoopWorkspace` <span class="notranslate">fork</span>, there is an <code>Actions</code> tab. If you have used <code>Actions</code> on this repository before, skip ahead to [Add Identifiers](#add-identifiers).

### First Use of Actions Tab

Click on the `Actions` tab of your `LoopWorkspace` repository.

* The first time you click on `Actions` with this repository you'll be informed that `Workflows aren't being run on this forked repository` as shown in the graphic below
* Tap on the green button that says: `I understand my workflows, go ahead and enable them`

    ![workflows disabled screen](img/gh-workflows-disabled.png){width="700"}
    {align="center"}

The `workflows` are now displayed: look at the list on the left side as shown in the graphic below. (You can dismiss the `Actions Enabled` message using the `X` near the upper right side if it appears).

![workflows displayed](img/gh-workflows-enabled.png){width="700"}
{align="center"}

### Add Identifiers

Refer to the graphic below for the numbered steps:

1. Click on the `Actions` tab of your `LoopWorkspace` repository
1. On the left side, click on 2. `Add Identifiers`
1. On the right side, click `Run Workflow` to show a drop-down menu
    * You will see your default branch (should be `main`)
    * If your default branch is not `main`, review [GitHub Early Adopters](gh-update.md#github-early-adopters)
1. Tap the green button that says `Run workflow`.

    ![add identifiers using github actions](img/action-02-add-identifiers.svg){width="700"}
    {align="center"}

The `Add Identifier` <span class=notranslate>Action</span> should complete (succeed or fail) in a few minutes as shown in the graphic below.

* If you see the green check (:octicons-check-circle-fill-16:{: .passed })  continue to the next section
* If you see the red `X` (:octicons-x-circle-fill-16:{: .failed }): 
    * [Examine the Error](gh-errors.md#examine-the-error) tells you how to download the file needed to diagnose your problem.
    * [Action: Add Identifiers Errors](gh-errors.md#action-add-identifiers-errors) lets you know what to search for in the downloaded file
    * Once you've resolved the error, repeat the Action: [Add Identifiers](#add-identifiers) step

![graphic showing a success and a failure for a GitHub Add Identifiers action](img/action-result.svg){width="700"}
{align="center"}

## Configure Identifiers for Loop

### Create App Group

The `Loop` *App Group* already exists if you previously built Loop using *Xcode* with this *Apple Developer ID*. If that is the case, skip ahead to [Find Loop Identifier](#find-loop-identifier).

If you have never built Loop with *Xcode* using your `TEAMID`, you need to create an *App Group* associated with your `TEAMID`.

1. Open this link: [`Register an App Group`](https://developer.apple.com/account/resources/identifiers/applicationGroup/add/) on the Apple developer site.
1. For **`Description`**, use `Loop App Group`.
1. For **`Identifier`**, enter `group.com.TEAMID.loopkit.LoopGroup`, substituting your team id for `TEAMID`.
1. Double-check the spelling - your `TEAMID` must be correct and the `Loop` *App Group* must match the format shown in the previous step
    * A mistake here means you will not be able to build Loop until you fix it
1. Click `Continue` and then `Register`.

### Find Loop Identifier

Open this link: [`Certificates, Identifiers & Profiles: Identifiers List`](https://developer.apple.com/account/resources/identifiers/list) on the Apple developer site.

#### New Builders

If you never built using *Xcode*, then after successfully performing the `Add Identifiers` *Action*, you will see the six items listed under **`NAME`** in the table below with the associated **`IDENTIFIER`** information, where your `Developer ID` replaces the `TEAMID` in the identifier.

#### Previous Xcode Builders

If you have built Loop using *Xcode*, then at least the Loop identifier will appear as `XC com.TEAMID.loopkit.Loop` under the **`NAME`** column. There may be other differences in the **`NAME`** column, but key off what you see under the **`IDENTIFIER`** column of the table. Only the six listed in the table below are of interest when building Loop.

#### Table with Name and Identifier for Loop 3

| `NAME` | `IDENTIFIER` |
|-------|------------|
| `Loop` | `com.TEAMID.loopkit.Loop` |
| `Loop Intent Extension` | `com.TEAMID.loopkit.Loop.Loop-Intent-Extension` |
| `Loop Status Extension` | `com.TEAMID.loopkit.Loop.statuswidget` |
| `Small Status Widget` | `com.TEAMID.loopkit.Loop.SmallStatusWidget` |
| `WatchApp` | `com.TEAMID.loopkit.Loop.LoopWatch` |
| `WatchAppExtension` | `com.TEAMID.loopkit.Loop.LoopWatch.watchkitextension` |

!!! warning "Loop 2 to Loop 3 Builders"
    Several people who built earlier versions of Loop with *Xcode* and are using the GitHub method say they can't find the *identifier names*. You can key off the **`IDENTIFIER`** instead of the **`NAME`** column in the table above.

    Or

    Follow the [`Delete Identifiers`](#delete-identifiers) instructions and then run Action: `Add Identifiers` again. You might not be able to delete the "Loop" identifier, so it will still begin with `XC`, but the others will appear with the short names shown above.

### Add or Review Configuration for Loop Identifier

Find and click on the row for the Loop identifier on the [Certificates, Identifiers & Profiles: Identifiers List](https://developer.apple.com/account/resources/identifiers/list) page. Look in the **`IDENTIFIER`** column to find `com.TEAMID.loopkit.Loop`. The name in the **`NAME`** column may be different than Loop. 

| `NAME` | `IDENTIFIER` |
|-------|------------|
| `Loop` | `com.TEAMID.loopkit.Loop` |

The `Edit Your App ID Configuration` screen will open. You will be taking two actions for the Loop identifier.

1. Looking at the `App Services` column, scroll down to the `App Groups` row
    * Ensure the check box (under the `Capabilities` column) for `App Groups` is checked
    * (`XC Loop`) - If the word `Edit` shows up under `NOTES`, move on to step 2 below
    * If the word `Configure` shows up, tap on it
        * This opens the `App Group Assignment` screen
        * Check the box by `Loop` *App Group* that uses your `TEAMID` in `group.com.TEAMID.loopkit.LoopGroup` and then `Continue`
1. Continue scrolling down to the **`Time Sensitive Notifications`** row
    * Check, or confirm the box is checked, next to `Time Sensitive Notifications` as shown in the following graphic
    * This is only needed for the `Loop` *identifier*

    ![time sensitive notification](img/add-time-sensitive-to-loop.png){width="600"}
    {align="center"}

1. Now scroll slowly back up to the top of the page. As you go, confirm that each of these is configured with a check mark; if any are missing, click to enable.
    * `Time Sensitive Notifications`
    * `Siri` (formerly known as `SiriKit`)
    * `Push Notifications`
    * `HealthKit`
    * `App Groups` (enabled with `group.com.TEAMID.loopkit.LoopGroup`)

If you modified settings for the `Loop` *identifier*, the `Save` button at the top right will become active. Click on `Save` before leaving this page - otherwise, the change does not take effect.

* Tap on `Save`
* This opens the `Modify App Capabilities` confirmation screen
* Click on `Confirm`

If you did not need to make changes, the `Save` button will not be active.

* Tap on the `< All Identifiers` button at the top left

The full list of Identifiers should be displayed again.

### Add App Group to Other Identifiers

You will now be checking the status for 3 more identifiers to ensure the App Group is configured to use the `Loop` *App Group*. You must add or confirm the *App Group* for these 3 identifiers:

| `NAME` | `IDENTIFIER` |
|-------|------------|
| `Loop Intent Extension` | `com.TEAMID.loopkit.Loop.Loop-Intent-Extension` |
| `Loop Status Extension` | `com.TEAMID.loopkit.Loop.statuswidget` |
| `Small Status Widget` | `com.TEAMID.loopkit.Loop.SmallStatusWidget` |

Find and click on a given identifier row on the [Certificates, Identifiers & Profiles: Identifiers List](https://developer.apple.com/account/resources/identifiers/list) page.

The `Edit Your App ID Configuration` screen will open. You will be taking one action for each of these three identifiers.

Looking at the `App Services` column, scroll down to the `App Groups` row

* Ensure the check box (under the `Capabilities column`) for `App Groups` is checked
* If the word `Edit` shows up under `NOTES`, return to the identifiers list
* If the word `Configure` shows up, tap on it
    * This opens the `App Group Assignment` screen
    * Check the box by `Loop App Group` that uses your `TEAMID` in `group.com.TEAMID.loopkit.LoopGroup` and then `Continue`

If you had to modify a given identifier, the `Save` button at the top right will become active

* Tap on `Save`
* This opens the `Modify App Capabilities confirmation` screen
* Click on `Confirm`

If you did not need to make changes, the `Save` button will not be active.

* Tap on the `< All Identifiers` button at the top left

The full list of Identifiers should be displayed again.

## Create Loop App in App Store Connect

If you have created a `Loop app` in *App Store Connect* before, you can skip this section.

If have previously used some kind of remote build, like `diawi` or `TestFlight`, you may have your Loop in the *App Store* but can't see it. Don't worry - there are instructions for this case.

1. Open this link: [`App Store Connect / Apps`](https://appstoreconnect.apple.com/apps) to view your apps; log in if needed.
    * If you have never added an app to *App Store Connect*, you will not see the icons inside the red rectangle and should keep going, although some people report the search icon shows up for them
    *  If you have an app that is not shown, you will see a search icon and the `All Statuses` dropdown. If you get to step 3 and cannot find your `com.TEAMID.loopkit.Loop` in the *Bundle ID* drop-down, this means you need to follow [Find My Loop](#find-my-loop).

    ![app store connect with deleted apps](img/01-app-store-connect.png){width="600"}
    {align="center"}

1. Click the `Add Apps` button or the blue "plus" icon (:material-plus-circle:{: .appstoreconnect } ) and select `New App` as shown in the graphic below

    ![choose to add a new app](img/new-app-in-store.png){width="300"}
    {align="center"}

1. The `New App` dialog box opens and should appear similar to the graphic below. Before you fill anything out, make sure your `Bundle ID` is available in the dropdown menu (it shows as `Choose` in the graphic below). If you do not see `com.TEAMID.loopkit.Loop`, with **`TEAMID`** matching your `TEAMID` in the dropdown menu; back out of this screen and follow the directions in [Find My Loop](#find-my-loop) instead.
    * Select `iOS`.
    * Enter a name: this will have to be unique
        * You could start with `Loop_ABC` where `ABC` are your initials
        * If that is already taken, you can add a number, for example, `Loop_ABC_123`
        * This name is what you see on the *App Store Connect* list and in the *TestFlight* app
        * Once installed on your phone, you will see Loop with the standard Loop Logo
        * You can [Change the App Store Connect Name](../gh-actions/gh-deploy.md#change-the-app-store-connect-name) later if you want
    * Select your primary language.
    * Choose the **`Bundle ID`** that matches `com.TEAMID.loopkit.Loop`
    * **`SKU`** can be anything; for example `123`.
    * Select "`Full Access`".

    ![create loop app in store connect - with missing bundle id](img/create-app-in-store.png){width="600"}
    {align="center"}

1. One last check - if the `Bundle ID` has a number other than your actual 10-digit `TEAMID` embedded in it, you will be creating an App in the App Store that you cannot use
    * In this case, do **NOT** select `Create`
    * Instead, go back and put the correct value into the `TEAMID`  *Secret*  and follow the steps in [Delete Identifiers](#delete-identifiers)
1. Click `Create` but do not fill out the next form. That is for submitting to the app store and you will not be doing that.

You are done with this activity and can close the browser tab. It's time to head back to your GitHub account and [Create Certificates](#create-certificates)

### Find My Loop

This section is for people who were not able to follow the instructions in the last section because `com.TEAMID.loopkit.Loop`, with **`TEAMID`** matching your `TEAMID`, was not in the dropdown menu for `Bundle ID`.

There are two possible reasons:

1. You did not complete [Add App Group to Other Identifiers](#add-app-group-to-other-identifiers) or one of the predecessor steps; review those steps
1. Your app is already in *App Store Connect*, but you cannot see it

You may have no memory of ever setting up `Loop` in *App Store Connect*. If you previously used some kind of remote build, like `diawi`, your `Loop` may be there as a *Removed App*.

* Open this link: [App Store Connect / Apps](https://appstoreconnect.apple.com/apps), look for `All Statuses` dropdown indicator and select `Removed Apps`

    ![app store connect with deleted apps](img/01-app-store-connect.png){width="600"}
    {align="center"}

* Click on the App name:

    ![find removed apps](img/find-removed-app.png){width="600"}
    {align="center"}

* Ensure this is the app you want by selecting `App Information`, highlighted on the left side in the graphic below.
    * Examine its `Bundle ID` (not in view in this graphic) - confirm it is correct.
    * The format should be: `com.TEAMID.loopkit.Loop` with your *TEAMID* included
* Then scroll down to the bottom and choose `Restore App`.

    ![find removed apps](img/restore-removed-01.png){width="800"}
    {align="center"}

* Make sure **`User Access`** is set to `Full Access` and click on `Restore`.

    ![find removed apps](img/restore-removed-02.png){width="800"}
    {align="center"}

* You are done with this step and ready to Create Certificates

## Create Certificates

Refer to the graphic below for the numbered steps:

1. Click on the "<code>Actions</code>" tab of your `LoopWorkspace` repository
1. On the left side, click on "`Create Certificates`"
1. On the right side, click "`Run Workflow`" to show a drop-down menu
    * You will see your default branch (should be `main`)
    * If your default branch is not `main`, review [GitHub Early Adopters](gh-update.md#github-early-adopters)
1. Tap the green button that says "`Run workflow`".

    ![create certificates using github actions](img/action-03-create-certs.svg){width="700"}
    {align="center"}

1. Wait a minute or two for the action to finish
    * If this action fails, head over to [Action: 3. Create Certificates Errors](gh-errors.md#action-create-certificates-errors)
    * Once you've resolved the error, repeat the Actions [Add Identifiers](#add-identifiers) and then `Create Certificates`. (The `Add Identifiers` might not be required but it is fast and should be done as a matter of routine.)

## Build Loop

Refer to the graphic below for the first four steps:

1. Click on the "`Actions`" tab of your `LoopWorkspace` repository.
1. On the left side, click on "4. `Build Loop`".
1. On the right side, click "`Run Workflow`" to show a drop-down menu
    * You will see your default branch (should be `main`)
    * If your default branch is not `main`, review [GitHub Early Adopters](gh-update.md#github-early-adopters)
1. Tap the green button that says "`Run workflow`".

    ![build loop using github actions](img/action-04-build-loop.svg){width="700"}
    {align="center"}

1. Wait a few minutes to make sure there is not an early failure
    * If this action fails, head over to [Action: Build Loop Errors](gh-errors.md#action-build-loop-errors)
    * Once you've resolved the error, it's a good idea to repeat all three steps in this order:
        * [Add Identifiers](#add-identifiers)
        * [Create Certificates](#create-certificates)
        * Build Loop
1. If the process appears to be happening without an error, go do something else for a while. The build should take about 20-30 minutes.
1. Your app should eventually appear on [`App Store Connect`](https://appstoreconnect.apple.com/apps).

## Set Up Users and Access (TestFlight)

Once the first build completes, you will be able to configure *TestFlight* for the app.

You are configuring a private capability for your family using an Internal Testing group (max of 100). You need the *Apple ID* email address for each adult installing from your build. When building for a child, you will use your own *Apple ID*, not theirs. See [Install TestFlight Loop for Child](gh-deploy.md#install-testflight-loop-for-child).

1. First you need to add the email address(es) to your *App Store Connect* Access Users list:

    * Open this link: [Users and Access](https://appstoreconnect.apple.com/access/users)
        * You must provide a role for each person - `Customer Support` is a good choice
        * Once you have added them here, you'll be able to select them in the `TestFlight` group for your app

    ![add email and role for your users](img/add-users.png){width="700"}
    {align="center"}

1. Open this link: [App Store Connect / Apps](https://appstoreconnect.apple.com/apps) to view your apps; log in if needed. Then select your Loop app. Click on `TestFlight` tab and the `Internal Testing` to add a group.

    ![open TestFlight tab for your app](img/setup-testflight-01.png){width="700"}
    {align="center"}

1. Fill out the name you want for the `Internal Testing` group
    * Be sure to check the box `Enable automatic distribution`
    * Click `Create` when done (this can always be modified later)

    ![add email and role for your users](img/setup-testflight-02.png){width="700"}
    {align="center"}

1. As soon as you create the group, you'll be asked who should be included
    * Click in the box beside each person you want to include
    * Each person in this group will get an email each time you update (build again) on GitHub
    * Click `Add` when you are done
    * If building for a child, you will send the invitation to yourself because you will install for your child: See [Install Loop for Child](gh-deploy.md#install-testflight-loop-for-child)

    ![select your users for the testing group](img/setup-testflight-03.png){width="700"}
    {align="center"}

## Deployment

The [GitHub Deployment](gh-deploy.md) walks you through the steps to deploy to a phone.


## Extra Steps

Most people won't need the information on the rest of this page.

### Already Have LoopWorkspace

Some people may already have a fork of `LoopWorkspace`. They might even have one that they forked from somewhere other than `LoopKit`.

Suggestions - choose one of these methods:

* Update the repository if it is forked from `LoopKit`
    * Open your `LoopWorkspace` repository (`https://github.com/username/LoopWorkspace`) where you use your GitHub `username` in the URL
    * Review the graphic in the [Successful Fork](#successful-fork) section
        * Make sure all the items highlighted by red rectangles are correct with the possible exception of your fork being up to date
    * If you see a message that your *fork* is not up to date - tap on the `Sync fork` button and follow the instructions
    * Continue with the [Create GH_PAT](#create-gh_pat) section
* Delete that repository if it is from somewhere other than `LoopKit` or the fork you wanted to start with (which might have customizations that you want)
    * Instructions to delete a repository are found at [GitHub Docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository)
    * You just need to make sure that a repository called `LoopWorkspace` is no longer in your GitHub account
    * Return to [Fork LoopWorkspace](#fork-loopworkspace) and follow all the instructions

### Delete Identifiers

When you have already built Loop with *Xcode*, the Identifier names will not match the directions and you might have trouble deciding which ones to configure.  Your existing `Loop` identifier will have a name that starts with `XC` as shown below, where your 10-digit `TEAMID` is used.

* `Name: XC com TEAMID loopkit Loop`
* `Identifier: com.TEAMID.loopkit.Loop`

The `Identifier` that is associated with the `Loop` identifier cannot be deleted if it is already in the *App Store* but all others can. If you attempt to delete the `XC` *Loop* identifier, you may be told it cannot be deleted because it is in use in the app store. That's OK. Same for other identifiers (if you build a bunch of Apps). If a `Bundle ID` has ever been associated with an app in the *App Store*, you cannot delete the `Identifier`.

To make it easy when configuring the identifiers, go through and delete as many as you can.

* Open this link: [Certificates, Identifiers & Profiles: Identifiers List](https://developer.apple.com/account/resources/identifiers/list) on the Apple developer site.
* Use the graphic below as a guide to removing identifiers
* Keep repeating the steps until you've removed all the identifiers you can (or want to) delete
* It is OK to delete an identifier even if it does have your correct `TEAMID`
    * If you try to delete the `Loop` identifier with your `TEAMID`, it will refuse, don't worry, just keep going
* Note - this graphic indicates where on this page you can find your `TEAMID`
    * If you notice an identifier with a value embedded in it that does not have your `TEAMID`, then delete it if you can and [Update Secrets](gh-update.md#update-secrets) with your correct `TEAMID`
    * If you try to delete a Loop identifier that does not have your `TEAMID`, but you already added to the *App Store*, it will refuse, don't worry, just keep going

![steps to delete a given identifier](img/delete-identifiers.svg){width="700"}
{align="center"}

If coming here from the GitHub Errors page because you enter the wrong `TEAMID` in `Secrets` - return to that page once you've deleted as many identifiers as you can: [Errors: Wrong TEAMID in Secrets](gh-errors.md#wrong-teamid-in-secrets).

If you were just trying to clean up the identifiers, then follow these steps:

* Run Action: [Add Identifiers](#add-identifiers) to add Identifiers with the documented short names
* If you did not complete [Find Loop Identifier](#find-loop-identifier) step, do it now
* Complete the [Add App Group to Other Identifiers](#add-app-group-to-other-identifiers)
* If you did not complete the [Create Loop App in App Store Connect](#create-loop-app-in-app-store-connect) step, do it now
* Continue with [Create Certificates](#create-certificates) and then [Build Loop](#build-loop_1)

