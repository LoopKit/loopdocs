## Update <span translate="no">Loop</span> using <span translate="no">GitHub Actions</span>

??? info "Time Estimate (click to open/close)"
    - Update your configuration for automatic builds: 10 minutes
    - Update your fork: 5 minutes
    - Follow the extra instructions to get <span translate="no">Loop</span> ready to build: 10 minutes
    - Start the Build process: 30 seconds
    - Wait for build to complete and appear in <span translate="no">TestFlight</span> on your phone
        * about an hour
        * depends on <span translate="no">GitHub</span>, <span translate="no">Apple</span> and <span translate="no">TestFlight</span>

??? abstract "Page Summary (click to open/close)"
    **You must build Loop every 90 days when you use the <span translate="no">GitHub</span> build method - this is a <span translate="no">TestFlight</span> requirement.**

    Most users will configure for automatic build when they update to Loop 3.4: see [GitHub Build Update](#github-build-update).

    If you are running Loop-dev, be sure to review [GitHub Build for dev](#github-build-for-dev)

??? question "FAQs (click to open/close)"
    - **Do I need a computer?** No.
    - **Did the directions change?** Yes. With the release of 3.4, you should configure for automatic update and build. You should not need to visit this page again with released code.
    - **How do I set my `GitHub Personal Access` token to never expire and allow automatic update and build?** See this section [<span translate="no">GitHub Token</span>](#github-token).
    - **What happens to my existing builds when I change my <span translate="no">GitHub Personal Access Token</span>?** Nothing. The <code>GH_PAT</code> only affect future builds. Previous build will be available for the full 90 days.

## <span translate="no">GitHub</span> Build Update

!!! abstract "Summary of Update Steps"
    * [Accept Agreements](#accept-agreements)
    * [Update Fork](#update-fork)
    * [Build Loop](#build-loop)
    * [Wait for <span translate="no">TestFlight</span>](#wait-for-testflight)
    * [Install or Confirm Installation](#install-or-confirm-installation)

    Ignore the email that says you need to fix "issues" in your app. You are not selling the app in the app store; so no action is required. The app you built is for personal use for you or a family member.


### Accept Agreements

Sign in to your [<span translate="no">Apple Developer</span> account](https://developer.apple.com/account). If there are agreements you have not accepted, your build will fail and you'll see an [<span translate="no">Annotation</span> Message](gh-errors.md#annotation-message) telling you to do this.

If you need detailed instructions, click on the [<code>Apple Program License Agreement</code>](https://support.pushpay.com/s/article/Accepting-the-Apple-Program-License-Agreement) help page.

* Accept the `Apple Program License Agreement` (only)
    * You do NOT need to accept anything related to the `Paid Applications Schedule Agreement`
    * That is only required when you sell an app through the `App Store`

### Update Fork

Open your <span translate="no">GitHub</span> account and select your LoopWorkspace repository from your repositories list.

#### Special Instructions for <span translate="no">Loop</span> 3.4

When updating from <span translate="no">Loop</span> 3.2.x to 3.4, you will need to take some extra steps. Once those steps are completed, your <span translate="no">Loop</span> app will be automatically updated and automatically built at least once a month.

Here is a summary of the extra steps; each step has an associated link. You need to do all of them.

1. Confirm the status of your <span translate="no">GitHub Personal Access Token</span> 
    * It should be configured with permission scope of `repo, workflow` and to never expire
    * You can check this using directions at [GitHub Token](#github-token)
1. Follow the directions for [Manual Update](#manual-update) for your fork
1. This list is repeated in the [Build Loop](#build-loop) section along with detailed instructions
    * Add and Update New Indentifier
    * Create Certificates
    * Build Loop

#### Manual Update

![message displayed when your fork of LoopWorkspace is behind LoopKit version](img/github-build-check-fork-status.svg){width="700"}
{align="center"}

* If your fork is up to date with LoopKit version, you will see the message `This branch is up to date with LoopKit/LoopWorkspace:{branch}` - there is no need to build again unless your Loop app in <span translate="no">TestFlight</span> is about to expire - in which case, proceed to [Build Loop](#build-loop)
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

### Wait for <span translate="no">TestFlight</span>

You'll receive an App Store Connect email confirming that the build has completed processing, and a <span translate="no">TestFlight</span> email confirming the new app is ready to test.

* If you get an email that the action failed, then return to your repository and look for Build Action error messages
    * Click on the most recent Build job with the red x by it
    * If the details show this message, "[Could not install WWDR certificate](gh-errors.md#could-not-install-wwdr-certificate)"
         * This means _<span translate="no">Apple</span>_ did not reply to <span translate="no">GitHub</span> as fast as <span translate="no">GitHub</span> expected
         * Make sure your developer account is in good standing and that there are no agreements that need to be accepted
        * Repeat the build (previous step)

The updated Loop app will show up in your <span translate="no">TestFlight</span> app on the Looper's phone.

* Your new app will have "Expires in 90 days"
    * There may be older builds that are still in <span translate="no">TestFlight</span>
    * It takes time for the update to show up in the <span translate="no">TestFlight</span> app
* You will also see a build number in parentheses, that number increments each build - don't worry about the number

### Install or Confirm Installation

#### Automatic Update Disabled

Option 1: If you chose to leave [TestFlight Automatic Updates](../gh-actions/gh-deploy.md#testflight-automatic-updates) disabled for Loop, you choose when to install the app on the phone.

* Open <span translate="no">TestFlight</span> on your phone and click `Install` as shown in the GIF below
* If you are building for a child, follow the [Install <span translate="no">TestFlight</span> Loop for Child](gh-deploy.md#install-testflight-loop-for-child) instructions again

![install Loop from <span translate="no">TestFlight</span>](img/testflight-install-loop.gif){width="300"}
{align="center"}

#### Automatic Update Enabled

Option 2: If you chose to leave [TestFlight Automatic Updates](../gh-actions/gh-deploy.md#testflight-automatic-updates) enabled for Loop, the updated build will be installed over your existing app.

* In this case, when you look at the <span translate="no">TestFlight</span> app on your phone, the app should have installed automatically
* Refer to the GIF above, the message will say `Open` instead of `Install`

## <span translate="no">GitHub</span> Build Details

!!! note "To Do"
    Update this section know the TestFlight information is displayed on Settings screen.

In the Loop app, once installed on your phone, tap on `Settings -> Support -> Issue Report`. The graphic below shows an example of the Build Details included in the report.

* The `profileExpiration` listed here is irrelevant - the app expires when the <span translate="no">TestFlight</span> expiration indicates
    * Pro Tip: Add a calender reminder for your next build
* An app built with <span translate="no">GitHub</span> will display a `sourceRoot` that starts with `/Users/runner/work/LoopWorkspace`
    * The `buildDateString` is when the app was built and transferred to <span translate="no">TestFlight</span>, not when it was installed on your phone
    * You can use 90 days from this date, as well as the Expires in ## Days on the <span translate="no">TestFlight</span> app, to know when you need to rebuild

![graphic indicating build details](img/gh-build-details.png){width="300"}
{align="center"}

## <span translate="no">GitHub Token</span>

With <span translate="no">Loop</span> 3.4, your <span translate="no">GitHub Personal Access Token</span> should be configured:

* `Never expire`
* `repo, workflow` permission scope

If your token has expired or will expire, the next section helps you to set up a new token and update your <code>Secrets</code>.

If you are not sure about the status of your token, go to 

!!! note "To Do"
    Revise this section for how-to review and update (not regenerate)

### Regenerate <span translate="no">GitHub Token</span>

You can regenerate your <span translate="no">GitHub Personal Access Token</span> at any time by clicking on the link below. (Right-click, control-click to open in a new browser tab.)

* [Link to access your <span translate="no">GitHub Personal Access Token</span>](https://github.com/settings/tokens)

If you are not logged in to <span translate="no">GitHub</span> and have not logged in recently, then you may see the authentication screen. Click on the link below, and authenticate if requested by clicking on the green `Send SMS` button or entering your password.

![two-factor authentication for access to tokens](img/gh-sms-access-screen.png){width="300"}
{align="center"}

Once you are authenticated, your screen should be similar to the graphic below. The `FastLane Access Token` is a clickable link.

![list of personal access tokens on github](img/gh-token-list.png){width="600"}
{align="center"}

After you click on `FastLane Access Token` your screen should be similar to the graphic below.

!!! question "Your existing <span translate="no">TestFlight</span> builds are fine"
    The yellow <span translate="no">GitHub</span> warning by the `Regenerate Token` button is for new builds you make in the future.

    Previous builds are still available in <span translate="no">TestFlight</span> and are not affected by this action.

Note - selecting the `workflow` check box below is new. If yours does not show that selection, add it before you click on Regenerate token (red highlight in graphic below).

![review of fastlane access token on github](img/gh-token-review.svg){width="600"}
{align="center"}

Click on Regenerate token (red highlight in previous graphic) to see screen similar to next graphic. 

* Most Loopers will have classic personal access tokens
    * If you are a developer who needs to use the fine-grained (by repository) option, that's fine

Be sure to change the Expiration from `30 days` to `No Expiration`. When you select `No Expiration` a <span translate="no">GitHub</span> warning appears. Click on the green `Regenerate Token` button (red highlight in following graphic).

![regenerate fastlane access token on github](img/gh-token-no-expiration.svg){width="600"}
{align="center"}

The next screen shows your new token. Copy the token using the copy icon and save it along with your other secret settings.

![copy fastlane access token on github](img/gh-token-to-copy.png){width="600"}
{align="center"}

The next step is to update GH_PAT in your LoopWorkspace Repository Secrets.

!!! tip "Update new GH_PAT to Secrets"
    After you get your new token, immediately add it to your Secrets for any app you build with this method. You don't have to rebuild the app, but it's a good idea to at least run Action 1. Verify Secrets for each repository to make sure you did not make a mistake.

### Update Secrets

!!! note "To Do"
    Update graphics to use a browser rather than a phone.

This example is for updating GH_PAT in the Secrets for your repository, but the same method can be applied when changing any Secret.

This can be done with the <span translate="no">GitHub Personal Access Token</span> still in your paste buffer - but to be safe, save the token with your other secret settings. If you lose track, just [Regenerate <span translate="no">GitHub Token</span>](#regenerate-github-token) again.

The graphics and instructions in this section are using a phone. This was done just to prove we weren't kidding when we said you can do it all on your phone. Most people use a computer browser.

Scroll all the way up to the top of the window to see the hamburger menu, click on it and choose your name and icon (near bottom of the list). Scroll down to the LoopWorkspace repository and tap on the link.

Do a horizontal scroll (required on your phone, probably not on a browser) on the row that starts with Code and ends in Settings and tap on Settings. If you don't see Settings (if last item on row is Insights), then you are **not** on your fork or you need to sign in to your <span translate="no">GitHub</span> account. You should see `username/LoopWorkspace` with forked from `LoopKit/LoopWorkspace` underneath.

Review the GIF below that shows horizontal scroll to find and tap on Settings, then scroll down on the phone to reach "Secrets and variables", open the drop down indicator to see Actions.

![phone screens showing the repository settings, secrets and actions](img/phone-with-settings.gif){width="300"}
{align="center"}

After tapping on Settings -> Secrets and Variables -> Actions, keep scrolling on the same screen, past the Action secrets / New repository secret row, until you see your Repository secrets list as shown in the next GIF.

![phone screen showing repository secrets list](img/phone-secret-list.gif){width="300"}
{align="center"}

When you see the secret, GH_PAT, tap on the pencil and then scroll down until you see the Actions secrets / Update secret dialog as shown in the next graphic. Paste your new token into the Value section and tap Update Secret.

![update secret dialog](img/update-secret-dialog.png){width="300"}
{align="center"}

Scroll all the way to the top of the screen and tap on your LoopWorkspace link. Then follow the [GitHub Build Update](#github-build-update) instructions to start a new build.

## <span translate="no">GitHub</span> Build for dev

!!! note "To Do"
    Update this section for dev 3.5.0 following 3.4 release.

You can build any desired branch (available at LoopKit/LoopWorkspace) using the <span translate="no">GitHub</span> Browser build method. This section is suitable if you have already built either dev or main branch using the [GitHub First-Time](gh-first-time.md) instructions.

**No matter the method used to build Loop for any branch other than main, you are testing development code. Please read this link now before continuing.**

* **[What's going on in the dev branch](../version/development.md#whats-going-on-in-the-dev-branch)**

The graphics show the dev branch. If you want a different branch, just substitute that branch name for dev.

!!! tip "Overview of what you will do"
    1. Your LoopWorkspace fork must have the branch you want
        * You will either add it or make sure it is up to date
        * You cannot just rename your existing branch to dev - you must get the dev branch from LoopKit
    1. When you select the action `4. Build Loop` and then click on the `Run Workflow` dropdown, you must select `dev` there before clicking the green `Run workflow` button - see [Build Branch](#build-branch)

### One-Time Changes

Look in this section for one-time changes to the dev branch that require special, one-time actions. At the current time, this section is blank.

### Check Current Branches

Your LoopWorkspace fork is at `https://github.com/username/LoopWorkspace` where you substitute your actual <span translate="no">GitHub</span> `username`. You need to be logged into <span translate="no">GitHub</span>. Review the graphic below as you go through the steps.

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
