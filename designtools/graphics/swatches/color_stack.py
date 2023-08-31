import xml.etree.ElementTree as ET
from collections.abc import Sequence

from designtools.color import Color
from designtools.graphics.svg import Circle, Group, SVG
from designtools.mathutil import Numeric
from .swatch_renderer import SwatchRenderer

STACK_ID = "stack-{0}"
CIRCLE_ID = "circle-{0}"


class ColorStack(SwatchRenderer):
    __slots__ = ("_size", "_radius", "_padding", "_y_inc", "_x_inc")

    def __init__(self, size: Numeric, padding: Numeric):
        self._size = size
        self._radius = size / 2
        self._padding = padding
        self._y_inc = size + padding
        self._x_inc = self._radius

    def _render_stack(self, index: int, color_group: Sequence[Color], cy: Numeric) -> Group:
        stack = Group(id_=STACK_ID.format(index))
        cx = self._padding + self._radius

        for color in color_group:
            stack.append(
                Circle(id_=CIRCLE_ID.format(color.hex_code), cx=cx, cy=cy, r=self._radius,
                       stroke="none", fill=f"#{color.hex_code}")
            )
            cx += self._radius

        return stack

    def _render_groups(self, color_groups: Sequence[Sequence[Color]]) -> Group:
        cy = self._padding + self._radius
        group = Group(id_="color-stacks")

        for index, color_group in enumerate(color_groups):
            if len(color_group) > 0:
                group.append(self._render_stack(index, color_group, cy))
                cy += self._y_inc

        return group

    def compute_size(self, color_groups: Sequence[Sequence[Color]]) -> tuple[Numeric, Numeric]:
        row_count = len(color_groups)
        col_count = max(len(group) for group in color_groups)

        width = ((col_count + 1) * self._radius) + (2 * self._padding)
        height = (row_count * self._y_inc) + self._padding

        return width, height

    def render(self, color_groups=Sequence[Sequence[Color]]) -> ET.Element:
        width, height = self.compute_size(color_groups)
        svg = SVG(viewBox=f"0 0 {width} {height}", xmlns="http://www.w3.org/2000/svg")
        svg.append(self._render_groups(color_groups))

        return svg
