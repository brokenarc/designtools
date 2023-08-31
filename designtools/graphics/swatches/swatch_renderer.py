import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from collections.abc import Sequence

from designtools.color import Color
from designtools.mathutil import Numeric


class SwatchRenderer(ABC):
    """Defines the interface that swatch renderers expose.
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
    def render(self, color_groups: Sequence[Sequence[Color]]) -> ET.Element:
        """Renders the given set of color groups as an SVG document.

        Args:
            color_groups: the color groups to render swatches for.

        Returns:
            The root element of the generated SVG document.
        """
        ...
