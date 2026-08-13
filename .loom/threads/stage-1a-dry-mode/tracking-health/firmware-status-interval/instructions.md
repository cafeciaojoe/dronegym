# firmware-status-interval

There is no per-base-station timeout in firmware. The active-map bitmap accumulates received sweeps
and is swapped and cleared each system-status update cycle, so that interval is the detection latency
floor — and shortening it is a one-constant change in the handheld build.

Handheld and flier want opposite tuning. For a handheld, freezing is cheap and instantly recoverable,
so it should fail fast. For a flier, a false LOST costs a landing mid-session, so it should be patient
and ride out brief occlusions.

Find the constant in your own checkout and measure it. Do not trust a figure quoted from memory.

## Done when
- [ ] Constant located in your firmware checkout; current value recorded
- [ ] Shortened in the handheld build only; the flier build left patient
- [ ] Flicker threshold found empirically — the interval below which bsActive drops spuriously
- [ ] `docs/tracking-health.md` updated with both values and why they differ
- [ ] `DECISIONS.md`: the handheld/flier split
