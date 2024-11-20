## Set Up Users and Access (TestFlight)

> You repeat this step if you need to add a User to your account. For example, you want to add another adult who can install the app on your child's phone or you want a spouse or friend to have a copy of the app on their phone as backup for a trip.

> As a developer, you are already included as a user with the Role of Account Holder, Admin. But you will need to add yourself to the TestFlight internal test group for each app you build.

Once the first build for a given app completes, you will be able to [Configure *TestFlight* Internal Testing Group](#configure-testflight-group-for-the-app) for that app.

!!! tip "Add Each User One Time"
    Once you add a user to have access to your TestFlight internal test group for an app, you don't need to do it again - it remains available to them across rebuilds and different versions for that app.

You are configuring a private capability for your family using an Internal Testing group. You need the *Apple ID* email address for each adult installing from your build. When building for a child, you will use your own *Apple ID*, not theirs. See [*TestFlight* for a Child](phone-install.md#testflight-for-a-child).

First you need to add the email address(es) to your *App Store Connect* Access Users list:

* Open this link: [Users and Access](https://appstoreconnect.apple.com/access/users){: target="_blank" }
    * You must provide a role for each person - `Customer Support` is a good choice
    * Once you have added them here, you'll be able to select them in the `TestFlight` internal test group for each of your apps

![add email and role for your users](img/add-users.png){width="700"}
{align="center"}

### Configure *TestFlight* Group for the App

1. Open this link: [App Store Connect / Apps](https://appstoreconnect.apple.com/apps){: target="_blank" } to view your apps; log in if needed.

    * Select your *Loop* app
    * Click on the `TestFlight` tab
    * **If you already have an Internal Testing Group for this app, skip to Step 4**
    
1. Click the blue plus button (<font color="#2997FF">:material-plus-circle:</font>) next to `Internal Testing` to add a group.

    ![open TestFlight tab for your app](img/setup-testflight-01.png){width="700"}
    {align="center"}

1. Fill out the name you want for the `Internal Testing` group
    * Be sure to check the box `Enable automatic distribution`
    * Click `Create` when done

    ![add email and role for your users](img/setup-testflight-02.png){width="700"}
    {align="center"}

1. You can add or remove emails to the Internal Test Group as any time
    * Click in the box beside each person you want to include
    * Each person in this group will get an email each time you update (build again) using the <code>*GitHub* Browser Build</code> method
    * Click `Add` when you are done
    * If building for a minor child, you will send the invitation to yourself or another person because a minor child is not authorized to use *TestFlight*: See [TestFlight for a Child](phone-install.md#testflight-for-a-child)

    ![select your users for the testing group](img/setup-testflight-03.png){width="700"}
    {align="center"}

## Next Step

It is now time to install your *Loop* app using the *TestFlight* app on the phone: [Install on Phone](phone-install.md).