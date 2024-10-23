"""Testing utility functions"""

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index

__author__ = "730654279"


def test_only_evens_return() -> None:
    """test only_even return"""
    evens: list[int] = [10, 20, 30, 40, 50]
    assert only_evens(evens) == [20, 40]


def test_only_evens_mutate() -> None:
    """test only_even mutation"""
    x: list[int] = [10, 20, 30]
    only_evens(x)
    assert x == [10, 20, 30]


def test_only_evens_edge() -> None:
    """test only_even with no evens"""
    x: list[int] = [1, 3, 5]
    assert only_evens(x) == []


def test_sub_return() -> None:
    """test sub return"""
    x: list[int] = [11, 21, 31]
    assert sub(x, -1, 4) == [11, 21, 31]


def test_sub_mutate() -> None:
    """testing sub mutating"""
    x: list[int] = [12, 22, 32]
    sub(x, 0, 2)
    assert x == [12, 22, 32]


def test_sub_edge() -> None:
    """testing sub w/ empty list"""
    x: list[int] = []
    assert sub(x, 0, 1) == []


def test_add_at_index_return() -> None:
    """testing add_at_index"""
    x: list[int] = [1, 2, 3]
    add_at_index(x, 4, 1)
    assert x == [1, 4, 2, 3]


def test_add_at_index_mutate() -> None:
    """Testing add_at_index w/ appending"""
    x: list[int] = [1, 2, 3]
    add_at_index(x, 4, 3)
    assert x == [1, 2, 3, 4]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    x: list[int] = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(x, 4, 5)
