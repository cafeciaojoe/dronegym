# jump-rejection

Reject any incoming sample implying a speed above a human arm (~4 m/s). Single sample, computed on
data you already have, so it is the fastest of the three mechanisms and it costs nothing.

This matters because the EKF keeps dead-reckoning through a dropout. For a handheld with no thrust
model that is double-integrated accelerometer noise — the position doesn't freeze, it wanders, then
snaps when Lighthouse returns.

## Done when
- [ ] Threshold set from measurement, not assumption
- [ ] Unit tests: a synthetic jump is rejected, fast-but-real arm motion is not
- [ ] Rejections counted and visible to the operator, not silently swallowed
- [ ] `docs/tracking-health.md` written or updated — what it does, how to run it
- [ ] `DECISIONS.md` entry if a choice was made — what we picked, what we rejected, why
