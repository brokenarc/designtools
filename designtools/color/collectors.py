from collections.abc import Container, Mapping, Sequence
from typing import cast

from designtools.common import ContainerChain
from designtools.mathutil import Range
from ._models import Color


class HsvCollector(Container[Color]):
    """Tests for membership based on one of a color's HSV components.

    The class assumes unit-less component values from ``0`` to ``1`` when
    testing for membership.

    Args:
        lower_bound: The lower hue boundary for this collector's range,
            inclusive.
        upper_bound: The upper hue boundary for this collector's range,
            exclusive.
    """

    COMPONENTS = ("h", "s", "v")
    __slots__ = ("_range", "_component")

    def __init__(self, component: str, lower_bound: float, upper_bound: float):
        if component not in HsvCollector.COMPONENTS:
            raise ValueError(f"component must be one of {HsvCollector.COMPONENTS}")

        self._component = HsvCollector.COMPONENTS.index(component)
        self._range = Range(lower_bound, upper_bound)

    def __repr__(self):
        return f"""HsvCollector("{self._component}", {self._range.min}, {self._range.max})"""

    def __contains__(self, color: object) -> bool:
        """Checks if an HSV color matches the criteria for this collector."""

        return cast(Color, color).hsv[self._component] in self._range


def segment_hues(names: Sequence[str]) -> Mapping[str, Container[str]]:
    """Generates a set of equally spaced hue collectors with the given names,
    assigned in the order that the names are given.

    Args:
        names: The strings that will be used as keys in the resulting mapping.

    Returns:
        The newly created hue collectors.
    """
    slices = len(names)
    return {
        name: HsvCollector("h", index / slices, (index + 1) / slices)
        for index, name in enumerate(names)
    }


GRAYS = {
    "00 dark grays": ContainerChain(
        HsvCollector("s", 0, 0.15), HsvCollector("v", 0, 0.5)
    ),
    "00 light grays": ContainerChain(
        HsvCollector("s", 0, 0.15), HsvCollector("v", 0, 1.1)
    ),
}
"""Collects shades of gray. Prefix this mapping to a collectors mapping to group
the neutrals separately."""

HUES_BASIC = segment_hues(
    (
        "01 red",
        "02 orange",
        "03 yellow",
        "04 yellow-green",
        "05 green",
        "06 blue-green",
        "07 cyan",
        "08 blue",
        "09 indigo",
        "10 violet",
        "11 purple",
        "12 pink",
    )
)
"""Basic division of the hue circle into 12 equal segments."""

HUES_MARTIAN = segment_hues(
    (
        "01 red",
        "02 orange",
        "03 turmeric",
        "04 yellow cheese",
        "05 yellow",
        "06 green grape",
        "07 chartreuse",
        "08 green pea",
        "09 green",
        "10 clover",
        "11 emerald",
        "12 malachite",
        "13 cyan",
        "14 turquoise",
        "15 azure",
        "16 royal blue",
        "17 blue",
        "18 dioxazine",
        "19 violet",
        "20 aniline",
        "21 magenta",
        "22 pink",
        "23 prickly pear",
        "24 red plum",
    )
)
"""Divides the hue circle into 24 equal segments named according to
`Warren Mars' color wheel`_.

.. _Warren Mars' color wheel:
    https://warrenmars.com/visual_art/theory/colour_wheel/colour_wheel.htm
"""
