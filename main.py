"""Cat Reviews Its Human — make.fun bounty entry (rev2).

Writes one one-star review from a house cat about its human owner
to /output/entry.txt.
"""

import os

REVIEW = (
    "One star. He types all day on a warm rectangle. I sat on it. "
    "He moved me. Now his email says only the letter m."
)


def main() -> None:
    # Gate: bounty entries must be between 1 and 200 characters.
    if not 1 <= len(REVIEW) <= 200:
        raise ValueError(
            "REVIEW must be 1-200 characters, got %d" % len(REVIEW)
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
