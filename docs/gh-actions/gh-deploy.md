## Deploy Using TestFlight

This is only available with Loop 3 and Loop dev branch.

**You must build Loop every 90 days when you use this method.**

After successfully building Loop using [GitHub Build Loop](../gh-actions/gh-first-time.md#build-loop), you are ready to deploy to as many phones as you and your family members need.

If you later need to add an adult family member to your list, refer to [Set Up Users and Access (TestFlight)](../gh-actions/gh-first-time.md#set-up-users-and-access-testflight)

## Install TestFlight

For any phone on which you want to deploy Loop from GitHub Build Actions, you must install TestFlight on that phone (one time only).

1. On the phone, for which you want to install Loop:
    * Install TestFlight
        * Hint on child's phone, do this while logged in for Media & Purchase as yourself
        * This is explained in [Install Loop for Child](gh-deploy.md#install-testflight-loop-for-child)
1. Open the TestFlight app
    * Once the build completes, the name you used when configuring your app will appear in the TestFlight apps to install
    * Choose Install
        * If you already have Loop installed on this phone, you will be warned that the app already exists on your phone and that you might lose the app's data.
        * Click Install (your pump connection and all your data will be fine)
    * Choose Open
    * Make sure the Loop app is operating as expected
    * If you are building Loop 3.x over Loop 2.x, you will be required to go through [Onboarding](../loop-3/onboarding.md)
1. Go back to the TestFlight app on your phone and tap on your Loop app name in the list to see an expanded screen with an option to automatically update or not.  You should choose which you prefer.
    * If you leave automatic update enabled (default), then whenever you issue Build Action command on from your LoopWorkspace fork, the version of the app on the phone will be installed as soon as each Build Action completes.
    * WARNING: If you later want to build using Xcode, you must first disable automatic update or Xcode will not be able to install to your phone.

1. The Apple ID used to sign in for TestFlight on a given phone does not have to match the Apple ID of the phone user. This is important for children. [Loopers Need Their Own Apple ID](../build/step6.md#loopers-need-their-own-apple-id), but children cannot use TestFlight with their ID. If you plan to [Install Loop for Child](#install-testflight-loop-for-child), you will need to use your ID on their phone (not the whole phone - just the Media & Purchase portion), so send the TestFlight invitation to the email associated with your ID.


### Install TestFlight Loop for Child

The adult (Apple Developer Account owner) can log into Media & Purchase (see steps below) without affecting the child Apple ID associated with a phone (and thus their health records used by Loop). After the adult installs or updates Loop using TestFlight, they probably should reverse those steps to remove their credentials from Media & Purchase.

Media & Purchase affects access to the App Store, Books, Music and Podcasts.

On the Looper's phone:

* Tap on Settings
* At the very top of Settings, tap on the Name of the phone, for example, `my kids phone`
* Apple ID Screen appears
    * Tap on Media & Purchases
    * Tap on Sign Out, and confirm
    * Reboot the phone
* After phone reboots, repeat the process and sign in with the adult (Apple Developer Account owner) Apple ID and password
* Install or Update Loop from TestFlight on child's phone
* Repeat the process to sign out the adult and (if needed) sign back in the child


