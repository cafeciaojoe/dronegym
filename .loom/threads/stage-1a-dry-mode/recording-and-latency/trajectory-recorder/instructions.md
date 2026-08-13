# trajectory-recorder

Record hand movement to a file and play it back. Stage 4 is built entirely on this, so pin the schema
now and version it from the first write.

## Done when
- [ ] Versioned format: fields, frame, units, handedness, rate, session metadata
- [ ] Round-trip test: record, replay, compare within tolerance
- [ ] Playback drives the same hand interface a live handheld does (1a.2.1)
- [ ] `docs/recording-format.md` written — the schema, with the version field explained
- [ ] `DECISIONS.md`: the schema, and what a version bump is allowed to change
