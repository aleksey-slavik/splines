from edu.tomanova.splines.plate.Triangle import Triangle
from edu.tomanova.splines.split.Splitter import Splitter
from edu.tomanova.splines.plate.SquarePlate import SquarePlate


class SquareSplitter(Splitter):

    def splitToTriangles(self, plate, count):
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


pl = SquarePlate(-0.5, -0.5, 0.5, 0.5)
splitter = SquareSplitter()
splitter.splitToTriangles(pl, 3)
splitter.plot(size=(10, 10))
