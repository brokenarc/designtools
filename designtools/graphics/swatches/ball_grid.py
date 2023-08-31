from collections.abc import Sequence

from designtools.color import Color
from designtools.graphics.svg import Circle, Defs, Group, RadialGradient, Stop
from designtools.mathutil import Numeric
from .grid_base import GridBase

GRAD_ID = "radgrad-{0}"
BALL_ID = "ball-{0}"

HIGHLIGHT = (1.0, 0.5, 1.5)
"""The HSV transform to apply to a color to get the highlight of the ball."""

SHADOW = (1.0, 1.5, 0.5)
"""The HSV transform to apply to a color to get the shadow of the ball."""


class BallGrid(GridBase):
    @staticmethod
    def _compute_stops(color: Color) -> Sequence[Stop]:
        return (
            Stop(offset="0%", stop_color=f"#{color.hsv_transform(*HIGHLIGHT).hex_code}"),
            Stop(offset="33%", stop_color=f"#{color.hex_code}"),
            Stop(offset="75%", stop_color=f"#{color.hex_code}"),
            Stop(offset="100%", stop_color=f"#{color.hsv_transform(*SHADOW).hex_code}")
        )

    def _make_ball(self, color: Color, cx: Numeric, cy: Numeric) -> tuple[RadialGradient, Circle]:
        ball_id = BALL_ID.format(color.hex_code)
        grad_id = GRAD_ID.format(color.hex_code)
        gradient = RadialGradient(id_=grad_id, cx="50%", cy="50%", fx="25%", fy="25%", fr="10%")
        gradient.extend(BallGrid._compute_stops(color))

        circle = Circle(id_=ball_id, cx=cx, cy=cy, r=self._half_width, fill=f"url(#{grad_id})")

        return gradient, circle

    def render_elements(self, colors: Sequence[Color]) -> tuple[Defs | None, Group]:
        cols, _ = self.get_grid_size(colors)
        defs = Defs()
        group = Group(id_="ball-grid")

        row = 0
        column = 0
        for color in colors:
            cx, cy = self.get_center(column, row)
            gradient, ball = self._make_ball(color, cx, cy)
            defs.append(gradient)
            group.append(ball)
            column += 1
            if column == cols:
                column = 0
                row += 1

        return defs, group
