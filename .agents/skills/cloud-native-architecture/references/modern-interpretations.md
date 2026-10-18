# Modern interpretations of Twelve-Factor

## Distinguish the sources

[Mahdi Yusuf's 12 Factor App Revisited](https://architecturenotes.co/p/12-factor-app-revisited)
reconsiders the original principles in a modern operational setting. Useful
assessment prompts include monorepo tradeoffs, external configuration services,
retained build artifacts, shutdown behavior, environment differences, and broader
observability. Treat this as the author's interpretation, not an official second
edition or a requirement to copy every architectural preference.

[Kevin Hoffman's Beyond the Twelve-Factor App](https://www.oreilly.com/library/view/beyond-the-twelve-factor/9781492042631/preface02.html)
is a separate expanded framework with fifteen factors. It adds explicit emphasis
on API-first design, telemetry, and authentication/authorization while revising
the original organization. Use it to ask whether contracts, operational feedback,
and identity were designed intentionally rather than added only after failures.

## Applying these ideas in this toolkit

These are contextual decision prompts, not universal implementation prescriptions:

- **Application boundaries:** a monorepo can contain several independently built
  applications. Assess ownership, dependency isolation, and release identity rather
  than treating repository count as an architecture verdict.
- **Configuration and credentials:** preserve separation from code. Choose supported
  environment injection, mounted configuration, or secret-manager integration
  according to rotation and access requirements; do not prescribe plaintext secrets
  in manifests or claim every setting must be an environment variable.
- **State:** distinguish disposable application instances from durable backing
  services. Stateful workloads are valid; assess persistence, consistency, backup,
  restoration, and ownership explicitly. Moving state elsewhere does not remove
  the need to operate it.
- **Delivery:** identify the artifact, configuration, and migration state composing
  a release. Assess promotion and rollback independently; an image rollback cannot
  guarantee reversal of a database migration.
- **Interfaces:** define meaningful contracts and compatibility expectations.
  API-first does not require decomposing a coherent application into microservices.
- **Observability and identity:** relate telemetry to operational questions and
  user outcomes. Check identity and access at real trust boundaries; a gateway
  alone is not evidence that internal authorization is correct.
- **Environment differences:** identify differences that could change behavior
  and verify them deliberately. Local development need not duplicate production
  capacity, and a managed dependency cannot always be reproduced on a laptop.
- **Proportionate complexity:** compare operating cost, team experience, recovery
  needs, and scale before recommending Kubernetes, a service mesh, or more services.

Document any departure from the original principle and its rationale. Use the
platform-specific reference and current primary documentation to verify concrete
mechanisms before recommending configuration changes.
