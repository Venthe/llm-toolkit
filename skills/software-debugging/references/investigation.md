# Hypotheses and experiments

## Establish a baseline

Record a concrete expected result and the actual failure. Capture the revision,
environment, input, and frequency. Minimize the reproduction while keeping the
failure; label a reduced case that only resembles it as a hypothesis aid.

For intermittent failures, record both failing and passing conditions and bound
repetition. Investigate timing, shared state, load, dependency failures, and
test ordering where evidence points there. A successful retry does not explain
the failure. Do not overwrite the useful failing sample with a later success.

## Narrow the explanation

Keep a small set of plausible hypotheses. For each, identify evidence that would
support or contradict it and select the next discriminating observation. Change
one relevant variable where practical. Avoid edits that merely hide the symptom
before understanding the violated contract.

Example: a request times out. Possible causes include a blocked dependency,
connection-pool exhaustion, or a deadline already expired before dispatch. A
correlated trace plus pool/deadline state can distinguish these; increasing
every timeout cannot establish which cause occurred.

Follow the failing data through boundaries and compare actual state with the
contract. Use stack traces and debugger observations to identify the first point
where behavior diverges. The last exception may be a downstream consequence.

Use history or bisection when a regression interval and reliable reproducer
exist. Preserve the worktree, use isolated checkouts when needed, and account
for changing dependencies. Do not call a candidate commit causal merely because
it is recent.

## Fix and verify

When authorized, implement the correction supported by the evidence. Verify the
original failing case, related boundaries, and meaningful regression coverage.
If practical, confirm a regression check fails on the original defect for the
right reason and passes with the correction.

If reproduction or decisive evidence is unavailable, provide the strongest
supported hypothesis, confidence, and the next concrete probe. Do not claim a
root cause from correlation alone. Clearly label any mitigation and remaining
risk; lack of proof is not a reason to make speculative production changes.
