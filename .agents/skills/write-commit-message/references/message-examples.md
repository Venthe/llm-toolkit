# Message examples and review checks

Use examples as wording guidance, never as a source of invented rationale or
IDs.

## Subject

An imperative subject completes “If applied, this commit will …”:

```text
Fix connection leak in worker pool
Add retry handling for API timeouts
Update installation documentation
```

Avoid vague subjects such as `Various fixes` and activity descriptions such as
`Updating documentation`. Preserve repository-required prefixes and scopes.

## Body

When the stated rationale supports it:

```text
Reject expired session tokens before authorization

Validate token expiry before calling the authorization service so expired
sessions fail consistently and avoid an unnecessary downstream request.
```

A simple documentation correction may need only a subject. A body should add
motivation, constraints, or consequences rather than narrating every changed
line. Keep known issue references and required trailers after the body; never
fabricate them. Preserve deliberate code, URLs, and structured formatting when
wrapping.

## Reviewing an existing message

Check target scope, imperative wording, subject/body separation, useful context,
repository limits, required trailers, and unsupported claims. Suggest concrete
corrections without staging or rewriting commits.
