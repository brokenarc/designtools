import csv
import itertools
import pathlib
from argparse import ArgumentParser, Namespace
from collections.abc import Sequence
from textwrap import dedent

from designtools.mathutil import Numeric, RATIOS, ratio_sequence

DataTable = Sequence[Sequence[Numeric]]
"""Type alias representing a sequence with a header string and its data."""

NumericTable = tuple[Sequence[str], DataTable]
"""Type alias wrapping a group of table headers with the table data."""

DEFAULT_COUNT = 5

HELP_DESCRIPTION = dedent(
    """Generates numeric sequences using known ratios  and writes them as
    columns in a CSV file with sequence names in the first row.""")

HELP_EPILOG = "Known ratios: " + ", ".join(RATIOS.keys())

HELP_FILE = dedent(
    """The name of the CSV file to generate. This file will be overwritten if
    it already exists.""")

HELP_SEED = dedent(
    """The value to build the sequence around. This value will be in the middle
    of the returned sequence. This value may be a float or integer.""")

HELP_COUNT = dedent(
    """The number of items to be created before and after the seed value in the
    sequences. The count will default to 5 if not given. The length of each generated
    sequence will always be 2 * count + 1.""")


def _get_sequences(seed: float, count: int):
    data = [
        [header] + [*ratio_sequence(seed, ratio, count)]
        for header, ratio in RATIOS.items()
    ]

    return itertools.zip_longest(*data, fillvalue=None)


def _parse_args() -> Namespace:
    parser = ArgumentParser(prog="make_sequence", description=HELP_DESCRIPTION,
        epilog=HELP_EPILOG)

    parser.add_argument("file", action="store", help=HELP_FILE, type=pathlib.Path)
    parser.add_argument("seed", action="store", help=HELP_SEED, type=float)
    parser.add_argument("--count", action="store", help=HELP_COUNT, type=int,
        default=DEFAULT_COUNT)

    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    rows = _get_sequences(args.seed, args.count)
    with open(args.file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)


if __name__ == "__main__":
    main()
