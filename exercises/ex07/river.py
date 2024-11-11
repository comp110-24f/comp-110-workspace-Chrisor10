"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__ = "730654279"


class River:
    """River Class."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears!"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Ages for fishes and bears."""
        new_fish: list = []
        new_bears: list = []
        for _ in self.fish:
            if Fish.age <= 3:
                new_fish.append(Fish)
        for _ in self.bears:
            if Bear.age <= 5:
                new_bears.append(Bear)
        return None

    def bears_eating(self):
        """Bears hunger effect on population."""
        for _ in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)  # Takes away 3 fish from river
                _.eat(3)  # Bear's hunger score increases by 3
        return None

    def check_hunger(self):
        """Bears hunger."""
        new_bear = []
        for _ in self.bears:
            if _.hunger_score >= 0:
                new_bear.append(_)
        self.bears = new_bear  # Update bear's population
        return None

    def repopulate_fish(self):
        """Repopulating fish."""
        num_fish_pairs = len(self.fish) // 2
        for _ in range(num_fish_pairs):
            for _ in range(4):  # For each 2 fish, add a new fish to population
                self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Repopulating bears."""
        num_bear_pairs = len(self.bears) // 2
        for _ in range(num_bear_pairs):
            self.bears.append(Bear())  # Adds a new bear for 2 bears
        return None

    def view_river(self):
        """Checks the populations of animals in river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate the 7 days."""
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int):
        """Removes fish from population."""
        for _ in range(amount):
            if self.fish:
                self.fish.pop(0)
