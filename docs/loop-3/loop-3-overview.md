# Loop 3 Overview


Loop 3.0 is the next big release. It is being developed and tested under the dev branch (Loop-dev). Loop-dev has significant improvements and looks different (in some ways) from the Loop 2.2.x versions.

!!! info "Loop-dev"
    The dev branch of Loop is currently under test by experienced loopers. If you are testing Loop-dev, the version number reported on your settings screen is Loop v2.3.0 (57).

    To report to developers about which particular version of Loop-dev you are running, look at the top of the [Loop Report](settings.md#issue-a-loop-report) under `Build Details`. The 7-digit alphanumeric indication to the right of workspaceGitRevision is sufficient.

    When this version is released, it will be Loop 3.0 and the interface for Loop 3.x versions will use this updated documentation.


!!! danger ""

    To make life easier for those of us preparing the new documentation, the wording on many pages in the Loop 3 section is set in the future - after the release

    This page will be updated and it and the rest of the Loop 3 section will be moved to Set Up App with the Loop 2.2.x version maintained under a sub-menu


## New with Loop 3

Loop 3 redesigns the app, building off work by Tidepool and DIY contributors. Some changes might not be obvious, but make the app more robust.

Here are some highlights:

* Onboarding protocol with guardrails to help configure settings
* Streamlined main screen display and user experience
* Better alerts and notifications
* Omnipod Dash compatibility
* Fingerstick blood glucose prompts when data is stale
* Non-pump insulin entry within the app
* [Remote Carb/Bolus capability](features.md#remote-carb-bolus)
* [Manual Temp Bolus capability for Omnipod](omnipod.md#manual-temp-basal)


## Building Loop 3

When Loop 3 is released, the build instructions will be updated (please allow a few days for documentation to catch up. Experienced users are testing Loop-dev using the [Loop-dev](../build/step13.md#advanced-users-only) download and build instructions. Do not build Loop-dev unless you are willing to pay attention to announcements on zulipchat and build frequently (plan on once a week.)

!!! warning "Users of dev Branch"
    It is up to you to review these new pages for the information you need.

    Please subscribe to the [Documentation Stream](https://loop.zulipchat.com/#narrow/stream/270362-documentation) on zulipchat. You will see a post there every time LoopDocs is updated.


Those of us who have been testing Loop-dev are very excited for this major update.

## Set Up Loop 3 Overview

!!! success "Congratulations on Building Loop!"

The first time you build Loop 3, the app takes you through the Onboarding process. Review the [Onboarding](onboarding.md) material before continuing.

First a suggestion and some orientation:

!!! tip "Suggestion"
    * Start by reading each page without clicking on any links
    * Return later to the page and click the links for more detail on a particular topic.  Use the back button on your browser to go back to your starting point.

### Brand New Loopers

* Review these 3 pages in detail before you touch any buttons on your app
    * [Onboarding](onboarding.md)
    * [Add CGM](add-cgm.md)
    * [Add Pump](add-pump.md)
* Read the rest of the pages listed under [All Loopers](#all-loopers), below. 

    * The information on the pages will become clearer as you learn to use the app.  You can find a page later using the search function
* Complete the Onboarding steps to set up Loop
* Learn to use Loop starting with the [Open Loop](../operation/loop/open-loop.md) page
* Once you are comfortable with manually controlling Loop and have settings that work with the algorithm, move on to the [Closed Loop](../operation/loop/close-loop.md) page
* Make [suggestions](../intro/loopdocs-how-to.md#how-to-improve-loopdocs) if you think parts of LoopDocs could be clarified, especially from the viewpoint of a brand-new Looper

### Experienced Loopers

* Review the 3 pages mentioned above for new Loopers and the section for experienced Loopers on the Onboarding page.
* Read the rest of the pages listed under [All Loopers](#all-loopers), below
    - Some of the screens and user interface changed with Loop 3
    - Many of the new Loop 3 features are described
    - Reach out if information is missing or needs to be clarified, [suggestions](../intro/loopdocs-how-to.md#how-to-improve-loopdocs) are always welcome
* LoopDocs design
    * Sections specific to experienced Loopers are after the sections for new Loopers
    * The goal is to make LoopDocs easier for new Loopers to navigate
    * Experienced Loopers can scroll ahead, check the page table of contents or use the search feature

### All Loopers

These pages have a lot of detailed Loop information.

* [Displays](displays_v3.md)
* [Settings](settings.md)
* [Therapy Settings](therapy-settings.md)
* [Optional Services](../operation/loop-settings/services.md)

And a lot of detailed information about Status and Commands for:

* [RileyLink](../operation/loop-settings/rileylink.md)
* [Omnipod Common](omnipod.md)
* [Medtronic](medtronic.md)

## Safety

Please be informed so you can Loop safely.

Consult with your health care professional regarding your diabetes management.

!!! warning "Open Source"
    * The Loop app is an open source project used by many, but it is not approved for therapy by any government organization.
    * **You take full responsibility for building and running this system and do so at your own risk.**
