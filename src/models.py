"""Provides simple color models.
"""
from __future__ import annotations

import colorsys
from typing import NamedTuple
from typing import Any, Callable, TypeVar

from pydesigntools.color._color_util import normalize_hex_color


class RgbColor(NamedTuple):
    """Simple model for an RGB color."""

    red: float = 0.0
    green: float = 0.0
    blue: float = 0.0

    @staticmethod
    def from_hex(hex_code: str) -> RgbColor:
        """Creates an instance from a hexadecimal color code.

        The method will attempt to normalize the hexadecimal value.

        Parameters
        ----------
        hex_code : str
            The hexadecimal RGB color to convert. The method will normalize this value before
            creating the instance.

        Returns
        -------
            The RGB color instance.

        See Also
        --------
            pydesigntools.color.color_util.normalize_hex_color
        """
        hex_safe = normalize_hex_color(hex_code)
        return RgbColor(*[int(hex_safe[i: i + 2], 16) / 255 for i in (0, 2, 4)])

    def to_hex(self) -> str:
        """Generates the hexadecimal representation of this color.

        The hexadecimal color code generated will be 6 characters long (8-bits per channel).

        Returns
        -------
            The hexadecimal color code.
        """
        return "{0:0>2x}{1:0>2x}{2:0>2x}".format(
            int(self.red * 255), int(self.green * 255), int(self.blue * 255)
        )

    def to_hsv(self) -> HsvColor:
        """Converts this color to HSV.

        Returns
        -------
        HsvColor
            The HSV representation of this color.
        """
        return HsvColor(*colorsys.rgb_to_hsv(self.red, self.green, self.blue))


class HsvColor(NamedTuple):
    """Simple model for an HSV color."""

    hue: float = 0.0
    saturation: float = 0.0
    value: float = 0.0

    def to_rgb(self) -> RgbColor:
        """Converts this color to RGB.

        Returns
        -------
        RgbColor
            The RGB representation of this color.
        """
        return RgbColor(*colorsys.hsv_to_rgb(self.hue, self.saturation, self.value))


class ColorData:
    """Provides a container that stores the hexadecimal, RGB, and HSV representations of a color.
    """
    __slots__ = ("_hex", "_rgb", "_hsv")

    def __init__(self, hex_code: str) -> None:
        """Creates and caches the color information for a hexadecimal color.

        Parameters
        ----------
        hex_code : str
            The hexadecimal representation of an RGB color. Alpha channel information is ignored
            and 3-character colors are expanded to 6-character versions.
        """
        self._hex = normalize_hex_color(hex_code)
        self._rgb = RgbColor.from_hex(self._hex)
        self._hsv = self._rgb.to_hsv()

    @property
    def hex_code(self) -> str:
        """The hexadecimal (and canonical) representation of this color."""
        return self._hex

    @property
    def hue(self) -> float:
        """The hue component of this color expressed as a float from 0 to 1."""
        return self._hsv.hue

    @property
    def saturation(self) -> float:
        """The saturation component of this color expressed as a float from 0 to 1."""
        return self._hsv.saturation

    @property
    def value(self) -> float:
        """The value component of this color expressed as a float from 0 to 1."""
        return self._hsv.value

    @property
    def red(self) -> float:
        """The red component of this color expressed as a float from 0 to 1."""
        return self._rgb.red

    @property
    def green(self) -> float:
        """The green component of this color expressed as a float from 0 to 1."""
        return self._rgb.green

    @property
    def blue(self) -> float:
        """The blue component of this color expressed as a float from 0 to 1."""
        return self._rgb.blue


ColorDatasSortKey = Callable[[ColorData], Any]
"""Provides the type for a sort key function to apply to ``ColorData`` instances.

Parameters
----------
ColorData
    The instance being compared.

Returns
-------
Any
    An instance that implements the rich comparison methods.
"""
