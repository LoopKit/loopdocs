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

    [<span class="loop-bigger">:material-skip-forward:</span>](tf-users.md#set-up-users-and-access-testflight) To skip the detailed instructions, click on [Set Up Users and Access (TestFlight)](tf-users.md#set-up-users-and-access-testflight).

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
    * If this action fails, head over to [Action: Build Loop Errors](bb-errors.md#action-build-loop-errors)
    * Once you've resolved the error, it's a good idea to repeat all three steps in this order:
        * [Add Identifiers](identifiers.md#add-identifiers)
        * [Create Certificates](certs.md#create-certificates)
        * Build Loop
1. If the process appears to be happening without an error, go do something else for a while. The build should take about 20-30 minutes.
1. You should get several emails
    * one says the build succeeded (or failed)
    * one says *TestFlight* is ready (typically half-hour after the build succeeds)
    * Ignore the one that says you need to fix "issues" in your app
1. Your app should eventually appear on [`App Store Connect`](https://appstoreconnect.apple.com/apps){: target="_blank" }.

#### *Apple* Email to Ignore

You can ignore an email from *Apple* that there are things you must fix in your app:

*  There is no action you need to take - the developers will handle any updates that are required before it affects your ability to build the app
* Other warnings only address issues if you were selling the app in the app store, but it is for your own personal use

## Build Failed?

Did you get a red X? Head over to the [Errors with Browser](bb-errors.md){: target="_blank" } to page find a solution.

## Successful Build

**Congratulations**

If you get the green check mark, your app successfully built. Just a few more steps.

## Next Steps

If this is your first build, you need to configure your TestFlight Users

* [TestFlight Users](tf-users.md)

If this is a repeat build, wait up to an hour for your new build to appear in TestFlight. Then from the phone where you want to install the *Loop* app, use TestFlight on that phone to install the app.

* [Install on Phone](phone-install.md)

### Caregivers

If you are a Caregiver who helps manage a loved-ones diabetes, you may use other open-source apps that can be built the same way:

* When you are done building and installing the *Loop* app, there are instructions to [Build Other Apps with Browser](other-apps.md)
