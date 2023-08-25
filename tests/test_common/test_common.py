import unittest

from designtools.color import hsv_color
from designtools.color.collectors import HsvCollector
from designtools.common import ContainerChain

# ----------------------------------------------------------------------------
# The collectors to build the chain from.
DATA_CHAIN = (HsvCollector("h", 0.25, 0.75), HsvCollector("s", 0.33, 0.66))

# ----------------------------------------------------------------------------
# Colors mapped to whether they should be collected by the chain.
DATA_COLORS = {
    hsv_color(0, 0, 0): False,
    hsv_color(0.5, 0.5, 0): True,
    hsv_color(0.5, 0.7, 0): False,
    hsv_color(0.8, 0.5, 0): False,
    hsv_color(0.25, 0.33, 0): True,
    hsv_color(0.75, 0.66, 0): False,
}


class ContainerChainTest(unittest.TestCase):

    def test_container_chain(self):
        c = ContainerChain(*DATA_CHAIN)
        for test, expect in DATA_COLORS.items():
            with self.subTest(f"{test} in {c} is {expect}"):
                self.assertEqual(test in c, expect)
