"""
Python Exercise to Calculate Body Mass Index
"""


class BMI:

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def body_mass_index(self):
        """
        method to calculate body mass index with weight and height
        """
        return "{name} - {age} - {height} mt - {weight} kg : {bmi}".format(
            name=self.name,
            age=self.age,
            height=self.height,
            weight=self.weight,
            bmi=round(self.weight / pow(self.height, 2), 2),
        )


if __name__ == "__main__":
    print("Enter Name, Age, Height(Mt), Weight(KGs)")
    obj = BMI("Mohit", 23, 1.79, 80)
    print(obj.body_mass_index())
