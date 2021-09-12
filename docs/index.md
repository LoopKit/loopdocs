# Welcome to Loop

## Introduction

What is Loop?

* Loop is an app you build yourself and load on your iPhone (or iPod)
* Loop assists in the many insulin dosing decisions people with diabetes face every day
* Loop uses a compatible continuous glucose monitor (CGM) and is paired using the RileyLink protocol with your compatible pump
    * Loop works with older Medtronic pumps and the Eros (not Dash) Omnipods
    * Loop requires a [RileyLink compatible device](build/step5.md#rileylink-compatible-devices) to communicate between the phone and pump

What CGMs work with Loop?

The Loop app works with Dexcom’s G4, G5 and G6 CGM. For Medtronic users, Loop also works with first generation Guardian and Guardian 2 Medtronic sensors compatible with the 522, 722, 523 and 723 pumps. There are other versions of Loop available that may work for you if you are not using one of these specific CGMs.  These other versions (known as forks) are created by Loop users and are maintained by them. This document does not cover those other CGM options, but check out the [Community Information](index.md#stay-in-the-loop) below.

![Loop main display on phone](img/phone_updated_loop.svg){width="300"}
![Loop watch screen on watch](img/watch_updated_loop.svg){width="300"}

!!! warning "Important"
    Please understand that this project:

    - Is highly experimental
    - Is not approved for therapy

    **You take full responsibility for building and running this system and do so at your own risk.**

The Loop algorithm on your phone predicts future glucose based on carbohydrate intake, insulin on board, and current CGM readings. You enter your own settings for desired correction range, basal schedule, insulin sensitivity factor (ISF), carbohydrate ratio (CR) and the type of insulin you are using.  The glucose predictions, using your settings and meal entries, provide Loop with the information needed to recommend a bolus or temporary basal rate to attain a targeted glucose range in the future.

The system can either operate “open-loop” where insulin delivery recommendations must be enacted by the user or “closed-loop” where modifications to insulin delivery are enacted automatically.

You may be saying, "I can't build an app." But the wonderful volunteers in this community prepared this amazing website with step-by-step instructions containing pictures and arrows (say thank you to Katie DiSimone). The website is updated by more volunteers as improvements are made to the Loop app and when Apple makes changes to its iOS, Xcode and macOS environment. This language may sound scary, but it will become easier. Most people who Loop want to keep looping, so they learn the terminology and how to reach out to mentors for help.

Once you've built the app, plan to learn to use it in stages. First, run “open loop” to familiarize yourself with Loop’s operation. This allows you to understand why Loop is making certain recommendations and determine if you need to adjust your Loop settings.

One thing many new users ask is why do my settings need to be different for Loop?  The main reason is that Loop uses a realistic insulin model including the long tail of residual insulin activity - and updates its calculations every 5 minutes. This is a different way of thinking about insulin delivery. Other strategies, e.g., assuming a linear fall-off model for insulin activity, correcting 2 or 3 hours after a meal, trading a higher basal rate to avoid worrying about snacks, etc. will not work.  There is a whole section on settings - just giving you a heads up.

When you progress to “closed-loop”, do so safely by starting with conservative Correction Ranges and Delivery Limits and only progress to more aggressive settings after several days of no lows. Please ask questions at this point about why Loop is making the recommendations it does.  It should be similar to the therapy decisions you would make yourself.  If the recommendations it makes are different than you would make, try to figure out why. Hint - it is probably your settings.

## How to Use These Docs

* Use the navigation menu at the top of the screen
    * Most menu items are only one level deep - so you see all the underlying pages by clicking on the menu name
    * Operate has a few top-level items plus 4 drop-down menus; the easiest way to go through these pages is hitting Next or the letter `n`
        * Operate->How To Use Loop App
        * Operate->Looping Tips
        * Operate->Algorithm
        * Operate->Troubleshoot
* Use the Table of Contents for the current page, which is displayed on the left side of the screen
    * On mobile devices, at the top of the page, tap the down arrow on the upper left to display the TOC, tap again to dismiss it
* Read (or at least skim) pages sequentially the first time through
    * Type the letter `n` for next and `p` for previous to navigate
* Search for topics by clicking the Search icon or typing the letter `s` on your keyboard
    * As you type in the search box, suggested section headings with the first few rows of content will show up below the search bar
    * Scroll down and select the Heading Title of the section of interest
    * If you hit return, the Search display vanishes
<br/><br/>![how to use the search for this site](img/search_example.png){width="400"}<br/><br/>
* There is another website, [Looptips](https://kdisimone.github.io/looptips/), you should review
    * While these articles were written and illustrated with an earlier version of Loop, they are well worth reading
    * This link is repeated on the Operate->Looping Tips->Loop Tips page

## Stay in the Loop!

There are a number of social media options. (Read the directions on each of these - some ask you to answer questions - please do so):

  * The fastest way to get help (with the most mentors) is [The Looped Facebook Group](https://www.facebook.com/groups/TheLoopedGroup).
  * There is another group, Loop and Learn, that has a lot of Loop-centric information, a T1D Speaker Series covering many topics of general diabetes interest as well as Loop-specific chats, alerts whenever there is an update to iOS and Xcode, Quick Tips and articles written by mentors providing their Loop experience.
      * [LoopandLearn Facebook Group](https://www.facebook.com/groups/LOOPandLEARN)
      * [LoopandLearn Website](https://www.loopandlearn.org)
  * Both the Looped and LoopandLearn Facebook groups provide support for some Loop forks, which support other CGM, as well as other DIY closed loop options.
  * Many Loopers use the Nightscout tool to assist them in monitoring their settings in Loop. The fastest Nightscout help can be found in the original #wearenotwaiting community [CGM in the Cloud](https://www.facebook.com/groups/CGMinthecloud).
  * For those not interested in Facebook or interested in what is coming next for Loop, join [Loop Zulipchat](https://loop.zulipchat.com) and be sure to subscribe to all the streams or you'll miss some interesting conversations.  

### Search Then Post

!!! danger ""
    It's really easy to panic if Loop is not working for you, but take the time to do a quick search in your favorite social group before posting a question. You might get an answer immediately.

    Please post your question in only one group on Facebook or under one stream on zulipchat - many mentors monitor more than one place. If you don't hear an answer in 24 hours, then try a different place

    On Facebook the protocol is:

    * Search to see if your question has already been answered
    * Add a comment if you find an existing post to say "I had this problem too and this post helped" - this bumps that post near the top so other can see it
    * Make a new post if you still have a question
    * Leave your question posted after you've gotten an answer, but edit the original post to say it's been resolved (add the word RESOLVED to the beginning of the original post)
        * Mentors save time - they know you've been helped and don't need to read all the comments on that post
        * Others may have the same question and will read your post


## Contribute

Please submit suggestions for updates and improvements to this documentation. If you notice a typo, poor word choice or some explanation that could be improved or clarified, there are a couple of options (more instructions follow):

* You can issue a Pull Request (best if it is a simple typo or wording update)
* You can open an Issue (best if a major rewrite is needed or you think a conversation would help)
* You can post on Facebook or Zulipchat

If you decide to do a Pull Request (PR) or create an Issue, first look to see if someone has already opened a [PR](https://github.com/LoopKit/loopdocs/pulls) or [Issue](https://github.com/LoopKit/loopdocs/issues) on the topic so you don't create a duplicate. Note - you do not have to log in to github to review the PR and Issues, but you cannot comment or add a new PR or Issue without logging in.

* If a PR or Issue on the topic is open, feel free to add your comments (don't be shy)
* If a PR doesn't exist, watch this [LoopDocs Pull Request video](https://youtu.be/6qSppvgGxpg) on how to create one (it's easy, video is less than 5 minutes)
* If your Issue is new, please add it by clicking on the `New Issue` button
    * Give the Issue a descriptive title
    * Indicate what page or pages need updating with a brief description
    * This opens the conversation (those who signed up to `watch` the loopdocs repository get a notice)
    * This collaboration is quite useful in finalizing changes


If you do not have a github userID, but are a member of the Loop Facebook group or Loop Zulipchat, you can post a message there.  

* On [Facebook](https://www.facebook.com/groups/TheLoopedGroup) - make sure your post is clear that you have a comment about LoopDocs
* On Loop Zulipchat, please use the [documentation stream, Loopdocs Issue](https://loop.zulipchat.com/#narrow/stream/270362-documentation/topic/Loopdocs.20Issue) topic

There are many pages of content and we need all the reviewers we can get to help find typos and pages that need to be updated.

For those interested in delving deeper, see the next few sections.

## Development History

Loop is an open-source, shared project.

  * Read about the early history of Loop development: [History of Loop and LoopKit](https://medium.com/@loudnate/the-history-of-loop-and-loopkit-59b3caf13805), written by Loop developer Nate Racklyeft

  * Read about the early days and the many advances brought about by the greater Diabetes Community of people who are not waiting: [The Artificial Pancreas Book](https://www.artificialpancreasbook.com/) written by Dana Lewis and check out her website [DIYPS](https://diyps.org)

  * Read about how hard it was to get a new insulin pump (Omnipod) to work with Loop: [Insulin Pumps, Decapped Chips and Software Defined Radios](https://medium.com/@ps2) written by Loop developer Pete Schwamb and [Deep Dip Teardown of Tubeless Insulin Pump](https://arxiv.org/ftp/arxiv/papers/1709/1709.06026.pdf) by Sergei Skorobogatov

The project continues to be a labor-of-love by a community of users; maintained and improved by volunteers.

## Information for Coders

[Loop](https://github.com/LoopKit/Loop) is an app template for building an automated insulin delivery system. It is a stone resting on the boulders of work done by many others.

The app is built on top of [LoopKit](https://github.com/LoopKit/LoopKit). LoopKit is a set of frameworks that provide data storage, retrieval, and calculation, as well as boilerplate view controllers used in Loop. Using the open-source Loop app template, you can build an insulin delivery system that uses specific commercial and open-source hardware and software technologies to bring together the insulin pump, continuous glucose monitor (CGM), and insulin dosing algorithm to create a DIY automated insulin delivery system. This version is known as Loop.  

For more information on how to contribute to an open-source project, please review:

  * [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
  * Review the Loop [LICENSE](https://github.com/LoopKit/Loop/blob/master/LICENSE.md)
  * Review the Loop [CODE_OF_CONDUCT](https://github.com/LoopKit/Loop/blob/master/CODE_OF_CONDUCT.md)

Then if you want to contribute, please join [Loop Zulipchat](https://loop.zulipchat.com) and be sure to subscribe to all the channels. Meet the developers and testers who make this app the life-changing tool that so many people use. Learn about what is coming next.
