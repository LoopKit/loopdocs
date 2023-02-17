## LoopDocs Contents

The LoopDocs website is organized as follows

* [Home](../index.md): What is Loop?
* [Intro](overview-intro.md): Introduction to Loop and LoopDocs
    * [Requirements](requirements.md): What is needed regardless of build method
* New with Loop 3: Two ways to build
    * [Browser Build](../gh-actions/gh-overview.md): Build Loop app using a browser (Mac computer not required)
    * [Mac-Xcode Build](../build/overview.md): Build Loop app with a Mac the first time, or [Update](../build/updating.md) next time
* [Set Up](../operation/overview.md): How to set up your Loop app
* [Operate](../operation/loop/open-loop.md): How to use the Loop app
* [Troubleshoot](../troubleshooting/overview.md): What to do if you're having trouble with the Loop app
* [Version](../version/overview-version.md): Information about Loop versions, code customization and development
* [Nightscout](../nightscout/overview.md): Loop-specific Nightscout details; Nightscout is a companion application that many Loopers use
* [FAQs](../faqs/overview-faqs.md): Pages with safety tips, frequently asked questions and the Glossary
* [Translation](../translate.md): Links to Google Translate provided as a convenience, no guaratees about the quality of the translation

It is totally understandable if the thought of building and operating your own Loop app feels intimidating. As you learn the information explained in LoopDocs, this will start feeling more comfortable.


## Building Loop

The process for building the Loop app is divided into short segments (sections or pages) in the Build tabs of LoopDocs.

!!! warning "Best Practice: Learn to Build"
    You are strongly encouraged to build Loop for yourself.

    * No links to providers who build Loop as a service  are found in LoopDocs
    * If you choose to use such a service, before you begin, you should:
        * Read all of LoopDocs
        * Know how to Set up and Operate Loop
        * Ask what features, if any, available with DIY loop are not available with their service
        * **These steps are important for your safety**

### Using a Simulator

You can build Loop and practice with a simulated phone, CGM and  pump. You can "dose" the simulated pump and your real pump at the same time and watch the glucose predictions.

Starting with a simulator can help you decide if you want to move forward with purchasing additional items required to Loop.

Please review [Simulator Build](../version/simulator.md) for more information.

#### Simulator using Browser Build:

* No Mac computer required
* Must have a paid Apple Developer ID ($99/year)
* Must have a compatible phone

#### Simulator using Mac-Xcode Build:

* Must have a Mac computer (or virtual machine, Intel chips only)
* Can build the simulator with a free Apple Developer ID
    * Build to Mac (no phone required)
    * Build to compatible phone

## Operating Loop

A significant amount of content is provided on this website and via link to other sources. Please review these pages when initially setting up and learning to use Loop.

Some techniques are specific to Loop, but the general concepts of how man-made insulin works and strategies to test basal, carb ratios and insulin sensitivity apply to all the hybrid closed-loop systems, commercial and open source.

## Development History

Loop is an open-source, shared project. The entire project has been, and continues to be, done by volunteers. From the code to the website, you're getting all this because dozens of volunteers have given their time, so please add your time by reading this website thoroughly before embarking on your Loop journey.

Here are development history links to other resources for you to explore.

* The early history of Loop development:
    * [History of Loop and LoopKit](https://medium.com/@loudnate/the-history-of-loop-and-loopkit-59b3caf13805), written by Loop developer Nate Racklyeft

* The early days and the many advances brought about by the `#We Are Not Waiting` diabetes community:
    * [The Artificial Pancreas Book](https://www.artificialpancreasbook.com/) written by Dana Lewis and check out her website [DIYPS](https://diyps.org).

* How the Omnipod Eros pods were cracked to work with Loop:
    * [Insulin Pumps, Decapped Chips and Software Defined Radios](https://medium.com/@ps2) written by Loop developer Pete Schwamb
    * [Deep Dip Teardown of Tubeless Insulin Pump](https://arxiv.org/ftp/arxiv/papers/1709/1709.06026.pdf) by Sergei Skorobogatov
