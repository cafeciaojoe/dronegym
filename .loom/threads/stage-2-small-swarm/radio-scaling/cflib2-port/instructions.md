# cflib2-port

CONDITIONAL. Do not start this unless 2.4.1 says v1 cannot carry the workshop drone count.

The DroneLink interface (1b.1.1) exists to make this port cheap *later*. That is an argument for
deferring it, not for scheduling it: v2 is an explicitly unstable preview, and a library swap late in
Stage 2 with a workshop date approaching is how you end up half-ported on the day.

If 2.4.1 says v1 is fine: drop this stitch with a reason.

## Done when
- [ ] 2.4.1 says the port is necessary — otherwise DROP this stitch
- [ ] Backend swapped behind DroneLink; nothing upstream changes
- [ ] v1 backend still works as a fallback you can reach in the room
- [ ] `docs/drone-link.md` updated
- [ ] `DECISIONS.md`: what forced the port
