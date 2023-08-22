import unittest

from designtools import mathutil

# Range test data
# (params, include, repr, str)
RANGE_DATA = (
    ((0, 10, True, False), (5, True), "Range(0, 10, True, False)", "Range [0, 10)"),
    ((0, 10, True, False), (-5, False), "Range(0, 10, True, False)", "Range [0, 10)"),
    ((0, 10, True, False), (0, True), "Range(0, 10, True, False)", "Range [0, 10)"),
    ((0, 10, True, False), (10, False), "Range(0, 10, True, False)", "Range [0, 10)"),
    ((0, 10, False, False), (0, False), "Range(0, 10, False, False)", "Range (0, 10)"),
    ((0, 10, True, True), (10, True), "Range(0, 10, True, True)", "Range [0, 10]"),
    ((0, 10, False, False), (10, False), "Range(0, 10, False, False)", "Range (0, 10)"),
    ((0, 10, False, False), (0, False), "Range(0, 10, False, False)", "Range (0, 10)"),
    ((0, 10, False, False), (5, True), "Range(0, 10, False, False)", "Range (0, 10)"),
)


class RangeTest(unittest.TestCase):
    def test_bad_range_init(self):
        bad_init_data = ((10, 0), (10, 10))

        for params in bad_init_data:
            with self.subTest(params):
                with self.assertRaises(ValueError):
                    mathutil.Range(*params)

    def test_range_contains(self):
        for params, include, *_ in RANGE_DATA:
            with self.subTest(f"{params}, {include}"):
                in_test = include[0]
                in_expect = include[1]
                r = mathutil.Range(*params)
                self.assertEqual(in_test in r, in_expect)

    def test_range_repr(self):
        for params, _, x_repr, _ in RANGE_DATA:
            with self.subTest(f"{params} -> {x_repr}"):
                r = mathutil.Range(*params)
                self.assertEqual(repr(r), x_repr)

    def test_range_str(self):
        for params, _, _, x_str in RANGE_DATA:
            with self.subTest(f"{params} -> {x_str}"):
                r = mathutil.Range(*params)
                self.assertEqual(str(r), x_str)


if __name__ == "__main__":
    unittest.main()
