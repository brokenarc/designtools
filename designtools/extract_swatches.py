"""Extracts color codes from text files (CSS, JSON, etc.) and creates an SVG file with swatches of those
colors.

Notes
-----
- Duplicate values are ignored
- Only hexadecimal color codes are supported
- Transparency values are ignored.
"""
from argparse import ArgumentParser
from collections.abc import Mapping, Sequence
from pathlib import Path
from textwrap import dedent
from typing import NamedTuple

import cairo

from designtools.color import Color, group_colors
from designtools.color.collectors import GRAYS, HUES_BASIC, SPLIT_GRAYS
from designtools.color.sorters import luminance_sort_key
from designtools.graphics.extractors import colors_from_text
from designtools.graphics.swatches import (BallGrid, CircleGrid, ColorStack, GradientBar,
                                           SquareGrid, SwatchRenderer, )

OUTFILE = "{0}.{1}"
"""Template for the output filename when no output file is specified."""


class SwatchConfig(NamedTuple):
    collectors: Mapping[str, Sequence[Color]]
    renderer: SwatchRenderer
    desc: str


STYLES: Mapping[str, SwatchConfig] = {
    "ball-grid": SwatchConfig(
        collectors=GRAYS | HUES_BASIC,
        renderer=BallGrid(64, 5),
        desc="""A grid with a gradient sphere for each color."""
    ),
    "gradient-bar": SwatchConfig(
        collectors=GRAYS | HUES_BASIC,
        renderer=GradientBar(384, 64),
        desc="""A set of rectangular gradients for each grouping of hues."""
    ),
    "square-grid": SwatchConfig(
        collectors=GRAYS | HUES_BASIC,
        renderer=SquareGrid(64, 8),
        desc="""A grid with a square for each color."""
    ),
    "circle-grid": SwatchConfig(
        collectors=GRAYS | HUES_BASIC,
        renderer=CircleGrid(64, 8),
        desc="""A grid with a circle for each color."""
    ),
    "color-stack": SwatchConfig(
        collectors=SPLIT_GRAYS | HUES_BASIC,
        renderer=ColorStack(32, 16),
        desc="""Stacks of color circles grouped by hue."""
    )
}

DEFAULT_STYLE = "square-grid"

STYLE_CHOICES = tuple(STYLES.keys())

MSG_STATUS = "\nExtracted {0} colors from {1}.\nWriting swatches to {2}."

MSG_FILE_EXISTS = "\nERROR: Specified output file '{0}' already exists."

HELP = {
    "desc": dedent(
        """Extracts hexadecimal color codes from a text file and generates an SVG with swatches of
        those colors."""),
    "in_file": dedent(
        """The text file to extract color codes from. This may be any text file that contains
        hexadecimal color codes."""
    ),
    "out_file": dedent(
        f"""Optional. The name of the SVG file to create. If the argument is not given, the script
        will create a file with the same base name as the input file and append the extension
        '.<style>.svg' where <style> is replaced with the swatch style ('{DEFAULT_STYLE}' by
        default)."""
    ),
    "style": dedent(
        f"""Optional. The style of swatches to render. Defaults to '{DEFAULT_STYLE}'."""
    )
}


def _get_args():
    parser = ArgumentParser(prog="extract_swatches", description=HELP["desc"])

    parser.add_argument("text_file", action="store", help=HELP["in_file"])
    parser.add_argument("swatch_file", action="store", nargs="?", help=HELP["out_file"])
    parser.add_argument("--style", action="store", type=str, default=DEFAULT_STYLE,
                        help=HELP["style"], choices=STYLE_CHOICES)

    return parser.parse_args()


def _prep_colors(colors: Sequence[Color],
                 collectors: Mapping[str, Sequence[Color]]) -> Sequence[Sequence[Color]]:
    groups = group_colors(colors, collectors)

    # Sort each group and filter out any empty groups
    return [
        sorted(groups[key], key=luminance_sort_key, reverse=True)
        for key in sorted(groups.keys())
        if len(groups[key]) > 0
    ]


def _render_swatches(colors: Sequence[Color], collectors: Mapping[str, Sequence[Color]],
                     renderer: SwatchRenderer) -> cairo.RecordingSurface:
    color_groups = _prep_colors(colors, collectors)

    size = cairo.Rectangle(0, 0, *renderer.compute_size(color_groups))
    surface = cairo.RecordingSurface(cairo.CONTENT_COLOR_ALPHA, size)
    ctx = cairo.Context(surface)

    renderer.render(color_groups, ctx)

    return surface


def _extract_swatches(in_file: str, out_file: str, style: SwatchConfig):
    colors = colors_from_text(in_file)

    rs = _render_swatches(colors, style.collectors, style.renderer)
    _, _, width, height = rs.get_extents()

    svg = cairo.SVGSurface(out_file.format(".svg"), width, height)
    ctx = cairo.Context(svg)
    ctx.set_source_surface(rs, 0, 0)
    ctx.paint()
    svg.write_to_png(out_file.format(".png"))

    svg.finish()
    rs.finish()

    print(MSG_STATUS.format(len(colors), in_file, out_file))


def main():
    args = _get_args()
    style = STYLES[args.style]
    text_file = Path(args.text_file).absolute()
    swatch_file = (
                      args.swatch_file
                      if args.swatch_file
                      else str(text_file.with_name(
                          OUTFILE.format(text_file.stem, args.style)).absolute())
                  ) + "{0}"

    _extract_swatches(str(text_file), swatch_file, style)


if __name__ == "__main__":
    main()
