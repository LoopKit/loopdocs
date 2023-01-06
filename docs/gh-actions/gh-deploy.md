## Deploy Using TestFlight

This is only available with Loop 3 and Loop dev branch.

**You must build Loop every 90 days when you use this method.**

After building Loop using [GitHub Build Loop](../gh-actions/gh-first-time.md#build-loop), you are ready to deploy to as many phones as you and your family members need.

* If you later need to add an adult family member to your list, refer to [Set Up Users and Access (TestFlight)](../gh-actions/gh-first-time.md#set-up-users-and-access-testflight).

* Children (under 13 in US, varies by country) cannot use TestFlight with their ID. If you plan to [Install Loop for Child](#install-testflight-loop-for-child), you will need to use your ID on their phone (not the whole phone - just the Media & Purchase portion), so send the TestFlight invitation to the email associated with your ID.


## Install TestFlight

If you already have TestFlight on your phone, skip ahead to [Install Loop with TestFlight](#install-loop-with-testflight).

In order to install Loop, you must install TestFlight on the phone:

* Open the App Store and Search for TestFlight (see GIF below)
* Choose TestFlight and Install or Download to that phone
    * Hint on child's phone, do this while logged in as yourself for Media & Purchase
    * Logging in as an adult is explained in [Install Loop for Child](gh-deploy.md#install-testflight-loop-for-child)

![search for and dowload TestFlight](img/testflight-app-store.gif){width="300"}
{align="center"}


## Install Loop with TestFlight

Once the GitHub Build completes (either green check mark on GitHub or you got an email), you can install Loop on your phone. Refer to the GIF below.

* Open TestFlight and find the name you used for your Loop app in the [Create Loop App in App Store Connect](../gh-actions/gh-first-time.md#create-loop-app-in-app-store-connect) step
* Tap on Install
    * If you already have Loop installed on this phone, you will be warned that the app already exists on your phone and that you might lose the app's data.
    * Click Install again (your pump connection and all your data will be fine)
* Choose Open
* Make sure the Loop app is operating as expected
* If you are building Loop 3.x over Loop 2.x, you will be required to go through [Onboarding](../loop-3/onboarding.md)

![install Loop from TestFlight](img/testflight-install-loop.gif){width="300"}
{align="center"}

## TestFlight Automatic Updates

Go back to the TestFlight app on your phone and tap on your Loop app name in the list to see an expanded screen similar to the graphic below. The row to enable or disable automatic updates is highlighted in the graphic. For this example, this feature is disabled.

* You should choose the option you prefer
* If you leave automatic update enabled (default), then whenever you issue the Actions: Build Loop command on from GitHub on your LoopWorkspace fork, the new build will be installed on that phone as soon as the build completes.
* WARNING: If you later want to build using Xcode, you must first disable automatic update or Xcode will not be able to install to your phone.

![enable or disable automatic update for Loop](img/testflight-auto-update.png){width="300"}
{align="center"}

If you tap on the bottom row that says `Previous Builds`, you can view and choose an older build (as long as it has not expired).

## Install TestFlight Loop for Child

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


