## Simulator Build

There are 2 main types of simulators users may want to build. Each of these require less up-front acquisition of hardware and may be desirable as a first step towards becoming a Looper.

Please, review all the Build pages, even if you will be skipping some.

## Build to a Simulated iPhone on a Computer

* Need access to a mac or virtual computer, see [Compatible Computer](../build/step1.md)
* Build pages you can skip
    * Compatible iPhone/iPod
    * Compatible Pump
    * Compatible CGM
    * Order a RileyLink
    * Apple Developer Program
* Follow [Download Xcode](../build/step8.md)
* Follow [Xcode Preferences](../build/step9.md) but can skip the `Add Apple ID` section
* Follow [Build the Loop App](../build/step14-post-loop-3.md) but with the following variation:
    * Skip the section on Developer Mode (that is only when building to a phone)
    * Download the code as directed
    * Choose to Sign Manually in the [Signing Targets](../build/step14-post-loop-3.md#signing-targets) section
    * Continue with the [Build Free Loop](../build/build-free-loop.md) page
    * Select a simulator (not your phone) when told to do so
    * Complete the [Build to a Simulator](../build/build-free-loop.md#build-to-a-simulator) section
* Use the simulated iPhone and [set up the app](../loop-3/loop-3-overview.md) as desired

## Build to a Real iPhone and use a Simulated Pump and CGM

### Loop Dev ONLY

Loop dev (which will be the next released version of Loop) can be built with the same prerequisites as [Released Loop](#released-loop).

Loop dev can also be built without using a Mac computer using Github Actions. If you choose this method to build and evaluate the app, it has slightly different prerequisites.

* Need access to an iPhone or iPod, see [Compatible iPhone/iPod](../build/step2.md)
* Paid Apple Developer Account ($99/year), see [Enroll in Apple Developer Program](../build/step6.md)
* Follow these instructions instead of the Build Directions in LoopDocs
    * [Build Loop dev using Github Actions](../gh-actions/gh-overview.md)

### Released Loop

* Need access to a mac or virtual computer, see [Compatible Computer](../build/step1.md)
* Need access to an iPhone or iPod, see [Compatible iPhone/iPod](../build/step2.md)
* Pages you can skip
    * Compatible Pump
    * Compatible CGM
    * Order a RileyLink
    * Apple Developer Program
* Follow [Download Xcode](../build/step8.md)
* Follow [Xcode Preferences](../build/step9.md)
    * If you have a developer ID, use it in the `Add Apple ID` step and follow the normal build directions
    * If you do not have a developer ID, use the [Free Developer Account](../build/step9.md#free-developer-account) instructions in the `Add Apple ID` section
* Follow [Build the Loop App](../build/step14-post-loop-3.md) using the Free Account instructions
    * If your phone is running iOS 16, you must enable Developer Mode
    * Download the code as directed
    * Choose to Sign Manually in the [Signing Targets](../build/step14-post-loop-3.md#signing-targets) section
    * Continue with the [Build Free Loop](../build/build-free-loop.md) page
* Once the App is on your phone
    * Follow the [set up the app](../loop-3/loop-3-overview.md) instructions on your phone but choose a simulated pump
    * If you have a Dexcom CGM, you can select Dexcom Follow or Nightscout for the CGM; otherwise, you can enter glucose values in Apple Health and Loop will pick up the values

