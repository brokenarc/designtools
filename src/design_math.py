"""Design-related constants, sequences, and utilities.
"""

import math
from collections.abc import Sequence


GOLDEN_RATIO = 1.618033988749895
"""Two quantities are in the golden ratio if their ratio is the same as the
ratio of their sum to the larger of the two quantities.

The Greek letter phi (φ or Φ) denotes the golden ratio.

.. [Ref] https://en.wikipedia.org/wiki/Golden_ratio
"""


GOLDEN_ANGLE = 137.50776405003785  # Degrees
"""The golden angle (g) is the smaller of the two angles created by sectioning
the circumference of a circle according to the golden ratio; that is, into
two arcs such that the ratio of the length of the smaller arc to the length
of the larger arc is the same as the ratio of the length of the larger arc to
the full circumference of the circle.

.. [Ref] https://en.wikipedia.org/wiki/Golden_angle
"""


SUPERGOLDEN_RATIO = 1.465571231876768
"""Two quantities are in the supergolden ratio if their quotient equals the
unique real solution to the equation `x**3 == x**2 + 1``. This solution is
commonly denoted ψ (psi).

.. [Ref] https://en.wikipedia.org/wiki/Supergolden_ratio
"""


SILVER_RATIO = 2.414213562373095
"""Two quantities are in the silver ratio if the ratio of the smaller of those
two quantities to the larger quantity is the same as the ratio of the larger
quantity to the sum of the smaller quantity and twice the larger quantity.

The silver ratio is the limiting ratio of consecutive Pell numbers and is the
second metallic mean. It is denoted by δS (delta, subscript S).

.. [Ref] https://en.wikipedia.org/wiki/Silver_ratio
"""


PLASTIC_NUMBER = 1.324717957244746
"""The plastic number ρ (rho)  is a mathematical constant which is the unique
real solution of the cubic equation `x**3 == x + 1`.

.. [Ref] https://en.wikipedia.org/wiki/Plastic_number
"""


GOLDEN_POWERS: tuple[float] = (
    1.0, 1.618033988749895, 2.618033988749895, 4.23606797749979,
    6.854101966249686, 11.090169943749476, 17.944271909999163,
    29.03444185374864, 46.978713763747805, 76.01315561749645,
    122.99186938124426, 199.0050249987407, 321.996894379985,
    521.0019193787257, 842.9988137587108, 1364.0007331374366,
    2206.9995468961474, 3571.000280033584, 5777.999826929732, 
    9349.000106963316
)
"""The Golden Ratio raised to powers 0 to 19."""


FLORET_ANGLES: tuple[float] = (
    0.0, 137.50776405003785, 275.0155281000757, 52.52329215011355,
    190.0310562001514, 327.53882025018925, 105.0465843002271,
    242.55434835026495, 20.062112400302794, 157.56987645034064,
    295.0776405003785, 72.58540455041634, 210.0931686004542,
    347.60093265049204, 125.10869670052989, 262.61646075056797,
    40.12422480060559, 177.6319888506432, 315.13975290068083,
    92.64751695071845
)
"""The sequence of angles that floret petals generally grow in nature. Index 0
is the first petal, index 1 is the second petal, and so on.

.. [Ref] https://en.wikipedia.org/wiki/Golden_angle#Golden_angle_in_nature
"""


FIBONACCI: tuple[int] = (
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
    2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418,
    317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465,
    14930352, 24157817, 39088169, 63245986, 102334155
)
"""The Fibonacci sequence is a sequence in which each number is the sum of the
two preceding ones.

.. [Ref] https://en.wikipedia.org/wiki/Fibonacci_sequence
.. [Ref] https://oeis.org/A000045
"""


LUCAS: tuple[int] = (
    2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843, 1364, 2207,
    3571, 5778, 9349, 15127, 24476, 39603, 64079, 103682, 167761, 271443,
    439204, 710647, 1149851, 1860498, 3010349, 4870847, 7881196, 12752043,
    20633239, 33385282, 54018521, 87403803
)
"""The Lucas sequence has the same recursive relationship as the Fibonacci
sequence, where each term is the sum of the two previous terms, but with
different starting values.

.. [Ref] https://en.wikipedia.org/wiki/Lucas_number
.. [Ref] https://oeis.org/A000032
"""


PELL: tuple[int] = (
    0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860, 33461, 80782,
    195025, 470832, 1136689, 2744210, 6625109, 15994428, 38613965,
    93222358, 225058681, 543339720, 1311738121, 3166815962, 7645370045,
    18457556052, 44560482149, 107578520350, 259717522849
)
"""Pell numbers are an infinite sequence of integers that comprise the
denominators of the closest rational approximations to the square root of 2.

.. [Ref] https://en.wikipedia.org/wiki/Pell_number
.. [Ref] https://oeis.org/A000129
"""


PELL_LUCAS: tuple[int] = (
    2, 2, 6, 14, 34, 82, 198, 478, 1154, 2786, 6726, 16238, 39202, 94642,
    228486, 551614, 1331714, 3215042, 7761798, 18738638, 45239074,
    109216786, 263672646, 636562078, 1536796802, 3710155682, 8957108166,
    21624372014, 52205852194, 126036076402, 304278004998
)
"""
.. [Ref] https://en.wikipedia.org/wiki/Pell_number#Pell%E2%80%93Lucas_numbers
.. [Ref] https://oeis.org/A002203
"""


METALLIC_MEAN: tuple[float] = (
    1.0, 1.618033988749895, 2.414213562373095, 3.302775637731995,
    4.23606797749979, 5.192582403567252, 6.16227766016838,
    7.140054944640259, 8.123105625617661, 9.109772228646444,
    10.099019513592784, 11.090169943749475, 12.082762530298218,
    13.076473218982953, 14.071067811865476, 15.06637297521078,
    16.06225774829855, 17.058621384311845, 18.055385138137417,
    19.0524865872714
)
"""The metallic means (also known as metallic ratios) may be defined as the
limiting ratio of consecutive terms of sequences connected to the Fibonacci
sequence via the invert transform.

.. [Ref] https://arxiv.org/abs/1901.02619
.. [Ref] https://en.wikipedia.org/wiki/Metallic_mean
"""


def scale_sequence(seq: Sequence[int | float], value: int | float, offset: int = -1) -> tuple[int | float]:
    """Derives a numeric sequence by scaling a known sequence against a
    specific value.

    The function creates a scaling value such that the value of index `offset`
    in the returned sequence is equal to `value`. All other indexes are scaled
    according to this scaling value.

    Examples
    --------
    >>> scale_sequence((1, 2, 3, 4, 5), 6, 2)
    (2, 4, 6, 8, 10)

    Parameters
    ----------
    seq: Sequence[int | float]
        The numeric sequence to scale.
    value: int | float
        The value that the sequence will be scaled to.
    offset: int, optional
        The index within the sequence where `value` should be after scaling. If
        this value is not given, the index nearest the midpoint of the sequence
        will be used.

    Returns
    -------
    tuple[int | float]
        The scaled sequence.
    """
    size = len(seq)
    index = offset if offset in range(size) else math.trunc(size / 2)
    scalar = value / seq[index]

    return tuple([scalar * item for item in seq])


def ratio_sequence(value: int | float, ratio: int | float, items: int) -> tuple[int | float]:
    """Creates a sequence based on a given value and ratio.

    Items before `value` in the resulting sequence will be successively divided
    by `ratio`, and those after `value` will be successively multiplied by
    `ratio`.

    Examples
    --------
    >>> ratio_sequence(10, 2, 3)
    (1.25, 2.5, 5.0, 10, 20, 40, 80)

    Parameters
    ----------
    value: int | float
        The value to build the sequence around. This value will be in the
        middle of the returned sequence.
    ratio: int | float
        The ratio to apply to each element to find it's predecessor (via 
        division) or its successor (via multiplication).
    items: int
        The number of items to be created before and after `value` in the
        returned sequence. The length of the returned sequence will always be
        `2 * items + 1`.

    Returns
    -------
    tuple[int | float]
        The sequence.
    """
    seq = [value]
    for x in range(0, items):
        seq.insert(0, seq[0] / ratio)
        seq.append(seq[-1] * ratio)
    return tuple(seq)


def round_seq(seq: Sequence[int | float], ndigits: int | None=None) -> tuple[int | float]:
    """Rounds each number in a sequence, returning a new tuple of the rounded
    results.

    Examples
    --------
    >>> round_seq((2.5123, 6.2815, 43.1412, -0.2311))
    (3, 6, 43, 0)

    >>> round_seq((2.5123, 6.2815, 43.1412, -0.2311), 2)
    (2.51, 6.28, 43.14, -0.23)

    Parameters
    ----------
    seq: Sequence[int | float]
    ndigits: int, optional
        An integer specifying the number of decimal places. If omitted,
        defaults to zero.

    Returns
    -------
    tuple[int | float]
    """
    return tuple([round(value, ndigits) for value in seq])


def fmod_seq(seq: Sequence[int | float], divisor: int | float) -> tuple[float]:
    """Applies `fmod` to each number in a sequence, returning a new tuple of
    the results.

    Examples
    --------
    >>> fmod_seq((180.5, 45.32, 27, 382, 522), 360)
    (180.5, 45.32, 27.0, 22.0, 162.0)

    Parameters
    ----------
    seq: Sequence[int | float]
    divisor: int | float

    Returns
    -------
    tuple[int | float]
    """
    return tuple([math.fmod(x, divisor) for x in seq])
