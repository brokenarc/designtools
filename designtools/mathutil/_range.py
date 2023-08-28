"""Provides a range that can handle floating point values.
"""
from collections.abc import Container
from ._types import Numeric


class Range(Container[Numeric]):
    """Provides a simple range (which may be open- or close-ended) that can test
    if a value is in the range.

    By default, the range is closed-ended.

    Example:
        >>> 4 in Range(1, 4)
        True

        >>> 4 in Range(1, 4, closed_ended=False)
        False

    Args:
        min_value: The minimum value for this range.
        max_value: The maximum value for this range.
        closed_ended: If ``True`` (default), the maximum value will be
            included when testing if a number is present on the range.

    Raises:
        ValueError: If ``min_value`` is not less than ``max_value``
    """

    __slots__ = ("_min", "_max", "_closed_ended")

    def __init__(
        self,
        min_value: Numeric,
        max_value: Numeric,
        closed_ended=True,
    ):
        if max_value <= min_value:
            raise ValueError("Maximum must be greater than minimum")

        self._min = min_value
        self._max = max_value
        self._closed_ended = closed_ended

    @property
    def min(self) -> Numeric:
        """The minimum value for this range."""
        return self._min

    @property
    def max(self) -> Numeric:
        """The maximum value for this range."""
        return self._max

    @property
    def closed_ended(self) -> bool:
        """Whether the range is closed-ended, meaning the maximum value will be
        included (``True``) or excluded (``False``) when testing if a number is
        present on the range."""
        return self._closed_ended

    def __contains__(self, value: Numeric) -> bool:
        """Tests if the given number is present in this range."""
        end = value <= self.max if self.closed_ended else value < self.max

        return (self.min <= value) and end

    def __repr__(self) -> str:
        return f"Range({self.min}, {self.max}, {self.closed_ended})"

    def __str__(self) -> str:
        end = "]" if self.closed_ended else ")"

        return f"Range [{self.min}, {self.max}{end}"
