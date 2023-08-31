import xml.etree.ElementTree as ET

import pytest

from designtools.graphics.svg import attr_filter, svg_tag_guard


@pytest.fixture
def allowed_attr():
    return "viewBox", "stroke", "fill", "xmlns", "stop-color", "id"


@pytest.mark.parametrize(
    "given, expected",
    [
        (
            {"fill": "#fff", "nope": "123", "stroke": None},
            {"fill": "#fff"},
        ),
        (
            {"x": "1", "y": "5"},
            {},
        ),
        (
            {"VIEWBOX": "0 0 10 10", "stroke": "#f00", "blank": ""},
            {"viewBox": "0 0 10 10", "stroke": "#f00"},
        ),
        (
            {"  stroke  ": "123", "stop_color": "#00f", "_id": "XYZ", "fill_": "none"},
            {"stroke": "123", "stop-color": "#00f", "id": "XYZ", "fill": "none"},
        ),
    ],
)
def test_attr_filter(allowed_attr, given, expected):
    assert attr_filter(allowed_attr, given) == expected


@pytest.mark.parametrize("bad_tag", ["zero", ET.Element("bad")])
def test_bad_svg_tag_guard(bad_tag):
    with pytest.raises(ValueError):
        svg_tag_guard(bad_tag)


@pytest.mark.parametrize(
    "good_tag, expected",
    [
        ("VIEWBOX", "viewBox"),
        ("viewBox", "viewBox"),
        ("  viewBox  ", "viewBox"),
        (ET.Element("circle"), ET.Element("circle")),
    ],
)
def test_good_svg_tag_guard(good_tag, expected):
    pass
