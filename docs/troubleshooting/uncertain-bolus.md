# Pod "Uncertain Bolus"

At some point in Loop use, you may run into the situation where you try to bolus and get a message back in Loop that the bolus was "uncertain".

## Why does this happen?

An "uncertain bolus" is when the bolus command was sent by Loop, but Loop never heard back from the pod with a comfirmation message that the command was received. Therefore, Loop is uncertain about the status of that command.

## What does Loop do when this happens?

Initially, Loop assumes the worst (conservative path) and starts tracking things as if the bolus has been delivered. If Loop gets a status response from the pod to a different command while the pod is still bolusing, Loop will use the delivery glags that indicate "bolusing" or "not bolusing" to become certain about the delivery status. If no status response is received that changes the uncertainty, then the dose is considered delivered and is finalized.

## What should you do when this happens?

There isn't much you can do in this situation presently. You can "enable bolus beeps" or listen for the clicking of a bolus while it is happening. That is one good method to get a secondary confirmation by audio sleuthing.

If you are sure that the bolus failed, you can delete the bolus record from Health app and Pod's event history.

## What is Loop dev doing?

There are some various methods that could help more quickly resolve the uncertainty, but none of them are 100% perfect. There will be some changes coming to dev branch to help with these "uncertain boluses", but they won't be visible in the user interface...they will be under-the-hood of Loop code.
