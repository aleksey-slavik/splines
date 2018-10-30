import sympy

"""
Represent point

@author iryna.tomanova
"""


class Point:

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

    def distance(self, other):
        """
        Calculate distance to other point

        Parameters
        ----------
        other: Point
            other point

        Return
        ------
        sqrt: float
            distance between points
        """
        return sympy.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __repr__(self):
        return "x: {0}, y: {1}".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
