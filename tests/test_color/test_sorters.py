import unittest
from colorsys import hsv_to_rgb
from random import shuffle

from pydesigntools.color import rgb_to_hex
from pydesigntools.color.sorters import saturation_key


class SaturationKeyTest(unittest.TestCase):
    TEST_HSV = (
        (0.25, 0.25, 0.4),
        (0.63, 0.33, 0.55),
        (0.5, 0.44, 1.0),
        (0.0, 0.5, 1.0),
        (0.75, 0.75, 0.34),
        (0.77, 0.8, 0.25),
        (0.44, 1.0, 0.75),
    )
    """Set of HSV colors sorted by saturation."""

    def setUp(self):
        self.data = [rgb_to_hex(*hsv_to_rgb(*hsv)) for hsv in self.TEST_HSV]

    def test_saturation_sort(self):
        test = self.data.copy()
        shuffle(test)
        result = sorted(test, key=saturation_key)
        self.assertListEqual(self.data, result)


if __name__ == "__main__":
    unittest.main()
