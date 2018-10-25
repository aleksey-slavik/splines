import sympy

from edu.tomanova.splines.core.plate.Point import Point

"""
Represent a triangle element of integration grid

@author: iryna.tomanova
"""


class Element:

    def __init__(self, point1, point2, point3):
        """
        Setup initial data

        Parameters
        ----------
        point1: Point
            first point of element
        point2: Point
            second point of element
        point3: Point
            third point of element
        """
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.middle12 = Point((point1.x + point2.x) / 2, (point1.y + point2.y) / 2)
        self.middle13 = Point((point1.x + point3.x) / 2, (point1.y + point3.y) / 2)
        self.middle23 = Point((point2.x + point3.x) / 2, (point2.y + point3.y) / 2)

    def square(self):
        """
        Using Heron's formula calculate square of triangle element
        """
        a = self.point1.distance(self.point2)
        b = self.point1.distance(self.point3)
        c = self.point2.distance(self.point3)
        p = (a + b + c) / 2

        return sympy.sqrt(p * (p - a) * (p - b) * (p - c))

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.point1 == other.point1 and self.point2 == other.point2 and self.point3 == other.point3
