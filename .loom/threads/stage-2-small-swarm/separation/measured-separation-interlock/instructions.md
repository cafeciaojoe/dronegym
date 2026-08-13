# measured-separation-interlock

Minimum separation enforced on MEASURED drone positions, outside the sim, as a hard interlock.

Why this exists: the sim's collision volumes are the primary separation mechanism, but the backfeed
spring (1c.1.1) drags a lagging drone's sim node backwards — which frees space in the sim that a
neighbour then advances into. So the backfeed erodes the separation margin exactly when the drones
are struggling to keep up. The sim must not be the only thing keeping them apart.

## Done when
- [ ] Interlock trips on measured positions alone, with the sim disabled
- [ ] Trip threshold derived from control_lag(speed) (0.3.2), not guessed
- [ ] Verified by 2.2.3
- [ ] `docs/separation.md` updated — both mechanisms, and why one is not enough
- [ ] `DECISIONS.md`: the interaction, written down so it is not rediscovered
