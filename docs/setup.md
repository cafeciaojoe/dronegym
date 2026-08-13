# Setup

Getting a working environment from a fresh machine. macOS (Apple Silicon).

Pinning this to an `environment.yml` is deliberately deferred — see `2.5 packaging-and-env`. Until
then this page is the source of truth for what to install.

---

## 1. Environment

```bash
conda create --name dronegym python=3.12 -y
```

```bash
conda activate dronegym
```

```bash
pip install mujoco cflib cfclient
```

What each one is for:

| Package | Why |
|---|---|
| `mujoco` | The physics engine. DeepMind's official wheel — pip, not conda. |
| `cflib` | Talking to Crazyflies. Bitcraze's library. |
| `cfclient` | The Crazyflie GUI. Needed for lighthouse geometry estimation and general troubleshooting, and it pulls in the USB stack. |

`numpy` is not listed because nothing imports it directly yet. It arrives anyway as a dependency of
both `mujoco` and `cfclient`. Add it explicitly the first time our own code imports it — a dependency
list should say what we need, not what happened to be installed.

**No `brew install libusb` needed.** cflib depends on `libusb-package`, a pip wheel that bundles the
native library. Verified on this machine: `cfclient` works in an env with no brew libusb present.
If a future platform isn't covered by that wheel, brew libusb is the fallback.

---

## 2. Verify

```bash
python -c "import mujoco; print(mujoco.__version__)"
```

Prints a version, no traceback.

---

## 3. Hello world

`assets/hello.xml` is a red ball falling onto a plane — the smallest thing that proves physics and
rendering both work.

```bash
python -m mujoco.viewer --mjcf=assets/hello.xml
```

**Plain `python` is correct here.** MuJoCo also ships `mjpython` on macOS, for scripts that drive the
viewer in passive mode and need to own the main thread. The `python -m mujoco.viewer` entry point
manages its own event loop, so it doesn't need it. If you later write a script using
`viewer.launch_passive()` and macOS complains about the main thread, that's when `mjpython` applies.

In the viewer: drag to orbit, scroll to zoom, space to pause. The **Physics** section of the left
panel has gravity, density and viscosity as live sliders.

---

## 4. VS Code

Install the **Python** extension (`ms-python.python`), then `Cmd+Shift+P` →
**Python: Select Interpreter** → pick `dronegym`. The status bar bottom-right should show
`Python 3.12.x ('dronegym': conda)`, and new terminals will auto-activate the env.

If `dronegym` isn't listed, hit Refresh in the picker — VS Code caches env discovery and won't notice
an env created after it started.

---

## 5. The loom

Work tracking needs bash 4+; macOS ships 3.2.

```bash
brew install bash
```

If you see `declare: -A: invalid option`, `/opt/homebrew/bin` isn't ahead of `/bin` on `PATH`.
See [../README.md](../README.md).
