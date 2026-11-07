#!/usr/bin/env python3
"""Audit Flutter projects for baseline feature coverage."""

from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable


EXCLUDE_DIRS = {
    ".git",
    ".dart_tool",
    "build",
    ".idea",
    ".vscode",
    ".vs",
    "ios",
    "android",
    "linux",
    "macos",
    "windows",
    "web",
}

AMOLED_MARKERS = ("amoled", "pure_black", "ispureblack", "background_mode")
UPDATE_MARKERS = (
    "checkforupdate",
    "updateservice",
    "app_update_service",
    "appupdaterservice",
    "app_updater_service",
    "new_version_plus",
    "upgrader",
)
REVIEW_API_MARKERS = (
    "requestreview",
    "openstorelisting",
    "openstorereviewpage",
    "requestinappreviewwithfallback",
)
SETTINGS_REVIEW_MARKERS = ("rate", "review", "in_app_review")


@dataclass
class AuditResult:
    app: str
    path: str
    theme_mode_found: bool
    amoled_found: bool
    update_found: bool
    review_dependency_found: bool
    review_api_found: bool
    review_settings_entry_found: bool
    missing: list[str]

    @property
    def passed(self) -> bool:
        return not self.missing


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def _iter_flutter_apps(root: Path) -> Iterable[Path]:
    for pubspec in root.rglob("pubspec.yaml"):
        parent = pubspec.parent
        if any(part in EXCLUDE_DIRS for part in parent.parts):
            continue
        if not (parent / "lib" / "main.dart").exists():
            continue
        yield parent


def _collect_lib_text(app_root: Path) -> str:
    chunks: list[str] = []
    lib_root = app_root / "lib"
    if not lib_root.exists():
        return ""
    for file in lib_root.rglob("*.dart"):
        chunks.append(_read_text(file).lower())
    return "\n".join(chunks)


def _find_settings_text(app_root: Path) -> str:
    chunks: list[str] = []
    lib_root = app_root / "lib"
    if not lib_root.exists():
        return ""
    for file in lib_root.rglob("*settings*.dart"):
        chunks.append(_read_text(file).lower())
    return "\n".join(chunks)


def _contains_any(text: str, markers: tuple[str, ...]) -> bool:
    return any(marker in text for marker in markers)


def _contains_theme_mode(text: str) -> bool:
    return bool(re.search(r"\bthememode\b", text))


def audit_app(app_root: Path) -> AuditResult:
    pubspec_text = _read_text(app_root / "pubspec.yaml").lower()
    lib_text = _collect_lib_text(app_root)
    settings_text = _find_settings_text(app_root)

    theme_mode_found = _contains_theme_mode(lib_text)
    amoled_found = _contains_any(lib_text, AMOLED_MARKERS)
    update_found = _contains_any(lib_text, UPDATE_MARKERS)

    review_dependency_found = "in_app_review" in pubspec_text
    review_api_found = _contains_any(lib_text, REVIEW_API_MARKERS)
    review_settings_entry_found = _contains_any(settings_text, SETTINGS_REVIEW_MARKERS)

    missing: list[str] = []
    if not (theme_mode_found and amoled_found):
        missing.append("theme(light-dark-amoled)")
    if not update_found:
        missing.append("update-tracking")
    if not (review_dependency_found and review_api_found and review_settings_entry_found):
        missing.append("rate-review-flow")

    return AuditResult(
        app=app_root.name,
        path=str(app_root),
        theme_mode_found=theme_mode_found,
        amoled_found=amoled_found,
        update_found=update_found,
        review_dependency_found=review_dependency_found,
        review_api_found=review_api_found,
        review_settings_entry_found=review_settings_entry_found,
        missing=missing,
    )


def print_text(results: list[AuditResult]) -> None:
    print("Flutter Feature Audit")
    print("====================")
    print(f"Apps found: {len(results)}")
    print("")
    for item in results:
        status = "PASS" if item.passed else "MISSING"
        print(f"[{status}] {item.app}")
        print(f"  path: {item.path}")
        print(f"  theme_mode: {item.theme_mode_found}")
        print(f"  amoled: {item.amoled_found}")
        print(f"  update: {item.update_found}")
        print(f"  review_dep: {item.review_dependency_found}")
        print(f"  review_api: {item.review_api_found}")
        print(f"  review_settings: {item.review_settings_entry_found}")
        if item.missing:
            print(f"  missing: {', '.join(item.missing)}")
        print("")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit Flutter baseline features.")
    parser.add_argument("root", nargs="?", default=".", help="Root directory to scan.")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Print JSON output.")
    args = parser.parse_args()

    root = Path(os.path.expanduser(args.root)).resolve()
    apps = sorted(set(_iter_flutter_apps(root)))
    results = [audit_app(app) for app in apps]

    if args.as_json:
        print(json.dumps([asdict(r) | {"passed": r.passed} for r in results], ensure_ascii=False, indent=2))
    else:
        print_text(results)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
