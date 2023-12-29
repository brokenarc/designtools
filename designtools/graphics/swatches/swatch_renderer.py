from abc import ABC, abstractmethod
from collections.abc import Sequence

import cairo

from designtools.color import Color
from designtools.mathutil import Numeric


class SwatchRenderer(ABC):
    """General interface for swatch renderer implementations.
    """

    @abstractmethod
    def compute_size(self, color_groups: Sequence[Sequence[Color]]) -> tuple[Numeric, Numeric]:
        """Computes the view box size for a given set of color groups.

        Args:
            color_groups: the color groups to measure

        Returns:
            The (width, height) of the view box.
        """
        ...

    @abstractmethod
    def render(self, color_groups: Sequence[Sequence[Color]], ctx: cairo.Context) -> None:
        """Renders the given set of color groups as an SVG document.

        Args:
            color_groups: the color groups to render swatches for.
            ctx: the graphics context to draw on.
        """
        ...
