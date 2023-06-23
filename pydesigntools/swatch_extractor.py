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
from pathlib import Path

from pydesigntools.color import group_colors
from pydesigntools.color.collectors import get_12_hue_collectors
from pydesigntools.color.sorters import hlv_step_sort_key
from pydesigntools.graphics import SwatchRenderer

HEX_COLOR = re.compile(r"(#[0-9a-f]{6}|#[0-9a-f]{3})", re.I)
"""Matches RGB hexadecimal colors, ignoring alpha."""

OUTFILE = "{0}.swatches.svg"
"""Template for the output filename when no output file is specified."""

SWATCH_RADIUS = 32
"""The diameter of each swatch circle. """

SWATCH_PADDING = SWATCH_RADIUS / 2
"""The padding around the swatch image and between the swatch rows."""


def __get_args():
    parser = ArgumentParser(
        prog="swatch_extractor",
        description="Creates an SVG swatch card from a text file",
    )

    parser.add_argument(
        "in_file", action="store",
        help="The text file to extract color codes from."
    )

    parser.add_argument(
        "out_file",
        action="store",
        nargs="?",
        help="The name of the SVG file to create.",
    )

    return parser.parse_args()


def __parse_file(filename: str) -> set[str]:
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

    return colors


def __process_colors(colors: [str]):
    groups = group_colors(colors, get_12_hue_collectors())

    # Sort each group and filter out any empty groups
    return [
        sorted(groups[key], key=hlv_step_sort_key, reverse=True)
        for key in sorted(groups.keys()) if len(groups[key]) > 0
    ]


def extract_swatches(in_file: str, out_file: str):
    colors = __parse_file(in_file)
    groups = __process_colors(colors)
    render = SwatchRenderer(SWATCH_RADIUS, SWATCH_PADDING)
    svg = render.render(groups)

    print(f"\nExtracted {len(colors)} colors from {in_file}")
    print(f"Writing swatches as {out_file}\n")

    with open(out_file, "x") as file:
        file.writelines(svg)


def main():
    args = __get_args()
    in_path = Path(args.in_file).absolute()
    out_path = args.out_file if args.out_file else str(in_path.with_name(OUTFILE.format(in_path.stem)).absolute())

    extract_swatches(str(in_path), out_path)


if __name__ == "__main__":
    main()
