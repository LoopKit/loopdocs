# Overview

Loop’s algorithm for adjusting insulin delivery is oriented around making a glucose prediction.  Every five minutes, triggered by new BG data, it generates a new prediction.  Both [bolus recommendations](bolus) and [temporary basal rates](temp_basal) are set based on this prediction.

## Terminology

This graph and legend illustrates terms commonly used in discussing Loop's algorithm,
and shows them in the context of historical and forecasted BG in a style similar to the
status screen of Loop.

![Chart illustrating terms](img/terms_graph.png)

<dl>
<dt>Insulin Action Duration</dt><dd>A configuration value that provides an estimate of how long insulin stays active after delivery.</dd>
<dt>Target Range</dt>
<dd>This is the low and high BG values that Loop will attempt to keep you between.</dd>
<dt>Predicted Glucose</dt>
<dd>Loop makes a prediction of glucose values out for a length of time equal to your Insulin Action Duration.</dd>
<dt>Eventual BG</dt>
<dd>The last value of the prediction.</dd>
<dt>Minimum BG</dt>
<dd>The lowest glucose value at any point in time within the prediction.</dd>
<dt>Minimum BG Guard</dt>
<dd>A configuration value below which Loop will suspend all insulin delivery.<dd>
<dt>CGM Data</dt>
<dd>Actual glucose measurements made by a continuous glucose monitor.<dd>
<dt>Insulin Sensitivity</dt>
<dd>A configuration value that provides an estimate of how much blood glucose will drop given a unit of insulin.</dd>
</dl>
