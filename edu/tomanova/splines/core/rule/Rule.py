import sympy

"""
Contains rules for set parameters for apexes and normals

@author: iryna.tomanova
"""


class Rule:

    def __init__(self, triangles, dxxfOnly=(), dxyfOnly=(), dyyfOnly=(), excludeApex=(), excludeNormal=()):
        """
        Setup initial data

        Parameters
        ----------
        triangles: list
            list of triangles
        dxxfOnly: list
            list of apexes for which must be only one parameter for d^2f/dx^2
        dxyfOnly: list
            list of apexes for which must be only one parameter for d^2f/dxdy
        dyyfOnly: list
            list of apexes for which must be only one parameter for d^2f/dy^2
        excludeApex: list
            list of apexes for which must be no parameters
        excludeNormal: list
            list of normals for which must be no parameters
        """
        self.triangles = triangles
        self.dxxfOnly = dxxfOnly
        self.dxyfOnly = dxyfOnly
        self.dyyfOnly = dyyfOnly
        self.excludeApex = excludeApex
        self.excludeNormal = excludeNormal
        self.apexes = []
        self.normals = []
        self.count = 0

    def setParams(self):
        """
        Set parameters for triangles
        """
        self.appendParams()

        for i in range(len(self.triangles)):
            self.triangles[i].apex1 = self.getApex(self.triangles[i].apex1)
            self.triangles[i].apex2 = self.getApex(self.triangles[i].apex2)
            self.triangles[i].apex3 = self.getApex(self.triangles[i].apex3)
            self.triangles[i].norm12 = self.getNorm(self.triangles[i].norm12)
            self.triangles[i].norm13 = self.getNorm(self.triangles[i].norm13)
            self.triangles[i].norm23 = self.getNorm(self.triangles[i].norm23)

    def appendParams(self):
        """
        Append parameters for apexes and normals
        """
        self.appendApexes()
        self.appendNormals()

    def appendApexDxxFOnly(self, apex):
        """
        Append parameter for d^2f/dx^2

        Parameters
        ----------
        apex: Apex
            apex for which must set parameter
        """
        self.count += 1
        apex.setDxxF(sympy.symbols("p{0}".format(self.count)))
        self.apexes.append(apex)

    def appendApexDxyFOnly(self, apex):
        """
        Append parameter for d^2f/dxdy

        Parameters
        ----------
        apex: Apex
            apex for which must set parameter
        """
        self.count += 1
        apex.setDxyF(sympy.symbols("p{0}".format(self.count)))
        self.apexes.append(apex)

    def appendApexDyyFOnly(self, apex):
        """
        Append parameter for d^2f/dy^2

        Parameters
        ----------
        apex: Apex
            apex for which must set parameter
        """
        self.count += 1
        apex.setDyyF(sympy.symbols("p{0}".format(self.count)))
        self.apexes.append(apex)

    def appendApex(self, apex):
        """
        Append all parameters for apex

        Parameters
        ----------
        apex: Apex
            apex for which must set parameters
        """
        self.count += 1
        apex.setF(sympy.symbols("p{0}".format(self.count)))

        self.count += 1
        apex.setDxF(sympy.symbols("p{0}".format(self.count)))

        self.count += 1
        apex.setDyF(sympy.symbols("p{0}".format(self.count)))

        self.count += 1
        apex.setDxxF(sympy.symbols("p{0}".format(self.count)))

        self.count += 1
        apex.setDxyF(sympy.symbols("p{0}".format(self.count)))

        self.count += 1
        apex.setDyyF(sympy.symbols("p{0}".format(self.count)))

        return self.apexes.append(apex)

    def appendNormal(self, normal):
        """
        Append parameter for dn

        Parameters
        ----------
        normal: Normal
            normal for which must set parameter
        """
        self.count += 1
        normal.setDN(sympy.symbols("p{0}".format(self.count)))
        self.normals.append(normal)

    def appendApexes(self):
        """
        Append parameters for apexes
        """
        for triangle in self.triangles:
            apexes = triangle.apexes

            for j in range(3):
                if apexes[j] in self.apexes:
                    continue

                elif apexes[j] in self.dxxfOnly:
                    self.appendApexDxxFOnly(apexes[j])

                elif apexes[j] in self.dxyfOnly:
                    self.appendApexDxyFOnly(apexes[j])

                elif apexes[j] in self.dyyfOnly:
                    self.appendApexDyyFOnly(apexes[j])

                elif apexes[j] in self.excludeApex:
                    self.apexes.append(apexes[j])

                else:
                    self.appendApex(apexes[j])

    def appendNormals(self):
        """
        Append parameters for normals
        """
        for normal in self.triangles:
            normals = normal.normals

            for j in range(3):
                if normals[j] in self.normals:
                    continue

                elif normals[j] in self.excludeNormal:
                    self.normals.append(normals[j])

                else:
                    self.appendNormal(normals[j])

    def getApex(self, apex):
        """
        Find given apex in list of apexes

        Parameters
        ----------
        apex: Apex
            given apex

        Return
        ------
        apex: Apex
            apex from list
        """
        for i in range(len(self.apexes)):
            if self.apexes[i] == apex:
                return self.apexes[i]

    def getNorm(self, norm):
        """
        Find given normal in list of normals

        Parameters
        ----------
        norm: Normal
            given normal

        Return
        ------
        norm: Normal
            normal from list
        """
        for i in range(len(self.normals)):
            if self.normals[i] == norm:
                self.normals[i].setDN = -self.normals[i].dn
                return self.normals[i]
