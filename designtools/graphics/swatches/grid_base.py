import math
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from collections.abc import Sequence
from itertools import chain

from designtools.color import Color
from designtools.graphics.svg import Defs, Group, SVG
from designtools.mathutil import Numeric
from .swatch_renderer import SwatchRenderer


class GridBase(SwatchRenderer, ABC):
    __slots__ = ("_width", "_half_width", "_cell_size", "_half_cell",)

    @staticmethod
    def get_grid_size(colors: Sequence[Color]) -> tuple[int, int]:
        """Calculates the grid size for the given set of colors.

        Returns:
            The (columns, rows) size of the grid.
        """
        count = len(colors)
        columns = int(math.sqrt(count))
        rows = math.ceil(count / columns)

        return columns, rows

    def __init__(self, width: Numeric, padding: Numeric):
        self._width = width
        self._half_width = width / 2
        self._cell_size = width + (padding * 2)
        self._half_cell = self._cell_size / 2

    def get_center(self, column, row) -> tuple[Numeric, Numeric]:
        """Computes the center of a cell at the given column and row based on this grid's cell size.

        Returns:
            The (x, y) center of the cell.
        """
        return (
            (column * self._cell_size) + self._half_cell,
            (row * self._cell_size) + self._half_cell
        )

    def compute_size(
        self, color_groups: Sequence[Sequence[Color]]
    ) -> tuple[Numeric, Numeric]:
        columns, rows = GridBase.get_grid_size(tuple(chain.from_iterable(color_groups)))
        width = (columns * self._cell_size)
        height = (rows * self._cell_size)

        return width, height

    @abstractmethod
    def render_elements(self, colors: Sequence[Color]) -> tuple[Defs | None, Group]:
        pass

    def render(self, color_groups: Sequence[Sequence[Color]]) -> ET.Element:
        width, height = self.compute_size(color_groups)
        svg = SVG(viewBox=f"0 0 {width} {height}", xmlns="http://www.w3.org/2000/svg")
        colors = tuple(chain.from_iterable(color_groups))
        defs, group = self.render_elements(colors)

        if defs is not None:
            svg.append(defs)

        svg.append(group)

        return svg
