from edu.tomanova.splines.plate.Apex import Apex
from edu.tomanova.splines.plate.Triangle import Triangle
from edu.tomanova.splines.split.Splitter import Splitter
from edu.tomanova.splines.plate.SquarePlate import SquarePlate

"""
Contains methods for split square areas

@author: iryna.tomanova
"""


class SquareSplitter(Splitter):

    def splitToTriangles(self, plate, count):
        """
        Create triangles for square areas

        Parameters
        ----------
        plate: SquarePlate
            square plate parameters
        count: int
            plate divides count

        Return
        ------
        triangles: list
            list of triangles
        """
        plates = self.splitToSquares(plate, count)
        triangles = []

        for i in range(len(plates)):
            triangles.append(
                Triangle(
                    Apex(plates[i].apex1.x,
                         plates[i].apex1.y),
                    Apex(plates[i].apex2.x,
                         plates[i].apex1.y),
                    Apex((plates[i].apex1.x + plates[i].apex2.x) / 2,
                         (plates[i].apex1.y + plates[i].apex2.y) / 2)))

            triangles.append(
                Triangle(
                    Apex(plates[i].apex2.x,
                         plates[i].apex1.y),
                    Apex(plates[i].apex2.x,
                         plates[i].apex2.y),
                    Apex((plates[i].apex1.x + plates[i].apex2.x) / 2,
                         (plates[i].apex1.y + plates[i].apex2.y) / 2)))

            triangles.append(
                Triangle(
                    Apex(plates[i].apex2.x,
                         plates[i].apex2.y),
                    Apex(plates[i].apex1.x,
                         plates[i].apex2.y),
                    Apex((plates[i].apex1.x + plates[i].apex2.x) / 2,
                         (plates[i].apex1.y + plates[i].apex2.y) / 2)))

            triangles.append(
                Triangle(
                    Apex(plates[i].apex1.x,
                         plates[i].apex2.y),
                    Apex(plates[i].apex1.x,
                         plates[i].apex1.y),
                    Apex((plates[i].apex1.x + plates[i].apex2.x) / 2,
                         (plates[i].apex1.y + plates[i].apex2.y) / 2)))

        self.triangles = triangles
        return self.triangles

    @staticmethod
    def splitToSquares(plate, count):
        """
        Split square plate

        Parameters
        ----------
        plate: SquarePlate
            square plate parameters
        count: int
            plate divides count

        Return
        ------
        squares: list
            list of square plates
        """
        squares = [plate]

        for k in range(count):
            new = []

            for i in range(len(squares)):
                new.append(
                    SquarePlate(
                        Apex(squares[i].apex1.x,
                             squares[i].apex1.y),
                        Apex((squares[i].apex1.x + squares[i].apex2.x) / 2,
                             (squares[i].apex1.y + squares[i].apex2.y) / 2)))

                new.append(
                    SquarePlate(
                        Apex((squares[i].apex1.x + squares[i].apex2.x) / 2,
                             squares[i].apex1.y),
                        Apex(squares[i].apex2.x,
                             (squares[i].apex1.y + squares[i].apex2.y) / 2)))

                new.append(
                    SquarePlate(
                        Apex((squares[i].apex1.x + squares[i].apex2.x) / 2,
                             (squares[i].apex1.y + squares[i].apex2.y) / 2),
                        Apex(squares[i].apex2.x,
                             squares[i].apex2.y)))

                new.append(
                    SquarePlate(
                        Apex(squares[i].apex1.x,
                             (squares[i].apex1.y + squares[i].apex2.y) / 2),
                        Apex((squares[i].apex1.x + squares[i].apex2.x) / 2,
                             squares[i].apex2.y)))

            squares = new

        return squares
