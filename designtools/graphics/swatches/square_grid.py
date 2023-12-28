from collections.abc import Sequence

import cairo

from designtools.color import Color
from .grid_base import GridBase


class SquareGrid(GridBase):
    def render_elements(self, colors: Sequence[Color], ctx: cairo.Context) -> None:
        cols, _ = self.get_grid_size(colors)

        row = 0
        column = 0
        for color in colors:
            cx, cy = self.get_center(column, row)
            x = cx - self._half_width
            y = cy - self._half_width

            ctx.set_source_rgb(color.rgb[0], color.rgb[1], color.rgb[2])
            ctx.rectangle(x, y, self._width, self._width)
            ctx.fill()

            column += 1
            if column == cols:
                column = 0
                row += 1
