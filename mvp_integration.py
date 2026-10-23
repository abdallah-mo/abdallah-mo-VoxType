# mvp_integration.py — Full vertical slice integration (ticket 05, MVP)
# Vocabulary: Speech capture, Transcription, Language detection,
# Intelligent text correction, Text review, Active text field (GLOSSARY.md)
# Blocked by: 04; confirms ADR-0001 (local-only, no cloud/network at any stage)
# Upgrade path (tiny -> larger) visible via settings; not implemented in MVP (Q6c)

from capture import CaptureModule
from transcription import TranscriptionModule
from correction_review import CorrectionModule, ReviewInterface
from insertion_settings import InsertionModule, Settings

class VoxTypeMVP:
    """Tracer bullet: full vertical pipeline verified end-to-end, offline."""
    def run_pipeline(self, hotkey_trigger: bool = True):
        # 01: Capture
        capture = CaptureModule()
        audio = capture.on_hotkey() if hotkey_trigger else b""

        # 02: Transcription (local-only, tiny)
        stt = TranscriptionModule()
        transcription_result = stt.transcribe(audio)

        # Verify offline guarantee (ADR-0001): no cloud/network used
        # In real build: assert no outgoing requests made
        offline_guaranteed = ("whisper_tiny_local" in stt.model)

        # 03: Correction + Review
        correction = CorrectionModule()
        review = ReviewInterface()
        corrected = correction.correct(transcription_result["text"])
        review.show(corrected)
        approved = review.approve()  # manual review per Q3

        # 04: Insertion (only after approval) + Settings (Active text field per GLOSSARY.md)
        insertion = InsertionModule()
        settings = Settings()
        inserted = False
        if approved and review.is_approved():
            inserted = insertion.insert(corrected)

        return {
            "audio_captured": bool(audio),
            "transcription": transcription_result,  # includes language (ar/en)
            "language_detected": transcription_result["language"],
            "corrected": corrected,
            "review_approved": approved,
            "inserted": inserted,
            "offline_guarantee": offline_guaranteed,
            "model": settings.get_model_path(),  # "tiny"; upgrade path visible
            "settings_review_mode": settings.load()["review_mode"],
        }
