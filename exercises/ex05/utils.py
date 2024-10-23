"""Ex05 utility functions"""

__author__ = "730654279"


def only_evens(x: list[int]) -> list:
    evens: list[int] = []
    for elem in x:
        if elem % 2 == 0:  # % operator in order to get the evens
            evens.append(elem)
    return evens


def sub(x: list[int], a: int, b: int) -> list:
    empty: list = []
    if len(x) == 0 or a >= len(x) or b <= 0:  # check for an empty list
        return empty
    if a < 0:
        a = 0
    if b > len(x):
        b = len(x)
    return x[a:b]


def add_at_index(x: list[int], elem: int, index: int) -> None:
    if index < 0 or index > len(x):
        raise IndexError("Index is out of bounds for the input list")
    x.append(elem)
    for idx in range(len(x) - 1, index, -1):  # make sure have all three arguments
        x[idx] = x[idx - 1]
    x[index] = elem
