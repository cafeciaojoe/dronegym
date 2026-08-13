# Decisions

What we chose, what we rejected, why. Newest last.

> **KEEP IT SHORT.** Four lines per entry. One sentence each, and only the sentence that will still
> matter in three months. If it needs a paragraph it belongs in `docs/`, not here. This is a log, not
> a memo — a wall of prose is a log nobody rereads.

Corrections go in place as a dated line, never a silent edit. The point is to show what we believed
and when.

```markdown
## NNN — <title>
**YYYY-MM-DD** · `<stitch-id>`
**Chose:** …  **Rejected:** …
**Why:** …
**Revisit if:** …
```

---

## 001 — Work is decomposed on a loom
**2026-08-11** · project setup
**Chose:** [zealtv/loom](https://github.com/zealtv/loom) v2.1.0, `PLAN.md` mirrors the same tree.
**Rejected:** flat task list, issue tracker.
**Why:** the work is a tree with real dependencies, and directory state is greppable, diffable, and
can't drift from the plan.
**Revisit if:** the tree stops changing shape.

---

## 002 — Every stage ends with a run-book
**2026-08-11** · `stage-<n>-runbook` ×5
**Chose:** each stage ends with a one-page run-book and someone who isn't Joseph running it unaided.
**Rejected:** all facilitation prep in the final week.
**Why:** whatever stage is finished when the workshop arrives is the one that runs, so every stage
has to be shippable — and a stage nobody else has operated isn't.
**Revisit if:** the workshop configuration gets fixed in advance.

---

## 003 — One package, no extras
**2026-08-11** · `0.1.1 repo-and-env`
**Chose:** single package — sim, creature, radio, safety.
**Rejected:** splitting a hardware-free core, or optional dependency extras.
**Why:** everyone working on this has cflib and flies drones, so there's nobody to separate it for.
**Revisit if:** someone needs to run the sim on a machine that can't install cflib.

**Correction 2026-08-11:** this originally claimed `import cflib` needs a radio attached. Wrong — it's
inert until `cflib.crtp.init_drivers()`. The real rule is just: don't call `init_drivers()` at import
time. The `python -c "import dronegym"` check it justified has been dropped.

---

## 004 — Stages 3 and 4 not planned yet
**2026-08-11** · planning scope
**Chose:** decompose to end of Stage 2 only.
**Rejected:** planning the evolution and recorded-human work now.
**Why:** planning it now produces detail that reads like knowledge and isn't.
**Revisit if:** Stage 2 ties — `2.6 stage-2-runbook` writes up what it taught, before Stage 3 gets
planned.

---

## 005 — Packaging deferred to end of Stage 2
**2026-08-11** · `0.1.1 repo-and-env` → `2.5 packaging-and-env`
**Chose:** Stage 0 gets a working env, nothing more. `pyproject.toml` and `environment.yml` move to
`2.5`. `docs/setup.md` is the source of truth until then.
**Rejected:** writing `environment.yml` alongside creating the env.
**Why:** with no code there's no real dependency list, so it would describe a guess — and a file
that's always stale gets ignored.
**Revisit if:** someone else needs to build the env before Stage 2 ends.

---

## 006 — Declare what the code imports, not what it needs
**2026-08-11** · `0.1.1 repo-and-env`
**Chose:** `pip install mujoco cflib cfclient`. numpy not listed.
**Rejected:** listing numpy "because we'll need it".
**Why:** nothing imports it yet; it arrives via mujoco and cfclient anyway. Declare it the day our
own code imports it — transitive dependencies vanish without warning.
**Revisit if:** we write `import numpy`.

---

## 007 — Findings: no brew libusb, no mjpython
**2026-08-11** · `0.1.1 repo-and-env`
Not decisions — recorded so they aren't rediscovered.
**libusb:** not needed. cflib pulls `libusb-package`, which bundles it. Verified on this machine.
**mjpython:** not needed. `python -m mujoco.viewer` owns its own event loop. `mjpython` is only for
scripts calling `viewer.launch_passive()`.
