# repo-and-env

A working Python environment with MuJoCo running in it. That's all this stitch is.

Everything about *packaging* — making `dronegym` an installable package, pinning the environment to
a file — is deferred to `packaging-and-env` at the end of Stage 2. There is nothing to package yet,
and guessing at the dependency list before the code exists produces a file that describes a guess.
Install what you need, write down what you installed, move on.

## Done when
- [ ] conda env `dronegym` (py3.12) created, with what you need installed (pip install mujoco cflib cfclient)
- [ ] MuJoCo hello-world runs and renders
- [ ] `.gitignore` covers logs, recordings, `__pycache__`, MuJoCo caches
- [ ] `docs/setup.md` written or updated — what it does, how to run it
- [ ] `DECISIONS.md` entry if a choice was made — what we picked, what we rejected, why
