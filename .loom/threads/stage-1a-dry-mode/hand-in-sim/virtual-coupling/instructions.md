# virtual-coupling

The hand is a dynamic body pulled toward the measured pose by a clamped PD force — never teleported.

A teleported body has no momentum, so it transfers no impulse and cannot push. And when it teleports
*into* something, the solver has to resolve a huge penetration in one step — which is the "explosive
contact". Same bug, both symptoms.

    F = kp * (x_measured - x_proxy) - kd * v_proxy
    F = clamp_norm(F, F_MAX)
    data.xfrc_applied[proxy_id, :3] = F

The clamp is what turns a tracking dropout from a punch into a glide: F_MAX caps the acceleration
regardless of how large the position error gets.

A mocap body carries the raw measured pose; the dynamic proxy does the physics. Not `equality/weld` —
it has solref/solimp/torquescale but no force cap, so the bound becomes implicit and unassertable.

## Done when
- [ ] `assert norm(F) <= F_MAX` holds under unit test
- [ ] A simulated 2 m dropout produces a bounded glide, not a teleport
- [ ] kp, kd and F_MAX written down with the reasoning, not left as magic numbers
- [ ] `docs/coupling.md` written — the model, the constants, how to retune
- [ ] `DECISIONS.md`: clamped PD vs weld, and why F_MAX bounds force and not energy
