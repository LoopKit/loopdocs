## Build Loop using GitHub Actions

This is only available with Loop 3 and Loop development branches.

!!! info "Time Estimate"
    - If you have never built Loop (allow up to one week elapsed time)
        * Requesting and getting an Apple Developer Account: 1-2 days
        * Creating and configuring your GitHub repositories (without Apple Information): 1-2 hours
        * Adding Secrets (requires Apple Developer Account): 1 hour
        * Performing the Action steps: 30 minutes to 2 hours
    - If you have previously built Loop with Xcode you have fewer steps and are probably familiar with some of the concepts
        * Expect 1 to 2 hours

!!! abstract "Summary"
    Once you have Apple Developer and GitHub accounts

    * Apple: Generate an API Key
    * GitHub:
        * Create an access token (GH_PAT)
        * Create a Match-Secrets private repository
        * Fork a repository (copy of LoopWorkspace)
        * Add Secrets to your repository
        * Action: Add Identifiers
    * Apple:
        * Configure Identifiers for Loop
        * Create your version of Loop in App Store (personal use only, not for distribution)
    * GitHub:
        * Action: Create Certificates
        * Action: Build Loop
    * Apple: Set up Internal TestFlight Group
    * Phone: Install Loop with TestFlight

!!! question "FAQs"
    - **Do I need a Mac computer?** No. This can be done on any browser, although it will be easier using a computer or tablet than just using a phone.
    - **Can I do this on my phone?** Yes, but the graphics shown on this page are from a computer browser.
    - **Isn't it hard to build every 90 days?** The initial setup (this page) and deploy (next page) takes a lot of your focused time. But once you build once, subsequent builds take very little of your time to start, then the rest is done automatically.
    - **Can I use this for my child?** You, as the adult, can install using TestFlight on your child's phone. The explict steps are provided.
    - **Can I still use my customizations?** This requires steps not yet documented. If you want customizations, stick with the Mac / Xcode build method for now.

**You must build Loop every 90 days when you use GitHub build method.**

* You will get an email from GitHub letting you know your GitHub Person Access Token is about to expire
* You can get a new token and start a new build within a few minutes - even on your phone: [GitHub Update](gh-update.md#github-update-summary)

!!! tip "Expect Updates"
    Plans are in progress to configure the GitHub action to automatically build every 60 days. Once this is in place, then you won't need to worry about building every 90 days. But these are just plans right now.

## Prerequisites

!!! tip "Read and Review"
    Building with GitHub using a browser requires you to do a series of steps in order with no mistakes. But once you've done it once, subsequent builds are trivial.

    At each point in the process

    * Check to make sure what you are doing matches the instructions
    * Check to make sure you did not skip a step
    * Notice - the actions show up alphabetically but they have to be done in A, C, B order
        * Add Identifiers (and do some more stuff), Create Certificates, Build Loop

    Different people approach this differently. Choose your method to achieve success:

    * Print the summary section above, go through the page sequentially doing each step and check off each step as you go
    * Read this whole page, then review it and read the [Most Common Mistakes](gh-errors.md#most-common-mistakes) section, then start doing each step
    * Figure out your method and use it


**Loop 3 requires iOS 15.1 or higher, no reason not to update to latest iOS**

### Build Loop

There are only two prerequisites to Build Loop with this method.

1. Paid Apple Developer account
1. Free GitHub account

### Install Loop

You will need TestFlight, from the Apple App Store, installed on your [Compatible Phone](../build/step2.md). You will install Loop on that phone using the TestFlight app.

### Use Loop

In order to use Loop, you need a [Compatible Pump](../build/step3.md) and [Compatible CGM](../build/step4.md). For pumps other than Omnipod DASH, you also need a [RileyLink Compatible Device](../build/step5.md).

For the initial steps, you'll be going back and forth between GitHub and Apple Developer webpages. It is best to open each in a separate window or tab for your browser.

## New Terms with GitHub Build

There are a number of terms that may seem unfamiliar with the GitHub Build. As you move through this page, there will be detailed instructions, but it helps to have the overview.

Some of these terms have ToolTips, so hover your mouse over the item - or review in the [Glossary](../faqs/glossary.md). Others need an expanded explanation. If reading this first is confusing, finish reviewing the whole page and then come back.

* Modules: You won't see this term but the concept is important when explaining the other terms
    * The Loop code uses modules to handle different components of the entire app
    * Some of these modules must be associated with your unique App Group
    * Others do not have this requirement
* Identifiers: The "Identifiers" are the names of the Modules that must be available to build Loop with GitHub
    * There are 4 Identifiers for LoopWorkspace that must be associated with your App Group
        * Loop, Loop Intent Extension, Loop Status Extension and Small Status Widget
    * There are 2 other Identifiers that do not require that association
        * WatchApp and WatchAppExtension
    * To further confuse users of the GitHub build method, the names you see depend on whether you previously build with Xcode and whether you previously built Loop 2.2.x or an early version of Loop 3 while it was still the dev branch
    * While the exact name might be different from those seen by people who have never built, it is ok - the build should still work
    * The directions with the Identifier names that do not start with XC are correct for people who have never built Loop with Xcode
* Secrets: a method to securely embed personal information into your fork of LoopWorkspace to enable GitHub to have access required to build Loop
    * There are 6 Secrets that must be added to your fork of LoopWorkspace
    * These Secrets work for any branch in your fork (main or dev, for example)
    * These same Secrets are added to your GitHub fork for [Other Apps](gh-other-apps.md) configured with the same GitHub build method
* [App Store Connect](https://appstoreconnect.apple.com): a website available for Apple Developers to review their apps
    * Once you purchase an Apple Developer annual account, you are an Apple Developer and have access to this site
    * Most Loopers will not have an App on their page until using the GitHub build method
    * The name of an app must be unique across the entire App Store worldwide
        * You will need a unique name for your Loop App

## Configure to use GitHub Build Actions

Review the entire process before starting and then go through slowly and carefully.

These instructions allow you to build Loop without having access to a Mac. They also allow you to easily install Loop on phones that are not connected to your computer.

* You can easily send Loop app updates to those you care for
* You can access and install Loop if you lose or damage your device
* You do not need to worry about correct Xcode/macOS versions

The setup steps are somewhat involved, but nearly all are one-time steps. Subsequent builds are trivial. The initial steps are best done on a computer where you can save and archive information for later use. Use a **text-only editor** for this archive file for your Secrets. People have gotten into difficulties when a lower-case character was "auto-corrected" to upper-case when pasting into their archive file.

TestFlight can be used to deploy Loop to a child's phone (under age 13 in the US) but requires a few extra steps on the phone itself. See [Install TestFlight Loop for Child](gh-deploy.md#install-testflight-loop-for-child).

Your app must be updated once every 90 days, at the current time, but it's simple to make a new build and can be done from anywhere, see [Update Loop using GitHub Actions](gh-update.md).

!!! tip "Expect Updates"
    Plans are in progress to configure the GitHub action to automatically build every 60 days. Once this is in place, then you won't need to worry about building every 90 days. But these are just plans right now.

    In the meantime, configure your GH_PAT to expire every 90 days. This acts as a reminder to rebuild. (You get an email from GitHub about a week ahead of time.)

    Keep checking back, or at least check when your 90-day GH_PAT expires. When the GitHub build process is updated, you can sync your fork, create a new GH_PAT that expires once a year, update it in secrets, create certs and build. But that is for the future.

### Save Your Information

!!! tip "Archive This Information"
    For many of the steps on this page, you will need to have access to usernames, email addresses, passwords, and in some cases, special parameters.

    * Record these in a safe place so you can find them when you need them
    * A digital copy is best because you will be copying and pasting in different locations

    **Be sure to use a Text-Only editor like NotePad (PC) or TextEdit (Mac) to archive your information.**

!!! info "A Note about Capitalization and Spaces"
    In places you will be told to give something a name like: FastLane API Key or FastLane Access Token. Please use these names.

    The Secrets that you will add later use names that are capitalized and use underscore instead of spaces. Be precise and careful.

     The relationship and creation of each item is explained step-by-step on this page.

!!! danger "Use a Text-Only Editor"
    If you use a "smart" editor, it may change lower-case letters to upper-case letters at the beginning of a line when you paste items into your archive file.

    If even one character is capitalized when it should not be, you will get [GitHub Errors](gh-errors.md).

The list below indicates what you need to record (save digitally so you can copy and paste). Notice that some information is created in one place and used in another. The items in all capital letters will be added to the Secrets for your LoopWorkspace fork, so they are listed twice in the list below.

**Needed or created at developer.apple.com**

* Email address (this is your username)
* password
* TEAMID
* FASTLANE_ISSUER_ID
* FASTLANE_KEY_ID
* FASTLANE_KEY

**Needed or created at github.com**

* Email address
* password
* username
* Your GitHub repository address will be: `https://github.com/username`
* Your LoopWorkspace repository address will be: `https://github.com/username/LoopWorkspace`
* GitHub Personal Access Token (GH_PAT)
* a password - make one up and save it (MATCH_PASSWORD)

**Needed when you [Configure Secrets](#configure-secrets)**

* Save names and values in a text-only editor
* These same secrets are used for Loop and for [Other Apps](gh-other-apps.md)
    * TEAMID
    * FASTLANE_ISSUER_ID
    * FASTLANE_KEY_ID
    * FASTLANE_KEY
    * GH_PAT
    * MATCH_PASSWORD

!!! tip "Note GH_PAT Expiration Date"
    In your text-only saved secrets file, indicate the day you configured the GH_PAT. Since you update this every 90 days, until further notice, adding a note like: generated on Jan 29, 2023 helps you know whether the GH_PAT stored in your file is current or needs to be updated.


## Apple Developer Account

If you have an Apple Developer Account, you should sign in to your account before starting. There will be links to take you to specific pages; if you are not already logged in, you will be required to log in before you can go to that page.

If you do not already have a paid Apple Developer account, you need to purchase one ($99 annual fee). It may take a few days for the account to be enabled.

* LoopDocs has an [Apple Developer Program](../build/step6.md) page that explains in detail how to sign up for an account
* This link takes you straight to [Apple Developer account](https://developer.apple.com) to sign up

### Generate API Key

You cannot generate the API Key until you have the paid Apple Developer account set up. If you are still waiting for Apple to enable your account, you can skip ahead to complete part of the GitHub steps but you will need to pause at [Configure Secrets](#configure-secrets).

This section will walk you through the steps required to gather or create these parameters.

|Name|Description|
|---------|---------|
|TEAMID|This 10-character identifier is associated with your Apple Developer ID and never changes|
|FASTLANE_ISSUER_ID|The issuer ID is associated with your Apple Developer ID and never changes|
|FASTLANE_KEY_ID|Key ID provided when you create an API key in App Store Connect; it is associated with the FASTLANE_KEY|
|FASTLANE_KEY|Copy the full key from the text file you downloaded when generating the API key - Filename has FASTLANE_KEY_ID value embedded in it.<br>Include everthing in the file from<br>-----BEGIN PRIVATE KEY-----<br>and ending in <br>-----END PRIVATE KEY-----<br> |

Each step has a link to take you to the specific page you need to do the next step. It is best if you open each link in a separate tab or window so you can refer back to these instructions as you move along.

1. Open this link: [Apple developer portal page](https://developer.apple.com/account/resources/certificates/list).
    * Look at the upper right hand corner of that page
    * The 10-character ID number below your name is your `TEAMID`
        * If all you see are icons, click on the Membership Details icon
    * Record this for use when you configure your Secrets and when you configure your unique App Group
    * Stop a moment and double check - if you get this wrong, you will have errors later
        * Do not "type" what you think you see; copy and paste from the Team ID from the webpage. (Avoid the wrong number of characters; avoid typing an 8 when it should be a B.)
1. Open this link: [App Store Connect/Access/API](https://appstoreconnect.apple.com/access/api)
    * Click the "Keys" tab
        * If this is your first time here, there will be a dialog for you to follow:

            "Permission is required to access the App Store Connect API. You can request access on behalf of your organization."

            * Click on `Request Access` and follow directions until access is granted

        * Once access is granted, click on the "Generate API Key" button

    * If you did not get routed through the "permission is required" screens click the blue &plus; sign
    * TO DO - update this graphic

    ![App Store Connect Key page](img/api-key-initial-screen.svg){width="700"}
    {align="center"}

    * A new "Generate API Key" dialog box will appear as shown in the graphic below

    ![generate api key dialog box](img/dev-generate-key.png){width="500"}
    {align="center"}


    * Enter the name of the key as "FastLane API Key" and choose "Admin" in the access drop down menu
    * Confirm the name and that Admin is selected and then click on the "Generate" button.

### Copy API Key Secrets

The Keys screen is seen again with the additional content similar to that shown in the graphic below; the key information is blanked out for security.

* Review the graphic and then follow directions below to save more parameters you will need to [Configure Secrets](#configure-secret)

    ![App Store Connect Key page](img/api-key-in-process.svg){width="700"}
    {align="center"}

1. A button labeled Copy is always adjacent to the Issuer ID above the word Active (this is the same for all keys that you generate with this Apple Developer ID)
    * Tap on the Copy button - this copies the Issuer ID into your paste buffer
    * In the file where you are saving information, paste this with the indication that it is for  `FASTLANE_ISSUER_ID`
1. Hover to the right of the Key ID and the Copy Key ID button shows up
    * Tap on the Copy Key ID button - this copies the Key ID into your paste buffer
    * In the file where you are saving information, paste this with the indication that it is for  `FASTLANE_KEY_ID`
1. Click on the Download API Key button - you will be warned you can only download this once.

    ![download key only once](img/dev-dl-key-once.png){width="700"}
    {align="center"}

6. Find your AuthKey download in your downloads folder. The name of the file will be "AuthKey_KeyID.p8" where KeyID matches your FASTLANE_KEY_ID

    * Double-click to open it and you will be presented a message asking how you'd like to open it (message shown is for a Mac - translate these directions to whatever computer you are using)
    * Click on "Choose Application..." and then select "TextEdit" (on a Mac, NotePad on a PC, or any text-only editor you prefer)

    ![img/apns-open.png](../nightscout/img/apns-open.png)

1. The contents of this file will be used for `FASTLANE_KEY`

    * Copy the full text, including the "-----BEGIN PRIVATE KEY-----" and "-----END PRIVATE KEY-----" lines
        * On a Mac, use CMD-A, then CMD-C to copy all the contents
        * On a PC, use CTL-A, then CTL-C to copy all the contents
    * In the file where you are saving information, paste this with the indication that it is for  `FASTLANE_KEY`

    ![img/apns-copy-key.png](../nightscout/img/apns-copy-key.png)

In summary, from this section, you have found or generated the following, and saved copies for later use

* `TEAMID`
* `FASTLANE_ISSUER_ID`
* `FASTLANE_KEY_ID`
* `FASTLANE_KEY`

!!! tip "Time for a Break?"
    This is a good place to pause if you need to. Just note where you are on the page so you can return later.

#### Lost FASTLANE_KEY

!!! danger "I can't find my FASTLANE_KEY"
    If you cannot find where you stored your information, you can get a new key. You cannot recover an old one. Return to [Generate API Key](#generate-api-key), but add this initial step.

    When you use the link in the Generate API Key step, you will see an Active key. You must first click Edit by the Active section, revoke your "FastLane API Key" and then follow the directions to generate a new one. You will have to update the Secrets for every App repository when you take this step.

    The FASTLANE_KEY_ID and FASTLANE_KEY must both be updated.

## New GitHub Account

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

Now you will configure a personal access token (GH_PAT), create one new repository and then fork the LoopWorkspace repository.

### Create GH_PAT

You must be logged into your GitHub account before starting this step. If you are continuing, you are already logged in.

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
* Be sure to check the box (red circle) to make the repository **private**
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
    * Leave the selection that says "Copy the main branch only" checked
    * Click on the green `Create fork` button

    ![fork information for LoopWorkspace](img/gh-fork-loopworkspace.svg){width="700"}
    {align="center"}

### Successful Fork

After creating the fork, your screen should be similar to the next graphic - it will say `main` for the branch instead of `dev` because this graphic was prepared before the release of Loop 3. You may or may not see the messages you are told to dismiss in the next two bullets. No worries if you don't see them.

* Near the top right, click on the X to dismiss the successfully fetched message
* In the middle, click on the Dismiss button to remove the "Your branch is not protected message"

![after creating the fork LoopWorkspace](img/gh-initial-fork-dismiss.png){width="500"}
{align="center"}

Carefully compare your screen to the graphic below paying attention to the highlighted sections.

* Note that your username is now showing
* The comment under your username indicates where the fork came from (that is a clickable link)
* The branch that is selected is `main`
* The message says "This branch is up to date with LoopKit/LoopWorkspace:main"

![after creating the fork LoopWorkspace](img/gh-after-fork.svg){width="700"}
{align="center"}

!!! tip "Time for a Break?"
    This is a good place to pause if you need to. Just note where you are on the page so you can return later.

### Configure Secrets

!!! tip "Secrets are Common"
    * There are 6 Secrets that must be added to your fork of LoopWorkspace
    * These Secrets work for any branch in your fork (main or dev, for example)
    * These same Secrets would be added to your fork of a repository for [Other Apps](gh-other-apps.md)

You need to be logged into GitHub.

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

        ![settings screen](img/gh-settings.svg){width="700"}
        {align="center"}

1. On the left side, find the `Secrets and variables` dropdown and choose Actions
    * After you select on Actions, your screen should look like the graphic below

        ![action secrets and variables screen](img/gh-actions-secrets.svg){width="700"}
        {align="center"}

1. Tap on the green button at the top right of your screen labeled "New repository secret" (refer to graphic above where the button is highlighted)
    * A new dialog screen appears as shown in the graphic below
    * Do not do anything yet - first read what you will do in the next section
        * In the Name* box where it says `YOUR_SECRET_NAME`, you will click in the box and paste one of the 6 secret names, as directed in [Enter Each Secret](#enter-each-secret)
        * In the Secret* box, you will click in the box and paste the value for that secret
        * Once you click on Add Secret, the secret will be added

![dialog for entering a new secret](img/new-secret-dialog.png){width="700"}
{align="center"}

#### Enter Each Secret

Refer to the list of parameters found in [Save Your Information](#save-your-information). This is the time you will enter these items.

Take a calming breath. This next part requires care.

* Once you enter and save a secret value, you will not be able to view what you just entered, so check carefully before you hit `Add Secret` to save it
    * You can replace the value for any secret later - you just can't see what you entered before
* If you make a mistake, the actions you take in the next sections will fail, but the error messages help you figure out which secrets you need to fix
* So collect the list of information you've gathered so it's handy and make up a password for the MATCH_PASSWORD and save that in your secrets archive file
* Confirm, one more time, that your TEAMID is correct
    * If it is not, all will appear fine until you try to Build Loop and then you will get failures

For each of the following secrets, follow the directions below - this list is configured with a copy button when you hover to the right of each word - this helps avoid spelling errors.
```
TEAMID
```
```
FASTLANE_ISSUER_ID
```
```
FASTLANE_KEY_ID
```
```
FASTLANE_KEY
```
```
GH_PAT
```
```
MATCH_PASSWORD
```

* For the FASTLANE_KEY value, copy the entire contents from<br>-----BEGIN PRIVATE KEY-----<br> through<br>-----END PRIVATE KEY-----<br>
* For MATCH_PASSWORD value - make up a password for this and save it for later use
    * The MATCH_PASSWORD must be the same for any repository using this method ([Other Apps](gh-other-apps.md))

Once all six secrets have been added to your LoopWorkspace, you are done with Settings. Your screen should look similar to the graphic below.

* Take a moment to be sure all of your secrets are spelled correctly
* If you notice a mistake, just delete the one that is not spelled correctly and add a `New respository secret` with the correct name

![all secrets entered](img/gh-done-adding-secrets.png){width="700"}
{align="center"}

!!! tip "Time for a Break?"
    This is a good place to pause if you need to. Just note where you are on the page so you can return later.

## Add Identifiers for Loop

!!! warning "Early Adopters"
    If you started using this method before Loop 3 was released, review [GitHub Early Adopters](gh-update.md#github-early-adopters).

Near the top middle of your LoopWorkspace fork, there is an Actions tab. If you have used Actions on this repository before, skip ahead to [Add Identifiers](#add-identifiers).

### First Use of Actions Tab

Click on the "Actions" tab of your LoopWorkspace repository.

* The first time you click on `Actions` with this repository you'll be informed that `Workflows aren't being run on this forked repository` as shown in the graphic below
* Tap on the green button that says: `I understand my workflows, go ahead and enable them`

    ![workflows disabled screen](img/gh-workflows-disabled.png){width="700"}
    {align="center"}

The workflows are now displayed: look at the list on the left side as shown in the graphic below. (You can dismiss the Actions Enabled message using the X near the upper right side if it appears).

![workflows displayed](img/gh-workflows-enabled.png){width="700"}
{align="center"}

### Add Identifiers

Refer to the graphic below for the numbered steps:

1. Click on the "Actions" tab of your LoopWorkspace repository
1. On the left side, click on "Add Identifiers"
1. On the right side, click "Run Workflow" to show a drop-down menu
    * You will see your default branch (should be `main`)
    * If you have additional branches, you can change the branch, for example, select `dev` for the development branch
1. Tap the green button that says "Run workflow".

    ![add identifiers using github actions](img/action-02-add-identifiers.svg){width="700"}
    {align="center"}

The Add Identifier Action should complete (succeed or fail) in a few minutes as shown in the graphic below.

* If you see the green check continue to the next section
* If you see the red X
    * [Examine the Error](gh-errors.md#examine-the-error) tells you how to download the file needed to diagnose your problem.
    * [Action: Add Identifiers Errors](gh-errors.md#action-add-identifiers-errors) lets you know what to search for in the downloaded file
    * Once you've resolved the error, repeat the Action: [Add Identifiers](#add-identifiers) step

![graphic showing a success and a failure for a GitHub Add Identifiers action](img/action-result.svg){width="700"}
{align="center"}

## Configure Identifiers for Loop

### Create App Group

The Loop App Group already exists if you previously built Loop using Xcode with this Apple Developer ID. If that is the case, skip ahead to [Find Loop Identifier](#find-loop-identifier).

If you have never built Loop with Xcode using your TEAMID, you need to create an App Group associated with your TEAMID.

1. Open this link: [Register an App Group](https://developer.apple.com/account/resources/identifiers/applicationGroup/add/) on the apple developer site.
1. For Description, use "Loop App Group".
1. For Identifier, enter "group.com.TEAMID.loopkit.LoopGroup", subsituting your team id for `TEAMID`.
1. Double check the spelling - your TEAMID must be correct and the Loop App Group must match the format shown in the previous step
    * A mistake here means you will not be able to build Loop until you fix it
1. Click "Continue" and then "Register".

### Find Loop Identifier

Open this link: [Certificates, Identifiers & Profiles: Identifiers List](https://developer.apple.com/account/resources/identifiers/list) on the apple developer site.

#### New Builders

If you never built using Xcode, then after successfully performing the Add Identifiers Action, you will see the six items listed under **NAME** in the table below with the associated **IDENTIFIER** information, where your developer ID replaces the TEAMID in the identifier.

#### Previous Xcode Builders

If you have built Loop using Xcode, then at least the Loop identifier will appear with the **NAME** `XC com.TEAMID.loopkit.Loop`. There may be other differences in the **NAME** column, but key off what you see under the **IDENTIFIER** column of the table. Only the six listed in the table below are of interest.

#### Table with Name and Identifier for Loop 3

| NAME | IDENTIFIER |
|-------|------------|
| Loop | com.TEAMID.loopkit.Loop |
| Loop Intent Extension | com.TEAMID.loopkit.Loop.Loop-Intent-Extension |
| Loop Status Extension | com.TEAMID.loopkit.Loop.statuswidget |
| Small Status Widget | com.TEAMID.loopkit.Loop.SmallStatusWidget |
| WatchApp | com.TEAMID.loopkit.Loop.LoopWatch |
| WatchAppExtension | com.TEAMID.loopkit.Loop.LoopWatch.watchkitextension |

!!! warning "Loop 2 to Loop 3 Builders"
    Several people who built earlier versions of Loop with Xcode and are using the GitHub method say they can't find the identifier names.

    If that is happening to you, follow the [Delete Identifiers](#delete-identifiers) instructions and then run Action: Add Identifiers again. You might not be able to delete the "Loop" identifier, so it will still begin with XC, but the others will appear with the short names shown above.

### Add or Review Configuration for Loop Identifier

Find and click on the Loop identifier row on the [Certificates, Identifiers & Profiles: Identifiers List](https://developer.apple.com/account/resources/identifiers/list) page.

The `Edit Your App ID Configuration` screen will open. You will be taking two actions for the Loop identifier.

1. Looking at the App Services column, scroll down to the App Groups row
    * Ensure the check box under Capabilities for App Groups is checked
    * (XC Loop) - If the word Edit shows up under NOTES, move on to step 2 below
    * If the word Configure shows up, tap on it
        * This opens the App Group Assignment screen
        * Check the box by Loop App Group that uses your TEAMID in group.com.TEAMID.loopkit.LoopGroup and then Continue
1. Continue scrolling down to the **Time Sensitive Notifications** row
    * Check, or confirm the box is checked, next to Time Sensitive Notifications as shown in the following graphic
    * This in only needed for the Loop identifier

    ![time sensitive notification](img/add-time-sensitive-to-loop.png){width="600"}
    {align="center"}

1. Now scroll slowly back up to the top of the page. As you go, confirm that each of these is configured with a check mark; if any are missing, click to enable.
    * Time Sensitive Notifications
    * SiriKit
    * Push Notifications
    * HealthKit
    * App Groups (enabled with group.com.TEAMID.loopkit.LoopGroup)

If you modified settings for the Loop identifier, the Save button at the top right will become active. Click on Save before leaving this page - otherwise the change does not take effect.

* Tap on Save
* This opens the Modify App Capabilities confirmation screen
* Click on Confirm

If you did not need to make changes, the Save button will not be active.

* Tap on the `< All Indentifiers` button at top left

The full list of Identifiers should be displayed again.

### Add App Group to Other Identifiers

You will now be checking the status for 3 more identifiers to ensure the App Group is configured to use the Loop App Group. You must add or confirm the App Group for these 3 identifiers:

| NAME | IDENTIFIER |
|-------|------------|
| Loop Intent Extension | com.TEAMID.loopkit.Loop.Loop-Intent-Extension |
| Loop Status Extension | com.TEAMID.loopkit.Loop.statuswidget |
| Small Status Widget | com.TEAMID.loopkit.Loop.SmallStatusWidget |

Find and click on a given identifier row on the [Certificates, Identifiers & Profiles: Identifiers List](https://developer.apple.com/account/resources/identifiers/list) page.

The `Edit Your App ID Configuration` screen will open. You will be taking one actions for each of these three identifiers.

Looking at the App Services column, scroll down to the App Groups row

* Ensure the check box under Capabilities for App Groups is checked
* If the word Edit shows up under NOTES, return to the identifiers list
* If the word Configure shows up, tap on it
    * This opens the App Group Assignment screen
    * Check the box by Loop App Group that uses your TEAMID in group.com.TEAMID.loopkit.LoopGroup and then Continue

If you had to modify a given identifier, the Save button at the top right will become active

* Tap on Save
* This opens the Modify App Capabilities confirmation screen
* Click on Confirm

If you did not need to make changes, the Save button will not be active.

* Tap on the `< All Indentifiers` button at top left

The full list of Identifiers should be displayed again.

## Create Loop App in App Store Connect

If you have created a Loop app in App Store Connect before, you can skip this section.

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

1. One last check - if the Bundle ID has a number other than your actual 10-digit TEAMID embedded in it, you will be creating an App in the App Store that you cannot use
    * In this case, do NOT select Create
    * Instead, go back and put the correct value into the TEAMID Secret and follow the steps in [Delete Identifiers](#delete-identifiers)
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

* Ensure this is the app you want by selecting on App Information, highlighted on the left side in the graphic below.
    * Examine its Bundle ID (not in view in this graphic) - confirm it is correct.
    * The format should be: `com.TEAMID.loopkit.Loop` with your TEAMID included
* Then scroll down to the bottom and choose `Restore App`.

    ![find removed apps](img/restore-removed-01.png){width="800"}
    {align="center"}

* Make sure User Access is set to Full Access and click on Restore.

    ![find removed apps](img/restore-removed-02.png){width="800"}
    {align="center"}

* You are done with this step and ready to Create Certificates

## Create Certificates

!!! warning "Early Adopters"
    If you started using this method before Loop 3 was released, review [GitHub Early Adopters](gh-update.md#github-early-adopters).

Refer to the graphic below for the numbered steps:

1. Click on the "Actions" tab of your LoopWorkspace repository
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

## Build Loop

Refer to the graphic below for the first four steps:

1. Click on the "Actions" tab of your LoopWorkspace repository.
1. On the left side, click on "Build Loop".
1. On the right side, click "Run Workflow" to show a drop-down menu
    * You will see your default branch (should be `main`)
    * If your default branch is not `main`, review [GitHub Early Adopters](gh-update.md#github-early-adopters)
    * If you have additional branches, you can change the branch, for example, select `dev` for the development branch
1. Tap the green button that says "Run workflow".

    ![build loop using github actions](img/action-04-build-loop.svg){width="700"}
    {align="center"}

1. Wait a few minutes to make sure there is not an early failure
    * If this action fails, head over to [Action: Build Loop Errors](gh-errors.md#action-build-loop-errors)
    * Once you've resolved the error, it's a good idea to repeat all three steps in this order:
        * [Add Identifiers](#add-identifiers)
        * Create Certificatess
        * Build Loop
1. If the process appears to be happening without an error, go do something else for a while. The build should take about 20-30 minutes.
1. Your app should eventually appear on [App Store Connect](https://appstoreconnect.apple.com/apps).

## Set Up Users and Access (TestFlight)

Once the first build completes, you will be able to configure TestFlight for the app.

You are configuring a private capability for your family using an Internal Testing group (max of 100). You need the Apple ID email address for each adult installing from your build. When building for a child, you will use your own Apple ID, not theirs. See [Install TestFlight Loop for Child](gh-deploy.md#install-testflight-loop-for-child).

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


## Extra Steps

Most people won't need the information on the rest of this page.

### Already Have LoopWorkspace

Some people may already have a fork of LoopWorkspace. They might even have one that they forked from somewhere other than LoopKit.

Suggestions - choose one of these methods:

* Update the repository if it is forked from LoopKit
    * Open your LoopWorkspace repository (`https://github.com/username/LoopWorkspace`) where you use your `username` in the URL
    * Review the graphic in the [Successful Fork](#successful-fork) section
        * Make sure all the items highlighted by red rectangles are correct with the possible exception of your fork being up to date
    * If you see a message that your fork is not up to date - tap on the Sync fork button and follow instructions
    * Continue with the [Create GH_PAT](#create-gh_pat) section
* Delete that repository if it is from somewhere other than LoopKit or the fork you wanted to start with (which might have customizations that you want)
    * Instructions to delete a repository are found at [GitHub Docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository)
    * You just need to make sure that a repository called LoopWorkspace is no longer in your GitHub account
    * Return to [Fork LoopWorkspace](#fork-loopworkspace) and follow all the instructions

### Delete Identifiers

When you have already built Loop with Xcode, the Identifier names will not match the directions and you might have trouble deciding which ones to configure.  Your existing Loop identifier will have a name that starts with XC as shown below, where your 10-digit TEAMID is used.

* Name: XC com TEAMID loopkit Loop
* Identifier: com.TEAMID.loopkit.Loop

The identifier that is associated with the Loop identifier cannot be deleted if it is already in the App Store but all others can. If you attempt to delete the XC Loop identifier, you may be told it cannot be deleted because it is in use in the app store. That's OK. Same for other identifiers (if you build a bunch of Apps). If a Bundle ID has ever been associated with an app in the App store, you cannot delete the Identifer.

To make it easy when configuring the identifiers, go through and delete as many as you can.

* Open this link: [Certificates, Identifiers & Profiles: Identifiers List](https://developer.apple.com/account/resources/identifiers/list) on the apple developer site.
* Use the graphic below as a guide to removing identifiers
* Keep repeating the steps until you've removed all the identifiers you can (or want to) delete
* It is OK to delete an identifier even if it does have your correct TEAMID
    * If you try to delete the Loop identifier with your TEAMID, it will refuse, don't worry, just keep going
* Note - this graphic indicates where on this page you can find your TEAMID
    * If you notice an identifier with a value embedded in it that does not have your TEAMID, then delete it if you can and [Update Secrets](gh-update.md#update-secrets) with your correct TEAMID
    * If you try to delete a Loop identifier that does not have your TEAMID, but you already added to the app store, it will refuse, don't worry, just keep going

![steps to delete a given identifier](img/delete-identifiers.svg){width="700"}
{align="center"}

If coming here from the GitHub Errors page because you enter the wrong TEAMID in Secrets - return to that page once you've deleted as many identifiers as you can: [Errors: Wrong TEAMID in Secrets](gh-errors.md#wrong-teamid-in-secrets).

If you were just trying to clean up the identifiers, then follow these steps:

* Run Action: [Add Identifiers](#add-identifiers) to add Identifiers with the documented short names
* If you did not complete [Find Loop Identifier](#find-loop-identifier) step, do it now
* Complete the [Add App Group to Other Identifiers](#add-app-group-to-other-identifiers)
* If you did not complete the [Create Loop App in App Store Connect](#create-loop-app-in-app-store-connect) step, do it now
* Continue with [Create Certificates](#create-certificates) and then [Build Loop](#build-loop_1)

