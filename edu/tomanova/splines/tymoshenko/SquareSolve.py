import sympy

from math import pow
from math import pi
from sympy import cos
from sympy import cosh
from sympy import sinh
from sympy import tanh

x, y = sympy.symbols(('x', 'y'))


class Solution:

    def __init__(self, plate, d=1, q=1, n=55):
        self.plate = plate
        self.d = d
        self.q = q
        self.n = n

    def build(self):
        return self.calculateW0()

    def calculateW0(self):
        res = 0

        for m in range(1, self.n, 2):
            res += \
                pow(-1, (m - 1) / 2) / pow(m, 5) * \
                cos((m * pi * x) / (2 * self.plate.b1)) * (
                        1 - (self.alpha(m) * tanh(self.alpha(m)) + 2) * cosh((m * pi * y) / (2 * self.plate.b1)) /
                        (2 * cosh(self.alpha(m))) + sinh((m * pi * y) / (2 * self.plate.b1)) * m * pi * y / (
                                4 * self.plate.b1 * cosh(self.alpha(m))))

        return res

    def alpha(self, m):
        return (m * pi * self.plate.b2) / (2 * self.plate.b1)

    def beta(self, m):
        return (m * pi * self.plate.b1) / (2 * self.plate.b2)
