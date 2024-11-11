"""File to define Fish class."""

__author__ = "730654279"


class Fish:
    """Fish Class."""

    age: int

    def __init__(self):
        """Fish init."""
        self.age: int = 0
        return None

    def one_day(self):
        """Increase age of fish."""
        self.age = self.age + 1
        return None
