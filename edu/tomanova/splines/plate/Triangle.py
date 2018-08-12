"""
Consist data of triangle

@author: iryna.tomanova
"""


class Triangle:

    def __init__(self, apex1, apex2, apex3):
        """
        Setup initial data

        Parameters
        ----------
        apex1: Apex
            first apex data
        apex2: Apex
            second apex data
        apex3: Apex
            third apex data
        """
        self.apex1 = apex1
        self.apex2 = apex2
        self.apex3 = apex3

    def __repr__(self):
        return str(self.__dict__)
