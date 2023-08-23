from collections.abc import Container, Mapping, Sequence

from designtools.mathutil import Range
from ._color_util import hex_to_hsv


class HsvCollector(Container[str]):
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

    def __contains__(self, hex_code: object) -> bool:
        """Checks if a color matches the criteria for this collector.

        Args:
            hex_code: The hexadecimal color code to check.

        Returns:
            ``True`` if the color matches this collector instance.
        """
        hsv = hex_to_hsv(str(hex_code))
        return hsv[self._component] in self._range


def get_hue_slice_collectors(names: Sequence[str]) -> Mapping[str, Container[str]]:
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


def get_12_hue_collectors() -> Mapping[str, Container[str]]:
    """Creates a set of hue collectors that divides the hue circle into 12
    equal slices.
    """
    names = (
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

    return get_hue_slice_collectors(names)


def get_martian_color_collectors() -> Mapping[str, Container[str]]:
    """Divides the hue circle into 24 equal slices named according to `Warren
    Mars' color wheel`_.

    .. _Warren Mars' color wheel:
        https://warrenmars.com/visual_art/theory/colour_wheel/colour_wheel.htm
    """
    names = (
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

    return get_hue_slice_collectors(names)
