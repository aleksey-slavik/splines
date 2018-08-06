import sympy

from math import pow
from math import pi
from sympy import cos
from sympy import cosh
from sympy import sinh
from sympy import tanh
from sympy.plotting import plot3d

from typing import Any, Union

from edu.tomanova.splines.plate.SquarePlate import SquarePlate

x, y = sympy.symbols(('x', 'y'))


class Solution:
    solution: Union[int, Any]
    params: Union[int, Any]

    def __init__(self, plate, d=1, q=1, n=25):
        self.plate = plate
        self.d = d
        self.q = q
        self.n = n
        self.vars = sympy.symbols('t0:%s' % self.n)

    def build(self):
        self.getParams()
        self.solution = self.calculateW0() + self.calculateW1() + self.calculateW2()
        return self.solution

    def plot(self):
        plot3d(self.solution, (x, self.plate.a1, self.plate.a2), (y, self.plate.b1, self.plate.b2))

    def valueAt(self, a, b):
        return self.solution.subs({x: a, y: b})

    def calculateW0(self):
        res = 0

        for m in range(1, self.n, 2):
            res += \
                pow(-1, (m - 1) / 2) / pow(m, 5) * \
                cos((m * pi * x) / (2 * self.plate.b1)) * \
                (1 - (self.alpha(m) * tanh(self.alpha(m)) + 2) * cosh((m * pi * y) / (2 * self.plate.b1)) /
                 (2 * cosh(self.alpha(m))) + sinh((m * pi * y) / (2 * self.plate.b1)) * m * pi * y /
                 (4 * self.plate.b1 * cosh(self.alpha(m))))

        res *= 4 * self.q * pow(2 * self.plate.b1, 4) / (pow(pi, 5) * self.d)

        return res

    def calculateW1(self):
        res = 0

        for m in range(1, self.n, 2):
            res += (self.params.get(self.vars[m]) * pow(-1, (m - 1) / 2) * cos((m * pi * x) / (2 * self.plate.b1))) / \
                   (pow(m, 2) * cosh(self.alpha(m))) * ((m * pi * y * sinh(m * pi * y / (2 * self.plate.b1))) /
                                                        (2 * self.plate.b1) - self.alpha(m) *
                                                        tanh(self.alpha(m)) * cosh(
                        m * pi * y / (2 * self.plate.b1)))

        res *= -pow(2 * self.plate.b1, 2) / (2 * pow(pi, 2) * self.d)
        return res

    def calculateW2(self):
        res = 0

        for m in range(1, self.n, 2):
            res += (self.params.get(self.vars[m]) * pow(-1, (m - 1) / 2) * cos((m * pi * y) / (2 * self.plate.b2))) / \
                   (pow(m, 2) * cosh(self.beta(m))) * ((m * pi * x * sinh(m * pi * x / (2 * self.plate.b2))) /
                                                       (2 * self.plate.b2) - self.beta(m) *
                                                       tanh(self.beta(m)) * cosh(
                        m * pi * x / (2 * self.plate.b2)))

        res *= -pow(2 * self.plate.b2, 2) / (2 * pow(pi, 2) * self.d)
        return res

    def getParams(self):
        system = []

        for i in range(1, self.n, 2):
            val = 0

            for m in range(1, self.n, 2):
                val += self.vars[m] / pow(m, 3) / pow((1 + pow(i, 2) / pow(m, 2)), 2)

            system.append(
                sympy.Eq(self.vars[i] / i *
                         (tanh(self.alpha(i)) + self.alpha(i) / cosh(self.alpha(i)) ** 2) + 8 * i / pi * val,
                         4 * self.q * (2 * self.plate.b1) ** 2 / (pi ** 3 * i ** 4) *
                         (self.alpha(i) / cosh(self.alpha(i)) ** 2 - tanh(self.alpha(i)))))

        self.params = sympy.solve(system, self.vars)
        return self.params

    def alpha(self, m):
        return (m * pi * self.plate.b2) / (2 * self.plate.b1)

    def beta(self, m):
        return (m * pi * self.plate.b1) / (2 * self.plate.b2)


pl = SquarePlate(-0.5, 0.5, -0.5, 0.5)
sol = Solution(pl)
print(sol.build())
print(sol.valueAt(0, 0))
sol.plot()
