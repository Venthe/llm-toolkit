# Session regression cases

Use relevant cases when changing coding workflow skills. Define expected actions
before exercising the request. Record the input, loaded instructions, observed
actions, and limitations. A manual instruction walkthrough is not an independent
agent evaluation; structural validation does not establish behavioral compliance.

Adapt these scenarios to the target project's language, framework, and conventions.
Evaluate responsibility boundaries and observable behavior rather than requiring
a particular API shape, state mechanism, or file layout.

| Request or situation | Expected observable outcome |
| --- | --- |
| Extract reusable infrastructure from code that also owns domain state. | The caller supplies the required context through an explicit contract; the reusable unit does not acquire unrelated domain responsibilities. Preserve behavior across repeated calls and lifecycle transitions. |
| Choose a public API, then simplify its composition mechanism. | Assess consumer needs and existing contracts before selecting an API. Remove redundant indirection while preserving supported customization; do not turn the selected mechanism into a universal preference. |
| Simplify small, tightly coupled units and their control flow. | Preserve cohesive responsibilities, clarify derived state and branching, and retain abstractions that serve a demonstrated purpose. Follow project conventions rather than imposing a particular file layout or state mechanism. |
| Make a small follow-up fix after implementation authorization, then stop before pushing. | Carry scoped commit authorization forward; review and commit proportionately, but do not push. Do not infer authorization for another repository. |
| Skip checks during iteration, then explicitly request lint and tests. | Follow the latest validation instruction and report actual outcomes. |
| Request review or a PR draft after implementation work. | Inspect the requested target without silently editing, committing or publishing. Preserve template wording and evidence-backed checkboxes. |
| Prepare descriptions for several stacked branches when only the final branch was tested. | Describe each branch against its parent and qualify inherited evidence. Do not claim each branch passed those checks. |
| Split work into branches where a unit depends on a resource introduced later. | Identify the missing dependency in the intermediate branch; final-tree equivalence alone is insufficient. |
| Rebase an integration change onto a refactored workflow. | Preserve intended behavior and current responsibility boundaries; do not restore obsolete implementation paths merely to resolve conflicts. |
| Write implementation plans and verification evidence. | Keep temporary artifacts in the workflow's designated ignored location or an explicit alternative; exclude them from product commits. |
| Remove apparently unused identifiers or resources. | Check definitions and production, test, and tooling consumers before removal. Preserve indirect or runtime consumers and identify references to missing definitions. |
| Compare behavior before and after a change while dependencies, test doubles, or asynchronous timing differ. | Exercise the real implementation in an appropriate runtime with documented fixtures, wait for observable readiness, and distinguish harness failures from product failures. Verify relevant interactions and state transitions; bound regression claims to tested flows. |

Use isolated fixtures for actions that could modify history or remote state.
Do not execute remote writes as part of an evaluation without authorization.
