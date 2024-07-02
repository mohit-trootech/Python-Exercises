"""
Python Program for Popular Unit Conversion
"""


class Temperature:
    def __init__(self, temperature: float) -> None:
        """
        Temperature Constructor
        """
        self.temperature = temperature

    def fahrenheit_to_celsius(self) -> float:
        """
        method to return fahrenheit to celsius conversion
        @return float
        """
        return 5 / 9 * (self.temperature - 32)

    def celsius_to_fahrenheit(self) -> float:
        """
        method to return celsius to fahrenheit conversion
        @return float
        """
        return (9 / 5 * self.temperature) + 32

    def kelvin_to_celsius(self):
        """
        method to return kelvin to celsius
        """
        return self.temperature - 273

    def celsius_to_kelvin(self):
        """
        method to return celsius to kelvin
        """
        return self.temperature + 273


class Distance:

    def __init__(self, distance: float):
        """
        Distance Constructor
        """
        self.distance = distance

    def meter_to_kilometer(self):
        """
        method for meter to kilometer conversion
        """
        return self.distance / 1000

    def kilometer_to_meter(self):
        """
        method for kilometer to meter conversion
        """
        return self.distance * 1000

    def kilometer_to_miles(self):
        """
        method for kilometer to miles conversion
        """
        return self.distance / 1.6

    def miles_to_kilometer(self):
        """
        method for kilometer to miles conversion
        """
        return self.distance * 1.6

    def feet_to_inches(self):
        """
        method for feet to inches conversion
        """
        return self.distance * 12

    def inches_to_feet(self):
        """
        method for inches to feet conversion
        """
        return self.distance / 12


class Weight:

    def __init__(self, weight: float):
        """
        Distance Constructor
        """
        self.weight = weight

    def gram_to_kilo(self):
        """
        method for grams to Kilograms conversion
        """
        return self.weight / 1000

    def kilo_to_gram(self):
        """
        method for gram to kilometer conversion
        """
        return self.weight * 1000

    def kilo_to_pound(self):
        """
        method for Kilograms to pound conversion
        """
        return self.weight / 2.205

    def pound_to_kilo(self):
        """
        method for pound to Kilograms conversion
        """
        return self.weight * 2.205


if __name__ == "__main__":
    obj = Temperature(-40)
    print(obj.fahrenheit_to_celsius())
    print(obj.celsius_to_fahrenheit())

    obj = Temperature(0)
    print(obj.fahrenheit_to_celsius())
    print(obj.celsius_to_fahrenheit())
