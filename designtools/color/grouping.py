"""Provides tools for collecting colors into groups.
"""
from collections.abc import (
    Container,
    Mapping,
    MutableMapping,
    MutableSequence,
    Sequence,
)

from ._color_util import normalize_hex_color


def group_colors(
    hex_codes: Sequence[str], collectors: Mapping[str, Container[str]]
) -> Mapping[str, Sequence[str]]:
    """Organizes a list of colors into groups according to a given set of
    container membership tests.

    Container membership tests are objects that implement a ``__contains__``
    method that will check a hexadecimal color code for membership.

    Colors will be placed in the first group whose membership test passed. The
    function ensures that any given color will only appear in one group even
    if it occurs more than once in ``hex_codes``.

    Args:
        hex_codes: The hexadecimal color codes to group.
        collectors: A mapping of group names to the container rule that
            determines membership in the group.

    Returns:
        A mapping of group names to a sequence of colors that were collected
        by that group's membership tests. The keys in this group will be the
        same as the keys for ``collectors``. Note that the associated sequence
        may be empty of none of the collector for that key did not match any
        of the given colors.
    """
    groupings: MutableMapping[str, MutableSequence[str]] = {}
    colors = set([normalize_hex_color(x) for x in hex_codes])

    for color in colors:
        for key, container in collectors.items():
            if key not in groupings:
                groupings[key] = []

            if color in container:
                groupings[key].append(color)
                break

    return groupings
