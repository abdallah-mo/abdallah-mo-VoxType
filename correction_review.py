# correction_review.py — Intelligent text correction + Review interface (ticket 03)
# Vocabulary: Intelligent text correction, Text review (GLOSSARY.md)
# Blocked by: 02 (Transcription); independent of Transcription model choice
# Constraint: no cloud/network; review required before insertion

class CorrectionModule:
    """Spelling/grammatical correction (Q8); works independently of STT model."""
    def correct(self, raw_text: str) -> str:
        # Minimal correction: normalize spacing, fix simulated errors
        corrected = raw_text.replace("  ", " ").strip()
        return f"[corrected] {corrected}"  # marker for demonstration

class ReviewInterface:
    """Text review: displays corrected text; approval blocks insertion (Q3)."""
    def __init__(self):
        self.approved = False
        self.display_text = None

    def show(self, corrected_text: str):
        self.display_text = corrected_text
        self.approved = False
        return self.display_text

    def approve(self) -> bool:
        """Manual review approval (default per Q3). Auto-insert out of MVP scope."""
        self.approved = True
        return True

    def is_approved(self) -> bool:
        return self.approved
