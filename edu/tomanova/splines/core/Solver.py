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

        return integral
