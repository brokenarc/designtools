"""Extracts color codes from text files (CSS, JSON, etc.) and creates an SVG
file with swatches of those colors.

Notes
-----
- Duplicate values are ignored
- Only hexadecimal color codes are supported
- Transparency values are ignored.
"""

import mathutil
import re
from argparse import ArgumentParser
from collections.abc import Iterable
from pathlib import Path


HEX_COLOR = re.compile(r"(#[0-9a-f]{6}|#[0-9a-f]{3})", re.I)
"""Matches RGB hexadecimal colors, ignoring alpha."""

SWATCH_ROW = 8
"""Number of swatches per row."""

SWATCH_SIZE = 32
"""Width and height of each swatch."""

SVG_OPEN = '<svg viewBox="0 0 {width} {height}"' + \
    'xmlns="http://www.w3.org/2000/svg">'

SVG_CLOSE = "</svg>"

RECT_TEMPLATE = '<rect x="{x}" y="{y}" width="{width}" ' + \
    'height="{height}" stroke="none" fill="{color}"/>'


def extract_colors(line: str) -> list[str]:
    """Extracts the colors from a string.

    Currently only supports hexadecimal color codes.
    """
    return [color.lower() for color in re.findall(HEX_COLOR, line)]


def parse_file(filename: str) -> set[str]:
    """Extracts the colors from a text file."""
    colors = set()
    with open(filename) as file:
        for line in file:
            colors.update(extract_colors(line))

    return colors


def make_svg_rects(colors: Iterable[str]) -> Iterable[str]:
    """Creates a list of SVG rectangle elements as strings."""
    rects = []
    col = 0
    row = 0
    for color in colors:
        rects.append(
            RECT_TEMPLATE.format(
                x=col * SWATCH_SIZE,
                y=row * SWATCH_SIZE,
                width=SWATCH_SIZE,
                height=SWATCH_SIZE,
                color=color,
            )
        )
        col = col + 1
        if col == SWATCH_ROW:
            col = 0
            row = row + 1

    return rects


def make_svg(colors: Iterable[str]) -> Iterable[str]:
    """Creates an SVG document of color swatches as a list of strings using a
    list of colors.
    """
    svg = [
        SVG_OPEN.format(
            width=SWATCH_SIZE * SWATCH_ROW,
            height=mathutil.ceil(len(colors) / SWATCH_ROW) * SWATCH_SIZE,
        )
    ]
    svg = svg + make_svg_rects(colors)
    svg.append(SVG_CLOSE)

    return tuple(svg)


def build_arg_parser() -> ArgumentParser:
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

    return parser


def extract_swatches(in_filename, out_filename=None):
    in_path = Path(in_filename).absolute()
    out_path = out_filename
    if not out_path:
        out_path = str(in_path.with_name(f"{in_path.stem}.svg").absolute())

    colors = parse_file(in_path)
    print(f"\nExtracted {len(colors)} colors from {in_path}")
    print(f"Creating swatches as {out_path}\n")

    with open(out_path, "x") as file:
        file.writelines(make_svg(colors))


if __name__ == "__main__":
    parser = build_arg_parser()
    args = parser.parse_args()

    extract_swatches(args.in_file, args.out_file)
