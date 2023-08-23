import unittest

from designtools.color.collectors import HsvCollector


class HsvCollectorTest(unittest.TestCase):
    DATA = {
        ("h", 0.25, 0.75): {
            "00ff00": True,
            "ff00ff": False,
            "1122ff": True,
            "111111": False,
            "ffffff": False,
            "00ffff": True,
            "0000ff": True,
        },
        ("s", 0.0, 0.085): {
            "00ff00": False,
            "ff00ff": False,
            "1122ff": False,
            "111111": True,
            "ffffff": True,
            "00ffff": False,
            "0000ff": False,
            "444644": True,
            "777077": True,
        },
    }

    def test_hue_collector(self):
        for r, data in self.DATA.items():
            c = HsvCollector(*r)

            with self.subTest(f"{c}"):
                for test, expect in data.items():
                    with self.subTest(f"{test} in {c} is {expect}"):
                        self.assertEqual(test in c, expect)


if __name__ == "__main__":
    unittest.main()
