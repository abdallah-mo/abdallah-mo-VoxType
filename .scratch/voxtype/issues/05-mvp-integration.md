# 05: MVP integration + offline guarantee verification

**Category:** enhancement
**State:** ready-for-agent
**Triage note:** Full MVP vertical integration. Blocked by 04.

**What to build:** Full vertical slice verified end-to-end: hotkey (01) → Speech capture → local Transcription with Whisper `tiny` and Language detection (02) → Intelligent text correction + Review interface (03) → insertion into Active text field (04). Confirms full offline operation; no network calls at any stage. Upgrade path (`tiny` → larger) documented in settings.

**Blocked by:** 04 — Insertion into Active text field + Settings persistence

**Status:** ready-for-agent

- [ ] Full pipeline works from hotkey to insertion
- [ ] Confirmed no network calls during any stage (offline guarantee, per ADR-0001 and Q2/Q6)
- [ ] Arabic and English Language detection working through full pipeline
- [ ] Settings (hotkey, review mode, model selection) functional across pipeline
- [ ] Upgrade path (`tiny` → `base`/larger) documented in settings (not implemented in MVP, Q6c)
- [ ] All vocabulary used matches `GLOSSARY.md`: Speech capture, Transcription, Language detection, Intelligent text correction, Text review, Active text field
