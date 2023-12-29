from collections.abc import Sequence

import cairo

from designtools.color import Color
from designtools.mathutil import Numeric
from .swatch_renderer import SwatchRenderer


class GradientBar(SwatchRenderer):

    @staticmethod
    def _add_color_stops(colors: Sequence[Color], gradient: cairo.Gradient) -> None:
        for index, color in enumerate(colors):
            offset = (index + 1) / len(colors)
            r, g, b = color.rgb
            gradient.add_color_stop_rgb(offset, r, g, b)

    def __init__(self, swatch_width: Numeric, swatch_height: Numeric):
        self._swatch_width = swatch_width
        self._swatch_height = swatch_height

    def _render_bar(self, colors: Sequence[Color], row: int, ctx: cairo.Context) -> None:
        ctx.save()
        x = 0
        y = row * self._swatch_height
        width = self._swatch_width
        height = self._swatch_height

        gradient = cairo.LinearGradient(x, y, x + width, y)
        GradientBar._add_color_stops(colors, gradient)

        ctx.set_source(gradient)
        ctx.rectangle(x, y, width, height)
        ctx.fill()

        ctx.restore()

    def compute_size(self, color_groups: Sequence[Sequence[Color]]) -> tuple[Numeric, Numeric]:
        return self._swatch_width, len(color_groups) * self._swatch_height

    def render(self, color_groups: Sequence[Sequence[Color]], ctx: cairo.Context) -> None:
        ctx.save()
        for index, colors in enumerate(color_groups):
            self._render_bar(colors, index, ctx)

        ctx.restore()
