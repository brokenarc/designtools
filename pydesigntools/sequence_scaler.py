import csv, itertools
from argparse import ArgumentParser, Namespace
from collections.abc import MutableSequence, Sequence
from pathlib import Path
import pathlib
from typing import Optional


from pydesigntools.mathutil import (
    FIBONACCI,
    GOLDEN_POWERS,
    LUCAS,
    METALLIC_MEAN,
    PELL,
    PELL_LUCAS,
)
from pydesigntools.mathutil import Numeric, scale_sequence

SEQUENCES = {
    "Fibonacci": FIBONACCI,
    "Golden Powers": GOLDEN_POWERS,
    "Lucas": LUCAS,
    "Metallic Mean": METALLIC_MEAN,
    "Pell": PELL,
    "Pell-Lucas": PELL_LUCAS,
}

DataTable = Sequence[Sequence[Numeric]]
"""Type alias representing a sequence with a header string and its data."""

NumericTable = tuple[Sequence[str], DataTable]
"""Type alias wrapping a group of table headers with the table data."""


def _get_scaled_columns(value: Numeric, offset: Optional[int] = None) -> NumericTable:
    columns = []
    headers: MutableSequence[str] = []
    index = offset if offset else int(min(len(s) for s in SEQUENCES.values()) / 2)

    for name, seq in SEQUENCES.items():
        headers.append(name)
        columns.append(scale_sequence(seq, value, index))

    return headers, tuple(itertools.zip_longest(*columns, fillvalue=None))


def _parse_args() -> Namespace:
    parser = ArgumentParser(
        prog="sequence_scaler",
        description="Generates scaled numeric sequences to a CSV file.",
    )

    parser.add_argument(
        "file",
        action="store",
        help="The name of the CSV file to generate.",
        type=pathlib.Path,
    )

    parser.add_argument(
        "value",
        action="store",
        help="The number to scale the sequences around.",
        type=float,
    )

    parser.add_argument(
        "--offset",
        action="store",
        help="The index within the sequence to use for scaling.",
        type=int,
    )

    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    headers, rows = _get_scaled_columns(args.value, args.offset)
    with open(args.file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(rows)


if __name__ == "__main__":
    main()
