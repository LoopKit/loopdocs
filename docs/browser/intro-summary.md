## Summary of Steps

???+ info "Time Estimate (click to open/close)"
    - If you have never built the *Loop* app (allow up to one week elapsed time)
        * Request and get an <span>*Apple Developer* Account</span>: 1-2 days
        * Create and configure your *GitHub* account and `repositories`: 1-2 hours
        * Add <code>Secrets</code> (requires *Apple Developer* Account): 1 hour
        * Perform the *GitHub* `Action` steps: 30 minutes to 2 hours
    - If you have previously built the *Loop* app with *Xcode* you have fewer steps and are probably familiar with some of the concepts
        * Expect 1 to 4 hours

???+ abstract "Summary for Browser Build with Links (click to open/close)"
    You may be overwhelmed at first with all the new terms and the many steps. Take a deep breath and work through the steps one at a time.

    * Use the template to [Save Your Information](intro-summary.md#make-a-secrets-reference-file){: target="_blank" }

    If you prefer watching your instructions, a narrated video is available:

    * [How to Build the *Loop* App With a Web Browser](https://www.youtube.com/watch?v=kiu5ho0MTW8){: target="_blank" }

    Once you have *Apple Developer* and *GitHub* accounts, the steps below are a high-level summary with links to the detailed `LoopDocs` section.

    You can think of the first part as a scavenger hunt where you find or generate and save six <code>Secrets</code>.

    * _<span translate="no">Apple</span>_:
        * [Collect the four *Apple* <code>Secrets</code>](secrets.md#collect-the-four-apple-secrets){: target="_blank" }
    * *GitHub*:
        * [Collect the <code>GH_PAT</code> Secret](secrets.md#collect-the-gh_pat-secret){: target="_blank" }
    * [Make up a Password](secrets.md#make-up-a-password){: target="_blank" } and save it as your sixth `Secret`

    Now it's time to use those <code>Secrets</code> to build the Loop app

    * *GitHub*:
        * [`Fork` the repository (make your copy of <code>LoopWorkspace</code>)](prepare-fork.md#fork-loopworkspace){: target="_blank" }
        * [Add <code>Secrets</code> to your `fork`](prepare-fork.md#configure-secrets){: target="_blank" }
        * [`Action: 1. Validate Secrets`](identifiers.md#validate-secrets){: target="_blank" }
        * [`Action: 2. Add Identifiers`](identifiers.md#add-identifiers){: target="_blank" }
    * _<span translate="no">Apple</span>_:
        * [Configure Identifiers for *Loop*](prepare-app.md#configure-identifiers-for-loop){: target="_blank" }
        * [Create your version of *Loop* in `App Store` (personal use only, not for distribution)](prepare-app.md#create-loop-app-in-app-store-connect){: target="_blank" }
    * *GitHub*:
        * [`Action: 3. Create Certificates`](certs.md#create-certificates){: target="_blank" }
        * [`Action: 4. Build Loop`](build-yml.md#build-the-loop-app){: target="_blank" }
    * _<span translate="no">Apple</span>_: [Set up `Internal TestFlight Group`](tf-users.md#testflight-users-overview){: target="_blank" }
    * Phone: [Install the *Loop* app using the *TestFlight* app](phone-install.md){: target="_blank" }

???+ question "FAQs (click to open/close)"
    - **Do I need a Mac computer?** No. This can be done on any browser, although it will be easier using a computer or tablet than just using a phone.
    - **Isn't it hard to build every 90 days?** The initial setup and installation take a lot of your focused time. But once you build, future updates and builds are automatic. You just need to keep your Apple Developer account up to date. Review any email that says a GitHub action failed - read the error and take action. For more information, see [Automatic Update & Build](automatic.md){: target="_blank" }.
    - **Can you explain the new automatic building?** There's a whole page on [Automatic Update & Build](automatic.md){: target="_blank" } for more explanations
    - **Can I use this for my child?** You, as the adult, can install using *TestFlight* on your child's phone. The explicit steps are provided at [Install on Phone: *TestFlight* for a Child](phone-install.md#testflight-for-a-child){: target="_blank" }.
    - **Can I still use my customizations?** Yes. [Customize using Browser](custom-browser.md){: target="_blank" }
    - **Is there a build video?** Yes. [How to Build the *Loop* App With a Web Browser](https://www.youtube.com/watch?v=kiu5ho0MTW8){: target="_blank" }

## Tips and Tricks

The steps to configure for building with a browser require a lot of focused attention. Take it in steps and take breaks as needed. Some people prefer a video. Some people prefer more detailed steps on a webpage and others only high-level steps.

!!! important "How to Ask for Help"
    First time setup should take several hours, but if you are having trouble don't get frustrated:

    * [Click here to find help](bb-errors.md#help-with-errors){: target="_blank" }.

### The Short Version

Complete instructions are found at this link for those comfortable with using *GitHub* and navigating the *Apple Developer* and *Apple App Connect* pages.

* [Using GitHub Actions + FastLane to deploy to TestFlight](https://github.com/LoopKit/LoopWorkspace/blob/main/fastlane/testflight.md){: target="_blank" }

### The Video Version

If you prefer watching your instructions, there is a narrated video of each step needed to build using a browser. This video was created for version 3.2.x and some steps have been simplified with version 3.4.x.

* [How to Build the *Loop* App With a Web Browser](https://www.youtube.com/watch?v=kiu5ho0MTW8){: target="_blank" }

Click in the comments for a full index of topics.  If you have issues with a particular section, use the index to advance to the relevant part of the video. Subtitles are in English. You can choose a different language but the automatic translation feature may provide translations that are not completely accurate.

### The Detailed Version

If you prefer seeing step-by-step instructions, those are provided too.

Some sections have a Section Summary for those who just want high-level steps without a lot of graphics. It also provides a high-level view of what you are going to do before you do it.

* To view the summary, click on the summary header
* If the summary is all you need, use the `skip forward` symbol (<span class="loop-big">:material-skip-forward:</span>) to skip to the next instruction
* Or follow the detailed instructions below the summary

## Save Your Information

**Everyone needs to read this section!**

You need to keep a digital copy of your 6 <code>Secrets</code>.

* You need to copy and paste those <code>Secrets</code> to build the app with a browser
* Make sure your editor does not change any characters in your <code>Secrets</code>; use a text-only editor like NotePad (PC) or TextEdit (Mac)
* Many people add other information to the <code>Secrets</code> file for easy reference

!!! info "A Note about Capitalization and Spaces"
    In places, you use a name like "`FastLane API Key`" or "`FastLane Access Token`". Please copy from the docs to use those exact names.

    The <code>Secrets</code> that you add use names that are capitalized and use underscore `_` instead of spaces or hyphens. Be precise and careful.

!!! important "Use a Text-Only Editor"
    **Be sure to use a Text-Only editor like NotePad (PC) or TextEdit (Mac) to archive your information.**

    If you use a "smart" editor, it may change lower-case letters to upper-case letters at the beginning of a line when you paste items into your archive file.

    If even one character is capitalized when it should not be, you will get errors.

### Make a <code>Secrets</code> Reference File

Please save yourself a lot of agony. Make a <code>Secrets</code> Reference folder and then create a <code>Secrets</code> Reference file in it.

You don't need to know anything about the <code>Secrets</code> to do this. Come up with your own names, but make sure you know where you put this file.

1. Decide where you want your <code>Secrets</code> saved and create a special folder
2. Open a text-only editor (do not use a Smart Editor, those might change capitalization or formating and ruin your <code>Secrets</code>)
    * Create a blank <code>Secrets</code> Reference file using the text-only editor
    * Tap on the copy icon below to copy the template and paste it into your blank file
    * Save the file
3. As you move through the steps of [Collect Secrets](secrets.md){: target="_blank" }, fill in the file
    * The `##` characters are used to indicate sections or title (text only file)
    * There is a reference pattern for each SECRET: replace that with your SECRET or you can add your secret below the pattern to give yourself confidence you got the correct item
4. In addition to the <code>Secrets</code>, this template has places for other pieces of information you may find handy to save in the same file
5. At the very beginning is a place to indicate the last day you updated the file

``` { .bash .copy title="Template to use for Secrets" }
MySecretsReferenceFile.txt

## This file updated on: DD MMM YYYY

Information needed to use Browser Build.
The same secrets are used for every app you build.

First some handy username and password information:

## Apple ID username for your Developer account is the associated email:
<your information here>
suggest you use your desired password tool to save the password for this account

## GitHub username
<your information here>
suggest you use your desired password tool to save the password for this account

These are the Six Secrets in alphabetical order - each one shows the expected format.
Delete each prototype as you gather your own secrets.
The letter A indicates an alphanumeric character.
Some may be lower case, some upper case and some numerals.
The FASTLANE_KEY may have additional characters included.
For that one copy the entire key
including -----BEGIN PRIVATE KEY-----
through
-----END PRIVATE KEY-----

## SECRETS BELOW:

TEAMID
<looks like this>
AAAAAAAAAA

FASTLANE_ISSUER_ID
<looks like this>
AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA

FASTLANE_KEY_ID
<looks like this>
AAAAAAAAAA


FASTLANE_KEY
<looks like this>
-----BEGIN PRIVATE KEY-----
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAA
-----END PRIVATE KEY-----

GH_PAT
<looks like this>
ghp_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

MATCH_PASSWORD
<looks like this>
AnyThingYouWant-sameForEveryRepository

## Repository Names for my Fork:

https://github.com/my-github-username/LoopWorkspace

Add additional apps here if you decide to build any
```

## New Terms with <code>*GitHub* Browser Build</code>

The <code>*GitHub* Browser Build</code> may use new and unfamiliar **terms**.

These instructions can be used without knowing what any of these terms mean. But if you are curious:

Some of these **terms** have ToolTips, so hover your mouse over those - or review them in the [Glossary](../faqs/glossary.md){: target="_blank" }.

* Some terms in the Glossary are not in alphabetical order to improve logical grouping. All the individual <code>Secrets</code> are listed after <code>Secrets</code> in the Glossary.

* `Actions`: available in your *GitHub* account to build your app (once you configure your repository)
    * You must be logged in to *GitHub* to run the actions
* <code>Secrets</code>: are required to enable *GitHub* to build the *Loop* app using *GitHub* Actions
    * Six <code>Secrets</code> must be added to your fork of LoopWorkspace
    * These <code>Secrets</code> work for any branch in your fork (`main` or `dev`, for example)
    * If you build [Other Apps](other-apps.md){: target="_blank" }, they use the same <code>Secrets</code>
    * For those who feel confident using *GitHub*, there are optional instructions to configure a free organizational account (for your personal use) that allows you to enter the <code>Secrets</code> only once and have them available for every repository in that organization account; see [Use a *GitHub* Organization Account](other-apps.md#use-a-github-organization-account){: target="_blank" }
* API `Key`:`Application Programming Interface Key`
    * You create an API key from the *Apple Developer* website
    * Doing this provides 3 of your <code>Secrets</code>
    * These secrets enable your *GitHub* account to interface with *Apple* to create your app
* `Identifiers`: are required to build the *Loop* app with <code>*GitHub* Browser Build</code> (these are automatically generated for you) when you run `Add Identifiers`
* [`App Store Connect`](https://appstoreconnect.apple.com){: target="_blank" }: a website available for *Apple Developer*s to review apps build with your *Apple Developer* account
    * Once you purchase an *Apple Developer* annual account, you are an *Apple Developer* and have access to this site
    * Most Loopers will not have an App until using the <code>*GitHub* Browser Build</code>
    * The instructions walk you through creating and naming your app: [Create Loop App in App Store Connect](prepare-app.md#create-loop-app-in-app-store-connect){: target="_blank" }

## Next Step

The next step is to [Collect and Save Secrets](secrets.md).