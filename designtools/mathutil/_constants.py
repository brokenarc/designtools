"""Design-related constants.
"""

GOLDEN_RATIO = 1.618033988749895
"""Two quantities are in the `golden ratio`_ if their ratio is the same as the
ratio of their sum to the larger of the two quantities.

The Greek letter phi (φ or Φ) denotes the golden ratio.

.. _golden ratio:
   https://en.wikipedia.org/wiki/Golden_ratio
"""

GOLDEN_ANGLE = 137.50776405003785  # Degrees
"""The `golden angle`_ (g) is the smaller of the two angles created by
sectioning the circumference of a circle according to the golden ratio; that
is, into two arcs such that the ratio of the length of the smaller arc to the
length of the larger arc is the same as the ratio of the length of the larger
arc to the full circumference of the circle.

.. _golden angle:
   https://en.wikipedia.org/wiki/Golden_angle
"""

SUPERGOLDEN_RATIO = 1.465571231876768
"""Two quantities are in the `supergolden ratio`_ if their quotient equals the
unique real solution to the equation ``x**3 == x**2 + 1``. This solution is
commonly denoted ψ (psi).

.. _supergolden ratio:
   https://en.wikipedia.org/wiki/Supergolden_ratio
"""

SILVER_RATIO = 2.414213562373095
"""Two quantities are in the `silver ratio`_ if the ratio of the smaller of
those two quantities to the larger quantity is the same as the ratio of the
larger quantity to the sum of the smaller quantity and twice the larger
quantity.

The silver ratio is the limiting ratio of consecutive Pell numbers and is the
second metallic mean. It is denoted by δS (delta, subscript S).

.. _silver ratio:
   https://en.wikipedia.org/wiki/Silver_ratio
"""

PLASTIC_NUMBER = 1.324717957244746
"""The `plastic number`_ ρ (rho)  is a mathematical constant which is the
unique real solution of the cubic equation ``x**3 == x + 1``.

.. _plastic number:
   https://en.wikipedia.org/wiki/Plastic_number
"""

MINOR_SECOND = 1.066666666666667
"""The musical `minor second`_ (16:15).

.. _minor second:
   https://en.wikipedia.org/wiki/Semitone#Minor_second
"""

MAJOR_SECOND = 1.125
"""The musical `major second`_ (9:8).

.. _major second:
   https://en.wikipedia.org/wiki/Major_second
"""

MINOR_THIRD = 1.2
"""The musical `minor third`_ (6:5).

.. _minor third:
   https://en.wikipedia.org/wiki/Minor_third
"""

MAJOR_THIRD = 1.250
""" The musical `major third`_ (5:4).

.. _major third:
   https://en.wikipedia.org/wiki/Major_third
"""

PERFECT_FOURTH = 1.333333333333333
"""The musical `perfect fourth`_ (4:3).

.. _perfect fourth:
   https://en.wikipedia.org/wiki/Perfect_fourth
"""

AUGMENTED_FOURTH = 1.414213562373095
"""The musical `augmented fourth`_ (`sqrt(2)`).

.. _augmented fourth:
   https://en.wikipedia.org/wiki/Tritone#Augmented_fourth_and_diminished_fifth
"""

PERFECT_FIFTH = 1.5
"""The musical `perfect fifth`_ (3:2).

.. _perfect fifth:
   https://en.wikipedia.org/wiki/Perfect_fifth
"""

RATIOS = {
    "Golden ratio": GOLDEN_RATIO,
    "Supergolden ratio": SUPERGOLDEN_RATIO,
    "Silver ratio": SILVER_RATIO,
    "Plastic number": PLASTIC_NUMBER,
    "Minor second": MINOR_SECOND,
    "Major second": MAJOR_SECOND,
    "Minor third": MINOR_THIRD,
    "Major third": MAJOR_THIRD,
    "Perfect fourth": PERFECT_FOURTH,
    "Augmented fourth": AUGMENTED_FOURTH,
    "Perfect fifth": PERFECT_FIFTH,
}
"""Mapping of the ratio names and values for use by command line tools.
"""
