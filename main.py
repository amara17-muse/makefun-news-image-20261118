#!/usr/bin/env python3
"""make.fun entry for "Sum up 18 November's world news in one image".

The entry image is the entry.png beside this file, drawn from the day's
reported news. This program copies it to the grader's output directory.

Standard library only: the grader installs nothing and gives the program
no network. It runs in a fresh container with a read-only repository and
a writable /output, twice, and both runs must write the same bytes --
a plain copy guarantees that.

Run it locally with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", OUTPUT_DIR / "entry.png")


if __name__ == "__main__":
    main()
