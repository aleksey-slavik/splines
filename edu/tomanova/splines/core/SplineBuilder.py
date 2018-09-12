import sympy

from math import factorial
from edu.tomanova.splines.core.Derivative import Derivative

"""
Contains spline of 5th degree

@author: iryna.tomanova
"""

x, y = sympy.symbols(('x', 'y'))


class SplineBuilder:

    def __init__(self, triangle):
        """
        Setup initial data

        Parameters
        ----------
        triangle: Triangle
            triangle, based on which spline was created
        """
        self.triangle = triangle
        self.spline = 0

    def build(self):
        """
        Create spline of 5th degree

        Return
        ------
        spline: expression
            spline of 5th degree
        """
        self.spline = 0
        self.spline = self.w()

        for k in range(3):
            i = self.triangle.normalApexes[k][0]
            j = self.triangle.normalApexes[k][1]
            self.spline += (self.triangle.getNormal(i - 1, j - 1).dn - self.dw(i, j)) * self.H(i, j)

        return self.spline

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
        apex = self.triangle.apexes
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
        apex = self.triangle.apexes
        result = 0

        for tr in range(3):
            for n in range(3):
                for m in range(n + 1):
                    result += apex[tr].getParam(Derivative(m, n - m)) * self.h(tr + 1, Derivative(m, n - m))

        return result

    def dw(self, i, j):
        """
        Depends on w(x,y) create function dn(w(x,y))

        Parameters
        ----------
        i: int
            number of apex
        j: int
            number of apex

        Return
        ------
        dw: expression
            function dn(w(x,y))
        """
        numb = [1, 2, 3]
        numb.remove(i)
        numb.remove(j)
        i -= 1
        j -= 1
        k = numb[0] - 1
        apex = self.triangle.apexes
        normal = self.triangle.getNormal(i, j)
        dw = normal.sign(apex[k]) / apex[i].distance(apex[j]) * (
                (apex[i].y - apex[j].y) * sympy.diff(self.w(), x) - (apex[i].x - apex[j].x) * sympy.diff(self.w(), y))
        return dw.subs({x: normal.point.x, y: normal.point.y})

    def H(self, i, j):
        """
        Create function H(i,j)

        Parameters
        ----------
        i: int
            number of apex
        j: int
            number of apex

        Return
        ------
        result: expression
            function H(x,y)
        """
        numb = [1, 2, 3]
        numb.remove(i)
        numb.remove(j)
        i -= 1
        j -= 1
        k = numb[0] - 1
        apex = self.triangle.apexes
        normal = self.triangle.getNormal(i, j)

        def omega(a, b):
            """
            Represent omega(x,y)

            Parameters
            ----------
            a: int
                number of apex
            b: int
                number of apex

            Return
            ------
            det: expression
                determinant of matrix omega(x,y)
            """
            matrix = sympy.Matrix(
                [[x - apex[b].x, y - apex[b].y, 0],
                 [apex[a].x - apex[b].x, apex[a].y - apex[b].y, 0],
                 [apex[b].x, apex[b].y, 1]])

            return matrix.det()

        def omegaSubs(a, b):
            """
            Represent omega(x,y) with substitution normal

            Parameters
            ----------
            a: int
                number of apex
            b: int
                number of apex

            Return
            ------
            det: float
                determinant of matrix omega(x,y)
            """
            return omega(a, b).subs({x: normal.point.x, y: normal.point.y})

        return omega(i, k) ** 2 * omega(j, k) ** 2 * omega(i, j) * normal.sign(apex[k]) / (
                    omegaSubs(i, k) ** 2 * omegaSubs(j, k) ** 2 * apex[i].distance(apex[j]))
