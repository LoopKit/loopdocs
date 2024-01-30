## Build the *Loop* App using *GitHub*

???+ info "Time Estimate (click to open/close)"
    - If you have never built the *Loop* app (allow up to one week elapsed time)
        * Request and get an <span>*Apple Developer* Account</span>: 1-2 days
        * Create and configure your *GitHub* account and `repositories`: 1-2 hours
        * Add <code>Secrets</code> (requires *Apple Developer* Account): 1 hour
        * Perform the *GitHub* `Action` steps: 30 minutes to 2 hours
    - If you have previously built the *Loop* app with *Xcode* you have fewer steps and are probably familiar with some of the concepts
        * Expect 1 to 4 hours

???+ abstract "Page Summary with Links (click to open/close)"
    There is a lot of introductory information on this page.

    * You can skip some sections but please read this one: [Save Your Information](#save-your-information)

    A narrated video is available:

    * [How to Build the *Loop* App With a Web Browser](https://www.youtube.com/watch?v=kiu5ho0MTW8){: target="_blank" }

    Once you have *Apple Developer* and *GitHub* accounts, the steps below are a high-level summary with links to the detailed section of this LoopDocs page.

    You can think of the first part as a scavenger hunt where you find or generate and save six <code>Secrets</code>.

    * _<span translate="no">Apple</span>_:
        * [Collect the four *Apple* <code>Secrets</code>](#collect-the-four-apple-secrets)
    * *GitHub*:
        * [Collect the <code>GH_PAT</code> Secret](#collect-the-gh_pat-secret)
    * [Make up a Password](#make-up-a-password)

    Now it's time to use those <code>Secrets</code> to build the Loop app

    * *GitHub*:
        * [Fork a repository (copy of <code>LoopWorkspace</code>)](#fork-loopworkspace)
        * [Add <code>Secrets</code> to your copy of LoopWorkspace repository](#configure-secrets)
        * [`Action: 1. Validate Secrets`](#validate-secrets)
        * [`Action: 2. Add Identifiers`](#add-identifiers)
    * _<span translate="no">Apple</span>_:
        * [Configure Identifiers for *Loop*](#configure-identifiers-for-loop)
        * [Create your version of *Loop* in `App Store` (personal use only, not for distribution)](#create-loop-app-in-app-store-connect)
    * *GitHub*:
        * [`Action: 3. Create Certificates`](#create-certificates)
        * [`Action: 4. Build Loop`](#build-the-loop-app)
    * _<span translate="no">Apple</span>_: [Set up `Internal TestFlight Group`](#set-up-users-and-access-testflight)
    * Phone: [Install the *Loop* app using the *TestFlight* app](../gh-actions/gh-deploy.md#deploy-using-testflight)

???+ question "FAQs (click to open/close)"
    - **Do I need a Mac computer?** No. This can be done on any browser, although it will be easier using a computer or tablet than just using a phone.
    - **Isn't it hard to build every 90 days?** The initial setup and installation take a lot of your focused time. But once you build, future updates and builds are automatic. You just need to keep your Apple Developer account up to date. Review any email that says a GitHub action failed - read the error and take action.
    - **Can you explain the new automatic building?** See this section [Automatic Update, Build, Install](gh-deploy.md#automatic-update-build-install) for more explanations
    - **Can I use this for my child?** You, as the adult, can install using *TestFlight* on your child's phone. The explicit steps are provided at [Install on Phone: *TestFlight* for a Child](gh-deploy.md#testflight-for-a-child).
    - **Can I still use my customizations?** Yes. [Customize using Browser](custom-browser.md)
    - **Is there a build video?** Yes. [How to Build the *Loop* App With a Web Browser](https://www.youtube.com/watch?v=kiu5ho0MTW8){: target="_blank" }

## Automatic Build of Loop

When you follow the directions on this page, for Loop 3.4 and later, you configure your app to automatically build at least once a month. You also configure your app to be updated within one week of a new release, in other words, when the LoopKit/LoopWorkspace main branch is updated.

* What if I want to modify the automatic update and build schedule?
    * [Modify Automatic Building](gh-update.md#modify-automatic-building)
* What if I want to turn off automatic building?
    * [Stop Building](gh-update.md#stop-building)

## Tips and Tricks

This page contains fully detailed steps including graphics, which makes it incredibly long.

Some sections have a Section Summary:

* To view the summary, click on the summary header
* If the summary is all you need, use the `skip forward` symbol (<span class="loop-big">:material-skip-forward:</span>) to skip to the next instruction
* Or follow the detailed instructions below the summary

As you configure for Browser Build, you go back and forth between *GitHub* and *Apple Developer* webpages. Use click to open a new tab or copy a link address, as appropriate, while proceeding.

An automatic table of contents (TOC) should appear for each page on the right side of your browser (if the browser is "wide" enough). If not, tap on the hamburger menu (upper left) and then this page name to see the TOC.

For sparse instructions, click on the link below:

* [LoopWorkspace Build Instructions](https://github.com/LoopKit/LoopWorkspace/blob/main/fastlane/testflight.md){: target="_blank" }

### How-to Video to Build with a Browser

In addition to this page, there is a narrated video of each step needed to build using a browser.

* [How to Build the *Loop* App With a Web Browser](https://www.youtube.com/watch?v=kiu5ho0MTW8){: target="_blank" }

Click in the comments for a full index of topics.  If you have issues with a step, use the index to  advance to the relevant part of the video. Subtitles are  in English. You can choose a different language but the automatic translation feature may provide translations that are not completely accurate.

## Prerequisites

#### Prerequisites to Build the *Loop* App

There are two prerequisites to build the *Loop* app using <code>*GitHub* Browser Build</code>.

1. Paid *Apple Developer* account ($99/year)
1. Free *GitHub* account

#### Prerequisites to Install Loop

To install Loop, you need the free *TestFlight* app, from the *Apple* App Store, installed on your [Compatible Phone](../build/phone.md).

#### Prerequisites to Use Loop

To use Loop, you need a [Compatible Pump](../build/pump.md) and [Compatible CGM](../build/cgm.md). For pumps other than Omnipod DASH, you also need a [RileyLink Compatible Device](../build/rileylink.md).

## New Terms with <code>*GitHub* Browser Build</code>

[<span class="loop-big">:material-skip-forward:</span>](#save-your-information) You can read details about new terms with *GitHub* build or skip ahead to [Save Your Information](#save-your-information).

The <code>*GitHub* Browser Build</code> may use new and unfamiliar **terms**.

Some of these **terms** have ToolTips, so hover your mouse over those - or review them in the [Glossary](../faqs/glossary.md).

* Some terms in the Glossary are not in alphabetical order. All the <code>Secrets</code> discussed on this page, are listed after <code>Secrets</code> in the Glossary.

If this summary of terms is confusing, finish reviewing the whole page and then come back.

* `Actions`: available in your *GitHub* account to build your app (once you follow the instructions on this page)
    * With `Loop 3`, the actions: `Validate Secrets`, <code>Add Identifiers</code>, `Create Certificates`, and `Build Loop` enable users to build the *Loop* app from a browser on any computer
    * If <code>*GitHub* Browser Build</code> Actions are not operating as you expect, check [*GitHub* Status](https://www.githubstatus.com/){: target="_blank" } to see if it is *GitHub* problem.
* <code>Secrets</code>: are required to enable *GitHub* to build the *Loop* app using *GitHub* Actions
    * Six <code>Secrets</code> must be added to your fork of LoopWorkspace
    * These <code>Secrets</code> work for any branch in your fork (`main` or `dev`, for example)
    * These <code>Secrets</code> can be added to [Other Apps](gh-other-apps.md) configured with the same <code>*GitHub* Browser Build</code> method
    * For those who feel confident using *GitHub*, there are optional instructions to configure a free organizational account (for your personal use) that allows you to enter the <code>Secrets</code> only once, see [Use a *GitHub* Organization Account](gh-other-apps.md#use-agithub-organization-account), and have them available for every repository in that organization account
* API `Key`:`Application Programming Interface Key`
    * You obtain and save this key from the *Apple Developer* website
    * Doing this provides 3 of your <code>Secrets</code>
    * It is required to enable your *GitHub* account to interface with *Apple* to create your app
* `Identifiers`: are required to build the *Loop* app with <code>*GitHub* Browser Build</code> (these are automatically generated for you)
    * Four Identifier Names must be associated with your `App Group`
        * `Loop`, `Loop Intent Extension`, `Loop Status Extension` and `Loop Widget Extension`
    * Two Identifier Names will exist but do not require that association
        * `WatchApp` and `WatchAppExtension`
    * The `Identifier` screen, has **`NAME`** and **`IDENTIFIER`** columns
        * If you previously built with Xcode, the items in the **`NAME`** column may start with `XC`
        * The items under the **`IDENTIFIER`** column match the table in [Add `App Group` to Identifiers](#add-app-group-to-identifiers)
* [`App Store Connect`](https://appstoreconnect.apple.com){: target="_blank" }: a website available for *Apple Developer*s to review apps build with your *Apple Developer* account
    * Once you purchase an *Apple Developer* annual account, you are an *Apple Developer* and have access to this site
    * Most Loopers will not have an App until using the <code>*GitHub* Browser Build</code>
    * The instructions walk you through creating and naming your app: [Create Loop App in App Store Connect](#create-loop-app-in-app-store-connect)

## Save Your Information

**Everyone needs to read this section!**

You need to keep a digital copy of your 6 <code>Secrets</code>.

* You need to copy and paste those <code>Secrets</code> to build the app with a browser
* Make sure your editor does not change any characters in your <code>Secrets</code>; use a text-only editor like NotePad (PC) or TextEdit (Mac)
* Many people add other information to the <code>Secrets</code> file for easy reference

!!! tip "Archive Your Information"
    To complete the steps on this page, you will need a username, email address, and password for *Apple* and *GitHub*. You will find, generate or make up six <code>Secrets</code> as instructed.

    * Record this information in a safe place where you can find them
    * A digital copy is best for copying and pasting in different locations

    **Be sure to use a Text-Only editor like NotePad (PC) or TextEdit (Mac) to archive your information.**

!!! info "A Note about Capitalization and Spaces"
    In places, you use a name like "`FastLane API Key`" or "`FastLane Access Token`". Please copy from the docs to use those exact names.

    The <code>Secrets</code> that you add use names that are capitalized and use underscore ++"_"++ instead of spaces. Be precise and careful.

!!! important "Use a Text-Only Editor"
    **Be sure to use a Text-Only editor like NotePad (PC) or TextEdit (Mac) to archive your information.**

    If you use a "smart" editor, it may change lower-case letters to upper-case letters at the beginning of a line when you paste items into your archive file.

    If even one character is capitalized when it should not be, you will get [Errors with Browser Build](gh-errors.md).

    If you use a smart editor to store your FASTLANE_KEY, you are likely to get the mysterious `invalid curve name` error.

## Save Six Secrets

??? abstract "Section Summary (click to open/close)"
    You require 6 <code>Secrets</code> (alphanumeric items) to use the <code>*GitHub* Browser Build</code> method and if you use the <code>*GitHub* Browser Build</code> method to build more than Loop, e.g., <code>Loop Follow</code> or <code>Loop Caregiver</code>, you **must** use the same 6 <code>Secrets</code> for each app you build with this method.

    Each secret is identified with `ALL_CAPITAL_LETTER_NAMES`.

    * Four <code>Secrets</code> are from your *Apple* Account
    * One Secret is from your *GitHub* account
    * One Secret is a password you make up and save
    * Be sure to save the 6 <code>Secrets</code> in a text file using a text editor
        - Do **NOT** use a smart editor, which might auto-correct and change the case, because these <code>Secrets</code> are case-sensitive
        - [<span class="loop-bigger">:material-skip-backward:</span>](#save-your-information) Refer back to [Save Your Information](#save-your-information) for more details about smart vs text editors

    [<span class="loop-bigger">:material-skip-forward:</span>](#collect-the-four-apple-secrets) To skip the detailed instructions, click on [Collect the Four `Apple Secrets`](#collect-the-four-apple-secrets)

You need to save your information digitally, so you can copy and paste. The information is created in one place and used in another. Refer to [Configure <code>Secrets</code>](#configure-secrets) for how the <code>Secrets</code> are used. In addition to the 6 <code>Secrets</code>, other important information to keep handy (like usernames and passwords) is listed below. Be sure to keep this file secure.

**Created at developer.apple.com**

* Email address (this is your username)
* password
* Four items used as <code>Secrets</code>
    * <code>TEAMID</code>
    * <code>FASTLANE_ISSUER_ID</code>
    * <code>FASTLANE_KEY_ID</code>
    * <code>FASTLANE_KEY</code>

**Created at github.com**

* Email address
* password
* username
* Your *GitHub* repository address will be: `https://github.com/username`
* Your LoopWorkspace repository address will be: `https://github.com/username/LoopWorkspace`
* One item used as a Secret
    * *GitHub* Personal Access Token (<code>GH_PAT</code>)

**Created yourself**

* a password - make one up and save it (<code>MATCH_PASSWORD</code>)

### Collect the Four `Apple Secrets`

??? abstract "Section Summary (click to open/close)"
    You will be saving 4 <code>Secrets</code> from your *Apple* Account in this step.

    1. Sign in to the [*Apple Developer* portal page](https://developer.apple.com/account){: target="_blank" }.
    1. If you need to accept a new agreement (happens about twice a year), be sure to do so now
        * Need help? Look at this section on the update page: [Accept Agreements](gh-update.md#accept-agreements)
    1. Copy the Team ID from the upper right of the screen. [Record this as your `TEAMID`](#find-teamid).
    1. Go to the [App Store Connect](https://appstoreconnect.apple.com/access/api){: target="_blank" } interface, click the "Keys" tab, and create a new key with "Admin" access. Give it the name: ["`FastLane API Key`"](#generate-api-key).
    1. [Record three more secrets](#copy-api-key-secrets)
        * Record the issuer id; this will be used for `FASTLANE_ISSUER_ID`.
        * Record the key id; this will be used for `FASTLANE_KEY_ID`.
        * Download the `API Key` itself, and open it in a text editor. The contents of this file will be used for `FASTLANE_KEY`. Copy the full text, including the "-----BEGIN PRIVATE KEY-----" and "-----END PRIVATE KEY-----" lines.

    [<span class="loop-bigger">:material-skip-forward:</span>](#collect-the-gh_pat-secret) To skip the detailed instructions, click on [Collect the <code>GH_PAT</code> Secret](#collect-the-gh_pat-secret)

This section provides detailed instructions for the four <code>Secrets</code> associated with your *Apple Developer* ID.

|Name|Description|
|---------|---------|
|<code>TEAMID</code>|This 10-character identifier is associated with your *Apple Developer* ID and never changes|
|<code>FASTLANE_ISSUER_ID</code>|The issuer ID is associated with your *Apple Developer* ID and never changes|
|<code>FASTLANE_KEY_ID</code>|Key ID provided when you create an `API Key` in App Store Connect; it is associated with the <code>FASTLANE_KEY</code>|
|<code>FASTLANE_KEY</code>|Copy the full key from the text file you downloaded when generating the `API Key` - Filename has <code>FASTLANE_KEY_ID</code> value embedded in it.<br>Include everything in the file from <br>`-----BEGIN PRIVATE KEY-----`<br>and ending in <br>`-----END PRIVATE KEY-----`<br> |

### New *Apple Developer* Account

[<span class="loop-bigger">:material-skip-forward:</span>](#find-teamid) If you have an *Apple Developer* Account, skip ahead to [Find <code>TEAMID</code>](#find-teamid).

If not, you need to purchase one ($99 annual fee). It may take a few days for the account to be enabled.

* LoopDocs has an [*Apple Developer* Program](../build/apple-developer.md) page that explains in detail how to sign up for an account
* This link takes you straight to [*Apple Developer* account](https://developer.apple.com){: target="_blank" } to sign up

### Find <code>TEAMID</code>

Sign in to your *Apple Developer* account at this link: [*Apple Developer* portal page](https://developer.apple.com/account){: target="_blank" }.

1. Click `Account` in the top menu bar
1. If you need to accept a new agreement (happens about twice a year), be sure to do so now
    * Need help? Look at this section on the update page: [Accept Agreements](gh-update.md#accept-agreements)
1. Click the `Membership Details` icon

    ![Apple Developer Account Membership Details](img/apple_dev_account-teamid-001.svg){width="600"}
    {align="center"}

1. Next to the `Team ID` field, is a 10-character ID number.
  This is your ***Apple Developer* `TEAMID`**.

![Apple Developer TEAMID](img/apple_dev_account-teamid-002.svg){width="500"}
    {align="center"}

Record this for use as <code>TEAMID</code> in your <code>Secrets</code> file. You will also need it when you [Create &nbsp;<span class="notranslate">App Group</span>](#create-app-group).

- Stop a moment and double-check
* If you get this wrong, you will have errors at the very end, which require you to delete some items and repeat some steps on this page

    !!! tip "Do not "type" what you think you see"
        **Copy and paste** the `Team ID` from the webpage.

        * <code>TEAMID</code> must be 10 characters
        * Avoid typing an&nbsp;<span class="loop-biggest">`8`</span>&nbsp;when it should be a&nbsp;<span class="loop-biggest">`B`</span>

### Generate `API Key`

!!! info "Paid *Apple Developer* Account is Required"
    To generate the `API Key`, you must have a paid *Apple Developer* account.

    If you are waiting for *Apple* to enable your account, you can skip ahead to create a [New *GitHub* Account](#new-github-account) and [Create *GitHub* `Personal Access Token`](#create-github-personal-access-token). You then pause at [Configure <code>Secrets</code>](#configure-secrets) until your *Apple* account is active.

1. Click this link in a new tab: [`App Store Connect/Access/API`](https://appstoreconnect.apple.com/access/api){: target="_blank" }

    * The top of the display is shown in the graphic below

    ![App Store Connect Key page](img/api-key-initial-screen.svg){width="700"}
    {align="center"}

    * Click the `Keys` tab as indicated in the graphic above
        * If this is your first time here, you will see:

            "`Permission is required to access the App Store Connect API. You can request access on behalf of your organization.`"

            * Click on `Request Access` and follow directions until access is granted

        * Once access is granted, click on the `Generate API Key` button

    * If you did not get routed through the `permission is required` screens click the blue &plus; sign

    * A new `Generate API Key` dialog box will appear as shown in the graphic below

    ![generate api key dialog box](img/dev-generate-key.png){width="500"}
    {align="center"}

    * Enter the name of the key as "`FastLane API Key`" and choose `Admin` in the access drop-down menu
    * Confirm the name and that "`Admin`" is selected and then click on the "`Generate`" button.

### Copy `API Key Secrets`

The `Keys` screen appears again with content similar to the graphic below; the key information is blanked out for security.

Review the graphic and then follow the directions below to save more parameters you will need to [Configure <code>Secrets</code>](#configure-secrets)

![App Store Connect Key page](img/api-key-in-process.svg){width="700"}
{align="center"}

1. A button labeled Copy is always adjacent to the `Issuer ID` above the word Active (this is the same for all keys that you generate with this *Apple Developer* ID)
    * Tap on the `Copy` button - this copies the `Issuer ID` into your paste buffer
    * In the file where you are saving information, paste this with the indication that it is for  `FASTLANE_ISSUER_ID`
1. Hover to the right of the `Key ID` and the `Copy Key ID` button shows up
    * Tap on the `Copy Key ID` button - this copies the `Key ID` into your paste buffer
    * In the file where you are saving information, paste this with the indication that it is for  `FASTLANE_KEY_ID`
1. Click on the `Download API Key` button - you will be warned you can only download this once.

    ![download key only once](img/dev-dl-key-once.png){width="700"}
    {align="center"}

6. Find your `AuthKey` download in your downloads folder. The name of the file will be "`AuthKey_KeyID.p8`" where `KeyID` matches your `FASTLANE_KEY_ID`

    * Double-click to open it and you will be presented a message asking how you'd like to open it (The message shown is for a Mac - translate these directions to whatever computer you are using)
    * Click on "`Choose Application...`" and then select "`TextEdit`" (on a Mac, NotePad on a PC, or any text-only editor you prefer)

    ![img/apns-open.png](../nightscout/img/apns-open.png)

1. The contents of this file will be used for `FASTLANE_KEY`

    * Copy the full text, including the "`-----BEGIN PRIVATE KEY-----`" and "`-----END PRIVATE KEY-----`" lines
        * On a *Mac*, use ++command+"A"++, then ++command+"C"++  to copy all the contents
        * On a **PC**, use ++control+"A"++ , then ++control+"C"++ to copy all the contents
    * In the file where you are saving information, paste this with the indication that it is for  `FASTLANE_KEY`

    ![img/apns-copy-key.png](../nightscout/img/apns-copy-key.png)

### Do Not Confuse Your Keys

!!! important "<span class="loop-big">`API Key`</span>&nbsp; vs&nbsp;<span class="loop-big">`APN Key`</span>"
    If you use [Remote Commands with <code>Nightscout</code>](../nightscout/remote-overview.md), you may notice the Application Programming Interface (API) key has the same type of format as the *Apple* Push Notification (APN) key. The keys for both of these purposes are p8 keys, but they should not be confused with each other.

    The <code>Secrets</code> for building with *GitHub* use the&nbsp;<span class="loop-bigger">`API Key`</span>.

    The config vars for `Nightscout` use the&nbsp;<span class="loop-bigger">`APN Key`</span>.

    * If you are using remote commands with `Nightscout` and building with <code>*GitHub* Browser Build</code>
        * [Remote Commands Config Vars](../nightscout/remote-config.md#remote-build-config-var-requirement): make sure you have a config var of `LOOP_PUSH_SERVER_ENVIRONMENT` with a value of `production` or remote commands will not work with `Nightscout`
    * This is true for using *<code>Nightscout</code>* directly or using *<code>Loop Caregiver</code>*

### Done with *Apple* Secrets

In summary, from this section, you have found or generated the following and saved copies for later use

* <code>TEAMID</code>
* <code>FASTLANE_ISSUER_ID</code>
* <code>FASTLANE_KEY_ID</code>
* <code>FASTLANE_KEY</code>

!!! tip "Time for a Break?"
    This is a good place to pause if you need to. Just note where you are on the page so you can return later.

### Collect the <code>GH_PAT</code> Secret

[<span class="loop-bigger">:material-skip-forward:</span>](#create-github-personal-access-token) If you already have a *GitHub* Account, skip ahead to [Create *GitHub* `Personal Access Token`](#create-github-personal-access-token).

### New *GitHub* Account

If you do not already have a *GitHub* account, you need to create one. Be sure to record the email, password, and username for your *GitHub* account.

Decide on a couple of usernames that you will be happy with - this will get embedded into your *GitHub* URL. Your first choice might not be available, so be prepared with several candidates. Your personal URL will be: `https://github.com/username`.

* Click on this link to sign up for a free account: [*GitHub* account signup](https://github.com/signup){: target="_blank" }
    * You will need to enter the **email** you want associated your *GitHub* account
    * You will be asked to enter a **password**
    * You will be asked to enter a **username**
    * You will be asked if you want to receive email, ok to say `N` for no - you still get important account information with that email
    * Solve the puzzle to prove you're a person
    * Check the associated **email** to get the code and enter the code into github.com to confirm your account
* You should get the Welcome to *GitHub* screen
    * Indicate it is "Just me" on your team and Continue
    * Don't check anything on the next screen, just tap `Continue`
    * Select the `Free` option by selecting `Continue for Free`

The free level comes with plenty of storage and compute time to build the *Loop* app.

### Create `GitHub Personal Access Token`

??? abstract "Section Summary (click to open/close)"
    Log into your *GitHub* account to create a personal access token, which you will save as <code>GH_PAT</code>.

     Click to create a [new `personal access token`](https://github.com/settings/tokens/new){: target="_blank" }:

    * Enter a name for your token, use "`FastLane Access Token`"
    * Change the Expiration selection to `No expiration`
    * Select the `workflow` `permission scope` (`repo` will be automatically selected)
        * This step enables automatic building
    * Click "Generate token"
    * Copy the token and record it. It will be used below as `GH_PAT`

    [<span class="loop-bigger">:material-skip-forward:</span>](#make-up-a-password) To skip the detailed instructions, click on [Make up a Password](#make-up-a-password).

!!! tip "Default Settings"
    These instructions are a prerequisite for automatic update and automatic build.

    Refer to [Modify Automatic Building](gh-update.md#modify-automatic-building) if you don't want to accept the default recommendation to automatically update and build.

You must be logged into your *GitHub* account before starting this step. If you are continuing, you are already logged in.

1. You will be creating a new *GitHub* `Personal Access Token` and giving it the name "`FastLane Access Token`"
1. Open this link: [https://github.com/settings/tokens/new](https://github.com/settings/tokens/new){: target="_blank" }
    * Referring to the graphic
        * Note that `Tokens (classic)` is highlighted
        * Most Looper will use the `classic Token`
            * If you are a developer who needs to use fine-grained `tokens`, that is fine
        * Edit the note box to be `FastLane Access Token`
    * The default Expiration time is 30 days - but you should select `No expiration` (use the drop-down menu to select)
        * *GitHub* will show a yellow warning when you do this
        * It is ok to ignore the warning
    * Add a check beside the `workflow` permission scope
    * A check will automatically appear in the `repo` scope as well - this is normal
    * Scroll all the way to the bottom and click `Generate token` (it's a long way, ignore all other settings, do not check anything else)

    ![request a new personal access token](img/gh-access-token.svg){width="700"}
    {align="center"}

    !!! tip "What does `repo` and  `workflow` do?"
        * `repo`: enables manual build actions
        * `workflow`: enables `repo` and automatic build actions

1. A new screen appears showing your access token
    * Copy the `token` and record it - once you leave this screen you can't see it again
    * You will use this for `GH_PAT` when you set up your Secrets
    * You can [Regenerate Personal Access Token](gh-update.md#regenerate-token) for `GH_PAT` if you lose it, but then you have to update that in the <code>Secrets</code> for all repositories using *GitHub* Build.

    ![copy fastlane access token on github](img/gh-token-to-copy.png){width="600"}
    {align="center"}

### Make up a Password

If you have not already made up a password, do it now and record it as <code>MATCH_PASSWORD</code>.

## Prepare your Repositories

### Fork LoopWorkspace

??? abstract "Section Summary (click to open/close)"
    Fork [https://github.com/LoopKit/LoopWorkspace](https://github.com/LoopKit/LoopWorkspace){: target="_blank" } into your account.

    [<span class="loop-bigger">:material-skip-forward:</span>](#configure-secrets) To skip the detailed instructions, click on [Configure <code>Secrets</code>](#configure-secrets)

!!! warning "Existing Fork"
    If you already have a fork of <code>LoopWorkspace</code>, click on [Already Have LoopWorkspace](#already-haveloopworkspace) to decide what to do. That section provides links to return you to these instructions.

1. Open this link [https://github.com/LoopKit/LoopWorkspace](https://github.com/LoopKit/LoopWorkspace){: target="_blank" } to open the <code>LoopWorkspace</code> repository owned by `LoopKit`.
1. Review the highlighted locations of the graphic below (yours won't look quite like this yet, but the `Fork` button is in the same place)
1. At the upper right side of the screen, click on the word `Fork`
    * If you already have a fork, you cannot proceed, see [Already Have LoopWorkspace](#already-haveloopworkspace)
1. Now your screen should look like the graphic below
    * Your username will be automatically filled in as the owner (`Owner`)
    * <code>LoopWorkspace</code> is the repository name (`Repository Name`)
    * Leave the selection that says "`Copy the main branch only`" checked
    * Click on the green `Create fork` button

    ![fork information for LoopWorkspace](img/gh-fork-loopworkspace.svg){width="700"}
    {align="center"}

#### Successful Fork

After creating the &nbsp;<span class="notranslate">fork</span>, your screen should be similar to the next graphic - it will say `main` for the branch instead of `dev` because this graphic was prepared before the release of `Loop 3`. You may or may not see the messages you are told to dismiss in the next two bullets. No worries if you don't see them.

* Near the top right, click on the close button :octicons-x-16: (`x`) to dismiss the `Successfully fetched` message
* In the middle, click on the `Dismiss` button to remove the "`Your branch is not protected`" message

![after creating the fork LoopWorkspace](img/gh-initial-fork-dismiss.png){width="500"}
{align="center"}

Carefully compare your screen to the graphic below paying attention to the highlighted sections.

* Note that your username is now showing
* The comment under your username indicates where the &nbsp;<span class="notranslate">fork</span>&nbsp; came from (that is a clickable link)
* The branch that is selected :octicons-git-branch-16: is `main`
* The message says "`This branch is up to date with LoopKit/LoopWorkspace:main`"

![after creating the fork LoopWorkspace](img/gh-after-fork.svg){width="700"}
{align="center"}

!!! tip "Time for a Break?"
    This is a good place to pause if you need to. Just note where you are on the page so you can return later.

## Configure <code>Secrets</code>

??? abstract "Section Summary (click to open/close)"
    These <code>Secrets</code> are the same for any repository for which you use `GitHub Browser Build`.

    * They are added once for a repository and work for all branches of that repository
    * They must be added to any other repository, such as <code>Loop Caregiver</code>, for which you also use `GitHub Browser Build`

    For each of the following <code>Secrets</code>, tap on "New repository secret", then add the name of the secret, along with the value you recorded for it:

    * `TEAMID`
    * `FASTLANE_ISSUER_ID`
    * `FASTLANE_KEY_ID`
    * `FASTLANE_KEY`
    * `GH_PAT`
    * `MATCH_PASSWORD`

    [<span class="loop-bigger">:material-skip-forward:</span>](#validate-secrets) To skip the detailed instructions, click on [Validate <code>Secrets</code>](#validate-secrets).

!!! tip "`Branches` and `Repositories`"
    * These &nbsp;<span class="notranslate">Secrets</span>&nbsp; are added to your `fork of LoopWorkspace` and work for any `branch` (`main` or `dev`, for example)
    * These &nbsp;<span class="notranslate">Secrets</span>&nbsp; must be added, if desired, for [Other App](gh-other-apps.md) `repositories`

### Prepare to Enter <code>Secrets</code>

Log into *GitHub*.

1. Return to your forked copy of <code>LoopWorkspace</code>
    * Click on your personal icon at the upper right to see the drop-down menu and select "`Your repositories`"

    ![drop-down-menu](img/gh-quick-access.png){width="200"}
    {align="center"}

1. Click on <code>LoopWorkspace</code> to open that repository
1. Click on the Settings Icon near the top right of your LoopWorkspace
    * If you don't see ⚙️ `Settings`, make your browser wider or scroll to the right
    * If you still don't see ⚙️ `Settings`, then you are **not** on your fork or you need to sign in to your *GitHub* account
    * After you click on ⚙️ `Settings`, your screen should look like the graphic below

        ![settings screen](img/gh-settings.svg){width="700"}
        {align="center"}

1. On the left side, find the `Secrets and variables` dropdown and choose <code>Actions</code>
    * After you select <code>Actions</code>, your screen should look like the graphic below

        ![action secrets and variables screen](img/gh-actions-secrets.svg){width="700"}
        {align="center"}

### Enter the <code>Secrets</code>

1. Tap on the green button at the top right of your screen labeled `New repository secret` (highlighted above)
    * A new screen appears as shown in the first graphic below
    * Do not do anything until reading the sub-bullets, examining the graphics, and proceeding to the next section where each `Secret` name is provided for you to copy and paste
        * Under `Name *`, click on `YOUR_SECRET_NAME` and paste one of the 6 secret names, as directed in [Enter Each Secret](#enter-each-secret)
        * Click inside the `Secret *` box and paste the value for that secret
        * Once you click on `Add Secret`, the secret will be added
        * The second graphic below shows `TEAMID` added and ready for save

![dialog for entering a new secret](img/new-secret-dialog.png){width="700"}
{align="center"}

![teamid secret ready to be saved](img/teamid-secret-ready-to-save.png){width="700"}
{align="center"}

#### Enter Each Secret

Enter the name of each <code>Secret</code> found in [Save Your Information](#save-your-information) and your value for that `Secret`.

* Once you save a secret value, you will not be able to view what you entered, so check carefully before you hit `Add Secret`
    * You can replace the value for any secret later - but you can't view the saved value
* Be especially careful with your `TEAMID`
    * If `TEAMID` is incorrect, the initial `Actions` will succeed but `Build Loop` will fail and you will have some clean-up to do

You can copy the names of the <code>Secrets</code> by hovering to the right of each word below until you see the copy button (:material-content-copy:). Click on the button to copy the `Secret` name and paste it into *GitHub* where you see `YOUR_SECRET_NAME`. This avoids spelling errors.
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
* For `MATCH_PASSWORD` value - if you did not already make up a password and save it with your other <code>Secrets</code>, do it now
    * The `MATCH_PASSWORD` must be the same for any repository using this method ([Other Apps](gh-other-apps.md))

Once all six <code>Secrets</code> have been added to your <code>LoopWorkspace</code>, your screen should look similar to the graphic below.

* Check that all of your <code>Secrets</code> are spelled correctly
* If one is misspelled, delete it and add a `New repository secret` with the correct name

![all secrets entered](img/gh-done-adding-secrets.png){width="700"}
{align="center"}

!!! tip "Time for a Break?"
    :fontawesome-regular-circle-pause: This is a good place to pause if you need to. Just note where you are on the page so you can return later.

## First Use of Actions Tab

Near the top middle of your <code>LoopWorkspace</code> &nbsp;<span class="notranslate">fork</span>&nbsp; is an <code>Actions</code> tab. This section provides detailed directions to enable <code>Actions</code>.

Click on the `Actions` tab of your <code>LoopWorkspace</code> repository.

* Your first time, a message appears saying `Workflows aren't being run on this forked repository` as shown in the graphic below
* Tap on the green button that says: `I understand my workflows, go ahead and enable them`

    ![workflows disabled screen](img/gh-workflows-disabled.png){width="700"}
    {align="center"}

The `workflows` are now displayed on the left side as shown in the graphic below. (Dismiss the `Actions Enabled` message using the `X` near the upper right side if it appears).

![workflows displayed](img/gh-workflows-enabled.svg){width="700"}
{align="center"}


## Validate <code>Secrets</code>

??? abstract "Section Summary (click to open/close)"
    This step validates most of your six <code>Secrets</code> and provides error messages if it detects an issue with one or more.

    1. Click on the "Actions" tab of your LoopWorkspace repository and enable workflows if needed
    1. On the left side, select `1. Validate Secrets`.
    1. On the right side, click "Run Workflow", and tap the green `Run workflow` button.
    1. Wait, and within a minute or two you should see a green checkmark indicating the workflow succeeded.
    1. The workflow will check if the required <code>Secrets</code> are added and that they are correctly formatted. If errors are detected, please check the run log for details.

    [<span class="loop-bigger">:material-skip-forward:</span>](#add-identifiers) To skip the detailed instructions, click on [<code>Add Identifiers</code>](#add-identifiers)

Near the top middle of your <code>LoopWorkspace</code> &nbsp;<span class="notranslate">fork</span>, click on the <code>Actions</code> tab.

* [<span class="loop-big">:material-skip-backward:</span>](#first-use-of-actions-tab)If you have never used <code>Actions</code> on this repository before, and need instructions (in addition to what *GitHub* shows), please back up to [First use of Actions Tab](#first-use-of-actions-tab).

Refer to the graphic below for the numbered steps:

1. Click on the `Actions` tab of your <code>LoopWorkspace</code> repository
1. On the left side, click on 1. <code>Validate Secrets</code>
1. On the right side, click `Run Workflow` to show a drop-down menu
    * You will see your default branch (typically this is `main`)
    * You can select a different branch, but typically, you run the default
1. Tap the green button that says `Run workflow`.

    ![add identifiers using github actions](img/action-01-validate-secrets.svg){width="700"}
    {align="center"}

The `Validate Secrets` &nbsp;<span class=notranslate>Action</span>&nbsp; should succeed or fail in a few minutes. Do not continue to the next step until this one succeeds.

* If you see the green check (:octicons-check-circle-fill-16:{: .passed })  continue to the next section
* If you see the red `X` (:octicons-x-circle-fill-16:{: .failed }):
    * [Examine the Error](gh-errors.md#examine-the-error) tells how to view the file needed to diagnose your problem.
    * [Action: Validate Secrets Errors](gh-errors.md#action-validate-secrets-errors) tells you what to search for in the file
    * Resolve the error and repeat the Action: [Validate Secrets](#validate-secrets)

## <code>Add Identifiers</code>

??? abstract "Section Summary (click to open/close)"
    1. Click on the "Actions" tab of your LoopWorkspace repository.
    1. On the left side, select "2. Add Identifiers".
    1. On the right side, click "Run Workflow", and tap the green `Run workflow` button.
    1. Wait, and within a minute or two you should see a green checkmark indicating the workflow succeeded.

    [<span class="loop-bigger">:material-skip-forward:</span>](#configure-identifiers-for-loop) To skip the detailed instructions, click on [Configure Identifiers for Loop](#configure-identifiers-for-loop).

Refer to the graphic below for the numbered steps:

1. Click on the `Actions` tab of your <code>LoopWorkspace</code> repository
1. On the left side, click on 2. <code>Add Identifiers</code>
1. On the right side, click `Run Workflow` to show a drop-down menu
    * You will see your default branch (typically this is `main`)
    * You can select a different branch, but typically, you run the default
1. Tap the green button that says `Run workflow`.

    ![add identifiers using github actions](img/action-02-add-identifiers.svg){width="700"}
    {align="center"}

The `Add Identifiers` &nbsp;<span class=notranslate>Action</span>&nbsp; should succeed or fail in a few minutes. Do not continue to the next step until this one succeeds.

* If you see the green check (:octicons-check-circle-fill-16:{: .passed })  continue to the next section
* If you see the red `X` (:octicons-x-circle-fill-16:{: .failed }):
    * [Examine the Error](gh-errors.md#examine-the-error) tells how to view the file needed to diagnose your problem.
    * [Action: Add Identifiers Errors](gh-errors.md#action-add-identifiers-errors) tells you what to search for in the file
    * Resolve the error and repeat the Action: [Add Identifiers](#add-identifiers)

## Configure Identifiers for Loop

Some steps can be skipped if you previously built the *Loop* app with `*Mac*`.

Please read carefully to avoid confusion.

### Create `App Group`

??? abstract "Section Summary (click to open/close)"
    [<span class="loop-bigger">:material-skip-forward:</span>](#previous-xcode-builders) If you have already built the *Loop* app via Xcode using this *Apple* ID, skip ahead to [Previous Xcode Builders](#previous-xcode-builders).

    1. Go to [Register an `App Group`](https://developer.apple.com/account/resources/identifiers/applicationGroup/add/){: target="_blank" } on the *Apple Developer* site.
    1. For Description, use "Loop App Group".
    1. For Identifier, enter "group.com.TEAMID.loopkit.LoopGroup", substituting your team id for `TEAMID`.
    1. Click "Continue" and then "Register".

    [<span class="loop-bigger">:material-skip-forward:</span>](#add-app-group-to-identifiers) To skip the detailed instructions, click on [Add `App Group` to Identifiers](#add-app-group-to-identifiers)

The `Loop` *App Group* already exists if you previously built the *Loop* app using *Xcode* with this *Apple Developer ID*. In that case, skip ahead to [Previous Xcode Builders](#previous-xcode-builders).

If you have never built the *Loop* app with *Xcode* using your `TEAMID`, you need to create an *App Group* associated with your `TEAMID`.

1. Open this link: [Register an App Group](https://developer.apple.com/account/resources/identifiers/applicationGroup/add/){: target="_blank" } on the *Apple Developer* site.
1. For **`Description`**, use `Loop App Group`.
1. For **`Identifier`**, enter `group.com.TEAMID.loopkit.LoopGroup`, substituting your team id for `TEAMID`.
1. Double-check the spelling - your `TEAMID` must be correct and the `Loop` *App Group* must match the format shown in the previous step
    * A mistake here means you will not be able to build the *Loop* app until you fix it
1. Click `Continue` and then `Register`.

### Add `App Group` to Identifiers

[<span class="loop-big">:material-skip-forward:</span>](#previous-xcode-builders) If you ever built the *Loop* app using *Mac*, skip ahead to [Previous Xcode Builders](#previous-xcode-builders).

#### New Builders

Click this link: [`Certificates, Identifiers & Profiles: Identifiers List`](https://developer.apple.com/account/resources/identifiers/list){: target="_blank" } on the *Apple Developer* site.

This will display a table similar to that linked below after a successful <code>Add Identifiers</code> *Action*. There are the six items under **`NAME`** with the associated **`IDENTIFIER`** information. Your `Developer ID` replaces the `TEAMID` in the `Identifier`.

[<span class="loop-big">:material-skip-forward:</span>](#table-with-name-and-identifier-for-loop-3) Skip ahead to [Table with Name and Identifier for Loop 3](#table-with-name-and-identifier-for-loop-3).

#### Previous Xcode Builders

Click this link: [`Certificates, Identifiers & Profiles: Identifiers List`](https://developer.apple.com/account/resources/identifiers/list){: target="_blank" } on the *Apple Developer* site.

Because you built the *Loop* app using *Xcode*, then the **`NAME`** associated with at least the `Loop identifier` will appear as `XC com.TEAMID.loopkit.Loop` under the **`NAME`** column. Ignore the **`NAME`** column and key off what you see under the **`IDENTIFIER`** column of the table. Only the six listed in the table below need to appear when building `Loop 3.4`. There may be other `Identifiers` here that are no longer used with the *Loop* app. Do not worry about those.

#### Table with Name and Identifier for `Loop 3`

| `NAME` | `IDENTIFIER` |
|-------|------------|
| `Loop` | `com.TEAMID.loopkit.Loop` |
| `Loop Intent Extension` | `com.TEAMID.loopkit.Loop.Loop-Intent-Extension` |
| `Loop Status Extension` | `com.TEAMID.loopkit.Loop.statuswidget` |
| `Loop Widget Extension` | `com.TEAMID.loopkit.Loop.LoopWidgetExtension` |
| `WatchApp` | `com.TEAMID.loopkit.Loop.LoopWatch` |
| `WatchAppExtension` | `com.TEAMID.loopkit.Loop.LoopWatch.watchkitextension` |

!!! warning "Loop dev Builders"
    The name and identifier for "`Small Status Widget`" has been renamed to "`Loop Widget Extension`". This only affects those using the dev branch until the next release. At that time, this table will be updated.

    If you are building with the dev branch, follow the directions at [One-Time Changes](../gh-actions/build-dev-browser.md#one-time-changes).

### Add or Review Configuration for `Loop Identifier`

??? abstract "Section Summary (click to open/close)"
    Note 1 - If you previously built with Xcode, the `Names` listed below may be different, but the `Identifiers` will match. A table was provided above that lists both `Names` and `Identifiers`. The Add Identifier Action that you completed above generates 6 identifiers, but only 4 need to be modified as indicated in this step.

    Note 2 - Depending on your build history, you may find some of the Identifiers already have your "App Group" and you are just verifying the status.

    1. Go to [Certificates, Identifiers & Profiles](https://developer.apple.com/account/resources/identifiers/list){: target="_blank" } on the *Apple Developer* site.
    1. For each of the following identifier names:
        * `Loop`
        * `Loop Intent Extension`
        * `Loop Status Extension`
        * `Loop Widget Extension`
    1. Click on the identifier's name
    1. On the "App Groups" capabilies, click on the "Configure" or "Edit" button
    1. If your "Loop App Group" with your TEAMID is not showing, then select it
        * Click "Save"
        * Click "Confirm"
    1. If your "Loop App Group" with your TEAMID is already configured
        * Click "All Identifiers" on upper left to return to the list
    1. Remember to do this for each of the identifiers in the table below

    [<span class="loop-bigger">:material-skip-forward:</span>](#create-loop-app-in-app-store-connect) To skip the detailed instructions, click on [Create Loop App in App Store Connect](#create-loop-app-in-app-store-connect)

Find and click on the row for the `Loop identifier` on the [Certificates, Identifiers & Profiles: Identifiers List](https://developer.apple.com/account/resources/identifiers/list){: target="_blank" } page. Look in the **`IDENTIFIER`** column to find `com.TEAMID.loopkit.Loop`. The name in the **`NAME`** column may be different than Loop.

| `NAME` | `IDENTIFIER` |
|-------|------------|
| `Loop` | `com.TEAMID.loopkit.Loop` |
| `Loop Intent Extension` | `com.TEAMID.loopkit.Loop.Loop-Intent-Extension` |
| `Loop Status Extension` | `com.TEAMID.loopkit.Loop.statuswidget` |
| `Loop Widget Extension` | `com.TEAMID.loopkit.Loop.LoopWidgetExtension` |

The `Edit Your App ID Configuration` screen will open. Take one action for the each identifier listed in this table:

1. In the `App Services` column, scroll down to the `App Groups` row
    * Ensure the check box (under the `Capabilities` column) for `App Groups` is checked
    * (`XC Loop`) - If the word `Edit` shows up under `NOTES`, move on to step 2 below
    * If the word `Configure` shows up, tap on it
        * This opens the `App Group Assignment` screen
        * Check the box by `Loop` *App Group* that uses your `TEAMID` in `group.com.TEAMID.loopkit.LoopGroup` and then `Continue`

If you modified settings for an `Identifier`, the `Save` button at the top right will become active. Click on `Save` before leaving this page - otherwise, the change does not take effect.

* Tap on `Save`
* This opens the `Modify App Capabilities` confirmation screen
* Click on `Confirm`

If you did not need to make changes, the `Save` button will not be active.

* Tap on the `< All Identifiers` button at the top left

The full list of Identifiers should be displayed again.

Repeat the steps until you have completed all 4 `Identifiers` in the table above. Yes - there are 6 `Identifiers` created, but only 4 need the `AppGroup` added.

## Create Loop App in App Store Connect

??? abstract "Section Summary (click to open/close)"
    If you have created a Loop app in App Store Connect before, skip ahead to [Create Certificates](#create-certificates).

    1. Click on the link [apps list](https://appstoreconnect.apple.com/apps){: target="_blank" } to open App Store Connect and click the blue "plus" icon to create a New App.
        * Select "iOS".
        * Select a name: this will have to be unique, so you may have to try a few different names here, but it will not be the name you see on your phone, so it's not that important.
        * Select your primary language.
        * Choose the bundle ID that matches `com.TEAMID.loopkit.Loop`, with TEAMID matching your team id.
        * SKU can be anything; e.g. "123".
        * Select "Full Access".
    1. Click Create

    You do not need to fill out the next form. That is for submitting to the app store.

    [<span class="loop-bigger">:material-skip-forward:</span>](#create-certificates) To skip the detailed instructions, click on [Create Certificates](#create-certificates).

If you have created a `Loop app` in *App Store Connect* before, skip ahead to [Create Certificates](#create-certificates).

If you have previously used some kind of remote build, like `diawi` or `TestFlight`, you may have your Loop in the *App Store* but can't see it. Don't worry - there are instructions for this case.

1. Open this link: [`App Store Connect / Apps`](https://appstoreconnect.apple.com/apps){: target="_blank" } to view your apps; log in if needed.
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
        * Once installed on your phone, you will see the *Loop* app with the standard `Loop Logo`
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

You are done with this activity and can close the browser tab. It's time to head back to your *GitHub* account and [Create Certificates](#create-certificates)

### Find My Loop

This section is for people who were not able to follow the instructions in the last section because `com.TEAMID.loopkit.Loop`, with **`TEAMID`** matching your `TEAMID`, was not in the dropdown menu for `Bundle ID`.

There are two possible reasons:

1. You did not complete [Add `App Group` to Identifiers](#add-app-group-to-identifiers) or one of the predecessor steps; review those steps
1. Your app is already in *App Store Connect*, but you cannot see it

You may have no memory of ever setting up `Loop` in *App Store Connect*. If you previously used some kind of remote build, like `diawi`, your `Loop` may be there as a *Removed App*.

* Open this link: [App Store Connect / Apps](https://appstoreconnect.apple.com/apps){: target="_blank" }, look for the `All Statuses` dropdown indicator, and select `Removed Apps`

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

## `Create Certificates`

??? abstract "Section Summary (click to open/close)"
    1. Go back to the "Actions" tab of your LoopWorkspace repository in *GitHub*.
    1. On the left side, select "3. Create Certificates".
    1. On the right side, click "Run Workflow", and tap the green `Run workflow` button.
    1. Wait, and within a minute or two you should see a green checkmark indicating the workflow succeeded.

    [<span class="loop-bigger">:material-skip-forward:</span>](#build-the-loop-app) To skip the detailed instructions, click on [Build the *Loop* App](#build-the-loop-app)

Refer to the graphic below for the numbered steps:

1. Click on the "<code>Actions</code>" tab of your <code>LoopWorkspace</code> repository
1. On the left side, click on "`Create Certificates`"
1. On the right side, click "`Run Workflow`" to show a drop-down menu
    * You will see your default branch (typically `main`)
    * You can select a different branch, but typically, you run the default
1. Tap the green button that says "`Run workflow`".

    ![create certificates using github actions](img/action-03-create-certs.svg){width="700"}
    {align="center"}

1. Wait a minute or two for the action to finish
    * If this action fails, head over to [Action: 3. Create Certificates Errors](gh-errors.md#action-create-certificates-errors)
    * Once you've resolved the error, repeat the Actions [Add Identifiers](#add-identifiers) and then `Create Certificates`.

## Build the *Loop* App

??? abstract "Section Summary (click to open/close)"
    1. Click on the "Actions" tab of your LoopWorkspace repository.
    1. On the left side, select "4. Build Loop".
    1. On the right side, click "Run Workflow", and tap the green `Run workflow` button.
    1. You have some time now. Go enjoy a coffee. The build should take about 20-30 minutes.
    1. You should get several emails
        * one says the build succeeded (or failed)
        * one says *TestFlight* is ready (typically half-hour after the build succeeds)
        * Ignore the one that says you need to fix "issues" in your app. You are not selling the app in the app store; so no action is required. The app you built is for personal use for you or a family member.
    1. Your app should eventually appear on [App Store Connect](https://appstoreconnect.apple.com/apps){: target="_blank" }.
    1. For each phone/person you would like to support:
        * Add them in [Users and Access](https://appstoreconnect.apple.com/access/users){: target="_blank" } on App Store Connect.
        * Add them to your *TestFlight* Internal Testing group.

    [<span class="loop-bigger">:material-skip-forward:</span>](#set-up-users-and-access-testflight) To skip the detailed instructions, click on [Set Up Users and Access (TestFlight)](#set-up-users-and-access-testflight).

Refer to the graphic below for the first four steps:

1. Click on the "`Actions`" tab of your <code>LoopWorkspace</code> repository.
1. On the left side, click on "4. `Build Loop`".
1. On the right side, click "`Run Workflow`" to show a drop-down menu
    * You will see your default branch (typically `main`)
    * You can select a different branch, but typically, you run the default
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
1. You should get several emails
    * one says the build succeeded (or failed)
    * one says *TestFlight* is ready (typically half-hour after the build succeeds)
    * Ignore the one that says you need to fix "issues" in your app. You are not selling the app in the app store; so no action is required. The app you built is for personal use for you or a family member.
1. Your app should eventually appear on [`App Store Connect`](https://appstoreconnect.apple.com/apps){: target="_blank" }.

## Build Failed?

Did you get a red X? Head over to the [Errors with Browser](gh-errors.md) to page find a solution.

## Successful Build

**Congratulations**

If you get the green check mark, your app successfully built. Just a few more steps.

### One Time Only (per User)

* Add users to your `App Store Connect` Users and Access by following the directions at [Set Up Users and Access (TestFlight)](#set-up-users-and-access-testflight)
* Continue following instructions to create an Internal Testing group for *TestFlight* for the *Loop* app
* Add the Users to the Internal Group and they get an email they must confirm

### Each Time

* Go to the phone for installing the updated app from *TestFlight*
* If you already set up your users, skip ahead to [Install on Phone](gh-deploy.md)

## Set Up Users and Access (TestFlight)

Once the first build completes, you will be able to configure *TestFlight* for the app.

!!! tip "Add Each Users One Time"
    Once you add a user to have access to your TestFlight for this app, you don't need to do it again - it remains available to them across rebuilds and different versions for that app.

You are configuring a private capability for your family using an Internal Testing group. You need the *Apple ID* email address for each adult installing from your build. When building for a child, you will use your own *Apple ID*, not theirs. See [*TestFlight* for a Child](gh-deploy.md#testflight-for-a-child).

1. First you need to add the email address(es) to your *App Store Connect* Access Users list:

    * Open this link: [Users and Access](https://appstoreconnect.apple.com/access/users){: target="_blank" }
        * You must provide a role for each person - `Customer Support` is a good choice
        * Once you have added them here, you'll be able to select them in the `TestFlight` group for your app

    ![add email and role for your users](img/add-users.png){width="700"}
    {align="center"}

1. Open this link: [App Store Connect / Apps](https://appstoreconnect.apple.com/apps){: target="_blank" } to view your apps; log in if needed. Then select your *Loop* app. Click on the `TestFlight` tab then click the blue plus button (<font color="#2997FF">:material-plus-circle:</font>) next to `Internal Testing` to add a group.

    ![open TestFlight tab for your app](img/setup-testflight-01.png){width="700"}
    {align="center"}

1. Fill out the name you want for the `Internal Testing` group
    * Be sure to check the box `Enable automatic distribution`
    * Click `Create` when done (this can always be modified later)

    ![add email and role for your users](img/setup-testflight-02.png){width="700"}
    {align="center"}

1. As soon as you create the group, you'll be asked who should be included
    * Click in the box beside each person you want to include
    * Each person in this group will get an email each time you update (build again) using the <code>*GitHub* Browser Build</code> method
    * Click `Add` when you are done
    * If building for a child, you will send the invitation to yourself because you will install for your child: See [TestFlight for a Child](gh-deploy.md#testflight-for-a-child)

    ![select your users for the testing group](img/setup-testflight-03.png){width="700"}
    {align="center"}

## Install on Phone

The [Install on Phone](gh-deploy.md) page walks you through the steps to use the *TestFlight* app to install the *Loop* app on a phone.

But wait - there's more.

* Caregivers who help manage a loved-ones diabetes often use other open-source apps that can be built the same way
* When you are done building and installing the *Loop* app, there are instructions to [Build Other Apps with Browser](gh-other-apps.md)

## Extra Steps

Most people won't need the information on the rest of this page.

### Already Have&nbsp;<span translate="no">LoopWorkspace</span>?

Some people may already have a copy of <code>LoopWorkspace</code>.

If your copy is **not** from `LoopKit`, follow the [Delete and Start Fresh](#delete-and-start-fresh) directions.

If your copy is from `LoopKit`:

* Open your <code>LoopWorkspace</code> repository (`https://github.com/username/LoopWorkspace`) where you use your *GitHub* `username` in the URL
* Review the graphic in the [Configure: Successful Fork](#successful-fork) section
    * Make sure all the items highlighted by red rectangles are correct with the possible exception of your fork being up to date
* If you see a message that your *fork* is not up to date - tap on the `Sync fork` button and follow the instructions
* Continue with [Create `GitHub Personal Access Token`](#create-github-personal-access-token)

#### Delete and Start Fresh

If your fork is not from `LoopKit`:

* Delete your LoopWorkspace repository
    * Instructions to delete a repository are found at [*GitHub* Docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository){: target="_blank" }
* Return to [Fork LoopWorkspace](#fork-loopworkspace) and follow all the instructions

### Delete Identifiers

When you have already built the *Loop* app with *Xcode*, the Identifier names will not match the directions and you might have trouble deciding which ones to configure.  Your existing `Loop` identifier will have a name that starts with `XC` as shown below, where your 10-digit `TEAMID` is used.

* `Name: XC com TEAMID loopkit Loop`
* `Identifier: com.TEAMID.loopkit.Loop`

The `Identifier` that is associated with the `Loop` identifier cannot be deleted if it is already in the *App Store* but all others can. If you attempt to delete the `XC` *Loop* identifier, you may be told it cannot be deleted because it is in use in the app store. That's OK. Same for other identifiers (if you build a bunch of Apps). If a `Bundle ID` has ever been associated with an app in the *App Store*, you cannot delete the `Identifier`.

To make it easy when configuring the identifiers, go through and delete as many as you can.

* Open this link: [Certificates, Identifiers & Profiles: Identifiers List](https://developer.apple.com/account/resources/identifiers/list){: target="_blank" } on the *Apple Developer* site.
* Use the graphic below as a guide to removing identifiers
* Keep repeating the steps until you've removed all the identifiers you can (or want to) delete
* It is OK to delete an identifier even if it does have your correct `TEAMID`
    * If you try to delete the `Loop` identifier with your `TEAMID`, it will refuse, don't worry, just keep going
* Note - this graphic indicates where on this page you can find your `TEAMID`
    * If you notice an identifier with a value embedded in it that does not have your `TEAMID`, then delete it if you can and [Update <code>Secrets</code>](gh-update.md#update-secrets) with your correct `TEAMID`
    * If you try to delete a Loop identifier that does not have your `TEAMID`, but you already added to the *App Store*, it will refuse, don't worry, just keep going
    * Delete all the other identifiers first that have the same incorrect `TEAMID` and then try to delete the Loop identifier with the incorrect `TEAMID`

![steps to delete a given identifier](img/delete-identifiers.svg){width="700"}
{align="center"}

If coming here from the Errors with Browser page because you enter the wrong `TEAMID` in `Secrets` - return to that page once you've deleted as many identifiers as you can: [Errors: Wrong TEAMID in Secrets](gh-errors.md#error-wrong-teamid-in-secrets).

If you were just trying to clean up the identifiers, then follow these steps:

* Run Action: [Add Identifiers](#add-identifiers) to add Identifiers with the documented short names
* Complete the [Add `App Group` to Identifiers](#add-app-group-to-identifiers)
* If you did not complete the [Create Loop App in App Store Connect](#create-loop-app-in-app-store-connect) step, do it now
* Continue with [Create Certificates](#create-certificates) and then [Build the *Loop* App](#build-the-loop-app)
