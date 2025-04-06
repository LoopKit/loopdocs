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

Refer to the graphic below for the first four steps:

1. Click on the "`Actions`" tab of your <code>LoopWorkspace</code> repository.
1. On the left side, click on "4. `Build Loop`".
1. On the right side, click "`Run Workflow`" to show a dropdown menu
    * You will see your default branch (typically `main`)
    * You can select a different branch, but typically, you run the default
1. Tap the green button that says "`Run workflow`".

    ![build loop using github actions](img/action-04-build-loop.svg){width="700"}
    {align="center"}

1. Wait a few minutes to make sure there is not an early failure

!!! tip "Be Patient"
    * Refresh the browser if you are unsure if the action started
    * Do not start a new action until the first one completes

If the process appears to be happening without an error, go do something else for a while. The build should take about 20-30 minutes.

You should get several emails

* one says the build succeeded (or failed)
* one says *TestFlight* is ready (typically half-hour after the build succeeds)
* Ignore the one that says you need to fix "issues" in your app

Your app should eventually appear on [`App Store Connect`](https://appstoreconnect.apple.com/apps){: target="_blank" }.

### Successful Build

**Congratulations**

If you get the green check mark, your app successfully built. Just a few more steps.

### *Apple* Email to Ignore

You can ignore an email from *Apple* that there are things you must fix in your app:

*  There is no action you need to take - the developers will handle any updates that are required before it affects your ability to build the app
* Other warnings only address issues if you were selling the app in the app store, but it is for your own personal use

### Build Failed?

Did you get a red X? Head over to the [Errors with Browser](bb-errors.md){: target="_blank" } to page find a solution.

## Next Steps

It may take up to an hour for your new build to appear in TestFlight.

From the phone where you want to install the *Loop* app, use TestFlight on that phone to install the app.

* [Install on Phone](phone-install.md)

If is you skipped the step about creating a *TestFlight* Group or want to add another person to your group:

* [TestFlight Group](tf-users.md)

## Caregivers

If you are a Caregiver who helps manage a loved-ones diabetes, you may use other open-source apps that can be built the same way:

* When you are done building and installing the *Loop* app, there are instructions to [Build Other Apps with Browser](other-apps.md)
