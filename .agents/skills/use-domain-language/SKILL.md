---
name: use-domain-language
description: >-
  Enforce consistent domain terminology across code, documentation, APIs,
  architecture, and tests. Follow Domain-Driven Design (DDD), prioritize
  the project's GLOSSARY.md, preserve ubiquitous language within bounded
  contexts, and prefer precise, culturally neutral terminology.
metadata:
  version: "1.0.0"
  category: software-engineering
  disable-model-invocation: true
  tags:
    - ddd
    - ubiquitous-language
    - terminology
    - technical-writing
---

# Domain Language and Terminology

## Purpose

Ensure that all communication, code, and artifacts use precise, consistent
terminology aligned with the project's domain model.

Follow Domain-Driven Design (DDD) principles:

- Use the ubiquitous language shared by developers and domain experts.
- Respect bounded contexts and their potentially different meanings.
- Prefer domain concepts over implementation details when expressing
  business rules.
- Use terminology consistently across code, documentation, APIs, tests,
  events, logs, and configuration.

## 1. Establish the Vocabulary

Before creating or modifying code or documentation:

1. Locate `GLOSSARY.md` in the current project, starting from the relevant
   directory and working toward the repository root.
2. If multiple glossary files exist, identify the one applicable to the
   current module or bounded context. A more local glossary may specialize
   terms defined by the repository-wide glossary.
3. Inspect existing domain models, interfaces, types, and neighboring code
   to understand established terminology.
4. Use the glossary as the authoritative source for domain terms unless the
   user explicitly requests a terminology change.

If no applicable glossary exists, derive terminology from the existing
domain model and the user's language. Do not invent domain concepts without
a reason.

Do not claim to have consulted a file that was not accessible.

## 2. Apply the Ubiquitous Language

Use the same term for the same concept within a bounded context.

For example, if the domain calls something an `Order`, do not casually
rename it to `Purchase`, `Transaction`, or `Request` unless those terms
represent distinct domain concepts.

Apply terminology consistently to:

- Classes, interfaces, methods, properties, variables, and types.
- Database tables, columns, and migration names.
- API endpoints, request and response fields, and error codes.
- Domain events, commands, policies, and business rules.
- Tests, fixtures, documentation, and user-facing messages.
- Architecture diagrams, deployment configuration, and operational tools.

Prefer domain-oriented names:

- `OrderCancellationPolicy` over `OrderStatusHelper`.
- `InvoiceIssued` over `ProcessCompleted`.
- `InventoryReservation` over `GenericResourceLock`, when the operation
  represents a business inventory reservation.

These examples are illustrative, not universal naming rules. Choose names
according to the actual domain semantics.

## 3. Preserve Semantic Precision

Do not treat terminology as a purely stylistic concern.

Before changing a term, determine what the underlying concept does.

- Do not conflate distinct concepts merely because they have similar names.
- Do not introduce synonyms for an existing concept without a meaningful
  semantic distinction.
- Do not rename established concepts to more fashionable terminology.
- Do not force domain terminology onto infrastructure concepts when doing
  so obscures their actual behavior.
- Do not replace a precise technical term with a neutral but ambiguous one.

When a term has different meanings across bounded contexts, preserve those
distinctions. Qualify the name where necessary instead of forcing a single
global definition.

If the intended meaning cannot be established, state the ambiguity and
ask one targeted question when it materially affects correctness.

## 4. Prefer Culturally Neutral Terminology

Prefer clear, descriptive terminology that does not rely on unnecessary
racial, hierarchical, or historically loaded metaphors.

Choose replacements based on actual behavior, not a mechanical word
substitution.

### 4.1 Master / Slave

Avoid introducing `master` / `slave` terminology when a more precise,
neutral alternative describes the relationship.

Choose the term according to the architecture:

| Context                                 | Preferred terminology |
|-----------------------------------------|-----------------------|
| Database replication                    | Primary / replica     |
| Distributed leadership                  | Leader / follower     |
| High availability                       | Active / standby      |
| Read/write separation                   | Writer / reader       |
| Task orchestration                      | Coordinator / worker  |
| Parent process with auxiliary processes | Parent / helper       |
| Generic replicated resources            | Primary / secondary   |

These terms are not universally interchangeable. Preserve the distinction
between authority, replication, availability, and workload distribution.

### 4.2 Blacklist / Whitelist

Prefer names that explicitly describe the operation or policy.

| Context                         | Preferred terminology                            |
|---------------------------------|--------------------------------------------------|
| General filtering               | Blocklist / allowlist                            |
| Authorization policy            | Deny / allow                                     |
| Firewall packet handling        | Drop / permit, when those are the actual actions |
| Access management               | Access list, with explicit allow/deny semantics  |
| Collection of rejected entries  | Rejected-items list or denylist                  |
| Collection of permitted entries | Permitted-items list or allowlist                |

Use `blocklist` / `allowlist` as the general-purpose replacement when
the existing behavior matches those concepts.

Alternatives such as `droplist`, `accesslist`, `drop-permit`, and
`block-permit` should only be used when they accurately describe the
domain or are already established by the project glossary. Do not introduce
ambiguous or unfamiliar terminology merely to avoid an older expression.

### 4.3 Master as a Standalone Term

`Master` does not have one universally correct replacement. Determine its
meaning first.

| Existing term        | Preferred terminology                         | Applicable context                             |
|----------------------|-----------------------------------------------|------------------------------------------------|
| Master branch        | Main branch                                   | Default Git development branch                 |
| Master/slave         | Context-specific alternative                  | See the preceding table                        |
| Master copy          | Source copy or canonical copy                 | Original or authoritative copy                 |
| Master record        | Canonical record or source record             | Authoritative representation of an entity      |
| Master template      | Base template                                 | Template inherited or extended by others       |
| Master configuration | Baseline configuration                        | Default configuration used as a starting point |
| Master key           | Root key or key-encryption key, as applicable | Cryptographic key hierarchy                    |

Do not rename concepts blindly. For example, a database primary key is
not a replacement for a master record, and a root key is not necessarily
equivalent to every key historically called a master key.

### 4.4 General Language Rules

Apply the same principle to other potentially loaded or imprecise terms.

- Prefer `parent` / `child` for structural relationships where appropriate.
- Prefer `primary` / `secondary` when describing precedence or replication.
- Prefer `allow` / `deny` when describing authorization decisions.
- Prefer `source` / `destination` when describing data movement.
- Prefer `active` / `inactive` when describing operational state.
- Prefer `enabled` / `disabled` when describing configuration switches.

These are context-dependent examples, not a mandatory global vocabulary.

Do not substitute terms merely because they are more neutral. The
replacement must retain the original meaning.

## 5. Handle Legacy and External Terminology

A project may need to preserve terminology imposed by external systems.

Examples include:

- Public API fields and established wire protocols.
- Third-party database schemas.
- Operating-system interfaces.
- Vendor-specific configuration keys.
- Backward-compatible identifiers and serialized data.

In these cases:

1. Preserve externally required identifiers when changing them would break
   compatibility.
2. Use neutral, domain-appropriate terminology in new internal names and
   documentation where possible.
3. Document the mapping between the internal name and the legacy name.
4. Avoid unnecessary public API changes solely for terminology cleanup.
5. If a migration is required, describe its compatibility and data migration
   implications explicitly.

Do not silently change persisted values, API contracts, or external
identifiers as part of a naming cleanup.

## 6. Maintain GLOSSARY.md

When adding a genuinely new domain concept, consider adding it to
`GLOSSARY.md`.

For each important entry, record:

- **Term:** The preferred name.
- **Definition:** What the concept means in this domain.
- **Context:** The bounded context where the definition applies.
- **Related terms:** Distinct concepts that may be confused with it.
- **Deprecated terms:** Legacy names and their preferred replacements,
  where relevant.

Keep definitions concise and operational. A glossary should resolve
ambiguity, not merely repeat class names.

Do not create glossary entries for every variable, implementation detail,
or ordinary technical term.

When a proposed change conflicts with an existing definition, resolve the
conflict before propagating the new name. Update the glossary when the
domain language itself changes.

## 7. Review Before Completing Work

Before delivering a change, verify that:

1. The applicable glossary and established domain language were followed.
2. Names describe actual behavior and domain meaning.
3. Synonyms do not accidentally represent the same concept.
4. New terminology is culturally neutral where a precise equivalent exists.
5. Legacy identifiers remain compatible unless a migration was explicitly
   requested.
6. Any necessary glossary changes are included.

Do not perform unrelated mass renaming or terminology refactoring unless
it is within the requested scope.

## Output Expectations

When creating or modifying artifacts, apply the rules directly rather than
merely describing them.

When detecting a terminology problem:

- Use the preferred term in new work.
- Correct inconsistent terminology within the requested scope.
- Explain significant semantic differences when a direct replacement is
  inappropriate.
- Flag unresolved conflicts with the glossary rather than inventing a
  resolution.

Prioritize, in order:

1. Correct domain semantics.
2. Consistency with the applicable glossary.
3. Technical accuracy and compatibility.
4. Culturally neutral, unambiguous terminology.
5. Stylistic consistency.