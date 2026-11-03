# Java testing

Inspect the build, Java version, test source sets, and existing conventions
before choosing tools. Use the project's Maven/Gradle wrapper and configured
test tasks where available; do not invent a task name or introduce a library for
preference.

- Follow existing JUnit lifecycle and mocking conventions.
- Prefer AssertJ when already established for expressive assertions.
- Use Awaitility when established for bounded eventual assertions; avoid fixed
  sleeps and ensure failures identify the condition that was not met.
- Use parameterized tests for meaningful related input cases, with readable case
  names and expected results.
- Follow fixture, naming, and cleanup patterns. Keep mocks at meaningful
  boundaries and verify real serialization/persistence semantics where needed.
- Prefer constructor-supplied dependencies for isolated tests. Start a framework
  context only when wiring or framework behavior is what needs verification.
- Separate fast tests from environment-dependent checks using existing project
  conventions. State when a requested task excludes integration tests.
- Check for shared static state, leaked threads, time-zone assumptions, and
  order-sensitive fixtures when tests pass alone but fail in a suite.

Use temporary resources with explicit ownership and cleanup. Do not point tests
at a developer's or production database merely because credentials are
available.
