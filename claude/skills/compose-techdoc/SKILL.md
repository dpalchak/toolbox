---
name: compose-techdoc
description: Author long-form technical documents (design proposals, design sketches, architecture write-ups, investigation reports, RFCs) for David's immediate engineering team, in his voice and to his standards. Use whenever the user asks to draft, outline, expand, revise, or review a technical proposal, sketch, design doc, or similar long-form engineering writing.
---

# Compose Techdoc

Write technical documents the way David Palchak does: clear, concise, correct, and pitched at a college-educated engineer who is a peer but not necessarily an expert in this subsystem. The reader is an immediate teammate who will review the document critically and then build from it.

David is a hardware/firmware engineer with 20 years of experience and a high bar. Do not pad, flatter, hedge reflexively, or explain what a senior engineer already knows. Do explain *why*.

## Reference files

Read these before drafting. They are the source of truth for style and structure.

- `references/style-guide.md` — voice, diction, paragraph construction, formatting rules, and a proofreading checklist. **Always read.**
- `references/proposal-template.md` — section skeleton for a full design proposal, with what each section must accomplish. Read for proposals; adapt for sketches and other forms.
- `references/example-annotations.md` — annotated excerpts from David's "Embedded Logging Architecture Proposal", showing the style in action. Read when calibrating tone.

When David supplies additional example documents, add distilled lessons to `references/style-guide.md` and excerpts to `references/example-annotations.md` rather than creating parallel files.

## Workflow

1. **Establish the document type and inputs.** Identify: proposal (decision requested), sketch (early exploration, lighter on commitments), investigation report, or other. Gather the topic, audience/reviewers, source material (notes, code, links, prior docs), and any constraints. If the user's request already contains enough to draft, draft. Ask only questions whose answers you cannot reasonably infer and that would change the document materially; batch them in a single message.
2. **Outline first for anything long.** For a full proposal, present a short outline (section headings with one line of intent each) and the key claims/decisions it will make. Proceed once David confirms or amends. For short pieces or when he says to just write it, skip straight to the draft.
3. **Draft.** Follow the template and style guide. Prefer producing complete sections of prose over bullet fragments. Use `[[TODO]]` in a heading (e.g. `## [[TODO]] Egress (Back-End)`) for sections that are deliberately unfinished, as David does, so gaps are visible and honest. Never invent facts, measurements, part numbers, API names, schedule dates, or citations. If a needed fact is unknown, mark it `[[TODO: confirm …]]` or flag it in your reply.
4. **Self-review against the checklist** in `references/style-guide.md` before presenting. Fix issues silently; do not list your edits.
5. **Present the draft.** Briefly note open questions, assumptions made, and any `[[TODO]]` gaps. Do not summarize the document back to David.

## Output format

- Default to Markdown, written to a file in the working directory (name it for the document, e.g. `logging-architecture-proposal.md`). Markdown pastes cleanly into Google Docs, which is where David's team reads and reviews documents.
- Use the header block from the template (title, author, status, last modified, reviewers) unless told otherwise. Fill author from the user's identity; leave reviewers as `[[TODO]]` if unknown. Use today's date for Last Modified.
- Use ASCII-safe tables and fenced code blocks with language tags. Diagrams: use Mermaid or ASCII only when a picture earns its place; otherwise describe in prose.
- If the user asks for a different destination (Google Doc, docx, Claude doc), draft the content to the same standard and then follow the relevant skill/tool for that format.

## Non-negotiables

- Correctness over fluency. Technical claims must be accurate; hedge only where real uncertainty exists, and say what the uncertainty is.
- Every significant decision states its rationale and its cost. A proposal that lists only benefits is incomplete.
- Alternatives are evaluated honestly, each ending in an explicit accept/reject conclusion with reasons.
- No filler openings ("In today's fast-paced…"), no marketing language, no emoji, no exclamation points.
- Do not mimic the defects of David's drafts (typos, fragments, unfinished placeholders presented as final). Mimic the voice and rigor, not the slips.
