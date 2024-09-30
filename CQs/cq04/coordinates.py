"""cq04 pt.1"""

__author__ = "730654279"


def get_coords(xs: str, ys: str) -> None:
    idx1: int = 0
    idx2: int = 0
    while idx1 < len(xs):
        while idx2 < len(ys):
            print("(" + xs[idx1] + "," + ys[idx2] + ")")
            idx2 = idx2 + 1
        idx1 = idx1 + 1
        idx2 = 0
