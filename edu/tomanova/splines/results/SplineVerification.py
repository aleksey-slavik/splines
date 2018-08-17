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

x, y = sympy.symbols(('x', 'y'))
d = sympy.symbols('d', positive=True)

f = \
    x ** 6 / factorial(6) + \
    x ** 5 * y / factorial(5) + \
    x ** 4 * y ** 2 / factorial(4) / factorial(2) + \
    x ** 3 * y ** 3 / factorial(3) / factorial(3) + \
    x ** 2 * y ** 4 / factorial(4) / factorial(2) + \
    x * y ** 5 / factorial(5) + \
    y ** 6 / factorial(6)


def Df(func, derivative, point):
    """
    Compute derivative of given function in given point

    Parameters
    ----------
    func: expression
        given function
    derivative: Derivative
        given derivative
    point: Apex
        given point

    Return
    ------
    value: float
        value of derivative of given function in given point
    """
    value = sympy.diff(func, x, derivative.dx, y, derivative.dy)
    return value.subs({x: point.x, y: point.y})


def Dn12(func):
    """
    Compute normal derivative for side of triangle between 1st and 2nd apexes

    Parameters
    ----------
    func: expression
        given function

    Return
    ------
    value: float
        value of derivative of given function
    """
    value = sympy.diff(func, y)
    return value.subs({x: triangle.norm12.point.x, y: triangle.norm12.point.y})


def Dn23(func):
    """
    Compute normal derivative for side of triangle between 2nd and 3rd apexes

    Parameters
    ----------
    func: expression
        given function

    Return
    ------
    value: float
        value of derivative of given function
    """
    value = (-1 / sympy.sqrt(2)) * (sympy.diff(func, x) + sympy.diff(func, y))
    return value.subs({x: triangle.norm23.point.x, y: triangle.norm23.point.y})


def Dn13(func):
    """
    Compute normal derivative for side of triangle between 1st and 3rd apexes

    Parameters
    ----------
    func: expression
        given function

    Return
    ------
    value: float
        value of derivative of given function
    """
    value = sympy.diff(func, x)
    return value.subs({x: triangle.norm13.point.x, y: triangle.norm13.point.y})


apex1 = Apex(0, 0)
apex1.params(Df(f, Derivative(0, 0), apex1),
             Df(f, Derivative(1, 0), apex1),
             Df(f, Derivative(0, 1), apex1),
             Df(f, Derivative(2, 0), apex1),
             Df(f, Derivative(1, 1), apex1),
             Df(f, Derivative(0, 2), apex1))

apex2 = Apex(d, 0)
apex2.params(Df(f, Derivative(0, 0), apex2),
             Df(f, Derivative(1, 0), apex2),
             Df(f, Derivative(0, 1), apex2),
             Df(f, Derivative(2, 0), apex2),
             Df(f, Derivative(1, 1), apex2),
             Df(f, Derivative(0, 2), apex2))

apex3 = Apex(0, d)
apex3.params(Df(f, Derivative(0, 0), apex3),
             Df(f, Derivative(1, 0), apex3),
             Df(f, Derivative(0, 1), apex3),
             Df(f, Derivative(2, 0), apex3),
             Df(f, Derivative(1, 1), apex3),
             Df(f, Derivative(0, 2), apex3))

triangle = Triangle(apex1, apex2, apex3)
triangle.norm12.dn = Dn12(f)
triangle.norm23.dn = Dn23(f)
triangle.norm13.dn = Dn13(f)

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
print('-----------------------------------------------')
print('|(x,y)  |(dx,dy)|h   |dxh |dyh |dxxh|dxyh|dyyh|')
print('-----------------------------------------------')

for tr in range(3):
    for n in range(3):
        for m in range(n + 1):
            h = Df(spline.h(tr + 1, Derivative(0, 0)), Derivative(n - m, m), triangle.apexes[tr])
            dxh = Df(spline.h(tr + 1, Derivative(1, 0)), Derivative(n - m, m), triangle.apexes[tr])
            dyh = Df(spline.h(tr + 1, Derivative(0, 1)), Derivative(n - m, m), triangle.apexes[tr])
            dxxh = Df(spline.h(tr + 1, Derivative(2, 0)), Derivative(n - m, m), triangle.apexes[tr])
            dxyh = Df(spline.h(tr + 1, Derivative(1, 1)), Derivative(n - m, m), triangle.apexes[tr])
            dyyh = Df(spline.h(tr + 1, Derivative(0, 2)), Derivative(n - m, m), triangle.apexes[tr])

            print("|({0},{1})  |({2},{3})  |{4}   |{5}   |{6}   |{7}   |{8}   |{9}   |".format(
                    triangle.apexes[tr].x, triangle.apexes[tr].y,
                    n - m, m,
                    h, dxh, dyh, dxxh, dxyh, dyyh))

            print('-----------------------------------------------')

w = sympy.simplify(spline.w())
print("w = {0}".format(w))
print('Verification for w:')
print('-------------------------------------------------------------------')
print('|(x,y)|f-w      |dxf-dxh  |dyf-dyh  |dxxf-dxxh|dxyf-dxyh|dyyf-dyyh|')
print('-------------------------------------------------------------------')

for tr in range(3):
    fw = Df(f, Derivative(0, 0), triangle.apexes[tr]) - Df(w, Derivative(0, 0), triangle.apexes[tr])
    dxfw = Df(f, Derivative(1, 0), triangle.apexes[tr]) - Df(w, Derivative(1, 0), triangle.apexes[tr])
    dyfw = Df(f, Derivative(0, 1), triangle.apexes[tr]) - Df(w, Derivative(0, 1), triangle.apexes[tr])
    dxxfw = Df(f, Derivative(2, 0), triangle.apexes[tr]) - Df(w, Derivative(2, 0), triangle.apexes[tr])
    dxyfw = Df(f, Derivative(1, 1), triangle.apexes[tr]) - Df(w, Derivative(1, 1), triangle.apexes[tr])
    dyyfw = Df(f, Derivative(0, 2), triangle.apexes[tr]) - Df(w, Derivative(0, 2), triangle.apexes[tr])

    print("|({0},{1})|{2}        |{3}        |{4}        |{5}        |{6}        |{7}        |".format(
            triangle.apexes[tr].x, triangle.apexes[tr].y,
            fw, dxfw, dyfw, dxxfw, dxyfw, dyyfw))

    print('-------------------------------------------------------------------')

print("H(1,2) = {0}".format(spline.H(1, 2)))
print("H(1,3) = {0}".format(spline.H(1, 3)))
print("H(2,3) = {0}".format(spline.H(2, 3)))
print('Verification for H:')
print('Verification at middle points:')
print('----------------------------------')
print('|H(i,j)|(x,y)     |dn12|dn13|dn23|')
print('----------------------------------')
alias = ['H(1,2)', 'H(1,3)', 'H(2,3)']
listH = [spline.H(1, 2), spline.H(1, 3), spline.H(2, 3)]

for tr in range(3):
    dn12 = Dn12(listH[tr])
    dn13 = Dn13(listH[tr])
    dn23 = Dn23(listH[tr])

    print("|{0}|({1}, {2})|{3}   |{4}   |{5}   |".format(
        alias[tr],
        triangle.normals[tr].point.x, triangle.normals[tr].point.y,
        dn12, dn13, dn23
    ))

    print('----------------------------------')

print('Verification at apexes:')
print('-----------------------------')
print('|H(i,j)|(x,y)  |(dx,dy)|H   |')
print('-----------------------------')

for tr in range(3):
    for n in range(3):
        for m in range(n + 1):
            H = Df(listH[tr], Derivative(n - m, m), triangle.apexes[tr])

            print("|{0}|({1},{2})  |({3},{4})  |{5}   |".format(
                    alias[tr],
                    triangle.apexes[tr].x, triangle.apexes[tr].y,
                    n - m, m,
                    H))

            print('-----------------------------')

S = sympy.simplify(spline.build())
print("S5 = {0}".format(S))
print('Verification for S5:')
print('Verification at apexes:')
print('------------------------')
print('|(x,y)  |(dx,dy)|f-S   |')
print('------------------------')

for tr in range(3):
    for n in range(3):
        for m in range(n + 1):
            fS = Df(f, Derivative(n - m, m), triangle.apexes[tr]) - Df(S, Derivative(n - m, m), triangle.apexes[tr])

            print("|({0},{1})  |({2},{3})  |{4}     |".format(
                    triangle.apexes[tr].x, triangle.apexes[tr].y,
                    n - m, m,
                    fS))

            print('------------------------')

print('Verification at middle points:')
print('------------------')
print('|(x,y)    |f-S   |')
print('------------------')
listS = [Dn12(f) - Dn12(S), Dn13(f) - Dn13(S), Dn23(f) - Dn23(S)]

for tr in range(3):
    print("|({0},{1})|{2}     |".format(
        triangle.normals[tr].point.x, triangle.normals[tr].point.y,
        listS[tr]))

    print('------------------')
