import csv, itertools
from argparse import ArgumentParser, Namespace
from collections.abc import MutableSequence, Sequence
from pathlib import Path
import pathlib
from typing import Optional


from pydesigntools.mathutil import (
    GOLDEN_RATIO,
    SUPERGOLDEN_RATIO,
    SILVER_RATIO,
    PLASTIC_NUMBER,
)
from pydesigntools.mathutil import Numeric, ratio_sequence

RATIOS = {
    "Golden Ratio": GOLDEN_RATIO,
    "Supergolden Ratio": SUPERGOLDEN_RATIO,
    "Silver Ratio": SILVER_RATIO,
    "Plastic Number": PLASTIC_NUMBER,
}

DataTable = Sequence[Sequence[Numeric]]
"""Type alias representing a sequence with a header string and its data."""

NumericTable = tuple[Sequence[str], DataTable]
"""Type alias wrapping a group of table headers with the table data."""


def _get_sequences(seed: float, count: int):
    data = [
        [header] + [*ratio_sequence(seed, ratio, count)]
        for header, ratio in RATIOS.items()
    ]

    return itertools.zip_longest(*data, fillvalue=None)


def _parse_args() -> Namespace:
    parser = ArgumentParser(
        prog="ratio_maker",
        description="Generates numeric sequences using known ratios to a CSV file.",
    )

    parser.add_argument(
        "file",
        action="store",
        help="The name of the CSV file to generate.",
        type=pathlib.Path,
    )

    parser.add_argument(
        "seed",
        action="store",
        help=(
            "The value to build the sequence around. This value will be in "
            "the middle of the returned sequence."
        ),
        type=float,
    )

    parser.add_argument(
        "--count",
        action="store",
        help=(
            "The number of items to be created before and after the"
            "seed value in the sequences. The length of each generated "
            "sequence will always be 2 * count + 1."
        ),
        type=int,
        default=5,
    )

    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    rows = _get_sequences(args.seed, args.count)
    with open(args.file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)


if __name__ == "__main__":
    main()
