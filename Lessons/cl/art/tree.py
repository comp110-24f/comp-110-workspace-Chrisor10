from .turtle import Turtle
from math import pi

# from random import random

__template__ = "https://24ss2.comp110.com/static/turtle/"

DEGREE: float = -pi / 180.0  # constant


def main() -> None: ...


def click(x: float, y: float) -> Turtle:
    """Moves turtle to wherever we click on the canvas."""
    t: Turtle = Turtle()
    t.setSpeed(100)
    t.moveTo(x, y)
    t.turnTo(90 * DEGREE)

    # code for a flower
    # i: int = 200
    # while i > 0:
    #   t.forward(i)
    #   t.left(pi / 2.0 - pi/8.0)
    #   i -= 2

    branch(t, y * 0.15, 90 * DEGREE)

    return t


def branch(t: Turtle, length: float, angle: float) -> None:
    t.turnTo(angle)
    t.forward(length)

    if length > 10.0:
        branch(t, length * 0.75, angle + 35 * DEGREE)
        branch(t, length * 0.75, angle - 35 * DEGREE)

    t.turnTo(angle + pi)
    t.forward(length)