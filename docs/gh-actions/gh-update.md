## Update Loop using Github Actions

This is only available with Loop 3 and Loop dev branch.

**You must build Loop every 90 days when you use this method.**

Once you have built Loop one time with github Build Actions, updates are fast and easy.

**You must build Loop every 90 days when you use this method.**

1. Sign in to Github and select your LoopWorkspace repository from your repositories list
1. Look to see if your fork is up to date
    * If your fork is up to date you will see the message `This branch is up to date with LoopKit/LoopWorkspace:dev` - there is no need to build again unless you are near your 90 day expiration data - in which case, proceed to Step 3
    * If your fork shows a message such as `This branch is 3 commits behind LoopKit:dev` and you want to update and build, then click `Sync Fork` by tapping where the red rectangle is shown in the graphic below, then in the pop-up window, tap on `Update branch`

    ![message displayed when your fork of LoopWorkspace is behind LoopKit version](img/github-build-check-fork-status.svg){width="700"}
    {align="center"}

1. Build Loop - refer to graphic below as you follow the steps
    * Click on the 'Actions' tab
    * Select the 'Build Loop' workflow and then click on 'run workflow' 
    * Wait ~25-45 min for the build to complete

    ![graphic indicating how to build again](img/github-build-actions-build-again.svg){width="700"}
    {align="center"}


1. You'll receive an App Store Connect email confirming that the build has completed processing, and a TestFlight email confirming the (now updated) app is ready to test.
    * If you get an email that the action failed, then return to your repository and look for Build Action error messages
        * Click on the most recent Build job with the red x by it
        * If the details show this message, "[Could not install WWDR certificate](gh-errors.md#could-not-install-wwdr-certificate)", make sure your developer account is in good standing and that there are no agreements that need to be accepted
        * Repeat the build and it should be fine the next time
1. The updated Loop app will automatically be pushed to and shown in your Test Flight app, so all you need to do is...
    * Open TestFlight on your phone and click `Install`
    * If you have automatic installation enabled in TestFlight, the app should have installed automatically, in which case the message should say `Open`.

    ![graphic indicating how to install app in TestFlight](img/testflight-app-install.svg){width="500"}
    {align="center"}

