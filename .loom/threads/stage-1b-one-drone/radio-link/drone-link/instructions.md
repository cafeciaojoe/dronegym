# drone-link

The interface setpoints go out through, plus a cflib v1 backend and a null backend.

The null backend is what makes dry mode possible — the room runtime with nothing flying. That is what
Stage 1a already is, and it is a genuinely good workshop tool in its own right: users can meet a
creature before anything spins up.

Stay on cflib v1 here. v2 is an explicitly unstable preview and you do not want to debug a moving
library and your first control loop at the same time.

## Done when
- [ ] Interface: set position, receive state, report link health
- [ ] cflib v1 backend behind a thin thread -> asyncio shim that holds no logic of its own
- [ ] Null backend: the full loop runs with nothing flying
- [ ] `docs/drone-link.md` written — the interface, and how to add a backend
- [ ] `DECISIONS.md`: v1 now, and what would make v2 worth the port
