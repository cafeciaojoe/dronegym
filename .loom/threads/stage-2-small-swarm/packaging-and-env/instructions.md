# packaging-and-env

Turn a folder of working code into something installable, and pin the environment it needs.

Deferred here from 0.1.1 deliberately. At the start there was no code to package and no way to know
the real dependency list, so any file written then would have described a guess. By the end of
Stage 2 both are known, and shaken out by having actually been run.

Known wrinkle so it isn't a surprise: conda's export options both disappoint. `--from-history` gives
a short portable file but silently omits pip packages, and mujoco and cflib are pip. `--no-builds`
includes them but emits hundreds of macOS-ARM-specific lines that won't resolve elsewhere. Expect to
write or repair the pip block by hand. The point of this stitch is that it gets done, not that it
gets done a particular way.

Only declare what the code actually imports. A dependency list should describe what you need, not
what happened to be installed the day you exported it.

## Done when
- [ ] `pyproject.toml` written; `pip install -e .` works
- [ ] `import dronegym` succeeds from a directory that isn't the repo
- [ ] `environment.yml` committed, listing everything actually needed
- [ ] Verified by building from the file alone into a fresh env with a different name
- [ ] Version pins only where a version actually matters — not everywhere on principle
- [ ] `docs/setup.md` rewritten to describe the file rather than a list of install commands
- [ ] `DECISIONS.md` entry if a choice was made — what we picked, what we rejected, why
