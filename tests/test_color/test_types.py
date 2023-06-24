import unittest

from pydesigntools.color import HsvColor, RgbColor, normalize_hex_color


class RgbColorTest(unittest.TestCase):
    HEX_TO_RGB = {
        "#fff": (1.0, 1.0, 1.0),
        "000000": (0.0, 0.0, 0.0),
        "ff0080": (1.0, 0.0, 0.5019607843137255),
        "#ffffff": (1.0, 1.0, 1.0),
    }
    """Maps hexadecimal codes to their expected RGB tuples."""

    def test_to_hex(self):
        for hex_code, rgb in self.HEX_TO_RGB.items():
            with self.subTest(f"{rgb} -> {hex_code}"):
                result = RgbColor(*rgb).to_hex()
                self.assertEqual(normalize_hex_color(hex_code), result)

    def test_to_tuple(self):
        for rgb in self.HEX_TO_RGB.values():
            with self.subTest(f"{rgb}"):
                result = RgbColor(*rgb).to_tuple()
                self.assertTupleEqual(rgb, result)

    def test_iter(self):
        for rgb in self.HEX_TO_RGB.values():
            with self.subTest(f"{rgb}"):
                result = [item for item in iter(RgbColor(*rgb))]
                self.assertTupleEqual(rgb, tuple(result))

    def test_from_hex(self):
        for hex_code, rgb in self.HEX_TO_RGB.items():
            with self.subTest(f"{hex_code} -> {rgb}"):
                result = RgbColor.from_hex(hex_code)
                self.assertTupleEqual(rgb, result.to_tuple())


class HsvColorTest(unittest.TestCase):
    RGB_TO_HSV = {
        (0, 0, 0): (0, 0, 0),
        (1, 1, 1): (0, 0, 1),
        (0.25, 0.75, 0.33): (0.36000000000000004, 0.6666666666666666, 0.75),
        (0.5, 0.5, 0.5): (0, 0, 0.5),
    }

    def test_to_tuple(self):
        for hsv in self.RGB_TO_HSV.values():
            with self.subTest(f"{hsv}"):
                test = HsvColor(*hsv)
                self.assertTupleEqual(hsv, test.to_tuple())

    def test_iter(self):
        for hsv in self.RGB_TO_HSV.values():
            with self.subTest(f"{hsv}"):
                result = [item for item in iter(HsvColor(*hsv))]
                self.assertTupleEqual(hsv, tuple(result))

    def test_from_rgb(self):
        for rgb, hsv in self.RGB_TO_HSV.items():
            with self.subTest(f"{rgb} -> {hsv}"):
                test = HsvColor.from_rgb(*rgb)
                self.assertTupleEqual(hsv, test.to_tuple())


if __name__ == "__main__":
    unittest.main()
