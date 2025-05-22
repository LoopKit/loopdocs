!!! tip "Take a deep breath"
    It is totally understandable if the thought of building and operating your own&nbsp;<span translate="no">Loop</span>&nbsp;app feels intimidating.
    
    As you learn the information explained in&nbsp;_<span translate="no">LoopDocs</span>_, this will start feeling more comfortable.

## <span translate="no">LoopDocs</span>&nbsp;Contents

The&nbsp;_<span translate="no">LoopDocs</span>_&nbsp;website is organized as follows

* [Home](../index.md): What is&nbsp;<span translate="no">Loop</span>?
* [Intro](overview-intro.md): Introduction to&nbsp;<span translate="no">LoopDocs</span>
    * [Requirements](requirements.md): What is needed regardless of build method
* There are two ways to build - you get the same app either way
    * [Build with Browser](../browser/bb-overview.md): Build&nbsp;<span translate="no">Loop</span>&nbsp;app using a browser on any computer or tablet
    * [Build with *Mac*](../build/overview.md): Build&nbsp;<span translate="no">Loop</span>&nbsp;app with a Mac the first time, or [Update](../build/updating.md) next time
* [Set Up](../loop-3/loop-3-overview.md): How to set up the&nbsp;<span translate="no">Loop</span>&nbsp;app
* [Operate](../operation/loop/open-loop.md): How to use the&nbsp;<span translate="no">Loop</span>&nbsp;app
* [Troubleshoot](../troubleshooting/overview.md): What to do if you're having trouble with the&nbsp;<span translate="no">Loop</span>&nbsp;app
* [Version](../version/overview-version.md): Information about&nbsp;<span translate="no">Loop</span>&nbsp;versions, code customization and development
* [<span translate="no">Nightscout</span>](../nightscout/overview.md): <span translate="no">Loop</span>-specific&nbsp;<span translate="no">Nightscout</span>&nbsp;details; [<span translate="no">Nightscout</span>](https://nightscout.github.io/) is an open-source cloud application used by people with diabetes and their caregivers
    * [Remote Overview](../nightscout/remote-overview.md): Overview on issuing commands remotely to a&nbsp;<span translate="no">Loop</span>&nbsp;app using&nbsp;<span translate="no">Nightscout</span>&nbsp;and Apple Push Notifications
    * [LoopCaregiver](../nightscout/loop-caregiver.md): Companion app useful for remote commands
* [FAQs](../faqs/overview-faqs.md): Pages with safety tips, frequently asked questions and the Glossary
* [Translation](../translate.md): Links to Google Translate provided as a convenience, no guarantees about the quality of the translation

### Using Links

You will notice many links in the *LoopDocs* pages pointing to detailed information. 

* If you notice an arrow pointing up and to the right beside the link:
    * This means a new tab or window (depending on your browser configuration) is opened when you click on the link
    * For example, the [What is Loop?](https://youtu.be/64qhgnmkyAE) video is found on *YouTube*

* This link format is used anytime the link will take you to a different website
* In some cases, it is also used when referring to a different *LoopDocs* page

### Using Tooltips

The *LoopDocs* pages contain words that may be unfamiliar. For a definition of any word with a dashed underline, simply hover your mouse over the word, or tap on the word on a mobile device, to view the definition. For example, Omnipod has a tooltip.

Every tooltip definition is also found in the [Glossary](../faqs/glossary.md) - so head over there if you have trouble reading a tooltip.

## Building&nbsp;<span translate="no">Loop</span>

The process for building the&nbsp;<span translate="no">Loop</span>&nbsp;app is divided into short segments (sections or pages) in the Build tabs of&nbsp;<span translate="no">LoopDocs</span>.

* [Build with Browser](../browser/bb-overview.md)
    * Build with a browser on any computer or tablet
    * App is installed on the iPhone using *TestFlight*
* [Build with *Mac*](../build/overview.md)
    * App is built on a *Mac* with *Xcode* connected to the iPhone
    * The operating system on the *Mac* and the version of *Xcode* must be kept up-to-date

!!! warning "Best Practice: Learn to Build"
    You are strongly encouraged to build&nbsp;<span translate="no">Loop</span>&nbsp;for yourself.

    * No links to providers who build&nbsp;<span translate="no">Loop</span>&nbsp;as a service  are found in&nbsp;<span translate="no">LoopDocs</span>
    * If you choose to use such a service, before you begin, you should:
        * Read&nbsp;<span translate="no">LoopDocs</span>
        * Know how to Set up and Operate&nbsp;<span translate="no">Loop</span>
        * Ask what features, if any, available with DIY loop are not available with their service
        * **These steps are important for your safety**

### Use a Simulator

You can build&nbsp;<span translate="no">Loop</span>&nbsp;and practice with a simulated phone, CGM and/or pump. You can "dose" the simulated pump and your real pump at the same time and watch the glucose predictions.

Starting with a simulator can help you decide if you want to move forward with purchasing additional items required to use the app. You can:

* Learn the interface
* Explore glucose predictions and dosing recommendations

!!! warning "Locked Phone or App in Background"
    Do not expect the simulator to work when the phone is locked or the app is in the background. The app relies on a real insulin pump or a real CGM to wake up the app when the phone is locked or the app is in the background. The simulator cannot do this.

Please review [Simulator Build](../version/simulator.md){: target="_blank" } for more information.

## Operating&nbsp;<span translate="no">Loop</span>

A significant amount of content is provided on this website and via link to other sources. 

Please review these pages when initially setting up and learning to use&nbsp;<span translate="no">Loop</span>.

Some techniques are specific to&nbsp;_<span translate="no">Loop</span>_, but the general concepts of how man-made insulin works and strategies to test basal, carb ratios and insulin sensitivity apply to all the hybrid closed-loop systems, commercial and open source.

## Development History

<span translate="no">Loop</span>&nbsp;is an open-source, shared project. The entire project has been, and continues to be, done by volunteers. From the code to the website, you're getting all this because dozens of volunteers have given their time, so please add your time by reading this website thoroughly before embarking on your&nbsp;<span translate="no">Loop</span>&nbsp;journey.

Here are development history links to other resources for you to explore.

* The early history of&nbsp;<span translate="no">Loop</span>&nbsp;development:
    * [History of&nbsp;<span translate="no">Loop</span>&nbsp;and&nbsp;<span translate="no">LoopKit</span>](https://medium.com/@loudnate/the-history-of-loop-and-loopkit-59b3caf13805), written by&nbsp;<span translate="no">Loop</span>&nbsp;developer Nate Racklyeft

* The early days and the many advances brought about by the `#We Are Not Waiting` diabetes community:
    * [The Artificial Pancreas Book](https://www.artificialpancreasbook.com/) written by Dana Lewis and check out her website [DIYPS](https://diyps.org).

* How the Omnipod Eros pods were cracked to work with&nbsp;<span translate="no">Loop</span>:
    * [Insulin Pumps, Decapped Chips and Software Defined Radios](https://medium.com/@ps2) written by&nbsp;<span translate="no">Loop</span>&nbsp;developer Pete Schwamb
    * [Deep Dip Teardown of Tubeless Insulin Pump](https://arxiv.org/ftp/arxiv/papers/1709/1709.06026.pdf) by Sergei Skorobogatov
