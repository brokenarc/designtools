from collections.abc import Callable, Sequence

from designtools.color import Color

ColorExtractor = Callable[[str], Sequence[Color]]
"""The interface for a method that extracts colors from a file (string filename) or from a string
of text."""
