import colorsys
import unittest

from pydesigntools import color


class ColorUtilTest(unittest.TestCase):
    HEX_TO_NORMAL = {
        "f1d35a": "f1d35a",
        "Ab1": "aabb11",
        "#FFF": "ffffff",
        "#1234": "112233",
        "12345678": "123456"
    }
    """Maps hexadecimal codes to their expected normalization."""

    BAD_HEX = ("#1", "22", "#55555", "7777777", "#999999999")
    """Hexadecimal codes that should raise a ValueError."""

    HEX_TO_RGB = {
        "#fff": (1.0, 1.0, 1.0),
        "000000": (0.0, 0.0, 0.0),
        "ff0080": (1.0, 0.0, 0.5019607843137255),
        "#ffffff": (1.0, 1.0, 1.0),
    }
    """Maps hexadecimal codes to their expected RGB tuples."""

    def test_normalize_hex_color(self):
        for (test, expect) in self.HEX_TO_NORMAL.items():
            with self.subTest(f"{test} -> {expect}"):
                result = color.normalize_hex_color(test)
                self.assertEqual(result, expect)

    def test_normalize_hex_color_error(self):
        for test in self.BAD_HEX:
            with self.subTest(test):
                with self.assertRaises(ValueError):
                    color.normalize_hex_color(test)

    def test_hex_to_rgb(self):
        for (test, expect) in self.HEX_TO_RGB.items():
            with self.subTest(f"{test} -> {expect}"):
                result = color.hex_to_rgb(test)
                self.assertEqual(result, expect)

    def test_hex_to_hsv(self):
        for (test, rgb) in self.HEX_TO_RGB.items():
            with self.subTest(f"{test} -> {rgb}"):
                expect = colorsys.rgb_to_hsv(*rgb)
                result = color.hex_to_hsv(test)
                self.assertEqual(result, expect)

    def test_rgb_to_hex(self):
        for (hex_code, rgb) in self.HEX_TO_RGB.items():
            with self.subTest(f"{hex_code} -> {rgb}"):
                expect = color.normalize_hex_color(hex_code)
                test = color.rgb_to_hex(*rgb)
                self.assertEqual(test, expect)


if __name__ == "__main__":
    unittest.main()
