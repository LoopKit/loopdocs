# Priming and Site Changes

Loop uses event history and reservoir levels to determine how much insulin has actually been delivered through the pump, and correspondingly the Insulin On Board (IOB).  **If you manually prime your tubing WITHOUT changing reservoirs**, Loop will detect that prime as an insulin delivery and count it as IOB.  Therefore, here are some suggestions for priming, set changes, and reservoir changes with Loop in mind.

## Site Changes

* If you change sites and increase reservoir volume (i.e., start a new reservoir), don't worry. So long as you are putting in a reservoir that has more insulin than the old one, IOB will be accurate in Loop.  When Loop sees a rewind and an increase in reservoir volume, it will not count any tubing primes as IOB.

* If you change sites but **do NOT increase reservoir volume** (i.e., you keep existing reservoir going), you will need to go into Loop's reservoir history and delete 30 minutes of continuous reservoir history including the prime event.  By deleting 30 minutes of reservoir history, Loop will use Event History to determine insulin deliveries and IOB. If you cannot get the prime to clear from the IOB, operate in Open Loop mode until the insulin action duration time has passed.  Deleting history is done by:

    (1)  clicking on the Insulin Delivery Chart  

    (2)  selecting the Reservoir history screen  

    (3)  swiping to delete individual reservoir readings  

    (4)  delete at least 30 minutes of reservoir readings, including the readings that involved priming events

## Prime Menu

When you finish priming on a Medtronic pump, please make sure to complete the priming menu.  In other words, finish all the prompts so that you get back to the (nearly blank) normal Medtronic pump screen.  If you don't finish the priming menu, the pump will not begin basal insulin delivery, nor does it alarm.  It is equivalent to the pump being suspended...but you won't be able to see any indication of that in Nightscout as a remotely monitoring parent.  Loop will not detect the prime screen issue and will keep sending temp basal messages...but the pump won't enact them.  On Loop, you could notice it by the active IOB continually going down and then eventually negative IOB, as the basal is not delivered and the reservoir level remains constant.  However, the temp basal graph will still show the bars from the temp basal commands loop has been sending.

So, remember to finish those prime menu screens through to the end.
