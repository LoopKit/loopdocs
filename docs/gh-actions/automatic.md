## Overview

**After the next release of the *Loop* app (version 3.4.0), this page will be required for all versions when building with a browser.**

**Before that release, this page is only relevant when building the `dev` branch with a browser and only when the `dev` branch is the default branch.**

## Modify Automatic Building

For someone using [development code](build-dev-browser.md) for their own use, they probably want to decide when to update their `fork` to the most recent commit. They can still have the advantage of automatic building without automatic updates. There may be other configurations someone would choose. These options are added to Loop 3.3.0 (`dev` branch) and later.

You can affect the default behavior:

1. [Modify Automatic Schedule](#modify-automatic-schedule)
1. [Disable Automatic Actions](#disable-automatic-actions)

### Modify Automatic Schedule

You can modify the automation by creating and using some variables.

To configure the automated build more granularly involves creating up to two environment variables: `SCHEDULED_BUILD` and/or `SCHEDULED_SYNC`. See [How to configure a variable](#how-to-configure-a-variable). 

Note that the weekly and monthly `Build Loop` actions will continue, but the actions are modified if one or more of these variables is set to false. **A successful Action Log will still appear, even if no automatic activity happens**.

* If you want to manually decide when to update your repository to the latest commit, but you want the monthly builds and keep-alive to continue: set `SCHEDULED_SYNC` to false and either do not create `SCHEDULED_BUILD` or set it to true
* If you want to only build when an update has been found: set `SCHEDULED_BUILD` to false and either do not create `SCHEDULED_SYNC` or set it to true
    * **Warning**: if no updates to your default branch are detected within 90 days, your previous TestFlight build may expire requiring a manual build

| <div style="width:110px">`SCHEDULED_SYNC`</div> | <div style="width:110px">`SCHEDULED_BUILD`</div> | Automatic Actions |
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
- If you disable any automation (both variables set to `false`), no updates, keep-alive or building happens when `Build Loop` runs
- If you disabled just scheduled synchronization (`SCHEDULED_SYNC` set to`false`), it will only run once a month, on the first of the month, no update will happen; keep-alive will run
- If you disabled just scheduled build (`SCHEDULED_BUILD` set to`false`), it will run once weekly, every Wednesday, to check for changes; if there are changes, it will update and build; keep-alive will run

### Disable Automatic Actions

To enable the scheduled build and sync, the `GH_PAT` must hold the `workflow` permission scopes. This permission serves as the enabler for automatic and scheduled builds with browser build. To disable this, follow these steps:

1. Go to your [FastLane Access Token](https://github.com/settings/tokens){: target="_blank" }
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
    * Please read [TestFlight Automatic Updates](gh-deploy.md#automatic-update-build-install) on how to configure TestFlight so you choose when the updated app gets installed on your phone
    * Otherwise, you may see the dreaded "Loop Beta has expired" message, have a Loop that won't open and not have a version ready to go in TestFlight that you can install within a few seconds

* If you are taking a break from Loop and want to stop monthly Build emails, consider disabling actions for the `Build Loop` action for your app.
    * [GitHub Directions to Disable and Enable a Workflow](https://docs.github.com/en/actions/using-workflows/disabling-and-enabling-a-workflow#disabling-a-workflow){: target="_blank" }
    * It is the Build action that kicks off the update and build steps, so simply disabling the one action is sufficient

* If you are done with Loop, you can delete the whole repository; but you should be sure about this because you'll need to start over with [Configure to Use Browser](gh-first-time.md) to restore ability to build Loop with GitHub.
