## Simulator Build

There are 2 main types of simulators users may want to build. Each of these require less up-front acquisition of hardware and may be desirable as a first step towards becoming a Looper.

Please, review all the Intro and Build pages, even if you will not complete them yet.

### Simulator using Browser Build:

* No Mac computer required
* Must have a paid Apple Developer ID ($99/year)
* Must have a compatible phone

Follow the normal instructions to build with browser, install the app on a compatible phone and explore the app using the Pump Simulator, CGM Simulator or both.

### Simulator using Build with *Mac*:

* Must have a Mac computer (or virtual machine, Intel chips only)
* Can build the simulator with a free Apple Developer ID
    * [Build to Mac (no phone required)](#build-to-a-simulated-phone-on-mac-computer)<br>
    or
    * [Build to a Compatible Phone using *Mac* Build](#build-to-a-compatible-phone-using-mac-build)

## Build to a Simulated Phone on Mac Computer

This simulator requires access to a Mac or virtual computer, see [Compatible Computer](../build/computer.md){: target="_blank" }

* Build pages to review, but complete later
    * [Apple Developer Program](../build/apple-developer.md){: target="_blank" } (can use a free account)
* Follow [Xcode Version](../build/xcode-version.md){: target="_blank" }
* Follow [Xcode Settings](../build/xcode-settings.md){: target="_blank" } but can skip the `Add Apple ID` section
* Follow [Build the Loop App](../build/build-app.md){: target="_blank" } but with the following variation:
    * Skip the section on Developer Mode (that is only when building to a phone)
    * Download the code as directed
    * Choose to Sign Manually in the [Signing Targets](../build/build-app.md#signing-targets) section
    * Continue with the [Build Free Loop](../build/build-free-loop.md){: target="_blank" } page
        * Select a simulator (not your phone) when told to do so
        * Complete the [Build to a Simulator](../build/build-free-loop.md#build-to-a-simulator) section
* Use the simulated iPhone that will appear on you *Mac* and [set up the app](../loop-3/loop-3-overview.md) as desired
* This gives you a feel for the interface, but the simulator on the *Mac* has limitations

## Build to a Compatible Phone

### Build to a Compatible Phone using Browser Build

You don't need to do anything special when you build the app using the [Build with Browser](../gh-actions/gh-overview.md) instructions. Install the app on your phone from TestFlight. Then select the CGM and/or Pump simulator desired. You must have a paid developer account.

### Build to a Compatible Phone using *Mac* Build

When building to a real phone using a *Mac*, you must have access to a [Compatible Computer](../build/computer.md){: target="_blank" } and a [Compatible Phone](../build/phone.md){: target="_blank" }.

* You can use a Free Apple Developer account
* Follow [Xcode Version](../build/xcode-version.md){: target="_blank" }
* Follow [Xcode Settings](../build/xcode-settings.md){: target="_blank" }
    * If you have a developer ID, use it in the `Add Apple ID` step and follow the normal build directions
    * If you do not have a developer ID, use the [Free Developer Account](../build/xcode-settings.md#free-developer-account) instructions in the `Add Apple ID` section
* Follow [Build the Loop App](../build/build-app.md){: target="_blank" } using the Free Account instructions
    * If your phone is running iOS 16 or newer, you must enable Developer Mode
    * Download the code as directed
    * Choose to Sign Manually in the [Signing Targets](../build/build-app.md#signing-targets) section
    * Continue with the [Build Free Loop](../build/build-free-loop.md){: target="_blank" } page
* Once the App is on your phone
    * Follow the [set up the app](../loop-3/loop-3-overview.md) instructions on your phone but choose a simulated pump
    * If you have a compatible CGM on this phone, you can select that or you can use the simulated CGM or enter glucose values on the main Loop screen

### What to Expect

!!! warning "Locked Phone or App in Background"
    Loop will not work in the background without either a real CGM or a real pump to "wake" it up.
    
    The app will only work in the background in these special cases:

    * Loop is on on the same phone as a CGM and you've added that CGM information to Loop
    * Loop is attached to a pump (Pod or Medtronic)
        * You can configure the pump to drip water (instead of being attached to your body)

    In all other cases, the phone must be open and unlocked for you to test the app.

These CGM and pump options work to provide glucose readings or accept pump commands while the app is open, but will not "wake" the app when in the background or phone is locked:

* Dexcom Share
* Nightscout Remote CGM
* CGM Simulator
* Pump Simulator

!!! warning "Disable Notifications"
    When you have the Loop app on your phone to test as a simulator, you may want to disable notifications when you are not actively using it. Even if you quit the app, you will get Loop not Looping notifications while the app is on your phone.

    To Disable Notifications:

    1. Tap on iOS Settings -> Notifications -> Loop
    1. Disable `Allow Notifications`

    The Loop app, when open, will be quite aggressive at warning you that you have disabled Notifications, so you can reverse those directions to enable notifications when actually using the app.


