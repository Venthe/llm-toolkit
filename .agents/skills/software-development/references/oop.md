# Object-oriented design

Use when objects and their contracts are meaningful to the task. Pure functions,
data records, and procedural modules remain appropriate where they are clearer.

## Model behavior and invariants

Place rules with the concept that owns them. Constructors and operations should
protect valid states; callers should not need to remember an undocumented sequence
of setters. Use value objects when they make a meaningful domain distinction or
centralize validation, not to wrap every primitive mechanically.

Keep mutable state private and consider defensive copies or immutable values at
ownership boundaries. Data transfer objects can appropriately carry data without
business behavior; distinguish them from objects responsible for domain rules.

## Contracts and variation

Use interfaces to describe a client-relevant capability or external boundary.
Avoid exposing methods a client does not need merely to mirror an implementation.
Prefer explicit dependencies over hidden service lookup or global mutable state.

Inheritance requires substitutability: a subtype must preserve the promises
clients rely on, including failure behavior and invariants. Prefer composition
when the relationship is only code reuse or when inheritance complicates state
and lifecycle. Do not introduce a strategy hierarchy for hypothetical variation.

## Review questions

- Whether objects protect their own invariants.
- Whether behavior is located with the data/concept it belongs to.
- Whether inheritance represents a genuine substitutable relationship rather than code reuse.
- Whether interfaces represent a client-relevant contract rather than implementation camouflage.
- Whether value objects or domain types would make invalid states harder to represent.
- Whether composition would simplify a complicated inheritance or dependency structure.
- Whether static/global helpers conceal dependencies or merely package genuinely pure operations.

Avoid using SOLID as a numerical scorecard. Use the principles to explain concrete coupling, cohesion, substitutability, or dependency problems.
