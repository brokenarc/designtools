from collections.abc import Container, Mapping

from pydesigntools.mathutil import Range
from ._color_util import hex_to_hsv


class HueCollector(Container[str]):
    """Tests for membership based on a color's hue.

    The class assumes unit-less hue values from ``0`` to ``1`` when testing
    for membership.
    """

    __slots__ = ("_hue_range",)

    def __init__(self, lower_hue: float, upper_hue: float):
        """
        Parameters
        ----------
        lower_hue : float
            The lower hue boundary for this collector's range, inclusive.
        upper_hue : float
            The upper hue boundary for this collector's range, exclusive.
        """
        self._hue_range = Range(lower_hue, upper_hue)

    def __repr__(self):
        return f"HueCollector({self._hue_range.min}, {self._hue_range.max}"

    def __contains__(self, hex_code: object) -> bool:
        """Check if the given color's hue is within this instance's range.

        Parameters
        ----------
        hex_code : str
            The hexadecimal color code to check.

        Returns
        -------
            ``True`` if the color's hue is in the instance's range.
        """
        hue, *_ = hex_to_hsv(str(hex_code))
        return hue in self._hue_range


def _get_hue_slice_collectors(names: [str]) -> Mapping[str, Container[str]]:
    """Generates a set of equally spaced hue collectors based on a list of
    names.

    Parameters
    ----------
    names : [str]

    Returns
    -------
    Mapping[str, Container[str]]
    """
    slices = len(names)
    return {name: HueCollector(index / slices, (index + 1) / slices) for index, name in enumerate(names)}


def get_12_hue_collectors() -> Mapping[str, Container[str]]:
    """Divides the hue circle into 12 equal slices.

    Returns
    -------
    Mapping[str, Container[str]]
    """
    names = ("01 red", "02 orange", "03 yellow", "04 yellow-green", "05 green", "06 blue-green", "07 cyan", "08 blue",
             "09 indigo", "10 violet", "11 purple", "12 pink")

    return _get_hue_slice_collectors(names)


def get_martian_color_collectors() -> Mapping[str, Container[str]]:
    """Divides the hue circle into 24 equal slices named according to Warren
    Mars' color wheel.

    Returns
    -------
    Mapping[str, Container[str]]

    See Also
    --------
        https://warrenmars.com/visual_art/theory/colour_wheel/colour_wheel.htm
    """
    names = ("01 red", "02 orange", "03 turmeric", "04 yellow cheese", "05 yellow", "06 green grape",
             "07 chartreuse", "08 green pea", "09 green", "10 clover", "11 emerald", "12 malachite",
             "13 cyan", "14 turquoise", "15 azure", "16 royal blue", "17 blue", "18 dioxazine",
             "19 violet", "20 aniline", "21 magenta", "22 pink", "23 prickly pear", "24 red plum")

    return _get_hue_slice_collectors(names)
