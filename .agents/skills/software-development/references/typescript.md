# TypeScript contracts and domain intent

Read when designing or reviewing TypeScript APIs, including React prop types.
Use repository conventions and the user's explicit choices; these are review
heuristics, not reasons to rewrite unrelated code.

## Make the accepted contract visible

Inline a short, private component's prop type when the declaration is easier to
read in place. Name types that are shared, complex, or meaningful domain concepts.
Do not introduce a named type solely to replace a small literal used once.

Reuse a source contract when the relationship is intentional. For example,
`ComponentProps<typeof Modal>` can keep a configuration's accepted props aligned
with the modal. A narrow `Pick` can preserve a callback signature. Avoid broad
`Partial` or intersections that hide which inputs a consumer actually requires;
spell out a small independent contract when that is clearer. Shared shape alone
does not establish shared responsibility.

Use `ReactNode` for ordinary renderable children. Require a narrower element
shape only when the API inspects that element's type or props. Do not narrow
children merely to satisfy an implementation that unnecessarily wraps siblings.
Distinguish a component type, a JSX element, and its props; a type assertion does
not convert between them. See [React composition](react-composition-lifecycle.md)
when an API passes views or configurations.

Make action callbacks and their absence explicit. Omit or disable an unavailable
action rather than quietly substituting a successful-looking no-op. If a task
explicitly requests an unfinished callback, mark its missing behavior with a
specific TODO and preserve the intended disabled/loading behavior.

## Name commands, state, and context precisely

Use imperative names for commands: `submitApplication`, `openPolicy`, or
`dismissApplication`. A past-tense name is appropriate for an event that reports
something that already happened; do not mechanically rename actual events into
commands. Domain-specific names are more informative than generic `submit` or
`change` when several operations are possible.

Give meaningful derived conditions names and keep the source of truth visible.
Do not mirror props or query results into another state container through an
effect solely to select a view. Keep local state for actual user transitions,
such as opening an application or recording a submission awaiting reconciliation.
Use a reducer or discriminated union when it clarifies real transitions or
prevents invalid combinations, not as mandatory ceremony.

Reusable hooks should accept typed caller-supplied context rather than reach
into unrelated domain hooks. For example, a page-report hook can accept an event
and an additional-data contract with a typed `isFoo` field. Avoid replacing
known fields with an untyped bag. Mark a transitional adapter as transitional and
explain the compatibility boundary instead of disguising it as the final API.

Use braces for conditional statements, including early returns, unless explicit
project conventions require otherwise. Apply mechanical conventions within the
requested scope; do not enable a repository-wide lint rule as a way to enforce
new-code-only style without checking its effect on existing code.

## Keep static domain data simple

Use a shared plain object for fixed contact information or similar domain data
used by several views. Display and machine-readable values may both be explicit
when they are stable facts, such as a formatted phone number and its dial value.
Do not add formatting/parsing helpers solely to derive one fixed literal from
another. Retain such logic when it serves variable input or a real domain rule.
Keep translatable prose in translations and test-only fixtures in tests; inspect
all consumers before moving or deleting a shared fixture.
