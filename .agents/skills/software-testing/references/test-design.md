# Testing and verification

## Select useful evidence

Start with the changed behavior and plausible regression. Identify the observable
contract and choose the narrowest level that can demonstrate it accurately:

- Unit tests for deterministic rules and state transitions.
- Integration tests for persistence, serialization, framework wiring, and external
  boundaries that isolated tests cannot faithfully exercise.
- Contract tests when independently changing components rely on a shared protocol.
- End-to-end tests for important workflows across the assembled system.

Use the project's existing toolchain. These levels are options, not a checklist
requiring every kind of test for every change. Test count and line coverage alone
do not establish confidence. Avoid introducing a test library for stylistic taste.

## Design regression protection

For a bug fix, reproduce the failure when practical, then verify the corrected
behavior. Distinguish a test that fails for the relevant defect from one that
fails because its setup is broken. Cover meaningful boundaries, negative cases,
and error handling supported by the contract, rather than every implementation
branch mechanically.

Assert outputs, state transitions, or externally meaningful interactions. Avoid
tests coupled to private methods, incidental call order, internal representation,
or exact prose unless those details are contractual. Small duplicated fixtures
can be clearer than an opaque shared test framework.

Use doubles at meaningful boundaries. A mock returning the value just configured
is not evidence that integration works. Verify real adapters where integration
semantics matter. Keep time, randomness, concurrency, and external state under
control; use bounded condition-based waits instead of arbitrary sleeps.

## Execute and interpret

Run focused checks first and required project checks before completion, subject
to user constraints. Broaden after new changes, failures, or unresolved risks.
During review with verification, use check modes that preserve source,
configuration, lockfiles, and snapshots. Builds and tests may create temporary
or generated artifacts in known output locations. Understand their writes and
external effects first; use isolation if needed. Inspection-only reviews do not
execute checks. Do not use formatter fix modes or accept new snapshots as part
of verification alone.

Read exit status and failure details. Do not suppress tests, weaken assertions,
or repeatedly retry until a flaky run passes. Identify whether a failure concerns
the implementation, the test, or an unavailable dependency. If attribution to the
change matters, compare an appropriate baseline when feasible and authorized.

Report the exact checks, tested revision/state, and outcomes. Distinguish tests
inspected from tests executed. A blocked integration environment leaves a gap;
it does not turn an isolated unit test into an integration result.

## Review existing tests

Ask whether a realistic regression would fail the test and whether a harmless
refactor would unnecessarily break it. Check setup isolation, resource cleanup,
clear failures, supported error cases, and hidden dependence on ordering or global
state. Document concrete coverage gaps and their risk without demanding tests for
every low-impact mechanical edit.
