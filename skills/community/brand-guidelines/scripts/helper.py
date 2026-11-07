#!/usr/bin/env python3
"""Helper utilities for claude-community--brand-guidelines."""
import argparse
import json
import sys

def main():
    parser = argparse.ArgumentParser(description="Claude Community:Brand Guidelines helper")
    parser.add_argument("--info", action="store_true", help="Show skill information")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    args = parser.parse_args()

    info = {
        "skill": "claude-community--brand-guidelines",
        "version": "1.0.0",
        "status": "active"
    }

    if args.info:
        if args.json:
            print(json.dumps(info, indent=2))
        else:
            for k, v in info.items():
                print(f"{k}: {v}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
