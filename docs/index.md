---
hide:
    - navigation
---

# Welcome to Loop

We call this website "LoopDocs". It is the place to learn all things Loop. Before you leave this introduction page in your excitement to get to the Build Loop pages, please make a promise to yourself to read all the pages AND read them slowly, without hurry. This provides the greatest chance for successful builds and **<U>SAFE</U>** Loop operation.

You may be overwhelmed or nervous to embark on building your own iPhone application, but don't be. This website has step-by-step instructions with screenshots and helpful arrows for every step. We do not expect people to have any prior technical knowledge ahead of time. The words may be very foreign and technical to most people, but the many screenshots will get you there even if you don't know the meanings of some words. The website is updated regularly to keep pace with Loop developments.

To help, there are navigation buttons are at the bottom of each LoopDocs page, so as you get done with one step or topic, click on the link to the "next" page to continue. There's also a Search tool in the upper right corner for when you aren't sure where to find information.

Finally, we highly recommend reading the [FAQs](faqs/docs-faqs.md) pages several times during your early Loop build and use. How to change your dexcom transmitter and sensor, how to change pods, how to deal with new iPhone, how to build with a windows computer, how much does this cost, etc...all in FAQs.

## Introduction

* Loop is an app you build yourself and load on an iPhone (or iPod)
* Loop predicts where your blood glucose is heading based on carbohydrate intake, insulin on board, CGM data, and your personal therapy settings (e.g., carbohydrate ratio, basal rates, etc). 
* Based on that prediction curve, Loop will automatically make (closed-loop mode) or recommend (open-loop mode) changes in insulin delivery to bring your blood glucose back to your specified target range.
* Loop requires a [compatible continuous glucose monitor (CGM)](build/step4.md) and a [compatible pump](build/step3.md). 
* For people using a compatible Medtronic pump or Eros pods, you'll also need a [pocket-sized device](build/step5.md) for the iPhone and pump to communicate. Originally, there was only one option for that device and it was called a RileyLink. There are newer options available now, in addition to the original RileyLink, with different pros/cons to each. DASH users do not require this device.

![Loop main display on phone](img/phone_updated_loop.svg){width="300"}
![Loop watch screen on watch](img/watch_updated_loop.svg){width="300"}

## Development History

Loop is an open-source, shared project. The entire project has been, and continues to be, done by volunteers. From the code to the website, you're getting all this because dozens of volunteers have given their family time, so please add your time by reading this website thoroughly before embarking on your Loop journey.

In addition to this website, here are links to other resources for you to explore.

  * The early history of Loop development: [History of Loop and LoopKit](https://medium.com/@loudnate/the-history-of-loop-and-loopkit-59b3caf13805), written by Loop developer Nate Racklyeft

  * The early days and the many advances brought about by the We Are Not Waiting diabetes community: [The Artificial Pancreas Book](https://www.artificialpancreasbook.com/) written by Dana Lewis and check out her website [DIYPS](https://diyps.org).

  * How the Omnipod Eros pods were cracked to work with Loop: [Insulin Pumps, Decapped Chips and Software Defined Radios](https://medium.com/@ps2) written by Loop developer Pete Schwamb and [Deep Dip Teardown of Tubeless Insulin Pump](https://arxiv.org/ftp/arxiv/papers/1709/1709.06026.pdf) by Sergei Skorobogatov


!!! warning "Important"
    Please understand that this project:

    - Is highly experimental
    - Is not approved for therapy

    **You take full responsibility for building and running this system and do so at your own risk.**

## Search Tool
It is not uncommon to have a question about Loop. But, it is exceptionally rare to have the question not already answered in LoopDocs, so please bookmark this website and **SEARCH FOR ANSWERS** using navigation menus or the search tool found in the upper right corner of this website.

Search for topics by clicking the Search tool, or typing the letter `s` on your keyboard. As you begin to type, suggested completions and links to pages are displayed.
    <br/><br/>![example of using search](img/new-look-search-example.png){width="600"}<br/>


## Stay in the Loop

or


## Finding Help

Since this is a project used and developed by remotely collaborating volunteers, most of the support and conversations are via online platforms. There are a [number of options](build/step12.md) for you to join in those conversations or as for help. Links to the main platforms are listed below. There are also numerous FB groups that formed by non-US Loop users (Italy, Australia, and several other countries have user groups).

  * The fastest way to get help (with the most mentors) is the [Looped Group](https://www.facebook.com/groups/TheLoopedGroup) on Facebook. Looped Group is the original FB group for DIY looping systems. There are lot of active members there with excellent history of helping people.
  * There is another Facebook group, Loop and Learn, that has a lot of Loop-centric information, a T1D Speaker Series covering many topics of general diabetes interest as well as Loop-specific chats, alerts whenever there is an update to iOS and Xcode, Quick Tips and articles written by mentors providing their Loop experience.
      * [LoopandLearn Facebook Group](https://www.facebook.com/groups/LOOPandLEARN)
      * [LoopandLearn Website](https://www.loopandlearn.org)
* The [LoopTips](https://loopkit.github.io/looptips/) website provides non-build information and is more of a "now that I'm Looping..." resource for how to print endo reports, find Loop data, deal with therapy settings changes, etc. 
* Many Loopers use [Nightscout](nightscout/overview.md). Nightscout help can be found in the [CGM in the Cloud](https://www.facebook.com/groups/CGMinthecloud) Facebook group. 
  * For those not interested in Facebook or interested in what is coming next for Loop, join [Loop Zulipchat](https://loop.zulipchat.com) and be sure to subscribe to all the streams or you'll miss some interesting conversations.  
  * Loop has an instagram account @diy.loop where updates are also shared.


#### Search Then Post

!!! danger "Tips on how to Post for Help"
    If you are having trouble building or using your Loop app, there are some important steps to help you get responses to your question, while also being considerate of our volunteers' time.
    
    1. Always search in **both** [LoopDocs](#search-tool) and in Looped Group. Confused on how to search or use Looped Group? [Here is a video](https://www.youtube.com/watch?v=_vSN6C-Uo04) to help.
    2.  Click on the Announcements section of the Looped Group; nearly a third of posts asking for help these days are already answered in the pinned announcements.
    1. Forcing our groups to repeatedly answer the same question is a sure way to burn-out our volunteers.
    3.  Don't post a duplicate question in multiple groups (mentors monitor many groups). Only post to a different group if you have had no responses for several hours.
    4.  If a LoopDocs search, FB search, and a check of Looped Group announcements haven't answered your question, then post for help. Review the [tips for how to post for help](build/step12.md) so that our volunteers get all the information they'll need to help you, without needing to ask 40 questions first.    
    5.  Leave your question posted even after you've gotten an answer, but edit the original post to add the word **RESOLVED** at the beginning of the original post. 
        * This helps other Loopers who have the same question
        * This helps mentors know they don't need to respond to help you


## LoopDocs Improvements

Please submit suggestions for updates and improvements to this documentation. There are many pages of content and we welcome reviewers to help find typos and outdated info/links. If you notice a typo, poor word choice or some explanation that could be improved or clarified, there are a few options. The first two options use Github, a website where open-source code is often shared.

1. You can issue a Pull Request (best option if it is a simple typo or wording update)
2. You can open an Issue (best option if a major rewrite is needed or you think a conversation would help), or 
3. You can post on Facebook or Zulipchat 

### Pull Requests and Issues

If you decide to do a Github Pull Request (PR) or create an Issue, first look to see if someone has already opened a [PR](https://github.com/LoopKit/loopdocs/pulls) or [Issue](https://github.com/LoopKit/loopdocs/issues) on the topic so you don't create a duplicate.

* If a PR or Issue on the topic is open, feel free to add your comments (don't be shy), but please don't create a duplicate
* If a PR doesn't exist, watch this [LoopDocs Pull Request video](https://youtu.be/6qSppvgGxpg) on how to create one (it's easy, video is less than 5 minutes)
* If your Issue is new, please add it by clicking on the `New Issue` button
    * Give the Issue a descriptive title
    * Indicate which page or pages need updating , along with a brief description of the problem(s)

### Facebook or Zulipchat
Helpful tips for providing LoopDocs feedback through Facebook and/or Zulipchat:

* In [Looped Group](https://www.facebook.com/groups/TheLoopedGroup) - make sure your post is clear that you have a comment about LoopDocs in particular.
* In Loop Zulipchat, please use the [documentation stream, Loopdocs Issue](https://loop.zulipchat.com/#narrow/stream/270362-documentation/topic/Loopdocs.20Issue) channel.

## Repositories and Code

If you're a developer looking for direct links to the code and documentation in Github:

* [Loop](https://github.com/LoopKit/Loop) 
* [LoopDocs](https://github.com/LoopKit/Loopdocs)

For more information on how to contribute code to the project, please review:

  * [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
  * Review the Loop [LICENSE](https://github.com/LoopKit/Loop/blob/master/LICENSE.md)
  * Review the Loop [CODE_OF_CONDUCT](https://github.com/LoopKit/Loop/blob/master/CODE_OF_CONDUCT.md)

If you want to contribute code improvements, please join [Loop Zulipchat](https://loop.zulipchat.com) and be sure to subscribe to all the channels. Meet the developers and testers who make this app, and learn about what is coming next.
