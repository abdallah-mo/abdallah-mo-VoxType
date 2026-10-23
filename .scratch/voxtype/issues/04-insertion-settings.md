# 04: Insertion into Active text field + Settings persistence

**Category:** enhancement
**State:** ready-for-agent
**Triage note:** Vertical slice: insertion + settings persistence. Blocked by 03.

**What to build:** Approved corrected text (from 03) inserted into the currently focused Windows text field (Active text field, per GLOSSARY.md). Settings persisted locally: hotkey, default language, review mode (manual/default), model selection (`tiny` with upgrade path noted).

**Blocked by:** 03 — Intelligent text correction + Review interface

**Status:** ready-for-agent

- [ ] Text inserted into Active text field after user approval
- [ ] Settings persisted locally and load on startup
- [ ] Hotkey setting affects capture behavior (links back to 01 module interface)
- [ ] Review mode setting respects manual review default (Q3); optional auto-insert noted but out of MVP scope
- [ ] Model selection shows `tiny` as current; upgrade path (`base`, larger) visible but disabled for MVP
