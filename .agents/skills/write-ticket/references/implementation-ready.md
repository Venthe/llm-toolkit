# Prepare a ticket

## Workflow

1. Identify the intended outcome, current problem, scope, and known constraints.
   Preserve domain terms and supplied identifiers.
2. Write independently testable acceptance criteria covering the outcome and
   relevant failure behavior. Prefer a few strong criteria; split by independent
   outcomes only when appropriate, not by an arbitrary criterion count.
3. Select a minimal applicable Definition of Done from the team's supplied
   checklist or [the default menu](definition-of-done.md). Read the menu when
   choosing default items; do not include every item automatically.
4. Write a description explaining context and purpose without repeating criteria
   or prescribing an implementation unless it is a requirement.
5. Use [the ticket template](../assets/ticket-template.md) when no team format
   is supplied. The default order is Definition of Done, Acceptance Criteria,
   Description. A user or team template takes precedence.
6. Check each criterion for a clear pass/fail outcome and verify that no
   behavior, stakeholder approval, completion status, dependency, or reference
   was invented.

## Handling incomplete requests

Produce a useful draft from supported information. Ask a focused question only
when missing behavior prevents meaningful acceptance criteria. Mark material
unknowns clearly rather than disguising them as requirements. At least one
criterion must describe an actual supported outcome; an unresolved placeholder
does not make a ticket ready for implementation.

Keep checklist items unchecked unless completion evidence is supplied. Omit
empty reference sections unless the team template requires them. For more
guidance on criterion quality, read
[acceptance-criteria guidance](acceptance-criteria.md).

Return only the ticket Markdown unless analysis was requested. Drafting does not
authorize creating or updating an issue in an external system.
