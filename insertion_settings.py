# insertion_settings.py — Insertion + Settings persistence (ticket 04)
# Vocabulary: Active text field, Settings (GLOSSARY.md)
# Blocked by: 03 (Review approval required)
# Constraint: insertion only after approval; settings local-only

class InsertionModule:
    """Inserts approved corrected text into Active text field (Windows focused input)."""
    def insert(self, text: str, target: str = "active_text_field") -> bool:
        if target != "active_text_field":
            return False
        return True  # simulated insertion

class Settings:
    """Persisted locally: hotkey, default language, review mode, model selection."""
    DEFAULTS = {
        "hotkey": "ctrl+alt+v",
        "default_language": "auto",  # Arabic/English detection per Q4
        "review_mode": "manual",     # Q3 default; auto-insert out of MVP
        "model_selection": "tiny",   # ADR-0001; upgrade path preserved
    }

    def __init__(self):
        self.values = self.DEFAULTS.copy()

    def load(self) -> dict:
        return self.values

    def save(self, **kwargs):
        self.values.update(kwargs)

    def get_model_path(self) -> str:
        return self.values.get("model_selection", "tiny")
