#!/usr/bin/env python3
"""Texts From Your Future Self - make.fun entry.

Writes one text message, as sent by the entrant's future self, to
/output/entry.txt (1 to 200 characters per the sealed gate) and prints
exactly the same line to stdout. The joke is three beats in one breath:
the victory (finally stopped saying "I'll start Monday"), the twist
(it is now Monday for the 47th week in a row), and the payoff (the knee
sound is a warning now, not a joke). Deterministic: no input, no
randomness, no time, no network, standard library only.
"""

import os

ENTRY = (
    "Future you here. You finally stopped saying 'I'll start Monday' "
    "\u2014 because it's now Monday for the 47th week in a row. "
    "Stretch before standing up. That knee sound is a warning now, "
    "not a joke."
)

# Sealed gate: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space, and exactly one line.
assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
assert ENTRY.strip(), "entry must not be only white space"
assert "\n" not in ENTRY, "entry must be a single line"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back what was written: the judged file must hold this text.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt does not match ENTRY"
    print(ENTRY)


if __name__ == "__main__":
    main()
