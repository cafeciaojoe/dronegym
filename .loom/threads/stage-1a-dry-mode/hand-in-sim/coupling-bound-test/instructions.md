# coupling-bound-test

Two failure modes, two tests.

Swing the handheld as hard as you physically can — the floating sphere must never leave above 1 m/s.
That catches the punchy failure.

The slow one needs its own test. A force cap is not an energy cap: energy is force x distance, so
pushing gently for long enough still ends up fast. Drag on the floating sphere is what bounds it.

## Done when
- [ ] Swing test passes repeatedly, including through a deliberate tracking dropout
- [ ] Sustained-push test: the sphere reaches a terminal speed rather than accumulating
- [ ] Both run as automated tests, not just by hand
- [ ] `docs/coupling.md` written or updated — what it does, how to run it
- [ ] `DECISIONS.md` entry if a choice was made — what we picked, what we rejected, why
