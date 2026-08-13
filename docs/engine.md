# engine

`dronegym/physics/engine.py` — the only module that imports mujoco. Everything else talks to the
simulation through `Engine`, so swapping or upgrading the physics engine touches one file.

Stitch `0.4.1 engine-module`. Incomplete — external forces are still to come.

---

## Using it

```python
from dronegym.physics.engine import Engine

e = Engine("assets/hello.xml")
e.pose("ball").position     # (0.0, 0.0, 1.0)
e.step()
e.time                      # 0.002
```

The XML path is an argument, so the caller chooses which world to load. `Engine` knows nothing about
Crazyflies, hands, or coupling — that lives in the layers above it.

---

## Things that will bite you

**Model vs data.** `_model` is structure — bodies, masses, and the physics options including
`timestep`. Fixed once loaded. `_data` is state — positions, velocities, contacts, `time`. Changes
every step. Anything you want to change while running goes in data; anything structural means editing
the XML and reloading, because MuJoCo compiles the model and can't grow new bodies at runtime.

**`Pose` is a snapshot, not a view.** `data.xpos[i]` is a live window into MuJoCo's memory — hold one
and the numbers change under you on the next step, silently. `pose()` copies the values out into a
frozen dataclass so callers can keep them.

**`__init__` calls `mj_forward`.** World positions are derived from joint coordinates and aren't
computed until something asks. Without that call, `pose()` returns zeros until the first `step()` —
so a body declared at `pos="0 0 1"` reads as being at the origin. `mj_forward` computes everything
implied by the current state without advancing time; `mj_step` does the same and then integrates.

**Unknown body names raise.** `mj_name2id` returns `-1` when a name isn't found, and `xpos[-1]` is
legal Python meaning *the last body*. So a typo would silently give you the wrong body's position
forever. `_body_id` checks for `-1` and raises `KeyError` instead.

**Bodies must be named in the XML** to be reachable. `<body name="ball" pos="0 0 1">`.

---

## Quaternions

`Pose.orientation` is `(w, x, y, z)` — scalar first, MuJoCo's convention. Plenty of other libraries
use scalar last. Same four numbers, different order, and nothing errors if you mix them up. See
`0.4.2 frame-conversion`.
