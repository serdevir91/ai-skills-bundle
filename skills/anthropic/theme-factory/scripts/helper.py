#!/usr/bin/env python3
"""Helper utilities for anthropic--theme-factory."""
import argparse
import json
import sys

def main():
    parser = argparse.ArgumentParser(description="Anthropic:Theme Factory helper")
    parser.add_argument("--info", action="store_true", help="Show skill information")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    args = parser.parse_args()

    info = {
        "skill": "anthropic--theme-factory",
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
