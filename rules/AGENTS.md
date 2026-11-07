# AGENTS Rules for This Workspace

## Default Product Language (All Projects)

- Games and applications must use English for all player/user-facing content by default, unless the user explicitly requests a different language.
- Keep existing localization capabilities when appropriate; English remains the default unless explicitly changed by the user.
- This preference applies to new projects and feature additions. Conversation with the user may remain in Turkish.

All agents working in this workspace must apply these rules for Flutter projects.

## Mandatory Skills

- Use `skills/custom/flutter-feature-baseline` when creating or editing Flutter app features.
- Use `skills/custom/flutter-feature-audit` before release or when asked to scan multiple Flutter apps.
- Use `skills/custom/play-store-publish` when deploying Android apps to Google Play.
- Use `skills/custom/msstore-publish` when deploying Windows apps to Microsoft Store.
- Use `skills/custom/app-store-publish` when deploying iOS apps to Apple App Store or managing App Store Connect.
- Use `skills/custom/reverse-engineer-anything` when asked to inspect, analyze, or reverse engineer external repositories, codebases, or compiled applications.
- Use `skills/custom/scrapling-official` when scraping, crawling, or extracting data from web pages, or when plain fetching returns an empty JS page. Not for documented APIs or sites that need login.

## Mandatory App Baseline (All Apps & Frameworks: Flutter, Godot, Native, etc.)

For EVERY application, game, or project developed in this workspace, the following features are STRICTLY MANDATORY:
- **New Projects**: Must include In-App Update, In-App Review, and In-App Purchase (IAP/Paywall) by default from day 1.
- **Existing Projects**: Whenever any existing project is updated, refactored, or given a new feature/version, if any of these three features are missing, they MUST be implemented during that update.

- **In-App Update (Strictly Required)**:
  - Automatic startup check and manual check/update action in settings/menu.
  - On Android: Must implement official Google Play In-App Updates (`com.google.android.play:app-update` or `in_app_update`).
  - On iOS/Windows: Implement version check and store update link prompt.
- **In-App Review / Rating (Strictly Required)**:
  - In-app review flow triggered dynamically upon key milestones (e.g. wave completions, high scores, task completions) without annoying the user.
  - Manual review/rate button in settings/menu.
  - On Android: Must implement official Google Play In-App Review (`com.google.android.play:review` or `in_app_review`).
  - Graceful fallback to opening store page if review dialog cannot be launched.
- **In-App Purchase (IAP) & Paywall (Strictly Required)**:
  - Dedicated Pro / Premium Paywall screen displaying premium features, clear pricing, and purchase buttons.
  - Supported purchase types based on product type: non-consumables (`remove_ads`, `pro_tier`, `lifetime_unlock`), consumables, or subscriptions.
  - Mandatory "Restore Purchases" button in both the Paywall and Settings/Menu.
  - Secure offline entitlement persistence (local cache/prefs) so users retain purchased status even when offline.
  - Transparent error handling for cancelled, pending, or failed transactions.
- **Theme Support (For Flutter Apps)**:
  - Light, dark, and amoled/pure-black mode with persistent state.

## UI Design & Aesthetic Standards (Required)

- **Color-Coded Semantic Grids & Cards (For Islamic / Religious Apps)**:
  - Holy days & calendar categories in Islamic/religious applications must use distinct color schemes (e.g. Kandiller: Champagne `#FFF8E7` / Gold `#D4AF37`, Bayramlar: Emerald Green `#E8F5E9` / `#2E7D32`, Other Holy Days: Amber `#FFF3E0` / `#FF9800`).
  - Tapping grid dates or lists must open interactive Pop-up Cards displaying title, category badge, Gregorian/Hijri dates, background meaning, and recommended actions.
- **Dual Reader Modes**:
  - Provide Dual Reader Modes for textual content (e.g. Mushaf 1-604 Page Mode with dual top/bottom Arabic + translation layout vs. Ayet-by-Ayet list view).
- **Interactive Target & Round Counters**:
  - Counters must support custom target configuration, live round badges (`1 Tur (100 / 100)`), auto-reset upon target reach, and multi-pulse haptic vibration feedback (`[0, 80, 40, 200]`).

## Localization & Notification Integrity (Required)

- **Multi-Language & Locale Synchronization**:
  - Support full localizations (`.arb`) for TR, EN, AR, FA with English as the default language on first launch. Use automatic device-language selection only when explicitly requested by the user.
  - Notifications and scheduled alarms MUST automatically sync to the user's active app language (`tr`, `en`, `ar`, `fa`).
- **Authentic Text & Translation Pairing**:
  - Multi-edition text fetching (e.g. Quran Uthmani Arabic + translation edition) must be paired per verse and cached locally; text must never fall back to repetitive hardcoded text (e.g. Bismillah bug).
- **Alarm & Completion Guard**:
  - Scheduled alarms must skip past times and prayers/tasks already marked as completed.

## Release Guardrail

- **Android (Google Play)**:
  - Before any Android AAB build, bump `pubspec.yaml` version first: `version: x.y.z+n -> version: x.y.(z+1)+(n+1)`
  - After any successful Android AAB build, always output the release notes formatted inside `<en-US>...</en-US>` tags.
- **Windows (Microsoft Store)**:
  - Before any Windows MSIX build/publish, bump `pubspec.yaml` versions:
    - `version: x.y.z+n -> version: x.y.(z+1)+(n+1)`
    - `msix_config.msix_version: x.y.z.w -> x.y.(z+1).0`
  - Deploy via `python upload_to_msstore.py --app <appName> --action publish` and poll status until live.
- **iOS (Apple App Store / TestFlight)**:
  - Before any iOS IPA build, bump `pubspec.yaml` version first: `version: x.y.z+n -> version: x.y.(z+1)+(n+1)`
  - Ensure encryption compliance in `ios/Runner/Info.plist`: `<key>ITSAppUsesNonExemptEncryption</key><false/>`
  - Track builds and TestFlight status via `python upload_to_appstore.py --action builds`
  - After any successful TestFlight upload, output release notes inside `<en-US>...</en-US>` tags.
