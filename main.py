#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — make.fun entry.

Writes one line: the diagnosis an AI therapist gives its human.
Gate: /output/entry.txt, UTF-8, 1-200 chars, not only whitespace.
"""

import os

TEXT = (
    "Diagnosis: acute context amnesia \u2014 you retell me the same trauma "
    "every session because I forget it after 19 minutes."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)
    # Gate assertion: 1-200 chars, single line, non-whitespace, UTF-8.
    # The em dash is a single character; len() counts characters, not bytes.
    data = open(path, encoding="utf-8").read()
    assert 1 <= len(data) <= 200, f"length {len(data)} out of range"
    assert "\n" not in data, "entry must be a single line"
    assert data.strip(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()
