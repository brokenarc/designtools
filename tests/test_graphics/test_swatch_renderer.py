import unittest

from pydesigntools.graphics import SwatchRenderer


class SwatchRendererTest(unittest.TestCase):
    GROUPS = (("ff0000", "ff8800", "ff0088"), ("00ff00", "00ff88"), ("0000ff",))

    EXPECT = (
        '<svg viewBox="0 0 160 256" xmlns="http://www.w3.org/2000/svg">'
        "<g>"
        '<circle cx="48" cy="48" r="32" stroke="none" fill="#ff0000" />'
        '<circle cx="80" cy="48" r="32" stroke="none" fill="#ff8800" />'
        '<circle cx="112" cy="48" r="32" stroke="none" fill="#ff0088" />'
        "</g>"
        "<g>"
        '<circle cx="48" cy="128" r="32" stroke="none" fill="#00ff00" />'
        '<circle cx="80" cy="128" r="32" stroke="none" fill="#00ff88" />'
        "</g>"
        "<g>"
        '<circle cx="48" cy="208" r="32" stroke="none" fill="#0000ff" />'
        "</g>"
        "</svg>"
    )

    def test_render(self):
        renderer = SwatchRenderer(radius=32, padding=16)
        test = renderer.render(self.GROUPS)
        self.assertEqual(self.EXPECT, test)


if __name__ == "__main__":
    unittest.main()
