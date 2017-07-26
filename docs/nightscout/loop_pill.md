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

Mouseover or Touch the Loop pill to view a tool tip containing one or more of the latest status messages. For example:

<img src="../img/loop_pill_message.jpg" width="350">

<img src="../img/loop_pill_message_error.jpg" width="350">


## Troubleshooting Loop
If you are getting unexpected status, review the [Getting a Green Loop](../use/green-loop) page. To learn more about a specific error message, review the [Common Error Messages](../use/green-loop?#common-problems) section on that page.
