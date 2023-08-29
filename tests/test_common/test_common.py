import pytest

from designtools.color import hsv_color
from designtools.color.collectors import HsvCollector
from designtools.common import ContainerChain


@pytest.fixture(scope="module")
def container_chain():
    return ContainerChain(HsvCollector("h", 0.25, 0.75), HsvCollector("s", 0.33, 0.66))


@pytest.mark.parametrize(
    "color, expected",
    [
        (hsv_color(0, 0, 0), False),
        (hsv_color(0.5, 0.5, 0), True),
        (hsv_color(0.5, 0.7, 0), False),
        (hsv_color(0.8, 0.5, 0), False),
        (hsv_color(0.25, 0.33, 0), True),
        (hsv_color(0.75, 0.66, 0), False),
    ],
)
def test_container_chain(container_chain, color, expected):
    assert (color in container_chain) == expected
