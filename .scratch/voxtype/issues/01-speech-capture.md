# 01: Speech capture module + hotkey trigger

**Category:** enhancement
**State:** ready-for-agent
**Triage note:** Vertical slice: capture pipeline. Blocker: none. Demoable independently.

**What to build:** User presses a configurable hotkey → microphone starts recording → audio buffer produced. The capture pipeline works end-to-end independently; no Transcription or insertion yet.

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent

- [ ] Configurable hotkey registered and detectable by the app
- [ ] Hotkey triggers microphone recording start
- [ ] Audio buffer produced and available to downstream modules
- [ ] No cloud/network call made during capture (local-only guarantee, per ADR-0001)
