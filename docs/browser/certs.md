## Overview

With the release of `Loop 3.6.0`, the build action includes the create certificates action. This action can be run independently, but is no longer required.

You can skip ahead to [Build the App](build-yml.md).

## `Create Certificates`

??? abstract "Section Summary (click to open/close)"
    1. Go back to the "Actions" tab of your LoopWorkspace repository in *GitHub*.
    1. On the left side, select "3. Create Certificates".
    1. On the right side, click "Run Workflow", and tap the green `Run workflow` button.
    1. Wait, and within a minute or two you should see a green checkmark indicating the workflow succeeded.

    [<span class="loop-bigger">:material-skip-forward:</span>](build-yml.md#build-the-loop-app) To skip the detailed instructions, click on [Build the *Loop* App](build-yml.md#build-the-loop-app)

Refer to the graphic below for the numbered steps:

1. Click on the "<code>Actions</code>" tab of your <code>LoopWorkspace</code> repository
1. On the left side, click on "`Create Certificates`"
1. On the right side, click "`Run Workflow`" to show a dropdown menu
    * You will see your default branch (typically `main`)
    * You can select a different branch, but typically, you run the default
1. Tap the green button that says "`Run workflow`".

    ![create certificates using github actions](img/action-03-create-certs.svg){width="700"}
    {align="center"}

1. Wait a minute or two for the action to finish

!!! tip "Be Patient"
    * Refresh the browser if you are unsure if the action started
    * Do not start a new action until the first one completes

### Success

Once you see the green check mark by `Create Certificates`, the next step is to [Build your *Loop* App](build-yml.md).

### Failure

* If you see the red `X` (:octicons-x-circle-fill-16:{: .failed }):
    * Use the Browser Build Errors page to resolve the error, then repeat the Action
    * [Quick Reference for Browser Build Errors](bb-errors.md#quick-reference-for-browser-build-errors){: target="_blank" }
