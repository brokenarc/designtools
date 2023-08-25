import unittest

from designtools import color

# ----------------------------------------------------------------------------
# Maps hexadecimal codes to their expected normalization.
DATA_NORMALIZE_HEX = {
    "f1d35a": "f1d35a",
    "Ab1": "aabb11",
    "#FFF": "ffffff",
    "#1234": "112233",
    "12345678": "123456",
}

# ----------------------------------------------------------------------------
# Hexadecimal codes that should raise a ValueError.
DATA_NORMALIZE_ERR = ("#1", "22", "#55555", "7777777", "#999999999")

# ----------------------------------------------------------------------------
# Maps hexadecimal codes to their expected RGB tuples.
DATA_HEX_RGB = {
    "#fff": (1.0, 1.0, 1.0),
    "000000": (0.0, 0.0, 0.0),
    "ff0080": (1.0, 0.0, 0.5019607843137255),
    "#ffffff": (1.0, 1.0, 1.0),
}

# ----------------------------------------------------------------------------
# Maps hexadecimal codes to their expected HSV tuples.
DATA_HEX_HSV = {
    "#fff": (0.0, 0.0, 1.0),
    "000000": (0.0, 0.0, 0.0),
    "ff0080": (0.9163398692810457, 1.0, 1.0),
    "#ffffff": (0.0, 0.0, 1.0),
}

# ----------------------------------------------------------------------------
# Maps RGB tuples to equivalent hexadecimal color
DATA_RGB_HEX = {
    (1.0, 1.0, 1.0): "ffffff",
    (0.0, 0.0, 0.0): "000000",
    (1.0, 0.0, 0.5019607843137255): "ff0080"
}


class ColorUtilTest(unittest.TestCase):
    def test_normalize_hex_color(self):
        for test, expect in DATA_NORMALIZE_HEX.items():
            with self.subTest(f"{test} -> {expect}"):
                result = color.normalize_hex_color(test)
                self.assertEqual(result, expect)

    def test_normalize_hex_color_error(self):
        for test in DATA_NORMALIZE_ERR:
            with self.subTest(test):
                with self.assertRaises(ValueError):
                    color.normalize_hex_color(test)

    def test_hex_to_rgb(self):
        for test, expect in DATA_HEX_RGB.items():
            with self.subTest(f"{test} -> {expect}"):
                result = color.hex_to_rgb(test)
                self.assertEqual(result, expect)

    def test_hex_to_hsv(self):
        for test, hsv in DATA_HEX_HSV.items():
            with self.subTest(f"{test} -> {hsv}"):
                result = color.hex_to_hsv(test)
                self.assertEqual(result, hsv)

    def test_rgb_to_hex(self):
        for rgb, hex_code in DATA_RGB_HEX.items():
            with self.subTest(f"{hex_code} -> {rgb}"):
                test = color.rgb_to_hex(*rgb)
                self.assertEqual(test, hex_code)


if __name__ == "__main__":
    unittest.main()
