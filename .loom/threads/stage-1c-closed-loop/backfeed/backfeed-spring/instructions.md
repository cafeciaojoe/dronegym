# backfeed-spring

A weak, well-damped spring from the drone's measured pose to its sim node.

Weak AND damped, not just soft. The loop is sim node -> setpoint -> drone -> measured pose -> sim
node, and roughly 30-40 ms of loop delay is exactly what turns a spring into an oscillator. It should
settle because the drone lags its setpoint (loop gain below 1) and the spring is weak — but that gets
measured, not assumed.

## Done when
- [ ] k_back much smaller than k_creature, with damping chosen rather than defaulted
- [ ] Applies to drones only, never to hand proxies
- [ ] Off switch — the fallback is to disable it and accept sim/room divergence
- [ ] `docs/backfeed.md` written
- [ ] `DECISIONS.md`: why the drone gets it and the hand does not
