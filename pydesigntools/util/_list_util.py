from collections.abc import Sequence
from typing import Optional, TypeVar

T = TypeVar("T")


def transpose(table: Sequence[Sequence[T]], empty_val: Optional[T] = None) -> Sequence[Sequence[T]]:
    """Transpose a table (sequence of sequences) so that each row becomes a
    column.

    The rows do not have to be of the same length, and each resulting
    column will be bottom padded with the value of `empty_val` so that each
    is the same length.

    Example:
        Given this table::

            [['a1', 'a2', 'a3'],
             ['b1', 'b2', 'b3'],
             ['c1', 'c2', 'c3'],
             ['d1', 'd2']]

        This table would be produced::

            [['a1', 'b1', 'c1', 'd1'],
             ['a2', 'b2', 'c2', 'd2'],
             ['a3', 'b3', 'c3', None]]

    Args:
        table (Sequence[Sequence[T]]) : the table to transpose
        empty_val (Optional[T]) : the value to fill empty cells with

    Returns:
        Sequence[Sequence[T]] : The transposed table.

    Raises:
        ValueError: If ``table`` was empty or ``None``.
    """
    if table is None or len(table) == 0:
        raise ValueError("Parameter `table` cannot be empty or None")

    max_len = max(len(s) for s in table)
    rows = []

    for i in range(max_len):
        row = []
        for column in table:
            cell = column[i] if i < len(column) else empty_val
            row.append(cell)
        rows.append(row)

    return rows
