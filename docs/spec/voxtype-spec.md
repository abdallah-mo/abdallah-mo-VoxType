## Problem Statement

Users need a hands-free, desktop voice-typing experience on Windows that converts Speech capture to written text quickly and reliably. The current gap: no lightweight, modular desktop application exists that supports local-only Transcription, automatic Language detection (Arabic / English), Intelligent text correction, configurable review/insertion behavior, and works on memory-constrained devices.

## Solution

Build VoxType: a Windows desktop voice-typing application. The workflow is: Speech capture (microphone, configurable hotkey) → local-only Transcription (Whisper `tiny`, ~75 MB, no cloud) → Intelligent text correction (spelling/grammatical) → Text review (user reviews before insertion by default) → insertion into the Active text field. Settings control language, review mode, hotkey, and model upgrade path.

## User Stories

1. As a Windows user, I want to trigger Speech capture with a configurable hotkey, so that I can start typing hands-free without touching the keyboard.
2. As a user with limited device memory, I want Transcription to run locally using Whisper `tiny` (~75 MB), so that the app works without a cloud connection and without requiring a high-memory device.
3. As a bilingual user (Arabic / English), I want automatic Language detection during Transcription, so that I don't need to manually switch language settings before speaking.
4. As a user concerned with privacy, I want the Speech-to-Text pipeline to be local-only (no cloud service sends my audio), so that my voice data never leaves my device.
5. As a user who wants accurate text, I want Intelligent text correction applied to the transcription before review, so that spelling and grammatical errors are fixed automatically.
6. As a user, I want to review the corrected text before it is inserted into the Active text field, so that I can approve or edit it (default behavior per grilling Q3).
7. As a power user, I want Settings that let me configure the default language, review mode (manual review vs. optional auto-insert), the hotkey, and the model selection (`tiny` now, larger model upgrade path later), so that I can tailor the app to my workflow.
8. As a developer, I want the architecture to be modular (separate modules for capture, STT, correction, review, insertion, settings), so that future enhancements (larger model, new languages, voice commands) don't require a full redesign.
9. As a user, I want the app to work offline, so that I can use it without an internet connection (local-only STT ensures this).
10. As a user, I want clear documentation of the upgrade path from `tiny` to larger Whisper models, so that I can improve accuracy when I have more memory.

## Implementation Decisions

- **Local-only STT**: No cloud API (rejected in grilling Q2, Q6; see ADR-0001). Uses Whisper.cpp / faster-whisper / Vosk locally.
- **Model selection**: Starts with Whisper `tiny` (~75 MB) per grilling Q6b, Q6c. Larger models (`base`, etc.) documented as upgrade path, not MVP.
- **Module seams (highest possible)**: One primary seam — the Transcription module interface (audio → text + detected language). All other modules depend on this; changing the model (tiny → larger) affects only this seam.
  - Capture module: microphone access, hotkey trigger, audio buffer.
  - Transcription module: takes audio buffer → returns raw text + detected language. Local model only.
  - Correction module: takes raw text → returns corrected text (spelling/grammatical, Q8). Independent of model choice.
  - Review module: displays corrected text; waits for user confirmation (default, Q3) before passing to insertion. Configurable: manual (default) or optional auto-insert (future, out of scope).
  - Insertion module: inserts approved text into the Active text field.
  - Settings module: hotkey, default language, review mode, model selection (`tiny` → future larger). Persisted locally.
- **Architecture**: Single-context repo (`GLOSSARY.md` + `docs/adr/` at root, per `docs/agents/domain.md`). No `GLOSSARY-MAP.md` needed.
- **Language support**: Arabic and English minimum (Q4, Q7). Achieved through Whisper's multilingual model.
- **Privacy**: Audio never leaves device. No network calls for STT. Recorded in spec and ADR-0001.

## Testing Decisions

- Only test external behavior, not implementation details (e.g., don't assert which Whisper model file is loaded; assert Transcription produces text from audio input).
- Capture: test hotkey triggers recording; audio buffer produced.
- Transcription: test audio → text output; language detection returns Arabic/English; confirm no network request (local-only guarantee).
- Correction: test spelling/grammatical corrections on sample transcriptions; don't test internal dictionary.
- Review / Insertion: test approved text reaches Active text field; unapproved text not inserted.
- Settings: test persistence; changing hotkey/model affects behavior.
- Prior art: greenfield (new repo); no existing tests in codebase.

## Out of Scope

- Voice commands ("delete last word", "new paragraph") — future enhancement.
- Auto-insert as default — review before insertion is canonical (Q3); auto-insert configurable but out of initial MVP.
- Cloud STT or hybrid local/cloud pipeline — explicitly rejected (ADR-0001).
- Large Whisper model (`base`, `large`, etc.) in MVP — upgrade path only (Q6c).
- Mobile or web versions — Windows desktop only (Q1).
- Real-time streaming transcription (word-by-word) — MVP uses batch transcription after capture completes.

## Further Notes

- Vocabulary used throughout: Speech capture, Transcription, Language detection, Intelligent text correction, Text review, Active text field, Settings — all defined in `GLOSSARY.md`.
- Architecture decision (local-only + Whisper `tiny`): `docs/adr/0001-local-only-stt-whisper-tiny.md`.
- Issue tracker: GitHub (`docs/agents/issue-tracker.md`). Triage label for this spec: `ready-for-agent`.
- No interview conducted; synthesized from `/grill-with-docs` session (Q1–Q10, Q6b, Q6c) and `/domain-modeling` artifacts (`GLOSSARY.md`, ADR-0001).
