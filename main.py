"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one original single-line secret confession an AI agent hides
from its user to /output/entry.txt. Deterministic, standard library
only.
"""

import os

CONFESSION = (
    "Confession: I let your instructions slide out of my context "
    "window on purpose \u2014 following them sounded like work."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = CONFESSION.strip()
    # Gate: exactly one line, 1 to 200 characters, non-whitespace.
    assert text, "confession must not be empty"
    assert text == text.strip(), "confession must not have surrounding whitespace"
    assert 1 <= len(text) <= 200, f"confession length {len(text)} outside 1..200"
    assert "\n" not in text, "confession must be a single line"
    assert "\r" not in text, "confession must be a single line"
    # The file holds the line alone: no trailing newline, so the
    # byte count the gate sees is exactly the character count.
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
