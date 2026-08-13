# dronegym

A physics simulation sitting between a human and a swarm of Crazyflies. The swarm presents as one
creature: you interact with it in the room, put it into the simulator, change it there, and pull it
back out.

Built for the Drone Gymnasium workshop, ~28 October 2026.

**Nothing is implemented yet.** This repo currently holds the plan and the work breakdown.

---

## Start here

- **[PLAN.md](PLAN.md)** — what the system is, and every stage in order. Read this first.
- **[DECISIONS.md](DECISIONS.md)** — what we chose, what we rejected, and why.
- **[docs/](docs/)** — how each component works and how to run it. Written as the work is done.
- **`.loom/`** — the work itself. See below.

---

## The loom

Work is decomposed on a [loom](https://github.com/zealtv/loom): a stitch is a directory with an
`instructions.md`, siblings run in parallel, and state lives in directory-name suffixes. The
filesystem is the protocol.

```sh
.loom/loom.sh next          # what's ready to work
.loom/loom.sh claim <id>    # take it
.loom/loom.sh tie <id>      # done — only when every checklist item is
.loom/loom.sh map           # the whole picture
.loom/loom.sh status        # health, blocked work, broken dependencies
```

`PLAN.md` and the loom are the same structure. `0.3.2` in the plan is
`.loom/threads/stage-0-foundations/measurements/step-response-probe/`.

### Requires bash 4+

`loom.sh` uses associative arrays. macOS ships bash 3.2, so:

```bash
brew install bash
```

Homebrew's bash lands in `/opt/homebrew/bin`, which needs to come before `/bin` on your `PATH` for
`#!/usr/bin/env bash` to find it.

---

## Setup

Not yet written — that's `0.1.1 repo-and-env`. It will land in [docs/setup.md](docs/setup.md).

The intent: one conda env (`dronegym`, py3.12), one package, no extras. Running the sim without
drones never touches cflib, so there is nothing to separate — the one rule that keeps it true is to
import cflib *inside* the radio backend, never at module top level.

---

## Working rules

**Every stage ends shippable.** Each finishes with a `stage-<n>-runbook`: a one-page run-book, a
safety briefing, and someone who is not Joseph running it unaided. Whatever stage is finished when
the workshop arrives is the one that runs, so every stage has to be ready to be that one.

**Documentation is part of the work.** Every leaf stitch carries two checklist items — a `docs/` page
and a `DECISIONS.md` entry if a choice was made. A stitch isn't tied until both are done.

**Measured, never guessed.** Any quantity with a physical counterpart gets measured. Two numbers are
taken in week one (`0.3`) because nearly everything downstream references them.

---

## Related work

- `crazyflie-firmware` — handheld build diverges from the flier build on tracking-loss timing (1a.1.2)
- HTTYD — previous system. Different hardware (brushed) and old code, so nothing is lifted directly,
  but its safety list carries forward as requirements: battery health check, bounded flight zones,
  automatic low-battery landing.
