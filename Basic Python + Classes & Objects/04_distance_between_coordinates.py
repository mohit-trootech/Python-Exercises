"""
Program to find distance between two points in XY plane
"""

import math


def distance_2_points(p1: list[float, float], p2: list[float, float]) -> float | None:
    """
    function to find the distance between two points in xy plane
    """
    if len(p1) == 2 and len(p2) == 2:
        return math.sqrt(((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2))
    else:
        print("Points Must Contain Exactly Two Coordinated X & y")


def distance_from_origin(p: list[float, float]) -> float | None:
    """
    function to find the distance between a point and origin in xy plane
    """
    if len(p) == 2:
        return round(math.sqrt(((p[0]) ** 2) + ((p[1]) ** 2)), 2)
    else:
        print("Points Must Contain Exactly Two Coordinated X & y")
