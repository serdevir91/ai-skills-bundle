---
name: app-store-publish
description: >-
  Deploy and manage iOS apps on Apple App Store Connect and TestFlight using
  App Store Connect API key (<KEY_ID>) and upload_to_appstore.py. Use when the
  user asks to build iOS apps, upload to TestFlight, check app/build status,
  manage App Store Connect versions, generate store assets/headers/screenshots,
  or inspect Apple Developer portal assets. Covers Workout Tracker, Flappy Rogue,
  Ezan Vakti Premium, SupZip, AutoShare, Snakey Rogue, and Markdown Keeper.
---

# Apple App Store Connect Deploy & Asset Management Skill

This skill provides the end-to-end standard for building, deploying, managing, and preparing store assets for Flutter iOS applications on **Apple App Store Connect** and **TestFlight** using the workspace credentials (`<KEY_ID>`).

---

## 1. Credentials & Configuration

- **API Key ID**: `<KEY_ID>`
- **Issuer ID**: `<ISSUER_ID>` (UUID)
- **Private Key (`.p8`)**:
  - `<WORKSPACE>\AuthKey_<KEY_ID>.p8`
  - `<WORKSPACE>\apple_credentials\AuthKey_<KEY_ID>.p8`
- **Credentials File**: `<WORKSPACE>\app_store_credentials.json`
- **GitHub Actions Secrets**:
  - `APP_STORE_CONNECT_KEY_IDENTIFIER`: `<KEY_ID>`
  - `APP_STORE_CONNECT_ISSUER_ID`: `<ISSUER_ID>`
  - `APP_STORE_CONNECT_PRIVATE_KEY`: Raw contents of `AuthKey_<KEY_ID>.p8`
  - `CERT_KEY_BASE64`: Base64 encoded p12 distribution certificate

---

## 2. App Icon Specifications (Strict Apple Requirements)

Apple strictly rejects or shows wireframes for icons that violate these rules:

1. **NO Transparency / Alpha Channel**:
   - Master icon must be strictly **RGB 24-bit** (NOT RGBA 32-bit).
   - In `pubspec.yaml` under `flutter_launcher_icons`:
     ```yaml
     flutter_launcher_icons:
       ios: true
       image_path: "assets/icon/icon.png"
       remove_alpha_ios: true # MANDATORY to prevent rejection
     ```
   - Verify with Python Pillow:
     ```python
     from PIL import Image
     im = Image.open('icon.png')
     if im.mode != 'RGB':
         im.convert('RGB').save('icon.png')
     ```
2. **Icon Dimensions**:
   - Master App Store icon: `1024 x 1024 px`
   - Location: `ios/Runner/Assets.xcassets/AppIcon.appiconset/`

---

## 3. Store Visual Assets Specifications

### A. Screenshots (`appScreenshotSets`)
All screenshots must be strictly **RGB (PNG or JPEG, no transparency)**:
| Display Type | Resolution | Devices Covered | Set Name |
|--------------|------------|-----------------|----------|
| **iPhone 6.7"** | `1290 x 2796` | iPhone 16 Pro Max, 15 Pro Max, 14 Pro Max | `APP_IPHONE_67` |
| **iPhone 6.5"** | `1242 x 2688` | iPhone 11 Pro Max, XS Max | `APP_IPHONE_65` |
| **iPad Pro 12.9"** | `2048 x 2732` | iPad Pro 12.9" (3rd-6th gen) | `APP_IPAD_PRO_3GEN_129` |

### B. Creative Assets / Asset Library (`appAssetLibraryImages` & `placements`)
Apple allows dedicated creative graphics above screenshots:

1. **Product Page Header (Ürün Sayfası Başlığı)**:
   - **Resolution**: `3840 x 1646 px` (21:9 Aspect Ratio) or `5244 x 2950 px` (16:9)
   - **Format**: PNG or JPEG, strictly RGB (no alpha)
   - **API Category**: `CREATIVE_ASSETS`
   - **API Placement**: `placementType: 'PRODUCT_PAGE_HEADER_ASSET'`

2. **Search Results Asset (Arama Sonuçları Görseli)**:
   - **Resolution**: `3840 x 2560 px` (3:2 Aspect Ratio), `1920 x 1280 px`, or `5244 x 2950 px` (16:9)
   - **Format**: PNG or JPEG, strictly RGB (no alpha)
   - **API Category**: `CREATIVE_ASSETS`
   - **API Placement**: `placementType: 'APP_STORE_SEARCH_RESULTS_ASSET'`

### C. Asset Upload Workflow (API)
```python
# 1. Reserve Asset
POST /v1/appAssetLibraryImages
{ "data": { "type": "appAssetLibraryImages", "attributes": { "category": "CREATIVE_ASSETS", "fileName": name, "fileSize": size }, "relationships": { "assetLibrary": { "data": { "type": "appAssetLibraries", "id": app_id } } } } }

# 2. Upload Binary Chunks via PUT
PUT <uploadOperation.url> (data=bytes, headers=requestHeaders)

# 3. Commit Upload
PATCH /v1/appAssetLibraryImages/<asset_id>
{ "data": { "type": "appAssetLibraryImages", "id": asset_id, "attributes": { "uploaded": True } } }

# 4. Create Placement
POST /v1/appAssetLibraryPlacements
{ "data": { "type": "appAssetLibraryPlacements", "attributes": { "placementType": "PRODUCT_PAGE_HEADER_ASSET" }, "relationships": { "appStoreVersionLocalization": { "data": { "type": "appStoreVersionLocalizations", "id": loc_id } }, "image": { "data": { "type": "appAssetLibraryImages", "id": asset_id } } } } }
```

---

## 4. Metadata Guidelines & Restrictions

1. **NO EMOJIS IN DESCRIPTION**:
   - Apple App Store API rejects descriptions containing emojis (`⭐, 🏋️, 📋, 📊, 🔒, etc.`) with HTTP 409 `INVALID_CHARACTERS`.
   - Use clean text formatting: uppercase headers, bullet hyphens (`-`), or bullet dots (`•`).
2. **Field Limits**:
   - **Promotional Text**: Max 170 characters. Editable anytime without a new build.
   - **Keywords**: Max 100 characters. Comma-separated, no spaces between commas to maximize keyword count.
   - **Description**: Max 4,000 characters.
   - **Subtitle**: Max 30 characters.
   - **Copyright**: Format: `YYYY Developer Name` (e.g. `2026 Serdar Devir`).
3. **App Review Information (`appStoreReviewDetails`)**:
   - `demoAccountRequired`: Set to `false` if the app does not require login or registration.
   - Contact fields are mandatory when patching review details: `contactFirstName`, `contactLastName`, `contactEmail`, `contactPhone` (must include `+` country code: `+90 5...`).
   - Reviewer Notes: Clearly state if the app operates fully offline or without accounts.

---

## 5. Build & CI/CD Pipeline (GitHub Actions)

### Runner Compatibility Warning:
- **Use `macos-15` runner**: Contains Xcode 16.4+ (iOS 18 SDK).
- `macos-14` uses Xcode 16.2 which triggers build errors on modern plugins (`isiOSAppOnVision` in `device_info_plus`, `introductoryOfferEligibility` in `in_app_purchase_storekit`).

### GitHub Actions Workflow Structure (`.github/workflows/ios_build.yml`):
```yaml
name: Build and Upload iOS

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: macos-15
    steps:
      - uses: actions/checkout@v4
      - uses: subosito/flutter-action@v2
        with:
          flutter-version: '3.29.0'
          channel: 'stable'
          cache: true

      - name: Setup Signing Certificate
        run: |
          echo "$CERT_KEY_BASE64" | base64 --decode > certificate.p12
          security create-keychain -p "" build.keychain
          security default-keychain -s build.keychain
          security unlock-keychain -p "" build.keychain
          security import certificate.p12 -k build.keychain -P "$CERT_PASSWORD" -T /usr/bin/codesign
          security set-key-partition-list -S apple-tool:,apple: -s -k "" build.keychain

      - name: Build IPA
        run: flutter build ipa --release --export-options-plist=ExportOptions.plist

      - name: Upload to App Store Connect
        run: |
          mkdir -p ~/.appstoreconnect/private_keys
          echo "$APP_STORE_CONNECT_PRIVATE_KEY" > ~/.appstoreconnect/private_keys/AuthKey_${{ secrets.APP_STORE_CONNECT_KEY_IDENTIFIER }}.p8
          xcrun altool --upload-app \
            -f build/ios/ipa/*.ipa \
            -t ios \
            --apiKey ${{ secrets.APP_STORE_CONNECT_KEY_IDENTIFIER }} \
            --apiIssuer ${{ secrets.APP_STORE_CONNECT_ISSUER_ID }}
```

---

## 6. In-App Subscriptions (StoreKit 2)

1. **Product IDs**: Must exactly match the app's Dart billing service (e.g. `premium_monthly`, `premium_yearly`).
2. **Subscription Setup Checklist**:
   - Subscription Group created.
   - Localizations (en-US, tr, etc.) added for each subscription with clear title and description.
   - Price schedules configured for primary currency tiers.
   - Review notes and screenshot attached for App Review approval.

---

## 7. App Registry Reference

| App Name | Bundle ID | App Store ID | Directory |
|----------|-----------|--------------|-----------|
| My App | `com.example.myapp` | `<APPLE_ID>` | `my_app/` |

---

## 8. Release Guardrail

1. Increment `pubspec.yaml` version: `version: x.y.z+n -> version: x.y.(z+1)+(n+1)`
2. Ensure encryption flag in `Info.plist`: `<key>ITSAppUsesNonExemptEncryption</key><false/>`
3. Check build state via `python upload_to_appstore.py --action builds` until `processingState == 'VALID'`.
4. Output release notes in `<en-US>...</en-US>` tags upon completion.
