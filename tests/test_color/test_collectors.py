import unittest

from designtools.color import hsv_color
from designtools.color.collectors import HsvCollector

# ----------------------------------------------------------------------------
# Data to test collecting both hue and saturation collection.
DATA_HSV_COLLECTOR = {
    ("h", 0.25, 0.75): {
        hsv_color(0.333, 1, 1): True,
        hsv_color(0.833, 1, 1): False,
        hsv_color(0.655, 0.93, 1): True,
        hsv_color(0, 0, 0.07): False,
        hsv_color(0, 0, 1): False,
        hsv_color(0.5, 1, 1): True,
        hsv_color(0.667, 1, 1): True,
    },
    ("s", 0.0, 0.085): {

        hsv_color(0.333, 1, 1): False,
        hsv_color(0.833, 1, 1): False,
        hsv_color(0.655, 0.93, 1): False,
        hsv_color(0, 0, 0.7): True,
        hsv_color(0, 0, 1): True,
        hsv_color(0.5, 1, 1): False,
        hsv_color(0.667, 1, 1): False,
        hsv_color(0.333, 0.03, 0.27): True,
        hsv_color(0.833, 0.06, 0.47): True,
    },
}


class HsvCollectorTest(unittest.TestCase):
    def test_hue_collector(self):
        for r, data in DATA_HSV_COLLECTOR.items():
            c = HsvCollector(*r)

            with self.subTest(f"{c}"):
                for test, expect in data.items():
                    with self.subTest(f"{test} in {c} is {expect}"):
                        self.assertEqual(test in c, expect)


if __name__ == "__main__":
    unittest.main()
