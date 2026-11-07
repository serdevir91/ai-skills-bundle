---
name: play-store-publish
description: >-
  Deploy Flutter apps to Google Play Console. Use when the user asks to build AAB bundles,
  upload to Play Store, check app status, update store listings, manage in-app products,
  or publish a new version. Covers all 5 apps: Workout Tracker, Flappy Rogue,
  Ezan Vakti Premium, SupZip, and AutoShare.
---

# Google Play Store Deploy & Manage Skill

This skill enables automated Google Play Console operations for the user's 5 Flutter apps using a pre-configured Service Account and Python deployment tools.

---

## Prerequisites

- **Python 3.x** with packages: `google-auth`, `google-api-python-client`
- **Service Account Key**: `<WORKSPACE>\play_service_account.json`
  - Email: `<SERVICE_ACCOUNT_EMAIL>`
  - Scopes: `androidpublisher` (Google Play Developer API v3)
- **Flutter SDK** on PATH for AAB builds

## App Registry

| App Name | Package Name | Project Directory | AAB Output Path |
|----------|-------------|-------------------|-----------------|
| My App | `com.example.myapp` | `my_app/` | `build/app/outputs/bundle/release/app-release.aab` |

> **Note**: Workout Tracker uses product flavors (`free`). Build with `flutter build appbundle --release --flavor free`. All other apps use default `flutter build appbundle --release`.

## Pre-Publish Checklist (MANDATORY)

Before any AAB build, always:

1. **Bump version** in `pubspec.yaml`:
   ```
   version: x.y.z+n  ->  version: x.y.(z+1)+(n+1)
   ```
2. **Run analysis**:
   ```bash
   flutter analyze lib/
   ```
3. **Build AAB**:
   ```bash
   # Standard apps:
   flutter build appbundle --release

   # Workout Tracker (has flavors):
   flutter build appbundle --release --flavor free
   ```

## Deployment Tools

### 1. Upload AAB to Play Store (`upload_to_playstore.py`)

Located at: `<WORKSPACE>\upload_to_playstore.py`

```bash
# Upload single app to production
python upload_to_playstore.py --app flappy_rogue --action upload --track production

# Upload all apps
python upload_to_playstore.py --app all --action upload --track production

# Check status of all apps
python upload_to_playstore.py --app all --action status

# Dry-run validation (no commit)
python upload_to_playstore.py --app flappy_rogue --action upload --dry-run

# Upload to internal test track
python upload_to_playstore.py --app supzip --action upload --track internal
```

**CLI Arguments**:
- `--app`: `workout_tracker`, `flappy_rogue`, `ezan_vakti_premium`, `supzip`, `autoshare`, `all`
- `--action`: `upload`, `status`
- `--track`: `production`, `beta`, `alpha`, `internal`
- `--status`: `completed`, `draft`, `inProgress`, `halted`
- `--dry-run`: Validate without committing

### 2. Update Store Listings (`update_store_listings.py`)

Located at: `<WORKSPACE>\update_store_listings.py`

```bash
# Dry-run validation
python update_store_listings.py --dry-run

# Commit changes to Google Play
python update_store_listings.py
```

Updates titles, short descriptions, and full descriptions in multiple languages for all 5 apps.

### 3. Using the API Directly (Python)

For custom operations, import the service helper:

```python
import sys
sys.path.insert(0, r'<WORKSPACE>')

# Force UTF-8 for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

from upload_to_playstore import get_service

service = get_service()
pkg = 'com.example.myapp'

# Create edit session
edit_id = service.edits().insert(body={}, packageName=pkg).execute()['id']

# List tracks
tracks = service.edits().tracks().list(packageName=pkg, editId=edit_id).execute()

# Get store listings
listings = service.edits().listings().list(packageName=pkg, editId=edit_id).execute()

# Update a listing
service.edits().listings().update(
    packageName=pkg, editId=edit_id, language='en-US',
    body={'language': 'en-US', 'title': 'New Title', 'shortDescription': '...', 'fullDescription': '...'}
).execute()

# Commit
service.edits().commit(packageName=pkg, editId=edit_id).execute()
```

## Post-Publish Steps

After a successful AAB upload, always output release notes:

```
<en-US>
- Brief description of changes
- Bug fixes and improvements
</en-US>
```

## Store Listing Limits

| Field | Max Characters |
|-------|---------------|
| Title | 30 |
| Short Description | 80 |
| Full Description | 4000 |

## Troubleshooting

- **Windows UTF-8 errors**: Always add `sys.stdout.reconfigure(encoding='utf-8')` at script start
- **403 Permission Denied**: Service account may not have publish permissions for that app in Play Console → Settings → API access
- **Edit session expired**: Sessions expire after ~1 hour. Create a new one with `edits().insert()`
- **"Changes cannot be sent for review"**: An active/pending edit already exists. Check Publishing Overview in Play Console
