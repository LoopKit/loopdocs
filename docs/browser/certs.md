## Create Certificate

The instructions on this page are required to build your app intially. It ties information in you Match-Secrets private repository to your Apple information so that the build action works. After that, it only needs to be run again in a few cases.

* When your certificates have expired (after one year) and you need to [Renew Certificates](bb-update.md#renew-certificate){:target="_blank"}
* When the developers have modified the Identifiers; this requires Create Certificates to be run after you successfully run Add Identifiers and update the new Identifiers

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
    * If this action fails, head over to [Action: 3. Create Certificates Errors](bb-errors.md#action-create-certificates-errors){: target="_blank" }
    * Once you've resolved the error, repeat the Actions [Add Identifiers](identifiers.md#add-identifiers){: target="_blank" } and then `Create Certificates`. (The <code>Add Identifiers</code> might not be required but it is fast and should be done as a matter of routine.)

## Next Step

The next step is to [Build your *Loop* App](build-yml.md).
