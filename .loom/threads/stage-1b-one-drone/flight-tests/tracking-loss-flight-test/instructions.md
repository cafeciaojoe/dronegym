# tracking-loss-flight-test

Cause a tracking loss deliberately, in the air, and confirm the drone descends instead of flying off.
You will lose tracking eventually — someone walks in front of a base station, a cable gets kicked —
so cause it on purpose while nothing valuable is in the room.

Occlude or cover the DECK rather than cutting power to one base station. With two base stations a
Crazyflie can often keep estimating from one, so a single-base-station kill may pass without ever
entering the state you are trying to test.

Low altitude, nothing valuable nearby, no human near the drone.

## Done when
- [ ] Deck occluded mid-flight; drone goes DEGRADED -> LOST -> controlled descent
- [ ] Three consecutive passes — intermittent failures are the ones that bite
- [ ] Recovery tested too: restore tracking, confirm it resumes sanely
- [ ] `docs/runbook-stage-1b.md` written or updated — what it does, how to run it
- [ ] `DECISIONS.md` entry if a choice was made — what we picked, what we rejected, why
