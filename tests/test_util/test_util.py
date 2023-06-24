import unittest

from pydesigntools.util import transpose


class TransposeTest(unittest.TestCase):
    DATA = {
        "1x1 (no empty)": {"table": [[1]], "empty_val": None, "expect": [[1]]},
        "3x3 (no empty)": {
            "table": [["a1", "a2", "a3"], ["b1", "b2", "b3"], ["c1", "c2", "c3"]],
            "empty_val": None,
            "expect": [["a1", "b1", "c1"], ["a2", "b2", "c2"], ["a3", "b3", "c3"]],
        },
        "3x4 (1 empty)": {
            "table": [
                ["a1", "a2", "a3"],
                ["b1", "b2", "b3"],
                ["c1", "c2", "c3"],
                ["d1", "d2"],
            ],
            "empty_val": "__",
            "expect": [
                ["a1", "b1", "c1", "d1"],
                ["a2", "b2", "c2", "d2"],
                ["a3", "b3", "c3", "__"],
            ],
        },
        "3x3 (3 empty)": {
            "table": [["a1", "a2", "a3"], ["b1", "b2"], ["c1"]],
            "empty_val": None,
            "expect": [["a1", "b1", "c1"], ["a2", "b2", None], ["a3", None, None]],
        },
        "3x3 (one row empty)": {
            "table": [["a1", "a2", "a3"], ["b1", "b2", "b3"], []],
            "empty_val": "__",
            "expect": [["a1", "b1", "__"], ["a2", "b2", "__"], ["a3", "b3", "__"]],
        },
    }

    def test_transpose(self):
        for name, data in self.DATA.items():
            with self.subTest(name):
                actual = transpose(data["table"], data["empty_val"])
                self.assertSequenceEqual(actual, data["expect"])

    def test_transpose_error(self):
        bad_data = {"empty": [], "None": None}

        for name, table in bad_data.items():
            with self.subTest(name):
                with self.assertRaises(ValueError):
                    transpose(table)


if __name__ == "__main__":
    unittest.main()
