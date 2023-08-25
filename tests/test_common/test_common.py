import unittest

from designtools.color import Color
from designtools.color.collectors import HsvCollector
from designtools.common import ContainerChain


class ContainerChainTest(unittest.TestCase):
    CHAIN = [HsvCollector("h", 0.25, 0.75), HsvCollector("s", 0.33, 0.66)]
    DATA = {
        Color(hsv=(0, 0, 0)): False,
        Color(hsv=(0.5, 0.5, 0)): True,
        Color(hsv=(0.5, 0.7, 0)): False,
        Color(hsv=(0.8, 0.5, 0)): False,
        Color(hsv=(0.25, 0.33, 0)): True,
        Color(hsv=(0.75, 0.66, 0)): False,
    }

    def test_container_chain(self):
        c = ContainerChain(*ContainerChainTest.CHAIN)
        for test, expect in ContainerChainTest.DATA.items():
            with self.subTest(f"{test} in {c} is {expect}"):
                self.assertEqual(test in c, expect)
