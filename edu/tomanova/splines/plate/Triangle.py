"""
Consist data of triangle

@author: iryna.tomanova
"""


class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        """
        Setup initial data

        Parameters
        ----------
        x1: int
            x coordinate of first axis
        y1: int
            y coordinate of first axis
        x2: int
            x coordinate of second axis
        y2: int
            y coordinate of second axis
        x3: int
            x coordinate of third axis
        y3: int
            y coordinate of third axis
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def __repr__(self):
        return str(self.__dict__)
