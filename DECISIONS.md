# Decisions

What we chose, what we rejected, and why.

Every stitch that makes a choice adds an entry here before it can be tied. This doubles as the
learning record — writing down *why* something is shaped the way it is is the part that's worth
having in three months, and it's more useful than a quiz because you have to be able to act on it.

Newest last. Keep entries short.

---

## Format

```markdown
## NNN — <short title>
**Date:** YYYY-MM-DD · **Stitch:** <stitch-id>

**Chose:** <what we did>
**Rejected:** <the alternative, named>
**Why:** <the reasoning — the part worth remembering>
**Would revisit if:** <what would change the answer>
```

---

## 001 — Work is decomposed on a loom
**Date:** 2026-08-11 · **Stitch:** — (project setup)

**Chose:** [zealtv/loom](https://github.com/zealtv/loom) v2.1.0, with `PLAN.md` as a readable mirror
of the same tree.

**Rejected:** A flat task list, and issue tracking.

**Why:** The work is genuinely a tree with real dependencies, and the shape matters — sibling stitches
being parallel and parents waiting for children is exactly how the stages actually behave. Directory
state means it's greppable and diffable, and the plan and the work can't drift apart because they're
the same structure.

**Would revisit if:** The tree stops changing shape, at which point a list would do.

---

## 002 — Every stage ends with a run-book, not just a working system
**Date:** 2026-08-11 · **Stitch:** `stage-<n>-runbook` ×5

**Chose:** Each stage's final stitch produces a one-page run-book, a safety briefing, and a test
where someone who is not Joseph runs the stage unaided. Anchored to need the substantive branches.

**Rejected:** Doing all facilitation preparation in the final week before the workshop.

**Why:** Whatever stage is finished when the workshop arrives is the one that runs. That only works
if every stage is actually shippable, and a stage nobody else has ever operated is not. It also means
the facilitation gets tested five times instead of once.

**Would revisit if:** The workshop configuration gets fixed in advance, which would make one final
run-book sufficient.

---

## 003 — One package, no extras
**Date:** 2026-08-11 · **Stitch:** `0.1.1 repo-and-env`

**Chose:** A single package containing sim, creature, radio and safety code.

**Rejected:** Splitting a hardware-free core from the room runtime, or using optional dependency
extras.

**Why:** Running the sim without drones never instantiates the radio backend, so at runtime there is
nothing to separate. The install-time argument — that someone without cflib shouldn't have to install
it — doesn't apply, because everyone working on this has cflib and flies drones.

**Would revisit if:** Someone needs to run the sim on a machine that can't install cflib. The one
rule that keeps that option cheap: import cflib *inside* the radio backend, never at module top
level, so `import dronegym` never needs the radio stack.

---

## 004 — Stages 3 and 4 are not planned yet
**Date:** 2026-08-11 · **Stitch:** — (planning scope)

**Chose:** Decompose to the end of Stage 2 only. Stages 3 and 4 get a paragraph each in `PLAN.md`.

**Rejected:** Planning the evolution and recorded-human work now.

**Why:** The shape of the creature work isn't knowable until Stage 2 exists and has been played with.
Planning it now would produce detail that reads like knowledge and isn't.

**Would revisit if:** Stage 2 ties. That's the trigger — `2.5 stage-2-runbook` ends by writing down
what Stage 2 taught, *before* Stage 3 gets planned.
