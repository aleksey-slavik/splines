import sympy

from edu.tomanova.splines.plate.Apex import Apex
"""
Consist data of normal

@author: iryna.tomanova
"""


class Normal:

    def __init__(self, apex1, apex2):
        """
        Setup initial data

        Parameters
        ----------
        apex1: Apex
            left point of line segment
        apex2: Apex
            right point of line segment
        """
        self.apex1 = apex1
        self.apex2 = apex2
        self.point = Apex(
            (apex1.x + apex2.x) / 2,
            (apex1.y + apex2.y) / 2)
        self.dn = 0

    def setDN(self, dn):
        """
        Change value of dn parameter for current normal

        Parameters
        ----------
        dn: float
            value of dn parameter for current normal
        """
        self.dn = dn

    def delta(self, apex):
        """
        Represent delta(i,j,k)

        Return
        ------
        det: expression
            determinant of matrix delta(i,j,k)
        """
        matrix = sympy.Matrix(
            [[self.apex1.x, self.apex1.y, 1],
             [self.apex2.x, self.apex2.y, 1],
             [apex.x, apex.y, 1]])

        return matrix.det()

    def sign(self, apex):
        """
        Represent direction of normal derivative depends on 3rd apex of triangle

        Return
        ------
        value: int
            direction of normal derivative
        """
        value = self.delta(apex)

        if value > 0:
            return 1
        elif value < 0:
            return -1
        else:
            return 0

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.point == other.point
