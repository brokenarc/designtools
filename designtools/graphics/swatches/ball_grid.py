import math
from collections.abc import Sequence

import cairo

from designtools.color import Color
from designtools.mathutil import Numeric
from .grid_base import GridBase

HIGHLIGHT = (1.0, 0.5, 1.5)
"""The HSV transform to apply to a color to get the highlight of the ball."""

SHADOW = (1.0, 1.5, 0.5)
"""The HSV transform to apply to a color to get the shadow of the ball."""


class BallGrid(GridBase):
    @staticmethod
    def _compute_stops(color: Color, gradient: cairo.Gradient) -> None:
        gradient.add_color_stop_rgb(0, *color.hsv_transform(*HIGHLIGHT).rgb)
        gradient.add_color_stop_rgb(0.3333333, *color.rgb)
        gradient.add_color_stop_rgb(0.75, *color.rgb)
        gradient.add_color_stop_rgb(1.0, *color.hsv_transform(*SHADOW).rgb)

    def _make_ball(self, color: Color, cx: Numeric, cy: Numeric, ctx: cairo.Context) -> None:
        rg = cairo.RadialGradient(cx - (self._half_width / 2), cy - (self._half_width / 2),
                                  self._half_width * 0.1, cx, cy, self._half_width)
        BallGrid._compute_stops(color, rg)

        ctx.set_source(rg)
        ctx.arc(cx, cy, self._half_width, 0, 2 * math.pi)
        ctx.fill()

    def render_elements(self, colors: Sequence[Color], ctx: cairo.Context) -> None:
        cols, _ = self.get_grid_size(colors)

        row = 0
        column = 0
        for color in colors:
            cx, cy = self.get_center(column, row)
            self._make_ball(color, cx, cy, ctx)
            column += 1
            if column == cols:
                column = 0
                row += 1
