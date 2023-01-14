## Simulator Build

There are 2 main types of simulators users may want to build. Each of these require less up-front acquisition of hardware and may be desirable as a first step towards becoming a Looper.

Please, review all the Intro and Build pages, even if you will not complete them yet.

## Mac Build to a Simulated iPhone

This simulator requires access to a Mac or virtual computer, see [Compatible Computer](../build/step1.md)

* Build pages to review, but complete later
    * Compatible iPhone/iPod
    * Compatible Pump
    * Compatible CGM
    * Order a RileyLink (not required for Omnipod DASH)
    * Apple Developer Program (can use a free account)
* Follow [Download Xcode](../build/step8.md)
* Follow [Xcode Preferences](../build/step9.md) but can skip the `Add Apple ID` section
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

This simulator requires a compatible phone, see [Compatible iPhone/iPod](../build/step2.md)

* Pages to review, but complete later
    * Compatible Pump
    * Compatible CGM
    * Order a RileyLink (not required for Omnipod DASH)

### Browser Build (Loop 3)

* Best to configure building using GitHub Actions with a computer or tablet. It does not need to be a Mac.

* Complete the steps in Browser Build tab, starting with [GitHub Build Overview](../gh-actions/gh-overview.md)


### Mac Build (Loop 2 or later)

* Need access to a mac or virtual computer, see [Compatible Computer](../build/step1.md)

* You can use a Free Apple Developer account
* Follow [Download Xcode](../build/step8.md)
* Follow [Xcode Preferences](../build/step9.md)
    * If you have a developer ID, use it in the `Add Apple ID` step and follow the normal build directions
    * If you do not have a developer ID, use the [Free Developer Account](../build/step9.md#free-developer-account) instructions in the `Add Apple ID` section
* Follow [Build the Loop App](../build/step14.md) using the Free Account instructions
    * If your phone is running iOS 16, you must enable Developer Mode
    * Download the code as directed
    * Choose to Sign Manually in the [Signing Targets](../build/step14.md#signing-targets) section
    * Continue with the [Build Free Loop](../build/build-free-loop.md) page
* Once the App is on your phone
    * Follow the [set up the app](../loop-3/loop-3-overview.md) instructions on your phone but choose a simulated pump
    * If you have a Dexcom CGM, you can select Dexcom Follow or Nightscout for the CGM; otherwise, you can enter glucose values in Apple Health and Loop will pick up the values

