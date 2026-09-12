# Research Documentation Flow Protocol

Paths below are relative to the target project root. Read this protocol when using a `research-*` skill from this template.

## Scope and Evidence

Use the user's language for conversation and runtime notes. At a meaningful change of activity, briefly state what is being done, whether it is read-only or will write a research artifact, and whether it stays in the main session or is delegated. This is a coordination notice, not an extra approval gate.

Start from the research question and intended use. Establish the decision, reader, date boundary, jurisdiction or system boundary when relevant, and the needed confidence before expanding collection. A broad topic is not yet a researchable question; propose a narrower first question when necessary.

Keep three layers distinct:

- `source claim`: what a source actually states, with enough location context to re-find it.
- `analysis`: an interpretation, comparison, calculation, or inference based on stated evidence.
- `decision`: the user's or project's chosen action, preference, or open direction.

Use direct quotations only when their exact wording matters and preserve context. Otherwise paraphrase faithfully. Never invent a source, locator, access result, quotation, consensus, or citation. Mark missing, conflicting, stale, paywalled, second-hand, or unverified material explicitly. A link alone is often insufficient: record a page, section, figure, timestamp, commit, row range, or other useful locator when the source permits it.

## Cognitive Pace

A complete-looking state file does not prove that the user understands the research. When a data choice, transformation, experiment result, key inference, or decision will constrain later work, create a short cognitive checkpoint: what is believed, why, which evidence or artifacts support it, what would invalidate it, and whether the user marks their understanding `confirmed`, `pending`, or `revisit`.

`pending` and `revisit` are cognitive debt, not failure. Keep them specific enough to study: for example, "cannot explain why this filter is needed" rather than "needs more reading." The agent may continue authorized low-risk exploration, but must not present an unconfirmed checkpoint as the user's settled understanding. It should surface relevant debt before work that relies on it.

For a long pause or when the user asks to review, use active recall before explanation when useful. Ask a small set of questions based on the actual question, evidence, and derivation chain. Include basic object-level questions when the user is early in a topic, then move through causal reasoning, scope boundaries, downstream dependencies, and counterfactuals as appropriate. After the user responds, correct against actual evidence and artifacts; store only the resulting cognitive debt or confirmed understanding, not a transcript of the quiz.

## Activities and Sources

| Activity | Outcome |
| --- | --- |
| `orient` | A bounded question, known material, source priorities, and unknowns |
| `collect` | Candidate sources and explicit selection criteria |
| `capture` | Traceable claims, context, limitations, and relevance |
| `analyze` | Comparisons and tentative inferences with evidence boundaries |
| `synthesize` | A reader-appropriate answer, note, report, or draft |
| `review` | A check of traceability, scope, conflicts, and unsupported language |

Local project files, supplied documents, primary sources, datasets, official documentation, secondary reporting, and personal notes have different evidentiary roles. Identify what was actually read. Prefer the strongest source practical for a claim, but do not discard useful contextual material merely because it is not primary; describe its role instead.

Reading a source does not by itself authorize a network search, download, tool installation, new database, publication, or broad reproduction. Follow the current request and available capabilities. Preserve existing user materials and project conventions; do not reorganize a library merely to fit this template.

## Main Session and Branches

The main coordinator maintains the research question, source map, unresolved claims, priorities, current next step, cognitive checkpoints, and the small set of derivation links that affect conclusions. `.agents/research-flow/state.md` is a compact handoff, not a transcript or authority. Only create or update it when persistence is in scope. Read the latest version before editing; existing sources and final artifacts take precedence over its summaries.

For each consequential data or experiment node, record only enough lineage to trace `input/version -> operation and key configuration -> output -> validation -> downstream consumer`. Do not inventory every temporary file. Use stable IDs or paths to connect source cards, datasets, scripts, run records, figures, drafts, and decisions where they exist. A missing link is an explicit uncertainty, not a reason to reconstruct a plausible history.

For a substantial source, use [source.md](templates/source.md). For multi-source writing, use [synthesis.md](templates/synthesis.md). Trim fields that do not help the task. A branch session may investigate a source cluster or one bounded question, but it returns its evidence packet to the main coordinator instead of editing the shared state.

Before dispatch, specify the question, permitted source set or search boundary, desired depth, output format, what counts as a locator, and return destination. Branches should report negative findings and access limits as carefully as positive claims. Do not claim a chat branch, file, source download, or external lookup exists without observing it.

On resume, verify old summaries and important derivation links against the actual source material and current artifact. Do not assume that an interrupted reader or unavailable source is complete. Preserve partial notes; distinguish them from checked evidence. Start with active recall when the user requests review or when a long gap makes their own understanding the priority.

## Synthesis and Completion

Tie material claims in a final artifact to source cards, citations, or an explicit explanation of why they are analytical judgment. Keep uncertainty near the conclusion it affects. When sources disagree, explain the disagreement, their scope or dates, and what evidence would change the conclusion rather than selecting a winner silently.

Before calling a research task complete, check the requested question and audience, claim traceability, important counterevidence, date/scope boundaries, known gaps, and any cognitive debt that materially qualifies the user's ability to rely on the result. Completion of a draft, a reading batch, a recommendation, and a published document are different delivery states. Do not imply later publication, citation-manager updates, or project decisions occurred unless they were observed.
