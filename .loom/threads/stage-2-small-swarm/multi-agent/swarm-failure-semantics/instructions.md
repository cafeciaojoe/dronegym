# swarm-failure-semantics

cflib v2 ships no swarm wrapper, so swarm-level failure behaviour is yours to write either way.
Decide it explicitly rather than discovering it.

Recommendation: any drone entering LOST puts the WHOLE creature into hold, because a creature missing
a limb is a different creature.

## Done when
- [ ] Policy written down before it is implemented
- [ ] Tested by inducing a single-drone failure mid-session
- [ ] Operator can see which drone failed and why
- [ ] `docs/swarm-failure.md` written
- [ ] `DECISIONS.md`: whole-creature hold vs continue, and why
