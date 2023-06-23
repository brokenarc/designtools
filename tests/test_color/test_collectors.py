import unittest

from pydesigntools.color.collectors import HueCollector


class HueCollectorTest(unittest.TestCase):
    DATA = {
        (0.25, 0.75): {
            "00ff00": True,
            "ff00ff": False,
            "1122ff": True,
            "111111": False,
            "ffffff": False,
            "00ffff": True,
            "0000ff": True
        }
    }

    def test_hue_collector(self):
        for (r, data) in self.DATA.items():
            c = HueCollector(*r)

            with self.subTest(f"{c}"):
                for (test, expect) in data.items():
                    with self.subTest(f"{test} in {c} is {expect}"):
                        self.assertEqual(test in c, expect)


if __name__ == "__main__":
    unittest.main()
