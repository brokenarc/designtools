"""Various color utility functions.
"""
import colorsys

CACHE_SIZE = 64
"""The number of color conversions to cache."""


def normalize_hex_color(hex_color: str) -> str:
    """Normalizes a hexadecimal color code by doing the following:

    - Remove the # prefix if present.
    - Remove any trailing or leading whitespace.
    - Convert to lowercase.
    - Remove alpha channel if present.
    - Expand 3-character codes to 6-character codes.

    Parameters
    ----------
    hex_color : str
        The hexadecimal color code to clean up.

    Returns
    -------
    str
        A six-digit hexadecimal color code.
    """
    value = hex_color.lstrip("#").lower()

    if len(value) not in (3, 4, 6, 8):
        raise ValueError("Hexadecimal color must have 3, 4, 6, or 8 digits.")

    if len(value) == 6:
        return value
    elif len(value) == 8:
        return value[:6]

    return "".join(char + char for char in value[:3])


def hex_to_rgb(hex_color: str) -> tuple[float, ...]:
    """Creates an RGB tuple from a hexadecimal color code.

    The method will attempt to normalize the hexadecimal value.

    Parameters
    ----------
    hex_color : str
        The hexadecimal RGB color to convert. The method will normalize this
        value before creating the instance.

    Returns
    -------
    tuple[float, ...]
        The (red, green, blue) values for the color with each value expressed
        as a float from ``0`` to ``1``.

    See Also
    --------
        pydesigntools.color.color_util.normalize_hex_color
    """
    hex_safe = normalize_hex_color(hex_color)
    return (
        int(hex_safe[0: 2], 16) / 255,
        int(hex_safe[2: 4], 16) / 255,
        int(hex_safe[4: 6], 16) / 255
    )


def rgb_to_hex(red: float, green: float, blue: float) -> str:
    """Converts RGB values to a hexadecimal color value. Each component must be
    a float from ``0`` to ``1``.

    Parameters
    ----------
    red : float
    green : float
    blue : float

    Returns
    -------
    str
        A six-digit hexadecimal color code.
    """
    return "{0:0>2x}{1:0>2x}{2:0>2x}".format(
        int(red * 255), int(green * 255), int(blue * 255)
    )


def hex_to_hsv(hex_code: str) -> tuple[float, ...]:
    """Convenience method to create an HSV tuple from a hexadecimal RGB color
    code.

    Parameters
    ----------
    hex_code : str
        The hexadecimal RGB color to convert. The method will normalize this
        value before creating the instance.

    Returns
    -------
    tuple[float, ...]
        The (hue, saturation, value) values for the color with each value
        expressed as a float from ``0`` to ``1``.

    See Also
    --------
        pydesigntools.color.color_util.normalize_hex_color
    """
    return colorsys.rgb_to_hsv(*hex_to_rgb(hex_code))
