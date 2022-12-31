## Build Loop using Github Actions

This is only available with Loop 3 and Loop dev branch.

### First Time Build Instructions

You can build Loop-dev using your github account and your (paid) Apple Developer account using a browser. You no longer require a Mac computer.

The instructions in the link below are basic - please read carefully and use the links provided in these directions.

* [Using Github Actions + FastLane to deploy to TestFlight](https://github.com/LoopKit/LoopWorkspace/blob/dev/fastlane/testflight.md)

**You must build Loop every 90 days when you use this method.**

After successfully building Loop using Actions in github, here are two important things to know. The next statements might not make sense to you if you have not gone to the link above and reviewed the instructions.

1. Once you have installed TestFlight on your phone and you see your app in the TestFlight screen, tap on it to see an expanded screen with an option to automatically update or not.  You should choose which you prefer. If you do not turn it off, the app will automatically update whenever a new Build action completes in your github fork.

1. The Apple ID used to sign in for TestFlight on a given phone does not have to match the Apple ID of the phone user. This is important for children. [Loopers Need Their Own Apple ID](../build/step6.md#loopers-need-their-own-apple-id), but children cannot use TestFlight with their ID. If you plan to [Install Loop for Child](#install-loop-for-child), you will need to use your ID on their phone (not the whole phone - just the Media & Purchase portion), so send the TestFlight invitation to the email associated with your ID.

