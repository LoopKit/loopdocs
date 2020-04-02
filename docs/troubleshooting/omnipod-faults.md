# Omnipod Faults

Pod faults are shown in the HUD:
<p align="center">
<img src="../img/pod-hud-fault.png" width="250">
</p></br>

Loop will put a higher battery load on a pod than the PDM due to its regular and repeated communications. A pod with lower battery level appears to be more likely to fault for conditions like static electricity and occlusions/pump issues that Loop is not directly causing, like internal fault codes 052, 061, 064 and 066. Pods always perform safety checks and if a potential problem is found, the pod will end itself by screaming and stop with the insulin delivery.

!!! note
    During extensive tests after getting all commands working properly, many failures due to one specific safety check were still encountered. This check needed to recover its counter within 30 minutes after a temp basal returning to a normal basal schedule, or else the pod would scream. Eventually, this was resolved by disabling _only_ this particular check. Therefore the 096-106 faults are always ignored in the current configuration of Loop.



## Known internal pod fault codes
The currently known pod faults are listed here on the openomni wiki page: [Pod Fault codes](https://github.com/openaps/openomni/wiki/Fault-event-codes)

## Ways to reduce the possibility of a fault

None of the ways listed here are certain to reduce the possibility of a screaming pod, but they could be worth considering if the hypothesis of a low battery is indeed the cause of some late-in-life pods.

* Keep the Loop app up to date; newer versions might include improvements to reduce pod battery load
* Do not use the "neutral temp basal" code customization
* Use a 433 Mhz RileyLink

## Not "replacement pod" situations

Normal pod use can still give these two internal pod faults, which are not eligible for a replacement pod:
* 028, Pod expired
* 024, Empty reservoir

## Replacement pod situations
You can always call Insulet tech support if a pod has a clear failure on the pod, such as:

* A cannula was sticking out when the end cap was removed.
* Visual inspection of the pod's cannula window indicating the cannula insertion was not successful.
* Leaking or kinked cannula was causing insulin delivery issues.
* The adhesive was not working properly when trying to place it on your body.

If the pod fails during use with Loop, a replacement might still be possible. However, the software which communicates with the pod isn't developed or supported by Insulet. Generally speaking, calling in failed pods for reasons not listed, above mid-pod life, maybe a bit of a reach for the DIY community. There is a grey area here that we should be careful of and acknowledge that Looping may be a cause in certain faults.


