def solve_quadratic_equation(a, b, c):
    if a == b == c == 0:
        raise ValueError("Every coefficient equals zero")
    delta = b ** 2 - 4 * a * c
    if delta == 0:
        return {-b / (2 * a)}
    elif delta > 0:
        return {(-b - delta ** 0.5) / (2 * a), (-b + delta ** 0.5) / (2 * a)}
    else:
        return set()


def find_straight_line_equation(point1, point2):
    if point1[0] == point2[0] and point1[1] == point2[1]:
        raise ValueError("Given points are equal")
    return (point2[1] - point1[1]) / (point2[0] - point1[0]),\
        point1[1] - point1[0] * (point2[1] - point1[1]) / (point2[0] - point1[0])
