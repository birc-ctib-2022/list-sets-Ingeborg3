"""List implementation of a set."""

from typing import (
    Generic, Iterable, TypeVar
)

T = TypeVar('T')


class ListSet(Generic[T]):
    """A set of elements of type T."""

    data: list[T]

    def __init__(self, init: Iterable[T]) -> None: # O(n)
        """Initialise set with init."""
        self.set = [] # O(1) to assign value to variable. 
        for element in init: # If n is the number of elements in the
            # iterable, the loop body of the loop is executed n times.
            self.set.append(element) # Amortized constant time analyzed
            # by Banker's method. Most append operations takes 1 
            # computation that takes time t. When the underlying list
            # has been filled (n elements can be in the list), all 
            # elements are though to be copied to a larger list. This 
            # takes n computations (tn time). If for each append
            # operation, 3 computations are 'payed', 2n computations
            # (2tn time) are in excess, when the elements are to be 
            # copied. 2n of the excess computations can be taken from 
            # the bank and used to pay the expensive operation, for 
            # which reason we only need to pay 2 computations for each 
            # operation. Therefore, amortized O(1).

    def __contains__(self, x: T) -> bool:
        """Test if x is in set."""
        return x in self.set # O(n) since the underlying data structure
        # is a python list, for which reason __contains__() of the 
        # python list class is called and this makes a linear search to
        # search through the list.

    def __bool__(self) -> bool:
        """
        Return truth value of the set.

        A set is True if it is non-empty and False
        otherwise
        """
        return len(self.set) != 0 # O(1)

    def add(self, x: T) -> None: # Amortized O(1)
        """Add x to the set."""
        self.set.append(x) 

    def remove(self, x: T) -> None: 
        """Remove x from the set."""
        self.set.remove(x) # remove takes an element as argument and
        # removes the first occurrence of it in the underlying list. 
        # All the elements at indices higher than the indice of the 
        # element removed, must be copied and moved one index down in
        # the list. Therefore, worst-case scenario is O(n) (first 
        # element removed) and best-case is O(1) (last element 
        # removed). 
