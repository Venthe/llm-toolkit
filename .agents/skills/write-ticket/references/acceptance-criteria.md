# Acceptance criteria

Based on the [Agile For Growth acceptance-criteria guidance](https://agileforgrowth.com/blog/acceptance-criteria-checklist/)
supplied by the user. Apply its tips pragmatically; they support shared
understanding rather than impose a universal Scrum procedure.

## Purpose and timing

Describe how the feature serves the end user or exposes observable system behavior.
State its business value and boundaries: what is included, what is excluded, and
what happens when meaningful failure conditions occur. Criteria are specific to
the story and provide the basis for acceptance tests.

Draft and review criteria during refinement, before implementation and before the
story is considered ready for planning under the team's process. Refine them as
understanding improves; do not retrospectively rewrite intent just to match the
implementation. When documenting existing behavior, label that context honestly.

The team can draft criteria jointly with the Product Owner or relevant stakeholder.
The important outcome is shared understanding and validation of intent. Do not
invent a Product Owner's approval or require a particular job title in a project
that uses another ownership model.

## Quality checks

1. An implementation-ready story has at least one concrete acceptance criterion.
2. Define expected outcomes before implementation where the workflow permits.
3. Each criterion can be tested independently against meaningful behavior.
4. Each has a clear pass/fail result, with enough context to avoid ambiguity.
5. Specify the result, not a preferred implementation, unless the interface or
   technical approach is an explicit requirement.
6. Include functional and relevant non-functional outcomes. Use supplied measurable
   thresholds; flag missing thresholds instead of fabricating them.
7. Have the responsible stakeholder verify the intended outcome under the team's
   process. Recording that expectation does not mean review has happened.

Cover happy paths and supported error behavior. Avoid vague criteria such as
"works correctly", unexplained jargon, or compound requirements with unclear
failure results. Do not narrow a criterion to one implementation or broaden it
into an entire product area. A testing detail need not become a separate criterion.

## Amount and scope

The supplied article suggests 1-3 criteria as a useful starting point, exploring
splits at 4-5, and treating 6 or more as a strong prompt to examine scope. These
are heuristics, not a cap or proof of what fits in a sprint. Split independent
outcomes when that enables delivery and feedback; preserve a coherent story with
several necessary boundary cases. Respect an explicit request for one ticket.

DoD checks do not replace story-specific behavior. A generic error-handling DoD
may cover routine expectations, but material user-visible failure behavior still
needs a clear agreed contract. Triage-ready tickets may leave criteria unresolved;
do not apply implementation readiness rules to preliminary triage.

## Examples

For a request to show an authenticated cardholder's statement, possible criteria
are statement balance, total balance, minimum payment, due date, and the agreed
unavailable-service response. Select only outcomes supported by the actual request.
Keep illustrative financial values internally consistent; they are example data,
not requirements. Do not copy amounts, dates, or error text into an unrelated ticket.

For a student-assessment report, current and previous results can be outcomes.
Printing, saving, or sharing may warrant separate stories when independently
valuable. Include failure behavior only when it is supplied or agreed.

Concrete wording for a known balance-display requirement:

- [ ] The authenticated user can view the current statement balance.
- [ ] The payment due date is displayed for the current billing period.

"Add a GET endpoint backed by repository X" describes an implementation. Use it
as a criterion only when that interface or implementation is itself required.

## Review

Verify that criteria define the requested outcome and boundaries, can be evaluated
individually, include supported failure conditions, and do not introduce invented
requirements. Preserve known constraints and references. Label material unknowns;
an unresolved placeholder is not a completed acceptance criterion.
