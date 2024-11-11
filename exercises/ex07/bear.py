"""File to define Bear class."""

__author__ = "730654279"


class Bear:
    """Bear Class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Bear init."""
        self.age: int = 0
        self.hunger_score: int = 0
        return None

    def one_day(self):
        """Increase age of bear."""
        self.age = self.age + 1
        self.hunger_score = self.hunger_score - 1
        return None

    def eat(self, num_fish: int):
        """What the bear eats."""
        self.hunger_score = self.hunger_score + num_fish
