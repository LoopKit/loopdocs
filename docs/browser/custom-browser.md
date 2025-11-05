## Overview

**This page is only relevant when building with a browser.**

**For *Mac*, please see: [Customize with *Mac*](../build/custom-mac.md)**

For new Loopers, please build the code before you make any changes. Start with Open Loop and familiarize yourself with the interface. Later, you can make the customization(s) you desire and build again. The second build will be much easier than your first build.

These customizations require you to modify the code used to build the *Loop* app and then build the app again with the modified code.

!!! warning "You take responsibility"
    You are responsible when you decide to use customizations.

    Be sure to report what changes you made if you need to ask for assistance with your app.

## Customizations Prepared for You

Some customizations are the same for everyone and have been prepared for easy use.

The *Loop and Learn* team commits to maintaining these prepared customizations and provides an easy method to add your selection from these customizations to your version of *Loop*.

Please read the documentation for these on the [Loop and Learn: Customization Select Page](https://www.loopandlearn.org/custom-code):

* [List of Customizations Available](https://www.loopandlearn.org/custom-code#custom-list)
* When building using a browser you will be modifying one of the special files that enable the *GitHub* action to build the *Loop* app. This file is called the build_loop.yml file and can be located at your `fork` of your `LoopWorkspace` repository. There are several sections you need to review on the *Loop and Learn* page:
    * You will copy a template that you paste into that file and then edit it to keep just the customizations you want
    * [Overview](https://www.loopandlearn.org/custom-code-browser-build/){: target="_blank" } of how to modify the build_loop.yml file
    * [Template for `main`](https://www.loopandlearn.org/custom-code-browser-build/#template-main){: target="_blank" }
    * [Template for `dev`](https://www.loopandlearn.org/custom-code-browser-build/#template-dev){: target="_blank" }

## Personal Customizations

Some customizations must be created for yourself. These are of two basic types: Custom Edits and Build-Time Flag.

The information needed to modify the code to make these customizations is found in the Versions tab because the information is independent of build method (think of these as your personal versions). The links are found below.

* [Version: Custom Edits](../version/code-custom-edits.md)
    * The page linked above indicates how you can modify behavior by editing the code
* [Version: Build-Time Flag](../version/build-time-flag.md)
    * By enabling or disabling features controlled by a Build-Time Flag, you are turning on or off features included in the code by the developers that they configured to be off or on by default
    * Please read about these flags on the page linked above

When preparing these personal edits using a browser, there is a page explaining how to get these edits into your personal `fork` of `LoopWorkspace` prior to building.

* [Custom Edits with Browser](edit-browser.md)

## Details at Links

The code changes required for these customizations are the same regardless of the build method. The pages that provide the documentation on modifying and incorporating these changes are found at the links above.
