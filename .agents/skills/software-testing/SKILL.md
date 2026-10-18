---
name: software-testing
description: Plan, write, run, or review software tests and regression checks. Use for test strategy, behavior coverage, fixtures, integration verification, or test reliability; use debugging when the cause of a failure needs investigation.
---

# Software testing

Establish what behavior needs evidence and choose verification that can expose a
meaningful regression. Follow the project's toolchain and user constraints.

## Workflow

1. Identify the request: plan tests, implement them, execute checks, or review
   existing coverage. A plan or review alone does not authorize code edits.
2. Inspect the contract, changed behavior, current tests, fixtures, configuration,
   and CI commands. Identify the revision and environment to be verified.
3. Read [test design and verification](references/test-design.md) when choosing
   test levels, assertions, doubles, or execution scope. For Java tests, also read
   [Java testing](references/java.md).
4. Select representative success, boundary, and failure cases according to risk.
   Prefer tests that fail for a realistic regression and tolerate harmless
   implementation changes. Avoid arbitrary coverage or test-count targets.
5. Add or modify tests only when requested or required by an authorized change.
   Run existing checks within that scope or in review with verification. An
   inspection-only review stays inspection-only; loading this skill does not
   expand its permissions.
   Start with focused checks, then required project checks; expand when unresolved
   risk or failures justify it. Understand fixture writes and cleanup first.
6. Investigate unexpected failures with [software-debugging](../software-debugging/SKILL.md)
   when causality is unclear. Do not weaken assertions or retry until green.
7. Report executed commands, results, tested state, and residual gaps. Distinguish
   planned tests, tests inspected, and tests actually executed.

## Boundaries

Use [software-development](../software-development/SKILL.md) for production-code
changes. A failing test can reveal either an implementation defect or a faulty
test; establish the contract before changing either. Keep review-only checks
from rewriting source files. Do not run destructive fixtures or load tests against
shared services without the necessary scope and authorization.

If a dependency or environment is unavailable, report the blocked check and
available evidence. Do not substitute a mocked result for a real integration
claim. For a plan, provide cases and expected outcomes; for review, prioritize
concrete coverage or reliability concerns with locations.
