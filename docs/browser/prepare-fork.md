## Fork `LoopWorkspace`

???+ tip "Are you a Caregiver? Are you planning to build more than one app? (Click to close/open)"
    Did you skip the optional section to [Create a Free *GitHub* Organization](secrets.md#create-a-free-github-organization){: target="_blank" }?

    If you plan to build more that one app and use your personal account, you must add the 6 <code>Secrets</code> to each repository for each app. It is not hard but it can get tiresome.

    If you make use of the organization option, you only enter the 6 <code>Secrets</code> one time for all your repositories. This is strongly recommended, but not required, for all Browser Builders.

???+ abstract "Section Summary (click to open/close)"
    Fork [https://github.com/LoopKit/LoopWorkspace](https://github.com/LoopKit/LoopWorkspace){: target="_blank" } into your account.

    [<span class="loop-bigger">:material-skip-forward:</span>](#configure-secrets) To skip the detailed instructions, click on [Configure <code>Secrets</code>](#configure-secrets)

!!! warning "Existing Fork"
    If you already have a fork of <code>LoopWorkspace</code>, click on [Already Have LoopWorkspace](#already-have-loopworkspace) to decide what to do. That section provides links to return you to these instructions.

### Create the `Fork`

1. Click this link [https://github.com/LoopKit/LoopWorkspace](https://github.com/LoopKit/LoopWorkspace){: target="_blank" } to open the <code>LoopWorkspace</code> repository owned by `LoopKit`
1. At the upper right side of the screen, click on the word `Fork`

    ![fork information for LoopWorkspace](img/gh-fork-loopworkspace-top.svg){width="700"}
    {align="center"}

1. Refer the the GIF below:
    * If you created a free organization (strongly recommended), you will see the display shown in the GIF below where you will choose your organization as the owner
        * If you did not set up a free organization, `my-name` will be automatically filled in as the owner (`Owner`)
    * If you already have a fork, you should not proceed, see [Already Have a LoopWorkspace](#already-have-loopworkspace)
    * The repository name is already filled in
        * **Do not rename the repository to something else**
        * It needs to **match the original repository name** or **automatic building will not work**
    * Leave the selection that says "`Copy the main branch only`" checked
    * Click on the green `Create fork` button

    ![fork information for LoopWorkspace](img/fork-org.gif){width="700"}
    {align="center"}

#### Successful Fork

After creating the &nbsp;<span class="notranslate">fork</span>, your screen should be similar to the next graphic - it will say `main` for the branch instead of `dev` because this graphic was prepared before the release of `Loop 3`. You may or may not see the messages you are told to dismiss in the next two bullets. No worries if you don't see them.

* Near the top right, click on the close button :octicons-x-16: (`x`) to dismiss the `Successfully fetched` message
* In the middle, click on the `Dismiss` button to remove the "`Your branch is not protected`" message

![after creating the fork LoopWorkspace](img/gh-initial-fork-dismiss.png){width="500"}
{align="center"}

Carefully compare your screen to the graphic below paying attention to the highlighted sections.

* Note that your URL is `https://github.com/my-name-org/LoopWorkspace` or `https://github.com/my-name/LoopWorkspace` where `my-name` is the name you chose:
    * Many graphics for LoopDocs are created using a free *GitHub* organization called `loopdocs-tester`
* The comment on the second row indicates where the &nbsp;<span class="notranslate">fork</span>&nbsp; came from (that is a clickable link)
* The branch that is selected :octicons-git-branch-16: is `main`
* The message says "`This branch is up to date with LoopKit/LoopWorkspace:main`"

![after creating the fork LoopWorkspace](img/gh-after-fork.svg){width="700"}
{align="center"}

## Configure <code>Secrets</code>

If you set up a GitHub organization (strongly recommended), follow this [set of instructions](#prepare-to-enter-secrets).

If you decided to not to use a GitHub organization, skip ahead to [Personal Account: Prepare to Enter <code>Secrets</code>](#personal-account-prepare-to-enter-secrets).

!!! tip "What if I already have a bunch of forks in my personal account?"
    You do not have to switch to an organization. But if you want to make the move, follow instructions here [Switch to a GitHub Organization](#switch-to-a-github-organization)

### Prepare to Enter <code>Secrets</code>

You will be adding `Secrets` and `Variables` to your organization. This makes them available to any app you decide to build as long as you set up your free *GitHub* organization as the [owner of the fork](#create-the-fork).

1. Tap on this [*GitHub* link](https://github.com/settings/organizations){: target="_blank" } to see your organizations. (If you don't see a screen similar to the graphic below - you are not logged in to *GitHub*).

    ![settings screen](img/gh-quick-access-org.png){width="700"}
    {align="center"}

1. Choose your organization name from the list (most people will only see one organization)
    * I chose `loopdocs-tester` as my organization, so you will see that name in the URL for graphics in this section.

    ![settings screen](img/gh-org-settings-01.png){width="700"}
    {align="center"}

1. Click on the Settings Icon near the top right
    * If you don't see ⚙️ `Settings`, make your browser wider or scroll to the right
    * After you click on ⚙️ `Settings`, your screen will show a lot of menu items on the left side of the screen. 
    * Scroll down until you can see the `Security` section with `Secrets and variables` drop down.
    * Click on the dropdown icon and then selection `Actions`

    ![settings screen](img/gh-org-settings-02.png){width="600"}
        {align="center"}

The next steps are identical whether you are configuring your organizations `Secrets` and  `Variables` or doing this for every repository in a personal account.

* Skip ahead to [Enter the Secrets](#enter-the-secrets)

### Personal Account: Prepare to Enter <code>Secrets</code>

> This section is only if you are using a personal *GitHub* account to build. Using an organization is recommended. If you are using an organization, skip ahead to [Enter the Secrets](#enter-the-secrets).

Log into *GitHub*.

1. Return to your forked copy of <code>LoopWorkspace</code>
    * Click on your personal icon at the upper right to see the dropdown menu and select "`Your repositories`"

    ![dropdown-menu](img/gh-quick-access.png){width="200"}
    {align="center"}

1. Click on <code>LoopWorkspace</code> to open that repository
1. Click on the Settings Icon near the top right of your LoopWorkspace
    * If you don't see ⚙️ `Settings`, make your browser wider or scroll to the right
    * If you still don't see ⚙️ `Settings`, then you are **not** on your fork or you need to sign in to your *GitHub* account
    * After you click on ⚙️ `Settings`, your screen should look like the graphic below

        ![settings screen](img/gh-settings.svg){width="700"}
        {align="center"}

1. Refer to the graphic above:
    * On the left side, find the `Secrets and variables` dropdown (red circlea)
    * Tap on <code>Actions</code> (red rectangle)

    ![action secrets and variables screen](img/personal-new-secret.png){width="500"}
    {align="center"}

At this point the instructions are the same whether you are using an organization or a personal account.

## Enter the <code>Secrets</code>

The steps to enter the `Secrets` and  `Variables` are identical whether you are configuring these in your [organization account](#prepare-to-enter-secrets) or repeating this for every repository in a [personal account](#personal-account-prepare-to-enter-secrets). Your screen should look like one of the graphics below. If not head back to [Configure Secrets](#configure-secrets).

If you are using a *GitHub* organization, tap on the green button for `New organization secret`:

![action secrets and variables screen](img/gh-org-actions-secrets.svg){width="600"}
{align="center"}

If you are using a personal account, tap on the green button for `New repository secret`::

![action secrets and variables screen](img/personal-new-secret.png){width="600"}
{align="center"}

1. After you tap on the `New secret` button
    * A new screen appears as shown in the first graphic below
    * Do not do anything until reading the sub-bullets, examining the graphics, and proceeding to the next section where each `Secret` name is provided for you to copy and paste
        * Under `Name *`, click on `YOUR_SECRET_NAME` and paste one of the 6 secret names, as directed in [Enter Each Secret](#enter-each-secret)
        * Click inside the `Secret *` box and paste the value for that secret
        * Once you click on `Add Secret`, the secret will be added
        * The second graphic below shows `TEAMID` added and ready for save

![dialog for entering a new secret](img/new-secret-dialog.png){width="700"}
{align="center"}

![teamid secret ready to be saved](img/teamid-secret-ready-to-save.png){width="700"}
{align="center"}

### Enter Each Secret

Enter the name of each <code>Secret</code> found in [Save Your Information](intro-summary.md#save-your-information) and your value for that `Secret`.

* Once you save a secret value, you will not be able to view what you entered, so check carefully before you hit `Add Secret`
    * You can replace the value for any secret later - but you can't view the saved value
* Be especially careful with your `TEAMID`
    * If `TEAMID` is incorrect, the initial `Actions` will succeed but `Build Loop` will fail and you will have some clean-up to do
* You can copy the names of the <code>Secrets</code> by hovering to the right of each word below until you see the copy button (:material-content-copy:). Click on the button to copy the `Secret` name and paste it into *GitHub* where you see `YOUR_SECRET_NAME`. This avoids spelling errors.
``` { .text .copy }
TEAMID
```
``` { .text .copy }
FASTLANE_ISSUER_ID
```
``` { .text .copy }
FASTLANE_KEY_ID
```
``` { .text .copy }
FASTLANE_KEY
```
``` { .text .copy }
GH_PAT
```
``` { .text .copy }
MATCH_PASSWORD
```

* For the `FASTLANE_KEY` value, copy the entire contents from<br>`-----BEGIN PRIVATE KEY-----`<br> through<br>`-----END PRIVATE KEY-----`<br>
* For `MATCH_PASSWORD` value - if you did not already make up a password and save it with your other <code>Secrets</code>, do it now
    * The `MATCH_PASSWORD` must be the same for any repository using this method ([Other Apps](other-apps.md){: target="_blank" })

Once you add all six <code>Secrets</code>, your screen should look similar to the one of the two examples in the graphic below.

> An organization account (top half of graphic) has an column for Visibility which is not seen in a personal account (bottom half of the graphic). The default setting for visibility is `Public repositories`. If yours says anything else, you should update the visibility by tapping on the pencil icon.

* Check that all of your <code>Secrets</code> are spelled correctly
* If one is misspelled, delete it and add a `New secret` with the correct name

![all secrets entered](img/gh-done-adding-secrets.svg){width="600"}
{align="center"}

### Add Variable

This is a new step. It will be used when `Loop 3.6.0` is released to provide automatic renewal of your certificates, which expire once per year.

1. While in the same screen where you enter the `Secrets`, click on the `Variables` tab to the right of the `Secrets` tab:
1. Select new variable and give it the name the `ENABLE_NUKE_CERTS` and enter `true` as the value

``` { .text .copy }
ENABLE_NUKE_CERTS
```

What did you just do?

* When `Loop 3.6.0` is released, certificates will be automatically updated if you have configured this `Variable`
* After `Loop 3.6.0` is released, as long as your *Apple* developers license is valid and all agreements are signed: **you can skip the steps to create or renew your certificates**!
* LoopFollow v2.3.0 or newer makes use of this variable to automate certificate renewal

![enable nuke certs](img/gh-nuke-certs.png){width="700"}
{align="center"}


## Next Step

The next step is to [Validate Secrets and Add Identifiers](identifiers.md).

## Switch to a *GitHub* Organization

If you are someone who already has a lot of forks in your personal account and want to switch to using a *GitHub* organization. Here's how:

1. Follow the steps to create your organization
    * [Create a Free *GitHub* Organization](secrets.md#create-a-free-github-organization){: target="_blank" }
1. Add the `Secrets` and the `Variable` to your *GitHub* organization as explained in [Prepare to Enter `Secrets`](#prepare-to-enter-secrets)
1. Fork all the repos you normally use, but this time, set your organization as the owner
1. For each repository in your organization:
    * Tap on the Actions tab
    * Enable Actions
    * Run the Create Certificates Action and wait for success
    * Run the Build Action
        * WHAT??
        * That's right - all the setup is done on the *Apple* side and you already did that
        * If you succeesfully built with your private *GitHub* account, everything is already configured
        * The one thing you might want to do is copy customizations from your personal account fork to the organization fork
4. Return to your private *GitHub* account
    * Your choice: either delete the forks in your personal account or at least disable the building from your personal account
    * [Disable Building for Personal *GitHub* Account](other-apps.md#disable-building-for-personal-github-account){: target="_blank" }

**Important**

> Your personal *GitHub* account is still needed. The free organization points to your personal account as a member. If you delete your personal *GitHub* account, you lose access to your organization account too.

## Already Have&nbsp;<span translate="no">LoopWorkspace</span>?

Some people may already have a copy (`fork`) of <code>LoopWorkspace</code>.

If your copy (`fork`) is **not** from `LoopKit`, follow the [Delete and Start Fresh](#delete-and-start-fresh) directions.

If your copy (`fork`) is from `LoopKit`:

* Open your <code>LoopWorkspace</code> repository (`https://github.com/my-name-org/LoopWorkspace`) where you use your version of `my-name` in the URL
* Review the graphic in the [Configure: Successful Fork](#successful-fork) section
    * Make sure all the items highlighted by red rectangles are correct with the possible exception of your fork being up to date
* If you see a message that your *fork* is not up to date - tap on the `Sync fork` button and follow the instructions
* Continue with [Validate Secrets and Add Identifiers](identifiers.md)

### Delete and Start Fresh

If your fork is not from `LoopKit`:

* Delete your LoopWorkspace repository
    * Instructions to delete a repository are found at [*GitHub* Docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository){: target="_blank" }
* Return to [Fork LoopWorkspace](#fork-loopworkspace) and follow all the instructions
