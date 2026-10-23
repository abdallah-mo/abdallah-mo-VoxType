# 03: Intelligent text correction + Review interface

**Category:** enhancement
**State:** ready-for-agent
**Triage note:** Vertical slice: correction + review UI. Blocked by 02.

**What to build:** Raw transcription (from 02) → Intelligent text correction (spelling/grammatical) → corrected text displayed in review interface. User reviews corrected output; insertion blocked until approval. Default review mode (manual, per Q3) working.

**Blocked by:** 02 — Local-only Transcription (Whisper tiny) with Language detection

**Status:** ready-for-agent

- [ ] Correction module applies spelling and grammatical fixes (Q8; see GLOSSARY.md: Intelligent text correction)
- [ ] Review interface displays corrected text to user
- [ ] User approval required before text moves to insertion (manual review, Q3)
- [ ] Correction works independently of Transcription model (change to `tiny` doesn't break correction)
