# React components

Read when implementing, refactoring, or reviewing React components. Apply the
[clean-code guidance](clean-code.md), including the step-down reading order.

## Separate presentation from orchestration

Split components into presentational ("dumb") and container ("smart")
responsibilities. Presentational components receive data and callbacks through
props and render the UI. Containers own data access, application state, business
decisions, and coordination, passing the values and actions the UI needs.

Keep this separation meaningful: extract a component around a coherent UI or
domain responsibility. Local presentation state does not by itself require a
container. Hooks can encapsulate orchestration logic while a container composes
the presentation.

## Name components for their domain function

Prefer names describing what a component does in the domain, including for
private subcomponents. For example, use `CallAdacButton` for the action that
calls ADAC and `PolicyDetails` for the policy information. Avoid names such as
`BottomButton` or `ContentBlock` when a domain responsibility is known.

## Keep contextual layout with the composing parent

Components should own their intrinsic appearance and internal layout. The
parent that arranges them should own contextual styling, such as spacing
between siblings, placement, and sizing within that composition. Avoid props
that encode a child's position or surrounding layout, such as `first`, `last`,
or `inSidebar`, when their only purpose is styling.

Expose a standard styling extension point when the parent needs one. In React,
accept `className`, type it from the root element's props, and merge it with the
root's intrinsic classes using the project's class composition convention.
For a div, use `ComponentPropsWithoutRef<'div'>['className']`. Forward that prop
through domain components to their rendered root so the composing parent can
control layout without adding wrapper elements or leaking positional knowledge
into descendants. Parent-owned gap or layout rules are also appropriate when
they express the relationship directly.

Keep semantic variants and behavior props when they represent real component
states or domain choices. This rule applies to contextual presentation; it does
not require replacing meaningful APIs with arbitrary styling overrides or
exposing every DOM prop.

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
