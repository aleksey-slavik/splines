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
                    plates[i].x1,
                    plates[i].y1,
                    plates[i].x2,
                    plates[i].y1,
                    (plates[i].x1 + plates[i].x2) / 2,
                    (plates[i].y1 + plates[i].y2) / 2))

            triangles.append(
                Triangle(
                    plates[i].x2,
                    plates[i].y1,
                    plates[i].x2,
                    plates[i].y2,
                    (plates[i].x1 + plates[i].x2) / 2,
                    (plates[i].y1 + plates[i].y2) / 2))

            triangles.append(
                Triangle(
                    plates[i].x2,
                    plates[i].y2,
                    plates[i].x1,
                    plates[i].y2,
                    (plates[i].x1 + plates[i].x2) / 2,
                    (plates[i].y1 + plates[i].y2) / 2))

            triangles.append(
                Triangle(
                    plates[i].x1,
                    plates[i].y2,
                    plates[i].x1,
                    plates[i].y1,
                    (plates[i].x1 + plates[i].x2) / 2,
                    (plates[i].y1 + plates[i].y2) / 2))

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
                        squares[i].x1,
                        squares[i].y1,
                        (squares[i].x1 + squares[i].x2) / 2,
                        (squares[i].y1 + squares[i].y2) / 2))

                new.append(
                    SquarePlate(
                        (squares[i].x1 + squares[i].x2) / 2,
                        squares[i].y1,
                        squares[i].x2,
                        (squares[i].y1 + squares[i].y2) / 2))

                new.append(
                    SquarePlate(
                        (squares[i].x1 + squares[i].x2) / 2,
                        (squares[i].y1 + squares[i].y2) / 2,
                        squares[i].x2,
                        squares[i].y2))

                new.append(
                    SquarePlate(
                        squares[i].x1,
                        (squares[i].y1 + squares[i].y2) / 2,
                        (squares[i].x1 + squares[i].x2) / 2,
                        squares[i].y2))

            squares = new

        return squares
