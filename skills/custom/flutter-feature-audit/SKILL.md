---
name: flutter-feature-audit
description: "Audit one or many Flutter projects for baseline feature compliance: theme support (light/dark plus amoled), update check flow, and in-app rating/review integration with settings entry. Use when user asks to scan Flutter repos, compare app parity, or list missing baseline features before release."
---

# Flutter Feature Audit

Run a deterministic scan over Flutter app folders and report which baseline features exist or are missing.
Use this to quickly prioritize fixes across multiple apps.

## Workflow

1. Run the audit script:

```bash
python scripts/audit_flutter_features.py "C:/path/to/root"
```

Optional JSON output:

```bash
python scripts/audit_flutter_features.py "C:/path/to/root" --json
```

2. Read the report and prioritize missing items:
- Theme baseline: `ThemeMode` plus amoled markers.
- Update baseline: update-check implementation markers.
- Review baseline: `in_app_review`, review API markers, settings entry markers.

3. Apply fixes using `$flutter-feature-baseline`:
- Reuse existing project architecture.
- Add only missing pieces.

4. Re-run audit until all apps pass.

## Detection Rules

- A folder is considered a Flutter app when it contains both:
- `pubspec.yaml`
- `lib/main.dart`
- Theme passes when both are found:
- Any `ThemeMode` marker in `lib/`
- Any amoled marker (`amoled`, `pure_black`, `isPureBlack`, `background_mode`)
- Update passes when an update marker is found in `lib/`:
- `checkForUpdate`, `UpdateService`, `app_update_service`, `app_updater_service`, `new_version_plus`, `upgrader`
- Review passes when all are found:
- `in_app_review` dependency in `pubspec.yaml`
- Review API marker (`requestReview`, `openStoreListing`, `openStoreReviewPage`, `requestInAppReviewWithFallback`)
- Settings marker in `lib/**/settings*.dart` (`rate`, `review`, or `in_app_review`)

## References

Read [baseline-patterns.md](references/baseline-patterns.md) for file-level implementation references from existing apps.

## Output Contract
- Report app-by-app status with `PASS` or `MISSING`.
- List missing feature categories per app.
- Propose concrete next edits (files + features) for each missing category.
