# frame-conversion

One world frame — the lighthouse frame. Everything converts to it on the way in.

Quaternion handedness and axis order are the classic silent bug: everything looks fine until
something is mirrored. Write the test that catches it before you need it.

## Done when
- [ ] Lighthouse <-> MuJoCo pose conversion, both directions
- [ ] A test that fails on a wrong-handed quaternion
- [ ] A test that fails on swapped axes
- [ ] `docs/frames.md` written or updated — what it does, how to run it
- [ ] `DECISIONS.md` entry if a choice was made — what we picked, what we rejected, why
