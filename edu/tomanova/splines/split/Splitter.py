import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from edu.tomanova.splines.utils.DataHelper import *
from edu.tomanova.splines.plate.Triangle import Triangle


class Splitter:
    triangles: list

    def fromFile(self, directoryName, fileName):
        self.triangles = loadFromFile(directoryName, fileName)
        return self.triangles

    def plot(self, size=(12, 9)):
        figure(figsize=size)

        for i in range(len(self.triangles)):
            plt.plot(
                [self.triangles[i].x1, self.triangles[i].x2],
                [self.triangles[i].y1, self.triangles[i].y2],
                'k-')
            plt.plot(
                [self.triangles[i].x2, self.triangles[i].x3],
                [self.triangles[i].y2, self.triangles[i].y3],
                'k-')
            plt.plot(
                [self.triangles[i].x3, self.triangles[i].x1],
                [self.triangles[i].y3, self.triangles[i].y1],
                'k-')

        plt.show()


#splitter = Splitter()
#splitter.fromFile('square', 'triangulation(1)')
#splitter.plot()

