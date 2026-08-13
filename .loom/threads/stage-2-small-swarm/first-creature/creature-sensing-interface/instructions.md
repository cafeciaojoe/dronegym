# creature-sensing-interface

What the creature can perceive of the human, behind a swappable interface.

Left open on purpose — it could be touch only, it could be a sphere of attraction or repulsion, and it
may well be a workshop question rather than a pre-workshop decision. That is exactly why it cannot be
hardcoded: "let's try repulsion instead" should be a dropdown, not a code change with staff and users
standing around.

Touch is free — the engine already computes contacts, because that is how the separation volumes
work. It is also the most faithful option: it is what the block pusher uses, and it is closest to
HTTYD, where the drone could only sense points the person had created.

## Done when
- [ ] Interface defined; sensing swappable at runtime, not compile time
- [ ] Touch implementation working
- [ ] At least one field implementation (attraction/repulsion) as the contrast case
- [ ] `docs/creature-sensing.md` written — the options, and what each one feels like
- [ ] `DECISIONS.md`: what was tried, and what it changed about the interaction
