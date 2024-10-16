"""Testing find_max"""

from CQs.cq07.find_max import find_and_remove_max

__author__ = "730654279"


def test_find_and_remove_max_return() -> None:
    max: list[int] = [1, 2, 3, 4, 5]
    assert find_and_remove_max(max) == 5


def test_find_and_remove_max_mutate() -> None:
    max: list[int] = [1, 2, 3, 4, 5]
    find_and_remove_max(max)
    assert max == [1, 2, 3, 4]


def test_find_and_remove_max_edge() -> None:
    max: list[int] = []
    assert find_and_remove_max(max) == -1
