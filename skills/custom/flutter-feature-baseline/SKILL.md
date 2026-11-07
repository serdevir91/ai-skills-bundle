---
name: flutter-feature-baseline
description: "Standardize Flutter applications with a reusable product baseline: light/dark/amoled theme support, persistent theme settings, update checks (startup plus settings action), and in-app rating/review flow (popup plus settings entry). Use when editing or creating Flutter apps, especially when user requests shared UX features across multiple apps or asks to align settings/release behavior."
---

# Flutter Feature Baseline

Apply a consistent feature baseline to Flutter apps so every project ships the same core UX and release behavior.
Use this before feature work, before release hardening, and when auditing parity between multiple Flutter apps.

## Baseline Requirements

### 1. Theme System (Light, Dark, Amoled)
- Keep `themeMode` selectable as `light`, `dark`, `system`.
- Add a separate "background mode" selector with an amoled option (`pure_black` or `amoled`).
- Persist both values in local storage (`SharedPreferences`, Hive, SQLite, or existing settings store).
- Wire settings to `MaterialApp(themeMode: ...)` and dark theme color tokens.
- Ensure amoled mode uses true black surfaces where appropriate.

### 2. Update Tracking
- Run a non-blocking update check near startup/onboarding gate.
- Add manual update controls in settings: check now, show latest version, show release notes (if available), and trigger update/open store.
- Prefer existing project updater implementation; only add dependency-based updater when no custom service exists.
- Handle platform differences gracefully (Android/iOS store listing vs desktop installer/download).

### 3. Rate and Review Flow
- Use `in_app_review` with fallback to store listing/review page.
- Add contextual popup prompt (not every launch): persist prompt/rated/never states.
- Include explicit settings entries:
  - `Rate and Comment` (in-app review request)
  - `Write Comment` or `Open Store Review Page` (direct store page)
- Fail safely with user-visible fallback message if review flow cannot open.

### 4. In-App Purchase (IAP) & Paywall Flow (Strictly Mandatory)
- Dedicated Pro / Premium Paywall screen presenting features, pricing, and purchase buttons.
- Supported product models: Non-consumables (`remove_ads`, `pro_tier`, `lifetime_unlock`), consumables, or subscriptions.
- Mandatory "Restore Purchases" button in both the Paywall and Settings/Menu.
- Secure offline entitlement persistence (local cache/prefs) so users retain purchased status even when offline.
- Transparent error handling for cancelled, pending, or failed transactions.
- New apps MUST include this by default; existing apps MUST implement this on their next update.

### 5. Release and Version Guardrail
- Before any Android AAB build, bump `pubspec.yaml` version first.
- Default bump rule:
  - `version: x.y.z+n -> version: x.y.(z+1)+(n+1)`
- Keep this consistent with project release scripts and changelog metadata flow.

## Implementation Workflow

1. Detect existing architecture:
- Identify state management and settings persistence layer.
- Reuse existing patterns instead of introducing a second settings system.

2. Implement missing baseline items:
- Add minimum dependencies only when needed (`in_app_review`, `in_app_purchase`, `in_app_update`, `package_info_plus`).
- Prefer service wrappers (`review_service`, `update_service`, `purchase_service`) over direct widget-level calls.

3. Expose settings UX:
- Ensure all baseline controls (Update check, Rate, Paywall/Restore) are reachable from a settings screen.
- Localize labels if project has localization.

4. Validate:
- Startup update path works without blocking first render.
- Settings update action works.
- Review prompt throttling works.
- Purchase/Restore flow works and entitlements persist across restarts.
- Theme and amoled persistence survives app restart.

## Project Patterns To Reuse

Read [implementation-map.md](references/implementation-map.md) for concrete file-level patterns extracted from existing apps.

## Done Criteria
- App supports light/dark/system and amoled mode with persistence.
- App has startup update check and settings update action.
- App has rate/review popup logic and settings review entries.
- App has In-App Purchase flow, Paywall screen, and Restore Purchases action with persistent entitlements.
- AAB builds follow required pre-build version bump rule.
