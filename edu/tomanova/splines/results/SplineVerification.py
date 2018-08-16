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


def Dh(func, derivative, point):
    value = sympy.diff(func, x, derivative.dx, y, derivative.dy)
    return value.subs({x: point.x, y: point.y})


triangle = Triangle(apex1, apex2, apex3)
spline = Spline(triangle)

print("h(1,0,0) = {0}".format(spline.h(1, Derivative(0, 0))))
print("h(1,1,0) = {0}".format(spline.h(1, Derivative(1, 0))))
print("h(1,0,1) = {0}".format(spline.h(1, Derivative(0, 1))))
print("h(1,2,0) = {0}".format(spline.h(1, Derivative(2, 0))))
print("h(1,1,1) = {0}".format(spline.h(1, Derivative(1, 1))))
print("h(1,0,2) = {0}".format(spline.h(1, Derivative(0, 2))))

print("h(2,0,0) = {0}".format(spline.h(2, Derivative(0, 0))))
print("h(2,1,0) = {0}".format(spline.h(2, Derivative(1, 0))))
print("h(2,0,1) = {0}".format(spline.h(2, Derivative(0, 1))))
print("h(2,2,0) = {0}".format(spline.h(2, Derivative(2, 0))))
print("h(2,1,1) = {0}".format(spline.h(2, Derivative(1, 1))))
print("h(2,0,2) = {0}".format(spline.h(2, Derivative(0, 2))))

print("h(3,0,0) = {0}".format(spline.h(3, Derivative(0, 0))))
print("h(3,1,0) = {0}".format(spline.h(3, Derivative(1, 0))))
print("h(3,0,1) = {0}".format(spline.h(3, Derivative(0, 1))))
print("h(3,2,0) = {0}".format(spline.h(3, Derivative(2, 0))))
print("h(3,1,1) = {0}".format(spline.h(3, Derivative(1, 1))))
print("h(3,0,2) = {0}".format(spline.h(3, Derivative(0, 2))))

print('Verification for h:')
print('-----------------------------------------------------------------------------')
print('|(x,y)  |(dx,dy)|h(x,y)   |dxh(x,y) |dyh(x,y) |dxxh(x,y)|dxyh(x,y)|dyyh(x,y)|')
print('-----------------------------------------------------------------------------')
for tr in range(3):
    for n in range(3):
        for m in range(n + 1):
            h = Dh(spline.h(tr + 1, Derivative(0, 0)), Derivative(n - m, m), triangle.apexes()[tr])
            dxh = Dh(spline.h(tr + 1, Derivative(1, 0)), Derivative(n - m, m), triangle.apexes()[tr])
            dyh = Dh(spline.h(tr + 1, Derivative(0, 1)), Derivative(n - m, m), triangle.apexes()[tr])
            dxxh = Dh(spline.h(tr + 1, Derivative(2, 0)), Derivative(n - m, m), triangle.apexes()[tr])
            dxyh = Dh(spline.h(tr + 1, Derivative(1, 1)), Derivative(n - m, m), triangle.apexes()[tr])
            dyyh = Dh(spline.h(tr + 1, Derivative(0, 2)), Derivative(n - m, m), triangle.apexes()[tr])

            print("|({0},{1})  |({2},{3})  |{4}        |{5}        |{6}        |{7}        |{8}        |{9}        |"
                .format(
                    triangle.apexes()[tr].x, triangle.apexes()[tr].y,
                    n - m, m,
                    h, dxh, dyh, dxxh, dxyh, dyyh))
            print('-----------------------------------------------------------------------------')
