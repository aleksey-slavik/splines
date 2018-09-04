import sympy
import math

from edu.tomanova.splines.core.integrate.Element import Element
from edu.tomanova.splines.core.integrate.Point import Point
"""
Contains method for integration

@author: iryna.tomanova 
"""

x, y = sympy.symbols(('x', 'y'))


class Integrate:

    def __init__(self, triangle, func, count=3):
        """
        Setup initial data

        Parameters
        ----------
        triangle: Triangle
            area of integration
        func: expression
            integrand
        count: int
            count of divide area of integration
        """
        self.grid = []
        self.grid.append(
            Element(
                Point(triangle.apex1.x, triangle.apex1.y),
                Point(triangle.apex2.x, triangle.apex2.y),
                Point(triangle.apex3.x, triangle.apex3.y)))
        self.func = func
        self.count = count
        self.points = []
        self.integral = 0

    def integrate(self):
        """
        Integrate function
        """
        self.integral = 0
        self.divideTriangles()

        for i in range(len(self.grid)):
            number = math.floor(i / math.pow(4, self.count))
            p1 = self.func.subs({x: self.grid[i].middle12.x, y: self.grid[i].middle12.y})
            p2 = self.func.subs({x: self.grid[i].middle23.x, y: self.grid[i].middle23.y})
            p3 = self.func.subs({x: self.grid[i].middle13.x, y: self.grid[i].middle13.y})
            self.integral += (p1 + p2 + p3) * self.square(number) / 3

        return self.integral

    def divideTriangles(self):
        """
        Divide grid for integration
        """
        elements = self.grid

        for i in range(self.count):
            temp = []

            for element in elements:
                temp.append(
                    Element(
                        element.point1,
                        element.middle12,
                        element.middle13))
                temp.append(
                    Element(
                        element.middle12,
                        element.middle13,
                        element.middle23))
                temp.append(
                    Element(
                        element.middle12,
                        element.point2,
                        element.middle23))
                temp.append(
                    Element(
                        element.middle23,
                        element.middle13,
                        element.point3))

            elements = temp

        self.grid = elements

    def p(self, number):
        """
        Additional function
        """
        return (self.grid[number].point1.distance(self.grid[number].point2) +
                self.grid[number].point2.distance(self.grid[number].point3) +
                self.grid[number].point1.distance(self.grid[number].point3)) / 2

    def square(self, number):
        """
        Calculate square of given triangle

        Parameters
        ----------
        number: int
            number of triangle
        """
        return sympy.sqrt(
            self.p(number) *
            (self.p(number) - self.grid[number].point1.distance(self.grid[number].point2)) *
            (self.p(number) - self.grid[number].point2.distance(self.grid[number].point3)) *
            (self.p(number) - self.grid[number].point1.distance(self.grid[number].point3)))
