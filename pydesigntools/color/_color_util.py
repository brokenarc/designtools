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

    Args:
        hex_color: The hexadecimal color code to clean up.

    Returns:
        A six-digit hexadecimal color code.

    Raises:
        ValueError: If ``hex_color`` does not have 3, 4, 5, or 8 digits.
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

    Args:
        hex_color: The hexadecimal RGB color to convert. The method will
            normalize this value before creating the instance. See
            :meth:`normalize_hex_color`

    Returns:
        The (red, green, blue) values for the color with each value expressed
        as a float from ``0`` to ``1``.
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

    Args:
        red: The red component.
        green: The green component.
        blue: The blue component.

    Returns:
        A six-digit hexadecimal color code.
    """
    return "{0:0>2x}{1:0>2x}{2:0>2x}".format(
        int(red * 255), int(green * 255), int(blue * 255)
    )


def hex_to_hsv(hex_code: str) -> tuple[float, ...]:
    """Convenience method to create an HSV tuple from a hexadecimal RGB color
    code.

    Args:
        hex_code: The hexadecimal RGB color to convert. The method will
            normalize this value before creating the instance. See
            :meth:`normalize_hex_color`

    Returns:
        The (hue, saturation, value) values for the color with each value
        expressed as a float from ``0`` to ``1``.
    """
    return colorsys.rgb_to_hsv(*hex_to_rgb(hex_code))


def get_luminance(red: float, green: float, blue: float) -> float:
    """Computes the `relative luminance`_ for the given RGB color.

    Args:
        red: The red component.
        green: The green component.
        blue: The blue component.

    Returns:
        The relative luminance.

    .. _relative luminance:
       https://en.wikipedia.org/wiki/Relative_luminance
    """
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue
