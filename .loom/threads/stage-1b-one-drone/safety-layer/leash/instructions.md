# leash

Capping delta caps *commanded* velocity, not actual. If the drone lags and you keep advancing the
setpoint at max delta, error accumulates — you get rubber-banding, then a fast catch-up.

So cap delta AND cap setpoint-to-measured error: never let the setpoint run more than L ahead of
where the drone actually is. Two lines, and it is what kills the snap.

## Done when
- [ ] L derived from control_lag (0.3.2)
- [ ] Test with a simulated lagging drone: assert the setpoint stops advancing beyond L
- [ ] No rubber-banding under a sustained fast command
- [ ] `docs/safety-layer.md` written or updated — what it does, how to run it
- [ ] `DECISIONS.md` entry if a choice was made — what we picked, what we rejected, why
