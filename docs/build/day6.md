# Step 6: Install Homebrew

Breath deep...this step looks kind of "programmer code" weirdness. BUT, it isn't. Well, it is...but we will be just smply copying and pasting one line of the weirdness and then walking away. We don't actually have to know much about Homebrew itself or what the line of code means exactly.

Homebrew is a program that will allow us to install the needed packages to build Loop. Open the Terminal application on your computer. It is located in your Applications folder and then look in the Utilities subfolder...Terminal application is in there like shown in the screenshot below.

<p align="center">
<img src="https://loopkit.github.io/loopdocs/build/img/terminal.png" width="550">
</p>

Terminal app is very plain looking when you open it. That is normal. Copy and paste the line in the little grey box below into Terminal prompt. 

`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

Your screen should look like something like this after you copy it in...if it does, then go ahead and press return to continue on with the installation command. 

<p align="center">
<img src="https://loopkit.github.io/loopdocs/build/img/homebrew-copy-line.png" width="450">
</p>
</br>

There will be a prompt asking if you want to continue.  Press return to continue, then it will prompt for your password.  <u>The password is your computer's password.</u>

**<u><font color = "red">Don't freak out that you can't see your password while you type. That is normal. Terminal app doesn't show keystrokes when you enter passwords, but it is still recording your password entry. If you think you messed up because you were confused, press the delete key a bunch of times and then start fresh with the password entry.</font></u>**  

Wait while the script does its thing...you’ll see info scroll by and then it will pause for awhile. Eventually, it will be done and you’ll see something that says “Installation successful” and you’ll have a ready Terminal prompt again.</br></br>

<p align="center">
<img src="https://loopkit.github.io/loopdocs/build/img/carthage.jpg" width="450">
</p>
</br>

You can close the Terminal application now. You’re done with it. You do not need to do these steps again for any subsequent Loop builds. This is one of those "just do it once" installations. If you get a new computer though, you will have to repeat this step for the new computer.

!!!danger "Time Estimate"
    * 10-15 minutes assuming you know your computer's password
    * 35 minutes if you can't remember your password and have to guess

!!!warning "FAQs"
    * **"What if I don't get an "Installation successful" message?"** If you don't see an installation successful message, then please try the copy paste again. If you fail to get Homebrew installed, your Loop build will also fail. You can't just skip this step. The most common cause of errors are failing to copy the ENTIRE line of code ...people sometimes fail get that last `"` at end of the line. Also, you need to be using a user account on the computer that has "admin" rights, since this process is installing a program on the computer.

!!!info "Summary"
    * Install Homebrew by simply copying and pasting that long line of gibberish into the ugly Terminal application.

