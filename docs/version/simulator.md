# Simulator Build

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
* Follow [Build the Loop App](../build/step14.md) but with the following variations:
    * When told to select ["Your Phone" in this section](../build/step14.md#select-loop-workspace-and-your-phone), instead choose a simulator
    * Follow the instructions in the [Build to a Simulator](../build/step14.md#build-to-a-simulator)
* Use the simulated iPhone on the computer and [set up the app](../operation/overview.md) as desired

## Build to a Real iPhone and use a Simulated Pump and CGM

### Loop Dev ONLY

Loop dev (which will be the next released version of Loop) can be built with the same prerequisites as [Released Loop](#released-loop).

Loop dev can also be built without using a Mac computer using Github Actions. If you choose this method to build and evaluate the app, it has slightly different prerequisites.

* Need access to an iPhone or iPod, see [Compatible iPhone/iPod](../build/step2.md)
* Paid Apple Developer Account ($99/year), see [Enroll in Apple Developer Program](../build/step6.md)
* Follow these instructions instead of the Build Directions in LoopDocs
    * [Build Loop dev using Github Actions](../build/build-select-dev.md#build-loop-dev-using-github-actions)

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
* When Building, use the [Build Loop App](../build/step14.md) page and select your phone`
    * If you do not have a developer ID, be sure to follow the [Free Account](../build/step14.md#free-account) instructions
* Once the App is on your phone
    * Follow the [set up the app](../operation/overview.md) instructions but choose a simulated pump
    * If you have a Dexcom CGM, you can select Dexcom Follow for the CGM; otherwise, you can enter glucose values in Apple Health and Loop will pick up the values

