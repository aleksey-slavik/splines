"""
Contains data of square plate

@author: iryna.tomanova
"""


class SquarePlate:

    def __init__(self, x1, y1, x2, y2):
        """
        Setup initial data

        Parameters
        ----------
        x1: float
            left border
        y1: float
            bottom border
        x2: float
            right border
        y2: float
            top border
        """
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
