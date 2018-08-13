"""
Consist data of apex

@author: iryna.tomanova
"""


class Apex:

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
        self.x = x
        self.y = y
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

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
