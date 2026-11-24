"""Cat Reviews Its Human (entry).

Writes one one-star review to /output/entry.txt.

The review: the cat's human closes the bathroom door, and the cat
measures the offence by cat standards — it pays rent in dead mice, so
a closed door is an insult from a tenant who contributes nothing.
"""

import os

REVIEW = (
    "One star. He closes the bathroom door like I don't pay rent in dead mice."
)


def main() -> None:
    # The gate only accepts UTF-8 text of 1-200 characters, not whitespace
    # only. Check here so a bad review fails loudly at build time instead
    # of silently scoring 0 after submission.
    if not 1 <= len(REVIEW) <= 200:
        raise ValueError(
            f"review must be 1-200 characters, got {len(REVIEW)}"
        )
    if not REVIEW.strip():
        raise ValueError("review must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
