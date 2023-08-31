from collections.abc import Sequence

from designtools.color import Color
from designtools.graphics.svg import Defs, Group, Rect
from .grid_base import GridBase

SQUARE_ID = "square-{0}"


class SquareGrid(GridBase):
    def render_elements(self, colors: Sequence[Color]) -> tuple[Defs | None, Group]:
        cols, _ = self.get_grid_size(colors)
        group = Group(id_="square-grid")

        row = 0
        column = 0
        for color in colors:
            cx, cy = self.get_center(column, row)
            x = cx - self._half_width
            y = cy - self._half_width
            rect = Rect(id_=SQUARE_ID.format(color.hex_code), x=x, y=y, width=self._width,
                        height=self._width, fill=f"#{color.hex_code}")
            group.append(rect)
            column += 1
            if column == cols:
                column = 0
                row += 1

        return None, group
