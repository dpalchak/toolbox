# Design Proposal Template

Adapt freely. Omit sections that do not apply; do not pad. For a **design sketch**, keep Scope, Motivation (short), Goals/Non-goals, the core design, Alternatives, and Open Questions, and state clearly that commitments are provisional.

```markdown
# Design Proposal

# <Descriptive Title in Title Case>

---

| | |
| :-: | :-: |
| Author(s): | [Name](mailto:...) |
| Status: | Draft \| Review \| Approved \| Superseded |
| Last Modified: | <Mon D, YYYY> |
| Reviewer(s): | [Name](mailto:...) ... |

---

# Scope
# Motivation
## Status Quo (As of <Month YYYY>)
## Goals
## Non-goals
## Relationship to <Neighboring Concept>   (only if confusion is likely)
# <Architecture | Design>
## <Component or Concern>
### <Topic>
# Common User Journeys
# Work Planning
# Alternatives Considered
# Future Work
# References
# Appendix
```

## What each section must accomplish

**Scope** — One paragraph. States what the proposal presents and what domains/channels/components it covers. A reader should know in 20 seconds whether the document concerns them. Example shape: "This proposal presents a comprehensive architecture for X across Y. It covers A, B, and C."

**Motivation → Status Quo** — Dated. Describes the current system factually and in enough technical detail (libraries, modes, data paths, links to docs/source) that a reviewer can verify the account. Follows the data path end to end where relevant (who calls what, where buffers live, what happens on overflow). Then a paragraph or more on why this is inadequate for *current and future needs*, each deficiency stated concretely and tied to a consequence (timing impact, defects, missing workflows).

**Goals** — Numbered, "in approximate priority order". Each goal is a verifiable outcome, begins with a verb, and may carry a short clarifying sentence or sub-list. Include the context the goal must hold in (e.g. "all firmware contexts (application, bootloader, ISR, …)"). Include backward-compatibility and future-growth goals if relevant.

**Non-goals** — Numbered. Preface: "Just as important as understanding what the proposed framework is intended to do is understanding what it is explicitly not intended to do." Each non-goal is something a reasonable reader might assume is in scope: guarantees not offered, adjacent systems not replaced, languages/platforms not supported.

**Relationship to Other X** — Defines the broad term, splits it into the categories in play, and characterizes each by what it prioritizes, its typical encoding, its scale of analysis, and an in-house example. Ends with a clear boundary.

**Architecture / Design** — Opens with the organizing principle (e.g. separation of concerns) and the reason for it. Then one section per component, each with: *Responsibilities* (what it does and does not do), the key data structures/API (small code snippet), the design decisions with rationale and tradeoffs, and interactions with neighboring components. Constraints from the execution environment (ISR-safe, lock-free, memory limits, timing) are stated explicitly where they drive the design. Summarize multi-dimensional rules (e.g. which property is used in which scope) in a table.

**Common User Journeys** — 2–4 concrete scenarios, each titled by the user's intent ("Track Control Flow", "Visualize Quantities in PlotJuggler"). Each: a motivating paragraph, a minimal code or command example, and an explanation of how the surrounding tooling completes the task.

**Work Planning** — Explains why the work is phased. States prioritization criteria in order. Summary table of Phase / Feature / Component. Then a short subsection per phase: its goal, what need it serves, and the exit condition ("Completion of phase 2 should be considered the minimum requisite for post-DVT testing").

**Alternatives Considered** — One subsection per serious alternative. Define the alternative fairly (including how the status quo or other systems use it), steelman its advantages, give the concrete drawbacks in this context (with examples or numbers), and end with an explicit verdict sentence. Include sub-alternatives for lower-level choices (framing, encoding, etc.).

**Future Work** — Deferred items the architecture anticipates. For each: what it is, how the current design accommodates it, and what is explicitly out of scope now.

**References** — Links to prior design pages, tickets, specs, datasheets, standards.

**Appendix** — Reference implementations or long snippets. Preface each with what it is and is not ("not intended to be a feature-complete, fully functional script"), and note any format assumptions subject to change.

## Status and metadata conventions

- Status progression: Draft → Review → Approved (→ Superseded). Update Last Modified on every revision.
- Reviewers are named with email links; ask the user who they are if unknown, else use `[[TODO]]`.
- Unfinished sections: add `[[TODO]]` to the heading text.
