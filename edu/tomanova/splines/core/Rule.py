import sympy


class Rule:

    def __init__(self, triangles):
        self.triangles = triangles
        self.apexes = []
        self.normals = []
        self.count = 0

    def setParams(self, dxxfOnly=(), dxyfOnly=(), dyyfOnly=(), excludeApex=(), excludeNormal=()):
        for i in range(len(self.triangles)):
            self.triangles[i].apex1 = self.getApex(self.triangles[i].apex1)
            self.triangles[i].apex2 = self.getApex(self.triangles[i].apex2)
            self.triangles[i].apex3 = self.getApex(self.triangles[i].apex3)
            self.triangles[i].norm12 = self.getNorm(self.triangles[i].norm12)
            self.triangles[i].norm13 = self.getNorm(self.triangles[i].norm13)
            self.triangles[i].norm23 = self.getNorm(self.triangles[i].norm23)

    def getApex(self, apex):
        for i in self.apexes:
            if self.apexes[i] == apex:
                return self.apexes[i]

    def getNorm(self, norm):
        for i in self.normals:
            if self.normals[i] == norm:
                self.normals[i] = -self.normals[i]
                return self.normals[i]

    def appendParams(self, dxxfOnly=(), dxyfOnly=(), dyyfOnly=(), excludeApex=(), excludeNormal=()):
        self.appendApexes(dxxfOnly, dxyfOnly, dyyfOnly, excludeApex)
        self.createNormalList(excludeNormal)

    def appendApexDxxFOnly(self, apex):
        self.count += 1
        apex.setDxxF(sympy.symbols("p{0}".format(self.count)))
        self.apexes.append(apex)

    def appendApexDxyFOnly(self, apex):
        self.count += 1
        apex.setDxyF(sympy.symbols("p{0}".format(self.count)))
        self.apexes.append(apex)

    def appendApexDyyFOnly(self, apex):
        self.count += 1
        apex.setDyyF(sympy.symbols("p{0}".format(self.count)))
        self.apexes.append(apex)

    def appendApex(self, apex):
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
        self.count += 1
        normal.setDN(sympy.symbols("p{0}".format(self.count)))
        self.normals.append(normal)

    def appendApexes(self, dxxfOnly, dxyfOnly, dyyfOnly, excludeApex):
        for i in self.triangles:
            apex = self.triangles[i].apexes

            for j in range(3):
                if apex[j] in dxxfOnly:
                    self.appendApexDxxFOnly(apex[j])

                elif apex[j] in dxyfOnly:
                    self.appendApexDxyFOnly(apex[j])

                elif apex[j] in dyyfOnly:
                    self.appendApexDyyFOnly(apex[j])

                elif apex[j] in excludeApex:
                    self.appendApex(apex[j])

                else:
                    self.apexes.append(apex[j])


    def createNormalList(self, excludeNormal):
        for i in self.triangles:
            norm = self.triangles[i].normals

            for j in range(3):
                if norm[j] in excludeNormal:
                    self.appendNormal(norm[j])

                else:
                    self.normals.append(norm[j])
