# Updating Loop

!!!danger "Time Estimate" _ 25 minutes, if already have updates done _ 40-90
minutes, if need to install Apple update(s)

!!!info "Summary" 1. Update macOS, Xcode, iOS, and/or watchOS 2. Download
updated Loop code 3. Open in Xcode, sign targets 4. Add optional code
customizations 5. Build onto your iPhone 6. Resolve Build Errors

!!!warning "FAQs" _ **"What is an update?"** Anytime you want to change branches
(i.e., go from omnipod-testing to dev branch), change customizations, or grab
updates to the same branch you built with before...that is an "update" of your
Loop app. _ **"Do I delete my old Loop app first?"** Definitely not! If you keep
your Loop app on your phone, your Loop settings (and existing pod) will continue
to work the same after the update. Seamless. _ **"What if I'm using a
new/different developer account?"** If you aren't building with the same
developer account as your existing app was built with (this includes going from
free to paid), then you will be installing a brand new (second) Loop app on your
phone. Your existing pod won't work with the new app, so you might want to time
this transition when you are due to change pods. Delete the old app once you get
the new one all set up. _ **"What if it is a new computer but the same developer
account?"** No big deal...you just want to make sure the computer has Homebrew
installed already and you've added your developer account to Xcode
preferences. \* **"Where can I find the list of features in a new release?"**
When a new version of Loop is released, you can click
[HERE](https://github.com/LoopKit/Loop/releases) to read what features or fixes
were a part of the new release.

## When to Update

You will have to rebuild your Loop app at a minimum once every 12 months. The
apps built and signed by you in Xcode with a paid developer account will only
last for 12 months before they expire and need rebuilding. So, at least once per
year you will have to rebuild your app and go through this update process.

Under ordinary circumstances, you do not _have to_ update your Loop app until
you are ready to grab new features. However, we encourage regular updates when a
new version is released because they often contain bug fixes or improvements
which may increase operational stability.

## Step 1: Update macOS and Xcode

!!!danger "Minimum Requirements" Between Loop app builds, there's a high
likelihood that Apple has updated one or more of the systems involved in your
Loop app. <u>If you miss macOS or Xcode updates, you may run into build
problems. Do not skip these steps before updating Loop.</u> You will need the
following minimum versions:</br></br>

_ macOS 10.14.3 (Mojave)</br></br> _ iOS 12.2</br></br> \* Xcode 11</br></br>

But why be a minimalist? Go ahead and install any available updates in all
areas; macOS, Xcode, iOS, and watchOS.

(You can only use macOS 10.13.6 High Sierra if you are building with Loop master
branch <u>and</u> have at least iOS 12 or 12.1. The next version of Loop master
branch will require Mojave at a minimum, so keep that in your planning for the
future. If building dev, omnipod-testing, or any other branch that supports
omnipod users, then you will need the minimum versions listed above.)

!!!info "Download Xcode 11 from the App store" Yes, this is important. If you
downloaded Xcode 11 GM previously in the last couple weeks, go to the App store
and get the Xcode update waiting for you now. Xcode 11 GM is not what you need
anymore...you need to get Xcode 11 from the App store.

!!!warning "Restart computer after updating Xcode" Make sure to restart your
computer after updating Xcode. There's a known issue that happens often enough
to be frustrating if you don't reboot. Either a build error about missing
simultors or a "device not connected" (even when phone is connected). Just
restart computer. It's easy enough.

!!!danger "Check Homebrew and Carthage" Depending on when you last built, you
may need to update Homebrew and Carthage. Please open Terminal app and copy &
paste `carthage version` into Terminal. If you see 0.33.0 returned, then you
don't need to do anything additional.

If you got a number other than 0.33.0 for your carthage version, then copy &
paste `brew update && brew upgrade carthage` into Terminal app. When the update
finishes, you should have carthage 0.33.0 (or later) installed.</br>

If you don't have 0.33.0 installed after that update, then you will need to use
`brew link --overwrite carthage` and then repeat the
`brew update && brew upgrade carthage` command. That should succeed in updating
you properly.

## Step 2: Download Updated Loop Code

After you've finished the updates to your devices listed above, you can move
onto downloading updated Loop code. You will not be simply using your old
downloaded Loop code (and in fact, you can delete those old folders now if you
want). Click on **ONE** of the links below to download an updated version of the
Loop code: </br></br>

<p align="center">
[Loop: Master branch](https://github.com/LoopKit/Loop/archive/master.zip)
</p></br>
<p align="center">
**OR**</br></br>
[Loop: Dev branch](https://github.com/LoopKit/Loop/archive/dev.zip)
</p></br>
<p align="center">
**OR**</br></br>
[Loop: Omnipod-testing branch](https://github.com/LoopKit/Loop/archive/omnipod-testing.zip)
</p></br>

!!!info "Reminder" It is best practice is to leave your Loop code in your
Downloads folder. If you store your Loop code a different folder than Downloads
(such as your Documents folder or Desktop), make sure the specified folder is
**not** an iCloud drive. Storing your Loop code in an iCloud drive folder will
prevent Loop from building successfully. How do you know if a folder is an
iCloud drive? Check your System Preferences. If your System Preferences for
iCloud is set as shown below, your Documents and Desktop folders are iCloud
drives and **NOT** appropriate places to save your Loop download.

<p align="center">
<img src="../img/icloud-drive.png" width="550">
</p></br>
Depending on your browser and settings, your Loop download may or may not automatically unzip. If it does not unzip automatically, you can right-click on the zip file and choose to "Open With" Archive Utility. This will create a blue folder called `Loop-master`. HOWEVER, if you already have an existing `Loop-master` folder from a previous download, the name of the next download will be something like `Loop-master (1)`. The problem with that folder name is that it contains a space...and spaces in the name will cause your Loop build to fail. So, either delete old copies of Loop before downloading/unzipping or rename the folder(s) to ensure that NO SPACES are in the folder name.
<p align="center">
<img src="../img/folder-name.png" width="550">
</p>

## Step 3: Build Like Normal

From here it is just like the old directions...you can go straight to
[Step 14 Build Loop app](https://loopkit.github.io/loopdocs/build/step14/) and
do just like you did the first time. Open the project, plug in the phone, sign
four targets, code customizations (if wanted), and then build button. Easy
peasy.

Note: If this is a computer that hasn't built Loop before, you would want to
make sure to do
[Step 7: install Homebrew](https://loopkit.github.io/loopdocs/build/step7/)
before doing your build on that computer.

## Step 4: Check Build Errors page if needed

!!!danger "CHECK BUILD ERRORS PAGE" If you get a build error...still check the
[Build Errors page](https://loopkit.github.io/loopdocs/build/build_errors/).
Because even if your exact error isn't there...the information you NEED to
provide when asking for help is listed out on that page. And that information is
critical. CRITICAL to be able to troubleshoot your build error.
