from collections.abc import Sequence

from designtools.color import Color
from designtools.mathutil import Numeric


class SwatchRenderer:
    """Renders an SVG of swatches using a sequence of color groups.

    The size of the SVG is based on the number of groups (affects height) and
    the size of the largest group (affects width).

    Args:
        radius: The radius of the swatch circles.
        padding: The padding around the image and between the groups.
    """

    def __init__(self, radius: Numeric, padding: Numeric):
        self._radius = radius
        self._padding = padding
        self._y_inc = (2 * radius) + padding
        self._x_inc = radius

    @staticmethod
    def _circle(
        cx: Numeric, cy: Numeric, r: Numeric, stroke: str = "none", fill: str = "none"
    ):
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" stroke="{stroke}" fill="{fill}" />'

    @staticmethod
    def _group(items: Sequence[str]):
        return f'<g>{"".join(items)}</g>'

    @staticmethod
    def _svg(view_width: Numeric, view_height: Numeric, body: str):
        return (
            f'<svg viewBox="0 0 {view_width} {view_height}"'
            f' xmlns="http://www.w3.org/2000/svg">'
            f"{body}"
            f"</svg>"
        )

    def _render_group_row(self, color_group: Sequence[Color], cy: Numeric) -> str:
        cx = self._padding + self._radius
        c = []

        for color in color_group:
            c.append(
                SwatchRenderer._circle(cx, cy, self._radius, fill=f"#{color.hex_code}"))
            cx += self._radius

        return SwatchRenderer._group(c)

    def _render_groups(self, color_groups: Sequence[Sequence[Color]]) -> str:
        cy = self._padding + self._radius
        rows = []

        for group in color_groups:
            if len(group) > 0:
                rows.append(self._render_group_row(group, cy))
                cy += self._y_inc

        return "".join(rows)

    def _compute_viewbox(
        self, color_groups: Sequence[Sequence[Color]]
    ) -> tuple[Numeric, Numeric]:
        row_count = len(color_groups)
        col_count = max(len(group) for group in color_groups)

        width = ((col_count + 1) * self._radius) + (2 * self._padding)
        height = (row_count * self._y_inc) + self._padding

        return width, height

    def render(self, color_groups=Sequence[Sequence[Color]]) -> str:
        """Renders a sequence of color groups as swatches in an SVG image.

        Each group is rendered as a row, and each swatch within a group is
        rendered as a circle that overlaps the previous swatch on that row.

        Args:
            color_groups: The color groups to render.

        Returns:
            The SVG image as a string
        """
        width, height = self._compute_viewbox(color_groups)
        rows = self._render_groups(color_groups)

        return self._svg(width, height, rows)
