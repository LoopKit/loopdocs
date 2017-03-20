# UPDATING NIGHTSCOUT SITE

If you are new to Loop and haven’t updated your NS site since before December 1, 2016, you will want to update your NS site.  You can run either the "master" or "dev" branches of cgm-remote-monitor with Loop.  To check what version your Nightscout site is running, go to your Nightscout site and pull open the site settings by clicking on the three horizontal lines at the top right of the screen.  Scroll down and see if you are running 0.9.2-dev-20161201 or newer for "dev" branch.  Notice the “dev” branch is date stamped 0.9.x-dev-YYYMMDD; or you’ll see version 0.9.2 for "master" branch deployments.

If you are a current NS user and simply want to update your site, this procedure will work as well.

## Updating your repository in GitHub

1. Copy, paste, and goto the one of the following links depending on which branch of cgm-remote-monitor you are currently running (replace "yourgithubname" with your actual GitHub user name)

For dev branch deployments:

https://github.com/yourgithubname/cgm-remote-monitor/compare/dev...nightscout:dev

 or for master branch deployments:

https://github.com/yourgithubname/cgm-remote-monitor/compare/master...nightscout:master

![Compare changes](img/compare_repo.jpg)

Click the big green "create pull request" button. Another screen will appear, fill in a title and click button to create the pull request, and then you can "Merge Pull Request", and finally "confirm merge".
 
![Compare changes](img/update1.jpg)
![Compare changes](img/update2.jpg)
![Compare changes](img/update3.jpg)

If you don’t have your Heroku set-up to automatically update when your repository is updated, you may have to go into your Heroku “deploy” section and manually deploy your branch now that your repository has been updated.  Make sure you are connected to your GitHub cgm-remote-monitor repository.

![Heroku Deployment screen](img/deploy_branch.jpg)

## New Loopers Variables

For new Loopers (but old Nightscout users), you will need to add some variables to your Heroku site to Loop.  

