## Overview

???+ info "Time Estimate (click to open/close)"
    - Update your configuration for automatic builds: 10 minutes
    - Update your fork: 5 minutes
    - Follow the extra instructions to get &nbsp;<span translate="no">Loop</span>&nbsp;ready to build: 10 minutes
    - Start the Build process: 30 seconds
    - Wait for build to complete and appear in &nbsp;<span translate="no">TestFlight</span>&nbsp;on your phone
        * about an hour
        * depends on &nbsp;<span translate="no">GitHub</span>, <span translate="no">Apple</span>&nbsp;and &nbsp;<span translate="no">TestFlight</span>

???+ abstract "Page Summary (click to open/close)"
    **You must build the app every 90 days when you build with a browser - this is a&nbsp;<span translate="no">TestFlight</span>&nbsp;requirement.**

    The default settings on these pages configure automatic build as part of the update to Loop 3.4: see [Update with Browser](#update-with-browser).

    * If you do not want automated builds, review [Modify Automatic Building](#modify-automatic-building)

    If you are running Loop-dev, be sure to review [GitHub Build for dev](#github-build-for-dev).

???+ question "FAQs (click to open/close)"
    - **Do I need a computer?** No.
    - **Did the directions change?** Yes. With the release of 3.4, we recommend you configure for automatic update and build. You should not need to visit this page again with released code.
    - **What if I don't want automatic update or automatic build?** See this section [Modify Automatic Building](#modify-automatic-building)
    - **What happens to my existing builds if I change my&nbsp;<span translate="no">GitHub Personal Access Token</span>?** Nothing. It only affect future builds. Previous build will be available for the full 90 days.

## Update with Browser

!!! abstract "Summary of Update Steps"
    * [Accept Agreements](#accept-agreements)
    * [Update Fork](#update-fork)
    * [Build Loop](#build-loop)
    * [Wait for &nbsp;<span translate="no">TestFlight</span>](#wait-for-testflight)
    * [Install or Confirm Installation](#install-or-confirm-installation)

    Ignore the email that says you need to fix "issues" in your app. You are not selling the app in the app store; so no action is required. The app you built is for personal use for you or a family member.

### Accept Agreements

Sign in to your [<span translate="no">Apple Developer</span>&nbsp;account](https://developer.apple.com/account). If there are agreements you have not accepted, your build will fail and you'll see an [<span translate="no">Annotation</span>&nbsp;Message](gh-errors.md#annotation-message) telling you to accept your agreement.

If you need detailed instructions, click on the [<code>Apple Program License Agreement</code>](https://support.pushpay.com/s/article/Accepting-the-Apple-Program-License-Agreement) help page.

* Accept the `Apple Program License Agreement` (only)
    * You do NOT need to accept anything related to the `Paid Applications Schedule Agreement`
    * That is only required when you sell an app through the `App Store`

!!! warning "Wait After You Agree"
    It typically takes 15 minutes before your updated agreement is available so you can complete your build.

    If your build with browser fails, wait longer. An hour wait was reported by one person.

### Update Fork

Open your &nbsp;<span translate="no">GitHub</span>&nbsp;account and select your LoopWorkspace repository from your repositories list.

#### Special Instructions for &nbsp;<span translate="no">Loop</span>&nbsp;3.4

When updating from&nbsp;<span translate="no">Loop</span>&nbsp;3.2.x to 3.4, you will need to take some extra steps. Once those steps are completed, your &nbsp;<span translate="no">Loop</span>&nbsp;app will be automatically updated and automatically built at least once a month.

!!! question "Can I Opt Out?"
    Yes - you can opt out of the automatic build.

    * The default instructions configure automatic update and automatic build
    * The instructions to opt-out of some or all of these automations start at [Modify Automatic Building](#modify-automatic-building)

Here is a summary of the extra steps; each step has an associated link. You need to do all of them.

1. Confirm the status of your &nbsp;<span translate="no">GitHub Personal Access Token</span>
    * Recommended permission scope is `repo, workflow` and set to never expire
    * You can check this using directions at [<span translate="no">GitHub Personal Access Token</span>](#github-personal-access-token)
1. Follow the directions for [Manual Update](#manual-update) for your fork
1. This list is repeated in the [Build Loop](#build-loop) section along with detailed instructions
    * Add and Update New Indentifier
    * Create Certificates
    * Build Loop

#### Manual Update

![message displayed when your fork of LoopWorkspace is behind LoopKit version](img/github-build-check-fork-status.svg){width="700"}
{align="center"}

* If your fork is up to date with LoopKit version, you will see the message `This branch is up to date with LoopKit/LoopWorkspace:{branch}` - there is no need to build again unless your Loop app in &nbsp;<span translate="no">TestFlight</span>&nbsp;is about to expire - in which case, proceed to [Build Loop](#build-loop)
* If your fork shows a message such as `This branch is 3 commits behind LoopKit:main` and you want to update and build, then click `Sync Fork` by tapping where the red rectangle is shown in the graphic above, then in the pop-up window, tap on `Update branch`
* If your fork shows a message such as `This branch is 3 commits behind LoopKit:main and 4 commits ahead of LoopKit:main`; you might need to manually sync and choose to `discard changes`; you can always customize again after the update

!!! question "Building a different branch"
    Do I need to do anything special to build a different branch?

    Yes: please follow instructions at [GitHub Build for dev](#github-build-for-dev)

### Build Loop

If you have successfully built Loop 3.4 with automatic build configuration enabled and later decide to manually build Loop, all that is required is to run the action: Build Loop for your fork and skip ahead to [Wait for TestFlight](#wait-for-testflight).

#### Updating from 3.2.x to 3.4

For the update from 3.2.x to 3.4, you must do a few more actions than normal, but you will get automatic updates and builds in the future.

#### Add and Update New Identifier

The `bundle ID` for the "`widget`" changed from "`SmallStatusWidget`" to the more descriptive "`LoopWidgetExtension`". You need to run Add Identifier, wait for it to succeed and then add the `App Group` to this one new Identifier, shown in the table below.

All other identifiers should be already set up. If they are not, please go through the steps on the [GitHub First Time](gh-first-time.md) page to figure out what you are missing.

| `NAME` | `IDENTIFIER` |
|-------|------------|
| `Loop Widget Extension` | `com.TEAMID.loopkit.Loop.LoopWidgetExtension` |

* Open the [Certificates, Identifiers & Profiles: Identifiers List](https://developer.apple.com/account/resources/identifiers/list) page.
* Click on the "`LoopWidgetExtension`" identifier
* Edit the App Group to include `group.com.TEAMID.loopkit.LoopGroup` where you use your `TEAMID`

#### Create Certificates and Build

You must create certificates again to cover the new Identifier name and to provide support for the addition of the Libre sensors. (This step is required whether you use Libre or not - Loop needs permission to have that capability). Once the certificate action succeeds, then run the action to build Loop.

1. Run the Action for Create Certificates
1. Run the Action for Build Loop

### Wait for &nbsp;<span translate="no">TestFlight</span>

You'll receive an App Store Connect email confirming that the build has completed processing, and a &nbsp;<span translate="no">TestFlight</span>&nbsp;email confirming the new app is ready to test.

* If you get an email that the action failed, then return to your repository and look for Build Action error messages
    * Click on the most recent Build job with the red x by it
    * If the details show this message, "[Could not install WWDR certificate](gh-errors.md#could-not-install-wwdr-certificate)"
         * This means _<span translate="no">Apple</span>_ did not reply to &nbsp;<span translate="no">GitHub</span>&nbsp;as fast as &nbsp;<span translate="no">GitHub</span>&nbsp;expected
         * Make sure your developer account is in good standing and that there are no agreements that need to be accepted
        * Repeat the build (previous step)

The updated app will show up in your&nbsp;<span translate="no">TestFlight</span>&nbsp;app.

* Your new app will have "Expires in 90 days"
    * It takes time for the update to show up in the&nbsp;<span translate="no">TestFlight</span>&nbsp;app
    * There may be older builds that are still in&nbsp;<span translate="no">TestFlight</span>
* You will also see a build number in parentheses, that number increments each build

### Install or Confirm Installation

#### TestFlight Automatic Update Disabled

Option 1: If you chose to [Disable Automatic Install from&nbsp;<span translate="no">TestFlight</span>](../gh-actions/gh-deploy.md#disable-automatic-install-fromtestflight) for Loop, you choose when to install the app on the phone.

* Open&nbsp;<span translate="no">TestFlight</span>&nbsp;on your phone and click `Install` as shown in the GIF below
* If you are building for a child, follow the&nbsp;[<span translate="no">TestFlight</span>&nbsp; for Child](gh-deploy.md#testflightfor-child) instructions again

![install Loop from &nbsp;<span translate="no">TestFlight</span>](img/testflight-install-loop.gif){width="300"}
{align="center"}

#### TestFlight Automatic Update Enabled

Option 2: If you chose to leave [TestFlight Automatic Updates](../gh-actions/gh-deploy.md#testflight-automatic-updates) enabled for Loop, the updated build will be installed over your existing app.

* In this case, when you look at the&nbsp;<span translate="no">TestFlight</span>&nbsp;app on your phone, the app should have installed automatically
* Refer to the GIF above, the message will say `Open` instead of `Install`

## <span translate="no">TestFlight</span>&nbsp;Expiration Warning

For version 3.3.0 and newer, the usual [<span translate="no">Loop</span> expiration notification system](../operation/features/notifications.md#loop-app-expiration-notification) alerts the user when the app is within 20 days of expiration. In addition to that modal alert, the user can examine the bottom of the Settings screen at any time to see the expected expiration date and time.

![expiration warning on settings for testflight example](../version/img/expiration-warning-testflight.svg){width="300"}
{align="center"}

## <span translate="no">GitHub Personal Access Token</span>

To enable automatic building, your&nbsp;<span translate="no">GitHub Personal Access Token</span>&nbsp;should be configured:

* `Never expire`
* `repo, workflow` permission scope

Refer to [Modify Automatic Building](#modify-automatic-building) if you don't want to accept the default recommendation to automatically update and build.

If you are not logged in to *GitHub* and have not logged in recently, then you may see the authentication screen when doing the steps below.

Authenticate if requested by clicking on the green `Send SMS` button or entering your password.

![two-factor authentication for access to tokens](img/gh-sms-access-screen.png){width="300"}
{align="center"}

Once you are authenticated, you will have access to view your personal access token.

### Modify Token

If your Token has not expired but does not have the desired permission, you should modify it. Do not regenerate it.

Click on the link to view your token and compare it to the graphic below.

* [Link to access your Personal Access Token](https://github.com/settings/tokens)

![access token with correct permissions](img/gh-token-correct-permission.png){width="600"}
{align="center"}

The graphic above has a blue rectangle added to indicate where you should see your token. If yours does not look like this, click on the link (`FastLane Access Token`) to open a new display. Watch the GIF below - there are 4 frames, the last one has the Update token button.

1. Click on the link (`FastLane Access Token`) to open a new display
1. This example has no workflow or repo checks in it
1. Add a check to the workflow box
1. Scroll all the way to the bottom of the screen and click on the green `Update token` button

![configure access token permissions](img/update-personal-access-token.gif ){width="600"}
{align="center"}

After you click on the `Update token` button, your `FastLane Access Token` should now show `repo, workflow` and look like the earlier graphic above.

The only reason to regenerate a token is if it is set to expire. Do not do the next section unless you have to.

### Regenerate Token

If your Personal Access Token has expired or has an expiration date, you can regenerate it.

!!! tip "Update new GH_PAT to Secrets"
    After you get your new token, immediately add it to your Secrets for any app you build with this method. You don't have to rebuild the app, but it's a good idea to at least run Action 1. Verify Secrets for each repository to make sure you did not make a mistake.

You can regenerate your Personal Access Token at any time by clicking on the link below. (Right-click, control-click to open in a new browser tab.)

* [Link to access your &nbsp;<span translate="no">GitHub Personal Access Token</span>](https://github.com/settings/tokens)

!!! question "Your existing &nbsp;<span translate="no">TestFlight</span> builds are fine"
    The yellow &nbsp;<span translate="no">GitHub</span> warning by the `Regenerate Token` button is for new builds you make in the future.

    Previous builds are still available in &nbsp;<span translate="no">TestFlight</span> and are not affected by this action.

The `FastLane Access Token` is a clickable link.

![list of personal access tokens on github](img/gh-token-list.png){width="600"}
{align="center"}

After you click on `FastLane Access Token` your screen should be similar to the graphic below.

Note - selecting the `workflow` check box below is new. If yours does not show that selection, add it before you click on Regenerate token (red highlight in graphic below).

![review of fastlane access token on github](img/gh-token-review.svg){width="600"}
{align="center"}

Click on Regenerate token (red highlight in previous graphic) to see screen similar to next graphic. 

* Most Loopers will have classic personal access tokens
    * If you are a developer who needs to use the fine-grained (by repository) option, that's fine

Be sure to change the Expiration from `30 days` to `No Expiration`. When you select `No Expiration` a &nbsp;<span translate="no">GitHub</span> warning appears. Click on the green `Regenerate Token` button (red highlight in following graphic).

![regenerate fastlane access token on github](img/gh-token-no-expiration.svg){width="600"}
{align="center"}

The next screen shows your new token. Copy the token using the copy icon and save it along with your other secret settings.

![copy fastlane access token on github](img/gh-token-to-copy.png){width="600"}
{align="center"}

The next step is to update GH_PAT in your LoopWorkspace Repository Secrets.

!!! tip "Update new GH_PAT to Secrets"
    After you get your new token, immediately add it to your Secrets for any app you build with this method. You don't have to rebuild the app, but it's a good idea to at least run Action 1. Verify Secrets for each repository to make sure you did not make a mistake.

### Update Secrets

This example is for updating GH_PAT in the Secrets for your repository, but the same method can be applied when changing any Secret.

Open the repository for which you will update Secrets. On the far right is a Settings selection. If you don't see Settings (if last item on row is Insights), then you are **not** on your fork or you need to sign in to your *GitHub* account. You should see `username/LoopWorkspace` with forked from `LoopKit/LoopWorkspace` underneath.

Refer to the GIF for help. There are 3 frames.

![screen showing repository secrets list](img/update-secret-gh-pat.gif){width="500"}
{align="center"}

1. Tap on Settings, then scroll down see "Secrets and variables" on the left side and click on the drop down indicator to see Actions.
1. Keep scrolling on the same screen, past the Action secrets / New repository secret row, until you see your Repository secrets list. 
1. Click on the GH_PAT, tap on the pencil and enter the new token in the form. Click on Update Secret to complete the action.

Scroll all the way to the top of the screen and tap on your LoopWorkspace link. Then follow the [Update with Browser](#update-with-browser) instructions to start a new build.

## *GitHub* Build for dev

You can build any desired branch (available at LoopKit/LoopWorkspace) using the *GitHub* Browser build method. This section is suitable if you have already built either dev or main branch using the [GitHub First-Time](gh-first-time.md) instructions.

**No matter the method used to build Loop for any branch other than main, you are testing development code. Please read this link now before continuing.**

* **[What's going on in the dev branch](../version/development.md#whats-going-on-in-the-dev-branch)**

The graphics show the dev branch. If you want a different branch, just substitute that branch name for dev.

!!! tip "Overview of what you will do"
    1. Your LoopWorkspace fork must have the branch you want
        * You will either add it or make sure it is up to date
        * You cannot just rename your existing branch to dev - you must get the dev branch from LoopKit
    1. When you select the action `4. Build Loop` and then click on the `Run Workflow` dropdown, you must select `dev` there before clicking the green `Run workflow` button - see [Build Branch](#build-branch)


### Check Current Branches

Your LoopWorkspace fork is at `https://github.com/username/LoopWorkspace` where you substitute your actual &nbsp;<span translate="no">GitHub</span> `username`. You need to be logged into &nbsp;<span translate="no">GitHub</span>. Review the graphic below as you go through the steps.

1. Click on the `Branches` icon to display the branches as shown in the lower half of the graphic below:
    * If the branch you want is not listed, then continue with Step 2
    * Otherwise, skip ahead to [Update Branch](#update-branch)
1. Click on the `New branch` button and follow the [Add Branch](#add-branch) steps

![steps to add a branch](img/add-branch-01.svg){width="700"}
{align="center"}

### Add Branch

Each step in the list below matches with the number in the graphic. In the top half of the graphic, the left side shows the initial display and the right side shows the display after making the indicated selections:

1. Click on the drop down menu labeled 1 in the graphic and choose LoopKit/LoopWorkspace as show in the top right graphic
2. Click on the drop down menu labeled 2 in the graphic and choose dev
3. Click on the Branch name box labeled 3 in the graphic and type dev
    * The branch name in your fork should always match the branch name you are adding; check that you type it correctly
4. Review the dialog items to make sure everything is correct and then tap on Create branch

![steps to add a branch continued](img/add-branch-02.svg){width="700"}
{align="center"}

### Update Branch

Tap the `Code` button (upper left) and ensure this branch in your fork is up to date.

* Select the desired branch in the dropdown menu (this graphic shows dev branch)
* If the message indicates this branch is "behind", tap on the sync fork button and then the Update branch button

![message displayed when your fork of LoopWorkspace is behind LoopKit version](img/github-build-check-fork-status.svg){width="700"}
{align="center"}

### One-Time Changes

Look in this section for one-time changes for building dev with a browser that require special, one-time actions. After the release of 3.4.0, this section is empty.

Skip ahead to [Build Branch](#build-branch).

### Build Branch

If you want a branch to be the one you build all the time, you may choose to [Change Default Branch](#change-default-branch). This is not necessary except for special cases.

If you have one branch as default, for example main, and choose to build a different branch, there is an extra step when you Build Loop. Refer to step 4 in the graphic below. Use the branch dropdown menu to select the branch you want before hitting the green Run workflow button.

![build loop using github actions](img/action-04-build-loop.svg){width="700"}
{align="center"}

## Change Default Branch

There can be several reasons why you would change your default branch.

* It can be convenient to have the branch you build most be configured as the default branch
* The branch you want to build has a different workflow than your default branch (not typical)
    * In this case, you **must** modify the default branch
    * Check the zulipchat conversation about the branch you are testing to see if it is necessary to make it default

These are the steps to modify the default branch.

For this example, we show how to change from a default branch of `main` to a default branch of `dev`. Note - only the owner of the repository can take this action and they must be logged in. Otherwise the Settings tab does not appear.

For the numbered steps below, refer to the graphic found under each group of steps.

1. Click on the Settings Icon near the top right of your LoopWorkspace
    * You may need to scroll down to see the Default Branch as shown in the graphic - do not tap on the Branches tab to the left under Code and Automation

    ![show default branch](img/gh-settings-branch-01.svg){width="700"}
    {align="center"}

1. To the right of the default branch name there is a pencil and a left-right arrow icon
    * Tap on the left-right arrow icon to bring up the `Switch default branch to another branch` dialog
1. Click on the dropdown next to the current default branch, in this example, `main`
1. Select the desired default branch, in this example, `dev`
1. Click on the `Update` button

    ![modify default branch](img/gh-settings-branch-02.svg){width="700"}
    {align="center"}

1. You will be presented with an are-you-sure question.
    * Click on the red `I understand, update the default branch.` button


    ![confirm default branch](img/gh-settings-branch-03.svg){width="400"}
    {align="center"}

Your default branch has been changed.

## Modify Automatic Building

For someone using [development code](#github-build-for-dev) for their own use, they probably want to decide when to update their fork to the most recent commit. They can still have the advantage of automatic building without automatic updates. There may be other configurations someone would choose. These options are added to Loop 3.3.0 and later.

You can affect the default behavior:

1. [Modify Automatic Schedule](#modify-automatic-schedule)
1. [Disable Automatic Actions](#disable-automatic-actions)

### Modify Automatic Schedule

You can modify the automation by creating and using some variables.

To configure the automated build more granularly involves creating up to two environment variables: `SCHEDULED_BUILD` and/or `SCHEDULED_SYNC`. See [How to configure a variable](#how-to-configure-a-variable). 

Note that the weekly and monthly Build Loop actions will continue, but the actions are modified if one or more of these variables is set to false. **A successful Action Log will still appear, even if no automatic activity happens**.

* If you want to manually decide when to update your repository to the latest commit, but you want the monthly builds and keep-alive to continue: set `SCHEDULED_SYNC` to false and either do not create `SCHEDULED_BUILD` or set it to true
* If you want to only build when an update has been found: set `SCHEDULED_BUILD` to false and either do not create `SCHEDULED_SYNC` or set it to true
    * **Warning**: if no updates to your default branch are detected within 90 days, your previous TestFlight build may expire requiring a manual build

|`SCHEDULED _SYNC`|`SCHEDULED _BUILD`|Automatic Actions|
|---|---|---|
| `true` (or NA) | `true` (or NA) | keep-alive, weekly update check (auto update/build), monthly build with auto update|
| `true` (or NA) | `false` | keep-alive, weekly update check with auto update, only builds if update detected|
| `false` | `true` (or NA) | keep-alive, monthly build, no auto update |
| `false` | `false` | no automatic activity, no keep-alive|

### How to configure a variable

1. Go to the "Settings" tab of your LoopWorkspace repository.
2. Click on `Secrets and Variables`.
3. Click on `Actions`
4. You will now see a page titled *Actions secrets and variables*. Click on the `Variables` tab
5. To disable ONLY scheduled building, do the following:
    - Click on the green `New repository variable` button (upper right)
    - Type `SCHEDULED_BUILD` in the "Name" field
    - Type `false` in the "Value" field
    - Click the green `Add variable` button to save.
7. To disable scheduled syncing, add a variable:
    - Click on the green `New repository variable` button (upper right)
    - - Type `SCHEDULED_SYNC` in the "Name" field
    - Type `false` in the "Value" field
    - Click the green `Add variable` button to save
  
Your build will run on the following conditions:

- Default behaviour:
    - Run weekly, every Wednesday at 08:00 UTC to check for changes; if there are changes, it will update your repository and build
    - Run monthly, every first of the month at 06:00 UTC, if there are changes, it will update your repository; regardless of changes, it will build
    - Each time the action runs, it makes a keep-alive commit to the `alive` branch if necessary
- If you disable any automation (both variables set to `false`), no updates, keep-alive or building happens when Build Loop runs
- If you disabled just scheduled synchronization (`SCHEDULED_SYNC` set to`false`), it will only run once a month, on the first of the month, no update will happen; keep-alive will run
- If you disabled just scheduled build (`SCHEDULED_BUILD` set to`false`), it will run once weekly, every Wednesday, to check for changes; if there are changes, it will update and build; keep-alive will run

### Disable Automatic Actions

To enable the scheduled build and sync, the `GH_PAT` must hold the `workflow` permission scopes. This permission serves as the enabler for automatic and scheduled builds with browser build. To disable this, follow these steps:

1. Go to your [FastLane Access Token](https://github.com/settings/tokens)
1. If it says `repo`, `workflow` next to the `FastLane Access Token` link, then automatic building is enabled
1. To disable automatic update and build, click on the link to open the token detail view
    * Click to uncheck the `workflow` box
    * Click to check the `repo` box
1. Scroll all the way down to and click the green `Update token` button
1. Your token now holds only the `repo` permission

If you choose not to have automatic building enabled, be sure the `GH_PAT` has `repo` scope or you won't be able to manually build.

## Stop Building

What if I decide I don't want the automatic building feature?

* If you are using the released version of Loop, please leave automatic building running
    * Please read [TestFlight Automatic Updates](gh-deploy.md#testflight-automatic-updates) on how to configure TestFlight so you choose when the updated app gets installed on your phone
    * Otherwise, you may see the dreaded "Loop Beta has expired" message, have a Loop that won't open and not have a version ready to go in TestFlight that you can install within a few seconds

* If you are taking a break from Loop and want to stop monthly Build emails, consider disabling actions for the Build Loop action for your app.
    * [GitHub Directions to Disable and Enable a Workflow](https://docs.github.com/en/actions/using-workflows/disabling-and-enabling-a-workflow#disabling-a-workflow)
    * It is the Build action that kicks off the update and build steps, so simply disabling the one action is sufficient

* If you are done with Loop, you can delete the whole repository; but you should be sure about this because you'll need to start over with [GitHub First Time](gh-first-time.md) to restore ability to build Loop with GitHub.
