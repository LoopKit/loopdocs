## Collect and Save Secrets

??? abstract "Section Summary (click to open/close)"
    You require 6 <code>Secrets</code> (alphanumeric items) to use the <code>*GitHub* Browser Build</code> method and if you use the <code>*GitHub* Browser Build</code> method to build more than Loop, e.g., <code>Loop Follow</code> or <code>Loop Caregiver</code>, you **must** use the same 6 <code>Secrets</code> for each app you build with this method.

    Each secret is identified with `ALL_CAPITAL_LETTER_NAMES`.

    * Four <code>Secrets</code> are from your *Apple* Account
    * One Secret is from your *GitHub* account
    * One Secret is a password you make up and save
    * Be sure to save the 6 <code>Secrets</code> in a text file using a text editor
        - Do **NOT** use a smart editor, which might auto-correct and change the case, because these <code>Secrets</code> are case-sensitive
        - [<span class="loop-bigger">:material-skip-backward:</span>](intro-summary.md#save-your-information) Refer back to [Save Your Information](intro-summary.md#save-your-information) for more details about smart vs text editors

    [<span class="loop-bigger">:material-skip-forward:</span>](#collect-the-four-apple-secrets) To skip the detailed instructions, click on [Collect the Four `Apple Secrets`](#collect-the-four-apple-secrets)

You need to save your information digitally, so you can copy and paste. The information is created in one place and used in another. Refer to [Configure <code>Secrets</code>](prepare-fork.md#configure-secrets) for how the <code>Secrets</code> are used. In addition to the 6 <code>Secrets</code>, other important information to keep handy (like usernames and passwords) is listed below. Be sure to keep this file secure.

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
        * Need help? Look at this section on the update page: [Accept Agreements](bb-update.md#accept-agreements)
    1. Copy the Team ID from the upper right of the screen. [Record this as your `TEAMID`](#find-teamid).
    1. Go to the [App Store Connect](https://appstoreconnect.apple.com/access/integrations/api){: target="_blank" } interface, click the "Integrations" tab, and create a new key with "Admin" access. Give it the name: ["`FastLane API Key`"](#generate-api-key).
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
    * Need help? Look at this section on the update page: [Accept Agreements](bb-update.md#accept-agreements)
1. Click the `Membership Details` icon

    ![Apple Developer Account Membership Details](img/apple_dev_account-teamid-001.svg){width="600"}
    {align="center"}

1. Next to the `Team ID` field, is a 10-character ID number.
  This is your ***Apple Developer* `TEAMID`**.

![Apple Developer TEAMID](img/apple_dev_account-teamid-002.svg){width="500"}
    {align="center"}

Record this for use as <code>TEAMID</code> in your <code>Secrets</code> file. You will also need it when you [Create &nbsp;<span class="notranslate">App Group</span>](prepare-app.md#create-app-group).

- Stop a moment and double-check
* If you get this wrong, you will have errors at the very end, which require you to delete some items and repeat some steps on this page

    !!! tip "Do not "type" what you think you see"
        **Copy and paste** the `Team ID` from the webpage.

        * <code>TEAMID</code> must be 10 characters
        * Avoid typing an&nbsp;<span class="loop-biggest">`8`</span>&nbsp;when it should be a&nbsp;<span class="loop-biggest">`B`</span>

### Generate `API Key`

!!! info "Paid *Apple Developer* Account is Required"
    To generate the `API Key`, you must have a paid *Apple Developer* account.

    If you are waiting for *Apple* to enable your account, you can skip ahead to create a [New *GitHub* Account](#new-github-account) and [Create *GitHub* `Personal Access Token`](#create-github-personal-access-token). You then pause at [Configure <code>Secrets</code>](prepare-fork.md#configure-secrets) until your *Apple* account is active.

1. Click this link to open in a new tab: [`App Store Connect/Access/Integrations/API`](https://appstoreconnect.apple.com/access/integrations/api){: target="_blank" }

    * The top of the display is shown in the graphic below

    ![App Store Connect Key page](img/api-key-initial-screen.svg){width="700"}
    {align="center"}

    * Click the `Integrations` tab as indicated in the graphic above
        * If this is your first time here, you will see:

            "`Permission is required to access the App Store Connect API. You can request access on behalf of your organization.`"

            * Click on `Request Access` and follow directions until access is granted

        * Once access is granted, click on the `Generate API Key` button

    * If you did not get routed through the `permission is required` screens click the blue &plus; sign

    * A new `Generate API Key` dialog box will appear as shown in the graphic below

    ![generate api key dialog box](img/dev-generate-key.png){width="500"}
    {align="center"}

    * Enter the name of the key as "`FastLane API Key`" and choose `Admin` in the access dropdown menu
    * Confirm the name and that "`Admin`" is selected and then click on the "`Generate`" button.

### Copy `API Key Secrets`

The `Integrations` screen appears again with content similar to the graphic below; the key information is blanked out for security.

Review the graphic and then follow the directions below to save more parameters you will need to [Configure <code>Secrets</code>](prepare-fork.md#configure-secrets)

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

    Refer to [Modify Automatic Building](automatic.md#modify-automatic-building){: target="_blank" } if you don't want to accept the default recommendation to automatically update and build.

You must be logged into your *GitHub* account before starting this step. If you are continuing, you are already logged in.

1. You will be creating a new *GitHub* `Personal Access Token` and giving it the name "`FastLane Access Token`"
1. Open this link: [https://github.com/settings/tokens/new](https://github.com/settings/tokens/new){: target="_blank" }
    * Referring to the graphic
        * Note that `Tokens (classic)` is highlighted
        * Most Looper will use the `classic Token`
            * If you are a developer who needs to use fine-grained `tokens`, that is fine
        * Edit the note box to be `FastLane Access Token`
    * The default Expiration time is 30 days - but you should select `No expiration` (use the dropdown menu to select)
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
    * You can [Regenerate Personal Access Token](bb-update.md#regenerate-token) for `GH_PAT` if you lose it, but then you have to update that in the <code>Secrets</code> for all repositories using *GitHub* Build.

    ![copy fastlane access token on github](img/gh-token-to-copy.png){width="600"}
    {align="center"}

### Make up a Password

If you have not already made up a password, do it now and record it as <code>MATCH_PASSWORD</code>.

## Next Step

The next step is to [Prepare your Fork (Copy of LoopWorkspace)](prepare-fork.md).