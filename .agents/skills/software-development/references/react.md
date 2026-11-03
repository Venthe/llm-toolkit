# React components

Read when implementing, refactoring, or reviewing React components. Apply the
[clean-code guidance](clean-code.md), including the step-down reading order.
For TSX contracts, also read [TypeScript](typescript.md). For component-valued
APIs, persistent containers, or lifecycle effects, read
[composition and lifecycle](react-composition-lifecycle.md).

## Assign ownership by domain responsibility

A component owns the data and behavior needed for its domain responsibility.
A parent that selects a view should not also manage that view's requests,
navigation, or submission guards. A policy modal can fetch its policy; an
application modal can guard dismissal while submitting. Split presentation from
orchestration when it creates a useful boundary, not merely because data access
is present. Hooks can encapsulate orchestration without requiring another
wrapper component.

Each translated subcomponent should obtain its own translation hook rather than
receive a translator as a prop. Keep reusable infrastructure hooks independent
of domain lookup: a telemetry hook receives typed event context from its caller
instead of discovering membership itself. Preserve meaningful shared state and
existing contracts when deciding where ownership belongs.

## Name components for their domain function

Prefer names describing what a component does in the domain, including for
private subcomponents. For example, use `CallAdacButton` for the action that
calls ADAC and `PolicyDetails` for the policy information. Avoid names such as
`BottomButton` or `ContentBlock` when a domain responsibility is known.

A name alone does not justify an extraction: a helper that only hides an
already clear translation key or library button can add indirection without a
useful responsibility. Keep it inline unless it owns behavior, a hook boundary,
reuse, or a cohesive piece of presentation. Conversely, extract a substantial
policy section into a named component even when it is used once.

## Keep contextual layout with the composing parent

Components should own their intrinsic appearance and internal layout. The
parent that arranges them should own contextual styling, such as spacing
between siblings, placement, and sizing within that composition. Avoid props
that encode a child's position or surrounding layout, such as `first`, `last`,
or `inSidebar`, when their only purpose is styling.

Expose a standard styling extension point when the parent needs one. In React,
accept `className` and, when needed, `style`; type them from the root element's
props. Merge `className` with the root's intrinsic classes using the project's
class composition convention.
For a div, use `ComponentPropsWithoutRef<'div'>['className']`. Forward that prop
through domain components to their rendered root so the composing parent can
control layout without adding wrapper elements or leaking positional knowledge
into descendants. Parent-owned gap or layout rules are also appropriate when
they express the relationship directly.

Keep semantic variants and behavior props when they represent real component
states or domain choices. This rule applies to contextual presentation; it does
not require replacing meaningful APIs with arbitrary styling overrides or
exposing every DOM prop.

## Choose composition deliberately

Child slots are an API design choice, not a default preference. Assess the
consumer's composition needs and existing contracts before choosing slots,
configuration objects, or explicit props. When using slots, accept ordinary
React children and relevant styling props on the slot itself; avoid redundant
pairs such as footer/footerClassName when the footer child can own className.

Keep small, tightly coupled components together. Extract files for independent
domain responsibilities or reuse, not one file per component. Inline prop types
for small private components; retain named types when shared or complex. Prefer
named, const-backed domain actions for meaningful event handlers. Trivial mapping
and render callbacks can remain inline. Update component, test and stylesheet
names when their responsibility changes. Group view-specific helpers with their
view; move genuinely shared assets and components to a shared location. Keep
public import paths stable during a file-layout-only change. Use the existing
styling module for existing styles and place new styles with their owner; avoid
copying generated or module class names as string literals.

Prefer explicit return branches over accumulating JSX in intermediate variables.
Use intermediate variables for meaningful derived state. Do not replace a useful
reducer merely to avoid reducers; remove effect/reducer synchronization when
ordinary derived state and event transitions express the behavior more clearly.
Remove redundant fragments and styling-only wrappers when existing component
props express the same layout. Keep fragments needed for sibling returns and
wrappers with real layout or semantic responsibilities. Follow the project's
conditional-brace convention; these guidelines do not imply a blanket ban on
reducers, fragments, separate files, or inline functions.

## Prefer arrow functions and step-down order

Prefer `const ComponentName = (...) => { ... }` for components. Put the main
component before its private subcomponents, following their order of use.
Place shared subcomponents below the components that use them. Keep these
definitions at module scope so rendering does not create new component types.

```tsx
export const PolicyOverview = ({ policy, onCall }) => (
  <section>
    <PolicyDetails policy={policy} />
    <CallInsurerButton onCall={onCall} />
  </section>
);

const PolicyDetails = ({ policy }) => <p>{policy.number}</p>;

const CallInsurerButton = ({ onCall }) => (
  <button onClick={onCall}>Call insurer</button>
);
```

The example omits prop types to focus on declaration order; use the project's
typing conventions in implementation. Preserve initialization safety: arrow
function bindings must be initialized before they are invoked. Deferred JSX
references in component bodies allow the parent-first reading order above.
