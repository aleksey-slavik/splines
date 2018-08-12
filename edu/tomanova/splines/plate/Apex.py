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

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y