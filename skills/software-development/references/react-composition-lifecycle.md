# React composition and lifecycle boundaries

Read when an API accepts or selects views, when a shell must survive content
changes, or when effects control focus, scrolling, or animation. Apply the
[React ownership guidance](react.md) first. The patterns below are conditional;
a normal component tree does not need a configuration protocol.

## Establish what the API returns

Before implementing a proposed composition API, write a minimal producer and
consumer example. State whether the producer returns plain props, a JSX element,
or a component type, and who renders it. Check this against the requested usage
before choosing an implementation.

A JSX element is a description. Given `<PolicyView />`, its props are the inputs
to `PolicyView`, not the output that `PolicyView` will eventually render. A parent
cannot extract nested slots by inspecting that element. Do not call a component
as an ordinary factory to discover its output: React must render components so
hooks and component identity retain their normal lifecycle.

A pure factory may return configuration data when that is the chosen contract.
A function that calls hooks must obey hook rules and use a hook API; a factory
name does not make conditional hook calls valid. Do not move all view hooks into
the parent just to make slot extraction possible. The selecting parent should
still select the view, while the selected component owns its data and behavior.

When component-owned hooks must configure a persistent shell, consider a small
adapter around the existing primitive. A context-based host/configuration pair
is one option, not a required React pattern. Document whether the configuration
renders DOM, what props and children it accepts, how many active configurations
are supported, and what happens outside the host. If registration uses effects,
ensure obsolete cleanup cannot clear a newer registration. Avoid teaching a
generic modal about domain-specific views.

## Separate shell identity from content changes

Keep a persistent shell at a stable place and type in the tree when preserving
its backdrop, scroll position, or animation is a requirement. Changing its `key`
remounts it; use an explicit content identity prop when the intended behavior is
only refocusing or measuring new content. Keep that identity stable during
ordinary typing, translation updates, or data refreshes that should preserve
interaction state.

A prop such as `contentKey` communicates a content transition without encoding
ADAC or another domain in the primitive. View components can supply it through
the same configuration contract as other modal props. Keep close-on-submit guards
with the submitting view; preserve the original opener until final dismissal,
not every internal view transition.

Verify behavior at the boundary that promises persistence: the same dialog and
backdrop survive a transition, a draft survives a background refresh, entering a
new view applies the intended focus policy, and dismissal restores the opener.
Do not claim persistence merely because both renders look identical.

## Give global effects a clear owner

Inspect the underlying UI library before adding body scroll locks, focus traps,
portals, or animation effects. Two layers restoring the same captured DOM style
can interfere even if each cleanup looks correct in isolation. Prefer one owner
for the effect; remove duplicate ownership only after checking required behavior
such as scroll targets and nested containers.

For lifecycle changes, exercise the full shell under Strict Mode, including
open, close, reopen, and unmount. Wrapping only a child view misses shell effects.
Check restoration of pre-existing values as well as empty defaults. Cleanup must
handle React's setup/cleanup replay without leaving a stale lock or registration.
Use browser checks for clipping, stacking, responsive sizing, and animation;
unit tests alone cannot establish those visual outcomes. Respect reduced-motion
settings unless an explicit, documented API requests an override.
