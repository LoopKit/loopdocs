## Build with a Browser

<span translate="no">Loop 3</span>&nbsp;can be built with a web browser using <span translate="no">GitHub Actions</span> and installed on your phone using the *TestFlight* app. This method works on any device with a browser (PC, Mac, tablet, or iPad) - no Mac computer required.

!!! success "Same App, Different Method"
    * If you prefer to use *Xcode* on your *Mac*, see [Build with *Mac*](../build/overview.md){: target="_blank" }
    * As long as you use the same *Apple Developer* account, the app you build is identical regardless of build method
    * When you install the app on your phone, settings and history are preserved; pump and CGM remain attached; selected Services are maintained

## Is This Method Right for You?

**Choose Browser Build if:**

- [x] You don't have a Mac or prefer not to use one
- [x] You want automatic monthly builds (after initial setup)
- [x] You're comfortable following step-by-step instructions with multiple accounts (Apple, GitHub)
- [x] You can dedicate 2-4 hours for first-time setup (spread over several days)

**Choose Mac Build if:**

- [x] You already have an up-to-date Mac and are comfortable with Xcode
- [x] You prefer building locally without cloud services
- [x] See [Build with Mac](../build/overview.md){: target="_blank" } for Mac requirements

## Requirements

### Phone, CGM and Pump

To use the *Loop* app, you need:

* [Compatible Phone](../build/phone.md){: target="_blank" }
* [Compatible CGM](../build/cgm.md){: target="_blank" }
* [Compatible Pump](../build/pump.md){: target="_blank" }
    * For pumps that do not support Bluetooth communications (older Medronic and Omnipod Eros), you also need a [RileyLink Compatible Device](../build/rileylink.md){: target="_blank" }

### Accounts

To build the&nbsp;_<span translate="no">Loop</span>_&nbsp;app using a browser, you need:

1. Free *GitHub* account: (instructions found at [New *GitHub* Account](secrets.md#new-github-account){: target="_blank" })
1. Paid *Apple* Developer account: ($99/year; instructions found at [*Apple* Developer Account](../build/apple-developer.md){: target="_blank" })

## Getting Started: Two Paths

Choose the path that matches your experience level:

### 🟢 Path 1: Detailed Step-by-Step (Recommended for First-Time Builders)

Follow the detailed instructions below with screenshots, explanations, and help at every step.

**Start here:** [Introduction and Summary](intro-summary.md){: target="_blank" }

### 🔵 Path 2: Quick Reference (For Experienced Users)

If you're comfortable with GitHub and Apple Developer portals, use the condensed version:

* **Documentation:** [Using GitHub Actions + FastLane to deploy to TestFlight](https://github.com/LoopKit/LoopWorkspace/blob/main/fastlane/testflight.md){: target="_blank" }
* **Video Guide:** [How to Build Loop With a Web Browser](https://www.youtube.com/watch?v=kiu5ho0MTW8) (shows version 3.2.3; some steps simplified in 3.4.1+, others added when an *Apple* interface was changed))

---

## Step-by-Step Build Process

The following pages guide you through the complete browser build process:

1. [Introduction and Summary](intro-summary.md){: target="_blank" }
1. [Collect Secrets](secrets.md){: target="_blank" }
    * Some from *Apple*
    * Some from *GitHub*
1. [Prepare Fork](prepare-fork.md){: target="_blank" }
1. [Prepare Identifiers](identifiers.md){: target="_blank" }
1. [Prepare App](prepare-app.md){: target="_blank" }
1. [Prepare *TestFlight* Group](tf-users.md){: target="_blank" }
1. [Build the *Loop* App](build-yml.md){: target="_blank" }

---

## After Building: Next Steps

Once your build completes successfully:

1. **[Install on Phone](phone-install.md){: target="_blank" }** - Use TestFlight to install the app on your iPhone
2. **[Update/Rebuild](bb-update.md){: target="_blank" }** - Learn how to update your app (much easier than initial build!)
3. **[Build Other Apps](other-apps.md){: target="_blank" }** - Optional: Build LoopCaregiver, LoopFollow, or other apps using the same setup

---

## Need Help?

!!! question "Stuck? Don't Get Frustrated!"
    First-time setup involves many steps across different websites. If something isn't working:

    **→ [Get Help from Mentors](bb-errors.md#help-with-errors){: target="_blank" }**

    Just provide your GitHub repository link and a brief description. Mentors can view your logs and guide you.

**Common troubleshooting resources:**

* [Most Common Mistakes](bb-errors.md#most-common-mistakes){: target="_blank" }
* [Complete Error Reference](bb-errors.md){: target="_blank" }
* [How to Find Help](../intro/loopdocs-how-to.md#how-to-find-help)

!!! warning "Please DON'T..."
    * Search Google or ask ChatGPT about your error
    * Spend hours frustrated
    * Delete your repository or GitHub account
    * Remove your app from App Store Connect

    **→ Ask a mentor instead!** They can quickly diagnose issues from your repository link.

---

## Additional Topics

### Automatic Updates

!!! success "Check Status of Build Action Monthly"
    The automatic build actions should occur every Sunday. They do for all OS-AID apps except for *Loop*, and even for *Loop*, some people are getting automatic builds.  ([We do not know why.](https://github.com/orgs/community/discussions/181236)) 

    * Keep your Apple Developer account active
    * Install updates from TestFlight when ready
    * **Note:** Starting May 2025, you may need to [manually trigger builds](automatic.md#manual-action-for-automatic-build){: target="_blank" } every 60 days

    Learn more: [Automatic Update & Build](automatic.md){: target="_blank" }

### Customization

Want to customize your Loop app? Both methods are supported:

* [Customize using Browser](custom-browser.md){: target="_blank" } - Configuration changes
* [Custom Edits with Browser](edit-browser.md){: target="_blank" } - Code modifications

### Development Version

For advanced users who want cutting-edge features before official release:

* [Build Development Version](build-dev-browser.md){: target="_blank" }

!!! tip "Build Stable First"
    We recommend building the stable release version first. Once successful, you can switch to the development version.

### Comparison: Browser vs Mac Build

| Feature | Browser Build | Mac Build |
|---------|--------------|-----------|
| **Device Required** | Any device with browser | Mac with recent macOS |
| **Xcode Required** | No (GitHub provides) | Yes (must update regularly) |
| **Initial Setup Time** | 2-4 hours over several days | 1-2 hours (if Mac is ready) |
| **Monthly Updates** | Automatic to TestFlight<br>[Manual Actions](automatic.md#manual-action-for-automatic-build){: target="_blank"}| Manual via Xcode |
| **Build Time** | ~1 hour (in cloud) | ~30 minutes (local) |
| **App Expiration** | 90 days (TestFlight) | 1 year |
| **Customization** | Supported | Supported |

Both methods produce the identical Loop app. Choose based on your available hardware and preferences.

