# hand-authored-creature

One creature, written by hand, that several drones embody and a person can interact with.

A hovering swarm can realise exactly one thing: the positions of N points in 3D, under minimum
separation and maximum speed and acceleration. Build the creature out of that — and put the limits
into the creature's own actuator model rather than into a checker after the fact. Then anything you
author, or later evolve, is flyable by construction. That is also the Pfeifer move: the constraint
lives in the morphology instead of in a special case.

## Done when
- [ ] Node speed and acceleration capped in the creature's actuator model, not post-hoc
- [ ] Loads from a creature file (2.3.1)
- [ ] Flies with N drones and reads as one creature rather than N drones — assessed first-person
- [ ] `docs/creatures.md` written
- [ ] `DECISIONS.md`: limits-in-the-body vs a validator, and why
