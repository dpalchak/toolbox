# Style Guide: David Palchak Technical Writing

Derived from "Embedded Logging Architecture Proposal" (Nov 2026). Update as more examples are supplied.

## 1. Voice

- **Impersonal, declarative, present tense.** The document describes the design as a thing that exists: "The front-end applies both global and per-topic filtering." "This proposal presents…" Use future tense only for genuinely future work ("Future work may include…") and conditional/expected-evolution statements ("The format of the entry data objects is expected to evolve").
- **No first person.** No "I think", "we believe", "let's". Occasionally the passive is used to keep the subject on the system or decision ("Macros are used here to provide a convenient seam for indirection.", "…were rejected."). Prefer active voice with the component as subject; use passive when the actor is irrelevant.
- **Calm and exact.** Confident where the reasoning supports it, plainly tentative where it doesn't ("It is expected that…", "The consequences … are deemed to be less severe…"). Never breathless, never salesy.
- **Dry, sparing humor.** Rare, brief, and always carrying a point: "the moral equivalent of factoring out a common helper function rather than accepting a bunch of copy-pasta"; "Macro-batics are avoided entirely due to their severely poor readability and maintainability." At most one or two per document. None in the Scope or Goals sections.
- **Direct opinions, argued.** Strong judgments ("severely poor readability", "inadequately addresses") are fine when immediately backed by specifics.

## 2. Diction

- **Precise technical vocabulary**, used consistently. Pick one term per concept and hold it for the whole document (front-end / middle-end / back-end; egress handler; entry). Do not vary terms for elegance.
- **Introduce coined or overloaded terms in quotes at first use**, with a definition: `a third, pseudo-subprocess, called the "middle-end"`. Alternate names are given with "aka": `legacy-style (aka C-style or printf-style) format strings`.
- **Glosses via "i.e." and examples via "e.g."**, usually parenthetical. Use them correctly: *i.e.* restates ("Infaux (i.e. STM32H7-based ML coprocessor)"), *e.g.* exemplifies ("destinations (e.g. UART transport, BLE transport, non-volatile storage)").
- **Name the real thing**: specific MCUs, libraries, standards, functions, file names, header fields, protocol names, with links to the authoritative source (datasheet, docs, source line) where they back a claim.
- **Quantify when possible**: "100M+ records from 10M+ devices", "one byte for every 255 characters (~0.39%)", "up to 100%". When a number is an estimate, say so.
- **Comparative framing**: "Contrast this with…", "In contrast, …", "Just as important as … is …". Defining a thing by what it is not is a signature move (Goals / Non-goals; telemetry vs logging).
- **Words and constructions David favors**: "comprises", "elided" (code removed), "seam", "salient", "in exchange for", "subsume", "superset", "best-effort", "in all circumstances", "that is,", "Thus", "Likewise", "Similarly", "Finally,". Use naturally, not as a checklist.
- **Avoid**: "leverage", "utilize" (use "use"), "robust" and "seamless" as empty praise, "very" as an intensifier without cause, "simply" when the thing isn't simple, "basically", "obviously", "just" as a softener, rhetorical questions, and exclamation points.
- **Audience level**: college-educated engineer. Define domain jargon outside embedded/firmware norms; do not define standard CS/EE concepts (ISR, mutex, ring buffer, protobuf) unless the specific usage is non-obvious. Expand an acronym once at first use unless it is universally known to the team.

## 3. Paragraph construction

- **Topic sentence first**, stating the point of the paragraph. Supporting sentences give mechanism, then consequence.
- **Typical paragraph: 3–6 sentences.** One idea per paragraph. Break rather than sprawl.
- **Move from what to why to tradeoff.** The recurring arc: state the design choice → give the advantages → state the cost honestly ("The tradeoff for using unstructured, plaintext messages is increased complexity on the analysis side.") → explain why the cost is acceptable ("However, analysis typically occurs on much more capable hardware where the overhead is negligible.").
- **Make priorities explicit.** When a decision resolves a conflict, say which side wins and why: "The consequences for accidentally eliding desired log messages are deemed to be less severe than the consequences for accidentally including undesired log messages and bloating an image."
- **Worked examples after rules.** State the rule, then a one-sentence concrete instance: "For example, applying a severity filter at INFO level results in DEBUG and WILD messages being filtered."
- **Close alternatives with a verdict.** Each rejected alternative ends in a sentence of the form "For these reasons, X was rejected." / "For this reason, Y is proposed as the initial scheme."
- **Prefer prose for reasoning; bullets for enumerations.** Rationale, tradeoffs, and mechanism belong in paragraphs. Use bullets for parallel items: responsibilities, formats, properties, option lists. Avoid long runs of terse sentence-fragment bullets for anything that needs justification (a weakness in some of David's later sections).

## 4. Document-level conventions

- **Header block**: title; a table with Author(s), Status (e.g. Draft / Review / Approved), Last Modified, Reviewer(s).
- **Scope** opens the document: one tight paragraph stating what the document covers.
- **Motivation** precedes design: status quo (with a date, "As of October 2026"), why it is inadequate, then Goals and Non-goals.
- **Goals are numbered and stated "in approximate priority order."** Non-goals are numbered and framed as important boundaries.
- **Disambiguate neighboring concepts** explicitly in a short section when readers might conflate them (e.g. "Relationship to Other Data Collection").
- **Tables** summarize multi-dimensional facts (filter scopes, phase plans). Always introduce with a sentence ("The following table summarizes…"). Bold column headers.
- **Code and formats** are shown as small, concrete snippets: struct definitions, API macros, file headers, schemas, example log lines. Keep them minimal and illustrative; longer reference code goes in an Appendix with a note that it is illustrative and not feature-complete.
- **User journeys** show how a real engineer uses the system end to end, each with a short motivating paragraph, a snippet, and what happens next.
- **Phased work plans** state their prioritization criteria in order, give a summary table (phase / feature / component), then a short paragraph per phase on goal and exit condition.
- **Alternatives Considered**: one subsection per alternative; define it, state its real advantages fairly, then the drawbacks in this context, then the verdict.
- **Future Work** captures things deliberately deferred, with enough detail to show the design anticipates them and does not foreclose them.
- **References** and **Appendix** at the end. Link external claims inline at the point of use.
- **Unfinished sections** are marked `[[TODO]]` in the heading. Do not leave an empty section unmarked.
- **Headings**: Title Case. H1 for major sections, H2 for components, H3 for topics. Keep headings short and noun-phrase-like (Scope, Motivation, Filter Precedence). Do not number headings.
- **Formatting inline**: backticks for identifiers, filenames, macros, and literal values; quotes for introduced terms and informal names ("snapshots", "debug logs"). Avoid bold in running prose except table headers and rare key terms.

## 5. Length and density

- Length follows the decision's complexity, not a template. A sketch may be 1–3 pages; a full architecture proposal may be 10–20+.
- Every sentence should carry information. Cut throat-clearing, restatement, and anything the reviewer would skim.
- Do not repeat the same justification in multiple sections; state it once and cross-reference ("As previously mentioned…", "See section below…").
- Prefer one clear example over three similar ones.

## 6. Correctness and rigor

- Technical statements must be verifiable. Check: units, orders of magnitude, direction of inequalities, which component owns which responsibility, consistency between code snippets and prose.
- Names in prose must match names in code and diagrams exactly.
- Do not claim guarantees the design does not provide; state non-guarantees explicitly (as in the "best-effort" non-goal).
- Where the author has not decided or verified something, say so, rather than smoothing it over.
- Cite external behavior with a link to docs or source when it supports a claim about the status quo or a third-party component.

## 7. Proofreading checklist (run before presenting)

Observed defects in earlier drafts — actively guard against them:

1. **Typos in technical acronyms and names** (e.g. "MSPC" vs MPSC, "HDCL" vs HDLC, "shall" vs shell). Verify every acronym and identifier against its first definition.
2. **Sentence fragments and run-ons** in prose (e.g. "Alternative options exist for framing … Common options for framing.").
3. **Wrong word / agreement** ("a macros", "featured development" for feature development, "intern developers" where "internal" was meant, "each are").
4. **Leftover drafting notes** such as "(newlib-nano?)" or duplicated words. Resolve or convert to explicit `[[TODO: …]]`.
5. **Inconsistent terms** for one concept; inconsistent capitalization of component names.
6. **Unmatched claims**: every "as previously mentioned" and "see below" points at something real.
7. **Unsupported superlatives**: replace with a specific reason or a number.
8. **Orphaned tradeoffs**: every decision lists a cost; every cost has an answer or an acknowledgement.
9. **Lists with mixed grammar**: make parallel items grammatically parallel.
10. **Tables and snippets** are introduced by a sentence and are consistent with the prose.
