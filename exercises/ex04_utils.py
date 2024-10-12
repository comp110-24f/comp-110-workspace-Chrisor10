"""Ex04:Commonly Useful Functions"""

__author__ = "730654279"


def all(x: list[int], y: int) -> bool:
    idx: int = 0
    result: bool = True  # have a local variable to return to
    if not x:
        result = False
    while idx < len(x):
        if x[idx] == y:
            result = result
        else:
            result = False
            return result
        idx = idx + 1
    return result


def max(x: list[int]) -> int:
    current = x[0]
    # current is the largest starting at the first int in the list
    if len(x) == 0:
        raise ValueError("max() arg is an empty List")
    for elem in x:
        if elem > current:
            current = elem
    return current


def is_equal(x: list[int], y: list[int]) -> bool:
    result: bool = True
    if len(x) != len(y):  # check if the lengths of the lists are equal
        return False
    for elem in range(len(x)):
        if x[elem] != y[elem]:
            result = False
    return result


def extend(x: list[int], y: list[int]) -> None:
    for elem in y:
        x.append(elem)
