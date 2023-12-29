import math
from abc import abstractmethod
from collections.abc import Sequence
from itertools import chain

import cairo

from designtools.color import Color
from designtools.mathutil import Numeric
from .swatch_renderer import SwatchRenderer

TWO_PI = 2 * math.pi


def get_color_grid(color_groups: Sequence[Sequence[Color]]) -> tuple[int, int, Sequence[Color]]:
    """Calculates the grid size for the given set of color groups.

    Returns:
        The grid size and flattened list of colors (columns, rows, colors).
    """
    colors = tuple(chain.from_iterable(color_groups))
    count = len(colors)
    columns = int(math.sqrt(count))
    rows = math.ceil(count / columns)

    return columns, rows, colors


class SwatchGrid(SwatchRenderer):
    """Provides the base utility logic for swatch grid renderers.

    Args:
        size: The width (and height) of the swatch area. Units for this value will be determined by
            the graphics context that is being rendered to.
        padding: The padding to add to each side of the swatch area. If no value is provided, a
            default of 1/8 ``size`` will be used. This results in a spacing between swatches equal
            to 1/4 of the swatch size. Units for this value are also deferred to the graphics
            context.
    """

    def __init__(self, size: Numeric, padding: Numeric | None):
        self._size = size
        self._half_size = size / 2
        self._padding = padding if padding is not None else size / 8
        self._cell_size = size + self._padding
        self._half_cell = self._cell_size / 2

    @property
    def size(self):
        return self._size

    @property
    def half_size(self):
        return self._half_size

    @property
    def padding(self):
        return self._padding

    @property
    def cell_size(self):
        return self._cell_size

    @property
    def half_cell(self):
        return self._half_cell

    def get_cell_location(self, column, row) -> tuple[Numeric, Numeric]:
        """Computes the location of the bounding box for a cell at the given row and column.

        Returns:
            The (x, y) location of the cell bounding box upper left corner.
        """
        return (column * self.cell_size), (row * self.cell_size)

    def get_cell_center(self, column, row) -> tuple[Numeric, Numeric]:
        """Computes the center of a cell at the given column and row based on this grid's cell size.

        Returns:
            The (x, y) center of the cell.
        """
        x, y = self.get_cell_location(column, row)
        half_size = self.cell_size / 2

        return x + half_size, y + half_size

    def compute_size(self, color_groups: Sequence[Sequence[Color]]) -> tuple[Numeric, Numeric]:
        """Computes the view box size for a given set of color groups.

        Args:
            color_groups: the color groups to measure

        Returns:
            The (width, height) of the view box.
        """
        columns, rows, _ = get_color_grid(color_groups)

        width = (columns * self.cell_size)
        height = (rows * self.cell_size)

        return width, height

    @abstractmethod
    def render_cell(self, ctx: cairo.Context, column: int, row: int, color: Color) -> None:
        """Renders the individual grid cell swatch.

        Args:
            ctx: The Cairo graphics context to draw on.
            column: The column for this cell.
            row: The row for this cell.
            color: The color this cell should represent.
        """
        ...

    def render(self, color_groups: Sequence[Sequence[Color]], ctx: cairo.Context) -> None:
        ctx.save()

        cols, _, colors = get_color_grid(color_groups)
        row = 0
        column = 0

        for color in colors:
            self.render_cell(ctx, column, row, color)

            column += 1
            if column == cols:
                column = 0
                row += 1

        ctx.restore()


class BallGrid(SwatchGrid):

    def __init__(self, size: Numeric, padding: Numeric | None):
        super().__init__(size, padding)

    @staticmethod
    def _add_color_stops(color: Color, gradient: cairo.Gradient) -> None:
        # The highlight color adjustment
        gradient.add_color_stop_rgb(0, *color.hsv_transform(1.0, 0.5, 1.5).rgb)
        gradient.add_color_stop_rgb(0.3333333, *color.rgb)
        gradient.add_color_stop_rgb(0.75, *color.rgb)
        # The shadow color adjustment
        gradient.add_color_stop_rgb(1.0, *color.hsv_transform(1.0, 1.5, 0.5).rgb)

    def render_cell(self, ctx: cairo.Context, column: int, row: int, color: Color):
        cx, cy = self.get_cell_center(column, row)
        rg = cairo.RadialGradient(cx - (self.half_size / 2), cy - (self.half_size / 2),
                                  self.half_size * 0.1, cx, cy, self.half_size)
        BallGrid._add_color_stops(color, rg)
        ctx.set_source(rg)
        ctx.arc(cx, cy, self.half_size, 0, TWO_PI)
        ctx.fill()


class CircleGrid(SwatchGrid):

    def __init__(self, size: Numeric, padding: Numeric | None):
        super().__init__(size, padding)

    def render_cell(self, ctx: cairo.Context, column: int, row: int, color: Color):
        cx, cy = self.get_cell_center(column, row)

        ctx.set_source_rgb(*color.rgb)
        ctx.arc(cx, cy, self.half_size, 0, TWO_PI)
        ctx.fill()


class SquareGrid(SwatchGrid):

    def __init__(self, size: Numeric, padding: Numeric | None):
        super().__init__(size, padding)

    def compute_size(self, color_groups: Sequence[Sequence[Color]]) -> tuple[Numeric, Numeric]:
        size = super().compute_size(color_groups)
        columns, rows, _ = get_color_grid(color_groups)

        return size[0] + self.padding, size[1] + self.padding

    def render_cell(self, ctx: cairo.Context, column: int, row: int, color: Color):
        x, y = self.get_cell_location(column, row)
        rx = x + self.padding
        ry = y + self.padding

        ctx.set_source_rgb(*color.rgb)
        ctx.rectangle(rx, ry, self.size, self.size)
        ctx.fill()
