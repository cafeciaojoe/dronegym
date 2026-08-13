# hand-link

The interface the sim gets hand poses through, plus the live Crazyflie backend.

Keep it an interface even though there is only one backend today. The brief raises HTC trackers as a
likely later move — they also give reliable yaw, which Lighthouse on a handheld does not — and Stage 4
needs a recorded hand to substitute for a live one. Both are the same swap.

## Done when
- [ ] Interface defined: pose + timestamp + health, nothing engine-specific
- [ ] Live Crazyflie backend delivering at a measured, logged rate
- [ ] cflib callbacks reach the loop cleanly (thread -> asyncio shim holding no logic of its own)
- [ ] `docs/hand-link.md` written — the interface, and how to add a backend
- [ ] `DECISIONS.md`: why an interface now rather than later
