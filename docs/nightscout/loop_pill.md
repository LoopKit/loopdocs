# Loop Pill in Nightscout &nbsp; <img src="../img/loop_pill.jpg" width="120">

The Loop pill in Nightscout provides Loop status at a glance, including how many minutes ago the status was received.

## Status Indicator
A small icon in the middle of the pill indicates the latest known status.

!!! info "Status indicator symbols"
    <font style='font-size: 1.2em;'>X</font> &nbsp;
    Error in Loop

    <font style='font-size: 1.4em;'>ϕ</font> &nbsp;
    Recommending basal, but not enacting (open loop or pump suspended)

    <font style='font-size: 2em;'>⌁</font> &nbsp;
    Enacted a new temp basal

    <font style='font-size: 1.5em;'>↻</font> &nbsp;
    Loop is continuing with last temp basal, no change

    <font style='font-size: 1.5em;'>⚠</font> &nbsp;
    Warning (Loop has not completed since since the time set on your LOOP_WARN setting in NS)

## Status Information

Mouseover or Touch the Loop pill to view a tool tip containing one or more of the latest status messages. The most up-to-date NS also includes information in the Loop pill for the minimum and maximum predicted BG, eventual predicted BG, BLE comms strength, and pump comms strength (for x23 and x54 model users).

<img src="../img/loop_pill_message.png" width="750">

## Troubleshooting Loop
If you are getting unexpected status, review the Troubleshooting pages. To find a specific error message, search the site for all or part of the message.
