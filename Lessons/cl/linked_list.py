from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
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


two: Node = Node(2, None)

one: Node = Node(1, two)
courses: Node = Node(110, Node(220, Node(301, None)))
print(one)
print(courses)
# Solve through here first


def to_str(head: Node | None) -> str:
    """Represents a Linked list as a str"""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))
print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of the Linked list"""
    if head.next is None:
        return head.value  # Base case
    else:
        return last(head.next)  # Recursive case


print(last(one))  # expect 2
print(last(courses))  # expect 301


def recursive_range(start: int, end: int) -> Node | None:
    """ "Build a linked list recursively from start up until end(not inclusive)"""
    # Raise an Exception with string "Invalid use of recursive_range" when called
    # Edge case
    if start > end:
        raise ValueError("Invalid use of recursive_range")

    if start == end:
        # Base case
        return None
    else:
        # Recursive case
        # Intuition: handle the first case based on the specific call
        # Build the rest of the list using the builder function recursively
        return Node(start, recursive_range(start + 1, end))

    # Try declaring a variable and assigning it the result of recursive_range
    # Then try printing that variable as a string


a: Node | None = recursive_range(2, 8)
b: Node | None = recursive_range(110, 112)
print(a)
print(b)
