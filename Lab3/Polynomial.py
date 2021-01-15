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
        str_result = ''
        for index in range(len(self.coefficients)):
            if self.coefficients[index] != 0:
                str_result += ' + ' + str(self.coefficients[index]) + '*x^' + str(index)
        return str_result

    def __bool__(self):
        if not any(self.coefficients):
            return False
        else:
            return True

    def __add__(self, other):
        if isinstance(other, (int, float)):
            self.coefficients[0] += other
            return Polynomial(self.coefficients)
        else:
            added = []
            for c1, c2 in zip_longest(self.coefficients, other.coefficients):
                added.append(correct_value(c1) + correct_value(c2))
            return Polynomial(added)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            self.coefficients[0] -= other
            return Polynomial(self.coefficients)
        else:
            subtracted = []
            for c1, c2 in zip_longest(self.coefficients, other.coefficients):
                subtracted.append(correct_value(c1) - correct_value(c2))
            return Polynomial(subtracted)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            multiplied = []
            for scalar in self.coefficients:
                multiplied.append(scalar * other)
            return Polynomial(multiplied)
        else:
            multiplied = Polynomial([0])
            for index in range(len(other.coefficients)):
                multiplied += Polynomial([0] * index + [other.coefficients[index] * coefficient
                                                    for coefficient in self.coefficients])
            return multiplied

    def __iadd__(self, other):
        added = self + other
        return added

    def __isub__(self, other):
        subtracted = self - other
        return subtracted

    def __imul__(self, other):
        multiplied = self * other
        return multiplied

    def calculate_value(self, x):
        result = 0
        for i in range(len(self.coefficients)):
            result += x ** i * self.coefficients[i]
        return result


# defaultdict sprawdziłby się tutaj dobrze, domyślna wartość mogłaby wynosić na przykład 0.
# Dla liczb zespolonych i macierzy również by działało, o ile macierze byłyby kwadratowe i ustalonego rozmiaru.
