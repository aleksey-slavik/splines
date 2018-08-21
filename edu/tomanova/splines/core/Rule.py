import sympy


class Rule:

    def __init__(self, triangles):
        self.triangles = triangles
        self.apexes = []
        self.normals = []
        self.count = 0

    def setParams(self):
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

    def appendParams(self):
        self.createApexList()
        self.createNormalList()
        self.appendApexParams()
        self.appendNormalParams()

    def appendApexParams(self):
        for i in range(len(self.apexes)):
            self.count += 1
            self.apexes[i].setF(sympy.symbols("p{0}".format(self.count)))
            self.count += 1
            self.apexes[i].setDxF(sympy.symbols("p{0}".format(self.count)))
            self.count += 1
            self.apexes[i].setDyF(sympy.symbols("p{0}".format(self.count)))
            self.count += 1
            self.apexes[i].setDxxF(sympy.symbols("p{0}".format(self.count)))
            self.count += 1
            self.apexes[i].setDxyF(sympy.symbols("p{0}".format(self.count)))
            self.count += 1
            self.apexes[i].setDyyF(sympy.symbols("p{0}".format(self.count)))

    def appendNormalParams(self):
        for i in range(len(self.normals)):
            self.count += 1
            self.normals[i].setDN(sympy.symbols("p{0}".format(self.count)))

    def createApexList(self):
        for i in range(len(self.triangles)):
            apex = self.triangles[i].apexes

            for j in range(3):
                if apex[j] not in self.apexes:
                    self.apexes.append(apex[j])

        return self.apexes

    def createNormalList(self):
        for i in range(len(self.triangles)):
            norm = self.triangles[i].normals

            for j in range(3):
                if norm[j] not in self.normals:
                    self.normals.append(norm[j])

        return self.normals
