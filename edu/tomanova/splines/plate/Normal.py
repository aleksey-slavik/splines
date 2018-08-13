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

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.point == other.point
