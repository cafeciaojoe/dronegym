# engine-module

All MuJoCo calls live in one module. Everything else talks to it through plain data.

## Done when
- [ ] Load a model, step it, read body poses, apply external forces — all through this module
- [ ] No `import mujoco` anywhere else in the package, enforced by a test
- [ ] Deterministic seeded replay: the same inputs produce the same trace
- [ ] `docs/engine.md` written or updated — what it does, how to run it
- [ ] `DECISIONS.md` entry if a choice was made — what we picked, what we rejected, why
