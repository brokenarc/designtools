"""Provides sorting keys for Color instances."""

from ._color_util import get_luminance
from ._models import Color


def saturation_key(color: Color) -> float:
    """Allows sorting colors based on their saturation."""
    return color.hsv[1]


def value_key(color: Color) -> float:
    """Allows sorting colors based on their HSV value."""
    return color.hsv[2]


def luminance_sort_key(color: Color) -> tuple[float, float, float]:
    """Implements a basic luminance sorting key."""
    h, s, v = color.hsv
    lum = get_luminance(*color.rgb)

    return lum, s, v


def hlv_step_sort_key(color: Color, repetitions=8) -> tuple[int, float, int]:
    """Implements a luminance step-sort key.

    Args:
        color: The color being sorted.
        repetitions: A smoothing factor for the algorithm.

    Returns:
        The value to sort this color on.

    .. [Ref] https://www.alanzucconi.com/2015/09/30/colour-sorting/
    """
    h, _, v = color.hsv
    lum = get_luminance(*color.rgb)

    h2 = int(h * repetitions)
    v2 = int(v * repetitions)

    return h2, lum, v2
