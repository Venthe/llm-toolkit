# Kubernetes workload recommendations

Use for a concrete Kubernetes workload or platform proposal. Establish cluster
version, workload/controller type, namespace, network/storage implementations,
policy constraints, and service objectives. Check documentation for that
version; do not assume a feature from the current website is enabled on the
target cluster.

## Configuration and delivery

Inspect the rendered configuration as well as chart/template inputs. Prefer
versioned declarative configuration and identifiable artifacts; assess drift and
rollback through the project's delivery process. Do not apply manifests during
an assessment. Rendering, local validation, server-side dry runs, and live tests
provide different evidence and have different access/side-effect requirements.
See
[configuration guidance](https://kubernetes.io/blog/2025/11/25/configuration-good-practices/).

## Health and lifecycle

- Readiness controls suitability for Service traffic; failure does not itself
  restart the container. Liveness should identify a condition a restart can
  repair.
- Startup probes can protect slow initialization before ordinary health checks
  begin. Choose thresholds from observed startup and failure behavior.
- Avoid making a shared dependency outage restart every application instance.
  Evaluate dependency checks in readiness according to actual serving capability
  and the effect of removing all replicas from traffic.
- Probe success is evidence of the checked condition, not end-to-end
  correctness.

See
[probe semantics](https://kubernetes.io/docs/concepts/workloads/pods/probes/).

Coordinate termination signals, in-flight requests, consumer shutdown, endpoint
propagation, and the grace period. A preStop hook consumes the termination
budget; it does not provide an independent unlimited delay. Verify behavior
during rollout and termination rather than assuming a fixed sleep drains
traffic. See
[Pod lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/).

## Capacity and scaling

Base requests and limits on observed demand and service objectives. Requests
affect scheduling; CPU limits can throttle, while memory pressure/limits can
lead to termination. Assess runtime overhead, startup spikes, and ephemeral
storage. Do not prescribe identical request/limit values or fixed numbers for
every service. Explain relevant autoscaling signals and prerequisites; more
replicas may overload a database instead of increasing useful throughput. See
[resource management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).

## Availability and data

Assess replicas, failure-domain placement, rollout strategy, and spare capacity
together. PodDisruptionBudgets constrain supported voluntary evictions; they do
not prevent node failures or substitute for workload-controller rollout
settings. Overly restrictive budgets can obstruct maintenance. Validate behavior
against the service's actual availability needs. See
[disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/).

For durable data, establish storage failure modes, recovery objectives, and an
exercised restoration path. A StatefulSet or persistent volume alone is not a
backup or disaster-recovery plan. Treat migration ownership and compatibility
across old/new application replicas as part of the rollout design.

## Security and operability

Assess least-privilege RBAC, service-account token use, non-root execution,
capabilities, privileged/host access, and supported security profiles. Select
controls compatible with the actual workload and cluster policy.

Kubernetes Secret encoding is not encryption. Check storage/access protection,
rotation, and accidental disclosure through manifests or diagnostics.
NetworkPolicy requires an enforcing network implementation; namespace separation
alone is not proof of traffic isolation. Inspect image provenance/update
practices and avoid unnecessary public exposure. See the
[security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/).

Identify operational owners, actionable telemetry, alerts tied to user impact,
and recovery procedures. Recommend failure exercises and load checks in an
authorized isolated environment; do not execute them against a shared cluster
merely to substantiate a recommendation. Report absent evidence as a gap rather
than asserting the production system has no control.
