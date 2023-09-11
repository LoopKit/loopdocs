## Simulator Build

There are 2 main types of simulators users may want to build. Each of these require less up-front acquisition of hardware and may be desirable as a first step towards becoming a Looper.

Please, review all the Intro and Build pages, even if you will not complete them yet.

## Mac-Xcode Build to a Simulated iPhone

This simulator requires access to a Mac or virtual computer, see [Compatible Computer](../build/computer.md)

* Build pages to review, but complete later
    * Compatible iPhone
    * Compatible Pump
    * Compatible CGM
    * Order a RileyLink (not required for Omnipod DASH)
    * Apple Developer Program (can use a free account)
* Follow [Download Xcode](../build/xcode-version.md)
* Follow [Xcode Preferences](../build/xcode-settings.md) but can skip the `Add Apple ID` section
* Follow [Build the Loop App](../build/step14.md) but with the following variation:
    * Skip the section on Developer Mode (that is only when building to a phone)
    * Download the code as directed
    * Choose to Sign Manually in the [Signing Targets](../build/step14.md#signing-targets) section
    * Continue with the [Build Free Loop](../build/build-free-loop.md) page
    * Select a simulator (not your phone) when told to do so
    * Complete the [Build to a Simulator](../build/build-free-loop.md#build-to-a-simulator) section
* Use the simulated iPhone and [set up the app](../loop-3/loop-3-overview.md) as desired

## Build to a Real iPhone

### Common Requirements

This simulator requires a compatible phone, see [Compatible iPhone](../build/phone.md)

* Pages to review, but complete later
    * Compatible Pump
    * Compatible CGM
    * Order a RileyLink (not required for Omnipod DASH)

### What to Expect

Loop will not work in the background without either a real CGM or a real pump to "wake" it up.

The app will only work in the background in these special cases:

* Loop is on on the same phone as a Dexcom CGM and you've added that CGM information to Loop
* Loop is attached to a pump (Pod or Medtronic) dripping water (instead of being attached to your body)

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

### Browser Build (Loop 3)

* Best to configure building using GitHub Actions with a computer or tablet. It does not need to be a Mac.

* Complete the steps in Browser Build tab, starting with [GitHub Build Overview](../gh-actions/gh-overview.md)


### Mac-Xcode Build (Loop 2 or later)

* Need access to a mac or virtual computer, see [Compatible Computer](../build/computer.md)

* You can use a Free Apple Developer account
* Follow [Download Xcode](../build/xcode-version.md)
* Follow [Xcode Preferences](../build/xcode-settings.md)
    * If you have a developer ID, use it in the `Add Apple ID` step and follow the normal build directions
    * If you do not have a developer ID, use the [Free Developer Account](../build/xcode-settings.md#free-developer-account) instructions in the `Add Apple ID` section
* Follow [Build the Loop App](../build/step14.md) using the Free Account instructions
    * If your phone is running iOS 16, you must enable Developer Mode
    * Download the code as directed
    * Choose to Sign Manually in the [Signing Targets](../build/step14.md#signing-targets) section
    * Continue with the [Build Free Loop](../build/build-free-loop.md) page
* Once the App is on your phone
    * Follow the [set up the app](../loop-3/loop-3-overview.md) instructions on your phone but choose a simulated pump
    * If you have a Dexcom CGM, you can select Dexcom Follow or Nightscout for the CGM; otherwise, you can enter glucose values in Apple Health and Loop will pick up the values

