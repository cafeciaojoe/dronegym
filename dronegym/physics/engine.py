"""The only module in dronegym that imports mujoco.

Everything else talks to the simulation through Engine.
"""

from dataclasses import dataclass

import mujoco


@dataclass(frozen=True)
class Pose:
    """Where a body was, at the moment it was read.

    A snapshot, not a live view — see Engine.pose().
    """

    position: tuple[float, float, float]
    orientation: tuple[float, float, float, float]  # quaternion, w x y z


class Engine:
    """One loaded MuJoCo model and its live state."""

    def __init__(self, xml_path: str) -> None:
        self._model = mujoco.MjModel.from_xml_path(xml_path)  # structure: fixed once loaded
        self._data = mujoco.MjData(self._model)  # state: changes every step
        self._body_ids: dict[str, int] = {}  # name -> index, so lookups aren't per-frame
        # World positions are derived from joint coordinates and aren't computed until
        # something asks. Without this, pose() reads zeros until the first step().
        mujoco.mj_forward(self._model, self._data)

    def step(self) -> None:
        """Advance the simulation by one timestep."""
        mujoco.mj_step(self._model, self._data)

    def pose(self, body: str) -> Pose:
        """Position and orientation of a body, in world coordinates."""
        i = self._body_id(body)
        # xpos/xquat are live views into MuJoCo's memory — copy the numbers out,
        # or they change under the caller on the next step.
        return Pose(
            position=tuple(float(v) for v in self._data.xpos[i]),
            orientation=tuple(float(v) for v in self._data.xquat[i]),
        )

    def _body_id(self, name: str) -> int:
        """Look up a body's index, cached. Raises if the name isn't in the model."""
        if name not in self._body_ids:
            i = mujoco.mj_name2id(self._model, mujoco.mjtObj.mjOBJ_BODY, name)
            # -1 means not found. Without this check, xpos[-1] would quietly
            # return the *last* body instead of raising.
            if i == -1:
                raise KeyError(f"no body named {name!r} in this model")
            self._body_ids[name] = i
        return self._body_ids[name]

    @property
    def time(self) -> float:
        """Simulation time in seconds since the model was loaded."""
        return self._data.time
