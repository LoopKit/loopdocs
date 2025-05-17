## Test Settings

!!! info "Time Estimate"
    - 2 hours to review the rest of *LoopDocs* (particularly the [Set Up](../loop-3/loop-3-overview.md){: target="_blank" }, [Operate](../operation/loop/open-loop.md){: target="_blank" }, and [FAQs](../faqs/overview-faqs.md){: target="_blank" } sections) and [LoopTips](https://loopkit.github.io/looptips/)
    * If you like quizzes, this older quiz has not been updated for version 3 of the *Loop* app and not all the links work (when your answers are scored), but the questions are still really good and the scoring report provides extra insight into why your answer was right or wrong
        - 15 minutes to take [this quiz](https://docs.google.com/forms/d/e/1FAIpQLSfTkL0pWC-x3a5l_I3aJYBSx3xAS7dtkBbQiiLd348H70TTWg/viewform) to confirm you understand the *Loop* app expected behavior
        * New with version 3 of the *Loop* app: 
            * you can remote bolus
            * you can set a manual temp basal rate
            * DASH pods can be used without a RileyLink
                * restarting your app or turning Bluetooth on and off replaces the Rileylink power cycle trouble-shooting tip
            * Nightscout with Heroku is no longer free, but there are other options
            * you do NOT need a Mac computer if you use [Build with Browser](../browser/bb-overview.md)
    - 1-3 days to test settings for safety and to get the most out of the *Loop* app
        * This step can be done after you build the *Loop* app, just stay in [`Open Loop`](../operation/loop/open-loop.md) while you test

!!! abstract "Summary"
    - Before you use <code>Closed Loop</code> mode, test and validate your basal rates, ISF (correction factor), and CR (carb ratios)
	- You may need to adjust your settings for the *Loop* app
	- Accurate settings are vital for success

!!! question "FAQs"
    - **"My endo chose my pump settings, so do I need to test them?"** Yes. Your endo chose your settings in a  different context, with different constraints. What is safe and ideal in traditional pump therapy, may not be the best selection for the *Loop* app. Testing your settings, even for just a couple days, makes a big difference.
    - **"I have great control, why would I need to test my settings?"**  "Great control" may be due to lots of adjustments - bumps and nudges of insulin or carbs. Those bumps and nudges may be covering for underlying settings that need adjustment. If you are coming from a treatment style that involves memorizing your insulin doses for meals, you may not know your actual CR or ISF. Testing is key to success with the *Loop* app.
    - **"I can't basal test with my 2-year-old. What can I do?"** That is pretty tough. Consult your endo, watch your patterns, and do the best you can...little kiddos are a difficult group to test settings. Once you become comfortable with the *Loop* app, there are tricks to adjust settings while staying in closed loop as long as settings are fairly close.

Loop is just a fancy calculator underneath the hood. The math problems it solves depend on the settings you provide. So test settings before using the *Loop* app.

## Basal Rates

Correct basal rates keep your blood glucose steady without food present. The standard method is to test your basal by having a relaxing 4-6 hours without eating at least two hours before you begin the test. Does your blood sugar stay steady? Or do you climb and need a correction? Or do you go low and need to eat? Setting basal is a crucial step to setting yourself up for success with the *Loop* app. It determines how much of the insulin delivered (from basal and bolus) is counted as insulin on board (IOB).

!!! tip "Basal Tricks"
    The *Loop* app keeps track of how much more or less insulin than your scheduled basal rates are required to keep glucose in target. Once you become a proficient looper, you can tune your basal by looking at IOB overnight or when food and exercise are not involved.

## Insulin Sensitivity Factor

The Insulin Sensitivity Factor (ISF), sometimes called Correction Factor, is how much one unit of insulin will bring down your glucose. The higher the value of this setting, the more sensitive to insulin you are. An ISF of 50 or 100 (2.8 or 5.5) means one unit of insulin lowers your glucose 50 or 100 mg/dL (2.8 or 5.5 mmol/L) in the absence of food or activity, when basal rates are correct.

 Test ISF after you test and determine your basal rates. Simply bring yourself to a higher glucose with a glucose tab or choose a time when you are "stuck" higher than your target.
 
 * Calculate how much insulin is required to lower your glucose to target, take it and observe if your glucose flattens out at your target within 3 hours
    * Do not do this test if you have recently eaten, recovered from a low glucose, engaged in physical activity, are sick or under stress
* A starting point for ISF is to take total daily dose and divide that into 1800
    * This is just a starting point, many people have higher or lower ISF than this formula suggests
    * Example, you take 30 U a day and have no idea what your ISF should be
        * Start with 60 mg/dL (3.2 mmol/L) and test it

## Carb Ratio

The Carb Ratio (CR) is the amount of carbs covered by one unit of insulin. Ideally, a good carb ratio will restore your glucose close to its starting point within 3 hours *of the meal*. (High fat/protein meals may cause glucose to be impacted longer.)

If you are spiking higher than you’d like after a meal, but still coming back to the starting glucose, consider pre-bolusing your meal earlier (maybe by 15-20 minutes) rather than changing the carb ratio.

## Other Resources

Check the companion site [LoopTips](https://loopkit.github.io/looptips). Several direct links to discussions are provided below:

* How to [check settings](https://loopkit.github.io/looptips/settings/settings/) 
* [Why settings are important](https://loopkit.github.io/looptips/settings/overview/)
* [What to do when you need to change settings](https://loopkit.github.io/looptips/settings/adjust/) which covers short term and long term reasons

If you’re fascinated by this topic, read the book *'Think Like A Pancreas'* by Gary Scheiner for a really great discussion.

## Next Step: Make Plans for `Loop Data`

Now you are ready to make plans for [Loop Data](loop-data.md).
