from itertools import *


def correct_value(value):
    if value is None:
        return 0
    else:
        return value


class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __str__(self):
        return ' + '.join([str(self.coefficients[index]) + '*x^' + str(index) for index in
                           range(len(self.coefficients)) if self.coefficients[index] != 0])

    def __bool__(self):
        if not any(self.coefficients):
            return False
        else:
            return True

    def __add__(self, other):
        if isinstance(other, (int, float)):
            coefficients = self.coefficients
            coefficients[0] += other
            return Polynomial(coefficients)
        else:
            coefficients = []
            for c1, c2 in zip_longest(self.coefficients, other.coefficients):
                coefficients.append(correct_value(c1) + correct_value(c2))
            return Polynomial(coefficients)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            coefficients = self.coefficients
            coefficients[0] -= other
            return Polynomial(coefficients)
        else:
            coefficients = []
            for c1, c2 in zip_longest(self.coefficients, other.coefficients):
                coefficients.append(correct_value(c1) - correct_value(c2))
            return Polynomial(coefficients)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            coefficients = [other * scalar for scalar in self.coefficients]
            return Polynomial(coefficients)
        else:
            result = Polynomial([0])
            for index in range(len(other.coefficients)):
                result += Polynomial([0] * index + [other.coefficients[index] * coefficient
                                                    for coefficient in self.coefficients])
            return result

    def __iadd__(self, other):
        added = self + other
        return added

    def __isub__(self, other):
        subtracted = self - other
        return subtracted

    def __imul__(self, other):
        multiplicated = self * other
        return multiplicated

    def calculate_value(self, x):
        result = 0
        for i in range(len(self.coefficients)):
            result += x ** i * self.coefficients[i]
        return result


# defaultdict sprawdziłby się tutaj dobrze, domyślna wartość mogłaby wynosić na przykład 0.
# Dla liczb zespolonych i macierzy również by działało, o ile macierze byłyby kwadratowe i ustalonego rozmiaru.
