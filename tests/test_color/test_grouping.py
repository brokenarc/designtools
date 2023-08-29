import pytest

from designtools.color import group_colors, hex_color
from designtools.color.collectors import HsvCollector


@pytest.fixture(scope="module")
def collectors():
    return {
        "00": HsvCollector("h", 0, 0.25),
        "01": HsvCollector("h", 0.25, 0.5),
        "02": HsvCollector("h", 0.5, 0.75),
        "03": HsvCollector("h", 0.75, 1.01),
    }


@pytest.mark.parametrize(
    "colors, expected",
    [
        (
            (
                hex_color("00ff00"),
                hex_color("ff00ff"),
                hex_color("1122ff"),
                hex_color("111111"),
                hex_color("ffffff"),
                hex_color("00ffff"),
                hex_color("0000ff"),
                hex_color("00ff00"),
            ),
            {
                "00": [hex_color("111111"), hex_color("ffffff")],
                "01": [hex_color("00ff00")],
                "02": [hex_color("1122ff"), hex_color("00ffff"), hex_color("0000ff")],
                "03": [hex_color("ff00ff")],
            },
        )
    ],
)
def test_group_colors(collectors, colors, expected):
    assert group_colors(colors, collectors) == expected
