# RED test — Capture module interface (tracer bullet for ticket 01)
# Vocabulary: Speech capture (GLOSSARY.md), local-only (ADR-0001)
# Seam: hotkey event -> audio buffer (no cloud call)

import pytest

def test_capture_hotkey_produces_audio_buffer():
    """Given hotkey trigger, capture produces audio buffer; no network call."""
    # RED — will fail: Capture module not implemented
    assert False, "RED: Capture module not yet implemented"
