import sympy
from sympy.solvers.solveset import linsolve
from edu.tomanova.splines.core.SplineBuilder import SplineBuilder
from edu.tomanova.splines.core.integrate.Integrate import Integrate


class Solver:

    def __init__(self, rule):
        self.rule = rule
        self.rule.setParams()
        self.splines = []

    def solve(self):
        integral = 0

        for triangle in self.rule.triangles:
            splineBuilder = SplineBuilder(triangle)
            splineBuilder.build()
            self.splines.append(splineBuilder.spline)
            integral += Integrate(triangle, splineBuilder.spline).integrate()

        system = self.system(integral)
        params = sympy.symbols("p1:{0}".format(self.rule.count + 1))
        roots = linsolve(system, params)
        splines = []

        for spline in self.splines:
            splines.append(spline.subs(roots))

        self.splines = splines

    def system(self, expression):
        system = []

        for i in range(self.rule.count):
            system.append(sympy.diff(expression, sympy.symbols("p{0}".format(i + 1))))

        return system
