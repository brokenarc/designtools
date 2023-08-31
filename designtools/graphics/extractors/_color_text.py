import re
from collections.abc import Sequence

from designtools.color import Color, hex_color

HEX_COLOR = re.compile(r"(#[0-9a-f]{6}|#[0-9a-f]{3})", re.I)
"""Matches RGB hexadecimal colors, ignoring alpha."""


def colors_from_text(filename: str) -> Sequence[Color]:
    """Extracts the colors from a text file.

    Currently only supports hexadecimal color codes.
    """
    colors = set()
    with open(filename) as file:
        for line in file:
            colors.update(
                # Extract any hexadecimal color codes from the current line.
                [hex_color(color) for color in re.findall(HEX_COLOR, line)]
            )

    return tuple(colors)
