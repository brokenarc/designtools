import math
from collections.abc import Sequence

import cairo

from designtools.color import Color
from .grid_base import GridBase


class CircleGrid(GridBase):
    def render_elements(self, colors: Sequence[Color], ctx: cairo.Context) -> None:
        cols, _ = self.get_grid_size(colors)

        row = 0
        column = 0
        for color in colors:
            cx, cy = self.get_center(column, row)

            ctx.set_source_rgb(color.rgb[0], color.rgb[1], color.rgb[2])
            ctx.arc(cx, cy, self._half_width, 0, 2 * math.pi)
            ctx.fill()

            column += 1
            if column == cols:
                column = 0
                row += 1
