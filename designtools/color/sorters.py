import colorsys
import math
from designtools.color._color_util import hex_to_hsv, hex_to_rgb, get_luminance


def saturation_key(hex_color: str) -> float:
    """Allows sorting hexadecimal RGB colors based on their saturation.

    Args:
        hex_color: The hexadecimal color being sorted.

    Returns:
        The saturation value (``0`` to ``1``) for ``hex_color``.
    """
    return hex_to_hsv(hex_color)[1]


def hlv_step_sort_key(hex_color: str, repetitions=8) -> tuple[int, float, int]:
    """Implements luminance-based key.

    Args:
        hex_color: The hexadecimal color being sorted.
        repetitions: A smoothing factor for the algorithm.

    Returns:
        The value to sort this color on.

    .. [Ref] https://www.alanzucconi.com/2015/09/30/colour-sorting/
    """
    r, g, b = hex_to_rgb(hex_color)
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    lum = get_luminance(r, g, b)

    h2 = int(h * repetitions)
    v2 = int(v * repetitions)

    return h2, lum, v2
