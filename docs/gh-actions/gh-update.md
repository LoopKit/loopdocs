## Update Loop using GitHub Actions

This is only available with Loop 3 and Loop development branch.

!!! info "Time Estimate"
    Build Loop

    - Start the Build: 5 minutes
    - Wait for build to complete and appear in TestFlight on your phone
        * about an hour
        * depends on GitHub, Apple and TestFlight

    Optional: If you need to update your GitHub Personal Access token

    * 5 minutes to regenerate token
    * 5 minutes to update the GH_PAT Secret for each of your app repositories

!!! abstract "Summary"
    **You must build Loop every 90 days when you use the GitHub build method - this is a TestFlight requirement.**

    * The GitHub Personal Access Token expiration is independent of the TestFlight app expiration
        * LoopDocs used to have you set up your token to expire at the same time as TestFlight but that added an unnecessary burden to the update process
        * The new recommendation is that your GitHub Personal Access Token be updated to `No Expiration`
    * To update your GitHub Personal Access Token, start at [GitHub Token](#github-token)
    * Otherwise, start at [GitHub Build Update](#github-build-update)

!!! question "FAQs"
    - **Do I need a computer?** No.
    - **Can I do this on my phone?** Yes, especially after you update your GitHub token to `No Expiration`.
    - **Did the directions change?** Yes. We now recommend you select a GitHub Personal Access Token that never expires. It simplifies the build every 90-day process significantly.
    - **How do I set my GitHub Personal Access token to never expire?** See this section [Regenerate GitHub Token](#regenerate-github-token).
    - **What happens to my existing builds when I change my GitHub Personal Access Token?** Nothing. The GH_PAT only affect future builds. Previous build will be available for the full 90 days.

## GitHub Build Update

!!! abstract "Summary of Update Steps"
    * [Update Fork](#update-fork)
    * [Build Loop](#build-loop)
    * [Wait for TestFlight](#wait-for-testflight)
    * [Install or Confirm Installation](#install-or-confirm-installation)

### Update Fork

Open GitHub in your browser (sign in if needed) and select your LoopWorkspace repository from your repositories list.

Look to see if your fork is up to date.

* When you go to your fork to do the update, simply sync the branch if it says there are updates and you get the latest release (details below graphic)
    * This particular graphic shows the dev branch
    * Yours should show the main branch

![message displayed when your fork of LoopWorkspace is behind LoopKit version](img/github-build-check-fork-status.svg){width="700"}
{align="center"}

* If your fork is up to date with LoopKit version for that `{branch}`, you will see the message `This branch is up to date with LoopKit/LoopWorkspace:{branch}` - there is no need to build again unless you are near your 90 day TestFlight expiration date - in which case, proceed to [Build Loop](#build-loop)
* If your fork shows a message such as `This branch is 3 commits behind LoopKit:main` and you want to update and build, then click `Sync Fork` by tapping where the red rectangle is shown in the graphic above, then in the pop-up window, tap on `Update branch`

!!! question "Building a different branch"
    Do I need to do anything special to build a different branch?

    Yes: please follow instructions at [GitHub Build for dev](#github-build-for-dev)

### Build Loop

The section continues immediately after the [Update Fork](#update-fork) section. Refer to graphic below as you follow the steps to Build Loop.

* Click on the 'Actions' tab
* Select the '4. Build Loop' workflow on the left
* Look on the right and click 'Run workflow' to  see the dropdown
* Click on the green `Run workflow` button in the dropdown
* Wait ~25 min for the build to complete successfully
* It is then processed by Apple and sent to TestFlight (be patient)

![graphic indicating how to build again](img/github-build-actions-build-again.svg){width="700"}
{align="center"}

### Wait for TestFlight

You'll receive an App Store Connect email confirming that the build has completed processing, and a TestFlight email confirming the new app is ready to test.

* If you get an email that the action failed, then return to your repository and look for Build Action error messages
    * Click on the most recent Build job with the red x by it
    * If the details show this message, "[Could not install WWDR certificate](gh-errors.md#could-not-install-wwdr-certificate)", make sure your developer account is in good standing and that there are no agreements that need to be accepted
    * Repeat the build (previous step) and it should be fine the next time - that just means Apple did not reply to GitHub as fast as GitHub expected
* You can ignore an email from Apple that there are things you must fix in your app - that refers to things to fix before putting that app in the App Store and you will not be doing that

The updated Loop app will show up in your TestFlight app on the Looper's phone.

* Your new app will have "Expires in 90 days"
    * There may be older builds that are still in TestFlight
    * It takes time for the update to show up in the TestFlight app
* You will also see a build number in parentheses, that number increments each build - don't worry about the number

!!! tip "Calendar Reminder"
    This is a good time to put a calendar reminder in your favorite app.

    Set it up for a few days before the TestFlight app will expire.

### Install or Confirm Installation

#### Automatic Update Disabled

Option 1: If you chose to leave [TestFlight Automatic Updates](../gh-actions/gh-deploy.md#testflight-automatic-updates) disabled for Loop, you choose when to install the app on the phone.

* Open TestFlight on your phone and click `Install` as shown in the GIF below
* If you are building for a child, follow the [Install TestFlight Loop for Child](gh-deploy.md#install-testflight-loop-for-child) instructions again

![install Loop from TestFlight](img/testflight-install-loop.gif){width="300"}
{align="center"}

#### Automatic Update Enabled

Option 2: If you chose to leave [TestFlight Automatic Updates](../gh-actions/gh-deploy.md#testflight-automatic-updates) enabled for Loop, the updated build will be installed over your existing app.

* In this case, when you look at the TestFlight app on your phone, the app should have installed automatically
* Refer to the GIF above, the message will say `Open` instead of `Install`

## GitHub Build Details

In the Loop app, once installed on your phone, tap on Settings -> Support -> Issue Report. The graphic below shows an example of the Build Details included in the report.

* The `profileExpiration` listed here is irrelevant - the app expires when the TestFlight expiration indicates - a later version of Loop 3 will probably capture that date and provide a notification in the app; but for now, you must remember
    * Pro Tip: Add a calender reminder for your next build
* An app built with GitHub will display a `sourceRoot` that starts with `/Users/runner/work/LoopWorkspace`
    * The `buildDateString` is when the app was built and transferred to TestFlight, not when it was installed on your phone
    * You can use 90 days from this date, as well as the Expires in ## Days on the TestFlight app, to know when you need to rebuild

![graphic indicating build details](img/gh-build-details.png){width="300"}
{align="center"}

## GitHub Token

If your GitHub Personal Access Token has not expired and you don't want to regenerate it, you don't need this section.

If you want to follow the new recommendation of using a GitHub Personal Access Token that never expires, you can regenerate the new one at any time.

!!! tip "Update new GH_PAT to Secrets"
    After you get your new token, immediately add it to your Secrets for any app you build with this method. You don't have to rebuild the app, but it's a good idea to at least run Action 1. Verify Secrets for each repository to make sure you did not make a mistake.

### Regenerate GitHub Token

You can regenerate your GitHub Personal Access Token at any time by clicking on the link below. (Right-click, control-click to open in a new browser tab.)

* [Link to access your GitHub Personal Access Token](https://github.com/settings/tokens)

If you are not logged in to GitHub and have not logged in recently, then you may see the authentication screen. Click on the link below, and authenticate if requested by clicking on the green `Send SMS` button or entering your password.

![two-factor authentication for access to tokens](img/gh-sms-access-screen.png){width="300"}
{align="center"}

Once you are authenticated, your screen should be similar to the graphic below. The `FastLane Access Token` is a clickable link.

![list of personal access tokens on github](img/gh-token-list.png){width="600"}
{align="center"}

After you click on `FastLane Access Token` your screen should be similar to the graphic below.

!!! question "Your existing TestFlight builds are fine"
    The yellow GitHub warning by the `Regenerate Token` button is for new builds you make in the future.

    Previous builds are still available in TestFlight and are not affected by this action.

![review of fastlane access token on github](img/gh-token-review.png){width="600"}
{align="center"}

Click on Regenerate token (red highlight in previous graphic) to see screen similar to next graphic. 

* Most Loopers will have classic personal access tokens
    * If you are a developer who needs to use the fine-grained (by repository) option, that's fine

Be sure to change the Expiration from `30 days` to `No Expiration`. When you select `No Expiration` a GitHub warning appears. Click on the green `Regenerate Token` button (red highlight in following graphic).

![regenerate fastlane access token on github](img/gh-token-no-expiration.svg){width="600"}
{align="center"}

The next screen shows your new token. Copy the token using the copy icon and save it along with your other secret settings.

![copy fastlane access token on github](img/gh-token-to-copy.png){width="600"}
{align="center"}

The next step is to update GH_PAT in your LoopWorkspace Repository Secrets. (If you build other apps with this method - update the GH_PAT for all of them right now - do not forget.)

### Update Secrets

This example is for updating GH_PAT in the Secrets for your repository, but the same method can be applied when changing any Secret.

This can be done with the GitHub Personal Access Token still in your paste buffer - but to be safe, save the token with your other secret settings. If you lose track, just [Regenerate GitHub Token](#regenerate-github-token) again.

The graphics and instructions in this section are using a phone. This was done just to prove we weren't kidding when we said you can do it all on your phone. Most people use a computer browser.

Scroll all the way up to the top of the window to see the hamburger menu, click on it and choose your name and icon (near bottom of the list). Scroll down to the LoopWorkspace repository and tap on the link.

Do a horizontal scroll (required on your phone, probably not on a browser) on the row that starts with Code and ends in Settings and tap on Settings. If you don't see Settings (if last item on row is Insights), then you are **not** on your fork or you need to sign in to your GitHub account. You should see `username/LoopWorkspace` with forked from `LoopKit/LoopWorkspace` underneath.

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

## GitHub Build for dev

You can build any desired branch (available at LoopKit/LoopWorkspace) using the GitHub Browser build method. This section is suitable if you have already built either dev or main branch using the [GitHub First-Time](gh-first-time.md) instructions.

**No matter the method used to build Loop for any branch other than main, you are testing development code. Please read this link now before continuing.**

* **[What's going on in the dev branch](../version/development.md#whats-going-on-in-the-dev-branch)**

The graphics show the dev branch. If you want a different branch, just substitute that branch name for dev.

!!! tip "Overview of what you will do"
    1. Your LoopWorkspace fork must have the branch you want
        * You will either add it or make sure it is up to date
    1. Run Action: 4. Build Loop but select your branch in the Run Workflow dropdown - see [Build Branch](#build-branch)

### Check Current Branches

Your LoopWorkspace fork is at `https://github.com/username/LoopWorkspace` where you substitute your actual GitHub `username`. You need to be logged into GitHub. Review the graphic below as you go through the steps.

1. Click on the Branches icon to display the branches as shown in the lower half of the graphic below:
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
