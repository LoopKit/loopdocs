## Update Loop using GitHub Actions

This is only available with Loop 3 and Loop dev branch.

Once you have built Loop one time with github Build Actions, updates are fast and easy.

## GitHub Build Details

**You must build Loop every 90 days when you use this method.**

In Loop, tap on Settings -> Support -> Issue Report. The graphic below shows an example of the Build Details included in the report.

* Note that the profileExpiration listed here is irrelevant - the app expires when the TestFlight expiration indicates - a later version of Loop 3 will probably capture that date and provide a notification in the app; but for now, you must remember
* Notice that the sourceRoot starts with `/Users/runner/work/LoopWorkspace`
    * When you see that sourceRoot, you know this app was installed from GitHub build and TestFlight
    * In this case the buildDataString is associated with when the app was built, not when it was installed on your phone
    * You can use 90 days from this date, as well as the Expires in ## Days on the TestFlight app, to know when you need to rebuild.

![graphic indicating build details](img/gh-build-details.png){width="300"}
{align="center"}




## GitHub Build Update

1. Sign in to GitHub and select your LoopWorkspace repository from your repositories list
1. Look to see if your fork is up to date
    * The dropdown in this graphic shows the dev branch.
    * After the release of Loop-dev as Loop 3.0, you will want master. For a specific release, such as 3.1.2 (which does not exist - so don't look for it), it will be that specific release.
    * If your fork is up to date with LoopKit version for that `{branch}`, you will see the message `This branch is up to date with LoopKit/LoopWorkspace:{branch}}` - there is no need to build again unless you are near your 90 day expiration data - in which case, proceed to Step 3
    * If your fork shows a message such as `This branch is 3 commits behind LoopKit:dev` and you want to update and build, then click `Sync Fork` by tapping where the red rectangle is shown in the graphic below, then in the pop-up window, tap on `Update branch`

    ![message displayed when your fork of LoopWorkspace is behind LoopKit version](img/github-build-check-fork-status.svg){width="700"}
    {align="center"}

1. Build Loop - refer to graphic below as you follow the steps
    * Click on the 'Actions' tab
    * Select the 'Build Loop' workflow on the left
    * Look on the right and click 'Run workflow'
    * Make sure the desired Branch is selected
    * Click on the green `Run workflow` button in the dropdown
    * Wait ~25-45 min for the build to complete

    ![graphic indicating how to build again](img/github-build-actions-build-again.svg){width="700"}
    {align="center"}


1. You'll receive an App Store Connect email confirming that the build has completed processing, and a TestFlight email confirming the (now updated) app is ready to test.
    * If you get an email that the action failed, then return to your repository and look for Build Action error messages
        * Click on the most recent Build job with the red x by it
        * If the details show this message, "[Could not install WWDR certificate](gh-errors.md#could-not-install-wwdr-certificate)", make sure your developer account is in good standing and that there are no agreements that need to be accepted
        * Repeat the build (previous step) and it should be fine the next time
1. The updated Loop app will show up in your TestFlight app
1. If you chose to leave [TestFlight Automatic Updates](../gh-actions/gh-deploy.md#testflight-automatic-updates) enabled for Loop, the updated build will be installed over your existing app.
1. If you choose to disable automatic updates
    * Open TestFlight on your phone and click `Install` as shown in the GIF below
    * If you have automatic updates enabled in TestFlight, the app should have installed automatically, in which case the message should say `Open`.

    ![install Loop from TestFlight](img/testflight-install-loop.gif){width="300"}
    {align="center"}


