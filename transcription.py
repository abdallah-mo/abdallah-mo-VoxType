# transcription.py — Local-only STT (ticket 02, ADR-0001)
# Vocabulary: Transcription, Language detection (GLOSSARY.md)
# Blocked by: 01 (Speech capture)
# Constraint: no cloud/network; Whisper tiny model; upgrade path noted

class TranscriptionModule:
    """Tracer bullet: audio buffer -> raw text + language (tiny model, local-only)."""
    MODEL_SIZE = "tiny"  # ~75 MB; upgrade path to larger models preserved

    def __init__(self):
        self.model = "whisper_tiny_local"  # simulated local model reference

    def transcribe(self, audio_buffer: bytes):
        """Local-only transcription; no network call."""
        # In real implementation: faster-whisper / whisper.cpp loads MODEL_SIZE
        raw_text = "[simulated transcription from audio]"
        detected_language = "ar"  # or "en"; multilingual support per Q4/Q7
        return {"text": raw_text, "language": detected_language, "model": self.MODEL_SIZE}

    def upgrade_path_available(self) -> bool:
        """Upgrade path: tiny -> base/larger (per Q6c, not implemented in MVP)."""
        return True
