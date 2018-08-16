import sympy

from math import factorial
from edu.tomanova.splines.core.Derivative import Derivative
"""
Contains spline of 5th degree

@author: iryna.tomanova
"""

x, y = sympy.symbols(('x', 'y'))


class Spline:

    def __init__(self, triangle):
        """
        Setup initial data

        Parameters
        ----------
        triangle: Triangle
            triangle, based on which spline was created
        """
        self.triangle = triangle

    def h(self, k, b):
        """
        Create function h(x,y)

        Parameters
        ----------
        k: int
            number of apex
        b: Derivative
            derivative value

        Return
        ------
        result: expression
            function h(x,y)
        """
        apex = self.triangle.apexes()
        numb = [1, 2, 3]
        numb.remove(k)
        i = numb[0] - 1
        j = numb[1] - 1
        k -= 1

        def omega():
            """
            Represent omega(x,y)

            Return
            ------
            det: expression
                determinant of matrix omega(x,y)
            """
            matrix = sympy.Matrix(
                [[x, y, 1],
                 [apex[i].x, apex[i].y, 1],
                 [apex[j].x, apex[j].y, 1]])
            return matrix.det()

        def DbOmega(derivative):
            """
            Represent derivative of omega(x, y) ** (-3) at point k

            Parameters
            ----------
            derivative: Derivative
                derivative value

            Return
            ------
            value: expression
                derivative of omega(x, y) ** (-3) at point k
            """
            value = sympy.diff(omega() ** (-3), x, derivative.dx, y, derivative.dy)
            return value.subs({x: apex[k].x, y: apex[k].y})

        def DbOmegaSeries():
            """
            Represent series of omega(x, y) ** (-3) at point k

            Return
            ------
            series: expression
                series of omega(x, y) ** (-3) at point k
            """
            seriesLength = 2 - b.dx - b.dy
            series = 0

            for n in range(seriesLength + 1):
                for m in range(n + 1):
                    series += DbOmega(Derivative(m, n - m)) * \
                              (x - apex[k].x) ** m / factorial(m) * \
                              (y - apex[k].y) ** (n - m) / factorial(n - m)

            return series

        return ((x - apex[k].x) ** b.dx) * ((y - apex[k].y) ** b.dy) * (omega() ** 3) / (
                factorial(b.dx) * factorial(b.dy)) * DbOmegaSeries()

    def w(self):
        """
        Create function w(x,y)

        Return
        ------
        result: expression
            function w(x,y)
        """
        apex = self.triangle.apexes()
        result = 0

        for tr in range(3):
            for n in range(3):
                for m in range(n + 1):
                    result += apex[tr].getParam(Derivative(m, n - m)) * self.h(tr + 1, Derivative(m, n - m))

        return result


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
