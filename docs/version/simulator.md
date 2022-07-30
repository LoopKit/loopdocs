# Simulator Build

## Options

There are 2 main types of simulators users may want to build. Each of these require less up-front acquisition of hardware and may be desirable as a first step towards becoming a Looper.

Please, review all the Build Steps, even if you will be skipping some.

### Build to a Simulated iPhone on a Computer

* Need access to a mac or virtual computer, see [Build Step 1](../build/step1.md)
* Build Steps you can skip
    * Step 2: Compatible iPhone/iPod
    * Step 3: Compatible Pump
    * Step 4: Compatible CGM
    * Step 5: Order a RileyLink
    * Step 6: Enroll in Apple Developer Program
* Follow [Build Step 8](../build/step8.md)
* Follow [Build Step 9](../build/step9.md) but can skip the `Add Apple ID` section
* Follow [Build Step 14](../build/step14.md) but with the following variations:
    * When told to select ["Your Phone" in this section](../build/step14.md#select-loop-workspace-and-your-phone), instead choose a simulator
    * Follow the instructions in the [Build to a Simulator](../build/step14.md#build-to-a-simulator)
* Use the simulated iPhone and [set up the app](../operation/overview.md) as desired

### Build to a Real iPhone and use a Simulated Pump and CGM

* Need access to a mac or virtual computer, see [Build Step 1](../build/step1.md)
* Need access to an iPhone or iPod, see [Build Step 2](../build/step2.md)
* Steps you can skip
    * Step 3: Compatible Pump
    * Step 4: Compatible CGM
    * Step 5: Order a RileyLink
    * Step 6: Enroll in Apple Developer Program
* Follow [Build Step 8](../build/step8.md)
* Follow [Build Step 9](../build/step9.md)
    * Use the instructions for a [Free Developer Account](../build/step9.md#free-developer-account)
* Follow [Build Step 14](../build/step14.md) using the Free Account instructions
* Once the App is on your phone
    * Follow the [set up the app](../operation/overview.md) instructions but choose a simulated pump
    * If you have a Dexcom CGM, you can select Dexcom Follow for the CGM; otherwise, you can enter glucose values in Apple Health and Loop will pick up the values

