import unittest

from designtools import mathutil

# ----------------------------------------------------------------------------
# Constructor parameters that should fail.
DATA_BAD_INIT = ((10, 0), (10, 10))

# ----------------------------------------------------------------------------
# Constructor parameters mapped to contains test and expected result.
DATA_CONTAINS = (
    ((0, 10, False), 5, True),
    ((0, 10, False), -5, False),
    ((0, 10, False), 0, True),
    ((0, 10, False), 10, False),
    ((0, 10, True), 10, True),
    ((0, 10, False), 10, False),
    ((0, 10, False), 5, True),
)

# ----------------------------------------------------------------------------
# Constructor parameters mapped to __repr__ output.
DATA_REPR = (
    ((0, 10, False), "Range(0, 10, False)"),
    ((0, 10, True), "Range(0, 10, True)"),
)

# ----------------------------------------------------------------------------
# Constructor parameters mapped to __str__ output.
DATA_STR = (
    ((0, 10, False), "Range [0, 10)"),
    ((0, 10, True), "Range [0, 10]"),
)


class RangeTest(unittest.TestCase):
    def test_bad_range_init(self):
        for params in DATA_BAD_INIT:
            with self.subTest(params):
                with self.assertRaises(ValueError):
                    mathutil.Range(*params)

    def test_range_contains(self):
        for params, test, expect in DATA_CONTAINS:
            with self.subTest(f"{test} {'in' if expect else 'not in'} {params}"):
                r = mathutil.Range(*params)
                self.assertEqual(test in r, expect)

    def test_range_repr(self):
        for params, x_repr in DATA_REPR:
            with self.subTest(f"{params} -> {x_repr}"):
                r = mathutil.Range(*params)
                self.assertEqual(repr(r), x_repr)

    def test_range_str(self):
        for params, x_str in DATA_STR:
            with self.subTest(f"{params} -> {x_str}"):
                r = mathutil.Range(*params)
                self.assertEqual(str(r), x_str)


if __name__ == "__main__":
    unittest.main()
