import unittest

from main.math_functions import *


class FindStraightLineEquationTest(unittest.TestCase):
    def test_incorrect_input(self):
        self.assertRaises(ValueError, find_straight_line_equation, (0, 0), (0, 0))

    def test_correct_input(self):
        self.assertCountEqual([1, 0], list(find_straight_line_equation((1, 1), (2, 2))))
        self.assertCountEqual([2.5, 5], list(find_straight_line_equation((0, 5), (5, 17.5))))


class SolveQuadraticEquationTest(unittest.TestCase):
    def test_incorrect_input(self):
        self.assertRaises(ValueError, solve_quadratic_equation, 0, 0, 0)

    def test_delta_negative(self):
        self.assertCountEqual({}, solve_quadratic_equation(2, 0, 3))
        self.assertCountEqual({}, solve_quadratic_equation(3, 0, 5))

    def test_delta_zero(self):
        self.assertCountEqual({-1}, solve_quadratic_equation(2, 4, 2))
        self.assertCountEqual({1}, solve_quadratic_equation(-3, 6, -3))

    def test_delta_positive(self):
        self.assertCountEqual({1, -1}, solve_quadratic_equation(1, 0, -1))
        self.assertCountEqual({2, -3}, solve_quadratic_equation(3, 3, -18))

    def test_a_coefficient_zero(self):
        self.assertCountEqual({1}, solve_quadratic_equation(0, 2, -2))
        self.assertCountEqual({-2}, solve_quadratic_equation(0, 3, 6))

    def test_zero_division(self):
        self.assertRaises(ZeroDivisionError, solve_quadratic_equation, 0, 0, 4)


if __name__ == "__main__":
    unittest.main()
