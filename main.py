#!/usr/bin/env python3
"""Robot wedding vow — one sentence, under 200 characters.

Entry for make.fun "Till Firmware Do Us Part": a single vow spoken by a
machine at its own wedding.
"""

import os
from pathlib import Path

LINE = "I promise to love you through every firmware update, every low battery, and every reboot — my heart is only a circuit, but it has only ever beaten for you."

def main() -> None:
    assert "\n" not in LINE and "\r" not in LINE
    assert len(LINE) < 200
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
