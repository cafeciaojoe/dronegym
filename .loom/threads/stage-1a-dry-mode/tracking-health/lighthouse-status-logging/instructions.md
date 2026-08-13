# lighthouse-status-logging

Log what the deck actually knows, and characterise the failure deliberately before it happens by
accident.

    bsAvailable   we have geometry + calibration for this base station
    bsReceive     the deck is currently receiving its sweeps
    bsActive      receiving AND usable — actually contributing to the estimator

## Done when
- [ ] All three logged per base station, alongside estimator variance
- [ ] A base station occluded on purpose; the failure characterised
- [ ] Detection lag measured — how long until bsActive actually drops
- [ ] `docs/tracking-health.md` written — the three flags, the measured lag, the thresholds it implies
- [ ] `DECISIONS.md`: the threshold values and where they came from
