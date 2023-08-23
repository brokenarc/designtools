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

RATIOS = {
    "Golden Ratio": GOLDEN_RATIO,
    "Supergolden Ratio": SUPERGOLDEN_RATIO,
    "Silver Ratio": SILVER_RATIO,
    "Plastic Number": PLASTIC_NUMBER
}
"""Mapping of the ratio names and values for use by command line tools.
"""
