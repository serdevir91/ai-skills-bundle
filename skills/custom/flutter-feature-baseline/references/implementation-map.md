# Flutter Baseline Implementation Map

Use these proven patterns from existing projects when implementing baseline features.

## Theme + Amoled
- `Workout-Tracker/lib/providers/settings_provider.dart`
  - Persists `ThemeMode` and `background_mode`.
  - Exposes `isPureBlack` for amoled behavior.
- `Workout-Tracker/lib/main.dart`
  - Applies `themeMode` and pure-black aware dark color scheme.
- `supzip/lib/providers/app_state_provider.dart`
  - Simple persisted `ThemeMode` approach.

## Update Tracking
- `Workout-Tracker/lib/services/app_update_service.dart`
  - Store-version check model with `new_version_plus`.
- `Workout-Tracker/lib/screens/startup_gate.dart`
  - Startup update check flow.
- `autoshare/lib/services/update_service.dart`
  - Cross-platform updater with download/install handling.
- `stream_app/lib/core/updater/app_updater_service.dart`
  - Custom updater with release notes and download progress.
- `stream_app/lib/features/settings/presentation/screens/settings_screen.dart`
  - Manual update controls in settings.

## Rate + Review
- `Workout-Tracker/lib/services/review_service.dart`
  - In-app review request with store fallback.
- `Workout-Tracker/lib/services/startup_flow_service.dart`
  - Prompt throttling and "never show again" persistence.
- `Workout-Tracker/lib/screens/workout_summary_screen.dart`
  - Contextual popup prompt UI.
- `Workout-Tracker/lib/screens/settings_screen.dart`
  - Settings entries for review actions.
- `supzip/lib/screens/home_screen.dart`
  - Lightweight one-time rate prompt using persisted flag.

## Release Guardrail
- `Workout-Tracker/scripts/build_free_aab_auto_version.ps1`
  - Version bump before AAB build (`x.y.z+n -> x.y.(z+1)+(n+1)`).
