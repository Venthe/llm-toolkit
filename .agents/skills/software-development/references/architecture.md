# Architecture

Use the sections relevant to the changed boundaries, while implementing or
reviewing. Establish the intended structure from existing code and decisions;
do not impose a named architecture on a simple script or service.

## Applying the guidance

For implementation, trace the affected responsibility, inputs, outputs, and
external mechanisms before choosing where code belongs. Keep business policy
at the boundary that owns it. Add a port or adapter when it protects a real
boundary, not simply to give each class an interface.

For review, map dependencies and types crossing the changed boundaries. Explain
concrete consequences and distinguish intentional coupling from accidental
leakage. Avoid architectural scores and mandated layer counts.

For a significant decision that needs a durable rationale, use the repository's
ADR process. An architectural observation alone does not require a new record.

### Dependency direction

Look for dependencies from domain/application policy toward UI, persistence, transport, frameworks, infrastructure, or vendor libraries. Distinguish runtime control flow from source-code dependency direction; these can legitimately point in opposite directions when dependency inversion is used.

### Boundary purity

At architectural boundaries, inspect the types crossing the boundary. Flag framework-generated or persistence-shaped types entering inner logic when this couples the inner logic to an outer mechanism.

### Ports and adapters

Identify inbound and outbound ports when they exist. Note whether multiple external mechanisms implement the same boundary, whether an adapter is performing business logic, and whether an interface exists solely for mechanical indirection without an evident boundary or variation.

### Core cohesion

Look for business policy mixed with mechanism. Examples include SQL embedded in domain rules, HTTP concerns in use-case logic, UI formatting in domain objects, or vendor SDK concepts propagated through the core.

### Infrastructure isolation

Check whether databases, queues, filesystems, network clients, clocks, random generators, OS services, and frameworks are isolated from policy code when the system's structure suggests they are intended to be external mechanisms.

### Test architecture

Use tests as evidence of boundaries. Note whether core behavior can be exercised without infrastructure, and whether infrastructure-specific tests are concentrated near the adapters that require them.

## Source principles

Use these sources when a finding depends on the meaning of a named architecture.
They inform judgment; the project's intended boundaries determine applicability.

- [Jeffrey Palermo: Onion Architecture, part 1](https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/):
  dependencies toward the core, infrastructure outside; contextual suitability
  for long-lived applications with complex business behavior.
- [Alistair Cockburn: Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture):
  ports express application interactions and adapters connect external technology;
  application behavior can be exercised independently of devices and databases.
- [Robert C. Martin: Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html):
  source dependencies point toward policy; boundary data should suit the inner
  side rather than exposing an outer mechanism.

Source dependency direction can differ from runtime control flow. None of these
principles requires a particular directory naming convention or an interface for
every class.
