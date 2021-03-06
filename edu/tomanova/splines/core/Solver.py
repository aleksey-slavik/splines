import sympy

from edu.tomanova.splines.core.SplineBuilder import SplineBuilder
from edu.tomanova.splines.core.integrate.Integrate import Integrate
from edu.tomanova.splines.core.rule.Rule import Rule

"""
Contains function for solve system of equations for find parameters of spline

@author: iryna.tomanova
"""

x, y = sympy.symbols(('x', 'y'))


class Solver:

    def __init__(self, rule, q=1):
        """
        Setup initial data

        Parameters
        ----------
        rule: Rule
            rules for set parameters for apexes and normals
        q: expression
            right part of biharmonical equation
        """
        self.q = q
        self.rule = rule
        self.splines = []

    def solve(self):
        """
        Find parameters of spline
        """
        integral = 0

        for triangle in self.rule.triangles:
            tmpSpline = SplineBuilder(triangle).build()
            self.splines.append(tmpSpline)
            tmpIntegral = Integrate(triangle, self.integrand(tmpSpline)).integrate()
            integral += tmpIntegral

        system = self.system(integral)
        params = sympy.symbols("p1:{0}".format(self.rule.count + 1))
        roots = sympy.solve(system, params)
        splines = []

        for spline in self.splines:
            splines.append(spline.subs(roots))

        self.splines = splines

    def integrand(self, spline):
        """
        Create integrand for given spline

        Parameters
        ----------
        spline: expression
            given spline

        Return
        ------
        spline: expression
            integrand for given spline
        """
        return (sympy.diff(spline, x, 2) + sympy.diff(spline, y, 2)) ** 2 - 2 * self.q * spline

    def system(self, expression):
        """
        Create system of equations for given expression

        Parameters
        ----------
        expression: expression
            given expression

        Return
        ------
        system: list
            system of equations for given expression
        """
        system = []

        for i in range(self.rule.count):
            system.append(sympy.diff(expression, sympy.symbols("p{0}".format(i + 1))))

        return system
