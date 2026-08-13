# Drone Gymnasium 2 — Plan

**Workshop: ~28 October 2026.** Whatever stage is finished by then is what runs. That is the point of
the staging, and it is the project's main risk control — there is no cliff, only an earlier stage.

**Numbering matches the loom.** `0.3.2` here is
`.loom/threads/stage-0-foundations/measurements/step-response-probe/`. This document is for reading;
the loom is for working. They are the same structure.

**Nothing past Stage 2 is decomposed.** It can't be planned usefully until Stage 2 exists and has
been played with.

---

## What the system is

A physics simulation sitting between a human and a swarm of Crazyflies. The swarm presents as one
creature. You interact with it in the room, put it into the simulator, change it there, and pull it
back out.

The sim is not decoration. It is the thing that makes contact avoidance possible, and it is the
safety envelope — every real body has a solid virtual volume around it, so resolving contact in the
sim *is* how minimum separation gets enforced.

---

## Rules that apply to every stage

**Every stage ends shippable.** Each one finishes with a `stage-<n>-runbook`: a one-page run-book, a
safety briefing, and someone who is not Joseph running it unaided. Since any stage might be the one
the workshop meets, "workshop-ready" is a property of every stage, not of the last week.

**Documentation is part of the work, not after it.** Every leaf stitch carries two checklist items —
a `docs/` page and a `DECISIONS.md` entry if a choice was made. `DECISIONS.md` does double duty:
writing down *why* something is shaped the way it is is also the learning record.

**Measured, never guessed.** Any quantity with a physical counterpart is measured. Two numbers are
taken in week one (0.3) because almost everything downstream references them.

---

## Stage 0 — Foundations

Nothing flies. Everything that has to exist before anything else can start.

The two measurements in 0.3 are the reason this stage is not just admin: the radio ceiling decides
the shape of Stage 2, and the control lag sets the delta cap, the leash and the collision radius. Both
are cheap, and taking them now means nothing later is a guess.

### 0.1 Project skeleton
The repo itself, and somewhere for documentation to live from day one.

#### 0.1.1 repo-and-env
Conda env, package layout, MuJoCo hello-world. One package, no extras — running the sim without
drones never touches cflib, so there is nothing to separate. One rule holds it: import cflib *inside*
the radio backend, never at module top level.

#### 0.1.2 docs-scaffold
`README.md`, `DECISIONS.md` and `docs/` created before there is anything to put in them, because
otherwise it never gets started.

### 0.2 Hardware baseline
Knowing the hardware is healthy before flying it.

#### 0.2.1 dg-doctor
One command that says what is broken before you lose an hour to it. Radio, lighthouse geometry,
batteries, firmware versions. Red/green checklist, non-zero exit on failure.

#### 0.2.2 preflight-checklist
A hard gate before anything arms motors. HTTYD flew for a month with a battery health check, bounded
flight zones and automatic low-battery landing — the code is being rewritten, but that list carries
forward as requirements rather than being rediscovered.

#### 0.2.3 cage-sim-model
Low-poly spherical cage in the sim. Because the cage is a sphere, the virtual and physical bodies are
the same shape — the sim sphere is not a metaphor. Mass and dimensions from the printed cage as
measured, not as designed.

### 0.3 Measurements — week one, before any architecture

#### 0.3.1 bandwidth-probe
How many drones one Crazyradio 2.0 carries at the setpoint rate you actually want. Bench, no flight.
The published "49 Crazyflies on one radio" figure is pre-planned trajectories — a very different load
from 100 Hz position setpoints plus a log uplink per drone.

#### 0.3.2 step-response-probe
One caged drone, step the position setpoint, measure the lag and the overshoot. The delta cap, the
leash and the collision radius all come from this. Taken on the **final** cage — the reprint removes
roughly half the mass, which changes all of it.

### 0.4 Physics core
The sim, and the one place that knows about MuJoCo. Not an abstraction layer for a hypothetical
second engine — just don't scatter engine calls.

#### 0.4.1 engine-module
Every MuJoCo call lives here, enforced by a test. Deterministic seeded replay so physics changes show
up as diffs.

#### 0.4.2 frame-conversion
One world frame — the lighthouse frame. Quaternion handedness and axis order are the classic silent
bug: everything looks fine until something is mirrored. The test comes before it's needed.

### 0.5 stage-0-runbook
Someone who is not Joseph brings the system up from cold, from the page alone.

---

## Stage 1a — Dry mode

The sim reads your hand. Nothing flies. All of the interaction design, none of the flight risk.

This is also the block pusher restaged with a human as one of the agents: your hand is one sphere, a
floating sphere is the other, you push it around. A creature you can hand-author before any evolution
exists.

### 1a.1 Tracking health
When the position estimate can be trusted, and what to do when it can't. Three mechanisms that
compose: jump rejection catches it in one sample, the timer catches the sustained case, and the
clamped coupling makes the recovery a glide instead of a punch.

#### 1a.1.1 lighthouse-status-logging
`bsAvailable` (we have geometry), `bsReceive` (sweeps arriving), `bsActive` (arriving *and* usable).
Occlude a base station on purpose and measure how long detection actually takes.

#### 1a.1.2 firmware-status-interval
There is no per-base-station timeout in firmware — the active-map bitmap is swapped and cleared each
system-status cycle, so that interval is the detection latency floor. Handheld and flier want
opposite tuning: a handheld should fail fast because freezing is cheap and recoverable; a flier should
be patient because a false LOST costs a landing. Find the constant in your own checkout.

#### 1a.1.3 jump-rejection
Reject any sample implying a speed above a human arm. Single sample, on data you already have, so it
is the fastest of the three. Matters because the EKF keeps dead-reckoning through a dropout — for a
handheld that's double-integrated accelerometer noise, so the position wanders and then snaps.

#### 1a.1.4 tracking-timer
A timer on `bsActive` with two constants: TRACKING → DEGRADED (freeze) → LOST (descend). The freeze
must be visible to the operator so staff can prompt the person back into coverage.

### 1a.2 Hand in sim
Getting your hand into the physics engine in a way that can push things and cannot punch them.

#### 1a.2.1 hand-link
The interface hand poses arrive through, plus the live Crazyflie backend. An interface even with one
backend, because HTC trackers (reliable yaw, which Lighthouse on a handheld doesn't give you) and
Stage 4's recorded hand are the same swap.

#### 1a.2.2 virtual-coupling
The answer to "objects reappear and carry no inertia" and "explosive contact" — one bug, two
symptoms. A teleported body has no momentum so it can't push, and when it teleports *into* something
the solver resolves a huge penetration in one step. Fix: a dynamic body pulled toward the measured
pose by a clamped PD force. The clamp turns a tracking dropout from a punch into a glide.

#### 1a.2.3 proxy-ghost-render
Shaded = the proxy that does the pushing. Ghost = the raw measurement. The gap between them *is* the
coupling force, so it's a free live diagnostic. Developer and operator view — the person in the room
is looking at a drone, not a screen.

#### 1a.2.4 coupling-bound-test
Two failures, two tests. Swing as hard as you physically can (catches the punch). Push gently for a
long time (catches the slow one) — a force cap is not an energy cap, so drag on the floating sphere
is what bounds it.

### 1a.3 block-pusher-scene
Two spheres, zero gravity, tunable weight and air density. Worth being precise about the borrowing:
Bongard's block pushers are one organism of jointed spheres grown by a genetic regulatory network,
and they crawl using ground contact — so the locomotion doesn't transfer. What does transfer, and is
the stronger idea, is that the environment shapes the creature: touch a growing agent and a chemical
diffuses from the contact point and changes which genes fire. That is the brief's "what we put into
the simulation would include the movement of the person."

### 1a.4 Recording and latency

#### 1a.4.1 trajectory-recorder
Record hand movement and play it back. Stage 4 is built entirely on this, so the schema is pinned and
versioned from the first write. Playback drives the same interface a live handheld does.

#### 1a.4.2 latency-harness
Measured, not estimated: jerk the handheld, timestamp both ends, subtract. Jitter matters more than
latency — you adapt to a constant 40 ms, not to something bouncing between 10 and 80. Be honest that
this measures the software path only; the drone's own response time (0.3.2) dominates what you feel.

### 1a.5 stage-1a-runbook
Nothing flies here, so this one really is runnable by anyone. An hour, unaided, from the page.

---

## Stage 1b — One drone, no human

The sim drives one flying drone from a scripted input. All of the flight risk, isolated from the
interaction design — so when 1c misbehaves you already know both halves were good.

### 1b.1 Radio link

#### 1b.1.1 drone-link
The interface setpoints go out through, plus a cflib v1 backend and a null backend. The null backend
is what makes dry mode possible, and dry mode is a genuinely good workshop tool — users can meet a
creature before anything spins up. Stay on v1: v2 is an unstable preview and you don't want to debug
a moving library and your first control loop at once.

#### 1b.1.2 setpoint-streaming
Continuous position setpoints at a fixed rate, so the onboard controller never extrapolates. What
HTTYD did.

### 1b.2 Safety layer
Four limits, independent on purpose — each should hold even if the others are wrong.

#### 1b.2.1 delta-cap
Cap the change per setpoint at a fixed rate and you have a velocity limit: `v_max = Δ_max × f`. At
100 Hz with a 1 cm cap the drone can never be asked to exceed 1 m/s. One legible number — and it's
the gym's weight stack, which you raise as the relationship develops. A design feature, not only a
safety feature.

#### 1b.2.2 leash
Capping Δ caps *commanded* velocity, not actual. If the drone lags and the setpoint keeps advancing,
you get rubber-banding then a fast catch-up. So also cap how far the setpoint may run ahead of where
the drone actually is.

#### 1b.2.3 workspace-clamp
A hard boundary independent of the sim. HTTYD's bounded flight zones, rewritten.

#### 1b.2.4 controlled-descent
LOST means descend and stop. Never fly away. Low-battery landing uses the same path.

### 1b.3 Flight tests
Causing the failures on purpose, while nothing valuable is in the room.

#### 1b.3.1 scripted-trajectory-flight
Ten minutes tracking a scripted path with the whole safety layer live.

#### 1b.3.2 tracking-loss-flight-test
Occlude the **deck**, not one base station — with two base stations a Crazyflie can often keep
estimating from one, so a single-base-station kill may pass without entering the state you're testing.
Three consecutive passes, because intermittent failures are the ones that bite. Test the recovery too.

### 1b.4 stage-1b-runbook
First stage where something flies, so the safety briefing is real.

---

## Stage 1c — Closed loop

Your hand moves a sphere in the sim, the sphere moves a real drone, and the real drone pushes back on
its own simulation. The first configuration that is a workshop rather than a test.

### 1c.1 Backfeed
Battery sag, wind, tracking error and control lag leak into the sim instead of being hidden by it —
the machine's resistance becomes part of the relationship rather than an error to filter out.
Pragmatically it's also what stops sim and room silently diverging. Only the drone gets this; the
human is the authority on where their own hand is.

#### 1c.1.1 backfeed-spring
Weak **and** damped. The loop is sim node → setpoint → drone → measured pose → sim node, and ~30–40 ms
of loop delay is exactly what turns a spring into an oscillator. Ships with an off switch — the
fallback is to disable it and accept divergence.

#### 1c.1.2 backfeed-ringing-test
Step it and check it settles. Then inject artificial delay to find where ringing starts, so you know
your margin.

### 1c.2 endurance-run
Ten minutes continuous, no divergence, no intervention. Plus the covered-sensor test with a person in
the loop: they unknowingly cover the handheld's deck. Test the freeze *and* the recovery — the
recovery is the part that used to be a punch.

### 1c.3 soma-writeup
Does it feel like pushing something? First-person, within a day. This is a soma design project;
"responsiveness and stability" is not only a plot, and if the felt quality isn't written down while
it's fresh it's gone.

### 1c.4 stage-1c-runbook
First configuration that could genuinely run a workshop. Facilitation notes, not just a run-book.

---

## Stage 2 — Small swarm

Several hands, several drones, presenting as one creature. **Stop here and play with it before
planning Stage 3.**

### 2.1 Multi-agent

#### 2.1.1 multi-drone-link
N drones at the rate the radio budget says is safe. Per-drone health, not one aggregate number.

#### 2.1.2 multi-hand
N hands with per-hand health. One hand losing tracking freezes only that proxy.

#### 2.1.3 swarm-failure-semantics
cflib v2 ships no swarm wrapper, so this is yours to write either way. Recommendation: any drone
entering LOST puts the *whole* creature into hold, because a creature missing a limb is a different
creature.

### 2.2 Separation
Two independent mechanisms, because the sim alone isn't enough.

#### 2.2.1 downwash-capsules
Each drone's proxy is a vertically-elongated capsule biased downward, approximating the downwash cone
— rather than a sphere plus a separate rule. The constraint lives in the morphology instead of in a
special case. Radius grows with commanded speed, so the envelope expands as people move faster.

#### 2.2.2 measured-separation-interlock
Separation enforced on **measured** positions, outside the sim. Necessary because the backfeed spring
drags a lagging drone's sim node backwards, freeing space that a neighbour then advances into — so
the backfeed erodes the margin exactly when the drones are struggling to keep up.

#### 2.2.3 two-drones-same-point-test
Command two drones to the same point. Each mechanism tested alone, then together. Three passes at the
fastest the delta cap allows.

### 2.3 First creature
One creature, authored by hand. No evolution — the point is to find out what a creature needs to be
before trying to evolve one.

#### 2.3.1 creature-file-format
Body, behaviour, sensing, provenance, versioned. The artefact the brief's headline rests on, and what
Stage 3 will extend. Roughly right now beats complete later.

#### 2.3.2 creature-sensing-interface
What the creature perceives of the human — behind a swappable interface. Left open on purpose: it
could be touch only, it could be attraction/repulsion, and it may be a workshop question. That's
exactly why it can't be hardcoded — "let's try repulsion" should be a dropdown, not a code change
with users standing around. Touch is free (the engine already computes contacts for separation) and
it's the most faithful option: what the block pusher uses, and closest to HTTYD.

#### 2.3.3 hand-authored-creature
A hovering swarm can realise exactly one thing: the positions of N points in 3D, under minimum
separation and maximum speed and acceleration. Put those limits into the creature's own actuator
model rather than a checker afterwards — then anything you author, or later evolve, is flyable by
construction.

### 2.4 Radio scaling

#### 2.4.1 bandwidth-confirm
Re-measure with real drones. 0.3.1 was a bench estimate.

#### 2.4.2 cflib2-port — **conditional**
Do not start unless 2.4.1 says v1 can't carry the workshop drone count. The DroneLink interface
exists to make this port cheap *later*, which is an argument for deferring it. A library swap late in
Stage 2 with a workshop approaching is how you end up half-ported on the day. If v1 is fine: drop
this stitch with a reason.

### 2.5 stage-2-runbook
A full multi-drone session run by someone else, unaided. Then write down what Stage 2 taught, before
planning Stage 3.

---

## Stages 3 and 4 — not decomposed

**Stage 3** — creatures that evolve. Genome, body, brain; selection; the loop where a creature goes
into the sim, changes, and comes back out.

**Stage 4** — recorded humans. Hannah and Giorgio own this: recording handheld movement, playing it
back against multiple creatures, and replaying it in different-but-similar ways so behaviour matches
the person's general way of moving rather than one specific recording. That last part is domain
randomisation; the cheap useful version is time-warp, rotation about the vertical, amplitude scale
and spatial jitter, scored on mean **and worst case** — worst case is what actually kills
recording-overfitting. Hannah's policy trainer sits on top.

Neither can be planned in useful detail until Stage 2 exists and has been played with. Two things are
worth recording now:

- **Stage 4's playback runtime and Stage 3's evolution runtime are nearly the same machine** —
  headless sim, creature loaded from a file, hand input that isn't a live drone, batch evaluation over
  variants. Stage 3 is that plus a genome encoding and a selection loop. Whichever gets built first
  should be built knowing the other is coming.
- **Human selection and fitness functions are opposites, and the project needs both.** Picbreeder and
  the lawnmower study are open-ended — people choose, with no metric. The block pusher has a scalar
  fitness function (distance the block moved). One interface with swappable implementations holds
  both, which is also how the staff decide, in conference with users, whether a session goes
  open-ended or task-directed.

One finding from the lawnmower study is already a requirement whenever the selection UI gets built:
participants couldn't track what they'd bred and resorted to screenshots pasted into Miro. Lineage
and provenance are not a nice-to-have.

---

## Working the loom

```sh
.loom/loom.sh next          # what's ready
.loom/loom.sh claim <id>    # take it
.loom/loom.sh tie <id>      # done — only when every checklist item is
.loom/loom.sh map           # the whole picture
.loom/loom.sh status        # health, blocked work, broken dependencies
```

If a stitch is trying to do too much, split it. If the outcome is no longer wanted, drop it with a
reason — `2.4.2 cflib2-port` is expected to be dropped if the numbers say so.
