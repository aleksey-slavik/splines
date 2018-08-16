import sympy

from math import factorial
from edu.tomanova.splines.core.Spline import Spline
from edu.tomanova.splines.core.Derivative import Derivative
from edu.tomanova.splines.plate.Triangle import Triangle
from edu.tomanova.splines.plate.Apex import Apex
"""
Contains verification of properties of spline of 5th degree 
on triangle with apexes (0, 0), (d, 0), (0, d) for function of 6th degree

@author: iryna.tomanova
"""

x, y, d = sympy.symbols(('x', 'y', 'd'))

apex1 = Apex(0, 0)
apex2 = Apex(d, 0)
apex3 = Apex(0, d)

f = \
    x ** 6 / factorial(6) + \
    x ** 5 * y / factorial(5) + \
    x ** 4 * y ** 2 / factorial(4) / factorial(2) + \
    x ** 3 * y ** 3 / factorial(3) / factorial(3) + \
    x ** 2 * y ** 4 / factorial(4) / factorial(2) + \
    x * y ** 5 / factorial(5) + \
    y ** 6 / factorial(6)

triangle = Triangle(apex1, apex2, apex3)
spline = Spline(triangle)

print('Verification for h:')
h100 = spline.h(1, Derivative(0, 0))
h110 = spline.h(1, Derivative(1, 0))
h101 = spline.h(1, Derivative(0, 1))
h120 = spline.h(1, Derivative(2, 0))
h111 = spline.h(1, Derivative(1, 1))
h102 = spline.h(1, Derivative(0, 2))

h200 = spline.h(2, Derivative(0, 0))
h210 = spline.h(2, Derivative(1, 0))
h201 = spline.h(2, Derivative(0, 1))
h220 = spline.h(2, Derivative(2, 0))
h211 = spline.h(2, Derivative(1, 1))
h202 = spline.h(2, Derivative(0, 2))

h300 = spline.h(3, Derivative(0, 0))
h310 = spline.h(3, Derivative(1, 0))
h301 = spline.h(3, Derivative(0, 1))
h320 = spline.h(3, Derivative(2, 0))
h311 = spline.h(3, Derivative(1, 1))
h302 = spline.h(3, Derivative(0, 2))

print("h(1,0,0) = {0}".format(h100))
print("h(1,1,0) = {0}".format(h110))
print("h(1,0,1) = {0}".format(h101))
print("h(1,2,0) = {0}".format(h120))
print("h(1,1,1) = {0}".format(h111))
print("h(1,0,2) = {0}".format(h102))

print("h(2,0,0) = {0}".format(h200))
print("h(2,1,0) = {0}".format(h210))
print("h(2,0,1) = {0}".format(h201))
print("h(2,2,0) = {0}".format(h220))
print("h(2,1,1) = {0}".format(h211))
print("h(2,0,2) = {0}".format(h202))

print("h(3,0,0) = {0}".format(h300))
print("h(3,1,0) = {0}".format(h310))
print("h(3,0,1) = {0}".format(h301))
print("h(3,2,0) = {0}".format(h320))
print("h(3,1,1) = {0}".format(h311))
print("h(3,0,2) = {0}".format(h302))
