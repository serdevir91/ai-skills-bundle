#!/usr/bin/env python3
"""Helper utilities for Claude Community:Agent Designer."""
import argparse
import json
import sys

def main():
    parser = argparse.ArgumentParser(description="Claude Community:Agent Designer helper")
    parser.add_argument("--info", action="store_true", help="Show skill information")
    parser.add_argument("--validate", action="store_true", help="Validate skill structure")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    args = parser.parse_args()

    info = {
        "skill": "claude-community--agent-designer",
        "display_name": "Claude Community:Agent Designer",
        "version": "1.0.0",
        "status": "active"
    }

    if args.info:
        if args.json:
            print(json.dumps(info, indent=2))
        else:
            for k, v in info.items():
                print(f"{k}: {v}")
    elif args.validate:
        skill_dir = Path(__file__).parent.parent
        checks = {
            "skill_md": (skill_dir / "SKILL.md").exists(),
            "readme": (skill_dir / "README.md").exists(),
            "scripts": (skill_dir / "scripts").exists(),
        }
        if args.json:
            print(json.dumps(checks, indent=2))
        else:
            for k, v in checks.items():
                status = "PASS" if v else "FAIL"
                print(f"  {k}: {status}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
