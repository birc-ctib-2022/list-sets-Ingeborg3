# List sets

You might already be familiar with the built-in `set` type. Whenever you need to use a set, you should probably use it. However, you might not always be working in a language that already has a set, but most languages will have something like the `list` type (or you can implement it yourself rather easily). In this exercise, I want you to implement the `set` functionality, but using a `list`.

In `src/listset.py` I have written a template class with the methods I want you to implement:

```python
class ListSet(Generic[T]):
    """A set of elements of type T."""

    data: list[T]  # Underlying data is a list

    def __init__(self, init: Iterable[T]) -> None:
        """Initialise set with init."""
        ...

    def __contains__(self, x: T) -> bool:
        """Test if x is in set."""
        ...

    def __bool__(self) -> bool:
        """
        Return truth value of the set.

        A set is True if it is non-empty and False
        otherwise
        """
        ...

    def add(self, x: T) -> None:
        """Add x to the set."""
        ...

    def remove(self, x: T) -> None:
        """Remove x from the set."""
        ...
```

**Exercise:** Implement the methods and tell me what the running time of each of them is.
