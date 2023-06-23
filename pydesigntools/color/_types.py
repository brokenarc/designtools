import colorsys
from abc import ABC, abstractmethod
from collections.abc import Iterator

from ._color_util import normalize_hex_color, rgb_to_hex


class ColorABC(ABC):
    @abstractmethod
    def to_tuple(self) -> tuple[float, ...]:
        """Returns this color's components.

        The ordering of the components within the tuple is up to the
        implementation, but it is recommended that this ordering follow the
        conventions in Python's `colorsys` module.

        See Also
        --------
            colorsys
        """
        pass

    def __iter__(self) -> Iterator[float]:
        """Allows iterating over this color's components in the order defined
        by the class' ``to_tuple`` implementation.
        """
        return iter(self.to_tuple())


class RgbColor(ColorABC):
    """Models an RGB color with supporting utilities.
    """
    __slots__ = ("_red", "_green", "_blue")

    def __init__(self, red: float, green: float, blue: float):
        self._red = red
        self._green = green
        self._blue = blue

    def __repr__(self):
        return f"RgbColor({self._red, self._green, self._blue}"

    @property
    def red(self) -> float:
        return self._red

    @property
    def green(self) -> float:
        return self._green

    @property
    def blue(self) -> float:
        return self._blue

    def to_hex(self) -> str:
        """Converts this instance to a six-digit (8-bits per color)
        hexadecimal color value.

        Returns
        -------
        str
            A six-digit hexadecimal color code.

        See Also
        --------
            pydesigntools.color.rgb_to_hex
        """
        return rgb_to_hex(self._red, self._green, self._blue)

    def to_tuple(self) -> tuple[float, ...]:
        """Returns this color's components as a tuple.

        Returns
        -------
        tuple[float, ...]
            ``(red, green, blue)``, with each element a float from ``0`` to
            ``1``.
        """
        return self._red, self._green, self._blue

    @staticmethod
    def from_hex(hex_code: str) -> "RgbColor":
        """Creates an RGB color from a hexadecimal color code.

        The method will attempt to normalize the hexadecimal value.

        Parameters
        ----------
        hex_code : str
            The hexadecimal color code to convert.

        Returns
        -------
        RgbColor
            The new RGB color instance
        """
        hex_safe = normalize_hex_color(hex_code)
        return RgbColor(
            int(hex_safe[0: 2], 16) / 255,
            int(hex_safe[2: 4], 16) / 255,
            int(hex_safe[4: 6], 16) / 255
        )


class HsvColor(ColorABC):
    """Models an HSV color with supporting utilities.
    """
    __slots__ = ("_hue", "_saturation", "_value")

    def __init__(self, hue: float, saturation: float, value: float):
        self._hue = hue
        self._saturation = saturation
        self._value = value

    def __repr__(self):
        return f"HsvColor({self._hue}, {self._saturation}, {self._value})"

    @property
    def hue(self):
        return self._hue

    @property
    def saturation(self):
        return self._saturation

    @property
    def value(self):
        return self._value

    def to_tuple(self) -> tuple[float, ...]:
        """Returns this color's components as a tuple.

        Returns
        -------
        tuple[float, ...]
            ``(hue, saturation, value)``, with each element a float from ``0``
            to ``1``.
        """
        return self._hue, self._saturation, self._value

    @staticmethod
    def from_rgb(red: float, green: float, blue: float) -> "HsvColor":
        """Creates an HSV color from RGB values (each a float from ``0`` to
        ``1``).

        Parameters
        ----------
        red : float
        green : float
        blue : float

        Returns
        -------
            The new HSV color instance.
        """
        return HsvColor(*colorsys.rgb_to_hsv(red, green, blue))
