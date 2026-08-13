# delta-cap

Cap the change per setpoint at a fixed rate and you have a velocity limit: v_max = delta_max x f. At
100 Hz with a 1 cm cap, the drone can never be asked to exceed 1 m/s.

One legible number — and it is the gym's weight stack. You raise it as the relationship develops.
Name it as a design feature, not only a safety feature.

## Done when
- [ ] delta_max derived from control_lag (0.3.2)
- [ ] Test: command a large jump, assert commanded velocity never exceeds v_max
- [ ] Exposed as one operator dial showing the resulting m/s, not the raw delta
- [ ] `docs/safety-layer.md` written or updated — what it does, how to run it
- [ ] `DECISIONS.md` entry if a choice was made — what we picked, what we rejected, why
