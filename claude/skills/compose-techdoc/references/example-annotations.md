# Annotated Excerpts

Short excerpts (paraphrase-light, trimmed) from "Embedded Logging Architecture Proposal" with notes on what to imitate. The full source is a Google Doc; ask David for the link if you need to re-read it.

---

## Scope: one tight paragraph

> This proposal presents a comprehensive architecture for standardized, reliable and efficient engineering-centric logging across all embedded nodes within a Skip robot. It covers log capture, retention, and egress via local real-time, local retained, and cloud upload channels.

**Notes**: Two sentences. The first names the thing and its qualities; the second enumerates coverage. No history, no pitch.

---

## Status quo: factual, linked, follows the data path

> Skip firmware uses the redirect mechanism, formatting messages via newlib's vprintf function into a temporary buffer. That temporary buffer is submitted in one call to the UART driver, which copies it to an internal driver-managed ring buffer. If the internal ring buffer overflows, excess characters are silently dropped. The UART ISR shifts data byte by byte from the internal buffer into the hardware peripheral.

**Notes**: Traces the actual path buffer by buffer, including the failure behavior (silent drop). Each sentence has the component as subject. Claims about third-party behavior are linked to docs/source in the original.

## Status quo: from facts to inadequacy

> The status quo inadequately addresses current and future needs of the Skip engineering team. Common development scenarios do not accommodate the physical wired connection required to observe messages transmitted UART. No retain/recall functionality is available to compensate. … Synchronous interpolation can impact timing and performance, of particular concern in latency-sensitive code such as ISRs. This compromises the applicable scope for logging.

**Notes**: Thesis sentence, then each deficiency tied to a consequence. (Proofreading catch for future drafts: "transmitted UART" is missing "over".)

---

## Goals: ranked, verifiable, context-qualified

> The proposed logging framework architecture explicitly aims to achieve the following goals, presented in approximate priority order:
> 1. Provide easy-to-use, performant, and safe ad-hoc log entry generation suitable for use in all firmware contexts (application, bootloader, ISR, motor control, etc).
> …
> 4. Provide a superset of status quo logging functionality. Subsume existing logging use without intrusive source code modifications.

**Notes**: Each goal opens with a verb. Priority is stated, not implied. A compatibility goal is explicit.

## Non-goals: boundaries a reader might wrongly assume

> Just as important as understanding what the proposed framework is intended to do is understanding what it is explicitly not intended to do. … Offer any meaningful guarantee of logs availability, format compatibility, and content consistency. All of these are offered strictly on a best-effort basis subject to the needs of the engineering team.

**Notes**: Frames non-goals as load-bearing. States non-guarantees outright.

---

## Disambiguating adjacent concepts

> Telemetry refers to the collection of regular (usually periodic), highly structured data. … Telemetry prioritizes completeness, consistency, uniformity, and efficient extraction, transformation, and loading (ETL). … Logging refers to the collection of ad-hoc, unstructured or loosely structured data, typically in a human readable plaintext format. Logging prioritizes ease of modification …, human consumption, sequential presentation, and wide accessibility.

**Notes**: Parallel construction — same sentence skeleton for both concepts (definition, encoding, priorities, scale, in-house example). Parallelism makes the contrast scannable.

---

## Architectural principle with rationale

> Maintaining a separation between log entry generation and log entry egress also allows each process to optimize toward different objectives. Log generation occurs at many different callsites across a codebase, some with very stringent latency requirements. Thus generation is best optimized for minimal code footprint, maximum run-time speed, maximum context compatibility (e.g. lock-free for ISRs), and developer ergonomics. Log egress is centralized, executes in a predictable, low-demand context, and must support a wide and growing variety of destinations. Egress is best optimized toward maintainability, extensibility, and feature richness.

**Notes**: Claim → facts about each side → derived optimization target for each side ("Thus"). The reasoning is visible, so the reader can disagree with a specific premise.

---

## Tradeoff stated openly

> The tradeoff for using unstructured, plaintext messages is increased complexity on the analysis side. An extra processing step is required to convert plaintext messages into machine-readable quantities for computation or visualization. However, analysis typically occurs on much more capable computing hardware where the additional computational overhead is negligible.

**Notes**: Cost named in the first sentence, quantified qualitatively in the second, mitigated in the third. This three-beat pattern recurs throughout.

## Decision with explicit priority ordering

> This order of precedence allows a single filter setting to guarantee the elision of a wide set of log messages from an image. This gives client projects an easy and reliable mechanism to control code memory footprint, in exchange for a slightly elevated risk of accidentally eliding desired log messages. The consequences for accidentally eliding desired log messages are deemed to be less severe than the consequences for accidentally including undesired log messages and bloating an image.

**Notes**: "in exchange for" marks the cost. The final sentence justifies why this side of the tradeoff was chosen.

## Rule followed by a concrete example

> Applying a severity filter results in all messages having a less severe rating being dropped. For example, applying a severity filter at INFO level results in DEBUG and WILD messages being filtered.

and

> That is, if the global dynamic filter is set to filter at severity DEBUG and the topic dynamic filter is set to filter at INFO, the effective filter setting will be INFO.

---

## Humor, sparingly and with a point

> It is the moral equivalent factoring out a common helper function rather than accepting a bunch of copy-pasta.

> Macro-batics are avoided entirely due to their severely poor readability and maintainability.

**Notes**: One short phrase each, grounded in an engineering analogy. (Proofreading catch: "equivalent of factoring" is missing "of".)

---

## Showing the problem with a real artifact

The Alternatives section includes a genuine, slightly modified firmware `LOG_D` call with ~25 interleaved format specifiers and arguments, introduced by: "Consider the following log call taken from the Skip firmware and slightly modified. The latent defect is nearly impossible to discern."

**Notes**: A real, ugly example is far more persuasive than an abstract claim about error-proneness. Pair it with what tools exist (compiler format attributes) and why the status quo doesn't use them.

---

## Alternative with fair treatment and a verdict

> Both HDLC and COBS offer the property of being self-synchronizing. This means that partial corruption in a LogStream file only affects the entries directly affected. … In contrast, with Delimited Protobuf partial corruption in some cases renders as unrecoverable the directly affected entry and all following entries. For this reason DelimitedProtobuf was rejected.

> COBS guarantees a maximum frame size increase of not more than ~3.1%. This is much better than the maximum frame size increase of up to 100% for HDLC. However, for plaintext strings, HDLC imposes no overhead while COBS adds one byte for every 255 characters (~0.39%). … It is not expected that framing overhead added by HDLC will contribute meaningfully to the size of each encoded LogEntry.

**Notes**: Concedes the competitor's headline advantage ("much better"), then shows it doesn't apply to the actual payload (plaintext-dominated). Numbers throughout. Ends with "For this reason, HDLC is proposed as the initial framing scheme. Future work can add COBS as an alternative should it prove advantageous."

---

## Work planning: criteria first, then phases

> The phase planning attempts to prioritize features according to the following criteria, in order of importance: 1. Urgency of need/prerequisite for other development efforts 2. Minimization of total effort … 3. Resiliency to short- and medium-term reprioritization (e.g. quickly get to "good" intermediate stopping points)

> The MO/GO project could immediately benefit from some type of file transport. This is currently a major limitation that impacts multiple other efforts (ESP-NOW comms debugging, encoder faults, etc). The goal of Phase 1 is to get a functioning basic local-file egress channel as quickly as possible.

**Notes**: Ties each phase to a concrete current pain point, names a goal, and gives an exit condition for later phases ("minimum requisite for post-DVT testing").

---

## What *not* to copy from the example

The source is a working draft. Do not imitate:

- Later-section bullets written as terse fragments where the earlier prose style would better convey rationale (Egress, File Transport).
- Typos and slips (MSPC, HDCL, "shell" → "shall", "a macros", "intern developers", "(newlib-nano?)").
- Empty or `[[TODO]]` sections presented without any outline of intent. A `[[TODO]]` heading is fine; add a one-line statement of what the section will cover.
