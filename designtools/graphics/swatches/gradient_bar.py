import xml.etree.ElementTree as ET
from collections.abc import Sequence

from designtools.color import Color
from designtools.graphics.svg import Defs, Group, LinearGradient, Rect, SVG, Stop
from designtools.mathutil import Numeric
from .swatch_renderer import SwatchRenderer

GRAD_ID = "lingrad-{0}"


class GradientBar(SwatchRenderer):
    __slots__ = ("_swatch_width", "_swatch_height")

    @staticmethod
    def _compute_stops(colors: Sequence[Color]) -> Sequence[Stop]:
        stops = []

        for index, color in enumerate(colors):
            offset = int(((index + 1) / len(colors)) * 100)
            stops.append(Stop(offset=f"{offset}%", stop_color=f"#{color.hex_code}"))

        return stops

    def __init__(self, swatch_width: Numeric, swatch_height: Numeric):
        self._swatch_width = swatch_width
        self._swatch_height = swatch_height

    def _render_bar(self, colors: Sequence[Color], row: int) -> tuple[LinearGradient, Rect]:
        gradient_id = GRAD_ID.format(row)
        gradient = LinearGradient(id_=gradient_id)
        gradient.extend(GradientBar._compute_stops(colors))
        rect = Rect(
            x=0,
            y=row * self._swatch_height,
            width=self._swatch_width,
            height=self._swatch_height,
            fill=f"url(#{gradient_id})",
        )

        return gradient, rect

    def _render_bars(self, color_groups: Sequence[Sequence[Color]]) -> tuple[Defs, Group]:
        group = Group(id_="gradient-bars")
        defs = Defs()

        for index, colors in enumerate(color_groups):
            gradient, bar = self._render_bar(colors, index)
            defs.append(gradient)
            group.append(bar)

        return defs, group

    def compute_size(self, color_groups: Sequence[Sequence[Color]]) -> tuple[Numeric, Numeric]:
        return self._swatch_width, len(color_groups) * self._swatch_height

    def render(self, color_groups: Sequence[Sequence[Color]]) -> ET.Element:
        width, height = self.compute_size(color_groups)
        defs, bar_group = self._render_bars(color_groups)

        svg = SVG(viewBox=f"0 0 {width} {height}", xmlns="http://www.w3.org/2000/svg")
        svg.append(defs)
        svg.append(bar_group)

        return svg
