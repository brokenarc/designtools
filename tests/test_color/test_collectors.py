import unittest

from designtools.color.collectors import ContainerChain, HsvCollector


class ContainerChainTest(unittest.TestCase):
    CHAIN = [HsvCollector("h", 0.25, 0.75), HsvCollector("s", 0.33, 0.66)]
    DATA = {
        (0, 0, 0): False,
        (0.5, 0.5, 0): True,
        (0.5, 0.7, 0): False,
        (0.8, 0.5, 0): False,
        (0.25, 0.33, 0): True,
        (0.75, 0.66, 0): False,
    }

    def test_container_chain(self):
        c = ContainerChain(*ContainerChainTest.CHAIN)
        for test, expect in ContainerChainTest.DATA.items():
            with self.subTest(f"{test} in {c} is {expect}"):
                self.assertEqual(test in c, expect)


class HsvCollectorTest(unittest.TestCase):
    DATA = {
        ("h", 0.25, 0.75): {
            (0.333, 1, 1): True,
            (0.833, 1, 1): False,
            (0.655, 0.93, 1): True,
            (0, 0, 0.07): False,
            (0, 0, 1): False,
            (0.5, 1, 1): True,
            (0.667, 1, 1): True,
        },
        ("s", 0.0, 0.085): {
            (0.333, 1, 1): False,
            (0.833, 1, 1): False,
            (0.655, 0.93, 1): False,
            (0, 0, 7): True,
            (0, 0, 1): True,
            (0.5, 1, 1): False,
            (0.667, 1, 1): False,
            (0.333, 0.03, 0.27): True,
            (0.833, 0.06, 0.47): True,
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
