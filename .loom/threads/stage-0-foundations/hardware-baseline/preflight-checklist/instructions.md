# preflight-checklist

A hard gate before anything arms motors.

HTTYD flew for a month with a battery health check, bounded flight zones and automatic low-battery
landing. The code is being rewritten, but carry that list forward as requirements rather than
rediscovering it.

## Done when
- [ ] Runnable pre-flight that blocks arming if any check fails
- [ ] Covers at minimum: battery threshold, geometry freshness, workspace bounds loaded, kill switch reachable
- [ ] Also written as a physical checklist, for whoever is running the room
- [ ] `docs/preflight.md` written or updated — what it does, how to run it
- [ ] `DECISIONS.md` entry if a choice was made — what we picked, what we rejected, why
