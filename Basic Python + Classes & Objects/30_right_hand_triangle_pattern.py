"""
Python Program to Print Triangle pattern
1
22
333
4444
55555...., Also Inverse Supported
"""


def right_angle_triangle_pattern(
    size: int = 5, pattern: str = "*", reverse: bool = False
) -> None:
    if not reverse:
        for i in range(1, size + 1):
            for j in range(i):
                print(pattern, end="")
            print()
    else:
        for i in range(size, 0, -1):
            for j in range(i):
                print(pattern, end="")
            print()


if __name__ == "__main__":
    right_angle_triangle_pattern()
    right_angle_triangle_pattern(size=10, pattern="~", reverse=True)
