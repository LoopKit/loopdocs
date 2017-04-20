# mLab Database Maintenance

Regardless of whether you are on Azure or Heroku for Nightscout, you are using an mLab database for storing your Loop data.  mLab allows you to store up to 500 MB for free.  When you hit that data cap, your NS will stop working.  Your Share Bridge will not pull data and your site will be “stale”.  

The good news?  Loop can still run just fine until you cleanout and/or compact your mLab database.  The bad news?  You just won’t be able to remotely monitor Loop through NS until you clear up some storage space in mLab.

Note there are two areas where the 500 MB data limit can be an issue.  One is called the `size` which is the actual data stored in your database.  The other is called `size on disk` which is the virtual space that your database takes up.  As data is written onto your free database, sometimes it is written inefficiently and virtually "spreads out" to take up more room.  Depending on where your issue is, you may need to delete or cleanout data (if `size` is the issue) or you may just need to compact data (if `size on disk` is the issue).

<p align="center">
<img src="../img/mlab_size2.jpg" width="650">
</p> 

## Cleanout mLab
There are two ways to cleanout space and delete data in your mLab database:

* mLab direct access
* Nightscout admin tools

### mLab Direct Access

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

*  You can confirm that your cleanout has resolved the problem, by checking that your database size is below 500 MB now.  Click on the `Home` link in top left.  Then review the size of the database as shown.

<p align="center">
<img src="../img/mlab_size.jpg" width="650">
</p> 

### Nightscout Admin Tools

If you go to your Nightscout site's settings (the three horizontal bars in the upper right of your Nightscout site), you will be able to access your Admin Tools for the site.  These include some useful quick mLab actions, includig deleting documents from the devicestatus collection similar to the action we took in the steps above.  But, it's worth noting that if you have errant future data in your Nightscout site that is causing problems (usually during time changes or overseas travel), you can clean-out future entries through this portal, too.

<p align="center">
<img src="../img/admin_tools.jpg" width="650">
</p> 

## Compact mLab

You may get an email from mLab, even after cleaning out enough space in your database, alerting you that your "file size limit" may have been exceeded. 

<p align="center">
<img src="../img/mlab_compact.jpg" width="650">
</p> 

To begin the compaction process, click on your database name.

<p align="center">
<img src="../img/mlab_compact1.png" width="650">
</p> 

Then click on the `Tools` tab in the screen that opens.  Click on the `commands` button and then select the `repairDatabase` from the dropdown menu of available commands.  At the bottom of the screen, select the `Run Command` button. 

<p align="center">
<img src="../img/mlab_compact2.png" width="650">
</p> 

Return to your home screen and you will be able to verify the `Size on Disk` has decreased.

<p align="center">
<img src="../img/mlab_compact3.png" width="650">
</p> 

