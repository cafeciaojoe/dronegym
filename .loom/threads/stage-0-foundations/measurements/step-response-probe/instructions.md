# step-response-probe

One caged drone, hovering. Step the position setpoint. Measure how long until it visibly moves and
how far it overshoots.

Almost every number downstream comes from this — the delta cap, the leash, the collision radius.
Doing it in week one means nothing later is guessed. Take it on the FINAL cage: the reprint removes
roughly half the mass, which changes thrust-to-weight and drag and therefore all of these.

## Done when
- [ ] Step response captured at 3+ step sizes, on the final cage
- [ ] First-order lag fitted; `control_lag(speed)` written down as a curve, not a constant
- [ ] Overshoot vs commanded speed plotted
- [ ] `docs/control-lag.md` written — the numbers, how they were taken, how to retake them
- [ ] `DECISIONS.md`: what these numbers set, and what changes if the cage changes
