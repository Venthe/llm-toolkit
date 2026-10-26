# ADR lifecycle and storage

## Location and identity

Use the repository's existing location, template, and ID convention. If the user
asks to add the first ADR and has no preference, use
`docs/adr/0001-short-title.md`. This is a toolkit default, not a requirement of
the ADR format.

Inspect actual files before allocating the next ID, including untracked records.
Use the next available increasing number; do not overwrite an existing record or
renumber old records to fill gaps. Recheck the destination before writing if
other work may have added a record in the meantime. Maintain an existing index
when customary, but do not create an extra catalog without a concrete need.

## State transitions

| State      | Evidence needed                                                       |
| ---------- | --------------------------------------------------------------------- |
| Proposed   | A choice is under discussion or acceptance is unknown                 |
| Accepted   | The user or a reliable project record establishes acceptance          |
| Rejected   | A reliable decision record establishes that the proposal was declined |
| Deprecated | The decision is no longer applicable, with the reason recorded        |
| Superseded | An accepted replacement changes the previous decision                 |

Follow project-specific state names and transition rules. A draft replacement
does not automatically supersede an accepted record. Identify the intended
replacement relationship while preserving the old status until it is warranted.

## Preserve decision history

When authorized to supersede a decision, write a new record explaining the
changed context and link it to the old one. Update the old record's status with
a link to the replacement; keep its original rationale readable. Check both
links and any existing index. Editorial corrections need not create a new
decision, but changing the substance of an accepted choice should remain
traceable.

Do not infer a project's historical decision date from today's date or a file's
modification time. A creation date can describe the new document if useful and
clearly labeled. Include decision owners or approvers only when known.
