# RED test — Transcription module interface (ticket 02)
# Vocabulary: Transcription, Language detection (GLOSSARY.md)
# Seam: audio buffer -> raw text + detected language; local-only (ADR-0001)
# Blocked by 01 (capture)

def test_transcription_local_only_whisper_tiny():
    """Audio buffer produces text + language; no cloud/network; uses tiny model."""
    assert False, "RED: Transcription module (Whisper tiny, local-only) not implemented"
