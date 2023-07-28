??? info "Time Estimate"
    - If you have never built Loop (allow up to one week elapsed time)
        * Requesting and getting an Apple Developer Account: 1-2 days
        * Creating and configuring your GitHub repositories (without Apple Information): 1-2 hours
        * Adding <code>Secrets</code> (requires Apple Developer Account): 1 hour
        * Performing the Action steps: 30 minutes to 2 hours
    - If you have previously built Loop with Xcode you have fewer steps and are probably familiar with some of the concepts
        * Expect 1 to 2 hours

??? abstract "Summary"
    Once you have Apple Developer and GitHub accounts:

    * Apple: 
        * Generate and save four <code>Secrets</code>
    * GitHub:
        * Generate and save two <code>Secrets</code>
        * Create a <code>Match-Secrets</code> private repository
        * Fork a repository (copy of LoopWorkspace)
        * Add <code>Secrets</code> to your repository
        * `Action: 1. Verify Secrets`
        * `Action: 2. Add Identifiers`
    * Apple:
        * Configure Identifiers for Loop
        * Create your version of Loop in App Store (personal use only, not for distribution)
    * GitHub:
        * `Action: 3. Create Certificates`
        * `Action: 4. Build Loop`
    * Apple: Set up Internal TestFlight Group
    * Phone: Install Loop with TestFlight

??? question "FAQs"
    - **Do I need a Mac computer?** No. This can be done on any browser, although it will be easier using a computer or tablet than just using a phone.
    - **Can I do this on my phone?** Yes, but the graphics shown on this page are from a computer browser.
    - **Isn't it hard to build every 90 days?** The initial setup and deployment take a lot of your focused time. But once you build once, subsequent builds take very little of your time to start, then the rest is done automatically.
    - **Can I use this for my child?** You, as the adult, can install using TestFlight on your child's phone. The explicit steps are provided at [GitHub Deploy: Install TestFlight Loop for Child](gh-deploy.md#install-testflight-loop-for-child).
    - **Can I still use my customizations?** Yes. [Customize with GitHub](gh-customize.md)


## Build Loop using GitHub Actions

* **This Try-Stuff page is for playing with ideas and letting folks on Slack throw darts**

The instructions for building Loop with a Browser using GitHub Actions can appear overwhelming when every step is fully detailed including graphics.

There is an automatic table of contents (TOC) for this page (look on the right side of your browser). If your browser doesn't show that, tap on the hamburger menu (upper left) and then this page name to see the TOC for the page.

## How to Use This Page

There are highlight boxes found at appropriate points below. If desired, click the arrow to the right for the summary of steps that are detailed in that section. If the summary is sufficient for you to complete the task, the last item in the summary "box" is a link to move you to the next section on this page.

## Prerequisites

??? tip "Prerequisites"
    The prerequisites are:

    * A [GitHub account](https://github.com/signup)
        * The free level comes with plenty of storage and free compute time to build loop, multiple times a day
    * A paid [Apple Developer account](https://developer.apple.com)
        * The cost is $99 per year

    Skip ahead to [New Terms with GitHub Build](#new-terms-with-github-build)

### Build Loop

There are only two prerequisites to build Loop with this method.

1. Paid Apple Developer account
1. Free GitHub account

### Install Loop

You will need TestFlight, from the Apple App Store, installed on your [Compatible Phone](../build/step2.md). You will install Loop on that phone using the TestFlight app.

### Use Loop

In order to use Loop, you need a [Compatible Pump](../build/step3.md) and [Compatible CGM](../build/step4.md). For pumps other than Omnipod DASH, you also need a [RileyLink Compatible Device](../build/step5.md).

For the initial steps, you'll be going back and forth between GitHub and Apple Developer webpages. It is best to open each in a separate window or tab for your browser.

## New Terms with GitHub Build

??? tip "New Terms with GitHub Build"
    There are a lot of new terms - you can read details about what they are (before you start), or just skip ahead to [Save Your Information](#save-your-information)

There are a number of terms that may seem unfamiliar with the GitHub Build. As you move through this page, there will be detailed instructions, but it helps to have the overview.

Some of these terms have ToolTips, so hover your mouse over the item - or review in the [Glossary](../faqs/glossary.md).

* You may find some terms in the Glossary not in alphabetical order. All the <code>Secrets</code> discussed on this page, are listed under <code>Secrets</code> in the Glossary.

Others terms need an expanded explanation. If reading about the new terms first is confusing, finish reviewing the whole page and then come back.

* `Modules`: You won't see this term but the concept is important when explaining the other terms
    * The Loop code uses modules to handle different components of the entire app
    * Some of these modules must be associated with your unique App Group
    * Others do not have this requirement
* `Identifiers`: The Identifiers refer to the Modules that must be available to build Loop with GitHub
    * There are 4 Identifier Names for LoopWorkspace that must be associated with your App Group
        * `Loop`, `Loop Intent Extension`, `Loop Status Extension` and `Small Status Widget`
    * There are 2 other Identifier Names that must exist but do not require that association
        * `WatchApp` and `WatchAppExtension`
    * On the `Identifier` screen, there will be **`NAME`** and **`IDENTIFIER`** columns
        * The items you see under the **`NAME`** column depend on whether you previously built with Xcode and may start with `XC`
        * The items under the **`IDENTIFIER`** column match the table in the documentation
* <code>Secrets</code>: a method to securely embed personal information into your fork of LoopWorkspace to enable GitHub to have the access required to build Loop
    * There are 6 <code>Secrets</code> that must be added to your fork of LoopWorkspace
    * These <code>Secrets</code> work for any branch in your fork (`main` or `dev`, for example)
    * These same <code>Secrets</code> are added to your GitHub fork for [Other Apps](gh-other-apps.md) configured with the same GitHub build method
* [`App Store Connect`](https://appstoreconnect.apple.com): a website available for Apple Developers to review their apps
    * Once you purchase an *Apple Developer* annual account, you are an Apple Developer and have access to this site
    * Most Loopers will not have an App on their page until using the GitHub build method
    * The name of an app must be unique across the entire App Store worldwide
        * You will need a unique name for your Loop App
* API `Key`: Application Programming Interface Key
    * This key will be obtained by you from the Apple Developer website to enable your GitHub account to interface with Apple to create your app
* `Actions`: a custom application for the GitHub Actions platform that performs a complex but frequently repeated task
    * With Loop 3, actions to `Verify Secrets`, `Add Identifiers`, `Create Certificates`, and `Build Loop` are provided to enable users to build the Loop app from a browser on any computer
    * The GitHub system is maintained by Microsoft Corporation and they do a good job of keeping it running - however, if there is a problem, it will be reported on [GitHub Status](https://www.githubstatus.com/).

## Save Your Information

There is no highlight box here - everyone needs to read this section!

!!! tip "Archive This Information"
    For many of the steps on this page, you will need to have access to usernames, email addresses, passwords, and in some cases, special parameters.

    * Record these in a safe place so you can find them when you need them
    * A digital copy is best because you will be copying and pasting in different locations

    **Be sure to use a Text-Only editor like NotePad (PC) or TextEdit (Mac) to archive your information.**

!!! info "A Note about Capitalization and Spaces"
    In places, you will be told to give something a name like FastLane API Key or FastLane Access Token. Please copy from the docs to use those exact names.

    The <code>Secrets</code> that you will add later use names that are capitalized and use underscore ++"_"++ instead of spaces. Be precise and careful.

     The relationship and creation of each item is explained step-by-step on this page.

!!! danger "Use a Text-Only Editor"
    If you use a "smart" editor, it may change lower-case letters to upper-case letters at the beginning of a line when you paste items into your archive file.

    If even one character is capitalized when it should not be, you will get [GitHub Errors](gh-errors.md).

    If you use a smart editor to store your FASTLANE_KEY, you are likely to get the mysterious `invalid curve name` error.

## Save Six Secrets

??? info "Save Six Secrets"
    You require 6 <code>Secrets</code> (alphanumeric items) to use the GitHub build method and if you use the GitHub method to build more than Loop, e.g., Loop Follow or LoopCaregiver, you will use the same 6 <code>Secrets</code> for each app you build with this method. Each secret is indentified below by `ALL_CAPITAL_LETTER_NAMES`.

    * Four <code>Secrets</code> are from your Apple Account
    * Two <code>Secrets</code> are from your GitHub account
    * Be sure to save the 6 <code>Secrets</code> in a text file using a text editor
        - Do **NOT** use a smart editor, which might auto-correct and change case, because these <code>Secrets</code> are case sensitive
    
    If you already have usernames and passwords saved, you can skip ahead to [Collect the Four `Apple Secrets`](#collect-the-four-apple-secrets)

The list below indicates what you need to record (save digitally so you can copy and paste). Notice that some information is created in one place and used in another. The items in all capital letters will be added to the <code>Secrets</code> for your LoopWorkspace fork, so they are listed twice in the list below.

**Needed or created at developer.apple.com**

* Email address (this is your username)
* password
* <code>TEAMID</code>
* <code>FASTLANE_ISSUER_ID</code>
* <code>FASTLANE_KEY_ID</code>
* <code>FASTLANE_KEY</code>

**Needed or created at github.com**

* Email address
* password
* username
* Your GitHub repository address will be: `https://github.com/username`
* Your LoopWorkspace repository address will be: `https://github.com/username/LoopWorkspace`
* GitHub Personal Access Token (GH_PAT)
* a password - make one up and save it (<code>MATCH_PASSWORD</code>)

**Needed when you [Configure <code>Secrets</code>](#configure-secrets)**

* Save names and values in a text-only editor
* These same <code>Secrets</code> are used for Loop and for [Other Apps](gh-other-apps.md)
    * <code>TEAMID</code>
    * <code>FASTLANE_ISSUER_ID</code>
    * <code>FASTLANE_KEY_ID</code>
    * <code>FASTLANE_KEY</code>
    * <code>GH_PAT</code>
    * <code>MATCH_PASSWORD</code>

### Collect the Four `Apple Secrets`

??? tip "Collect the Four `Apple Secrets`"
    This step is common for all repositories that use GitHub Browser Build method; do this step only once. You will be saving 4 <code>Secrets</code> from your Apple Account in this step.

    1. Sign in to the [Apple developer portal page](https://developer.apple.com/account/resources/certificates/list).
    1. Copy the Team ID from the upper right of the screen. Record this as your `TEAMID`.
    1. Go to the [App Store Connect](https://appstoreconnect.apple.com/access/api) interface, click the "Keys" tab, and create a new key with "Admin" access. Give it the name: "FastLane API Key".
    1. Record the issuer id; this will be used for `FASTLANE_ISSUER_ID`.
    1. Record the key id; this will be used for `FASTLANE_KEY_ID`.
    1. Download the API key itself, and open it in a text editor. The contents of this file will be used for `FASTLANE_KEY`. Copy the full text, including the "-----BEGIN PRIVATE KEY-----" and "-----END PRIVATE KEY-----" lines.

    To skip the detailed section, click on [Collect the Two GitHub Secrets](#collect-the-two-github-secrets)

### New Apple Developer Account

If you have an Apple Developer Account, skip ahead to [Find <code>TEAMID</code>](#find-teamid), you should sign in to your account before starting. There will be links to take you to specific pages; if you are not already logged in, you will be required to log in before you can go to that page.

If you do not already have a paid Apple Developer account, you need to purchase one ($99 annual fee). It may take a few days for the account to be enabled.

* LoopDocs has an [Apple Developer Program](../build/step6.md) page that explains in detail how to sign up for an account
* This link takes you straight to [Apple Developer account](https://developer.apple.com) to sign up

### Find <code>TEAMID</code>

- Open this link: [Apple developer portal page](https://developer.apple.com/account).
- Click `Account` in the top menu bar
- Click the `Membership Details` icon  
    ![Apple Developer Account Membership Details](img/apple_dev_account-teamid-001.svg)
- Next to the `Team ID` field, you will see a 10-character ID number.  
  This is your **Apple Developer `TEAMID`**.
    ![Apple Developer TEAMID](img/apple_dev_account-teamid-002.svg)
- Record this for use when you configure your *Secrets* and when you configure your unique <span class="notranslate">App Group</span>  
- Stop a moment and double-check - if you get this wrong, you will have errors later

    !!! tip "Do not "type" what you think you see"
        **Copy and paste** from the `Team ID` from the webpage.  
        (Avoid the wrong number of characters; avoid typing an `8` when it should be a `B`.)

### Generate API Key
!!! info "Need a Paid Apple Developer Account Set Up to Generate the API Key"
    You cannot generate the API Key until you have the paid Apple Developer account set up.  
    If you are still waiting for Apple to enable your account, you can skip ahead to complete part of the GitHub steps (see [New GitHub Account](#new-github-account) or [Setup GitHub](#setup-github)), but you will need to pause at [Configure Secrets](#configure-secrets).

!!! abstract
    This section will walk you through the steps required to gather or create these parameters.

    |Name|Description|
    |---------|---------|
    |<code>TEAMID</code>|This 10-character identifier is associated with your Apple Developer ID and never changes|
    |<code>FASTLANE_ISSUER_ID</code>|The issuer ID is associated with your Apple Developer ID and never changes|
    |<code>FASTLANE_KEY_ID</code>|Key ID provided when you create an API key in App Store Connect; it is associated with the <code>FASTLANE_KEY</code>|
    |<code>FASTLANE_KEY</code>|Copy the full key from the text file you downloaded when generating the API key - Filename has <code>FASTLANE_KEY_ID</code> value embedded in it.<br>Include everything in the file from <br>`-----BEGIN PRIVATE KEY-----`<br>and ending in <br>`-----END PRIVATE KEY-----`<br> |
    
    Each step has a link to take you to the specific page you need to do the next step. It is best if you open each link in a separate tab or window so you can refer back to these instructions as you move along.


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

### Copy `API Key Secrets`

The `Keys` screen is seen again with the additional content similar to that shown in the graphic below; the key information is blanked out for security.

* Review the graphic and then follow the directions below to save more parameters you will need to [Configure <code>Secrets</code>](#configure-secrets)

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


### Collect the Two GitHub Secrets




