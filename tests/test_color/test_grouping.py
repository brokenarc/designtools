import unittest

from designtools.color import group_colors, hex_color
from designtools.color.collectors import HsvCollector

# ----------------------------------------------------------------------------
# Trivial hue collectors
DATA_COLLECTORS = {
    "00": HsvCollector("h", 0, 0.25),
    "01": HsvCollector("h", 0.25, 0.5),
    "02": HsvCollector("h", 0.5, 0.75),
    "03": HsvCollector("h", 0.75, 1.01)
}

# ----------------------------------------------------------------------------
# Colors to group, including a duplicate.
DATA_COLORS = (
    hex_color("00ff00"),
    hex_color("ff00ff"),
    hex_color("1122ff"),
    hex_color("111111"),
    hex_color("ffffff"),
    hex_color("00ffff"),
    hex_color("0000ff"),
    hex_color("00ff00"),
)

# ----------------------------------------------------------------------------
# Expected color groupings
DATA_EXPECT = {
    "00": [hex_color("111111"), hex_color("ffffff")],
    "01": [hex_color("00ff00")],
    "02": [hex_color("1122ff"), hex_color("00ffff"), hex_color("0000ff")],
    "03": [hex_color("ff00ff")]
}


class GroupingTest(unittest.TestCase):
    def test_group_colors(self):
        test = group_colors(DATA_COLORS, DATA_COLLECTORS)
        self.assertListEqual(list(test.keys()), list(DATA_EXPECT.keys()))

        for name, colors in test.items():
            self.assertListEqual(sorted(colors), sorted(DATA_EXPECT[name]))


if __name__ == "__main__":
    unittest.main()
