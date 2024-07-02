"""
Find Coordinated from Origin Based on Directions
@return: Magnitude
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


print(
    "Enter the Step by Step Position\n"
    "Press N/n fpr North\n"
    "Press S/s fpr South\n"
    "Press E/e fpr East\n"
    "Press W/w for West\n"
    "ps - Press C/c for Cancel - "
)

x, y = 0, 0
try:
    while True:
        direction = input("Choose Direction Press C/c to Stop- ").lower()
        if direction != "c":
            steps = float(input(f"Enter Steps in {direction.upper()} - ").lower())
            if direction == "n" or direction == "s":
                y += abs(steps)
            elif direction == "w" or direction == "e":
                x += abs(steps)
            else:
                print("Invalid Input Choose Input From N/E/W/S - ")
        else:
            break
except ValueError:
    print("Enter a Number input")
print(f"Position in XY Plane (x, y) = ({x}, {y})")
print(f"Distance From Origin(0,0) is {distance_from_origin((x, y))}")
