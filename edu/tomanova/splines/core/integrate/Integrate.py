import sympy

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

        for element in self.grid:
            P1 = self.func.subs({x: element.middle12.x, y: element.middle12.y})
            P2 = self.func.subs({x: element.middle23.x, y: element.middle23.y})
            P3 = self.func.subs({x: element.middle13.x, y: element.middle13.y})
            self.integral += (P1 + P2 + P3) * element.square() / 3

        return self.integral

    def divideTriangles(self):
        """
        Divide area for integration
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
