import sympy

from edu.tomanova.splines.core.SplineBuilder import SplineBuilder
from edu.tomanova.splines.core.integrate.Integrate import Integrate

x, y = sympy.symbols(('x', 'y'))


class Solver:

    def __init__(self, rule, q=1):
        self.q = q
        self.rule = rule
        self.rule.setParams()
        self.splines = []

    def solve(self):
        integral = 0

        for triangle in self.rule.triangles:
            splineBuilder = SplineBuilder(triangle)
            splineBuilder.build()
            self.splines.append(splineBuilder.spline)
            integral += Integrate(triangle, self.integrand(splineBuilder.spline)).integrate()

        system = self.system(integral)
        params = sympy.symbols("p1:{0}".format(self.rule.count + 1))
        roots = sympy.solve(system, params)
        splines = []

        for spline in self.splines:
            splines.append(spline.subs(roots))

        self.splines = splines

    def integrand(self, spline):
        return (sympy.diff(spline, x, 2) + sympy.diff(spline, y, 2)) ** 2 - 2 * self.q * spline

    def system(self, expression):
        system = []

        for i in range(self.rule.count):
            system.append(sympy.diff(expression, sympy.symbols("p{0}".format(i + 1))))

        return system
