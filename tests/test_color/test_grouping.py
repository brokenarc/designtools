import unittest

from pydesigntools.color import group_colors, hex_to_rgb


class RgbGrouper:
    def __init__(self, channel: int, threshold: float):
        self._channel = channel
        self._threshold = threshold

    def __contains__(self, item):
        rgb = hex_to_rgb(item)
        return rgb[self._channel] > self._threshold


class GroupingTest(unittest.TestCase):
    COLLECTORS = {
        "red": RgbGrouper(0, 0.5),
        "green": RgbGrouper(1, 0.5),
        "blue": RgbGrouper(2, 0.5),
    }

    COLORS = (
        "00ff00",
        "ff00ff",
        "1122ff",
        "111111",
        "ffffff",
        "00ffff",
        "0000ff",
        "00ff00",
    )

    EXPECT = {
        "red": ["ff00ff", "ffffff"],
        "green": ["00ff00", "00ffff"],
        "blue": ["1122ff", "0000ff"],
    }

    def test_group_colors(self):
        test = group_colors(self.COLORS, self.COLLECTORS)
        self.assertListEqual(list(test.keys()), list(self.EXPECT.keys()))

        for name, colors in test.items():
            self.assertListEqual(sorted(colors), sorted(self.EXPECT[name]))


if __name__ == "__main__":
    unittest.main()
