import pytest

from designtools import color


@pytest.mark.parametrize(
    "test, expected",
    [
        ("f1d35a", "f1d35a"),
        ("Ab1", "aabb11"),
        ("#FFF", "ffffff"),
        ("#1234", "112233"),
        ("12345678", "123456"),
    ],
)
def test_normalize_hex_color(test, expected):
    assert color.normalize_hex_color(test) == expected


@pytest.mark.parametrize("test", ["#1", "22", "#55555", "7777777", "#999999999"])
def test_normalize_hex_color_error(test):
    with pytest.raises(ValueError):
        color.normalize_hex_color(test)


@pytest.mark.parametrize(
    "hex_code, rgb",
    [
        ("#fff", (1.0, 1.0, 1.0)),
        ("000000", (0.0, 0.0, 0.0)),
        ("ff0080", (1.0, 0.0, 0.5019607843137255)),
        ("#ffffff", (1.0, 1.0, 1.0)),
    ],
)
def test_hex_to_rgb(hex_code, rgb):
    assert color.hex_to_rgb(hex_code) == rgb


@pytest.mark.parametrize(
    "hex_code, hsv",
    [
        ("#fff", (0.0, 0.0, 1.0)),
        ("000000", (0.0, 0.0, 0.0)),
        ("ff0080", (0.9163398692810457, 1.0, 1.0)),
        ("#ffffff", (0.0, 0.0, 1.0)),
    ],
)
def test_hex_to_hsv(hex_code, hsv):
    assert color.hex_to_hsv(hex_code) == hsv


@pytest.mark.parametrize(
    "rgb, hex_code",
    [
        ((1.0, 1.0, 1.0), "ffffff"),
        ((0.0, 0.0, 0.0), "000000"),
        ((1.0, 0.0, 0.5019607843137255), "ff0080"),
    ],
)
def test_rgb_to_hex(rgb, hex_code):
    assert color.rgb_to_hex(*rgb) == hex_code
