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

    def apexes(self):
        """
        Represent apexes of current triangle as list

        Return
        ------
        apexes: list
            list of apexes of triangle
        """
        return [self.apex1, self.apex2, self.apex3]

    def normals(self):
        """
        Represent normals of current triangle as list

        Return
        ------
        normals: list
            list of normals of triangle
        """
        return [self.norm12, self.norm13, self.norm23]

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
        apex = self.apexes()
        normal = self.normals()

        for k in range(3):
            if normal[k] == Normal(apex[i], apex[j]):
                return normal[k]

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.apex1 == other.apex1 and self.apex2 == other.apex2 and self.apex3 == other.apex3
