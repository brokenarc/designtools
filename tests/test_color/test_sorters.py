import unittest
from random import shuffle

from designtools.color import hsv_color
from designtools.color.sorters import saturation_key

# ----------------------------------------------------------------------------
# Colors sorted by saturation.
DATA_COLORS = (
    hsv_color(0.25, 0.25, 0.4),
    hsv_color(0.63, 0.33, 0.55),
    hsv_color(0.5, 0.44, 1.0),
    hsv_color(0.0, 0.5, 1.0),
    hsv_color(0.75, 0.75, 0.34),
    hsv_color(0.77, 0.8, 0.25),
    hsv_color(0.44, 1.0, 0.75),
)


class SaturationKeyTest(unittest.TestCase):

    def test_saturation_sort(self):
        mixed_data = list(DATA_COLORS)
        shuffle(mixed_data)
        result = sorted(mixed_data, key=saturation_key)

        self.assertListEqual(list(DATA_COLORS), result)


if __name__ == "__main__":
    unittest.main()
