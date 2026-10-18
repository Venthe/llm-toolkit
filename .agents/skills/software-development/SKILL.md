---
name: software-development
description: Implement, refactor, or review software using pragmatic architecture, clean code, OOP, and XP practices. Use for code changes or reviews of a worktree, commit, or specified component across languages.
---

# Software development and review

## Establish the task

Read applicable project instructions, nearby code, build configuration, tests,
and relevant decisions. Identify the intended behavior and existing contracts.

Choose the mode from the request:

- **Implementation:** make the requested feature, fix, or refactor and verify it.
- **Review:** inspect code and existing evidence, then report; do not edit files
  or execute builds/tests. Use this mode for a review without execution.
- **Review with verification:** inspect and run relevant existing tests, builds,
  linters, or analysis in check mode. Temporary files, caches, and generated build
  output are allowed in known local output locations. Preserve source,
  configuration, lockfiles, snapshots, and user data; do not apply fixes or update
  baselines. Use an isolated workspace if the check cannot preserve those inputs.
- **Review and fix:** inspect first, then apply fixes within the requested scope.
  Do not interpret a general review request as permission to implement findings.

Select review with verification when the user requests executable verification or
applicable project instructions require it; no repeated approval is needed within
that scope. Otherwise use inspection-only review. Respect explicit no-execution
constraints. Neither review mode permits shared-service mutations, destructive
fixtures, or deployments merely because they are part of a test command.

For Git work, follow [version-control](../version-control/SKILL.md). For a worktree or
commit review, read [target selection](../version-control/references/review-targets.md)
to include relevant untracked files and handle root commits, merges, and missing
ancestry. Inspect surrounding code from the reviewed revision. Reuse the established
mode and scope when consulting companion skills; a link does not turn review into
implementation, authorize execution, or require loading every linked skill.

## Load relevant guidance

Use these references for both writing and reviewing code. Read only those relevant
to the behavior and boundaries at hand.

| Topic | When to read |
| --- | --- |
| [Architecture](references/architecture.md) | Changes cross components, policy/infrastructure boundaries, or external interfaces |
| [Cloud-native architecture](../cloud-native-architecture/SKILL.md) | Recommending deployment architecture, Twelve-Factor practices, or Kubernetes workload improvements |
| [Clean code](references/clean-code.md) | Assessing clarity, complexity, cohesion, errors, side effects, or duplicated knowledge |
| [OOP](references/oop.md) | Designing or reviewing objects, invariants, inheritance, interfaces, or domain types |
| [XP](references/xp.md) | Assessing evolutionary design, refactoring scope, integrability, or feedback |
| [Software testing](../software-testing/SKILL.md) | Selecting verification, adding regression protection, or assessing test quality |
| [Software debugging](../software-debugging/SKILL.md) | Reproducing failures and establishing root cause before selecting a fix |
| [Java](references/java.md) | Implementing or reviewing Java code |
| [Review procedure and reporting](references/reviewing.md) | Producing findings for a review request |

For other languages, use project conventions and add a language reference only
when reusable, demonstrated guidance warrants one. A comprehensive review should
consider each applicable topic; a small change need not invent architectural work.

## Implementation workflow

1. Understand the desired behavior, affected dependencies, and regression risks.
2. Make the smallest coherent change that fully solves the problem. Preserve
   contracts unless changing them is part of the request.
3. Prefer existing conventions and dependencies. Keep state, side effects, and
   failure behavior explicit; avoid speculative abstractions or unrelated cleanup.
4. Add or update meaningful tests where justified and permitted. Run the narrow
   relevant checks and required project checks, expanding only when evidence
   calls for it. Use configured formatters and linters for mechanical style.
5. Review the final diff and report changed behavior, verification, and limitations.

## Review workflow

1. State scope and baseline; separate introduced behavior from existing concerns.
2. Inspect changed code and trace callers, boundaries, and invariants as needed.
3. Assess correctness first, then maintainability and feedback consequences using
   the applicable references. Heuristic or pattern differences alone are not bugs.
4. In review with verification, run relevant safe checks within the selected
   scope; in inspection-only review, report checks as not run. Identify which
   revision was executed; a test failure in another state does not prove a
   regression in this change.
5. Merge duplicate findings and order by practical impact. Give locations,
   triggering conditions, consequences, and confidence. Distinguish demonstrated
   defects, potential concerns, and observations.
6. Offer bounded future directions where useful; do not choose an architecture
   on the user's behalf. State when no actionable findings were found.

Honor constraints on testing and execution. Report what actually ran and what
remains unverified; do not turn missing infrastructure into a code defect.
