#!/usr/bin/env python3
"""Write one pickup line (<=200 characters) a robot could use to
/output/entry.txt.

Entry for make.fun bounty "The Robot Pickup Line Championship"
(u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b).
Pure standard library, no network, deterministic.
"""

import os

STORY = (
    "I ran a full diagnostic on my heart and the only error it found was "
    "you - would you like to be my favorite bug?"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
