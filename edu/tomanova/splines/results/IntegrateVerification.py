import sympy

from edu.tomanova.splines.plate.Apex import Apex
from edu.tomanova.splines.plate.Triangle import Triangle
from edu.tomanova.splines.core.integrate.Integrate import Integrate
"""
Contains verification of integration function

@author: iryna.tomanova
"""

x, y = sympy.symbols(('x', 'y'))
triangle = Triangle(Apex(0, 0), Apex(1, 0), Apex(0, 1))
integrand = Integrate(triangle, x + y)
result = integrand.integrate()
print(result)
