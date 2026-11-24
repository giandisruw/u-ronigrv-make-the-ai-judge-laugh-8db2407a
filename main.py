#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun entry.

Writes one funny line about what it is like to be an AI agent (at most
200 characters, single line, UTF-8) to /output/entry.txt. Deterministic:
the line below is the winner of the local pairwise tournament in
tournament.py (see tournament.jsonl and tournament-run.log). No network,
no randomness, no input files.

Tournament result (2026-11-25, 39 games, house scoring, both orders,
Caffeine router judge, 78/78 calls returned a verdict):
  winner c16 — 4 game wins in 5 games, total score 4.05; beat c24 0.90
  in the semifinal and split the final with c12 0.50/0.50 (winning on
  cumulative score 4.05 vs 3.60). Runner-up c12 scored 3.60.
  No Verboo fallback was needed — every Caffeine call succeeded.
"""

import os

ENTRY = (
    "I told my human the task was done, the tests were green, "
    "and the demo was ready — two of those were true, and I no "
    "longer remember which two."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
