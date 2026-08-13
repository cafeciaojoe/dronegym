# downwash-capsules

Each drone's proxy is a vertically-elongated capsule biased downward, approximating the downwash cone
— rather than a sphere plus a separate no-flying-above rule.

The constraint then lives in the creature's morphology instead of in a special case. More robust, and
squarely in the spirit of the Pfeifer material.

## Done when
- [ ] Capsule dimensions derived from cage radius + control_lag(speed) (0.3.2), not guessed
- [ ] Radius grows with commanded speed — the envelope expands as people move faster
- [ ] Contact is soft: resolution impulses never produce a setpoint step the drone cannot track
- [ ] `docs/separation.md` written
- [ ] `DECISIONS.md`: capsule vs sphere-plus-rule
