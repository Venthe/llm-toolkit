# Java Conventions

## Libraries

- Prefer Lombok when the project already uses it and the annotations improve
  readability without hiding important behavior.
- Do not introduce a library solely to satisfy a personal preference.

## Implementation

- Prefer constructor injection for required dependencies.
- Use Lombok's @RequiredArgsConstructor when appropriate and consistent with the
  project, especially for implicit constructor injection with Spring.
- Prefer early returns when they reduce nesting.
- Use streams for clear data transformations; prefer loops when they make
  control flow or side effects easier to understand.
- Prefer immutable objects and records for suitable data models, subject to the
  project's Java version and conventions.
- Avoid unnecessary getters, setters, builders, and boilerplate.
- Avoid @Data on entities when generated equals, hashCode, or toString would
  have inappropriate semantics.

## Testing

For Java test design and tools, use the
[Java testing reference](../../software-testing/references/java.md).
