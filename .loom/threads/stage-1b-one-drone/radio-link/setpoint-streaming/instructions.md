# setpoint-streaming

Continuous position setpoints at a fixed rate. You are feeding the onboard controller a fresh target
faster than its own dynamics, so it never has to extrapolate. Smooth and robust, and it is what
HTTYD did.

## Done when
- [ ] Fixed-rate streaming with measured, logged jitter
- [ ] Rate chosen from the radio budget (0.3.1), not picked
- [ ] Graceful behaviour if the loop stalls — hold the last setpoint, never extrapolate
- [ ] `docs/setpoints.md` written or updated — what it does, how to run it
- [ ] `DECISIONS.md` entry if a choice was made — what we picked, what we rejected, why
