import sympy
import math

from edu.tomanova.splines.plate.Triangle import Triangle
from edu.tomanova.splines.core.Derivative import Derivative

x, y = sympy.symbols(('x', 'y'))


class Integrate:

    def __init__(self, triangles, splines, q=1, count=3):
        self.grid = triangles
        self.splines = splines
        self.q = q
        self.count = count
        self.points = []

    def integrate(self):
        res = 0

        for i in range(len(self.grid)):
            number = math.floor(i / math.pow(4, self.count))
            value = (self.dS(Derivative(2, 0), number) + self.dS(Derivative(0, 2), number)) ** 2 - \
                2 * self.q * self.splines[number]
            p1 = value.subs({x: self.grid[i].norm12.point.x, y: self.grid[i].norm12.point.y})
            p2 = value.subs({x: self.grid[i].norm23.point.x, y: self.grid[i].norm23.point.y})
            p3 = value.subs({x: self.grid[i].norm13.point.x, y: self.grid[i].norm13.point.y})
            res += (p1 + p2 + p3) * self.square(number) / 3

        return res

    def divideTriangles(self):
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

    def dS(self, derivative, number):
        return sympy.diff(self.splines[number], x, derivative.dx, y, derivative.dy)

    def p(self, number):
        return (self.grid[number].apex1.distance(self.grid[number].apex2) +
                self.grid[number].apex2.distance(self.grid[number].apex3) +
                self.grid[number].apex1.distance(self.grid[number].apex3)) / 2

    def square(self, number):
        return sympy.sqrt(
            self.p(number) *
            (self.p(number) - self.grid[number].apex1.distance(self.grid[number].apex2)) *
            (self.p(number) - self.grid[number].apex2.distance(self.grid[number].apex3)) *
            (self.p(number) - self.grid[number].apex1.distance(self.grid[number].apex3)))
