"""
Contains data of square plate

@author: iryna.tomanova
"""


class SquarePlate:

    def __init__(self, apex1, apex2):
        """
        Setup initial data

        Parameters
        ----------
        apex1: Apex
            left bottom apex
        apex1: Apex
            right top apex
        """
        self.apex1 = apex1
        self.apex2 = apex2

    def __repr__(self):
        return str(self.__dict__)
