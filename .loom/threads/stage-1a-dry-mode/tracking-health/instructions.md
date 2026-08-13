# tracking-health

Knowing when the position estimate can be trusted, and what to do when it can't.

Three mechanisms that compose: jump rejection catches it in one sample, the bsActive timer catches
the sustained case, and the clamped coupling (1a.2.2) makes the recovery a glide instead of a punch.
