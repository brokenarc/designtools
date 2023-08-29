import pytest

from designtools.color import hsv_color
from designtools.color.collectors import HsvCollector


@pytest.fixture(scope="module")
def hue_collector():
    return HsvCollector("h", 0.25, 0.75)


@pytest.fixture(scope="module")
def sat_collector():
    return HsvCollector("s", 0.0, 0.085)


@pytest.mark.parametrize(
    "name, color, expected",
    [
        ("hue_collector", hsv_color(0.333, 1, 1), True),
        ("hue_collector", hsv_color(0.833, 1, 1), False),
        ("hue_collector", hsv_color(0.655, 0.93, 1), True),
        ("hue_collector", hsv_color(0, 0, 0.07), False),
        ("hue_collector", hsv_color(0, 0, 1), False),
        ("hue_collector", hsv_color(0.5, 1, 1), True),
        ("hue_collector", hsv_color(0.667, 1, 1), True),
        ("sat_collector", hsv_color(0.333, 1, 1), False),
        ("sat_collector", hsv_color(0.833, 1, 1), False),
        ("sat_collector", hsv_color(0.655, 0.93, 1), False),
        ("sat_collector", hsv_color(0, 0, 0.7), True),
        ("sat_collector", hsv_color(0, 0, 1), True),
        ("sat_collector", hsv_color(0.5, 1, 1), False),
        ("sat_collector", hsv_color(0.667, 1, 1), False),
        ("sat_collector", hsv_color(0.333, 0.03, 0.27), True),
        ("sat_collector", hsv_color(0.833, 0.06, 0.47), True),
    ],
)
def test_hsv_collector(name, color, expected, request):
    collector = request.getfixturevalue(name)
    assert (color in collector) == expected
