## Help with Errors

!!! important "Get Help, Not Frustrated"
    For first-time builders, there are a lot of one-time steps that all have to be correct and many screens look similar.

    If you are updating your build, the process can be confusing and some error messages can be misleading.

    You are not alone - please reach out.

If you are having trouble:

#### Please DO:

* Use the LoopDocs search feature
* Use the zulipchat or Facebook search feature
* [Ask a mentor for help](#where-to-get-help-with-browser-build)

#### Please do NOT:

* Search in a general internet browser to find your error
* Ask ChatGPT (or other AI) how to fix your error
* Spend hours in frustration
* Rename or delete a repository
* Delete your GitHub account
* Remove your App from App Store Connect

### Where to Get Help with Browser Build

These are two places to ask for help, but please choose only one. You may get a faster response from Facebook, but there are mentors on both sites:

* [LoopandLearn Facebook Group](https://www.facebook.com/groups/LOOPandLEARN){: target="_blank" }
* [Zulipchat: Loop: Build Help]( https://loop.zulipchat.com/#narrow/channel/148543-Loop/topic/Browser.20Build){: target="_blank" }

### What Information is Needed for Help

1. Your GitHub name used for building (required):

    * Best to provide a link to your repository, like the example, but substitute your information
    * If you are building an app other than Loop, replace LoopWorkspace with the app repository name

    ``` {.text .copy  title="If you use an organization" }
    https://github.com/my-name-org/LoopWorkspace
    ```

    ``` { .text .copy  title="If you do not use an organization" }
    https://github.com/my-name/LoopWorkspace
    ```

1. A brief summary of the step you are on and what isn't working.

That's all we need to get started.

Mentors can go to your public&nbsp;_<span translate="no">GitHub repository</span>_, make sure your code is up to date, examine your customizations (if any), then click on the Action tab and view your log files directly.

* Do not copy from the log file and post the words
* Do not take a screenshot of what you think is an error

!!! tip "GitHub URL, Not Pictures"
    If you've been around the DIY community for a while, you know the mantra about screenshots. Well, when using a browser to build, **screenshots are close to useless**.

    All that is needed to assist is your link to the *GitHub* repository where you are building.

## Quick Reference for Browser Build Errors

Please make this your first stop if you get any kind of an error with Browser Build.

### Link Styles

If you notice an arrow pointing up and to the right beside the link:

* This means a new tab or window (depending on your browser configuration) is opened when you click on the link
* Your original place in the docs is in the original tab, so you can return to your same position in the docs

If there is no upright arrow by a link, then the location is on the same page:

* Once you have read that section, hit the back arrow in your browser to return to your original location

### Look at the Annotation

If you get an error in an Action. Click on the link and scroll down to view the annotation. An example is shown below. Most errors have a clear annotation telling you what to do. If the annotation is not clear to your, please [ask a mentor for help](#where-to-get-help-with-browser-build).

![graphic with an example validate secret error](img/example-annotation.png){width="800"}
{align="center"}

### Rebuild or New Builder

* If you have successfully built before and this is a rebuild, skip ahead to [Rebuild Errors Quick Reference](#rebuild-errors-quick-reference)
* If you are a new builder, please continue reading

## New Builder: Quick Reference

### New Builder: Validate Secrets Error

This is the first step. If you have not succeeded (&#x2705;) with this action - STOP.

* No other action will work - because all the other actions repeat Validate Secrets as the first step of the action
* Be sure to [Look at the Annotation](#look-at-the-annotation)
* You can [ask a mentor for help](#where-to-get-help-with-browser-build)

If you want to try to solve it yourself, refer back to these section in the documentation:

* [Collect Secrets](secrets.md){: target="_blank" }
* [Enter the Secrets](prepare-fork.md#enter-the-secrets){: target="_blank" }

### New Builder: Add Identifiers Error

If you succeeded with Validate Secrets, this should also succeed. If it does not, please skip ahead to [Error: `missing a required attribute`](#error-missing-a-required-attribute).

Do not hesitate to [ask a mentor for help](#where-to-get-help-with-browser-build).

### New Builder: Create Certificates Error

This is one of the hardest ones to solve. If you are getting this, don't be afraid to [ask a mentor for help](#where-to-get-help-with-browser-build). If you want to solve it yourself, a link is coming your way but first read this:

#### This is NOT Your Error

When you start this action, GitHub starts a cloud computer to run your job for you. It doesn't have any information about you or your secrets - yet.

Early in the log file you will see two phrases in red font:

> There are no local code signing identities found.

> security: SecItemCopyMatching: The specified item could not be found in the keychain.

This is normal. The next steps will set up a keychain for you using your Match-Secrets repository and your MATCH_PASSWORD passphrase.

#### Where to find the Certificate Solutions

Head over to [Action: Create Certificate Errors](#action-create-certificates-errors) and find your specific error.

### New Builder: Build Errors

The most likely reason to get errors here is a mistake in the [Prepare App](prepare-app.md){: target="_blank" } page. 

Common errors are:

* You skipped one of the Identifiers when adding the App Group to it
* The App Group was spelled wrong
* You unchecked a capability on one of the Identifiers (because you watched an old video)
* You did not select the correct identifier when creating your app
* You entered an incorrect TEAMID

All of these solutions are found in [Action: Build Loop Errors](#action-build-loop-errors). The mentors can pick out the exact solution quickly if you [ask a mentor for help](#where-to-get-help-with-browser-build).

An example annotation for skipping one of the Identifiers is shown in the graphic below. The App Group for `Loop-Intent-Extension` was deliberately removed to provoke that error.

![graphic with an example build error](img//example-identifier-build-errors.png){width="800"}
{align="center"}

Ignore the warnings - this does not affect the build.


## Rebuild Errors: Quick Reference

### `Check Upstream and Keep Alive` Error

!!! important "`Check Upstream and Keep Alive` Error"
    **Error**: Your Browser Build fails and when you click on the link, you see

    * **`Check Upstream and Keep Alive`** failed

    **Consequence**: any required sync of your fork is skipped and build is skipped

    **Solution**:

    * Manually sync your fork of the repository: [Update `Fork`](bb-update.md#update-fork){: target="_blank" }
    * Manually start your build: [Build](bb-update.md#build-the-app){: target="_blank" }

    **Details about what happened**:

    On 21 April 2025, *GitHub* removed one of the third-party repositories that we used to keep automatic building going without action on your part. The repository was removed because it was in violation of the *GitHub* terms of service. *GitHub* disables automatic actions for repositories that have been inactive (no commits added in 60 days). For stable apps, like the *Loop* app, this third-party repository enabled a workaround to keep the builds happening.

    This affected all the Open-Source apps in our community - Loop, LoopFollow, LoopCaregiver, Trio, iAPS and xDrip4iOS. The developers in our community have restored the ability to build using the Browser Build method. Stay tuned for updates to required actions in the documentation over the next few months, before we hit the 60 day limit.

### Manual Enable for Build Action May be Required

The automatic build actions continue to happen on schedule, but starting May 2025, you may find your build action disabled by *GitHub*. (This might happen every 60 days, but it might happen sooner.) In that case, no build actually happens, no warning email is sent and a green checkmark (&#x2705;) appears beside a very short build action in which the actual build was skipped.

If necessary, enable the build action at your repository as shown in the graphic below and then launch a manual build.

![fix a disabled build state](img/build-disabled-fix.png )

### Rebuild: Create Certificates Error

With `Loop 3.6.0`, these should be a thing of the past - but you must first manually update (sync) your repository in order to get this feature added and you must do this new step [Add Variable](prepare-fork.md#add-variable){: target="_blank" }

> Caveat - your Apple Developer account must be in good standing with a valid credit card attached and all agreements signed.

### Rebuild: Build Error

After you update to `Loop 3.6.0`, the Create Certificates Action is incorporated into the Build Action. So for rebuilders, if you completed the manual sync and added the new variable, you should not get an error when building.

> Caveat - your Apple Developer account must be in good standing with a valid credit card attached and all agreements signed.

There are, however, a few intermittent errors that can happen when *GitHub* and *Apple* don't communicate for some reason or there is a problem with the *TestFlight* upload. Check out [Action: `Build Loop` Errors when Updating](#action-build-loop-errors-when-updating).

## Most Common Mistakes

If you get an error when building with a browser, you can use this page to figure out what to do - but don't be afraid to [ask for help](#help-with-errors).

!!! important "Certificate is missing"
    If you get this build error message: `No code signing identity found and can not create a new one because you enabled`, you do not have certificates needed to run the build.

    * With `Loop 3.6.0` and newer, this should not happen. Make sure you [Add Variable](prepare-fork.md#add-variable){: target="_blank" } to automatically renew certificates.

These are some of the most common errors to date.

1. You made a spelling error when adding <code>Secrets</code>
    * Each secret must be spelled exactly the way it is presented in the instructions
    * If you are using an automatic translation, please keep an original page open too and copy from it to make sure there are no spelling errors in the secret name
1. You made a spelling error in creating the `App Group Identifier` or did not add the `App Group Identifier` to all 4 of the required identifiers in this step: [Add `App Group` to `Identifiers`](prepare-app.md#add-app-group-to-identifiers){: target="_blank" }
    * See [Annotation without Clear Message (*Build*)](#annotation-without-clear-message-build) for an example of this kind of failure
1. You used a smart editor instead of a text-only editor to save your information
    * It only takes one letter to be changed from small to capital by your smart editor to ruin your day
    * The alpha-numeric values used for `GH_PAT`, `FASTLANE_ISSUER_ID` and `FASTLANE_KEY` contain both small and capital characters and all the values are case-sensitive
1. When saving `TEAMID`, you typed what you thought you saw instead of using copy and paste
1. You skipped running one of the actions
1. You need to sign a program license agreement or update a credit card at&nbsp;<span translate="no">Apple Developer</span>
    * Be sure to read [Misleading Error Message](#misleading-error-message)
1. You got an error regarding a branch with `alive` in the name
    * You can delete any branch that starts with the name `alive` and try again
    * See [Automatic Creation of `alive branch`](automatic.md#automatic-creation-of-alive-branch){: target="_blank" }

## Examine Annotation

If a&nbsp;<span translate="no">*GitHub* Action</span>&nbsp;fails, you will see a clear notification.

First consider the following results from the&nbsp;<span translate="no">*GitHub* Action: 1. Validate Secrets</span>.

### Annotation with Clear Message

Your screen may look similar to the graphic below. The name in parentheses refers to the branch used to develop these wonderful messages. Yours will almost always be the `main` branch.

![graphic showing failure to validate secrets](img/error-validate-secrets.png){width="500"}
{align="center"}

But there are so many reasons why this could happen. The first step is to click on the link highlighted by the red rectangle in the graphic above. This opens a new detailed view. The GIF below shows two different error messages. The first frame shows the error in the Annotation box at the bottom (you may need to scroll down to see this), and you may need to click on "Show More" to see the full message as seen in the second frame. The third frame of the GIF shows a different message. Each one these messages is designed to make it easier for you to diagnose your own problem.

![graphic showing validate secret error messages](img/error-annotations-validate-secrets.gif){width="800"}
{align="center"}

Notice that&nbsp;<span translate="no">*GitHub* Action: 1. Validate Secrets</span>&nbsp;is broken into three jobs each of which will either pass and show a green check or fail and show a red check. The secrets are validated with each action.

### Annotation without Clear Message (*Certificates*)

This section is left here for those who have an older version (3.4 or older) in their fork.

> If you have updated to 3.6.0 or newer, refer to [Rebuild Errors: Quick Reference](#rebuild-errors-quick-reference) and ignore this section.

Not all error messages had a clear annotation (up through version 3.4.x).

For example, the graphic below shows a failure of&nbsp;<span translate="no">*GitHub* Action: 3. Create Certificates</span>&nbsp;.

![graphic showing failure to create certificates](img/error-create-certs.png){width="800"}
{align="center"}

This is an example of a message that is not terribly descriptive - which is why it is shown here. In this case, you can click on just the one job that failed. There will be less to sort through to find your error. The most likely reason for this error is [Error: Could not Create](#error-could-not-create).

### Missing Certificates

> With `Loop 3.6.0` or newer, certificates are automatically renewed if your developer account is up to date, all agreements are signed and you completed the new [Add Variable](prepare-fork.md#add-variable){: target="_blank" } step.

If your certificates have expired, you will see this error when you try to build. It does not have a clear annotation. The error string starts with: `No code signing identity found and can not create a new one because you enabled`.

> The first automatic build when Loop 3.6.0 is released will update the files required for automatic certificate creation. The next automatic build will use the new files. So if the first attempt with Loop 3.6.0 fails, try again.

![graphic showing missing distribution certificate](img/missing-distribution-certificate.png){width="800"}
{align="center"}

### Annotation without Clear Message (*Build*)

The GIF below shows a failure of&nbsp;_<span translate="no">*GitHub* Action: 4. Build Loop</span>_&nbsp;. The nice messages have not been added to this yet - you will have to follow the [Find the Error](#find-the-error) instructions, but now, you are automatically taken to the correct section so there is less of the log to deal with.

* Frame 1 shows the failure message - click on one of the build links highlighted with the red rectangle (it does not matter which link you click)
* Frame 2 shows the screen displayed after you click the link - you will see the display automatically move to the first item that failed
    * The area indicated by the orange rectangle near the top right is where you will paste the strings offered in [Action: `Build Loop` Errors](#action-build-loop-errors)
* Frame 3 shows what happens when you paste in the correct string
    * Note that if the string is not found, nothing happens
    * If the string is found, the display automatically moves to the section of the log with that string
    * The particular `Identifier`, which does not have the required `App Group` for this example, is the SmallStatusWidget
        * Note that with version 3.4, SmallStatusWidget is no longer used - perhaps an unfortunate choice for this GIF

![graphic showing failure to create certificates](img/missing-app-group.gif){width="800"}
{align="center"}


## Find the Error

This section is required when you need to search for a string to diagnose and error that does not have a clear annotation.

### Misleading Error Message

If there are *Apple* Developer agreements you have not accepted, you may get errors when you try to Build that indicate your *Apple* <code>Secrets</code> are incorrect even if they are not.

* The misleading message tells you that one or more of these: <code>FASTLANE_ISSUER_ID</code>, <code>FASTLANE_KEY_ID</code> or <code>FASTLANE_KEY</code> is not correct
    * Once `Loop 3.6.0` or newer is available, this should no longer appear unless you have a mistake in one of those
* Check your *Apple* Developer account for agreements first, before trying to fix those `Secrets`
* If you previously built successfully - it is almost certainly the agreement
* It can take 15 minutes to an hour after the agreement is signed before it can be used

If you need detailed instructions, click on this [<code>Apple Program License Agreement</code> Help Page](https://support.pushpay.com/s/article/Accepting-the-Apple-Program-License-Agreement){: target="_blank" }.

You can also get this message if the credit card used to purchase the Developer account is not current, e.g., no longer valid or credit card expiration date, as entered at *Apple*, has passed.

### Find Your Error

At this point, it may be faster to [ask a mentor for help](#where-to-get-help-with-browser-build). But if you want to dig into the details of the log and find the error yourself, the information is here.

There is a separate section for each step in the process. First, you must follow the [Examine Annotation](#examine-annotation) instructions to view the record of the failed action. Then go to the section for the Action you were trying to complete to look for possible error strings to copy into the search box. For each section there are possible strings to paste to search the log.

* Paste in a possible error string (copy it exactly); repeat until you find a match
* If the possible error string is found - follow the directions for that error

Error annotations are available for the *Loop* app version 3.4 and later for some of the actions. We believe the first two actions have a complete set of error annotations.

1. [Action: `Validate Secrets`](#action-validate-secrets-errors)
1. [Action: `Add Identifiers` Errors](#action-add-identifiers-errors)
1. [Action: `Create Certificates` Errors](#action-create-certificates-errors)
1. [Action: `Build Loop` Errors](#action-build-loop-errors) before a successful build
1. [Action: `Build Loop` Errors when Updating](#action-build-loop-errors-when-updating) after a successful build

If you discover a new error, please reach out to help us update the documentation.

## Do Not Remove an App

Please do not remove an existing app if you have trouble building a different app. Your build error is not caused by any existing app.

!!! Important "Remove App Warning"
    If you remove an app and later want to restore that app, you might not be able to.

    Sad and Expensive Scenario:

    1. User removed app with name "My App" and unique bundle ID that includes their TEAMID
    1. User later decided to restore their app, but in the meantime, someone else has used the name "My App"
    1. When trying to restore your app, Apple doesn't allow you to change just the name of the app and will not allow you to restore it because someone else has that name, even though your bundle ID is different
    1. After spending time on the phone with Apple, user's only option was to purchase a new Apple Developer account so they can get a new TEAMID (see steps below) or doing a custom change to the Loop code to modify the bundle ID (no instructions are provided for this - easy to do it wrong)

## Instructions to Diagnose Your Errors

## Action: `Validate Secrets` Errors

For Version 3.4 and later - use [Examine Annotation](#examine-annotation) and read the annotation.

## Action: `Add Identifiers` Errors

### Error: `missing a required attribute`

This happens if your `FASTLANE_KEY` is invalid. You may have copied it incorrectly or there may be some other reason why the value that you correctly copied from your `p8` file is not working.

Copy the words on the line below and paste them into the search function for your action log.

> ``` { .text .copy }
> The provided entity is missing a required attribute - You must provide a value for the attribute
> ```

There were a number of cases recently where the solution was to revoke your `FASTLANE_KEY`, create a new one and then update these two secrets in your organzation, or in every repository if you are using a personal *GitHub* account to build.

* `FASTLANE_KEY`
* `FASTLANE_KEY_ID`

Before revoking your key, first make sure that when you saved them to your Secrets Reference file, there was not a mistake. Make sure you are NOT using a smart editor; that can change a small letter to a capital letter. Make sure you did NOT insert or remove a line break and that you copied from the first hyphen to the last hyphen. The 2 keys should look like this:

```
FASTLANE_KEY_ID
<looks like this>
AAAAAAAAAA

FASTLANE_KEY
<looks like this>
-----BEGIN PRIVATE KEY-----
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAA
-----END PRIVATE KEY-----
```

The `FASTLANE_KEY` can be taken from the `p8` file you downloaded. The other keys are all able to be copied again from your *Apple* Developer account page. See [Copy `API Key Secrets`](secrets.md#copy-api-key-secrets){: target="_blank" }.

If you decide to revoke the key and start again, see [Generate `API Key`](secrets.md#generate-api-key){: target="_blank" }. You will need to first revoke the existing `FASTLANE_KEY`:

* Select `Edit`
* Click on the checkbox beside `FASTLANE_KEY`
* Select `Revoke Key`

Then follow the normal steps detailed in that section to generate a new key and save the updated key and key ID in your Secrets Reference file and in your organization or repositories.

Do not hesitate to [ask a mentor for help](#where-to-get-help-with-browser-build).

## Action: `Create Certificates` Errors

> Reminder - If it is not obvious to you what your error is, please [ask a mentor for help](#where-to-get-help-with-browser-build)

> * you might get to the answer sooner
> * you are less likely to do something that makes it harder for the mentor to help you later

Review [Find the Error](#find-the-error) for instructions on how to use the error strings.

List of certificate errors on this page:

* [Error: No profile for team](#error-no-profile-for-team)
* [Error: Error cloning certificates](#error-error-cloning-certificates)
* [Error: Could not decrypt](#error-could-not-decrypt)
* [Error: Could not create](#error-could-not-create)
 
### Error: No profile for team

This happens if you entered the wrong TEAMID in `Secrets`.

Copy the words on the line below and paste them into the search function for your action log.

> ``` { .text .copy }
> error: No profile for team '***' matching 'match AppStore
> ```

If that phrase is found, then:

* You probably do not have the correct `TEAMID` entered in your `Secrets`
* The rest of these instructions assume:
    * You have already created a *Loop* App in the *App Store* with that incorrect `TEAMID`
    * This is true if you completed the steps after running Action: `Add Identifiers` and before Action: `Create Certificates`

Click on this link to [Delete Identifiers](#delete-identifiers).

- Delete all the other identifiers first, then try to delete the *Loop* identifier with the wrong <code>TEAMID</code>
- It is fine to just ignore identifiers with the wrong <code>TEAMID</code>, but do not use them

#### Rerun Steps with correct TEAMID

1. Enter your `TEAMID` correctly in the repository `Secrets`
    - Make sure you use copy and paste from your [Apple Developer Membership](https://developer.apple.com/account/#!/membership){: target="_blank" } page for that `TEAMID`.
    - Follow the update instructions here (this example is for `GH_PAT`, you'll do the same but for `TEAMID`) [Update Secrets](bb-update.md#update-secrets)

1. Run Action: [Configure to Use Browser: `Add Identifiers`](identifiers.md#add-identifiers) again

1. Follow all the steps in this section with the **correct** `TEAMID` [Configure to Use Browser: Configure Identifiers for Loop](prepare-app.md#configure-identifiers-for-loop) but when you get to the [Configure to Use Browser: Create Loop App in App Store Connect](prepare-app.md#create-loop-app-in-app-store-connect), you need to return to this page and follow the instructions below to remove the app and add a new one.

The first time through, you created an app with a `Bundle ID` that does NOT include your `TEAMID`.

You will remove that app and create a new one.

#### Remove App with Incorrect `TEAMID`

Go to [`App Store Connect / Apps`](https://appstoreconnect.apple.com/apps){: target="_blank" } and follow the numbered steps in the graphic below.

1. Find the *Loop* app you created earlier and click on it
2. On the left side, under `General`, click on `App Information`
    * Confirm that the value listed under `Bundle ID` is the incorrect one
    * The `Bundle ID` says: `com.NOT_YOUR_TEAMID.loopkit.Loop`
3. Scroll to the bottom of the page and tap on `Remove App`
4. The dialog box, similar to the one in the graphic below, should appear and you tap `Remove`
    * After the *App* is removed, you'll see a very similar screen, where you can tap on `Restore App`
5. But since you want that *App* removed, tap on `Apps` at the very top of the screen and proceed to the next step

![graphic with steps to remove and app from app store connect](img/delete-app-bad-bundle-id.svg){width="700"}
{align="center"}

That *App* with the wrong `Bundle ID` remains in the *App store* but it is hidden so it won't confuse you.

#### Add App with Correct `TEAMID`

Now click on the `Add Apps` button or the :heavy_plus_sign: (plus sign) if you have other apps in the *App Store*.

Follow the [Configure to Use Browser: Create Loop App in App Store Connect](prepare-app.md#create-loop-app-in-app-store-connect) directions with these additions:

* You must come up with a new name for your *Loop* App
* Triple-check that the `Bundle ID` you choose is for *Loop* and contains your `TEAMID`, it should look like: `com.TEAMID.loopkit.Loop`
* You must come up with a new `SKU` for your *Loop* App (try `1234`, if you used `123` before)

#### Create Certificates

You should be able to continue with the [Configure to Use Browser Steps to `Create Certificates`](certs.md#create-certificates) and then proceed from there with `Build Loop` and keep going.

### Error: Error cloning certificates

This indicates you do not have the appropriate Repository access.

Copy the words on the line below and paste them into the search function for your action log.

> ``` { .text .copy }
> Error cloning certificates
> ```

The full error looks like this:

> Error cloning certificates repo, please make sure you have read access to the repository you want to use

or

> Error cloning certificates git repo, please make sure you have access to the repository - see instructions above

If you see this phrase, the `fastlane` package that is utilized during the `3. Create Certificates` action cannot access your repository to create certificates for your *Loop* app. This is due to insufficient repository access rights that were not granted during the creation of your `GH_PAT` token.

To fix this error:

- Open this link: [https://github.com/settings/tokens/](https://github.com/settings/tokens/){: target="_blank" }
  - Here you will see your personal access token (`Fastlane Access Token`) that was created during [Configure to Use Browser: Setup *GitHub*: Create `GitHub Personal Access Token`](../browser/secrets.md#create-github-personal-access-token)
  - Note that `Tokens (classic)` is highlighted in the menu on the left
  - Click on the token name (should be bold, blue **`Fastlane Access Token`** ) to open its detail page
  - None of the checkboxes under **`Select Scopes`** will be checked – this is what's causing the issue.
  - Add a check beside the `workflow` permission scope (the graphic does not match the words, you want to use `workflow` to get both `repo` and `workflow` scope)
  - Scroll all the way to the bottom and click `Update token` (it's a long way, ignore all other settings, do not check anything else)

![graphic showing missing repo scope with circled checkbox that user must check](img/gh-missing-repo-scope.png){width=700}

After you have clicked `Update token` you should see the token overview again with the message `Some of the scopes you’ve selected are included in other scopes. Only the minimum set of necessary scopes has been saved. ` (You can dismiss the message using the `X` near the upper right side if it appears).

#### Create Certificates

You should be able to continue with the [Configure to Use Browser Steps to `Create Certificates`](certs.md#create-certificates) and then proceed from there with `Build Loop` and keep going.

### Error: Could not decrypt

Copy the words on the line below and paste them into the search function for your log file.

> ``` { .text .copy }
> decrypt the repo
> ```

The full error message is:

> `Couldn't decrypt the repo, please make sure you enter the right password`

If you know you entered the incorrect <code>MATCH_PASSWORD</code> in your repository <code>Secrets</code>, go and fix it now and try again.

Otherwise, you need to follow the steps to [Reset Match-Secrets](#reset-match-secrets).

### Error: Could not create

Copy the words on the line below and paste them into the search function for your log file.

> ``` { .text .copy }
> Could not create another Distribution certificate
> ```

The full error message is:

> `Could not create another Distribution certificate, reached the maximum number of available Distribution certificates`

#### New with `Loop 3.6.0`

> If you just updated to 3.6.0, you might not have added the new variable, `ENABLE_NUKE_CERTS`. Go do that now and then try again. It will take care of renewing your certificates automatically. See [Add Variable](prepare-fork.md#add-variable){: target="_blank" }.

These steps are only needed to make room for a `Certificate` when running versions earlier than 3.6.0 if you choose not to add the `ENABLE_NUKE_CERTS` variable:

1. Delete an old `Distribution Certificate`
    * *Apple* limits you to two `Distribution Certificates`
    * Use this link to view your [Apple Developer Certificates](https://developer.apple.com/account/resources/certificates/list){: target="_blank" }
        * Carefully examine the `Type` column - do **not** delete a `Development` `Certificate`
        * If you accidentally delete a `Development` `Type` certificate associated with an Xcode build for your Loop app - it will stop working and you will be very sad
    * Click on the oldest `Distribution` `Certificate` and revoke it
        * You will get an email informing you the certificate was revoked
1. To create a new `Certificate`:
    * Return to *GitHub* and your fork
    * Run the `Action`: `Create Certificates`
1. You are now ready to run the `Action`: `Build Loop`

!!! question "But what about *TestFlight* builds?"
    Previous builds using this method that are already in *TestFlight* are not affected by deleting the `Distribution Certificate`.

## Action: `Build Loop` Errors

This section is for people who have not successfully built the *Loop* app one time. If you are a repeat builder, please skip ahead to [Action: `Build Loop` Errors when Updating](#action-build-loop-errors-when-updating).

!!! warning "Run `Create Certificates` First"
    When running a version earlier than `Loop 3.6.0`, you must run Action: `Create Certificates` before attempting to run Action: `Build Loop`

    If you had to step backward and fix an `Identifier`, you must run `Create Certificates` again.

Refer to [Annotation without Clear Message (*Build*)](#annotation-without-clear-message-build) for a detailed example of these steps:

* Click on the Action log on *GitHub*
* There will be a series of green items followed by a red one
* Click on the red item to view the error
* Use the search function in this log to locate your error using one of the strings below

For each section below, copy the phrase into the search function of the log. If you find it, solve that error. If not, move on to the next one.

List of build errors in this section:

* [`Error: Could not find an app on App Store Connect`](#error-could-not-find-an-app-on-app-store-connect)
* [`Error: Provisioning Profile`](#error-provisioning-profile)
* [`Error: A new one cannot be created because you enabled`](#error-a-new-one-cannot-be-created-because-you-enabled)


### `Error: Could not find an app on App Store Connect`

Copy the words on the line below and paste them into the search function for your action log.

> ``` { .text .copy }
> Could not find an app on App Store Connect
> ```

If that phrase is found, then:

* Make sure you completed the [Create Loop App in App Store Connect](prepare-app.md#create-loop-app-in-app-store-connect) Step
    * Once you've resolved that step, run `Build Loop` action again


* This can also be caused if you correctly created the *Loop* App but entered an incorrect value for the `TEAMID`.
    * If you have the incorrect `TEAMID`, check this link: [Certificates, Identifiers & Profiles](https://developer.apple.com/account/resources/identifiers/list){: target="_blank" } for entries with the incorrect `TEAMID` embedded
    * For example, if your `TEAMID` is `0123456789`, but you entered `000123`, you may see both of these in your identifiers list
        * `com.0123456789.loopkit.Loop`
        * `com.000123.loopkit.Loop`
    * Delete the "bogus" identifier version, fix your `TEAMID` and rerun all three steps:
        * `Add Identifier`
        * `Create Certificates`
        * `Build Loop`

### `Error: Provisioning Profile`

Copy the words on the line below and paste them into the search function for your action log.

> ``` { .text .copy }
> error: Provisioning profile "match AppStore
> ```

If that phrase is found one, or more times, it means you missed a step when configuring the Loop identifier or missed associating your *Loop* App Group with one or more identifiers.

For example, you might see:

* `error: Provisioning profile "match AppStore com.***.loopkit.Loop`
* `error: Provisioning profile "match AppStore com.***.loopkit.Loop.LoopWidgetExtension`
* `error: Provisioning profile "match AppStore com.***.loopkit.Loop.statuswidget`
* `error: Provisioning profile "match AppStore com.***.loopkit.Loop.Loop-Intent-Extension`

Return to [First-Time: Identifiers for the `Loop` app](prepare-app.md#identifiers-for-the-loop-app) and make sure you followed all the steps.

You can build *Loop*:

* Action: `Build Loop`

### `Error: A new one cannot be created because you enabled`

Copy the words on the line below and paste them into the search function for your action log.

> ``` { .text .copy }
> A new one cannot be created because you enabled
> ```

If that phrase is found with lines similar to the following:

```
[31mA new one cannot be created because you enabled `readonly`[0m
[31mProvisioning profiles in your repo for type `appstore`:[0m
[31m- 'AppStore_com.NOT_YOUR_TEAMID.loopkit.Loop.statuswidget.mobileprovision'[0m
[31m- 'AppStore_com.NOT_YOUR_TEAMID.loopkit.Loop.SmallStatusWidget.mobileprovision'[0m
[31m- 'AppStore_com.NOT_YOUR_TEAMID.loopkit.Loop.mobileprovision'[0m
[31m- 'AppStore_com.NOT_YOUR_TEAMID.loopkit.Loop.LoopWatch.mobileprovision'[0m
[31m- 'AppStore_com.NOT_YOUR_TEAMID.loopkit.Loop.Loop-Intent-Extension.mobileprovision'[0m
[31m- 'AppStore_com.NOT_YOUR_TEAMID.loopkit.Loop.LoopWatch.watchkitextension.mobileprovision'[0m
```

This tells you, the `Bundle ID` you selected in [First-Time: Create Loop App in App Store Connect](prepare-app.md#create-loop-app-in-app-store-connect) does NOT have your `TEAMID` embedded in the name.

Once you have created an app in the *App Store* that is not based on your `TEAMID`, you cannot delete it, but you can Remove it (i.e. hide it so that it is no longer visible on this page and you don't accidentally click on it).

1. Open this link: [App Store Connect / Apps](https://appstoreconnect.apple.com/apps){: target="_blank" } to view your apps; log in if needed.
1. Find the App with the wrong `Bundle ID` and click on it
1. On the left-hand side, click on `App Information` (under `General`)
    * Confirm the `Bundle ID` listed does not include your `TEAMID`
    * Scroll all the way to the bottom
    * Tap on `Remove App`
    * New dialog window appears, select `Remove`

At this point, get your correct `TEAMID`, fix your Secrets file to have the correct `TEAMID` and then return to [First-Time: Configure Secrets](prepare-fork.md#configure-secrets). This time you will be updating `TEAMID` in the secret list.

## Action: `Build Loop` Errors when Updating

This section is only for people who have successfully built using *GitHub Build Actions*.

Use the [Examine Annotation](#examine-annotation) instructions to find your error message.

### `ERROR: Asset validation failed`

This error indicates your fork needs to be updated. As of 24 April 2025, you are required to use Xcode 16 to build the app. This is provided with `Loop 3.6.0` and newer versions.

There are serveral phrases you can check for. All of them have the same solution.

Copy the words on the line below and paste them into the search function for your action log.

> ``` { .text .copy }
> ERROR: Asset validation failed
> ```

> ``` { .text .copy }
> Could not download/upload from App Store Connect
> ```

Solution: Update your fork. See instructions on the Update page: [Update `Fork`](bb-update.md#update-fork){: target="_blank" }

### Intermittent TestFlight Upload Number Error

!!! warning "This is an intermittent error"
    Looking into history, we see that this error has been reported intermittently over the last few years.

Copy the words on the line below and paste them into the search function for your action log.

> ``` { .text .copy }
> Error: The provided entity includes an attribute
> ```

The full error looks like this: `Error: The provided entity includes an attribute with a value that has already been used The bundle version must be higher than the previously uploaded version: #`

Examine the number that is there. If it is 3, you need to use 4 in the Solution step. If it is 53, you use 54.

**Solution:** You must force Apple to update to a build number higher than the one it has on record.

Summary of what you will do (don't do it yet); there are detailed steps and graphics below:

1. You will edit the Fastfile in your `fork` and save the changes to a new `patch` branch
3. Perform the Action to `Build Loop` and select the `patch` branch when you build

> There is no reason to expect subsequent builds to fail with this same error, but if it does, repeat this section.

#### Prepare your `fork`

The graphic below shows the steps to make sure your `fork` is up to date and to locate the `fastfile` folder:

1. Select the `branch` that you plan to build
2. Check the `fork` for that `branch` is up to date
    * If it is behind, `sync` the fork
3. Scroll down to locate the folder `fastlane` and click on it (next graphic)

    ![Graphic shows steps to get fork up to date and locate fastfile](img/tf-build-number-error-01.svg){width="750"}
    {align="center"}

#### Prepare to Edit your Fastfile

1. After clicking on the `fastlane` folder, 3 files are visible; click on `Fastfile`
3. When the `Fastfile` file opens click on the pencil icon so you can edit the file

![Graphic shows steps to select and edit fastfile](img/tf-build-number-error-02.svg){width="750"}
{align="center"}

#### Edit your Fastfile

1. Type either ++command+"F"++ (Mac) or ++control+"F"++ (PC) to reveal the find and replace dialog shown in the graphic below
    * Copy the phrase indicated below and paste it into the find buffer, and then type into the replace buffer the build number you want to require (one more than indicated by your last error)

    ``` { .txt .copy }
    previous_build_number + 1
    ```

2. Tap on the `Find` button and the `Replace` button to make 2 changes to the file
3. After modifying the two lines, click on the `Commit changes` button at upper right

![Graphic shows steps to edit fastfile](img/tf-build-number-error-03.svg){width="750"}
{align="center"}

#### Save to a Patch Branch

Refer to the graphic below. The number `3` by the `Commit changes` button indicates the selection made in the previous step; it is shown for reference.

1. Tap on indicator that you will save to a new branch - *GitHub* will automatically name it for you
2. Tap on `Propose changes` button and then STOP; do not click on `Open pull request` - you are done with this step

![Graphic shows steps to edit fastfile](img/tf-build-number-error-04.svg){width="750"}
{align="center"}

#### Build using Patch Branch

Select `Action: Build Loop`

Refer to the first graphic below:

* Tap on Run Workflow (on the right side)
* Tap on the dropdown arrow to the right of the default `branch`
* Choose the `branch` you just created
    * Start to type `patch` in the `branch` selection dropdown
    * Only `branches` with that phrase will be displayed
* After you have the correct `branch` selected, tap on run workflow

![select the branch branch to build](img/tf-find-patch.png){width="400"}
{align="center"}

There is not a lot of indication that the build started - be patient - or refresh the screen - do NOT start another build. Your build status should be similar to the next graphic.

![build is in progress](img/tf-workflow-running.png){width="700"}
{align="center"}

Once you get a successful build, you return to using your normal `branch` for future builds.

> There is no reason to expect subsequent builds to fail with this same error, but if it does, repeat this section.

### `Could not install WWDR certificate`

Assuming you have successfully built using the Browser-Build / *GitHub* method before:

* If the details show this message, `Could not install WWDR certificate`, make sure your [*Apple developer* account](https://developer.apple.com){: target="_blank" } is in good standing and that there are no agreements that need to be accepted and that your `Distribution Certificates` did not expire
* Sometimes this is a sign that *Apple* did not respond to a request, this failure happens in the first few minutes
    * Repeat the build and it should be fine the next time

![graphic showing failure to install certificate](img/github-error-cert-failed.png){width="500"}
{align="center"}

## Extra Sections

It is unlikely you will need these sections.

### Reset `Match-Secrets`

This is not the first thing to try, but sometimes it is the best approach.

There might be several reasons to do this:

* You lost your <code>MATCH_PASSWORD</code> and want to build one of the [Other Apps](other-apps.md)
* You thought you entered the correct <code>MATCH_PASSWORD</code> but you are getting [Error: Could not decrypt](#error-could-not-decrypt)
* You are having trouble renewing your certificates after using Browser Build for a year

These steps are needed to reset your `Match-Secrets`:

1. Delete your `Match-Secrets` `Repository`
    * Instructions to delete a repository are found at [*GitHub* Docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository){: target="_blank" }
1. In your fork of LoopWorkspace:
    * This will automatically create a new `Match-Secrets` `Repository` for you
    * Run the `Action`: `Create Certificates`
    * If this fails, click on this link for the most likely [Error: Could not create](#error-could-not-create)
    * If that doesn't help, check all your <code>Secrets</code> and try again
1. You are now ready to run the `Action`: `Build Loop`

!!! important "Other Apps"
    All DIY iOS apps that have an associated <code>*GitHub* Browser Build</code> method require the same 6 <code>Secrets</code>.

    If you add an app to your *GitHub* username (by forking the repository and adding <code>Secrets</code>) and then build it, it encrypts your `Certificate` using `MATCH_PASSWORD`.

    If you already have the other apps configured and then you delete `Match-Secrets` and add a new one, you will need to run `Create Certificates` for each app before the next time you build each app - go ahead and do that now so you don't forget.

### Delete Identifiers

These instructions are useful if:

* You messed up your TEAMID when initially setting up your app and you want to remove identifiers that may be confusing
* You built an app but no longer want it, and want to clean up the list of identifiers so it is shorter

The `Identifier` that is associated with the `Loop` identifier cannot be deleted if it is already in the *App Store* but all others can. If you attempt to delete the `XC` *Loop* identifier, you may be told it cannot be deleted because it is in use in the app store. That's OK. If a `Bundle ID` has ever been associated with an app in the *App Store*, you cannot delete the `Identifier`.

* Open this link: [Certificates, Identifiers & Profiles: Identifiers List](https://developer.apple.com/account/resources/identifiers/list){: target="_blank" } on the *Apple Developer* site.
* Use the graphic below as a guide to removing identifiers
* Keep repeating the steps until you've removed all the identifiers you can (or want to) delete
* It is OK to delete an identifier even if it does have your correct `TEAMID`
    * If you try to delete the `Loop` identifier with your `TEAMID`, it will refuse, don't worry, just keep going
* Note - this graphic indicates where on this page you can find your `TEAMID`
    * If you notice an identifier with a value embedded in it that does not have your `TEAMID`, then delete it if you can and [Update <code>Secrets</code>](bb-update.md#update-secrets){: target="_blank"} with your correct `TEAMID`
    * If you try to delete a Loop identifier that does not have your `TEAMID`, but you already added to the *App Store*, it will refuse, don't worry, just keep going
    * Delete all the other identifiers first that have the same incorrect `TEAMID` and then try to delete the Loop identifier with the incorrect `TEAMID`

![steps to delete a given identifier](img/delete-identifiers.svg){width="700"}
{align="center"}

If coming here because you enter the wrong `TEAMID` in `Secrets` - return to [Rerun Steps with Correct TEAMID](#rerun-steps-with-correct-teamid) when you've deleted as many identifiers as you can.

After you delete identifiers, you must add them back before you can build a given app. Configure them and build again.

### New Developer ID with Same GitHub Account

You can use the same GitHub account with a new developer ID. This is an uncommon scenario, but if you lost access to the developer ID you used to use, you can modify your *GitHub* account to use a new one. Remember - this will be a new app, requiring you to enter your settings fresh and add your pump again. (New pod required if using Omnipod.)

Here are the steps:

1. Update the 4 secrets that are associated with the Apple Account for each repository on the GitHub used for browser build:
    * TEAMID
    * FASTLANE_ISSUER_ID
    * FASTLANE_KEY_ID
    * FASTLANE_KEY
1. Once the Secrets are updated, start at the [Identifiers](identifiers.md){:target="_blank"} page and work through the process for each app
