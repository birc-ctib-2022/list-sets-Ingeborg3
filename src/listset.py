"""List implementation of a set."""

from typing import (
    Generic, Iterable, TypeVar
)

T = TypeVar('T')


class ListSet(Generic[T]):
    """A set of elements of type T."""

    data: list[T]

    def __init__(self, init: Iterable[T]) -> None:
        """Initialise set with init."""
        ...  # FIXME

    def __contains__(self, x: T) -> bool:
        """Test if x is in set."""
        ...  # FIXME

    def __bool__(self) -> bool:
        """
        Return truth value of the set.

        A set is True if it is non-empty and False
        otherwise
        """
        ...  # FIXME

    def add(self, x: T) -> None:
        """Add x to the set."""
        ...  # FIXME

    def remove(self, x: T) -> None:
        """Remove x from the set."""
        ...  # FIXME
