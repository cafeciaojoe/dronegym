# proxy-ghost-render

Shaded = the dynamic proxy, which is what actually pushes things. Ghost/wireframe = the mocap body,
the raw measurement. When tracking is clean and you are not pushing hard they coincide and the ghost
is invisible.

The gap between them IS the coupling force, so this is a free live diagnostic. Put the distance
between them on the operator panel as a single health number.

This is a developer and operator view. The person in the room is looking at a drone, not a screen.

## Done when
- [ ] Both bodies rendered and visually distinct
- [ ] Gap magnitude shown as one scalar on the operator panel
- [ ] Legible at a glance mid-session — checked with someone else driving
- [ ] `docs/operator-view.md` written or updated — what it does, how to run it
- [ ] `DECISIONS.md` entry if a choice was made — what we picked, what we rejected, why
