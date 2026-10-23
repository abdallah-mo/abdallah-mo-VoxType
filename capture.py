# capture.py — Speech capture module (ticket 01, local-only per ADR-0001)
# Vocabulary: Speech capture (GLOSSARY.md)
# Seam: hotkey event -> audio buffer

class CaptureModule:
    """Minimal vertical slice: registers hotkey, produces audio buffer, no cloud."""
    def __init__(self):
        self.recording = False
        self.buffer = None

    def on_hotkey(self):
        """Trigger recording; no network call (local-only guarantee)."""
        self.recording = True
        self.buffer = b"audio_buffer_data"  # mock buffer for MVP
        return self.buffer

    def stop(self):
        self.recording = False
        return self.buffer
