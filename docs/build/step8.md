# Step 8: Download Xcode

!!!danger "Time Estimate"
    * 45 minutes to 2 hours, depending on internet connection...but you don't need to babysit the download.

!!!info "Summary"
    * After making sure your macOS is up-to-date for your iPhone's iOS (see the info below), download Xcode from your computer's App Store application.

!!!warning "FAQs"
    * **"Why isn't my Xcode installing?"** I can't see your computer to know exactly why...but the two most common reasons are (1) lack of internet connection or (2) not enough free space on the computer's hard drive. Xcode is a pretty beefy-sized download...and needs even a little more space to properly unpack and install itself. Best to try to have about 20-25GB of free space on your hard drive before starting to be on the safe side. If you get low on free space, I've seen installation failures. You can check your free space by clicking on the `About this Mac` (like in Step 1) and clicking the `Storage` tab.

Today is an easy one, but probably takes the longest of most of any of the days in terms of time...only because the download takes a while. The good news is that you don't have to watch this. Instead, you can start the download and simply walk away for the rest of it.

Xcode is a free application for Apple computers. Xcode will turn the Loop "raw" code into an iOS application and install it onto your iPhone/iPod. **Make sure you have updated your macOS AND checked the `Software Updates` button before proceeding...in other words, make sure you did Step 1's work.**

Open your App Store in your computer and search for Xcode...you'll either be downloading it brand new or updating an existing installation. The minimum version you need will depend on the iOS your iPhone is running. The version number should be showing in the "what's new" description as shown in the image below. This is a big download, so don't expected this to be fast.

<p align="center">
<img src="../img/xcode.png" width="750">
</p></br>

!!!danger"Two important facts"
    1. The minimum version of Xcode that you need is dependent on the version of iOS you have on the iPhone. The newer the version of iOS, the newer of Xcode you'll also need. 
    2. The newest Xcode version **may also require you to update your macOS version**. If you have an old version of macOS, then the App Store will not show you that a newer version of Xcode is available. This can create confusion because your iOS could be requiring a newer Xcode, but the App Store won't show it as available. 
    
## How do all the minimum versions relate to each other?

Most often what happens is that people will update their iOS on the iPhones more often than they update their macOS or Xcode.  So it is quite common that people will not realize they've updated their iOS to a point that triggered additional required updates to other parts of this whole process.  Use the chart below to double check your minimum versions based on your iOS. For example, if you are running iOS 13.4.x, you will need macOS 10.15 (also called Catalina) and Xcode 11.4.x.  If you are running an iPhone with iOS 13.4.x, but you still have macOS 10.14.4 (also called Mojave), you will not be told there's an Xcode 11.4.x available in the App Store as noted in the important facts box above. You'd need to update your macOS to Catalina (macOS 10.15.2 minimum) FIRST and then the App Store will have Xcode 11.4.1 (or newer) available.  Please make sure you are checking the minimum Xcode and macOS versions when you update your iOS between Loop builds. (Don't worry about beta versions...they aren't in the App Store and we don't want to use them anyways.)

(Source for the figure below is [wikipedia](https://en.wikipedia.org/wiki/Xcode#11.x_series))

<p align="center">
<img src="../img/minimum-related.png" width="750">
</p></br>

## What happens if you try using too old of Xcode?

It isn't some catastrophic failure if you try to build with an outdated Xcode without realizing it. You'll see a pretty obvious error message during your Loop build that says "Could not locate device support files." That messages is telling you that your iOS on the phone requires you to get a newer version of Xcode to be able to build Loop onto that phone.

<p align="center">
<img src="../img/device-support-files.jpg" width="750">
</p></br>
    
So, if you see that error message realize you may have to update your macOS to be able to see the newest Xcode version. 
    
## Next Step: Xcode Preferences

Now you are ready to move onto Step 9 to [work on Xcode Preferences](https://loopkit.github.io/loopdocs/build/step9/).

