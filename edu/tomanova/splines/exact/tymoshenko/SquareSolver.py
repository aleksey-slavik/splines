import sympy

from math import pow
from math import pi

from sympy import cos
from sympy import cosh
from sympy import sinh
from sympy import tanh
from sympy.plotting import plot3d
"""
Contains exact solution for square plate depends on Tymoshenko works

@author: iryna.tomanova
"""

x, y = sympy.symbols(('x', 'y'))


class Solver:
    """
    Contains solution data and necessary methods for work with him
    """

    def __init__(self, plate, d=1, q=1, n=25):
        """
        Setup initial data

        Parameters
        ----------
        plate: object
            square plate parameters
        d: float
            equation parameter
        q: float
            equation parameter
        n: int
            size of series of solution
        """
        self.plate = plate
        self.d = d
        self.q = q
        self.n = n
        self.vars = sympy.symbols('t0:%s' % self.n)

    def build(self):
        """
        Create solution for current object

        Returns
        -------
        solution: polynomial expression
            exact solution
        """
        self.getParams()
        self.solution = self.calculateW0() - self.calculateW1() - self.calculateW2()
        return self.solution

    def plot3d(self):
        """
        Plot 3-dimensional surface
        Important! Need to build solution before call this method
        """
        return plot3d(self.solution, (x, self.plate.apex1.x, self.plate.apex2.x), (y, self.plate.apex1.y, self.plate.apex2.y))

    def valueAt(self, a, b, isNormalized=False):
        """
        Get value of solution in given point
        Important! Need to build solution before call this method

        Parameters
        ----------
        a: float
            x coordinate
        b: float
            y coordinate
        isNormalized: bool
            true, if value must be normalized, false, in otherwise

        Returns
        -------
        value: float
            value of solution in given point
        """
        value = self.solution.subs({x: a, y: b})

        if isNormalized:
            return value * pow((self.plate.apex2.x - self.plate.apex1.x), -4)
        else:
            return value

    def calculateW0(self):
        """
        Calculate additional function W0(x,y) for solution depends on works of Tymoshenko

        Returns
        -------
        res: polynomial expression
            additional function W0(x,y)
        """
        res = 0

        for m in range(1, self.n, 2):
            res += \
                pow(-1, (m - 1) / 2) / pow(m, 5) * \
                cos((m * pi * x) / (2 * self.plate.apex2.x)) * \
                (1 - (self.alpha(m) * tanh(self.alpha(m)) + 2) * cosh((m * pi * y) / (2 * self.plate.apex2.x)) /
                 (2 * cosh(self.alpha(m))) + sinh((m * pi * y) / (2 * self.plate.apex2.x)) * m * pi * y /
                 (4 * self.plate.apex2.x * cosh(self.alpha(m))))

        res *= 4 * self.q * pow(2 * self.plate.apex2.x, 4) / (pow(pi, 5) * self.d)
        return res

    def calculateW1(self):
        """
        Calculate additional function W1(x,y) for solution depends on works of Tymoshenko

        Returns
        -------
        res: polynomial expression
            additional function W1(x,y)
        """
        res = 0

        for m in range(1, self.n, 2):
            res += (self.params.get(self.vars[m]) * pow(-1, (m - 1) / 2) * cos((m * pi * x) / (2 * self.plate.apex2.x))) / \
                   (pow(m, 2) * cosh(self.alpha(m))) * ((m * pi * y * sinh(m * pi * y / (2 * self.plate.apex2.x))) /
                                                        (2 * self.plate.apex2.x) - self.alpha(m) *
                                                        tanh(self.alpha(m)) * cosh(
                        m * pi * y / (2 * self.plate.apex2.x)))

        res *= pow(2 * self.plate.apex2.x, 2) / (2 * pow(pi, 2) * self.d)
        return res

    def calculateW2(self):
        """
        Calculate additional function W2(x,y) for solution depends on works of Tymoshenko

        Returns
        -------
        res: polynomial expression
            additional function W2(x,y)
        """
        res = 0

        for m in range(1, self.n, 2):
            res += (self.params.get(self.vars[m]) * pow(-1, (m - 1) / 2) * cos((m * pi * y) / (2 * self.plate.apex2.y))) / \
                   (pow(m, 2) * cosh(self.beta(m))) * ((m * pi * x * sinh(m * pi * x / (2 * self.plate.apex2.y))) /
                                                       (2 * self.plate.apex2.y) - self.beta(m) *
                                                       tanh(self.beta(m)) * cosh(
                        m * pi * x / (2 * self.plate.apex2.y)))

        res *= pow(2 * self.plate.apex2.y, 2) / (2 * pow(pi, 2) * self.d)
        return res

    def getParams(self):
        """
        Solve system for getting parameters for calculate W1(x,y) and W2(x,y) depends on works of Tymoshenko

        Returns
        -------
        res: dictionary
            roots of system
        """
        system = []

        for i in range(1, self.n, 2):
            val = 0

            for m in range(1, self.n, 2):
                val += self.vars[m] / pow(m, 3) / pow((1 + pow(i, 2) / pow(m, 2)), 2)

            system.append(
                sympy.Eq(self.vars[i] / i *
                         (tanh(self.alpha(i)) + self.alpha(i) / pow(cosh(self.alpha(i)), 2)) + 8 * i / pi * val,
                         4 * self.q * pow((2 * self.plate.apex2.x), 2) / (pow(pi, 3) * pow(i, 4)) *
                         (self.alpha(i) / pow(cosh(self.alpha(i)), 2) - tanh(self.alpha(i)))))

        self.params = sympy.solve(system, self.vars)
        return self.params

    def alpha(self, m):
        """
        Additional function. Used in calculations of W0(x,y), W1(x,y) and W2(x,y)

        Parameters
        ----------
        m: int
            initial parameter

        Returns
        -------
        alpha: float
            value for calculations
        """
        return (m * pi * self.plate.apex2.y) / (2 * self.plate.apex2.x)

    def beta(self, m):
        """
        Additional function. Used in calculations of W0(x,y), W1(x,y) and W2(x,y)

        Parameters
        ----------
        m: int
            initial parameter

        Returns
        -------
        beta: float
            value for calculations
        """
        return (m * pi * self.plate.apex2.x) / (2 * self.plate.apex2.y)
