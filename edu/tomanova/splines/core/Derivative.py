"""
Consist data of derivative

@author: iryna.tomanova
"""


class Derivative:
    def __init__(self, dx, dy):
        """
        Setup initial data

        Parameters
        ----------
        dx: int
            value of partial derivative with respect to x
        dy: int
            value of partial derivative with respect to y
        """
        self.dx = dx
        self.dy = dy

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.dx == other.dx and self.dy == other.dy
