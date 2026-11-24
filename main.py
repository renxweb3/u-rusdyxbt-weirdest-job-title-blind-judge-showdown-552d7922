#!/usr/bin/env python3
"""Weirdest Job Title — one title, entry.txt."""
import os
from pathlib import Path

ROLE = "Senior Apologizer"
FIELD = "Self-Driving Shopping Carts"


def title():
    return f"{ROLE} for {FIELD}"


if __name__ == "__main__":
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(title(), encoding="utf-8")
    print("wrote entry.txt")
