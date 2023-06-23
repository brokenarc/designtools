import colorsys
import math
from pydesigntools.color._color_util import hex_to_hsv, hex_to_rgb


def saturation_key(hex_color: str) -> float:
    """Allows sorting hexadecimal RGB colors based on their saturation.

    Parameters
    ----------
    hex_color : str
        The hexadecimal color being sorted.

    Returns
    -------
    float
        The saturation value (``0`` to ``1``) for ``hex_color``.
    """
    return hex_to_hsv(hex_color)[1]


def hlv_step_sort_key(hex_color: str, repetitions=8) -> tuple[int, float, int]:
    """Implements luminance-based key.

    Parameters
    ----------
    hex_color : str
        The hexadecimal color being sorted.
    repetitions : int
        A smoothing factor for the algorithm.

    Returns
    -------
    tuple[int, float, int]
        The value to sort this color on.

    See Also
    --------
        https://www.alanzucconi.com/2015/09/30/colour-sorting/
        https://en.wikipedia.org/wiki/Relative_luminance
    """
    r, g, b = hex_to_rgb(hex_color)
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    lum = 0.2126 * r + 0.7152 * g + 0.0722 * b

    h2 = int(h * repetitions)
    v2 = int(v * repetitions)

    return h2, lum, v2
