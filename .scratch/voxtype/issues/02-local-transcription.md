# 02: Local-only Transcription (Whisper tiny) with Language detection

**Category:** enhancement
**State:** ready-for-agent
**Triage note:** Vertical slice: local STT with Whisper tiny + language detection. Blocked by 01.

**What to build:** Audio buffer (from 01) → Whisper `tiny` model produces raw text + detected language (Arabic / English minimum). Confirms ADR-0001 decision: local-only STT, `tiny` model (~75 MB), upgrade path documented but not required for MVP.

**Blocked by:** 01 — Speech capture module + hotkey trigger

**Status:** ready-for-agent

- [ ] Whisper `tiny` model loaded locally (no download at runtime; bundled or pre-downloaded)
- [ ] Audio buffer → raw transcription text
- [ ] Language detection returns Arabic or English (multilingual support confirmed)
- [ ] Verified: no network request made during Transcription (offline guarantee)
- [ ] Model upgrade path (`tiny` → larger) noted in module interface (not implemented)
