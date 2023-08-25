import unittest
from collections.abc import Container
from typing import cast

from designtools.color import Color, hex_color
from designtools.color import group_colors


class RgbGrouper(Container[Color]):
    def __init__(self, channel: int, threshold: float):
        self._channel = channel
        self._threshold = threshold

    def __contains__(self, c: object) -> bool:
        return cast(Color, c).rgb[self._channel] > self._threshold


class GroupingTest(unittest.TestCase):
    def test_group_colors(self):
        collectors = {
            "red": RgbGrouper(0, 0.5),
            "green": RgbGrouper(1, 0.5),
            "blue": RgbGrouper(2, 0.5),
        }

        colors = (
            hex_color("00ff00"),
            hex_color("ff00ff"),
            hex_color("1122ff"),
            hex_color("111111"),
            hex_color("ffffff"),
            hex_color("00ffff"),
            hex_color("0000ff"),
            hex_color("00ff00"),
        )

        expect = {
            "red": [hex_color("ff00ff"), hex_color("ffffff")],
            "green": [hex_color("00ff00"), hex_color("00ffff")],
            "blue": [hex_color("1122ff"), hex_color("0000ff")],
        }

        test = group_colors(colors, collectors)
        self.assertListEqual(list(test.keys()), list(expect.keys()))

        for name, colors in test.items():
            self.assertListEqual(sorted(colors), sorted(expect[name]))


if __name__ == "__main__":
    unittest.main()
