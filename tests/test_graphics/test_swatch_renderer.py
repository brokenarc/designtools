from textwrap import dedent

import pytest

from designtools.color import hex_color
from designtools.graphics import SwatchRenderer


@pytest.fixture(scope="module")
def renderer():
    return SwatchRenderer(radius=32, padding=16)


@pytest.fixture(scope="module")
def color_groups():
    return (
        (hex_color("ff0000"), hex_color("ff8800"), hex_color("ff0088")),
        (hex_color("00ff00"), hex_color("00ff88")),
        (hex_color("0000ff"),),
    )


@pytest.mark.parametrize(
    "color_groups, expected",
    [
        (
            (
                (hex_color("ff0000"), hex_color("ff8800"), hex_color("ff0088")),
                (hex_color("00ff00"), hex_color("00ff88")),
                (hex_color("0000ff"),),
            ),
            dedent(
                """
            <svg viewBox="0 0 160 256" xmlns="http://www.w3.org/2000/svg">
            <g>
            <circle cx="48" cy="48" r="32" stroke="none" fill="#ff0000" />
            <circle cx="80" cy="48" r="32" stroke="none" fill="#ff8800" />
            <circle cx="112" cy="48" r="32" stroke="none" fill="#ff0088" />
            </g>
            <g>
            <circle cx="48" cy="128" r="32" stroke="none" fill="#00ff00" />
            <circle cx="80" cy="128" r="32" stroke="none" fill="#00ff88" />
            </g>
            <g>
            <circle cx="48" cy="208" r="32" stroke="none" fill="#0000ff" />
            </g>
            </svg>
            """
            )
            .replace("\n", "")
            .replace("\r", "")
            .strip(),
        )
    ],
)
def test_svg_render(renderer, color_groups, expected):
    assert renderer.render(color_groups) == expected
