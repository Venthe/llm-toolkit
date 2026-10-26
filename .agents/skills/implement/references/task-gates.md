# Task execution gates

Apply these gates to every implementation-plan step. Read the existing
[testing workflow](../../software-testing/SKILL.md),
[test design](../../software-testing/references/test-design.md),
[development workflow](../../software-development/SKILL.md), and
[review reporting](../../software-development/references/reviewing.md) as their
conditions apply. This reference coordinates them; it does not replace them.

## Before a step

- Restate the step's observable outcome and acceptance evidence.
- Check dependencies and the current worktree diff. Keep the change bounded to
  the step; adjust the plan when evidence requires it and record why.
- Identify a focused test or verification command before implementation.

## Red, green, refactor

For a behavior change:

1. Add the smallest meaningful test for the expected behavior.
2. Run that test and observe a failure caused by the missing or incorrect
   behavior. If it fails for setup, compilation, or unrelated reasons, fix the
   test setup and establish the intended failing result.
3. Implement the smallest production change that makes the test pass.
4. Rerun the focused test and confirm it passes. Run adjacent tests that protect
   related behavior.
5. Refactor only while the relevant tests stay green; rerun them afterward.

For non-behavioral steps, such as documentation or mechanical configuration,
choose an appropriate direct check. Do not add artificial tests to claim TDD. If
no viable automated test exists, document the closest available evidence and the
gap.

## Quality gate and commit

After the step's tests pass:

- Run configured lint/static checks relevant to changed files. Use check mode;
  do not auto-fix unrelated files.
- Review the diff against the step's acceptance outcome and inspect whitespace,
  generated files, secrets, and scope.
- Apply the existing development review workflow at a level proportionate to the
  change. A review can be a self-review when no independent reviewer tool is
  available; state that limitation rather than claiming independent review.
- Resolve findings and rerun the checks affected by those changes.
- Stage explicit paths or hunks for this coherent step, inspect the staged diff,
  and commit when the task request and repository policy permit. Use the commit
  message skill. Do not include unrelated or pre-existing work.

Proceed to the next step only after its gate is satisfied or a concrete blocker
is recorded. A later failure requires investigation and appropriate rechecking;
it does not erase prior evidence or justify skipping remaining gates.

## Final gate

Run the planned project-level test, lint, and build checks that apply. Inspect
the full branch diff against its base, including every step commit. Review the
result against the original request and plan, resolve in-scope findings, then
rerun relevant checks and commit those corrections. Report exact commands,
outcomes, baseline failures, and checks that could not run.
