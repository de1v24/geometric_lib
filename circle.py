import math


def area(r):
    assert r >= 0

    return math.pi * r * r


def perimeter(r):
    assert r >= 0

    return 2 * math.pi * r
