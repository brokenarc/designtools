"""Extracts color codes from text files (CSS, JSON, etc.) and creates an SVG
file with swatches of those colors.

Notes
-----
- Duplicate values are ignored
- Only hexadecimal color codes are supported
- Transparency values are ignored.
"""

import re
from argparse import ArgumentParser
from collections.abc import Sequence
from pathlib import Path
from textwrap import dedent

from designtools.color import group_colors
from designtools.color.collectors import get_12_hue_collectors
from designtools.color.sorters import hlv_step_sort_key
from designtools.graphics import SwatchRenderer

HEX_COLOR = re.compile(r"(#[0-9a-f]{6}|#[0-9a-f]{3})", re.I)
"""Matches RGB hexadecimal colors, ignoring alpha."""

OUTFILE = "{0}.swatches.svg"
"""Template for the output filename when no output file is specified."""

SWATCH_RADIUS = 32
"""The diameter of each swatch circle. """

SWATCH_PADDING = SWATCH_RADIUS / 2
"""The padding around the swatch image and between the swatch rows."""

MSG_STATUS = "\nExtracted {0} colors from {1}.\nWriting swatches to {2}."

HELP_DESCRIPTION = dedent(
    """Extracts hexadecimal color codes from a text file and generates an SVG
    with swatches of those colors."""
)

HELP_IN_FILE = dedent(
    """The text file to extract color codes from. This may be any text file
    that contains hexadecimal color codes."""
)

HELP_OUT_FILE = dedent(
    """Optional. The name of the SVG file to create. If the argument is not
    given, the script will create a file with the same base name as the
    input file and append the extension '.swatches.svg'."""
)


def __get_args():
    parser = ArgumentParser(prog="extract_swatches", description=HELP_DESCRIPTION)

    parser.add_argument("text_file", action="store", help=HELP_IN_FILE)
    parser.add_argument("swatch_file", action="store", nargs="?", help=HELP_OUT_FILE)

    return parser.parse_args()


def __parse_file(filename: str) -> Sequence[str]:
    """Extracts the colors from a text file.

    Currently only supports hexadecimal color codes.
    """
    colors = set()
    with open(filename) as file:
        for line in file:
            colors.update(
                # Extract any hexadecimal color codes from the current line.
                [color.lower() for color in re.findall(HEX_COLOR, line)]
            )

    return tuple(colors)


def __process_colors(colors: Sequence[str]):
    groups = group_colors(colors, get_12_hue_collectors())

    # Sort each group and filter out any empty groups
    return [
        sorted(groups[key], key=hlv_step_sort_key, reverse=True)
        for key in sorted(groups.keys())
        if len(groups[key]) > 0
    ]


def extract_swatches(in_file: str, out_file: str):
    colors = __parse_file(in_file)
    groups = __process_colors(colors)
    render = SwatchRenderer(SWATCH_RADIUS, SWATCH_PADDING)
    svg = render.render(groups)

    print(MSG_STATUS.format(len(colors), in_file, out_file))

    with open(out_file, "x") as file:
        file.writelines(svg)


def main():
    args = __get_args()
    text_file = Path(args.text_file).absolute()
    swatch_file = (
        args.swatch_file
        if args.swatch_file
        else str(text_file.with_name(OUTFILE.format(text_file.stem)).absolute())
    )

    extract_swatches(str(text_file), swatch_file)


if __name__ == "__main__":
    main()
