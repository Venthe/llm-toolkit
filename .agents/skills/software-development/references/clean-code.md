# Pragmatic clean code

Use these to investigate a concrete maintenance concern.

### Make intent obvious

Names, control flow, types, and decomposition should make the important behavior understandable without reconstructing hidden assumptions. Comments are useful when they explain why, constraints, invariants, or non-obvious external behavior; do not require comments to compensate for unclear code.

### Keep responsibilities cohesive

A function/method/class/module should have a coherent reason for the behavior it owns. Look for unrelated responsibilities, policy mixed with mechanism, and objects that merely shuttle data while behavior lives elsewhere.

Do not infer responsibility from class length alone. A long cohesive method can be preferable to many tiny methods when decomposition only adds indirection.

### Control complexity

Prefer straightforward control flow. Look for deep nesting, unnecessary branching, boolean-state combinations, temporal coupling, duplicated conditionals, excessive callbacks, and abstractions that make the execution path harder to follow.

### Encapsulation

State invariants should be protected at the boundary that owns them. Avoid exposing mutable state or requiring callers to perform sequences of operations to maintain an object's validity.

### Abstraction should earn its place

Introduce an abstraction when it captures a meaningful concept, protects a boundary, accommodates real variation, or improves testability in a concrete way. Do not create interfaces, factories, generic base classes, strategy hierarchies, or extension points solely because variation might exist later.

Prefer composition when it produces a simpler dependency structure. Use polymorphism when different behaviors genuinely belong behind the same concept.

### Coupling and cohesion

Identify dependencies that make changes ripple unnecessarily. Prefer dependencies on stable concepts over volatile implementation details. Distinguish useful coupling required by the domain from accidental coupling caused by framework, persistence, transport, or utility details.

### DRY means duplicated knowledge, not duplicated text

Apply DRY in its original “once and only once” sense: avoid expressing the same knowledge in multiple places when a change to that knowledge would require coordinated updates. Do not mechanically eliminate every similar-looking fragment.

Treat coincidental similarity as potentially legitimate duplication. Consider whether two pieces of code are expected to change together before recommending unification.

### Simplicity over speculative flexibility

Do not reward generic solutions, hooks, configuration points, extension interfaces, or elaborate patterns that are not required by current behavior. A small direct design is preferable when it communicates the present requirement clearly.

### Error handling

Check whether errors are handled at the appropriate boundary, whether exceptions/results preserve useful context, whether failure states are explicit, and whether invalid states can propagate farther than necessary. Avoid catching errors merely to rethrow them unchanged.

### Side effects and state

Make side effects visible and localized. Look for hidden I/O, hidden mutation, global state, ambient context, order-dependent operations, and non-obvious lifecycle requirements.

### Tests as design evidence

Tests should expose behavior and intent. Prefer tests that isolate one meaningful condition and remain readable. Do not sacrifice test readability solely to eliminate small amounts of test duplication.


## Source influences

Consult when interpreting simple design or duplication of knowledge.

- [Martin Fowler: Beck Design Rules](https://martinfowler.com/bliki/BeckDesignRules.html)
- [Martin Fowler: Repetition / Once and Only Once](https://martinfowler.com/ieeeSoftware/repetition.pdf)
- [Martin Fowler: Continuous Design](https://martinfowler.com/ieeeSoftware/continuousDesign.pdf)

Use these as contextual heuristics. Similar text is not enough to establish
duplicated knowledge; ask whether the fragments should change together. Favor
design that communicates current intent without speculative extension points.
