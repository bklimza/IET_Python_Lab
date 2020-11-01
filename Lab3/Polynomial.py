from itertools import *


def value(x):
    if x is None:
        return 0
    else:
        return x


class Polynomial:
    def __init__(self, coefficients: list):
        self.coefficients = coefficients

    def __add__(self, other):
        if isinstance(other, (int, float)):
            coefficients = self.coefficients
            coefficients[0] += other
            return Polynomial(coefficients)
        else:
            coefficients = []
            for c1, c2 in zip_longest(self.coefficients, other.coefficients):
                coefficients.append(value(c1) + value(c2))
            return Polynomial(coefficients)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            coefficients = self.coefficients
            coefficients[0] -= other
            return Polynomial(coefficients)
        else:
            coefficients = []
            for c1, c2 in zip_longest(self.coefficients, other.coefficients):
                coefficients.append(value(c1) - value(c2))
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

    def calc(self, x: float):
        result = 0
        for i in range(len(self.coefficients)):
            result += x ** i * self.coefficients[i]
        return result

    def __str__(self):
        return ' + '.join([str(self.coefficients[index]) + '*x^' + str(index) for index in
                           range(len(self.coefficients)) if self.coefficients[index] != 0])

    def __bool__(self):
        if self.coefficients[-1] == 0:
            return False
        else:
            return True


#Dla liczb zespolonych i macierzy również by działało, o ile macierze byłyby kwadratowe i ustalonego rozmiaru.

