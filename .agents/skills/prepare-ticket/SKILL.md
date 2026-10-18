---
name: prepare-ticket
version: 1.0.0
description: "Create concise Jira/Linear tickets in Markdown with Description, Acceptance Criteria, and a configurable Definition of Done, using testable outcome-focused acceptance criteria and a conditional DoD checklist."
---

# Jira / Linear Ticket Markdown Skill

## Purpose

Turn a feature request, bug, task, or rough product/technical note into a clear Markdown ticket suitable for Jira or Linear.

The resulting ticket MUST contain these sections, in this order:

1. Definition of Done
2. Acceptance Criteria
3. Description

The ticket should establish shared understanding of the requested outcome, define testable boundaries, and avoid prescribing an implementation unless the implementation constraint is itself part of the requirement.

## Core principles

- Write for the people who will build, test, review, and accept the ticket.
- Prefer observable outcomes over implementation instructions.
- Keep the scope explicit. Clarify what is in scope and, where useful, what is out of scope.
- Do not invent product behavior, requirements, dependencies, stakeholders, APIs, metrics, environments, or references that were not provided or clearly supported by the input.
- Preserve known domain terminology and identifiers.
- Keep the ticket detailed enough to remove ambiguity, but do not turn it into a design document unless requested.

## Output format

Produce Markdown in this shape:

```markdown
# <Ticket title>

## Definition of Done

- [ ] ...

## Acceptance Criteria

- [ ] ...

## Description

<problem, context, intended outcome, scope, and relevant details>

### References

- <reference>
```

The title is optional when the caller asks only for the body. Do not add a title if one was explicitly supplied and the target format expects only the ticket body.

## Acceptance Criteria

Acceptance criteria describe how the feature can be used or verified from the end-user, stakeholder, or observable system-behavior perspective. They establish the boundary of the story and form the basis for acceptance testing.

### Rules

Every ticket MUST have at least one acceptance criterion.

Each acceptance criterion SHOULD:

- be independently testable;
- produce a clear pass/fail result;
- describe the expected outcome, not the implementation approach;
- use simple, unambiguous language;
- cover functional behavior and relevant non-functional behavior when applicable;
- cover meaningful failure/error behavior when the behavior matters to the story;
- establish scope boundaries where ambiguity is otherwise likely.

Avoid criteria that are:

- tied unnecessarily to a specific implementation or technical approach;
- so narrow that alternative valid user behavior is excluded;
- so broad that the team cannot determine where the story stops;
- complex, jargon-heavy, or difficult to test;
- merely restatements of the implementation plan.

Prefer a small number of high-value criteria. As a rule of thumb, target 1–3 criteria for a normal story. When a story needs roughly 4–5 criteria, consider whether it should be split. Six or more is a strong signal to investigate splitting the story.

Acceptance criteria should be defined before implementation begins, where practical, so that they represent customer/product intent rather than merely documenting the implemented solution.

### Acceptance-criteria style

Use concise statements that can be verified directly.

Prefer:

```markdown
- [ ] The authenticated user can view the current statement balance.
- [ ] The payment due date is displayed for the current billing period.
- [ ] When the balance service is unavailable, the user sees an actionable error message.
```

Avoid:

```markdown
- [ ] Add a `GET /balance` endpoint backed by repository method X.
- [ ] Refactor the balance service to use Redis.
```

The latter are implementation details unless the implementation itself is an explicit requirement.

### Splitting signal

If the ticket accumulates many independent acceptance criteria or several distinct user outcomes, consider treating that as evidence that the work should be split into multiple stories. Do not split automatically when the user explicitly wants one ticket.

## Definition of Done

The Definition of Done is a reusable checklist. It is NOT an instruction to include every item on every ticket.

Select only the items that are relevant to the ticket and its product context. Preserve the hierarchy below when selected.

### Feature tests

- [ ] Feature tests
  - [ ] Unit tests are written and passing
  - [ ] Integration tests are written and passing
  - [ ] Functional specifications are written and tested by automatic tests
  - [ ] System-level non-functional requirements (e.g. system-level performance) are tested and passed

### Code review

- [ ] Code review
  - [ ] Code review is passed with all questions reconciled
  - [ ] Code does not have Static Analysis issues ranked MAJOR or above
  - [ ] All commits are ready to merge and are succinctly described
  - [ ] Target branch is building with the feature/commit
  - [ ] Any configuration or build changes are documented
  - [ ] TODO/FIXME items for the story ID are resolved accordingly
  - [ ] Manual functional tests are passed
  - [ ] Manual exploratory tests are passed
  - [ ] Project is deployed on a test environment identical to the production platform
  - [ ] If not covered by automatic functional tests, the feature is tested against the acceptance criteria
  - [ ] If not covered by automatic functional tests, non-regression is confirmed
  - [ ] All relevant languages are translated
  - [ ] Tested on relevant applications
  - [ ] Tested on relevant browsers
  - [ ] Tested on relevant devices
  - [ ] Bugs ranked Major or above are fixed

### Stakeholder review

- [ ] Stakeholder review
  - [ ] Product Owner has had functionality presented and has accepted the functionality
  - [ ] UX Designer confirmed the design
  - [ ] Marketing input is done
  - [ ] Documentation updated
  - [ ] Technical description
    - [ ] Public and/or private API definition updated

### Functional

- [ ] Functional
  - [ ] Dependent Stories identified and linked
  - [ ] Legal documents are done
  - [ ] Environment variables documented and present in staging and production environments

## How to select Definition of Done items

Choose the smallest applicable subset rather than copying the entire checklist mechanically.

Typical selection logic:

- Backend logic with meaningful behavior: unit tests; integration tests when external boundaries are involved.
- End-to-end user-facing behavior: functional specifications/automatic tests and relevant manual validation.
- Performance, scale, availability, security, or other measurable NFRs: system-level NFR verification.
- UI changes: manual functional/exploratory testing; relevant browsers and devices; UX review; translations where applicable.
- Public or private API changes: API definition/documentation updates.
- Configuration or deployment changes: configuration/build documentation and staging/production environment variables.
- Cross-story work: dependency identification and linking.
- Compliance-sensitive work: legal-document checks.
- Production-like deployment requirements: test-environment deployment verification.
- Marketing- or externally communicated functionality: marketing input.
- Documentation-sensitive changes: documentation update.

Do not mark an item applicable merely because it exists in the template.

Do not claim that a DoD item is complete during ticket creation. The skill only defines the checklist unless completion status is explicitly supplied.

## Description

The Description should explain the reason for the work and the intended outcome without duplicating the acceptance criteria line by line.

A strong description usually contains, as applicable:

- Context / problem: what is happening today or what need exists.
- Objective: what capability or outcome is needed.
- User or system impact: who benefits and how.
- Scope: important inclusion/exclusion boundaries.
- Constraints: known business, product, compatibility, or technical constraints that genuinely affect the work.
- References: links to designs, specifications, related tickets, incidents, documentation, discussions, or other source material.

Do not invent a user story persona when none is supplied. Use neutral wording such as "The system should..." or "Users need..." when the actor is known only at a general level.

Do not duplicate acceptance criteria wholesale inside the description. The description provides context; acceptance criteria define verifiable outcomes.

## References

Always reserve space for references when the ticket may have supporting material.

Use:

```markdown
### References

- <link or ticket reference>
```

If no references are provided or implied by the input, keep the section as an empty placeholder only when the target team's ticket template expects it. Otherwise omit the References subsection.

Never invent URLs, ticket IDs, document IDs, or other references.

## Handling incomplete input

Do not ask for clarification merely because the input is rough. Produce the best supported ticket from the available information.

When important information is genuinely absent:

- avoid inventing it;
- phrase the ticket using only supported requirements;
- leave a concise placeholder only when the omission would otherwise make the ticket unusable.

Examples:

```markdown
- [ ] <Define expected behavior when the external dependency is unavailable>
```

Use placeholders sparingly. Prefer a neutral, useful statement when the intended outcome is already clear.

## Ticket-generation procedure

When asked to create a Jira/Linear ticket:

1. Identify the primary business, user, or system outcome.
2. Identify the concrete scope and important constraints from the input.
3. Draft 1–3 outcome-focused acceptance criteria when practical.
4. Add relevant failure/error and non-functional criteria when supported by the request.
5. Select only the applicable Definition of Done categories and checklist entries.
6. Write a description that explains context, objective, impact, scope, and constraints without prescribing unnecessary implementation details.
7. Add a References subsection when there are references or when the requested ticket format calls for one.
8. Validate that acceptance criteria are independently testable and pass/fail.
9. Validate that no requirement, completion state, stakeholder approval, or technical detail has been invented.
10. Return the ticket as Markdown.

## Review procedure

When asked to review an existing Jira/Linear ticket, check:

- all three required sections are present and in the expected order;
- Definition of Done items are relevant rather than mechanically exhaustive;
- there is at least one acceptance criterion;
- each acceptance criterion is independently testable and pass/fail;
- criteria describe outcomes rather than implementation details;
- relevant functional and non-functional behavior is covered;
- the scope boundary is understandable;
- the description provides context without duplicating AC;
- references are preserved and not invented;
- excessive acceptance criteria do not indicate an obvious story-splitting opportunity;
- no completion status is falsely implied.

## Preferred output

Unless the caller asks for analysis, return only the Markdown ticket.

Do not wrap the ticket in a prose introduction such as "Here is the ticket".
