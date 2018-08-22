import sympy
import math

from edu.tomanova.splines.plate.Triangle import Triangle
from edu.tomanova.splines.core.Derivative import Derivative

x, y = sympy.symbols(('x', 'y'))


class Integrate:

    def __init__(self, triangles, splines, q, count=3):
        self.triangles = triangles
        self.grid = triangles
        self.splines = splines
        self.q = q
        self.count = count
        self.points = []

    def integrate(self):
        res = 0

        for i in range(len(self.triangles)):
            number = math.floor(i / math.pow(4, self.count))
            value = (self.dS(Derivative(2, 0), number) + self.dS(Derivative(0, 2), number)) ** 2 - \
                2 * self.q * self.splines[number]
            p1 = value.subs()
            p2 = value.subs()
            p3 = value.subs()
            res += (p1 + p2 + p3) * self.sqrt(number) / 3

        return res

    def divideTriangles(self):
        triangles = self.triangles

        for i in range(self.count):
            temp = []

            for triangle in triangles:
                temp.append(Triangle(triangle.apex1, triangle.norm12.point, triangle.norm13.point))
                temp.append(Triangle(triangle.norm12.point, triangle.norm13.point, triangle.norm23.point))
                temp.append(Triangle(triangle.norm12.point, triangle.apex2, triangle.norm23.point))
                temp.append(Triangle(triangle.norm23.point, triangle.norm13.point, triangle.apex3))

            triangles = temp

        self.triangles = triangles

    def dS(self, derivative, number):
        return sympy.diff(self.splines(number), x, derivative.dx, y, derivative.dy)

    def p(self, number):
        return (self.triangles[number].apex1.distance(self.triangles[number].apex2) +
                self.triangles[number].apex2.distance(self.triangles[number].apex3) +
                self.triangles[number].apex1.distance(self.triangles[number].apex3)) / 2

    def sqrt(self, number):
        return sympy.sqrt(
            self.p(number) *
            (self.p(number) - self.triangles[number].apex1.distance(self.triangles[number].apex2)) *
            (self.p(number) - self.triangles[number].apex2.distance(self.triangles[number].apex3)) *
            (self.p(number) - self.triangles[number].apex1.distance(self.triangles[number].apex3)))
