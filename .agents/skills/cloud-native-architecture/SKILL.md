---
name: cloud-native-architecture
description: >-
  Assess and recommend application delivery and runtime architecture using
  Twelve-Factor principles, modern reinterpretations, and Kubernetes workload
  practices. Use for architecture/DevOps recommendations, production-readiness
  assessments, or deployment design; routine container commands belong in
  container-workflow.
---

# Cloud-native architecture recommendations

Recommend changes that address demonstrated delivery or operational needs.
Explain benefits, costs, applicability, and uncertainty; do not score pattern
compliance or assume Kubernetes, microservices, or a platform migration is the
desired outcome.

## Establish the context

1. Identify the decision or assessment scope, application boundaries, workload,
   deployment model, backing services, and operational ownership.
2. Inspect relevant architecture records, build/release configuration,
   manifests, charts, application lifecycle code, and available operational
   evidence. Treat desired manifests and observed runtime state as different
   evidence.
3. Establish known availability, latency, recovery, security, cost, and team
   constraints. Do not invent targets or block a useful assessment on every
   unknown.
4. Confirm deployed platform versions and enabled features where they matter.
   Discover actual runtime/MCP capabilities if runtime evidence is needed. Use
   scoped read-only inspection; recommendations alone do not authorize
   deployment, migrations, cluster changes, restarts, or external
   communications.

## Select references

| Reference                                                      | When to read                                                                                     |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| [Twelve-Factor baseline](references/twelve-factor.md)          | Assessing application packaging, configuration, process model, and delivery                      |
| [Modern interpretations](references/modern-interpretations.md) | Applying the baseline to monorepos, secret management, observability, APIs, and modern platforms |
| [Kubernetes workloads](references/kubernetes.md)               | Kubernetes is deployed or is a concrete option under consideration                               |

Read only the topics relevant to the decision. For code-boundary design, consult
[development architecture](../software-development/references/architecture.md).
For actual Docker/Podman operations use
[container-workflow](../container-workflow/SKILL.md). For an unexplained failure
use [software-debugging](../software-debugging/SKILL.md). These links do not
require loading every companion skill for an assessment.

## Assessment and recommendations

1. Describe observed behavior and its evidence before suggesting a change.
2. Explain the failure mode or constraint the recommendation addresses. Identify
   whether the application, delivery pipeline, platform, or operating practice
   owns it.
3. Compare reasonable options, including retaining the current approach.
   Recommend a preferred option when evidence supports it; state its assumptions
   and tradeoffs.
4. Prioritize by likely impact, urgency, effort, and dependencies. Separate
   immediate corrections from experiments and longer-term proposals; avoid false
   precision.
5. Define how each recommendation would be verified: observable success
   criteria, relevant tests or measurements, rollout/rollback considerations,
   and ownership if known. Planning a check is not evidence it passed.
6. If a durable decision record is requested, use [adr](../write-adr/SKILL.md).
   If implementation is requested, apply the development and testing workflows
   within that scope; preserve deployment authorization boundaries.

## Output

Return scope and evidence limits, prioritized recommendations, and material open
decisions. Each actionable recommendation includes its location/evidence,
problem, suggested change, benefit, costs/risks, and verification approach. Say
when the current design is sufficient. Do not produce an exhaustive checklist
for a narrow question or turn a missing artifact into proof that a control does
not exist.

Use current primary documentation for version-sensitive recommendations. The
bundled references are decision aids, not replacements for the target platform's
supported APIs and operational policies.
