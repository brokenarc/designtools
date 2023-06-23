import colorsys
import unittest

from pydesigntools.color._color_util import normalize_hex_color
from src.models import RgbColor, HsvColor


class TestRgbColorModel(unittest.TestCase):
    hex_data = {
        "#fff": (1.0, 1.0, 1.0),
        "000000": (0.0, 0.0, 0.0),
        "ff0080": (1.0, 0.0, 0.5019607843137255),
        "#ffffff": (1.0, 1.0, 1.0),
    }

    def test_from_hex(self):
        for (hex_code, expect) in self.hex_data.items():
            actual = RgbColor.from_hex(hex_code)
            self.assertTupleEqual(actual, expect)

    def test_to_hex(self):
        for (hex_code, rgb) in self.hex_data.items():
            expect = normalize_hex_color(hex_code)
            color = RgbColor(*rgb)
            self.assertEqual(color.to_hex(), expect)

    def test_to_hsv(self):
        data = (
            (1.0, 0.0, 0.0),
            (0.5, 0.5, 0.5),
            (0.5, 1.0, 0.25),
            (0.33, 0.33, 1.0)
        )

        for color in data:
            rgb = RgbColor(*color)
            self.assertTupleEqual(rgb.to_hsv(), colorsys.rgb_to_hsv(*color))


class TestHsvColorModel(unittest.TestCase):
    def test_to_rgb(self):
        data = (
            (1.0, 0.0, 0.0),
            (0.5, 0.5, 0.5),
            (0.5, 1.0, 0.25),
            (0.33, 0.33, 1.0)
        )

        for color in data:
            hsv = HsvColor(*color)
            self.assertTupleEqual(hsv.to_rgb(), colorsys.hsv_to_rgb(*color))


if __name__ == '__main__':
    unittest.main()
