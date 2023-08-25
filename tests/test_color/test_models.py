import unittest

from designtools.color import Color

# ----------------------------------------------------------------------------
# Colors that should fail to initialize.
DATA_BAD_COLOR_INIT = (
    {"hex_code": None, "rgb": None, "hsv": None},
    {"hex_code": "fffff"},
    {"hex_code": "ffffxx"},
    {"hex_code": ""},
    {"rgb": (2.0, 0.0, 0.1)},
    {"rgb": (0.5, 0.0)},
    {"hsv": (2.0, 0.0, 0.1)},
    {"hsv": (0.0, 0.1)},
)

# ----------------------------------------------------------------------------
# Constructor parameters mapped to expected instance hex_code.
DATA_PARAM_PRECEDENCE = (
    ({"hex_code": "ffffff", "rgb": (1, 0, 0), "hsv": (0.5, 0.5, 0.5)}, "ffffff"),
    ({"rgb": (1, 0, 0), "hsv": (0.5, 0.5, 0.5)}, "ff0000"),
)

# ----------------------------------------------------------------------------
# Constructor parameters mapped to expected instance properties.
DATA_COLORS = (
    (
        {"hex_code": "ffd500"},
        {
            "hex_code": "ffd500",
            "rgb": (1.0, 0.8352941176470589, 0),
            "hsv": (0.1392156862745098, 1.0, 1.0),
        },
    ),
    (
        {"rgb": (0.13333333333333333, 0.4666666666666667, 1.0)},
        {
            "hex_code": "2277ff",
            "rgb": (0.13333333333333333, 0.4666666666666667, 1.0),
            "hsv": (0.6025641025641025, 0.8666666666666667, 1.0),
        },
    ),
    (
        {"hsv": (0.3333333333333333, 0.8, 1.0)},
        {
            "hex_code": "32ff32",
            "rgb": (0.19999999999999996, 1.0, 0.19999999999999996),
            "hsv": (0.3333333333333333, 0.8, 1.0),
        },
    ),
)


class ColorTest(unittest.TestCase):
    def test_bad_color_init(self):
        for params in DATA_BAD_COLOR_INIT:
            with self.subTest(params):
                with self.assertRaises(ValueError):
                    Color(**params)

    def test_init_param_precedence(self):
        for params, expect in DATA_PARAM_PRECEDENCE:
            with self.subTest(params):
                c = Color(**params)
                self.assertEqual(c.hex_code, expect)

    def test_color_data(self):
        for params, expect in DATA_COLORS:
            c = Color(**params)
            self.assertEqual(c.hex_code, expect["hex_code"])

            for a, x in zip(c.rgb, expect["rgb"]):
                self.assertAlmostEqual(a, x)

            for a, x in zip(c.hsv, expect["hsv"]):
                self.assertAlmostEqual(a, x)


if __name__ == "__main__":
    unittest.main()
