# Step 8: Download Xcode

!!!danger "Time Estimate"
    * 45 minutes to 2 hours, depending on internet connection...but you don't need to babysit the download.

!!!info "Summary"
    * After making sure your macOS is up-to-date for your iPhone's iOS (see the info below), download Xcode from your computer's App Store application.

!!!warning "FAQs"
    * **"Why isn't my Xcode installing?"** I can't see your computer to know exactly why...but the two most common reasons are (1) lack of internet connection or (2) not enough free space on the computer's hard drive. Xcode is a pretty beefy-sized download...and needs even a little more space to properly unpack and install itself. Best to try to have about 20-25GB of free space on your hard drive before starting to be on the safe side. If you get low on free space, I've seen installation failures. You can check your free space by clicking on the `About this Mac` (like in Step 1) and clicking the `Storage` tab.

Today is an easy one, but probably takes the longest of most of any of the steps in terms of time...only because the download takes a while. The good news is that you don't have to watch this. Instead, you can start the download and simply walk away for the rest of it.

Xcode is a free application for Apple computers. Xcode will turn the Loop "raw" code into an iOS application and install it onto your iPhone/iPod. **Make sure you have updated your macOS AND checked the `Software Updates` button before proceeding...in other words, make sure you did Step 1's work.**

Open your App Store in your computer and search for Xcode...you'll either be downloading it brand new or updating an existing installation. The minimum version you need will depend on the iOS your iPhone is running. The version number should be showing in the "what's new" description as shown in the image below. This is a big download, so don't expected this to be fast.

<p align="center">
<img src="../img/xcode.png" width="750">
</p></br>

!!!warning "Two important facts"
    
    1. The minimum version of Xcode that you need is dependent on the version of iOS you have on the iPhone. The newer the version of iOS, the newer of Xcode you'll also need. </br></br>The most current version of iOS (14+) requires Xcode 12 and macOS 10.15.4 at a minimum</br></br> 
    2. The newest Xcode version **may also require you to update your macOS version**. If you have an old version of macOS, then the App Store will not show you that a newer version of Xcode is available. This can create confusion because your iOS could be requiring a newer Xcode, but the App Store won't show it as available. 
    
## How do all the minimum versions relate to each other?

Most often what happens is that people will update their iOS on the iPhones more often than they update their macOS or Xcode.  You know how it goes...you're tapping on your phone one day and it says there's a new version of iOS available for your phone. Want to update it now? Or be reminded of it later? Or maybe you even have the setting on your phone set to automatically install iOS updates.

Because the update looks so innocuous and we all lead busy lives, we forget that there might be consequences to iOS updates.


!!!danger "Loop and iOS updates"
    For Loopers...the consequence to an iOS update is nothing immediate. Your Loop app won't die, it will keep humming along. </br></br>BUT, before you ***<u>update or rebuild</u>*** your Loop app on that phone, you will likely need to update your macOS and Xcode applications because of the newer iOS.  And you will need to do the updates/checks in a certain order:</br></br>
    1st: Check if your macOS has updates</br></br>
    2nd: Check for an Xcode update.</br></br>

The chart below is a helpful visual of the minimum versions you'll need based on your iOS. 

* macOS: If you are running an iPhone with iOS 14, you need to make sure your macOS is 10.15.4 at a minimum as the first step. If you don't have the minimum version, go to [Step 1 Compatible Computer](https://loopkit.github.io/loopdocs/build/step1/#check-your-macos) and follow directions for updating your macOS. 

* Xcode: Now that your macOS is updated to 10.15.4 minimum, the App Store in your computer will have Xcode 12.0.1 (or newer) available for you to download/update. 

If you have a brainfart and leave your macOS back at 10.15.2...the App Store won't even tell you Xcode version 12 or newer exists. That's why it is important to do the macOS updates FIRST. I can't tell you how many people post for help saying "I'm trying to update my Loop app but am getting errors." If I ask what Xcode version they have and if they've updated, the response is "I don't have any Xcode updates available in the App Store...so I must be running the most current version." When actually what's happened is they have forgotten to check for macOS updates FIRST and therefore cannot see the needed Xcode update yet.

(Source for the chart is [wikipedia](https://en.wikipedia.org/wiki/Xcode))

<p align="center">
<img src="../img/minimum-related.png" width="750">
</p></br>

## What happens if you try using too old of Xcode?

It isn't some catastrophic failure if you try to build with an outdated Xcode without realizing it. You'll see a pretty obvious error message during your Loop build that says "Could not locate device support files." That messages is telling you that your iOS on the phone requires you to get a newer version of Xcode to be able to build Loop onto that phone.

<p align="center">
<img src="../img/device-support-files.jpg" width="750">
</p></br>
    
So, if you see that error message realize you may have to update your macOS to be able to see the newest Xcode version that you will need. Make sure to check that chart to see what your minimum versions are for the iOS you are running on your iPhone.
    
## Next Step: Xcode Preferences

Now you are ready to move onto Step 9 to [work on Xcode Preferences](https://loopkit.github.io/loopdocs/build/step9/).

