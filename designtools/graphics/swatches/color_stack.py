import math
from collections.abc import Sequence

import cairo

from designtools.color import Color
from designtools.mathutil import Numeric
from .swatch_renderer import SwatchRenderer


class ColorStack(SwatchRenderer):

    def __init__(self, size: Numeric, padding: Numeric):
        self._size = size
        self._radius = size / 2
        self._padding = padding
        self._y_inc = size + padding
        self._x_inc = self._radius

    def _render_stack(self, color_group: Sequence[Color], cy: Numeric, ctx: cairo.Context) -> None:
        cx = self._padding + self._radius

        for color in color_group:
            ctx.set_source_rgb(color.rgb[0], color.rgb[1], color.rgb[2])
            ctx.arc(cx, cy, self._radius, 0, 2 * math.pi)
            ctx.fill()

            cx += self._radius

    def compute_size(self, color_groups: Sequence[Sequence[Color]]) -> tuple[Numeric, Numeric]:
        row_count = len(color_groups)
        col_count = max(len(group) for group in color_groups)

        width = ((col_count + 1) * self._radius) + (2 * self._padding)
        height = (row_count * self._y_inc) + self._padding

        return width, height

    def render(self, color_groups: Sequence[Sequence[Color]], ctx: cairo.Context) -> None:
        ctx.save()
        cy = self._padding + self._radius

        for color_group in color_groups:
            if len(color_group) > 0:
                self._render_stack(color_group, cy, ctx)
                cy += self._y_inc

        ctx.restore()
