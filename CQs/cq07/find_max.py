"""Defining find_max"""

__author__ = "730654279"


def find_and_remove_max(input: list[int]) -> int:
    max: int = 0
    idx: int = 0
    if not input:
        max = max - 1
        return max
    for elem in input:
        if elem > max:
            max = elem
    while idx < len(input):
        if input[idx] == max:
            input.pop(idx)
            # for pops, they pop the index of a list, not the actual value
        else:
            idx = idx + 1
    return max
