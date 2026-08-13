# bandwidth-probe

How many drones can one Crazyradio 2.0 carry at the setpoint rate you actually want? Bench test, no
flight. This determines the shape of Stage 2, so it happens before the architecture, not after.

The published "49 Crazyflies on one radio" figure is drones flying pre-planned trajectories — a very
different load from streaming position setpoints at 100 Hz plus a log uplink per drone.

## Done when
- [ ] Packets/sec/drone budget written down on paper first
- [ ] Measured ceiling for 100 Hz position setpoints x N with log uplink running
- [ ] The N at which latency or packet loss degrades, recorded
- [ ] `docs/radio-budget.md` written — the numbers and how to retake them
- [ ] `DECISIONS.md`: one radio or two, and whether the cflib2 port is needed at all
