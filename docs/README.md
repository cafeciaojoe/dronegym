# docs

One page per component, written as the stitch that builds it gets tied. A stitch is not done until
its page exists.

Audience: you in three months, and the support staff who have to operate whatever stage the workshop
lands on.

Most of the list below doesn't exist yet. The Stitch column says who owes it — that's the point of
this page, since `ls` can show you what's here but not what's missing. Once most of these exist, this
page has stopped earning its keep and should be deleted.

## Setup and operations

| Page | What it covers | Stitch |
|---|---|---|
| `setup.md` | Recreating the environment from scratch | 0.1.1 |
| `dg-doctor.md` | Each check, what it means, what to do when it fails | 0.2.1 |
| `preflight.md` | The gate before anything arms motors | 0.2.2 |

## Measurements

| Page | What it covers | Stitch |
|---|---|---|
| `radio-budget.md` | Packets/sec/drone, the measured ceiling, how to retake it | 0.3.1, 2.4.1 |
| `control-lag.md` | Step response and `control_lag(speed)` — sets the Δ-cap, leash and collision radius | 0.3.2 |
| `latency.md` | Loop latency and jitter; what is measured and what isn't | 1a.4.2 |

## Simulation

| Page | What it covers | Stitch |
|---|---|---|
| `engine.md` | The MuJoCo surface and why it's shaped that way | 0.4.1 |
| `frames.md` | The one world frame, and what converts where | 0.4.2 |
| `cage-model.md` | The cage in the sim, and regenerating it after a reprint | 0.2.3 |
| `coupling.md` | Clamped-PD virtual coupling, the constants, how to retune | 1a.2.2, 1a.2.4 |
| `scenes.md` | The block pusher scene and its tunable parameters | 1a.3 |
| `backfeed.md` | The drone pushing back on its own sim node, and the ringing margin | 1c.1.1, 1c.1.2 |

## Links and formats

| Page | What it covers | Stitch |
|---|---|---|
| `hand-link.md` | The hand-pose interface and how to add a backend | 1a.2.1, 2.1.2 |
| `drone-link.md` | The setpoint interface and how to add a backend | 1b.1.1, 2.1.1, 2.4.2 |
| `setpoints.md` | Continuous position-setpoint streaming | 1b.1.2 |
| `recording-format.md` | The trajectory schema, versioned — Stage 4 depends on this | 1a.4.1 |
| `creature-format.md` | A creature in a file, versioned | 2.3.1 |
| `creature-sensing.md` | What the creature can perceive, and what each option feels like | 2.3.2 |
| `creatures.md` | The hand-authored creature | 2.3.3 |

## Safety

| Page | What it covers | Stitch |
|---|---|---|
| `tracking-health.md` | The three lighthouse flags, measured lag, thresholds | 1a.1.1–1a.1.4 |
| `safety-layer.md` | Δ-cap, leash, workspace clamp, controlled descent | 1b.2.1–1b.2.4 |
| `separation.md` | Both separation mechanisms, and why one isn't enough | 2.2.1–2.2.3 |
| `swarm-failure.md` | What happens when one drone of N fails | 2.1.3 |
| `operator-view.md` | What the operator panel shows and how to read it | 1a.2.3 |

## Run-books

One per stage. Each is the thing that makes its stage shippable — a one-page bring-up, a safety
briefing, and enough that someone else can run it unaided.

| Page | Stitch |
|---|---|
| `runbook-stage-0.md` | 0.5 |
| `runbook-stage-1a.md` | 1a.5 |
| `runbook-stage-1b.md` | 1b.3.1, 1b.3.2, 1b.4 |
| `runbook-stage-1c.md` | 1c.2, 1c.4 |
| `runbook-stage-2.md` | 2.5 |

## Design record

| Page | What it covers | Stitch |
|---|---|---|
| `soma-1c.md` | First-person account of the closed loop — does it feel like pushing something? | 1c.3 |
