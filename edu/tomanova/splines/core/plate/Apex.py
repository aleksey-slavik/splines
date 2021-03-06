import sympy

from edu.tomanova.splines.core.Derivative import Derivative
from edu.tomanova.splines.core.plate.Point import Point

"""
Consist data of apex

@author: iryna.tomanova
"""


class Apex(Point):

    def __init__(self, x, y):
        """
        Setup initial data

        Parameters
        ----------
        x: float
            x coordinate of  apex
        y: float
            y coordinate of  apex
        """
        super().__init__(x, y)
        self.f = 0
        self.dxf = 0
        self.dyf = 0
        self.dxxf = 0
        self.dxyf = 0
        self.dyyf = 0

    def params(self, f, dxf, dyf, dxxf, dxyf, dyyf):
        """
        Change values of parameters for current apex

        Parameters
        ----------
        f: float
            value of f(x,y) for current apex
        dxf: float
            value of df(x,y)/dx for current apex
        dyf: float
            value of df(x,y)/dy for current apex
        dxxf: float
            value of d^2f(x,y)/dx^2 for current apex
        dxyf: float
            value of d^2f(x,y)/dxdy for current apex
        dyyf: float
            value of d^2f(x,y)/dy^2 for current apex
        """
        self.setF(f)
        self.setDxF(dxf)
        self.setDyF(dyf)
        self.setDxxF(dxxf)
        self.setDxyF(dxyf)
        self.setDyyF(dyyf)

    def setF(self, f):
        """
        Change value of f(x,y) for current apex

        Parameters
        ----------
        f: float
            value of f(x,y) for current apex
        """
        self.f = f

    def setDxF(self, dxf):
        """
        Change value of df(x,y)/dx for current apex

        Parameters
        ----------
        dxf: float
            value of df(x,y)/dx for current apex
        """
        self.dxf = dxf

    def setDyF(self, dyf):
        """
        Change value of df(x,y)/dy for current apex

        Parameters
        ----------
        dyf: float
            value of df(x,y)/dy for current apex
        """
        self.dyf = dyf

    def setDxxF(self, dxxf):
        """
        Change value of d^2f(x,y)/dx^2 for current apex

        Parameters
        ----------
        dxxf: float
            value of d^2f(x,y)/dx^2 for current apex
        """
        self.dxxf = dxxf

    def setDxyF(self, dxyf):
        """
        Change value of d^2f(x,y)/dxdy for current apex

        Parameters
        ----------
        dxyf: float
            value of d^2f(x,y)/dxdy for current apex
        """
        self.dxyf = dxyf

    def setDyyF(self, dyyf):
        """
        Change value of d^2f(x,y)/dy^2 for current apex

        Parameters
        ----------
        dyyf: float
            value of d^2f(x,y)/dy^2 for current apex
        """
        self.dyyf = dyyf

    def getParam(self, derivative):
        """
        Return parameter of apex depends on derivative

        Parameters
        ----------
        derivative: Derivative
            given derivative

        Return
        ------
        value: float
             parameter of apex
        """
        if derivative == Derivative(0, 0):
            return self.f
        elif derivative == Derivative(1, 0):
            return self.dxf
        elif derivative == Derivative(0, 1):
            return self.dyf
        elif derivative == Derivative(2, 0):
            return self.dxxf
        elif derivative == Derivative(1, 1):
            return self.dxyf
        elif derivative == Derivative(0, 2):
            return self.dyyf

    def distance(self, other):
        """
        Calculate distance to other apex

        Parameters
        ----------
        other: Apex
            other apex

        Return
        ------
        sqrt: float
            distance between apexes
        """
        return sympy.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __repr__(self):
        return "x: {0}, y: {1}, f: {2}, dxf: {3}, dyf: {4}, dxxf: {5}, dxyf: {6}, dyyf: {7}"\
            .format(self.x, self.y, self.f, self.dxf, self.dyf, self.dxxf, self.dxyf, self.dyyf)

    def __eq__(self, other):
        return super().__eq__(other)
