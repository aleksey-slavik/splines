import sympy
"""
Represent point

@author: iryna.tomanova
"""


class Point:

    def __init__(self, x, y):
        """
        Setup initial data

        Parameters
        ----------
        x: float
            x coordinate of point
        y: float
            y coordinate of point
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