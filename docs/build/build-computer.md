# Set up your Apple Computer

Any Apple computer will work so long as it is running a compatible macOS version and you have administrative rights to be able to install new programs on the computer.

## Verify macOS

You need to be running macOS 10.13.6 (High Sierra) or 10.14 (Mojave), so verify by clicking the apple logo in your computer display's upper left corner and selecting `About this Mac`.

<p align="center">
<img src="../img/macOS.png" width="450">
</p>

If your macOS is not the minimum version, click on the `Software Update` button and update.  If your computer is older than late 2009/2010 (depending on computer model), you may not be able to update macOS sufficiently to use the most recent Xcode.  You can check the latest macOS compatibility [here](https://www.apple.com/macos/how-to-upgrade/#hardware-requirements).

## Install Homebrew

Homebrew is a program that will allow us to install the needed packages to build Loop.  Open the Terminal application on your computer.  It is located in the Applications folder, and then look in the Utilities subfolder for the Terminal application.

<p align="center">
<img src="../img/terminal.png" width="550">
</p>

Terminal app is very plain looking when you open it.  That is normal. Copy and paste the line below into Terminal prompt.  Press return after you paste it in.

`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

There will be a prompt asking if you want to continue.  Press return to continue, then it may prompt for your password.  Enter your computer user password (don't worry, Terminal app doesn't show keystrokes when you enter passwords, but it is still reading your typing).  

Wait while the script does its thing...you’ll see info scroll by and then it will pause for awhile.  Eventually, it will be done and you’ll see something that says “Installation successful” and you’ll have a ready Terminal prompt again.

<p align="center">
<img src="../img/carthage.jpg" width="450">
</p>

You can close the Terminal application now.  You’re done with it.  You do not need to do these steps again for any subsequent Loop builds. This is one of those "just do it once" installations.

Now you are ready to move onto the next steps to [Setup Apple Developer Account](https://loopkit.github.io/loopdocs/build/build-developer/).
