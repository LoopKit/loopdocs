# Step 7: Install Homebrew

!!!danger "Time Estimate"
    * 10-15 minutes assuming you know your computer's password
    * 35 minutes if you can't remember your password and have to guess
    
!!!info "Summary"
    * Install Homebrew by simply copying and pasting a long line of gibberish into the ugly Terminal application.

!!!warning "FAQs"
    * **"What if I don't get an "Installation successful" message?"** If you don't see a successful installation message, please try the copy-paste again. If you fail to get Homebrew installed, your Loop build will also fail. You can't just skip this step. The most common cause of errors is failing to copy the ENTIRE line of code ...people sometimes fail to get that last `"` at the end of the line. Also, you need to be using a user account on the computer that has "admin" rights, since this process is installing a program on the computer.

Breath deep...this step looks kind of "programmer code" weirdness. BUT, it isn't. Well, it is...but we will be just simply copying and pasting one line of the weirdness and then walking away. We don't actually have to know much about Homebrew itself or what the line of code means exactly.

Homebrew is a program that will allow us to install the needed packages to build Loop. Before installing Homebrew, we need to double check one thing...that the user account on the computer that you are using to build Loop, that **user account needs to have Administrative rights on the computer**. How can you tell? Go to the computer's System Preferences application, open the Users & Groups section. If your account that you are using doesn't say "Admin" under your name, then you need to click the lock and change that to an Admin account before proceeding. If you are using a work computer, you may not have admin rights on that computer...so be aware that you may have restrictions on company owned computers.

<p align="center">
<img src="../img/admin-user.png" width="550">
</p>

Side note: If you are a (1) computer-savvy person and (2) already installed Homebrew on a different user account on the computer previously...please go use that user account on the computer to build Loop. Or, delete Homebrew from that User account and install on your account. Homebrew is a bit picky.

Ok, now that we have the user account confirmed, let's open the Terminal application on your computer. It is located in your Applications folder and then look in the Utilities subfolder...the Terminal application is in there like shown in the screenshot below.

<p align="center">
<img src="https://loopkit.github.io/loopdocs/build/img/terminal.png" width="550">
</p>

The Terminal app is very plain looking when you open it. That is normal. Copy and paste the line in the little grey box below into Terminal prompt. 

`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

Your screen should look like something like this after you copy it in...if it does, then go ahead and press return to continue on with the installation command. 

<p align="center">
<img src="https://loopkit.github.io/loopdocs/build/img/homebrew-copy-line.png" width="450">
</p>
</br>

There will be a prompt asking if you want to continue.  Press return to continue, then it will prompt for your password.  <u>The password is your computer's password.</u>

**<u><font color = "red">Don't freak out that you can't see your password while you type. That is normal. The Terminal app doesn't show keystrokes when you enter passwords, but it is still recording your password entry. If you think you messed up because you were confused, press the delete key a bunch of times and then start fresh with the password entry.</font></u>**  

Wait while the script does its thing...you’ll see info scroll by and then it will pause for a while. Eventually, it will be done and you’ll see something that says “Installation successful” and you’ll have a ready Terminal prompt again.</br></br>

<p align="center">
<img src="https://loopkit.github.io/loopdocs/build/img/carthage.jpg" width="450">
</p>
</br>

You can close the Terminal application now. You’re done with it. You do not need to do these steps again for any subsequent Loop builds. This is one of those "just do it once" installations. If you get a new computer though, you will have to repeat this step for the new computer.

## Uninstall Homebrew

If you have something go wrong in Homebrew installation, want to delete it and start fresh, the uninstall command is:

`ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"`

Copy and paste that entire line into Terminal application. Then you can retry the installation of Homebrew using the install command listed earlier in this page.


## Next Step: Download Xcode

Now you are ready to move onto Step 8 to [download Xcode](https://loopkit.github.io/loopdocs/build/step8/).
