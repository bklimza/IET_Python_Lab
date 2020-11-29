def check_if_number(number):
    if not isinstance(number, (int, float)):
        raise TypeError("Please check numbers")


def solve_quadratic_equation(a, b, c):
    for number in (a, b, c):
        check_if_number(number)

    if a == b == c == 0:
        raise ValueError("Every coefficient equals zero")
    if a == 0:
        return {-c / b}  # linear equation
    if a == b == 0:
        raise ZeroDivisionError("Contradictory equation")
    delta = b ** 2 - 4 * a * c
    if delta == 0:
        return {-b / (2 * a)}
    elif delta > 0:
        return {(-b - delta ** 0.5) / (2 * a), (-b + delta ** 0.5) / (2 * a)}
    else:
        return set()


def find_straight_line_equation(point1, point2):
    for point in (point1, point2):
        if len(point) == 2:
            for coordinate in point:
                check_if_number(coordinate)
        else:
            raise TypeError("Please check numbers")
    if point1[0] == point2[0] and point1[1] == point2[1]:
        raise ValueError("Given points are equal")
    return (point2[1] - point1[1]) / (point2[0] - point1[0]),\
        point1[1] - point1[0] * (point2[1] - point1[1]) / (point2[0] - point1[0])
