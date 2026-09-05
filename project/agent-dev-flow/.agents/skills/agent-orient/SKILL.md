---
name: agent-orient
description: Build a read-only working understanding of an unfamiliar or long-unvisited repository, including its main flows, validation entry points, and open questions. Use for project onboarding or learning before deciding what to change.
---

# Agent Orient

Read [the shared protocol](../../dev-flow/protocol.md). This skill establishes project understanding; use `agent-resume` instead when the main question is the status of already dispatched work.

## Establish the Working Model

Announce `explore` and `read-only explore`, plus whether this stays in the main session or uses an authorized branch session. Begin with the user's learning question, not an exhaustive repository inventory.

If this is a main session starting on an existing repository without reliable prior conversation context, classify it as `reconstructed` bootstrap. Rebuild from repository facts and user-confirmed intent; do not invent lost history or initialize a cockpit during the read-only pass.

Locate project instructions, README, manifests, important entry points, and available tests. Read `.agents/dev-flow/state.md` if it exists, then check its claims against the current branch, revision, and relevant changes. Do not initialize files during exploration.

Trace one representative flow through actual code: input, important processing, stored state or external calls, and output. Explain the modules and design choices the user needs to understand that flow. Ground claims in paths and symbols; separate documented intentions from observed implementation.

Find how the project is built and checked by reading its configuration. Distinguish a discovered command from one actually executed. Under read-only scope, do not install dependencies or run commands that generate project files. Name a useful probe for later when executing it would require writes.

## Return an Exploration Report

Keep the first screen useful to someone returning after months away:

- What the project does and where its main flow begins.
- The few modules and relationships needed for the user's question.
- Current relevant work, evidence, and unverified assumptions.
- Validation entry points and what has actually been checked.
- A recommended next step: more exploration, diagnosis, a bounded implementation, or no change.

Use [the report template](../../dev-flow/templates/report.md) only if a durable handoff would help. For a branch session, return the report to the coordinator without editing the cockpit. For the main session, offer the findings in chat; persist them only when documentation or state updates are within the user's request.

An exploration result does not automatically authorize implementation. If implementation is already part of the request, the main session can use the findings to proceed within that scope without another approval ritual.
