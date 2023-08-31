"""Utilities that don't fit anywhere else.
"""

import secrets

from collections.abc import Container
from typing import TypeVar

T = TypeVar("T")


class ContainerChain(Container[T]):
    """Tests for membership in a sequence of containers.

    Args:
        *containers: the containers to chain together.
    """

    __slots__ = "_containers"

    def __init__(self, *containers: Container[T]):
        self._containers = containers

    def __repr__(self):
        chain = ", ".join([repr(c) for c in self._containers])
        return f"ContainerChain({chain})"

    def __contains__(self, o: object) -> bool:
        """Returns ``True`` if the given object is contained by all the containers in this chain.
        """
        return all(o in c for c in self._containers)


def id_token(length: int = 8):
    """Returns a reasonably unique URL-safe token of a given length."""
    return secrets.token_urlsafe(length)
