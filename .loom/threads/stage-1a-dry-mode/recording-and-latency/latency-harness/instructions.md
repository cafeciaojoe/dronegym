# latency-harness

Measured, not estimated. Jerk the handheld, timestamp it, timestamp when the outgoing setpoint
changes, subtract. Do not add up component datasheets and hope.

Latency is the delay. Jitter is how much the delay varies — and jitter is the one that ruins the
feel, because a person adapts to a constant 40 ms but cannot adapt to something bouncing between 10
and 80.

Be honest about what this measures. The felt loop includes the drone physically moving, and a caged
Crazyflie's own response time (0.3.2) will dominate everything the software does. This number is the
software path only.

## Done when
- [ ] Median and spread measured end-to-end, not estimated per component
- [ ] Median under 40 ms for the software path
- [ ] Jitter characterised as a distribution, not just a median
- [ ] `docs/latency.md` written — what is measured, what is not, how to retake it
- [ ] `DECISIONS.md`: the target, and what to do if it is missed
