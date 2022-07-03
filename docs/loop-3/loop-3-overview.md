# Loop 3 Overview


Loop 3.0 will be the next big release. It is being developed and tested under the dev branch (Loop-dev). Loop-dev has significant improvements and looks different (in some ways) from the Loop 2.2.x versions.

!!! info "Loop-dev"
    At the current time, the dev branch of Loop is under test by experienced loopers. If you are testing Loop-dev, the version number reported on your settings screen is Loop v2.3.0 (57). 

    To report to developers about which particular version of Loop-dev you are running, look at the top of the [Loop Report](settings.md#issue-a-loop-report) under `Build Details`. The 7-digit alphanumeric indication to the right of workspaceGitRevision is sufficient.
    
    When this version is released, it will be Loop 3.0 and the interface for Loop 3.x versions will use this updated documentation.


!!! danger ""

    To make life easier for those of us preparing the new documentation, the wording on many pages in the Loop 3 section is set in the future - after the release
    
    This page will be updated and it and the rest of the Loop 3 section will be moved to Set Up App with the Loop 2.2.x version maintained under a sub-menu


## New with Loop 3

!!! info ""
    Information from this section will be moved to the Version / Releases page after release.

Loop 3 provides a major redesign of the app, building off the public portion of some Tidepool work in addition to the DIY contributors. There is a lot of work "under-the-hood" with Loop 3 that may not be obvious to the user, but makes the app more robust.

Here are some highlights:

* Onboarding protocol with guardrails to assist in configuring settings
* Streamlined main screen display and user experience
* Better alerts and notifications
* Omnipod Dash compatibility
* Fingerstick blood glucose prompts when data is stale
* Non-pump insulin entry within the app
* Remote Carb/Bolus capability


## Building Loop 3

When Loop 3 is released, the build instructions will be updated (please allow a few days for documentation to catch up.) In the meantime, experienced users are testing Loop-dev and starting with the [Loop-dev](../build/step13.md#advanced-users-only) download and build instructions. Do not build Loop-dev unless you are willing to pay attention to announcements on zulipchat and build frequently (plan on once a week.)

!!! warning "Users of dev Branch"
    It is up to you to review these new pages for the information you need.
    
    Please subscribe to the [Documentation Stream](https://loop.zulipchat.com/#narrow/stream/270362-documentation) on zulipchat. You will see a post there every time LoopDocs is updated.


Those of us who have been testing Loop-dev are very excited for this major update.

## Set Up Loop 3 Overview

!!! success "Congratulations on Building Loop!"

The first time you build Loop 3 on your device, as either a new Looper or an experienced Looper, you will be going through the [Onboarding](onboarding.md) process. But don't click on that link yet.

First some orientation:

### Brand New Loopers

* Please review in detail these 3 pages before you touch any buttons on your app
    * [Onboarding](onboarding.md)
    * [Add CGM](add-cgm.md)
    * [Add Pump](add-pump.md)
* Read the rest of the Set Up section with an eye to understanding that while some of the information may not be clear now, as you learn to use the app, you'll know the information exists and can return (or use the search function)
* Then move on to learning the Loop app starting with the [Open Loop](../operation/loop/open-loop.md) page
* Once you are comfortable with manually controlling Loop and feel you have your settings adjusted for the algorithm, move on to the [Closed Loop](../operation/loop/clos-loop.md) page
* Make suggestions if you think parts of LoopDocs could be clarified, especially from the viewpoint of a brand-new Looper

### Experienced Loopers

* There is no harm in completely reviewing the 3 pages mentioned above for new Loopers
* There is a section for experienced Looper on the Onboarding page.
* Read the rest of the Set Up pages - you will learn a lot of new Loop 3 features by doing this and save asking mentors questions when the answers are found in LoopDocs
* Make suggestions if you think parts of LoopDocs could be clarified, especially from the viewpoint of an experienced Looper switching to Loop 3
    * Please note that sections specific to experienced Loopers are being moved after the sections aimed at new Loopers
    * The goal is to make LoopDocs easier for new Loopers to navigate
    * Experienced Loopers can scroll ahead, check the page table of contents or use the search feature

### All Loopers

!!! abstract "Please Review Detailed Pages"
    There is a lot of detailed information in the Set Up App section.

    * [Displays](displays_v3.md)
    * [Settings](settings.md)
    * [Therapy Settings](therapy-settings.md)
    * [Optional Services](../operation/loop-settings/services.md)

    Status and Commands for :

    * [RileyLink](../operation/loop-settings/rileylink.md)
    * [Omnipod Common](omnipod.md)
    * [Medtronic](medtronic.md)

## Safety

Please be informed so you can Loop safely.

Please consult with your health care professional regarding your diabetes management. 

!!! warning "Open Source"
    * The Loop app is an open source project used by many, but it is not approved for therapy by any government organization. 
    * **You take full responsibility for building and running this system and do so at your own risk.**
