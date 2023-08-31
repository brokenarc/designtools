import pytest

from designtools.color import Color


@pytest.mark.parametrize(
    "params",
    [
        {"hex_code": None, "rgb": None, "hsv": None},
        {"hex_code": "fffff"},
        {"hex_code": "ffffxx"},
        {"hex_code": ""},
        {"rgb": (2.0, 0.0, 0.1)},
        {"rgb": (0.5, 0.0)},
        {"hsv": (2.0, 0.0, 0.1)},
        {"hsv": (0.0, 0.1)},
    ],
)
def test_bad_color_init(params):
    with pytest.raises(ValueError):
        Color(**params)


@pytest.mark.parametrize(
    "params, expected_hex",
    [
        ({"hex_code": "ffffff", "rgb": (1, 0, 0), "hsv": (0.5, 0.5, 0.5)}, "ffffff"),
        ({"rgb": (1, 0, 0), "hsv": (0.5, 0.5, 0.5)}, "ff0000"),
    ],
)
def test_init_param_precedence(params, expected_hex):
    assert Color(**params).hex_code == expected_hex


@pytest.mark.parametrize(
    "params, expected",
    [
        (
            {"hex_code": "ffd500"},
            {
                "hex_code": "ffd500",
                "rgb": (1.0, 0.8352941176470589, 0),
                "hsv": (0.1392156862745098, 1.0, 1.0),
            },
        ),
        (
            {"rgb": (0.13333333333333333, 0.4666666666666667, 1.0)},
            {
                "hex_code": "2277ff",
                "rgb": (0.13333333333333333, 0.4666666666666667, 1.0),
                "hsv": (0.6025641025641025, 0.8666666666666667, 1.0),
            },
        ),
        (
            {"hsv": (0.3333333333333333, 0.8, 1.0)},
            {
                "hex_code": "32ff32",
                "rgb": (0.19999999999999996, 1.0, 0.19999999999999996),
                "hsv": (0.3333333333333333, 0.8, 1.0),
            },
        ),
    ],
)
def test_color_data(params, expected):
    c = Color(**params)
    assert c.hex_code == expected["hex_code"]
    assert c.rgb == pytest.approx(expected["rgb"])
    assert c.hsv == pytest.approx(expected["hsv"])


@pytest.mark.parametrize(
    "base_color, xform, new_color",
    [
        (Color(hsv=(1, 1, 1)), (1, 0.5, 0.5), Color(hsv=(1, 0.5, 0.5))),
        (Color(hsv=(0.5, 1, 1)), (1, 2, 2), Color(hsv=(0.5, 1, 1))),
        (Color(hsv=(0.5, 1, 1)), (1, -2, -2), Color(hsv=(0.5, 0, 0))),
        (Color(hsv=(0.5, 1, 1)), (2, 1, 1), Color(hsv=(1, 1, 1))),
    ]
)
def test_hsv_transform(base_color, xform, new_color):
    assert base_color.hsv_transform(*xform) == new_color


@pytest.mark.parametrize(
    "base_color, xform, new_color",
    [
        (Color(rgb=(1, 1, 1)), (0.5, 0.5, 0.5), Color(rgb=(0.5, 0.5, 0.5))),
        (Color(rgb=(1, 1, 1)), (0, 1, 2), Color(rgb=(0, 1, 1))),
        (Color(rgb=(0.5, 1, 1)), (1, -2, -2), Color(rgb=(0.5, 0, 0))),
    ]
)
def test_rgb_transform(base_color, xform, new_color):
    assert base_color.rgb_transform(*xform) == new_color
