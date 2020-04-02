# Loop Crashes Upon Opening

If your Loop app crashes immediately upon opening, you have a problem that needs to be fixed. What do I mean by "crashes"? That your Loop app immediately turns to a white screen and shuts itself down, landing you back at your iPhone's main screen. No amount of tapping will let you keep your Loop app open.

There are only two potential causes of this: 

1. App expired, or
2. A correction range was saved backward.

## Expired app 

Your Loop app has an expiration date. The expiration date will depend on the type of developer account that signed the app.

* If you build with a free account, your app will expire after 7 days.
* If you build with a paid account, your app will expire after 12 months.

Many people *accidentally* build with their old free account even after buying a paid account. How can you tell which you're signing with? The free signing team has the `(Personal Team)` listed after your name in the signing team.

If your app expires, you simply need to plug your phone back into the computer and press the play button on your project again. This will rebuild. If you want to change to a paid signing team before rebuilding, please make sure to double-check which signing team is selected before building again. 

## Incorrectly entered correction range

!!!info "Important To Know"
    Correction ranges in Loop are to be entered in minimum-maximum...in other words, LOW-HIGH. If you enter the range backward, your app will crash as soon as Loop tries to use that backward target range...that could be immediately or at a time in the future, depending on when the backwards entry is in your schedule.
    
    * An example of a properly entered correction range: 100-120 mg/dL
    * An example of an improperly entered correction range: 120-100 mg/dL

    Please be careful when entering in the correction range. Follow the greyed out text suggestions in the Loop user interface that say `min-max`.

This issue has been fixed in the latest release of Loop.  If your app crashes because of an improperly set correction range, verify you are running Loop v2.0.

If you continue to experience similar crashes with Loop v2.0 or later, generate an [Issue Report](https://loopkit.github.io/loopdocs/troubleshooting/overview/#issue-report) and submit it to the Loop developers via GitHub.


