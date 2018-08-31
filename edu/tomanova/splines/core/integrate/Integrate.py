import sympy
import math

from edu.tomanova.splines.plate.Triangle import Triangle
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
        self.grid = triangle
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
            p1 = self.func.subs({x: self.grid[i].norm12.point.x, y: self.grid[i].norm12.point.y})
            p2 = self.func.subs({x: self.grid[i].norm23.point.x, y: self.grid[i].norm23.point.y})
            p3 = self.func.subs({x: self.grid[i].norm13.point.x, y: self.grid[i].norm13.point.y})
            self.integral += (p1 + p2 + p3) * self.square(number) / 3

        return self.integral

    def divideTriangles(self):
        """
        Divide grid for integration
        """
        triangles = self.grid

        for i in range(self.count):
            temp = []

            for triangle in triangles:
                temp.append(Triangle(triangle.apex1, triangle.norm12.point, triangle.norm13.point))
                temp.append(Triangle(triangle.norm12.point, triangle.norm13.point, triangle.norm23.point))
                temp.append(Triangle(triangle.norm12.point, triangle.apex2, triangle.norm23.point))
                temp.append(Triangle(triangle.norm23.point, triangle.norm13.point, triangle.apex3))

            triangles = temp

        self.grid = triangles

    def p(self, number):
        """
        Additional function
        """
        return (self.grid[number].apex1.distance(self.grid[number].apex2) +
                self.grid[number].apex2.distance(self.grid[number].apex3) +
                self.grid[number].apex1.distance(self.grid[number].apex3)) / 2

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
            (self.p(number) - self.grid[number].apex1.distance(self.grid[number].apex2)) *
            (self.p(number) - self.grid[number].apex2.distance(self.grid[number].apex3)) *
            (self.p(number) - self.grid[number].apex1.distance(self.grid[number].apex3)))
