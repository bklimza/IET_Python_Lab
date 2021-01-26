from itertools import *


class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients    # coefficients może być modyfikowalne

    def __bool__(self):
        if not any(self.coefficients):  # return any(...)
            return False
        else:
            return True

    def __str__(self):
        polynomial_list = [str(self.coefficients[index]) + 'x**' + str(index) for index in range(len(self.coefficients))
                           if self.coefficients[index] != 0]
        return ' + '.join(polynomial_list)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            self.coefficients[0] += other
            return Polynomial(self.coefficients)    # jednocześnie Pan modyfikuje wielomian i zwraca nowy
        else:
            added = [c1 + c2 for c1, c2 in zip_longest(self.coefficients, other.coefficients, fillvalue=0)]
            return Polynomial(added)    # a tu tylko Pan zwraca

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            self.coefficients[0] -= other
            return Polynomial(self.coefficients)
        else:
            subtracted = [c1 - c2 for c1, c2 in zip_longest(self.coefficients, other.coefficients, fillvalue=0)]
            return Polynomial(subtracted)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            multiplied = [coeff * other for coeff in self.coefficients]
            return Polynomial(multiplied)
        else:
            multiplied_len = len(other.coefficients) + len(self.coefficients) - 1
            multiplied = [0 for _ in range(multiplied_len)]
            for i in range(len(other.coefficients)):
                for j in range(len(self.coefficients)):
                    multiplied[i+j] += other.coefficients[i] * self.coefficients[j]
            return Polynomial(multiplied)

    def __iadd__(self, other):
        return self + other

    def __isub__(self, other):
        return self - other

    def __imul__(self, other):
        return self * other

    def calculate_value(self, value):
        calculated_list = [(value ** index) * self.coefficients[index] for index in range(len(self.coefficients))]
        return sum(calculated_list)


# defaultdict byłby w porządku, domyślna wartość mogłaby wynosić 0.
# Dla liczb zespolonych i macierzy również by działało, o ile macierze byłyby kwadratowe i ustalonego rozmiaru.
