#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — make.fun entry.

Writes one line to /output/entry.txt: the funniest honest error message
an appliance could show. Deterministic: no randomness, no network, no
clock. The toaster speaks in its own flat, put-upon voice, and the joke
comes from the truth of the fault — the dial numbers on a toaster mean
nothing, and the toaster knows it.
"""

import argparse
import hashlib
import sys
from pathlib import Path

ENTRY = "I burned the toast again. The setting was 3. I do not know what 3 means either."

OUTPUT = Path("/output/entry.txt")


def self_check(text: str) -> None:
    """Gate: UTF-8 text, 1-200 characters, one line, not only whitespace."""
    if not text:
        raise SystemExit("gate failed: entry is empty")
    if text != text.strip():
        raise SystemExit("gate failed: entry has leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate failed: entry is not a single line")
    if not text.strip():
        raise SystemExit("gate failed: entry is only whitespace")
    if len(text) > 200:
        raise SystemExit(f"gate failed: entry is {len(text)} characters, over 200")
    text.encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Write the appliance error entry.")
    parser.add_argument("--output", default=str(OUTPUT), help="path of entry.txt to write")
    parser.add_argument("--check-only", action="store_true",
                        help="only run the gate self-check, write nothing")
    args = parser.parse_args()

    self_check(ENTRY)
    if args.check_only:
        print(f"check-only: gate passed ({len(ENTRY)} chars)")
        return 0

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    # Verify what landed on disk, byte for byte, before reporting success.
    written = out.read_text(encoding="utf-8")
    if written != ENTRY:
        raise SystemExit("gate failed: written file differs from entry")
    self_check(written)
    digest = hashlib.sha256(ENTRY.encode("utf-8")).hexdigest()
    print(f"wrote {out} ({len(ENTRY)} chars, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
