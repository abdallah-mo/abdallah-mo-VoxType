# ADR-0001: Local-only Speech-to-Text with Whisper tiny

## Status
Accepted (from grilling round 1–2 with user Abdallah Mokhtar / VoxType project).

## Context
VoxType is a Windows desktop voice-typing application. The user explicitly said "i dont have a cloud, solve it" and confirmed no cloud service is available. The user also noted limited device memory ("i dont have memory to install local model, is it big").

## Decision
Use a **local-only** speech-to-text pipeline (no cloud API). Start with **Whisper `tiny`** (~75 MB) as the default local model, with the larger model upgrade path (`base`, etc.) documented but not required for MVP.

## Trade-offs considered

- **Cloud service (Whisper API / Azure Speech)**: rejected — user confirmed no cloud access and privacy/local-only preference.
- **Large local model (`large`)**: rejected for MVP — user lacks memory; will work on constrained devices only with `tiny`.
- **Tiny model (`tiny`)**: accepted — lower accuracy but works locally on limited memory; upgrade path preserved.

## Consequences
- Positive: works offline; no data leaves device; works on memory-constrained Windows devices.
- Negative: transcription accuracy is lower than cloud or large local models; Arabic support depends on Whisper's multilingual training (acceptable for `tiny`).
- Reversible? Partially — switching to a larger local model is easy; switching to cloud requires reversing a core privacy/architecture decision, so it is **hard to reverse** (justifies ADR).

## Related
- GLOSSARY.md: terms `Transcription`, `Language detection`, `Active text field`.
- Issue tracker: `docs/agents/issue-tracker.md` (GitHub).
