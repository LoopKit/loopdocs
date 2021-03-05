# Step 1: Compatible Computer

!!!danger "Time Estimate"
    * 5 minutes, if already have Mojave or Catalina macOS
    * 30-60 minutes, if need to install macOS updates

!!!info "Summary"
    * Check your macOS and make sure it is Mojave or Catalina. **If you have the latest iOS version on the iPhone that will be using Loop...then you need Catalina.**
    * Do not use any of the beta macOS versions. (If you don't know what that means, don't worry...that means you aren't using one.)
    * If your macOS is not Mojave or Catalina, check to see if you can up update your macOS to one of those.
    * If you cannot upgrade your existing computer to Mojave or Catalina, you'll need to check into a borrowed computer, patcher tool, or perhaps a new/used computer compatible with Mojave or Catalina.
    * Check the `Software Update` to see if your computer has any updates available since you first installed it.

!!!warning "FAQs"
    * **"Can I use a PC or Windows computer? I don't own an Apple computer."** Yes...sort of. Please see [this FAQ about using Virtual Machine](https://loopkit.github.io/loopdocs/faqs/FAQs/#can-i-use-a-pc-or-windows-computer-to-build). Windows computers with AMD processors will not be able to successfully build using Virtual Machine, so please make sure you check your processor type before embarking down the Virtual Machine path.
    * **"What can I do if my computer is too old to be upgraded to Catalina?"** You could take a look at using [Catalina Patcher](http://dosdude1.com/catalina/), but this is totally on your own and not part of these instructions. Just offering the answer to the FAQ...it is up to you to read about the patcher tool and what risks it may involve for you.
    * **"Can I borrow someone else's Apple computer?"** Yes, please see [this FAQ about borrowing a computer](https://loopkit.github.io/loopdocs/faqs/FAQs/#do-i-need-to-own-my-own-apple-computer) to learn more.
    * **"How often do I need to use the computer?"** Computer access is only required when you are initially installing the Loop app or updating to a newer Loop release. You do NOT need access to an Apple computer in order to troubleshoot or change Loop settings, such as basal profiles or carb ratios.

## New M1 chip Apple Computers

Yes, the newest Apple computers just released in November 2020 are compatible with Loop building. There is ONE little step to be aware of with the new computers, and that is on the Step 7 Install Homebrew page. I've highlighted in a colored boxes on that page the parts that M1 users will need to do. I promise, it's quick and painless.

And...with that...I'm extremely jealous that you have the new computer. They will make Loop building extremely fast and the time estimates on these docs will be ridiculously slower than you will be experiencing. Lucky duck, I have FOMO.

## Big Sur MacOS

Yes, Big Sur is compatible with Loop building...I'm working on updating this page for that soon. Hang tight.

## Catalina vs Mojave, which do you need?

Do you need Catalina or Mojave? The answer will depend on the iOS of your iPhone you'll install Loop onto.

**If you have iOS 12.4 to 13.2**, you can use macOS 10.14.4 (Mojave) or 10.15.2 or newer (Catalina). 

**If you have iOS 13.4 or newer**, you will not be able to use Mojave and will need Catalina at a minimum. In other words, you'll need macOS 10.15.2 at a minimum to build Loop onto an iPhone running iOS 13.4 or newer.

!!!danger "iOS dictates your computer needs"
    Put simply for Loopers...the more up-to-date you keep your iOS, the more up-to-date your computer and macOS will need to be, too. That's not necessarily a bad thing, and you can't avoid iOS updates forever...you just do need to be aware of how they relate to each other if your computer is "getting on the older side".

## Check your macOS
You need an Apple computer that has at least the minimum macOS version as described above; Mojave macOS 10.14.4 (or newer) or Catalina macOS 10.15 (or newer). To find out which version you have installed, click on the little Apple icon in your computer's upper left corner and select the `About this Mac`. It doesn't matter if the computer is a MacBook, iMac, macMini, etc...just so long as it has the minimum you'll need. 

If your computer does not have the required minimum version, you'll need to check the `Software Update` button on that screen to see if you can update.

<p align="center">
<img src="https://loopkit.github.io/loopdocs/build/img/macosx.png" width="500">
</p>

If your computer does not give you the option to update to the newer macOS (in other words you are stuck on older versions)...it is quite possible that Apple has decided your computer is too old to run the latest and greatest. How old is too old? That will depend on your computer model and year as shown below:

<p align="center">
<img src="https://loopkit.github.io/loopdocs/build/img/mojave-minimum.png" width="750">
</p>


## Next Step: Compatible iPhone/iPod touch

Now you are ready to move onto Step 2 to check if you have a [Compatible iPhone/iPod touch](https://loopkit.github.io/loopdocs/build/step2/).
