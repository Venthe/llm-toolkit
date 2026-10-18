# Extreme Programming practices

Use the sections relevant to the change and available evidence, during both
implementation and review.

## Applying the practices

Implement in small verifiable steps. When practical for a behavior change, write
a focused failing example, make it pass, then simplify while preserving behavior.
Follow the project's test workflow and user constraints; do not claim a historical
test-first sequence from the final diff. See [software testing](../../software-testing/SKILL.md) for test design.

Keep behavior changes and refactoring distinguishable in the work and explanation.
Use existing fast checks frequently enough to catch mistakes near their cause.
Integration guidance does not authorize committing or pushing without a request.

### Self-testing code

Check whether behavior introduced or modified by the change is protected by automated tests appropriate to the level at which the behavior is exposed. Tests should fail for meaningful regressions and be understandable enough to act as executable examples.

A lack of a test is not automatically a defect when the change is inherently difficult or inappropriate to test at that level. Record the gap and its practical risk.

### Simple design

Use the XP simple-design heuristics:

- the tests pass;
- duplicated logic is avoided, including hidden duplication such as parallel class hierarchies;
- important intent is stated in the code; and
- there are no unnecessary classes or methods.

Treat these as interacting heuristics. A decomposition that reduces duplication but makes intent substantially harder to understand may not be an improvement.

### Refactoring

Separate behavior changes from structural cleanup where the diff permits it. Look for opportunities where small behavior-preserving transformations would reduce complexity or duplication without requiring speculative redesign.

Do not demand refactoring merely because code is imperfect. Focus on changed code and local structures that directly affect the change.

### Continuous integration and feedback

Check whether the change can be integrated and verified by the project's existing build/test/lint tooling. Identify missing automated verification, brittle tests, build coupling, and changes that make feedback significantly slower or less deterministic.

### Small, integrable changes

When reviewing a commit, note whether the change is self-contained or mixes unrelated behavior, structural rewrites, formatting churn, migrations, or generated files in a way that obscures verification.

This is a review observation, not a demand to split the commit.

### Collective ownership / code readability

The change should be understandable and maintainable by another developer. Flag assumptions encoded only in local knowledge, opaque conventions, or hidden dependencies when they materially increase the cost of modification.

## Source influences

Consult when interpreting a practice in the review.

- [Martin Fowler: Beck Design Rules](https://martinfowler.com/bliki/BeckDesignRules.html)
- [Martin Fowler: The New Methodology](https://martinfowler.com/articles/newMethodologyOriginal.html)
- [Martin Fowler: Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html)
- [Martin Fowler: Self-Testing Code](https://martinfowler.com/bliki/SelfTestingCode.html)

Repository artifacts can show how verification is configured. They do not by
themselves establish how often a team integrates, whether it pairs, or the order
in which tests and implementation were written.
