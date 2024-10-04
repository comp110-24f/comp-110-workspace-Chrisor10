"""Mutating functions"""

__author__ = "730654279"


def manual_append(x: list[int], y: int) -> None:
    a: list[int] = x
    a.append(y)


def double(z: list[int]) -> None:
    idx1: int = 0
    while idx1 < len(z):
        z[idx1] = z[idx1] * 2
        idx1 = idx1 + 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
