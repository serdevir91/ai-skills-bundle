---
name: msstore-publish
description: >-
  Deploy Flutter and Windows apps to the Microsoft Store using MSStore CLI and
  upload_to_msstore.py. Use when the user asks to build MSIX packages, upload/publish
  to Microsoft Store, check Windows submission status, or manage Windows store apps.
  Covers AutoShare and future Windows apps.
---

# Microsoft Store Deploy & Manage Skill

This skill enables automated Microsoft Store publishing and submission management for Flutter Windows desktop applications using the pre-configured **MSStore Developer CLI** and the workspace deployment script `upload_to_msstore.py`.

---

## Prerequisites & Credentials

- **MSStore CLI** installed on PATH (`msstore --version`).
- **Partner Center & Microsoft Entra ID Authentication**:
  - Pre-configured in MSStore CLI settings (`settings.json`).
  - **Seller ID**: `<SELLER_ID>`
  - **Tenant ID**: `<TENANT_ID>` (`<TENANT_DOMAIN>`)
  - **Client ID**: `<CLIENT_ID>` (`StoreSubmissionAPI`)
  - Associated in Partner Center under **User Management > Microsoft Entra applications** with the **Manager** role.
- **Flutter SDK** with Windows desktop support (`flutter config --enable-windows-desktop`).
- **Visual Studio 2022** with C++ desktop development workload.
- **MSIX Packaging Tool**: `msix` dev_dependency in `pubspec.yaml` (`dart run msix:create`).

---

## App Registry

| App Name | Product ID | Package Identity | Package Family Name | Project Directory | MSIX Output | Store URL |
|----------|------------|------------------|---------------------|-------------------|-------------|-----------|
| My App | `<STORE_ID>` | `Publisher.MyApp` | `Publisher.MyApp_<PUBLISHER_HASH>` | `my_app/` | `build/windows/x64/runner/Release/my_app.msix` |

---

## Pre-Publish Checklist (MANDATORY)

Before building or publishing any Windows release:

1. **Bump versions in `pubspec.yaml`**:
   - Standard version:
     ```yaml
     version: 1.0.26+27
     ```
   - MSIX 4-part version (under `msix_config`):
     ```yaml
     msix_config:
       msix_version: 1.0.26.0
     ```
   *(Note: Microsoft Store requires the MSIX version to be strictly higher than the previously published version).*

2. **Run Flutter Code Analysis**:
   ```bash
   flutter analyze lib/
   ```

3. **Verify `msix_config` identity parameters**:
   Ensure `pubspec.yaml` contains correct Partner Center identity values:
   ```yaml
   msix_config:
     display_name: AutoShare
     publisher_display_name: My Company
     identity_name: Publisher.MyApp
     publisher: CN=16B64AA2-AD0A-42FD-BEE3-2DBE64B34A35
     msix_version: 1.0.26.0
     logo_path: assets/icon.png
     capabilities: internetClient, privateNetworkClientServer
     store: true
   ```

---

## Deployment Tools

### 1. Unified Deployment CLI (`upload_to_msstore.py`)

Located at: `<WORKSPACE>\upload_to_msstore.py`

```bash
# Check current submission status of AutoShare
python upload_to_msstore.py --app autoshare --action status

# List all managed apps in Partner Center account
python upload_to_msstore.py --action apps

# Get full application metadata
python upload_to_msstore.py --app autoshare --action get

# Build Windows Release & Package MSIX
python upload_to_msstore.py --app autoshare --action build

# Publish MSIX directly to Microsoft Store
python upload_to_msstore.py --app autoshare --action publish

# Publish in draft mode (without committing live)
python upload_to_msstore.py --app autoshare --action publish --no-commit

# Poll submission until PUBLISHED or FAILED
python upload_to_msstore.py --app autoshare --action poll
```

**CLI Arguments**:
- `--app`: `autoshare` (default), `all`
- `--action`: `status`, `apps`, `get`, `build`, `publish`, `poll`
- `--no-commit` / `--dry-run`: Keeps submission in draft state without committing.
- `-v, --verbose`: Enables verbose HTTP and CLI diagnostic output.

---

### 2. Direct MSStore CLI Reference

For low-level operations or manual troubleshooting:

```bash
# Verify credentials & active configuration
msstore info

# List applications
msstore apps list

# App details
msstore apps get <STORE_ID>

# Check submission status
msstore submission status <STORE_ID>

# Direct publish command
msstore publish "<WORKSPACE>\my_app" -i "<WORKSPACE>\my_app\build\windows\x64\runner\Release" -id <STORE_ID>

# Re-configure CLI credentials if secrets rotate
msstore reconfigure
```

---

## Post-Publish Steps

After any successful Windows Store submission or update:

1. Run `python upload_to_msstore.py --app autoshare --action poll` to monitor Partner Center certification and ingestion progress.
3. Commit and push the project changes to git repository.

---

## Troubleshooting Guide

- **400 Bad Request ("A valid account could not be found with given authorization token")**:
  - The Microsoft Entra Tenant is not associated with the Partner Center account.
  - Fix: Partner Center > Account settings > Tenants > Associate tenant (`<TENANT_DOMAIN>`).
- **401 Unauthorized ("Identity cannot be authorized")**:
  - The App Registration (Client ID) exists in Entra ID, but has not been linked inside Partner Center or lacks the `Manager` role.
  - Fix: Partner Center > Account settings > User management > **Microsoft Entra applications** tab > Associate application and assign **Manager** role.
- **Code Signing Error on Ingestion**:
  - Unpackaged Win32 EXEs require an expensive public EV/OV certificate.
  - Solution: Always use **MSIX (`store: true`)** packaging. The Microsoft Store automatically signs MSIX packages with its official Microsoft certificate for free upon upload.
- **MSIX Version Collision**:
  - If Microsoft Store rejects the package due to version conflict, ensure `msix_config.msix_version` in `pubspec.yaml` has incremented higher than the last published build (e.g., `1.0.25.0` -> `1.0.26.0`).
