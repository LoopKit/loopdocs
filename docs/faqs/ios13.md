# iOS 13 FAQs

Every time a new iOS release comes out...there's loads of questions and a flurry of activity. To help answer these questions, this page will be here short term to help answer these FAQs.

## Should I update to iOS 13?

That is a question that you should answer separate from Loop considerations. New iOS releases often have bugs in them, so I tend to avoid updating my daughter's phone for a bit. Instead, I update my phone and test things out first. Dexcom's app could have problems even...who knows. But, I certainly want to get a chance to kick-the-tires (or watch other people kick tires) for a bit before I try new iOS releases. Once I see things are ok and working without major issues, then I'll update her phone's iOS. Plus, going backwards once you've updated is a pain and usually not possible shortly after the new version is released.

Also, I don't update iOS until I've had time to update my macOS and Xcode as well. Once you update iOS, you'll likely have to do matching updates to other Apple software for Loop building...so might as make sure you successfully update the other pieces so that everything is squared away.

## Will my Loop keep working if I don't update to iOS 13?

Yes. Your Loop app will work for one year after you built it (or until the developer team's enrollment/signing certificate expires, whichever comes first). So, if you don't update iOS...no big deal for your Loop app.

## Will my Loop keep working if I update to iOS 13?

Yes. We have not had one iOS update that has broken Loop apps already installed on the phone. I think we started Loop on iOS 9? Loop has worked through all the updates.

## Do I have to update my Loop if I change to iOS 13?

No. You don't have to. 

## Is there a benefit to updating my Loop if I use iOS 13?

Nope. Unless you want to try dark mode which is in dev branch and being developed there...that's about the only thing that is iOS 13 specific in Loop.

## Why is iOS update a big deal then?

Because iOS major releases (like going from iOS 12 to 13...where the whole number changes) involve updates to several major other Apple-related things. It's a cascade effect.

If you update iOS with a major release, then Xcode will need to update, too. Because Xcode will need the new command tools, Swift language updates, and simulators to be able to properly build for devices that have the new iOS.

And then the cascade continues...that new Xcode will likely require a macOS update. And sometimes (as happened when Xcode 10 was released), the required update to macOS was also a major update (High Sierra to Mojave) that some computers couldn't do. They were "unsupported" by Apple and were aged-out. Luckily, the update to Xcode 11 does not involve aging out any computers this time. If you were running Xcode 10 already, you'll be able to update to Xcode 11 without fear that you'll be left out based on macOS age.

So, iOS updates are a big deal (for Loopers) because they involve needing to do some updates to be able to properly build Loop again the next time you want to. And people forget about updates. And then they forget about LoopDocs' page specifically to help with Updating your Loop app. And so they just blindly download and build like they did last time...unaware there were needed updates.

It's not so much about Loop when you update iOS...the issue is about what other things you need to update BEFORE you build Loop again and AFTER you update iOS.

## What do I need to do to build now with iOS 13?

As of today, September 23rd...things are much easier:

!!!danger "Download Xcode 11 from the App store"
    If you downloaded Xcode 11 GM previously, go to the App store and get the Xcode update waiting for you now. Xcode 11 GM is not what you need anymore...you need to get Xcode 11 from the App store.
    
!!!warning "Restart computer after updating Xcode"
    Make sure to restart your computer after updating Xcode. There's a known issue that happens often enough to be frustrating if you don't reboot. Either a build error about missing simultors or a "device not connected" (even when phone is connected). Just restart computer. It's easy enough.

!!!info "Use the Updating Loop app page in LoopDocs"
    Anytime you want to update your Loop app (aka rebuild your Loop app), always start with the [Updating Loop page](https://loopkit.github.io/loopdocs/build/updating/). That page will have current info to help you get going with what the new minimums are. Always start there. Is it possible there will be a slight delay in updating that page? Yes, I'm human. I have kids, job, house, etc. so it might be slightly delayed sometimes. But, generally during times like this when things are important to update...I make sure the pages reflect that. I'll do my part...your part is to check that page for current info.
    
!!!danger "CHECK BUILD ERRORS PAGE"
    If you get a build error...still check the [Build Errors page](https://loopkit.github.io/loopdocs/build/build_errors/). Because even if your exact error isn't there...the information you NEED to provide when asking for help is listed out on that page. And that information is critical. CRITICAL to be able to troubleshoot your build error.

## What if I don't have Xcode 11? Can I still build?

I cannot understand why you wouldn't update to Xcode 11 at this point..but since you asked the answer depends on which version of iOS **AND** which branch of Loop you are using. If you are using iOS 13, YES...in any branch of Loop you want to build ever, you will need Xcode 11. If you are using dev branch, YES. No matter what iOS you are using with dev branch, you'll need Xcode 11.  Checkout out this chart to find out specifically about your combination of ios/branch and the needed Xcode minimum. (But really...just pull off the band-aid and install Xcode 11 anyways.)

<p align="center">
<img src="../img/xcode11.png" width="650">
</p>
