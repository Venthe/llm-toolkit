---
name: draw-diagram
description: Create, edit, and review clear, semantically accurate PlantUML diagrams. Use when asked to document architecture, software structure, interactions, workflows, deployment, data models, state transitions, or other processes as PlantUML.
---

# PlantUML Diagram Author

Create PlantUML diagrams that communicate a system or process accurately, at the right level of abstraction, and with enough visual explanation to stand alone.

## Required workflow

1. **Establish intent and scope.** Determine the question the diagram must answer, the intended audience, the system boundary, and the level of abstraction. Prefer evidence from the repository and supplied requirements over assumptions. Ask a focused question only when a material ambiguity prevents an accurate diagram; otherwise make the smallest reasonable assumption and state it.
2. **Use domain language.** Inspect relevant project documentation and existing diagrams. If `GLOSSARY.md` exists, read it and use its terms consistently. Prefer the domain's established names over implementation details unless implementation is the diagram's subject. Do not invent components, technologies, protocols, or behavior. Mark uncertain details as assumptions or keep them generic.
3. **Choose the diagram type intentionally.** Use the type that answers the question with the least notation overhead. Examples: sequence for ordered interactions; component for logical software building blocks and dependencies; deployment for runtime nodes and placement; class for static types and associations; activity for workflows and decisions; state for lifecycle transitions; use-case for actor goals; entity-relationship for data relationships. Consult `references/PlantUML_Documentation_Reference.md` and its official links for syntax and supported diagram types.
4. **Write the source.** Produce plain-text PlantUML source, with balanced blocks and explicit aliases for stable identifiers. Keep the diagram focused; split it when it mixes unrelated concerns or becomes difficult to scan.
5. **Apply the diagram readability rules.** Follow the rules below, including a title, explicit scope, named elements, labelled relationships, and a legend.
6. **Validate.** If a PlantUML renderer or CLI is available, render the diagram and inspect the output. Prefer syntax validation followed by rendering. Fix syntax errors, collisions, misleading layout, unreadable labels, and unexpected line crossings. If rendering cannot be performed, state that the source was not rendered and do not claim validation succeeded.
7. **Run the checklist.** Complete the checklist at the end of this file against the finished diagram. Resolve every “No” that indicates a defect. If an item truly does not apply, simplify the diagram to avoid the unused visual encoding where practical and record why it is not applicable instead of implying it was verified.
8. **Deliver the source.** Return the complete `.puml` source or save it at the requested path. Include rendered output only when requested or useful and available. Briefly note material assumptions and whether the diagram was rendered/validated.

## Diagram rules

### General

- Every diagram **must have a meaningful title**. The title should identify the subject and, when useful, the viewpoint.
- Make the **diagram type** understandable from its standard notation and title. If the type could be confused with another type, state it in the title or a small subtitle.
- Make the **scope explicit**. State the boundary, actors, time window, environment, or level of abstraction that is included. Use the title's second line or a concise note when necessary.
- Include a **legend/key in every diagram**. Keep it compact. Explain custom colors, shapes, stereotypes, icons, line styles, arrowheads, sizes, and abbreviations. When using only standard notation, say so and explain the non-obvious conventions that matter.
- Use one diagram for one primary purpose. Avoid mixing context, container, component, class, deployment, and detailed interaction views into one unreadable picture.
- Prefer a simple, consistent layout over manual direction hints. Use `left to right direction` when it materially improves reading order; do not over-constrain placement.
- Do not use color or styling decoratively. Every non-default visual encoding must carry a clear and documented meaning. If it has no semantic purpose, remove it.
- Expand acronyms at first use or in the legend. Avoid ambiguous abbreviations.

### Elements

- Give every meaningful element a clear, unique visible name. Use aliases for stable identifiers, not as a substitute for readable labels. Standard UML pseudostates, such as initial/final markers, do not need artificial names.
- Make the **kind and abstraction level** clear: e.g. person, external system, service, component, container, process, data store, class, event, or state. Use stereotypes or concise secondary labels where necessary.
- Describe each element's responsibility with a short label or note when the responsibility is not obvious from its name.
- Show technology choices only when known and relevant. Distinguish a logical role from its implementation, e.g. `Order store\n[PostgreSQL]`. Never infer a specific technology from a generic role.
- Explain every acronym, color, shape, icon, border style, and non-standard size. Prefer standard, widely understood notation. Do not encode meaning through size unless the sizing rule is stated in the legend.
- Keep labels readable and concise. Avoid paragraph-length element names; use notes for detail.

### Relationships

- Label every meaningful relationship line with its intent. Use verbs or concise phrases such as `publishes event`, `reads`, `calls`, `owns`, `contains`, `replicates`, or `transitions when`. For sequence diagrams, the message text itself is the relationship label.
- Where relevant and known, document the relationship's technology, protocol, or mechanism, such as `HTTPS`, `gRPC`, `AMQP`, or `SQL`. Do not invent a protocol to fill a label.
- Make arrowheads unambiguous. Use the correct notation for dependency, inheritance, composition, aggregation, message flow, response, or state transition. Explain non-obvious arrowheads in the legend.
- Use solid, dashed, dotted, and colored lines consistently. If line appearance carries meaning, define it in the legend. Do not use a dashed line merely for visual variety.
- Avoid crossing lines where possible. Re-route, group, or split the diagram rather than making relationships ambiguous.
- Expand acronyms in relationship labels or the legend.

## PlantUML source conventions

- Start and end each ordinary diagram with `@startuml` and `@enduml`.
- Include `title` and `legend`; keep all `if`/`endif`, `alt`/`end`, `group`/`end`, and other paired constructs balanced.
- Prefer explicit declarations and readable aliases when they improve clarity:

  ```plantuml
  @startuml
  title Checkout request flow\nScope: synchronous payment authorization

  actor "Customer" as customer
  participant "Checkout API" as checkout
  participant "Payment provider" as payment

  customer -> checkout : Submit checkout
  checkout -> payment : Authorize payment (HTTPS)
  payment --> checkout : Authorization result
  checkout --> customer : Checkout outcome

  legend bottom
    Solid arrow: request or command
    Dashed arrow: response/result
    HTTPS: Hypertext Transfer Protocol Secure
  endlegend
  @enduml
  ```

- Use stable aliases for source references, but use human-readable visible names. Avoid duplicate aliases and unexplained stereotypes.
- Prefer standard, monochrome notation unless color materially improves comprehension. If using colors, icons, line styles, shapes, or relative sizes to convey meaning, define each mapping in the legend.
- Avoid external images/icons or remote includes unless the user requests them and they are available and safe to depend on. Prefer source that renders in the user's likely environment.
- Do not use a PlantUML feature solely because it is available. Use it only when it makes the diagram more precise or readable.

## Rendering and validation

When command-line access is available, validate and render the source with the installed PlantUML version. A typical invocation is:

```sh
java -jar plantuml.jar --check-syntax diagram.puml
java -jar plantuml.jar -tsvg diagram.puml
```

Use the actual project toolchain if it has a configured renderer. If syntax-checking flags differ by installed version, consult the official command-line documentation linked from the reference file. Inspect the rendered diagram, not only the source. If tools are unavailable, review syntax manually and label validation status accurately.

## Final quality checklist

For each question, select **Yes** or **No** based on the completed diagram. Do not mark “Yes” merely because a property could be inferred by its author. Fix defects before delivery; use the notes column to explain a genuine non-applicable case.

### General

| Review question | Yes | No | Notes |
|---|:---:|:---:|---|
| Does the diagram have a title? | [ ] | [ ] | |
| Do you understand what the diagram type is? | [ ] | [ ] | |
| Do you understand what the diagram scope is? | [ ] | [ ] | |
| Does the diagram have a key/legend? | [ ] | [ ] | |

### Elements

| Review question | Yes | No | Notes |
|---|:---:|:---:|---|
| Does every element have a name? | [ ] | [ ] | Standard UML pseudostates are exempt. |
| Do you understand the type of every element (i.e. the level of abstraction, such as software system, container, or component)? | [ ] | [ ] | |
| Do you understand what every element does? | [ ] | [ ] | |
| Where applicable, do you understand the technology choices associated with every element? | [ ] | [ ] | |
| Do you understand the meaning of all acronyms and abbreviations used? | [ ] | [ ] | |
| Do you understand the meaning of all colours used? | [ ] | [ ] | |
| Do you understand the meaning of all shapes used? | [ ] | [ ] | |
| Do you understand the meaning of all icons used? | [ ] | [ ] | |
| Do you understand the meaning of all border styles used (e.g. solid, dashed)? | [ ] | [ ] | |
| Do you understand the meaning of all element sizes used (e.g. small vs. large boxes)? | [ ] | [ ] | |

### Relationships

| Review question | Yes | No | Notes |
|---|:---:|:---:|---|
| Does every line have a label describing the intent of that relationship? | [ ] | [ ] | For sequence diagrams, the message text is the label. |
| Where applicable, do you understand the technology choices associated with every relationship (e.g. protocols for inter-process communication)? | [ ] | [ ] | |
| Do you understand the meaning of all acronyms and abbreviations used? | [ ] | [ ] | |
| Do you understand the meaning of all colours used? | [ ] | [ ] | |
| Do you understand the meaning of all arrowheads used? | [ ] | [ ] | |
| Do you understand the meaning of all line styles used (e.g. solid, dashed)? | [ ] | [ ] | |

## Reference files

Read `references/PlantUML_Documentation_Reference.md` for an offline quick reference and links to the official PlantUML documentation. Use the official guide for detailed or version-specific syntax questions.
