from collections.abc import Sequence

from designtools.color import Color
from designtools.graphics.svg import Circle, Defs, Group
from .grid_base import GridBase

CIRCLE_ID = "circle-{0}"


class CircleGrid(GridBase):
    def render_elements(self, colors: Sequence[Color]) -> tuple[Defs | None, Group]:
        cols, _ = self.get_grid_size(colors)
        group = Group(id_="circle-grid")

        row = 0
        column = 0
        for color in colors:
            cx, cy = self.get_center(column, row)
            c = Circle(id_=CIRCLE_ID.format(color.hex_code), cx=cx, cy=cy, r=self._half_width,
                       fill=f"#{color.hex_code}")
            group.append(c)
            column += 1
            if column == cols:
                column = 0
                row += 1

        return None, group
