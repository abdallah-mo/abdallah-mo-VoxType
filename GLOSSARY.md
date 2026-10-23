# GLOSSARY — VoxType

## Canonical terms (resolved through grilling)

### Speech capture
Audio recording from the microphone, triggered by a user-configurable hotkey. The entry point for the VoxType workflow.

### Transcription (STT — Speech to Text)
Converting captured audio to written text. **Decision (Q2, Q6): local-only** — no cloud service; uses a local model (Whisper.cpp / faster-whisper / Vosk). **Decision (Q6b, Q6c): starts with Whisper `tiny` (~75 MB)** to work on memory-constrained devices; larger models (`base`, etc.) are documented as future upgrade path. Cloud option explicitly rejected.

### Language detection
Automatic detection of spoken language. **Decision (Q4): supported** — must handle Arabic and English at minimum, ideally more languages.

### Intelligent text correction (post-processing)
Correction applied to the transcription output before review/insertion. **Decision (Q8): spelling and grammatical correction** — not just formatting.

### Text review
**Decision (Q3): user reviews transcribed text before insertion.** Default behavior; automatic insertion may be configurable but review is the canonical path.

### Active text field
The currently focused text input on Windows where the final text is inserted after review / correction.

### Settings / configuration
**Decision (Q9): configurable** — default language, review mode (manual/auto), hotkey, model selection (tiny → future larger).

### MVP scope
**Decision (Q10): MVP = capture audio → local STT (tiny model) → review interface → manual insertion.** Future enhancements (larger model, auto-insert, advanced commands) come after MVP validation.
