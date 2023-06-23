"""Utilities for numeric sequences.
"""
import math
from collections.abc import Sequence
from typing import Optional

from ._types import Numeric


def scale_sequence(seq: Sequence[Numeric], value: Numeric, offset: Optional[int] = None) -> Sequence[Numeric, ...]:
    """Derives a numeric sequence by scaling a known sequence against a
    specific value.

    The function creates a scaling factor such that the value of index
    ``offset`` in the returned sequence is equal to ``value``. All other
    indexes are scaled according to this scaling factor.

    Examples
    --------
    >>> scale_sequence((1, 2, 3, 4, 5), 6, 2)
    (2, 4, 6, 8, 10)

    Parameters
    ----------
    seq: Sequence[Numeric]
        The numeric sequence to scale.
    value: Numeric
        The value that the sequence will be scaled to.
    offset: int, optional
        The index within the sequence where ``value`` should be after scaling.
        If this value is not given or is outside the bounds of the sequence,
        the index nearest the midpoint of the sequence will be used.

    Returns
    -------
    Sequence[Numeric, ...]
        The new scaled sequence.
    """
    size = len(seq)
    index = offset if offset is not None else math.trunc(size / 2)
    if index not in range(size):
        raise ValueError("Give offset must be within the given sequence.")

    scalar = value / seq[index]

    return tuple([scalar * item for item in seq])


def ratio_sequence(seed: Numeric, ratio: Numeric, count: int) -> Sequence[Numeric, ...]:
    """Creates a sequence based on a given seed value and ratio.

    Items before ``seed`` in the resulting sequence will be successively
    divided by ``ratio``, and those after ``seed`` will be successively
    multiplied by ``ratio``.

    Examples
    --------
    >>> ratio_sequence(10, 2, 3)
    (1.25, 2.5, 5.0, 10, 20, 40, 80)

    Parameters
    ----------
    seed: Numeric
        The value to build the sequence around. This value will be in the
        middle of the returned sequence.
    ratio: Numeric
        The ratio to apply to each element to find its predecessor (via
        division) or its successor (via multiplication).
    count: int
        The number of items to be created before and after ``seed`` in the
        returned sequence. The length of the returned sequence will always be
        ``2 * items + 1``.

    Returns
    -------
    Sequence[Numeric, ...]
        The new scaled sequence.
    """
    seq = [seed]
    for x in range(0, count):
        seq.insert(0, seq[0] / ratio)
        seq.append(seq[-1] * ratio)
    return tuple(seq)


def round_sequence(seq: Sequence[Numeric], digits: Optional[int] = None) -> Sequence[Numeric, ...]:
    """Rounds each number in a sequence, returning a new sequence of the
    rounded results.

    Examples
    --------
    >>> round_sequence((2.5123, 6.2815, 43.1412, -0.2311))
    (3, 6, 43, 0)

    >>> round_sequence((2.5123, 6.2815, 43.1412, -0.2311), 2)
    (2.51, 6.28, 43.14, -0.23)

    Parameters
    ----------
    seq: Sequence[Numeric]
        The sequence to round.
    digits: int, optional
        An integer specifying the number of decimal places. If omitted,
        defaults to zero.

    Returns
    -------
    Sequence[Numeric, ...]
        The new sequence with rounded values.
    """
    return tuple([round(value, digits) for value in seq])


def fmod_sequence(seq: Sequence[Numeric], divisor: Numeric) -> Sequence[Numeric, ...]:
    """Applies ``fmod`` to each number in a sequence, returning a new tuple of
    the results.

    Examples
    --------
    >>> fmod_sequence((180.5, 45.32, 27, 382, 522), 360)
    (180.5, 45.32, 27.0, 22.0, 162.0)

    Parameters
    ----------
    seq: Sequence[Numeric]
    divisor: Numeric

    Returns
    -------
    Sequence[Numeric, ...]
    """
    return tuple([math.fmod(x, divisor) for x in seq])
