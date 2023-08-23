import csv
import itertools
import pathlib
from argparse import ArgumentParser, Namespace
from collections.abc import MutableSequence, Sequence
from textwrap import dedent
from typing import Optional

from designtools.mathutil import Numeric, SCALAR_SEQUENCES, scale_sequence

DataTable = Sequence[Sequence[Numeric]]
"""Type alias representing a sequence with a header string and its data."""

NumericTable = tuple[Sequence[str], DataTable]
"""Type alias wrapping a group of table headers with the table data."""

HELP_DESCRIPTION = dedent(
    """Scales known numeric sequences around a given value and writes them as
    columns in a CSV file with sequence names in the first row.""")

HELP_EPILOG = "Known sequences: " + ", ".join(
                  [f"{k} ({len(v)} values)" for (k, v) in SCALAR_SEQUENCES.items()]
              )

HELP_FILE = dedent(
    """The name of the CSV file to generate. This file will be overwritten if
    it already exists.""")

HELP_VALUE = "The number to scale the sequences around."

HELP_OFFSET = dedent(
    """The index within the sequence that should equal the given value after
    scaling. If offset is not given, the offset will be set to half the middle
    of the shortest known sequence.""")


def _get_scaled_columns(value: Numeric, offset: Optional[int] = None) -> NumericTable:
    columns = []
    headers: MutableSequence[str] = []
    index = offset if offset else int(
        min(len(s) for s in SCALAR_SEQUENCES.values()) / 2)

    for name, seq in SCALAR_SEQUENCES.items():
        headers.append(name)
        columns.append(scale_sequence(seq, value, index))

    return headers, tuple(itertools.zip_longest(*columns, fillvalue=None))


def _parse_args() -> Namespace:
    parser = ArgumentParser(prog="scale_sequence", description=HELP_DESCRIPTION,
                            epilog=HELP_EPILOG)

    parser.add_argument("file", action="store", help=HELP_FILE, type=pathlib.Path)
    parser.add_argument("value", action="store", help=HELP_VALUE, type=float)
    parser.add_argument("--offset", action="store", help=HELP_OFFSET, type=int)

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
