# Baseline Patterns

These projects in `<WORKSPACE>` provide known-good patterns:

- `Workout-Tracker`
  - Theme + amoled persistence.
  - Startup update check.
  - In-app review service.
  - Prompt throttling and settings review entries.
- `supzip`
  - Theme mode persistence.
  - Update check with `new_version_plus`.
  - Lightweight rate popup with saved state.
- `autoshare`
  - Startup update check and manual settings update action.
  - Custom update service.
- `stream_app`
  - Full settings update panel with version/release notes/progress.
  - Custom updater service.

Use these apps first when deriving implementation details for missing features.
