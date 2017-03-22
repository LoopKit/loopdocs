# mLab Database Maintenance

Regardless of whether you are on Azure or Heroku for Nightscout, you are using an mLab database for storing your Loop data.  mLab allows you to store up to 500 MB for free.  When you hit that data cap, your NS will stop working.  Your Share Bridge will not pull data and your site will be “stale”.  

The good news?  Loop can still run just fine until you cleanout your mLab database.  The bad news?  You just won’t be able to remotely monitor Loop through NS until you clear up some storage space in mLab.

There are two ways to cleanout some space or otherwise get into your mLab database:

* mLab direct access
* Nightscout admin tools

## mLab Direct Access

*  Login to your mLab database.  

    * If you setup your own Azure site and mLab database, go directly to [mLab](http://mlab.com) and login, or

    * If you setup your own Azure site and mLab database, then setup a Heroku account and pointed back to your old mLab database (i.e., copy and pasted the MONGODB_URI from Azure), go directly to [mLab](http://mlab.com) and login, or

    * If you setup a Heroku site and let Heroku setup an mLab database for you (which is typical for new Heroku sites), you will access mLab through your Heroku account main page.   Login to your Heroku account and click on the mLab logo as shown below.

<p align="center">
<img src="../img/mlab_link.jpg" width="650">
</p> 
 
* (Users coming directly from a Heroku click will see the screen below.  If you had to login to mLab with a name and password, you will first see a line with your MongoDB database.  Click on your database name to see the screen below with all the collection names.) 

    Your various collections are shown, similar to the screen shot below.  The amount of data each collection is using is listed to the far right of each collection’s line.  I recommend emptying the “loop” collection first and then "devicestatus" to free up database storage.  If you need any of the information in the database, you may want to do a selective delete of data. For example, if you are headed into an endocrinologist appointment and want to print out recent Nightscout reports to take with you. Eventually you may need to empty more collections.  It should be awhile though, as the other collections are significantly smaller and will take a long time to fill.

    Click on a collection’s name to open it.

<p align="center">
<img src="../img/collections.jpg" width="650">
</p> 

*  Click on the button that says “Delete all documents in collection” and then confirm the deletion.

<p align="center">
<img src="../img/delete.jpg" width="650">
</p> 

*  You can confirm that your cleanout has resolved the problem, by checking that your database size is below 500 MB now.  Click on the “Home” link in top left.  Then review the size of the database as shown.

<p align="center">
<img src="../img/mlab_size.jpg" width="650">
</p> 

## Nightscout Admin Tools

If you go to your Nightscout site's settings (the three horizontal bars in the upper right of your Nightscout site), you will be able to access your Admin Tools for the site.  These include some useful quick mLab actions, includig deleting documents from the devicestatus collection similar to the action we took in the steps above.  But, it's worth noting that if you have errant future data in your Nightscout site that is causing problems (usually during time changes or overseas travel), you can clean-out future entries through this portal, too.

<p align="center">
<img src="../img/admin_tools.jpg" width="650">
</p> 


