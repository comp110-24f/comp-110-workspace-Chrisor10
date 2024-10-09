"""Summing the elements of a list using different loops"""

__author__ = "730654279"


def w_sum(vals: list[float]) -> float:
    idx: int = 0
    sum: float = 0
    while idx < len(vals):
        sum = sum + vals[idx]
        idx = idx + 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0
    for elem in vals:
        sum = sum + elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0
    for elem in range(len(vals)):
        sum = sum + elem
    return sum
