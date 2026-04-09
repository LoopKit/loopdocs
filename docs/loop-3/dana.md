!!! warning "🚧 Documentation Under Construction 🚧"
    
    This page is under development. 

    The addition of the Dana-i and DanaRS-v3 pump to iOS Open-Source Automated Insulin Delivery systems is new.
    
    Please review the [DanaKit Issues](https://github.com/bastiaanv/DanaKit/issues) page for open issues reported for the DanaKit Pump Manager.


!!! important
    This Issue is very important:
    
    * [When Bluetooth communication is interrupted during a bolus, cannot cancel, bolus finalized while in progress](https://github.com/bastiaanv/DanaKit/issues/34)
        * This issue prevents you from cancelling a bolus from inside the OS-AID app if Bluetooth communication with the pump is lost during a bolus


### Testing Dana with the *Loop* App

* The branch needed to get Dana in *Loop* is: `feat/dev-dana-medtrum`
    * This branch is subject to rapid updates
    * If you also want to use the Eversense CGM, the `feat/eversense` branch provides support for Dana and Medtrum along with the Eversense CGM

* Please refer to the [zulipchat Loop-dev development channel](https://loop.zulipchat.com/#narrow/channel/144182-development/topic/Loop-dev.20Status/with/515372445) before building this branch.



Most of the information needed for the Dana pump can be found here:

* [How to add a Dana Pump](add-pump.md#dana-i-danars-v3){: target="_blank" }
* [Dana Troubleshooting](../troubleshooting/dana-faq.md){: target="_blank" }
