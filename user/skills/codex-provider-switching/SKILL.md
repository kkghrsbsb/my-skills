---
name: codex-provider-switching
description: "Safely inspect, configure, and switch Codex or ChatGPT Desktop between its official OpenAI login and an independently authenticated custom model provider. Use for provider setup, migration, troubleshooting, or safe switching; not for routing third-party traffic through OpenAI credentials."
---

# Codex Provider Switching

Use this skill when a user wants to keep their existing official ChatGPT/OpenAI login while also using a separately authenticated provider, proxy, router, cloud deployment, or local model endpoint. Preserve the official login as an independent authentication path.

Do not treat a provider that merely accepts Chat Completions requests as compatible. Determine the required protocol from the current Codex documentation and test the target endpoint before configuring it.

## Non-negotiable security boundary

Never read, print, copy, transform, upload, or place in configuration any ChatGPT access token, refresh token, browser cookie, session cookie, OAuth grant, or content from the official credential store. Do not run logout, revoke, re-login, or edit official credential storage unless the user specifically asks.

Do not configure a third-party provider to use official OpenAI/ChatGPT authentication. A third-party provider must have its own authentication path. Do not point the built-in official provider at a third-party relay merely to make it appear to retain the official login.

Keep third-party secrets out of config files, profile files, shell history, command-line arguments, tool output, screenshots, and diagnostics. Prefer a platform credential manager or a provider-authentication command that retrieves the secret at runtime. If neither is available, offer an ephemeral, terminal-prompted environment variable; explain that it is not persistent and may remain visible to same-user processes while the app is running. Do not silently downgrade to plaintext-at-rest storage.

If a secret is echoed, logged, or otherwise exposed during the work, stop using it, tell the user to rotate it, and do not persist it.

## Discovery before changes

Perform only read-only work until the user approves a concrete plan and supplies any required provider details.

1. Fetch the current official Codex documentation for configuration, authentication, custom providers, profiles, and the relevant desktop client. Prefer official OpenAI documentation; do not infer current key names, protocol support, profile behavior, or credential paths from memory.
2. Inspect the installed desktop and CLI versions, executable provenance, current configuration locations, profile support, login status, enabled/managed restrictions, and diagnostic output. Redact values and inspect credential files only by metadata and supported status commands.
3. Establish the present official state: selected provider, selected model, authentication mode, and whether official credentials are separate from API-key credentials. Do not open the credential contents.
4. Inspect the custom endpoint without modifying state. Confirm the canonical base URL, the required authentication scheme, available target model identifiers, and the current wire protocol. Use a non-billable capability or validation request first. Do not send repository content. Obtain permission before any request that might generate billed model output.
5. Record uncertainties explicitly. If a managed policy, desktop build, protocol behavior, or secure-secret mechanism cannot be verified, stop short of mutation and present the evidence and options.

## Configuration strategy

Use the current official configuration reference as the source of truth for exact field names and permitted values.

- Define custom provider routing only in the user-level configuration layer that the current client documents as machine-local. Do not place provider selection, provider definitions, provider credentials, or routing overrides in a repository configuration.
- Keep the official provider as the base/default unless the user explicitly wants the desktop default changed. Register the additional provider as inactive until selected.
- Use a distinct, non-reserved provider identifier. Do not redefine a built-in provider.
- Select the third-party provider's own credential mechanism. Use a documented runtime secret source or command-backed token retrieval when available; do not reuse official login state.
- Set a model identifier only after it has been confirmed by the target provider. Do not assume the official model catalog is available through the relay.
- Use CLI profiles only if the installed version and current official documentation support them. A profile should contain only the values that differ from the base configuration. Keep an explicit official profile as well when it improves recovery.
- Do not assume a Desktop app has a profile picker or hot reload. Verify the UI and client behavior. If it only reads configuration on startup, design switching around a full app restart and state that requirement clearly.

Before writing, show the user the exact files to be changed, which provider will be default afterward, how credentials will be sourced, whether a restart is needed, and the proposed rollback action. Get confirmation for state-changing work.

## Switching and session isolation

Treat each provider as a separate conversation boundary.

- Switch only while no turn is running. Check the active provider before and after every switch.
- Start a new, visibly labeled conversation after switching. Do not resume, fork, or continue a thread that has already exchanged content with another provider.
- Local files and Git state may be shared. Pass only a deliberately selected summary, file path, diff, or commit between provider-specific conversations.
- If automation is requested, build an explicit status command and separate switch commands. Make them fail closed when the desktop app is still running, when the target provider is unavailable, or when required credentials are absent. Do not automate force-quitting the app without explicit approval.
- A CLI profile switch and a Desktop default switch may have different scopes. Explain which client each mechanism affects rather than implying simultaneous hot switching.

### Portable command contract

When the user asks for a consistent cross-machine workflow, provide the same public commands on every supported machine after the discovery, confirmation, backup, and validation steps above:

- `codex-use-official` selects the preserved official provider for the supported Desktop workflow.
- `codex-use-relay` selects the independently authenticated provider for the supported Desktop workflow.
- `codex-provider status` reports the active selection without printing credentials.

These names are the user-facing contract, not a mandate for a fixed implementation. Before creating them, discover a suitable user-level executable directory, check the command names are not already owned by another program, and ask before replacing any collision. Generate thin wrappers that locate the current Codex configuration and application at runtime or from detected installation state; do not bake in a home directory, executable location, provider ID, model ID, or secret value.

For Desktop workflows, require a full exit before changing a startup-only setting, do not force-quit the application, and start a new labeled conversation after relaunch. A Relay launcher may obtain a third-party secret through the detected secure mechanism or a no-echo terminal prompt, but must never embed, echo, or persist the secret. Also generate explicit CLI equivalents only when the installed CLI supports the selected mechanism. If a client cannot support this contract safely, create the status command and document the manual, client-specific switching steps instead of simulating a switch.

## Backup, rollback, and verification

Before changing configuration, create a timestamped, mode-restricted backup of every configuration file that will be modified. Verify the backup parses and contains no secret that was newly introduced. Do not back up or copy credential stores.

After each write:

1. Run the current client’s strict configuration or diagnostic validation in a redacted mode.
2. Verify the selected provider, authentication requirement, model identifier, and active profile with supported status/diagnostic commands.
3. Verify that the official login remains present without reading its credential data.
4. Verify that no secret appears in configuration, profile files, command history, terminal output, or diagnostic output.
5. With permission, perform the smallest safe protocol/authentication test against the custom provider. Test a real model request only when the user accepts possible usage charges.
6. For Desktop changes, fully restart the app, start a new labeled conversation, and verify the provider shown in current-session status.

Rollback restores only the backed-up configuration files, then restarts the affected client and rechecks official login status. Remove custom provider definitions, profiles, helper launchers, and third-party secret material only when the user explicitly asks. Never use destructive resets on the whole Codex home directory.

## Troubleshooting

Diagnose without exposing secrets.

- Configuration rejected: compare the precise error to the current official schema; do not guess renamed or deprecated fields.
- Provider reports a missing key: check the existence and scope of the designated runtime secret source, never print its value.
- Authentication fails: confirm the custom provider is not marked to use official authentication, confirm the base URL and auth scheme, and retry only after checking key rotation/expiry.
- Protocol or streaming failure: determine whether the endpoint supports the currently required API transport and streaming behavior. Do not substitute a deprecated protocol just because the provider advertises general OpenAI compatibility.
- Desktop appears unchanged: confirm the process was fully restarted, the correct user-level config location is in use, and no managed policy overrides the setting.
- Conversation/history concern: stop and create a new provider-labeled conversation; do not move an existing transcript across the boundary.
- Need to recover quickly: select the explicit official profile or restore the configuration backup, then verify official login status.

## When to re-check online

Re-read current official documentation and repeat capability detection before acting whenever any of these applies:

- Codex CLI, ChatGPT Desktop, or a managed policy has changed since the last setup.
- The user asks to change provider type, authentication method, base URL, model family, transport, or secret storage.
- A configuration key is unrecognized, deprecated, undocumented, or conflicts with local diagnostics.
- The provider claims a new OpenAI-compatible feature, streaming mode, WebSocket mode, or protocol.
- The plan moves between CLI-only, Desktop, IDE, cloud, managed, or remote environments.
- A security incident, credential rotation, authentication failure, or unexpected cross-provider session behavior occurs.

Treat all version-dependent details as hypotheses until they have been confirmed by the installed client and current official documentation.
