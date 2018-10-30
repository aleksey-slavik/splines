from edu.tomanova.splines.core.rule.Rule import Rule
from tomanova.splines.core.plate.Apex import Apex
"""
Implementation of Rule.
Contains rules for set parameters for apexes and normals for square plate

@author: iryna.tomanova
"""


class SquarePlateRule(Rule):

    def __init__(self, plate, triangles):
        """
        Setup initial data

        Parameters
        ----------
        plate: SquarePlate
            square plate
        triangles: list
            list of triangles
        """
        super().__init__(triangles)

        self.corners = [
            Apex(plate.apex1.x, plate.apex1.y),
            Apex(plate.apex1.x, plate.apex2.y),
            Apex(plate.apex2.x, plate.apex2.y),
            Apex(plate.apex2.x, plate.apex1.y)]

        self.verticalBorders = [
            plate.apex1.x,
            plate.apex2.x]

        self.horizontalBorders = [
            plate.apex1.y,
            plate.apex2.y]

    def appendApexes(self):
        """
        Append parameters for apexes
        """
        for triangle in self.triangles:
            apexes = triangle.apexes

            for j in range(3):
                if apexes[j] in self.apexes:
                    continue

                elif apexes[j] in self.corners:
                    self.appendApexDxyFOnly(apexes[j])

                elif apexes[j].x in self.verticalBorders:
                    self.appendApexDxxFOnly(apexes[j])

                elif apexes[j].y in self.horizontalBorders:
                    self.appendApexDyyFOnly(apexes[j])

                else:
                    self.appendApex(apexes[j])

    def appendNormals(self):
        """
        Append parameters for normals
        """
        for triangle in self.triangles:
            normals = triangle.normals

            for j in range(3):
                if normals[j] in self.normals:
                    continue

                elif normals[j].point.x in self.verticalBorders or normals[j].point.y in self.horizontalBorders:
                    self.normals.append(normals[j])

                else:
                    self.appendNormal(normals[j])
