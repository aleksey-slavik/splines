from edu.tomanova.splines.core.integrate.Point import Point
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
