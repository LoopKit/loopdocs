## *Loop* Services

Near the bottom of your *Loop* settings screen is a section called "Services".

!!! question "Sevices are Optional"
    * *Loop* will work whether you use these or not.
    * *Nightscout* is highly recommended by experienced Loopers but can be added later - you don't need it to get started.

The services are added by tapping on the &plus; sign and choosing the service from the list. Services are shown alphabetically. The most common services are [*Nightscout*](#nightscout) and [*Tidepool*](#tidepool).

![img/services.JPG](img/loop-3-services.png){width="350"}
{align="center"}

## *Nightscout*

There is a whole section in LoopDocs about *Nightscout*. Please follow this link to the [Using *Nightscout* with *Loop*](../nightscout/overview.md){: target="_blank" } section of LoopDocs. That also has the links you might need to the official [*Nightscout* Documentation](https://nightscout.github.io/){: target="_blank" } (different website).

If you have an existing *Nightscout* site, it's still a good idea to review that section, but here's the quick summary of how to add your Site URL and API_SECRET to have your *Loop* data transmitted to your *Nightscout* site. If you can’t remember your API_SECRET, it can be found under Settings, Reveal Config Vars for Heroku sites (or Application Settings, Connection Strings for Azure sites).

The two most common errors in filling out this section are:

1. Failure to use `https://`  in the site URL.  If you use `http://` (see how that doesn't have the "s" at the end?), you will get an error message about an App Transport Security policy.
2. Having a trailing slash on the end of the URL (or an embedded space). If you copy and paste from a web browser, make sure to delete the trailing slash on the URL entry.

!!! tip "More Tips about *Nightscout*"
    * One family had an app configured to block some websites for their child's phone and accidentally blocked their *Nightscout* URL - took them a while to figure out that mistake.

## *Tidepool*

Data can be directly uploaded from *Loop* to *Tidepool* by adding it as a Service.

Please refer to the [LoopTips: Data: *Tidepool*](https://loopkit.github.io/looptips/data/tidepool/){: target="_blank" } page for more information about *Tidepool*.

When you add the *Tidepool* Service to *Loop*, be sure to disable *Tidepool* Mobile ability to read from Apple Health.

![img/services.JPG](img/loop-3-tidepool-mobile.png){width="350"}
{align="center"}

!!! warning "Double entries"
    If you have *Tidepool* Mobile installed on your phone, with the Connect to Health feature enabled, while also using the *Tidepool* Service in *Loop*, all of your carb and insulin records will be doubled on the *Tidepool* Web browser display.

    Even when you turn off the access to Health on the *Tidepool* Mobile app when you turn on *Loop* *Tidepool* service, you will still get 7 days of overlap because *Loop* stores 7 days of data.

    There is a filter button on the *Tidepool* Website you can use to separate the two data sources.

You can still use the note taking feature with *Tidepool* Mobile when Health is not connected, although you must have internet connectivity for this to work.

*Tidepool* Support is available to help troubleshoot issues or answer questions about using *Tidepool*. Contact them via email at support@tidepool.org.

## Loggly

[Loggly](https://loggly.com){: target="_blank" } is a free logging service. If you sign up for an account, you'll need to go under Source Setup and then Customer Tokens. Copy and paste your customer token into your *Loop* App settings for Loggly.

![img/loggly.png](img/loggly.png){width="500"}
{align="center"}

## Amplitude

[Amplitude](https://amplitude.com){: target="_blank" } is a remote event monitoring service and can be used to quickly identify errors and events with *Loop*. Amplitude stores the events and allows you to view those events as points in time. To retrieve the details of the events you will need to look at corresponding mLab data entries to get a complete picture of the issues. If you sign up for a free account with Amplitude, you will be given an API Key that you can enter here to have *Loop* integration setup.

![img/amplitude.png](img/amplitude.png){width="500"}
{align="center"}

## Next Step: *Loop* Displays

Great job, almost finished! Now that you have completed your services, let's move onto understanding your [*Loop* Displays](displays-v3.md). This page is a valuable tool for understanding your Loop and a great page to review when troubleshooting.
