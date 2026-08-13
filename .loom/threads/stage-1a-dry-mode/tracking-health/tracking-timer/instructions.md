# tracking-timer

A timer on bsActive with two constants. Not a subsystem.

    t = now - last_time(bsActive != 0)
    t < T_DEGRADE  -> TRACKING
    t < T_LOST     -> DEGRADED   (freeze setpoint / freeze proxy)
    else           -> LOST       (controlled descent)

For a handheld that goes DEGRADED, freeze its proxy rather than feeding garbage into the sim. A lost
hand tracker that keeps streaming is how you get a 3 m/s virtual punch.

The freeze must be visible to the operator, so staff can prompt the person back into coverage.

## Done when
- [ ] Thresholds taken from 1a.1.1's measurements
- [ ] Handheld freeze and recovery both tested — the recovery is the part that used to be a punch
- [ ] Operator sees the state, not just the log
- [ ] `docs/tracking-health.md` written or updated — what it does, how to run it
- [ ] `DECISIONS.md` entry if a choice was made — what we picked, what we rejected, why
