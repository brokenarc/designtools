import unittest
from textwrap import dedent

from designtools.color import hex_color
from designtools.graphics import SwatchRenderer

# ----------------------------------------------------------------------------
# Render these groups of colors as swatches.
DATA_GROUPS = (
    (hex_color("ff0000"), hex_color("ff8800"), hex_color("ff0088")),
    (hex_color("00ff00"), hex_color("00ff88")),
    (hex_color("0000ff"),)
)

# ----------------------------------------------------------------------------
# The expected SVG content.
DATA_EXPECT = dedent("""
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
""").replace('\n', '').replace('\r', '').strip()


class SwatchRendererTest(unittest.TestCase):
    def test_render(self):
        renderer = SwatchRenderer(radius=32, padding=16)
        test = renderer.render(DATA_GROUPS)
        self.assertEqual(DATA_EXPECT, test)


if __name__ == "__main__":
    unittest.main()
