# workspace-clamp

A hard boundary on where a setpoint can be, independent of the sim. HTTYD had bounded flight zones;
this is the same idea, rewritten.

## Done when
- [ ] Bounds loaded from config and checked at startup by dg-doctor
- [ ] Test: command a position outside the bounds, assert it is clamped
- [ ] Clamping is visible to the operator, not silent
- [ ] `docs/safety-layer.md` written or updated — what it does, how to run it
- [ ] `DECISIONS.md` entry if a choice was made — what we picked, what we rejected, why
