import sympy
from math import factorial

x, y = sympy.symbols(('x', 'y'))


class Spline:
    def __init__(self, triangle):
        self.triangle = triangle


def h00(b1, b2, apex1, apex2, apex3):
    return ((x - apex1.x) ** b1) * ((y - apex1.y) ** b2) * \
           (omega(apex2, apex3) ** 3) / (factorial(b1) * factorial(b2)) * \
           (alpha(apex1, apex2, apex3) +
            beta(1, 0, apex1, apex2, apex3) * (x - apex1.x) + beta(0, 1, apex1, apex2, apex3) * (y - apex1.y) +
            beta(2, 0, apex1, apex2, apex3) * (x - apex1.x) ** 2 / 2 +
            beta(1, 1, apex1, apex2, apex3) * (x - apex1.x) * (y - apex1.y) +
            beta(0, 2, apex1, apex2, apex3) * (y - apex1.y) ** 2 / 2)


def h10(b1, b2, apex1, apex2, apex3):
    return ((x - apex1.x) ** b1) * ((y - apex1.y) ** b2) * \
           (omega(apex2, apex3) ** 3) / (factorial(b1) * factorial(b2)) * \
           (alpha(apex1, apex2, apex3) +
            beta(1, 0, apex1, apex2, apex3) * (x - apex1.x) + beta(0, 1, apex1, apex2, apex3) * (y - apex1.y))


def h01(b1, b2, apex1, apex2, apex3):
    return ((x - apex1.x) ** b1) * ((y - apex1.y) ** b2) * \
           (omega(apex2, apex3) ** 3) / (factorial(b1) * factorial(b2)) * \
           (alpha(apex1, apex2, apex3) +
            beta(1, 0, apex1, apex2, apex3) * (x - apex1.x) + beta(0, 1, apex1, apex2, apex3) * (y - apex1.y))


def h20(b1, b2, apex1, apex2, apex3):
    return ((x - apex1.x) ** b1) * ((y - apex1.y) ** b2) * \
           (omega(apex2, apex3) ** 3) / (factorial(b1) * factorial(b2)) * alpha(apex1, apex2, apex3)


def h11(b1, b2, apex1, apex2, apex3):
    return ((x - apex1.x) ** b1) * ((y - apex1.y) ** b2) * \
           (omega(apex2, apex3) ** 3) / (factorial(b1) * factorial(b2)) * alpha(apex1, apex2, apex3)


def h02(b1, b2, apex1, apex2, apex3):
    return ((x - apex1.x) ** b1) * ((y - apex1.y) ** b2) * \
           (omega(apex2, apex3) ** 3) / (factorial(b1) * factorial(b2)) * alpha(apex1, apex2, apex3)


def omega(apex1, apex2):
    matrix = sympy.Matrix(
        [[x, y, 1],
         [apex1.x, apex1.y, 1],
         [apex2.x, apex2.y, 1]])

    return matrix.det()


def omega2(apex1, apex2):
    matrix = sympy.Matrix(
        [[x - apex2.x, y - apex2.y, 0],
         [apex1.x - apex2.x, apex1.y - apex2.y, 0],
         [apex2.x, apex2.y, 1]])

    return matrix.det()


def omega3(apex1, apex2, apex3):
    matrix = sympy.Matrix(
        [[(apex1.x + apex2.x) / 2 - apex3.x, (apex1.y + apex2.y) / 2 - apex3.y, 0],
         [apex2.x - apex3.x, apex2.y - apex3.y, 0],
         [apex3.x, apex3.y, 1]])

    return matrix.det()


def delta(apex1, apex2, apex3):
    matrix = sympy.Matrix(
        [[apex1.x, apex1.y, 1],
         [apex2.x, apex2.y, 1],
         [apex3.x, apex3.y, 1]])

    return matrix.det()


def sing(apex1, apex2, apex3):
    value = delta(apex1, apex2, apex3)

    if value > 0:
        return 1

    if value < 0:
        return -1

    return 0


def alpha(apex1, apex2, apex3):
    value = 1 / (omega(apex2, apex3) ** 3)
    return value.subs({x: apex1.x, y: apex1.y})


def beta(b1, b2, apex1, apex2, apex3):
    value = sympy.diff(1 / (omega(apex2, apex3) ** 3), x, b1, y, b2)
    return value.subs({x: apex1.x, y: apex1.y})
