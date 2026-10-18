# Twelve-Factor baseline

Use the [original Twelve-Factor methodology](https://12factor.net/) as a lens for
service applications. The following condensed questions map its twelve concerns;
they are not a requirement that every workload adopt the same topology.

| Factor | Assessment question |
| --- | --- |
| Codebase | Can each deployed application be traced to versioned source? |
| Dependencies | Are required libraries and runtime dependencies explicitly declared? |
| Config | Can deployment-specific settings change without editing application code? |
| Backing services | Are external resources accessed through configurable connections? |
| Build, release, run | Can a built artifact be promoted into an identifiable release? |
| Processes | Does durable state survive loss of an application process? |
| Port binding | Does a serving process expose an explicit network interface? |
| Concurrency | Can workload types scale according to demand? |
| Disposability | Does startup and termination behavior support replacement? |
| Dev/prod parity | Are consequential environment differences controlled? |
| Logs | Can the platform collect application events? |
| Admin processes | Are maintenance operations versioned and reproducible? |

Inspect artifacts and behavior for the relevant question. Record unmet needs and
deliberate exceptions rather than awarding a compliance score. Use
[modern interpretations](modern-interpretations.md) when translating these ideas
to today's runtime and delivery choices.
