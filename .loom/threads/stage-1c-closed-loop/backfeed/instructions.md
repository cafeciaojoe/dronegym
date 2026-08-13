# backfeed

The real drone's measured pose pulls its own sim node.

Battery sag, wind, tracking error and control lag leak into the sim instead of being hidden by it —
the machine's resistance becomes part of the relationship rather than an error to filter out.
Pragmatically it is also what stops sim and room silently diverging.

Only the drone gets this. The human is the authority on where their hand is; there is no controller
trying and failing to reach a target.
