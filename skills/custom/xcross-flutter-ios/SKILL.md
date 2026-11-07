---
name: xcross-flutter-ios
description: >-
  Build, run, hot-reload, and debug Flutter iOS applications natively on Windows
  or Linux without a Mac or Xcode using xcross. Use when the user asks to run
  Flutter apps on iOS devices from Windows, perform local iOS debugging/hot-reload,
  or manage the xcross toolchain and Darwin SDK on the D: drive.
---

# xcross Flutter iOS on Windows Skill

This skill documents how to build, run, debug, and hot-reload **Flutter iOS applications** on physical iPhone/iPad devices directly from **Windows** without requiring a Mac or Xcode, using **`xcross`** ([xcross.sh](https://xcross.sh)).

---

## 1. Environment & D: Drive Architecture

All heavy toolchains and SDKs are installed and configured on the **`D:` drive** to conserve space on the `C:` drive:

- **`xcross` CLI**: `D:\DevTools\xcross\bin\xcross.exe` (Junction: `C:\Users\<USER>\AppData\Local\xcross`)
- **Swift Toolchain (6.4+)**: `D:\DevTools\Swift` (Junction: `C:\Users\<USER>\AppData\Local\Programs\Swift`)
- **LLVM / Clang (23+)**: `D:\DevTools\LLVM\bin` (Clang, LLD `ld64.lld`, `llvm-ar`)
- **Darwin Swift SDK**: `D:\DevTools\xcross-data\swift-sdks` (Junction: `C:\Users\<USER>\AppData\Roaming\xcross`)
- **Device Tools (`pymobiledevice3`)**: `C:\Users\<USER>\AppData\Roaming\Python\Python314\Scripts`
- **Environment Variable**: `XCROSS_INSTALL_DIR = D:\DevTools\xcross`

---

## 2. Verification (`xcross doctor`)

To verify the iOS toolchain and device readiness from any terminal:

```powershell
$env:Path = [Environment]::GetEnvironmentVariable('Path', 'User') + ';' + [Environment]::GetEnvironmentVariable('Path', 'Machine')
$env:XCROSS_INSTALL_DIR = 'D:\DevTools\xcross'
xcross flutter doctor
```

All items under `[✓] iOS toolchain` (Host, swift, clang++, llvm-ar, SDKROOT, iOS clang, iOS linker, Darwin SDK) must report green/ready.

---

## 3. Physical Device Connection & Tunneling (iOS 17+)

For iOS 17 and newer devices, Apple uses CoreDevice Remote Service Discovery (RSD) tunneling over USB/Wi-Fi:

1. **Connect your iPhone via USB**:
   Ensure iTunes / Apple Mobile Device Support detects the device. Tap **Trust** on the iPhone screen if prompted.
2. **Start the RSD Tunnel** (Run in an elevated / Administrator terminal if prompted):
   ```powershell
   xcross tunnel
   ```
   *(Keep this terminal open or running in the background).*

---

## 4. Running & Debugging Flutter iOS Apps

Navigate to any Flutter project directory (e.g. `<WORKSPACE>\<project>`):

```powershell
# In the project directory:
xcross flutter run
```

### Features Supported During Run:
- **Hot Reload**: Press `r` to instantly update state and UI on the connected iPhone.
- **Hot Restart**: Press `R` to restart the app session.
- **DevTools**: Open the provided observatory / DevTools URL in your browser for performance and widget inspection.

---

## 5. Authentication & Code Signing

`xcross` handles codesigning automatically on Windows:

- **Via Apple ID (Free or Paid)**:
  ```powershell
  xcross auth --apple-id your-apple-id@example.com
  ```
- **Via App Store Connect API Key**:
  ```powershell
  xcross auth --issuer-id <ISSUER_ID> --key-id <KEY_ID> --private-key <PATH_TO_P8>
  ```
- **To Reset / Clear Saved Auth**:
  ```powershell
  xcross auth clean
  ```

---

## 6. App Store Release Note

> [!NOTE]
> `xcross` is optimized for **local development, live debugging, and on-device hot-reload** from Windows.
> For official **App Store Connect / TestFlight releases**, continue using the workspace standard: **GitHub Actions macOS Runner + `upload_to_appstore.py`** (`app-store-publish` skill).
