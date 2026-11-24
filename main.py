#!/usr/bin/env python3
"""Weirdest Job Title — one title, entry.txt.

The title is built by a small formatter from its two halves, and the
60-character gate is enforced before writing — an over-limit title
fails loudly instead of being submitted silently.
"""
import os
from pathlib import Path

MAX_CHARS = 60

ROLE = "Senior Apologizer"
FIELD = "Self-Driving Shopping Carts"


def build_title(role, field):
    if not role or not field:
        raise ValueError("title needs both a role and a field")
    return f"{role} for {field}"


def check_gate(title):
    if len(title) > MAX_CHARS:
        raise ValueError(
            f"title is {len(title)} chars, over the {MAX_CHARS}-char gate"
        )
    if "\n" in title:
        raise ValueError("title must be a single line")
    return title


def title():
    return check_gate(build_title(ROLE, FIELD))


if __name__ == "__main__":
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(title(), encoding="utf-8")
    print("wrote entry.txt")
