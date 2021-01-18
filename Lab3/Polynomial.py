from itertools import zip_longest


class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __bool__(self):
        if not any(self.coefficients):
            return False
        else:
            return True

    def __str__(self):
        str_result = [str(self.coefficients[index]) + '*x^' + str(index) for index in range(len(self.coefficients))
                      if self.coefficients[index] != 0]
        return '+'.join(str_result)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            self.coefficients[0] += other
            return Polynomial(self.coefficients)
        else:
            added = [c2 + c2 for c1, c2 in zip_longest(self.coefficients, other.coefficients)]
            return Polynomial(added)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            self.coefficients[0] -= other
            return Polynomial(self.coefficients)
        else:
            subtracted = [c1 - c2 for c1, c2 in zip_longest(self.coefficients, other.coefficients)]
            return Polynomial(subtracted)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            multiplied = [scalar * other for scalar in self.coefficients]
            return Polynomial(multiplied)
        else:
            multiplied = Polynomial([0])
            for index in range(len(other.coefficients)):
                multiplied += Polynomial(index * [0] + [other.coefficients[index] * coefficient
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
        calculated = [x ** index * self.coefficients[index] for index in range(len(self.coefficients))]
        return sum(calculated)

# defaultdict sprawdziłby się, domyślna wartość mogłaby wynosić 0.
# Dla liczb zespolonych i macierzy również by działało, o ile macierze byłyby kwadratowe i ustalonego rozmiaru.
