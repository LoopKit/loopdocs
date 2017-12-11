# Glucose Prediction

Loop makes a new glucose prediction every five minutes by computing the effects
of insulin that has been administered from the pump, and carbohydrate records that
have been entered into Loop. Two additional terms, glucose momentum, and optionally
retrospective correction will also be used.

You can see the individual contributions of these effects by tapping on the
predicted glucose graph on Loop's status screen.

This section needs to be fleshed out with details of how insulin and carb
effects are calculated, and how momentum and retrospective correction work. For
now, refer to:

  -  [CarbStore.getGlucoseEffects()](https://github.com/LoopKit/LoopKit/blob/master/CarbKit/CarbStore.swift#L615)
  - [DoseStore.getGlucoseEffects()](https://github.com/LoopKit/LoopKit/blob/master/InsulinKit/DoseStore.swift#L936)
  -  [GlucoseStore.getRecentMomentumEffect()](https://github.com/LoopKit/LoopKit/blob/master/GlucoseKit/GlucoseStore.swift#L244)
  - [LoopDataManager.updateRetrospectiveGlucoseEffect()](https://github.com/LoopKit/Loop/blob/master/Loop/Managers/LoopDataManager.swift#L445)
