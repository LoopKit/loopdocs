Volunteers answer questions about the *Loop* app. They are not paid. Doing your homework and giving them the details they need gets you a faster answer.

## How to Ask for Help

If you are having trouble building or using your Loop app, there are some important steps to get responses to your question, while also being considerate of our volunteers' time.

> If you are in a panic about something, it's ok to post in [`LoopandLearn` Facebook Group](https://www.facebook.com/groups/LOOPandLEARN) without searching all the places listed below. 
Just explain the situation and someone will give you an answer pretty quickly. For non-panic situations, try searching - you may learn a lot.

1. Always search in **both** [LoopDocs](../intro/overview-intro.md#website-search) and your favorite [support group](../intro/loopdocs-how-to.md#how-to-find-help). 
    * Confused about how to search in a Facebook group? [Here is a video](https://www.youtube.com/watch?v=_vSN6C-Uo04) to help.
2.  If you use Facebook, click on the Featured posts (at the top of the page); many posts asking for help are already answered there.
3.  Don't post a duplicate question in multiple groups (mentors monitor many groups). Only post to a different group if you have had no responses for several hours.
4.  If a LoopDocs search, FB or Zulipchat search, and a check of Looped Group featured posts pinned to the top of the page haven't answered your question, then post for help. Review the [tips for how to post for help](#descriptive-language) so that our volunteers get all the information they'll need to help you, without needing to ask 40 questions first.    
5.  Leave your question posted even after you've gotten an answer, but edit the original post to add the word **RESOLVED** at the beginning of the original post. 
    * This helps other Loopers who have the same question
    * This helps mentors know they don't need to respond to help you

## Screenshots

Please take screenshots of your issue and include them in your posts - unless you want Browser Build help. **For Browser Build, include your URL, not a screenshot.**

### Help with the app

If you are asking for help using the *Loop* app after you've already built it, take screenshots on your phone and upload to either Facebook or zulipchat along with your question.

If you are posting *Nightscout* graphics, use the full window from either your phone or your computer in your screenshot.

> [How to Find Help](../intro/loopdocs-how-to.md#how-to-find-help){: target="_blank" }

### Help with Browser Build

If you need help with building the app using a browser, copy the URL for the LoopWorkspace fork and paste it into Facebook or zulipchat along with your question.

> [How to Find Help](../intro/loopdocs-how-to.md#how-to-find-help){: target="_blank" }

### Help with Mac Build

If you are building with a Mac computer and need assistance, **use screenshots** from your Mac computer. Taking a cell phone photo of your Mac screen is generally insufficient.

Include full window capture when asking for help. The *Nightscout* and *Xcode* apps have lots of valuable information off-to-the-side that can be valuable for troubleshooters.

> [How to Find Help](../intro/loopdocs-how-to.md#how-to-find-help){: target="_blank" }

#### How to Obtain a Screenshot on a Mac

On an Apple computer, press ++shift+command+4++ keys at the same time and a little crosshairs tool will appear. Click-and-drag across the area you'd like to include in the screenshot. When you let go of the button, the screenshot will be saved to your desktop with a file name starting with the name `Screenshot`. To capture an entire window, press ++shift+command+4++ keys at the same time followed by pressing ++space++ (the  space bar) and then click on the window of interest.

## Descriptive Language

Use descriptive language - the most accurate, detailed words possible - when asking for help. Try to avoid the word "it" and instead use details and information to explain why you're asking for help, what you've already tried, and what happened when you tried those things (including screenshots). Let's illustrate with a couple of examples.

### Example 1

The *Loop* app no longer allows you to enter your correction range in the wrong order, i.e., 110 to 90; but it once did and the *Loop* app would stop working. We're using that problem as an example below.

**Bad:** "`It's not working.`" <----makes me wonder what "it" is? What part of "it" isn't working exactly? The app? The glucose control? The pump integration? Alarms? Bolusing? CGM

**Ok:** "`My Loop app won't open.`" <---- Ok, so now I know the *Loop* app itself seems to be the problem, but still don't know if this is a build error or an error that has happened after building. The solutions might be different.

**Better:** "`My Loop app was working yesterday just fine, and now today it's not doing the things like I expect.`" <----- Getting closer. Now, I know this is not a build error and that it sounds like a more recent issue. I'm starting to narrow down the potential causes. This is about as much detail as it takes for me, as a volunteer, to consider helping. I might not have to ask 42 questions, but instead only 4 questions to find the remaining information for troubleshooting. If there were more details, it would save time.

**Awesome:** "`My Loop app was working yesterday. Around lunch time, I went into the settings screen and made some adjustments and ever since it just turns white and closes no matter what I try.`" <---- DEFINITELY getting closer. Now I have a strong suspicion about where the bug is happening and can help with a couple links.

**GOLD MEDAL WORTHY:** "`My Loop app was working yesterday. Around lunch time, I went into the settings screen and made some adjustments to correction ranges. Ever since I did that, the app immediately turns white and shuts down. I have tried restarting my phone, but it has not fixed the problem. I tried searching the docs for 'loop closing' but didn't see results that matched my issue.`" <----- This person is doing an outstanding job of describing the problem. Lots of good details. Has shown initiative to try to use the resources already. This person did an excellent job of helping all of us help them.

### Example 2

This example is not quite as old, but does refer to details from older *Loop* and *iOS* versions. It exemplifies the details needed to assist someone with a build error.

!!! tip "Build with Browser"
    If you are using the Build with Browser method, we still need descriptive details but we do not need screenshots. All that is required is to list your *GitHub* user name. Of course it's really nice if you just paste in your URL - then we don't have to construct the link. The volunteers can then read your publicly available log files. (All private information is automatically redacted in those logs.)

**Bad:** "`My Loop app won't build.`" <----- What step are you on? What is the iOS on your phone? What kind of computer are you using? What macOS? What Xcode version? Have you built successfully before or is this new?

**Ok:** "`I'm trying to update my Loop app and am getting a few errors that I don't understand.`" <----- Wow, sure would be nice to know what those error messages are. Are they red or yellow? A screenshot sure would help here.

**Awesome:** "`I have a macOS Big Sur 11.5.3 computer with Xcode 12.5.1 and my phone is running iOS 14.7.1. Downloaded Loop-master (2.2.6) this morning and I'm getting some red errors about an exit code that I don't understand. I've tried everything in the docs and nothing worked.`" <---- While I'm super happy they "tried everything", I'm no closer to knowing what the exact error message is nor which "stuff" exactly they tried. But all the version numbers are included.

**GOLD MEDAL WORTHY:** "`I have a macOS Big Sur 11.5.3 computer with Xcode 12.5.1 and my phone is running iOS 14.7.1. Downloaded Loop-master (2.2.6) this morning and I'm getting some red errors about an exit code 645 that I don't understand. Here's the screenshot of the error message. I tried searching the docs for "exit code 645" and didn't see any responses that helped.`" <---- This is the kind of detail that will get you to an answer very fast.

## Be OK with Links

Often, the best answer to your question is sending a link to the answer in *LoopDocs* or *LoopTips*.  This provides you a quick, accurate and complete answer. We understand that there is so much information in these sites that it can be hard to find answers.  Mentors know the docs well, are experts at using the search tools and will send direct links to the sections that best answer your question.

If you've searched the docs and read relevant info already, please include that in your post or your reply. That way you don't get linked back to the part you are confused about. And if you have already read the specific section a mentor just linked, be specific about why your problem is not addressed by that link.  Or just say "I'm confused when the doc says this". Letting us know when these docs can be improved is very useful.

- - -
