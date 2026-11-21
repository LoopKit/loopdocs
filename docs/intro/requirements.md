## Two Ways to Build the App

You get the same app either way:

* [Build with Browser](../browser/bb-overview.md)
    * Build with a browser on any computer or tablet
    * The app installs on your iPhone with *TestFlight*
    * Most new builders choose this method
* [Build with *Mac*](../build/overview.md)
    * Build on a *Mac* with *Xcode*, with your iPhone connected
    * You must keep *macOS* and *Xcode* up to date
    * Consider this method if you already own a *Mac*

!!! warning "Best Practice: Learn to Build"
    Build the&nbsp;<span translate="no">Loop</span>&nbsp;app yourself.

    * _<span translate="no">LoopDocs</span>_&nbsp;does not link to services that build the app for you
    * If you use one anyway, first read&nbsp;_<span translate="no">LoopDocs</span>_, learn how to set up and operate the app, and ask which DIY features their version leaves out
    * **These steps are important for your safety**

## Common Requirements

You need these whichever way you build:

1. [Compatible iPhone](../build/phone.md)
1. [Compatible Pump](../build/pump.md)
1. [Compatible CGM](../build/cgm.md)
1. [RileyLink Compatible Device](../build/rileylink.md)
    * Not needed with Omnipod 5, Omnipod DASH, Medtrum, Dana or Tandem Mobi
    * Required for Medtronic and Omnipod Eros
1. [Apple Developer Membership](../build/apple-developer.md)
    * Building for a child? Read [Loopers Need Their Own Apple ID](../build/apple-developer.md#loopers-need-their-own-apple-id)
    * Build with Browser needs a paid account
    * Build with *Mac* can use a free account, but you must rebuild every 7 days

### Added Requirements to [Build with Browser](../browser/bb-overview.md){: target="_blank" }

* A free *GitHub* account

### Added Requirements to [Build with *Mac*](../build/overview.md){: target="_blank" }

* A [Compatible Computer](../build/computer.md#check-your-macos-version)
* [Xcode](../build/xcode-version.md) (free from *Apple*)

## Cost and Time

Beyond your pump, CGM, supplies and insulin, plan for these costs:

| Item | Cost | Notes |
|---|---|---|
| *Apple* Developer Program | $99 per year | Required for Build with Browser; Build with *Mac* can use a free account if you rebuild every 7 days |
| RileyLink compatible device | About $150 each, one time | Only for Medtronic and Omnipod Eros; a spare is recommended |
| *GitHub* account and *Xcode* | Free | |
| *Nightscout* (optional) | Free or a small cost if you build it yourself, or a monthly fee from a provider | See [Loop Data](../build/loop-data.md) |

And for this time:

| Step | Time |
|---|---|
| Check your phone, pump and CGM | Less than an hour |
| Order a RileyLink compatible device, if needed | 15 minutes, plus shipping |
| Enroll in the *Apple* Developer Program | 15-20 minutes, then up to 2 days for *Apple* to confirm |
| Build the app | A few hours, which you can spread over several days |
| Test your settings | 1-3 days, in Open Loop |

## Getting Ready to Build

!!! tip "Simulator Option"
    You can try the *Loop* app with a simulated CGM and pump, without any hardware. You can also give it real CGM data from *Dexcom Share* or *Nightscout*.

    Simulators work with either build method. They stop working when the phone is locked or the app is in the background, because only a real pump or CGM can wake the app.
    
    See [Simulator](../version/simulator.md){: target="_blank" }.

Read the pages for your build method more than once before you start. Then work through them at your own pace. If you get confused, [ask for help](../intro/loopdocs-how-to.md#how-to-find-help).

After you build, continue with [Set Up](../setup/overview.md) and [Operate](../operation/loop/open-loop.md).

## Next Step

Start with [Compatible iPhone](../build/phone.md), then use Next (or the `n` key) to go through the rest of the Intro pages. If you have already reviewed them, go to [Build with Browser](../browser/bb-overview.md) or [Build with *Mac*](../build/overview.md).
