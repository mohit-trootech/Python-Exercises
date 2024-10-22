"""
To understand inheritance lets understand the following example, a Polygon inheritance example.
A polygon is a closed figure with 3 or more sides
"""


class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [
            float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)
        ]

    def dispSides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print("The area of the triangle is {:.2f}".format(area))


if __name__ == "__main__":
    t = Triangle()
    t.inputSides()
    t.dispSides()
    t.findArea()
