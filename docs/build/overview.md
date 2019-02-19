# Overview of Build Process

The overall installation process is pretty simple.  Loop's code is stored online and available for free download. In order to compile all that code into a useable app, you need to use a free Apple program called Xcode.  However, Apple is particular about apps and who can install custom apps on their devices, so you will have to enroll in Apple's Developer Program.  Once you enroll as a developer, you will be able to "sign" the Loop app in Xcode so that it will properly install onto your iPhone.

While all of this is probably quite intimidating at first, I promise that it is quite doable by the average apple computer user.

If you are worried about how long this will take and want to break this up into chunks, the following might be some helpful stopping points to consider and generally follow the instructional pages to make things easier:

* Day 1 (15 minutes): Order a RileyLink from [GetRileyLink.org](https://getrileylink.org)</br></br>
* Day 2 (30 minutes or less): [Update macOS on your computer and install Homebrew on your computer](https://loopkit.github.io/loopdocs/build/build-computer/).</br></br>
* Day 3 (20 minutes): [Setup an Apple Developer account](https://loopkit.github.io/loopdocs/build/build-developer/) (wait for enrollment confirmation email)</br></br>
* Day 4 (1-2 hours): [Download and setup Xcode](https://loopkit.github.io/loopdocs/build/build-xcode/) (basically this step is one that you can walk away from since the download just chugs along while you go do other things) </br></br>
* Day 5 (50 minutes): [Build Loop app using Xcode](https://loopkit.github.io/loopdocs/build/build-loop/)</br></br>

!!! info "Time Saving Tips"
    * Check your watchOS, iPhone OS, macOS, Xcode first to see if they need updates.  If you have iOS 12 (or newer), you will need at a minimum watchOS 4.1, macOS 10.13.6, and Xcode 10.1.  If you have newer versions than the minimum, that is fine.</br></br>
    * Apple watches need to be paired with the iPhone BEFORE the Loop app is built onto the phone in order to have the Loop on the watch, too.  If you pair a new Apple watch later, you'll have to rebuild the Loop app onto the iPhone again, before the watch will work with Loop functions.</br></br>
