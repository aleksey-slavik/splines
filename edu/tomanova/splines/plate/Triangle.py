import math

from edu.tomanova.splines.plate.Normal import Normal

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
        self.norm12 = Normal(apex1, apex2)
        self.norm13 = Normal(apex1, apex3)
        self.norm23 = Normal(apex2, apex3)
        self.apexes = [self.apex1, self.apex2, self.apex3]
        self.normals = [self.norm12, self.norm13, self.norm23]
        self.normalApexes = [[1, 2], [1, 3], [2, 3]]

    def getNormal(self, i, j):
        """
        Find normal by numbers of two apexes

        Parameters
        ----------
        i: int
            number of first apex
        j: int
            number of second apex

        Return
        ------
        normal: Normal
            normal of triangle between apexes
        """
        for k in range(3):
            if self.normals[k] == Normal(self.apexes[i], self.apexes[j]):
                return self.normals[k]

    def square(self):
        """
        Using Heron's formula calculate square of current triangle
        """
        a = self.apex1.distance(self.apex2)
        b = self.apex1.distance(self.apex3)
        c = self.apex2.distance(self.apex3)
        p = (a + b + c) / 2

        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    def minX(self):
        return min(self.apex1.x, self.apex2.x, self.apex3.x)

    def maxX(self):
        return max(self.apex1.x, self.apex2.x, self.apex3.x)

    def minY(self):
        return min(self.apex1.y, self.apex2.y, self.apex3.y)

    def maxY(self):
        return max(self.apex1.y, self.apex2.y, self.apex3.y)

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.apex1 == other.apex1 and self.apex2 == other.apex2 and self.apex3 == other.apex3
