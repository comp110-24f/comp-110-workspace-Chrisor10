"""While Loops Function Challenge Question"""

__author__ = "730654279"


def num_instances(phrase: str, search_char: str) -> int:
    """Return the number of times a character appears in a phrase"""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count = count + 1
        index = index + 1
    return count
