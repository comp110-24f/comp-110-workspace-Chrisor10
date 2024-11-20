"""Ex08 Linked Lists."""

from __future__ import annotations


class Node:
    """Node Class."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Inital values."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Represents a Node object as a string."""
        rest: str = "?"
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


def value_at(head: Node | None, index: int) -> int:
    """Returns the value of the Node at a given index."""
    # Base Case
    if head is None:
        raise IndexError("Index is out of bounds on the list")
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Finds the max value in the linked list."""
    # Base Case
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value
    rest_max: int = max(head.next)
    if head.value > rest_max:
        return head.value
    else:
        return rest_max


def linkify(items: list[int]) -> Node | None:
    """Returns the called items of the given list in the same order."""
    # Base case, if list is empty
    if not items:
        return None
    # Node of first element, and link to rest of list
    return Node(items[0], linkify(items[1:]))  # Recursively link to the rest of list


def scale(head: Node | None, factor: int) -> Node | None:
    """A new linked list where the og list is multiplied by a scaling factor."""
    # Base Case
    if head is None:
        return None
    return Node(head.value * factor, scale(head.next, factor))
