# repo-and-env

Python environment and package layout. One package, no extras — running the sim without drones never
touches cflib, so there is nothing to separate.

One rule worth holding: import cflib *inside* the radio backend, not at module top level, so
`import dronegym` never needs the radio stack present.

## Done when
- [ ] conda env `dronegym` (py3.12) created; `environment.yml` committed
- [ ] `python -c "import dronegym"` succeeds with no hardware attached
- [ ] MuJoCo hello-world runs and renders
- [ ] `.gitignore` covers logs, recordings, `__pycache__`, MuJoCo caches
- [ ] `docs/setup.md` written or updated — what it does, how to run it
- [ ] `DECISIONS.md` entry if a choice was made — what we picked, what we rejected, why
