import colorsys
from collections.abc import Sequence

from ._color_util import hex_to_rgb, normalize_hex_color, rgb_to_hex


class Color:
    """Provides a mechanism for storing the pre-computed hexadecimal, RGB, and
    HSV representations of a color in a single object.

    Argument precedence is ``hex_code``, ``rgb``, then ``hsv``. The first
    non-None parameter present in that order will be used, and the rest will be
    ignored.

    This class supports comparison and sorting based on its hexadecimal color
    code. Hashing is also delegated to the has of the hexadecimal code.

    Args:
        hex_code: The hexadecimal color.
        rgb: The RGB components as a tuple of floats, each on the range [0, 1].
        hsv: The HSV components as a tuple of floats, each on the range [0, 1].

    Raises:
        ValueError: If an invalid hex code is given
        ValueError: If any RGB or HSV components are outside the range [0, 1].
        ValueError: If all parameters are ``None``.
    """

    __slots__ = ("_hex", "_rgb", "_hsv")

    def __init__(
        self,
        hex_code: str | None = None,
        rgb: Sequence[float] | None = None,
        hsv: Sequence[float] | None = None,
    ):
        if hex_code:
            self._hex = normalize_hex_color(hex_code)
            self._rgb = hex_to_rgb(self._hex)
            self._hsv = colorsys.rgb_to_hsv(*self._rgb)
        elif rgb:
            if (len(rgb) == 3) and all(0 <= c <= 1 for c in rgb):
                self._rgb = rgb
                self._hex = rgb_to_hex(*self.rgb)
                self._hsv = colorsys.rgb_to_hsv(*self._rgb)
            else:
                raise ValueError("All 3 RGB components must be >= 0 and <= 1.")
        elif hsv:
            if (len(hsv) == 3) and all(0 <= c <= 1 for c in hsv):
                self._hsv = hsv
                self._rgb = colorsys.hsv_to_rgb(*self._hsv)
                self._hex = rgb_to_hex(*self.rgb)
            else:
                raise ValueError("All 3 HSV components must be >= 0 and <= 1.")
        else:
            raise ValueError("One of hex_code, rgb, or hsv must be given.")

    @property
    def hex_code(self) -> str:
        """The hexadecimal representation of the color."""
        return self._hex

    @property
    def rgb(self) -> Sequence[float]:
        """The RGB representation of the color."""
        return self._rgb

    @property
    def hsv(self) -> Sequence[float]:
        """The HSV representation of the color."""
        return self._hsv

    def __repr__(self):
        return f"Color({self._hex})"

    def __hash__(self):
        return hash(self._hex)

    def __eq__(self, other: "Color"):
        return self._hex == other._hex

    def __lt__(self, other: "Color"):
        return self._hex < other._hex

    def __gt__(self, other: "Color"):
        return self._hex > other._hex


def hex_color(hex_code: str) -> "Color":
    """Convenience function to create Color from hex code."""
    return Color(hex_code=hex_code)


def rgb_color(red: float, green: float, blue: float) -> "Color":
    """Convenience function to create Color from RGB values."""
    return Color(rgb=(red, green, blue))


def hsv_color(hue: float, saturation: float, value: float) -> "Color":
    """Convenience function to create Color from HSV values."""
    return Color(hsv=(hue, saturation, value))
