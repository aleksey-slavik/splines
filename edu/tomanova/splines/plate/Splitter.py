import matplotlib.pyplot as plt
from edu.tomanova.splines.utils.DataHelper import loadFromFile


class Splitter:

    triangles: list

    def split(self, directoryName, fileName):
        self.triangles = loadFromFile(directoryName, fileName)
        return self.triangles

    def plot(self):
        for i in range(len(self.triangles)):
            plt.plot(
                [self.triangles[i][0][0], self.triangles[i][0][1]],
                [self.triangles[i][1][0], self.triangles[i][1][1]],
                'k-')
            plt.plot(
                [self.triangles[i][1][0], self.triangles[i][1][1]],
                [self.triangles[i][2][0], self.triangles[i][2][1]],
                'k-')
            plt.plot(
                [self.triangles[i][2][0], self.triangles[i][2][1]],
                [self.triangles[i][0][0], self.triangles[i][0][1]],
                'k-')
        plt.show()


splitter = Splitter()
splitter.split('square', 'triangulation(1)')

splitter.plot()
