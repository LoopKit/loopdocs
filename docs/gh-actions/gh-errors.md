## GitHub Build Method Errors

This method is fairly new so new errors are being captured as people use this method. Each time a new error is discovered, we try to update LoopDocs to make it easier for the next person to succeed without errors.

If you've been around Loop for a while, you know the mantra about screen shots. Well, for GitHub Build Action Failures, **screen shots are close to useless**. If you get an error with an Action, you should use the search feature for known diagnosis strings. If you are still stuck then post your request for help along with your **GitHub username**. Mentors can go to your public LoopWorkspace fork - check that your branch is up to date and then view your Action log files directly.

But first - try to diagnose it yourself using this page.

## Most Common Mistakes

These are some of the most common errors to date.

* Make a spelling error when adding Secrets
    * Each secret must be spelled exactly the way it is presented in the instructions
* Save your Secrets, as directed, but use a smart editor instead of a text-only editor
    * It only takes one letter to be changed from lower-case to upper-case by your smart editor to ruin your day
    * The alpha-numeric values used for GH_PAT, FASTLANE_ISSUER_ID and FASTLANE_KEY contain both upper and lower-case characters and all the values are case-sensitive
* When entering TEAMID, make a spelling error in the value - please copy and paste instead of typing what you think you see
    * If you type in your TEAMID as 0123498989 when it is really 012349B989, you may not notice
        * Hint: what should have been the letter "B", got typed as the number "8"
    * The incorrect TEAMID will show up in your identifiers as the Bundle ID but . . .
        * You will not be able to Create Certificates or Build Loop because your TEAMID does not match the Bundle ID
* Run the actions out of order or skip one

## Find Your Error

There is a separate section for each step in the process. First you must follow the [Examine the Error](#examine-the-error) instructions to view the record of the failed action. Then go to the section for the Action you were trying to complete to look for possible error strings to copy into the search box.

1. [Action: Verify Secrets](#action-verify-secrets-errors)
1. [Action: Add Identifiers Errors](#action-add-identifiers-errors)
1. [Action: Create Certificates Errors](#action-create-certificates-errors)
1. [Action: Build Loop Errors](#action-build-loop-errors) before successful build
1. [Repeat Build Loop Errors](#repeat-build-loop-errors) after successful build

If you discover a new error, please reach out to help us update the documentation.

## Examine the Error

It doesn't matter which action you are running; after the action completes, you will either see a green check mark for success or a red x mark for failure. The graphic below shows an example for the Add Identifiers action.

![graphic showing a success and a failure for a GitHub Add Identifiers action](img/action-result.svg){width="700"}
{align="center"}

If you click on the action name, it opens a secondary screen as shown below.

![graphic showing a success and a failure for a GitHub Add Identifiers action](img/action-result-secondary.svg){width="500"}
{align="center"}

Click on the top link to view the record of the failed action as shown in the graphic below. You will be pasting strings into the search box (highlighted with green rectangle) to look for a documented error. Please read the instructions below the graphic.

![graphic with failure details for a GitHub Add Identifier action](img/action-result-failure.svg){width="700"}
{align="center"}

* Paste in a possible error string (copy it exactly); repeat until you find a match
* If the possible error string is found - follow the directions for that error
* Still stuck?
    * Post for help including your GitHub **username**
    * With that, mentors can diagnose your problem - or at least made a good guess at what you need to try
    * Please **do not post a screenshot**

## Action: Verify Secrets Errors

A new action was added with Loop 3.1 to provide better error messages if something is wrong with your Secrets. In addition, the Actions are numbered to match the order in which they should be applied.

![actions shown for Loop 3.1 and newer versions](img/gh-actions-3.1.png){width="200"}
{align="left"}

To generate the graphic below, some items were deliberately set to be incorrect in the Secrets list. Representative error messages are shown when running the validate secrets action.

![representative messages with deliberate errors when running validate secrets](img/gh-validate-secrets.png){width="800"}
{align="center"}


## Action: Add Identifiers Errors

Use the [Examine the Error](#examine-the-error) instructions to find your error message.

There are two errors that we are familiar with at this point. Look for text matching what is listed below and view what has caused this error to be seen.

### Authentication credentials are missing or invalid

If you see:

* Authentication credentials are missing or invalid. - Provide a properly configured and signed bearer token, and make sure that it has not expired. Learn more about Generating Tokens for API Requests https://developer.apple.com/go/?id=api-generating-tokens

This can be caused by an error in the value (or spelling) of one of these keys:

* FASTLANE_ISSUER_ID
* FASTLANE_KEY_ID
* FASTLANE_KEY
* GH_PAT

!!! danger "Use a Text-Only Editor"
    If you used a "smart" editor when saving your Secrets in an archive file before pasting into the repository Secrets, it might have changed a lower case letter to an upper case letter.

    If even one character is capitalized when it should not be, you will not succeed at the Add Identifiers step.

### Invalid curve name

If you see:

* invalid curve name

This was caused by an error in the format of the value entered for the FASTLANE_KEY.

Make sure you copy in a text editor from the first hyphen to the last hyphen.


## Action: Create Certificates Errors

Use the [Examine the Error](#examine-the-error) instructions to find your error message.

### Wrong TEAMID in Secrets

Copy the words on the line below and paste it into the search function for your text editor.

`error: No profile for team '***' matching 'match AppStore`

If that phrase is found, then:

* You probably do not have the correct TEAMID entered in your Secrets
* The rest of these instructions assume:
    * You have already created a Loop App in the App Store with that incorrect TEAMID
    * This is true if you completed the steps after running Action: Add Identifiers and before Action: Create Certificates

Follow these steps - best to open each link below in a separate tab so you can return to this list and keep using the links in each step:

1. Delete all the identifiers that you can following the steps in [First Time: Delete Identifiers](gh-first-time.md#delete-identifiers)
    - You will not be able to delete the Loop identifier with the wrong TEAMID, but don't worry about it

1. Enter your TEAMID correctly in the repository Secrets
    - Make sure you use copy and paste from your [Apple Developer Membership](https://developer.apple.com/account/#!/membership) page for that TEAMID.
    - Follow the update instructions here (this example is for GH_PAT, you'll do the same but for TEAMID) [Update Secrets](gh-update.md#update-secrets)

1. Run Action: [First Time: Add Identifiers](gh-first-time.md#add-identifiers) again

1. Follow all the steps in this section with the Correct TEAMID [First Time: Configure Identifiers for Loop](gh-first-time.md#configure-identifiers-for-loop) but when you get to the [First Time: Create Loop App in App Store Connect](gh-first-time.md#create-loop-app-in-app-store-connect), you need to return to this page and follow the instructions below to remove the app and add a new one.

The first time through, you created an app with a `Bundle ID` that does NOT include your TEAMID.

You will remove that app and create a new one.

#### Remove App with Incorrect TEAMID

Go to [App Store Connect / Apps](https://appstoreconnect.apple.com/apps) and follow the numbered steps in the graphic below.

1. Find the Loop app you created earlier and click on it
2. On the left side, under General, click on App Information
    * Confirm that the value listed under Bundle ID is the incorrect one
    * The Bundle ID says: com.NOT_YOUR_TEAMID.loopkit.Loop
3. Scroll to the bottom of the page and tap on `Remove App`
4. The dialog box, similar to the one in the graphic below, should appear and you tap Remove
    * After the App is removed, you'll see a very similar screen, where you can tap on `Restore App`
5. But since you want that App removed, tap on Apps at the very top of the screen and proceed to the next step

![graphic with steps to remove and app from app store connect](img/delete-app-bad-bundle-id.svg){width="700"}
{align="center"}

That App with the wrong bundle ID remains in the App store but it is hidden so it won't confuse you.

#### Add App with Correct TEAMID

Now click on the Add Apps button or the + sign if you have other apps in the store.

Follow the [First Time: Create Loop App in App Store Connect](gh-first-time.md#create-loop-app-in-app-store-connect) directions with these additions:

* You must come up with a new name for your Loop App
* Triple check that the Bundle ID you choose is for Loop and has your TEAMID embedded, it should look like: com.TEAMID.loopkit.Loop
* You must come up with a new SKU for your Loop App (try 1234, if you used 123 before)

#### Create Certificates

You should be able to continue with the First Time Steps to Create Certificates and then Build Loop and keep going.



### Missing Repository Access

Copy the words on the line below and paste it into the search function for your text editor.

`Error cloning certificates git repo, please make sure you have access to the repository - see instructions above`

or 

`Error cloning certificates repo, please make sure you have read access to the repository you want to use`

If you see this phrase, the `fastlane` package that is utilized during the `3. Create Certificates` action cannot access your repository to create certificates for your Loop app. This is due to insufficient repository access rights that were not granted during the creation of your `GH_PAT` token.

To fix this error:

- Open this link: [https://github.com/settings/tokens/](https://github.com/settings/tokens/)
  - Here you will see your personal access token (`Fastlane Access Token`) that was created during [First Time: Setup GitHub: Create GH_PAT](gh-first-time.md#create-gh_pat)
  - Note that Tokens (classic) is highlighted in the menu on the left
  - Click on the token name (should be bold, blue **Fastlane Access Token** ) to open its detail page
  - None of the checkboxes under **Select Scopes** will be checked – this is what's causing the issue.
  - Add a check beside the `repo` permission scope (see red circled checkbox in graphic)
  - Scroll all the way to the bottom and click `Update token` (it's a long way, ignore all other settings, do not check anything else)

![graphic showing missing repo scope with circled checkbox that user must check](img/gh-missing-repo-scope.png){width=700}

After you have clicked `Update token` you should see the token overview again with a message `Some of the scopes you’ve selected are included in other scopes. Only the minimum set of necessary scopes has been saved. ` (You can dismiss the message using the X near the upper right side if it appears).

#### Create Certificates

You should be able to continue with the [First Time Steps to Create Certificates](gh-first-time.md/#create-certificates) and then proceed from there with Build Loop and keep going.



## Action: Build Loop Errors

!!! warning "Run Create Certificates First"
    You must run Action: Create Certificates before attempting to run Action: Build Loop

Use [Examine the Error](#examine-the-error)

* Download the log archive file and unzip it
* Open the `1_build.txt` file
* Search for the phrase below

For each Build Loop Error section below, copy the phrase into the search function of your text editor. If you find it, solve that error. If not, move on to the next one.

### Could not find an app on App Store Connect

Copy the words on the line below and paste it into the search function for your text editor.

`Could not find an app on App Store Connect`

If that phrase is found, then:

* Make sure you completed the [Create Loop App in App Store Connect](gh-first-time.md#create-loop-app-in-app-store-connect) Step
    * Once you've resolved that step, run these Actions again:
        * Create Certificates
        * Build Loop


* This can also be caused if you correctly created the Loop App but entered an incorrect value for the TEAMID.
    * If you have the incorrect TEAMID, check this link: [Certificates, Identifiers & Profiles](https://developer.apple.com/account/resources/identifiers/list) for entries with the incorrect TEAMID embedded
    * For example, if your TEAMID is 0123456789, but you entered 000123, you may see both of these in your identifiers list
        * com.0123456789.loopkit.Loop
        * com.000123.loopkit.Loop
    * Delete the "bogus" identifier version, fix your TEAMID and rerun all three steps:
        * Add Identifier
        * Create Certificates
        * Build Loop

### Error: Provisioning Profile

Copy the words on the line below and paste it into the search function for your text editor.

`error: Provisioning profile "match AppStore`

If that phrase is found one, or more times, it means you missed a step when configuring the Loop identifier or missed associating your Loop App Group with one or more identifiers.

For example, if you see:

* `error: Provisioning profile "match AppStore com.***.loopkit.Loop" doesn't include the com.apple.developer.usernotifications.time-sensitive entitlement.`

Go back to [First-Time: Add or Review Configuration for Loop Identifier](gh-first-time.md#add-or-review-configuration-for-loop-identifier) and make sure you enabled the Time-Senstive notification for Loop.


For example, you might see:

* `error: Provisioning profile "match AppStore com.***.loopkit.Loop.SmallStatusWidget`
* `error: Provisioning profile "match AppStore com.***.loopkit.Loop.statuswidget`
* `error: Provisioning profile "match AppStore com.***.loopkit.Loop.Loop-Intent-Extension`

Return to [Add App Group to Other Identifiers](https://loopkit.github.io/loopdocs/gh-actions/gh-first-time/#add-app-group-to-other-identifiers) and fix the missing items.

You must create certificates again before you can build:

* Action: Create Certificates
* Action: Build Loop

### A new one cannot be created because you enabled

Copy the words on the line below and paste it into the search function for your text editor.

`A new one cannot be created because you enabled`

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

This tells you, the bundle ID you selected in [First-Time: Create Loop App in App Store Connect](gh-first-time.md#create-loop-app-in-app-store-connect) does NOT have your TEAMID embedded in the name.

Once you've created an app in the App Store that is not based on your TEAMID, you cannot delete it, but you can Remove it, so you don't click on it by accident.

1. Open this link: [App Store Connect / Apps](https://appstoreconnect.apple.com/apps) to view your apps; log in if needed.
1. Find the App with the wrong Bundle ID and click on it
1. On left hand side, click on App Information (under General)
    * Confirm the Bundle ID listed does not include your TEAMID
    * Scroll all the way to the bottom
    * Tap on Remove App
    * New dialog window appears, select Remove

At this point, get your correct TEAMID, fix your Secrets file to have the correct TEAMID and then return to [First-Time: Configure Secrets](gh-first-time.md#configure-secrets). This time you will be updating TEAMID in the repository secret list.


## Repeat Build Loop Errors

This section is only for people who have successfully built using GitHub Build Actions.

Use the [Examine the Error](#examine-the-error) instructions to find your error message.

### Could not install WWDR certificate

Assuming you have successfully built using the GitHub method before:

* If the details show this message, "Could not install WWDR certificate", make sure your developer account is in good standing and that there are no agreements that need to be accepted
* Sometimes this is a sign that Apple did not respond to a request, this failure happens in the first few minutes
    * Repeat the build and it should be fine the next time

![graphic showing failure to install certificate](img/github-error-cert-failed.png){width="500"}
{align="center"}

## Starting Over

This is not the first thing to try, but sometimes it is the best approach.

!!! danger "Totally Frustrated"
    The directions on the [GitHub First Time](gh-first-time.md) page have been improved.

    If you tried this earlier and did not make progress, you can delete the Match-Secrets repository and LoopWorkspace fork in your GitHub account. Make sure your Secrets are all correct and consistent, then start over at [First-Time: Create Match-Secrets](gh-first-time.md#create-match-secrets) and keep going. It will go much faster this time.
    
    * Instructions to delete a repository are found at [GitHub Docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository)
